from __future__ import annotations

import csv
import hashlib
import json
import re
import sqlite3
import unicodedata
import uuid
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urlparse


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def normalize_keyword(value: str) -> str:
    value = unicodedata.normalize("NFKC", value).casefold()
    value = value.replace("microswitch", "micro switch")
    value = re.sub(r"[‐‑‒–—−_]", "-", value)
    value = re.sub(r"\s*-\s*", "-", value)
    value = re.sub(r"\s+", " ", value).strip(" .,-")
    return value


def stable_id(prefix: str, value: str) -> str:
    return f"{prefix}_{sha256_bytes(value.encode('utf-8'))[:20]}"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{number}: invalid JSON: {exc}") from exc
        if not isinstance(value, dict):
            raise ValueError(f"{path}:{number}: each JSONL line must be an object")
        rows.append(value)
    return rows


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(canonical_json(row) + "\n")
            count += 1
    return count


def read_skill_bundle(skill_root: Path) -> tuple[str, str]:
    paths = [
        skill_root / "SKILL.md",
        skill_root / "references" / "seo-and-editorial-policy.md",
        skill_root / "references" / "fact-library-policy.md",
        skill_root / "references" / "source-pack.schema.json",
    ]
    missing = [str(path) for path in paths if not path.is_file()]
    if missing:
        raise FileNotFoundError("missing skill files: " + ", ".join(missing))
    parts = [path.read_text(encoding="utf-8") for path in paths]
    bundle = "\n\n".join(parts)
    return bundle, sha256_bytes(bundle.encode("utf-8"))


@dataclass(frozen=True)
class Paths:
    root: Path

    @property
    def pipeline(self) -> Path:
        return self.root / "pipeline"

    @property
    def state(self) -> Path:
        return self.pipeline / "state"

    @property
    def db(self) -> Path:
        return self.state / "content-pipeline.db"

    @property
    def outputs(self) -> Path:
        return self.state / "outputs"

    @property
    def posts(self) -> Path:
        return self.root / "_posts"


class Store:
    def __init__(self, paths: Paths):
        self.paths = paths

    @contextmanager
    def connect(self):
        self.paths.state.mkdir(parents=True, exist_ok=True)
        connection = sqlite3.connect(self.paths.db)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")
        try:
            with connection:
                yield connection
        finally:
            connection.close()

    def initialize(self) -> None:
        schema = (self.paths.pipeline / "schema.sql").read_text(encoding="utf-8")
        with self.connect() as connection:
            connection.executescript(schema)
            self._migrate(connection)

    def _migrate(self, connection: sqlite3.Connection) -> None:
        batch_sql_row = connection.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='batch_requests'").fetchone()
        if batch_sql_row and "'review'" not in (batch_sql_row[0] or ""):
            connection.execute("ALTER TABLE batch_requests RENAME TO batch_requests_legacy")
            connection.execute("""CREATE TABLE batch_requests (
              custom_id TEXT PRIMARY KEY, run_id TEXT NOT NULL REFERENCES runs(run_id),
              kind TEXT NOT NULL CHECK (kind IN ('plan','article','review','repair')),
              job_id TEXT REFERENCES content_jobs(job_id), endpoint TEXT NOT NULL, model TEXT NOT NULL,
              input_sha256 TEXT NOT NULL, batch_id TEXT, input_file_id TEXT, output_file_id TEXT,
              error_file_id TEXT, parent_custom_id TEXT, retry_count INTEGER NOT NULL DEFAULT 0,
              usage_json TEXT NOT NULL DEFAULT '{}', status TEXT NOT NULL, response_json TEXT,
              error_json TEXT, created_at TEXT NOT NULL, updated_at TEXT NOT NULL)""")
            legacy_columns = {row[1] for row in connection.execute("PRAGMA table_info(batch_requests_legacy)")}
            target_columns = [row[1] for row in connection.execute("PRAGMA table_info(batch_requests)")]
            common = [name for name in target_columns if name in legacy_columns]
            joined = ",".join(common)
            connection.execute(f"INSERT INTO batch_requests({joined}) SELECT {joined} FROM batch_requests_legacy")
            connection.execute("DROP TABLE batch_requests_legacy")
        additions = {
            "keywords": {
                "exclusion_reason": "TEXT",
                "serp_signature_json": "TEXT NOT NULL DEFAULT '[]'",
                "data_version": "TEXT",
            },
            "content_jobs": {
                "created_run_id": "TEXT REFERENCES runs(run_id)",
                "source_pack_json": "TEXT",
                "duplicate_of_job_id": "TEXT REFERENCES content_jobs(job_id)",
                "text_fingerprint": "TEXT",
                "semantic_score": "REAL",
            },
            "batch_requests": {
                "job_id": "TEXT REFERENCES content_jobs(job_id)",
                "input_file_id": "TEXT", "output_file_id": "TEXT", "error_file_id": "TEXT",
                "parent_custom_id": "TEXT", "retry_count": "INTEGER NOT NULL DEFAULT 0",
                "usage_json": "TEXT NOT NULL DEFAULT '{}'",
            },
        }
        for table, columns in additions.items():
            existing = {row[1] for row in connection.execute(f"PRAGMA table_info({table})")}
            for name, declaration in columns.items():
                if name not in existing:
                    connection.execute(f"ALTER TABLE {table} ADD COLUMN {name} {declaration}")
        connection.execute("CREATE INDEX IF NOT EXISTS idx_keywords_exclusion ON keywords(exclusion_reason)")
        connection.execute("CREATE INDEX IF NOT EXISTS idx_jobs_duplicate ON content_jobs(duplicate_of_job_id)")
        connection.execute("CREATE INDEX IF NOT EXISTS idx_batch_status ON batch_requests(status)")

    def create_run(self, config_hash: str, skill_hash: str, stage: str = "initialized") -> str:
        run_id = f"run_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}_{uuid.uuid4().hex[:8]}"
        now = now_iso()
        with self.connect() as connection:
            connection.execute(
                "INSERT INTO runs(run_id,created_at,updated_at,stage,status,config_hash,skill_hash) VALUES(?,?,?,?,?,?,?)",
                (run_id, now, now, stage, "running", config_hash, skill_hash),
            )
        return run_id

    def ensure_run(self, run_id: str) -> None:
        with self.connect() as connection:
            row = connection.execute("SELECT run_id FROM runs WHERE run_id = ?", (run_id,)).fetchone()
        if not row:
            raise ValueError(f"unknown run_id: {run_id}")

    def record_cost(
        self,
        run_id: str,
        provider: str,
        operation: str,
        amount_usd: float,
        hard_limit: float | None,
        request_id: str | None = None,
        units: int | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> float:
        self.ensure_run(run_id)
        with self.connect() as connection:
            spent = connection.execute(
                "SELECT COALESCE(SUM(amount_usd),0) FROM api_costs WHERE run_id=? AND provider=?",
                (run_id, provider),
            ).fetchone()[0]
            projected = float(spent) + float(amount_usd)
            if hard_limit is not None and projected > hard_limit + 1e-9:
                raise RuntimeError(
                    f"{provider} budget blocked: ${projected:.4f} would exceed ${hard_limit:.4f}"
                )
            cursor = connection.execute(
                "INSERT OR IGNORE INTO api_costs(run_id,provider,operation,request_id,amount_usd,units,recorded_at,metadata_json) VALUES(?,?,?,?,?,?,?,?)",
                (
                    run_id,
                    provider,
                    operation,
                    request_id,
                    float(amount_usd),
                    units,
                    now_iso(),
                    canonical_json(metadata or {}),
                ),
            )
            if cursor.rowcount == 0:
                projected = float(connection.execute(
                    "SELECT COALESCE(SUM(amount_usd),0) FROM api_costs WHERE run_id=? AND provider=?", (run_id, provider)
                ).fetchone()[0])
        return projected

    def import_keywords(self, path: Path, location_code: int, language_code: str) -> tuple[int, int]:
        if path.suffix.casefold() == ".jsonl":
            raw_rows = load_jsonl(path)
        elif path.suffix.casefold() == ".csv":
            with path.open(encoding="utf-8-sig", newline="") as handle:
                raw_rows = list(csv.DictReader(handle))
        else:
            raise ValueError("keyword input must be .csv or .jsonl")

        inserted = 0
        duplicates = 0
        now = now_iso()
        with self.connect() as connection:
            for row in raw_rows:
                keyword = str(row.get("keyword", "")).strip()
                if not keyword:
                    continue
                normalized = normalize_keyword(keyword)
                keyword_id = stable_id("kw", normalized)
                cursor = connection.execute(
                    """
                    INSERT OR IGNORE INTO keywords(
                      keyword_id,keyword,normalized_keyword,source_endpoint,location_code,language_code,
                      search_volume,cpc,competition,intent,trend_json,created_at,updated_at
                    ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)
                    """,
                    (
                        keyword_id,
                        keyword,
                        normalized,
                        row.get("source_endpoint"),
                        location_code,
                        language_code,
                        _int_or_none(row.get("search_volume")),
                        _float_or_none(row.get("cpc")),
                        row.get("competition"),
                        row.get("intent"),
                        canonical_json(row.get("trend", {})),
                        now,
                        now,
                    ),
                )
                if cursor.rowcount:
                    inserted += 1
                else:
                    duplicates += 1
        return inserted, duplicates

    def summary(self) -> dict[str, Any]:
        self.initialize()
        tables = ["runs", "keywords", "clusters", "content_jobs", "sources", "claims", "batch_requests"]
        with self.connect() as connection:
            counts = {table: connection.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0] for table in tables}
            costs = {
                row["provider"]: round(row["spent"], 6)
                for row in connection.execute(
                    "SELECT provider, SUM(amount_usd) AS spent FROM api_costs GROUP BY provider"
                ).fetchall()
            }
            jobs = {
                row["status"]: row["n"]
                for row in connection.execute(
                    "SELECT status, COUNT(*) AS n FROM content_jobs GROUP BY status"
                ).fetchall()
            }
        return {"database": str(self.paths.db), "counts": counts, "costs_usd": costs, "jobs_by_status": jobs}


def _int_or_none(value: Any) -> int | None:
    return None if value in (None, "") else int(float(value))


def _float_or_none(value: Any) -> float | None:
    return None if value in (None, "") else float(value)


def slugify(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii").casefold()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


_MARKDOWN_EXTERNAL_LINK = re.compile(
    r"(\[[^\]]+\]\((https?://[^)\s]+)\))(?!\{:\s*rel=)",
    re.IGNORECASE,
)


def nofollow_external_links(markdown: str) -> str:
    internal_hosts = {"microswitchguide.com", "www.microswitchguide.com"}

    def replace(match: re.Match[str]) -> str:
        if (urlparse(match.group(2)).hostname or "").casefold() in internal_hosts:
            return match.group(1)
        return f'{match.group(1)}{{: rel="nofollow noopener noreferrer" }}'

    return _MARKDOWN_EXTERNAL_LINK.sub(replace, markdown)


def render_post(article: dict[str, Any], publish_date: date, author: str, timezone_offset: str) -> str:
    tags = "\n".join(f"  - {tag}" for tag in article["tags"])
    body = article["body_markdown"].strip()
    # The post layout renders page.title as the sole H1. Older model outputs
    # sometimes begin with a second Markdown H1; do not render it twice.
    body = re.sub(r"\A#\s+[^\n]+\n+(?=\S)", "", body, count=1)
    sources = article.get("sources", [])
    if sources:
        source_lines = ["", "## Sources and references", ""]
        for source in sources:
            source_lines.append(f"- {source['publisher']}: [{source['title']}]({source['url']})")
        body += "\n" + "\n".join(source_lines)
    body = nofollow_external_links(body)
    return (
        "---\n"
        f"title: {yaml_string(article['title'])}\n"
        f"description: {yaml_string(article['description'])}\n"
        f"date: {publish_date.isoformat()} 00:00:00 {timezone_offset}\n"
        "publication_date_only: true\n"
        f"category: {article['category']}\n"
        "tags:\n"
        f"{tags}\n"
        f"author: {author}\n"
        "---\n\n"
        f"{body}\n"
    )


def sanitize_schema_for_strict(value: Any, *, property_map: bool = False) -> Any:
    unsupported = {"$schema", "title", "description", "minLength", "maxLength", "pattern", "format", "uniqueItems", "minItems", "maxItems"}
    if isinstance(value, dict):
        return {
            key: sanitize_schema_for_strict(item, property_map=(key == "properties"))
            for key, item in value.items()
            if property_map or key not in unsupported
        }
    if isinstance(value, list):
        return [sanitize_schema_for_strict(item) for item in value]
    return value
