#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import sys
from datetime import date
from pathlib import Path
from typing import Any

from batch import build_batch_requests, extract_response_json, schema_for_kind, write_batch
from core import (
    Paths,
    Store,
    canonical_json,
    load_json,
    load_jsonl,
    now_iso,
    read_skill_bundle,
    render_post,
    sha256_bytes,
    sha256_file,
)
from validators import (
    article_policy_errors,
    normalize_plan_metadata,
    plan_policy_errors,
    reconcile_review_deterministic_checks,
    source_pack_errors,
    validate_schema,
)
from credentials import effective_credentials
from operations import _review_custom_id, _review_payload, add_commands, dispatch
from content_ops import apply_authoritative_internal_links, assemble_article_draft, authoritative_internal_links, ingest_source_pack


def is_authoritative_article_request(connection: sqlite3.Connection, request_row: sqlite3.Row) -> bool:
    """Allow only the newest article lineage to change a content job."""
    if not request_row["job_id"]:
        return False
    latest = connection.execute(
        """SELECT custom_id FROM batch_requests
           WHERE job_id=? AND run_id=? AND kind='article'
           ORDER BY created_at DESC,custom_id DESC LIMIT 1""",
        (request_row["job_id"], request_row["run_id"]),
    ).fetchone()
    if not latest:
        return False
    ancestor = request_row
    visited: set[str] = set()
    while ancestor["kind"] == "repair" and ancestor["parent_custom_id"]:
        parent_id = ancestor["parent_custom_id"]
        if parent_id in visited:
            return False
        visited.add(parent_id)
        parent = connection.execute(
            "SELECT * FROM batch_requests WHERE custom_id=?",
            (parent_id,),
        ).fetchone()
        if parent is None:
            return False
        ancestor = parent
    return ancestor["kind"] == "article" and ancestor["custom_id"] == latest["custom_id"]


def is_authoritative_review_request(connection: sqlite3.Connection, request_row: sqlite3.Row) -> bool:
    """Bind a semantic review response to the exact current article payload."""
    if not request_row["job_id"]:
        return False
    job = connection.execute(
        "SELECT * FROM content_jobs WHERE job_id=?",
        (request_row["job_id"],),
    ).fetchone()
    if not job or not job["article_json"] or not job["plan_json"] or not job["source_pack_json"]:
        return False
    payload = _review_payload(connection, job)
    expected = _review_custom_id(
        request_row["run_id"], job["job_id"], job["article_json"], payload
    )
    return request_row["custom_id"] == expected


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description="MicroSwitchGuide content pipeline")
    root.add_argument("--project-root", type=Path, default=Path(__file__).resolve().parents[1])
    commands = root.add_subparsers(dest="command", required=True)

    commands.add_parser("init", help="create the local SQLite state database")
    commands.add_parser("status", help="show local pipeline counts and recorded costs")
    commands.add_parser("audit", help="check local readiness without paid API calls")
    add_commands(commands)

    create_run = commands.add_parser("create-run", help="create a traceable pipeline run")
    create_run.add_argument("--stage", default="initialized")

    import_keywords = commands.add_parser("import-keywords", help="idempotently import keyword CSV or JSONL")
    import_keywords.add_argument("input", type=Path)

    record_cost = commands.add_parser("record-cost", help="record provider cost with a hard budget gate")
    record_cost.add_argument("--run-id", required=True)
    record_cost.add_argument("--provider", required=True)
    record_cost.add_argument("--operation", required=True)
    record_cost.add_argument("--amount", required=True, type=float)
    record_cost.add_argument("--request-id")
    record_cost.add_argument("--units", type=int)

    build_batch = commands.add_parser("build-batch", help="build OpenAI Batch JSONL without submitting it")
    build_batch.add_argument("--kind", choices=["plan", "article", "review", "repair"], required=True)
    build_batch.add_argument("--run-id", required=True)
    build_batch.add_argument("--input", type=Path, required=True)
    build_batch.add_argument("--output", type=Path, required=True)
    build_batch.add_argument("--model")
    build_batch.add_argument("--max-output-tokens", type=int)

    ingest = commands.add_parser("ingest-batch", help="parse and reconcile a downloaded Batch output JSONL")
    ingest.add_argument("--input", type=Path, required=True)
    ingest.add_argument("--output", type=Path)

    validate = commands.add_parser("validate-article", help="validate article JSON and editorial policy")
    validate.add_argument("input", type=Path)

    render = commands.add_parser("render", help="render validated article JSON into a Jekyll post")
    render.add_argument("input", type=Path)
    render.add_argument("--date", default=date.today().isoformat())
    render.add_argument("--output", type=Path)

    return root


def context(project_root: Path) -> tuple[Paths, dict[str, Any], Store, str, str]:
    project_root = project_root.resolve()
    paths = Paths(project_root)
    config_path = paths.pipeline / "config.json"
    config = load_json(config_path)
    skill_root = Path(config["skill"]["root"])
    skill_text, skill_hash = read_skill_bundle(skill_root)
    config_hash = sha256_file(config_path)
    return paths, config, Store(paths), skill_text, skill_hash + ":" + config_hash


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    paths, config, store, skill_text, combined_hash = context(args.project_root)
    skill_hash, config_hash = combined_hash.split(":", 1)

    if args.command == "init":
        store.initialize()
        source_schema = load_json(Path(config["skill"]["root"]) / "references" / "source-pack.schema.json")
        for source_pack in sorted((paths.pipeline / "sources").glob("*.json")):
            ingest_source_pack(store, load_json(source_pack), source_schema)
        print(canonical_json({"status": "initialized", "database": str(paths.db)}))
        return 0
    if args.command == "status":
        print(json.dumps(store.summary(), ensure_ascii=False, indent=2))
        return 0
    if args.command == "audit":
        return audit(paths, config, store, skill_hash, config_hash)
    if args.command == "create-run":
        store.initialize()
        run_id = store.create_run(config_hash, skill_hash, args.stage)
        print(run_id)
        return 0
    if args.command == "import-keywords":
        store.initialize()
        inserted, duplicates = store.import_keywords(
            args.input,
            config["site"]["location_code"],
            config["site"]["language"],
        )
        print(canonical_json({"inserted": inserted, "duplicates": duplicates}))
        return 0
    if args.command == "record-cost":
        hard_limit = None
        if args.provider.casefold() == "dataforseo":
            hard_limit = config["budgets_usd"]["dataforseo_run_hard_limit"]
        total = store.record_cost(
            args.run_id,
            args.provider,
            args.operation,
            args.amount,
            hard_limit,
            args.request_id,
            args.units,
        )
        print(canonical_json({"provider": args.provider, "run_total_usd": round(total, 6)}))
        return 0
    if args.command == "build-batch":
        store.initialize()
        store.ensure_run(args.run_id)
        inputs = load_jsonl(args.input)
        kind = "article" if args.kind == "repair" else args.kind
        schema = load_json(paths.pipeline / "schemas" / "article-draft.schema.json") if args.kind == "article" else schema_for_kind(paths.pipeline, kind)
        model = args.model or config["models"]["generation"]
        max_tokens = args.max_output_tokens or (4500 if args.kind == "article" else (1500 if kind == "review" else 2500))
        rows = build_batch_requests(args.kind, inputs, model, skill_text, schema, max_tokens)
        result = write_batch(args.output, rows)
        now = now_iso()
        with store.connect() as connection:
            inputs_by_id = {item.get("custom_id") or f"msg-{args.kind}-{index:06d}": item for index, item in enumerate(inputs, 1)}
            for row in rows:
                input_hash = sha256_bytes(canonical_json(row).encode("utf-8"))
                existing = connection.execute("SELECT input_sha256 FROM batch_requests WHERE custom_id=?", (row["custom_id"],)).fetchone()
                if existing and existing["input_sha256"] != input_hash:
                    raise ValueError(f"custom_id already exists with different input: {row['custom_id']}")
                source = inputs_by_id.get(row["custom_id"], {})
                job_id = source.get("job_id") or (source.get("payload") or {}).get("job_id")
                connection.execute(
                    """
                    INSERT INTO batch_requests(custom_id,run_id,kind,job_id,endpoint,model,input_sha256,status,created_at,updated_at)
                    VALUES(?,?,?,?,?,?,?,?,?,?)
                    ON CONFLICT(custom_id) DO UPDATE SET
                      updated_at=excluded.updated_at
                    """,
                    (row["custom_id"], args.run_id, args.kind, job_id, "/v1/responses", model, input_hash, "prepared", now, now),
                )
        result.update({"run_id": args.run_id, "kind": args.kind, "model": model, "skill_hash": skill_hash})
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    if args.command == "ingest-batch":
        store.initialize()
        parsed_rows = []
        failures = 0
        for line in load_jsonl(args.input):
            custom_id, output, error = extract_response_json(line)
            request_row = None
            with store.connect() as connection:
                request_row = connection.execute("SELECT * FROM batch_requests WHERE custom_id=?", (custom_id,)).fetchone()
            if request_row is None:
                raise ValueError(f"output custom_id was not prepared locally: {custom_id}")
            validation_errors = []
            embedded_review_result = None
            if output is not None:
                effective_kind = request_row["kind"]
                ancestor = request_row
                while effective_kind == "repair" and ancestor["parent_custom_id"]:
                    parent_kind = None
                    if ancestor["parent_custom_id"]:
                        with store.connect() as connection:
                            parent = connection.execute("SELECT * FROM batch_requests WHERE custom_id=?", (ancestor["parent_custom_id"],)).fetchone()
                        parent_kind = parent["kind"] if parent else None
                    effective_kind = parent_kind or ("article" if "body_markdown" in output else ("review" if "checks" in output else "plan"))
                    if parent is None:
                        break
                    ancestor = parent
                schema = schema_for_kind(paths.pipeline, effective_kind)
                if effective_kind == "plan":
                    output = normalize_plan_metadata(output)
                if effective_kind == "article" and request_row["job_id"]:
                    with store.connect() as connection:
                        links = authoritative_internal_links(connection, request_row["job_id"])
                        job = connection.execute(
                            "SELECT source_pack_json,plan_json FROM content_jobs WHERE job_id=?",
                            (request_row["job_id"],),
                        ).fetchone()
                    compact_article = any(version in custom_id for version in ("-v10-", "-v11-")) and set(output) == {"body_markdown", "used_claim_ids", "self_review"}
                    if compact_article:
                        draft_schema = load_json(paths.pipeline / "schemas" / "article-draft.schema.json")
                        validation_errors.extend(validate_schema(output, draft_schema))
                        self_review = output.get("self_review") or {}
                        embedded_review_result = dict(self_review)
                        failed_checks = sorted(key for key, value in self_review.items() if value is not True)
                        if failed_checks:
                            validation_errors.append(f"embedded self-review failed: {failed_checks}")
                        if not job or not job["plan_json"] or not job["source_pack_json"]:
                            validation_errors.append("article job lacks approved plan or source pack")
                        if not validation_errors:
                            output = assemble_article_draft(
                                output,
                                json.loads(job["plan_json"]),
                                json.loads(job["source_pack_json"]),
                                links,
                            )
                    else:
                        output = apply_authoritative_internal_links(output, links)
                if not validation_errors:
                    validation_errors.extend(validate_schema(output, schema))
                if effective_kind == "plan" and not validation_errors:
                    validation_errors.extend(plan_policy_errors(output, config))
                    if request_row["job_id"] and output.get("content_signature"):
                        with store.connect() as connection:
                            duplicate = connection.execute(
                                """SELECT job_id FROM content_jobs
                                   WHERE job_id<>? AND plan_json IS NOT NULL
                                     AND json_extract(plan_json,'$.content_signature')=?
                                   LIMIT 1""",
                                (request_row["job_id"], output["content_signature"]),
                            ).fetchone()
                        if duplicate:
                            validation_errors.append(
                                f"duplicate content_signature already owned by {duplicate['job_id']}"
                            )
                if effective_kind == "article" and not validation_errors:
                    validation_errors.extend(article_policy_errors(output, config))
                    if request_row["job_id"]:
                        with store.connect() as connection:
                            job = connection.execute("SELECT source_pack_json,plan_json FROM content_jobs WHERE job_id=?", (request_row["job_id"],)).fetchone()
                        if not job or not job["source_pack_json"]:
                            validation_errors.append("article job has no attached source pack")
                        else:
                            validation_errors.extend(source_pack_errors(output, json.loads(job["source_pack_json"])))
                if validation_errors:
                    error = {"code": "validation_failed", "errors": validation_errors}
                    output = None
            status = "completed" if output is not None else "failed"
            failures += int(error is not None)
            usage = ((line.get("response") or {}).get("body") or {}).get("usage") or {}
            with store.connect() as connection:
                cursor = connection.execute(
                    "UPDATE batch_requests SET status=?,response_json=?,error_json=?,usage_json=?,updated_at=? WHERE custom_id=?",
                    (
                        status,
                        canonical_json(output) if output is not None else None,
                        canonical_json(error) if error is not None else None,
                        canonical_json(usage),
                        now_iso(),
                        custom_id,
                    ),
                )
                if (
                    output is None
                    and request_row["kind"] == "repair"
                    and request_row["job_id"]
                    and request_row["retry_count"] >= config["batch"]["content_revision_retries"]
                ):
                    connection.execute(
                        """UPDATE content_jobs
                           SET status='retry_exhausted',validation_json=?,updated_at=?
                           WHERE job_id=? AND status NOT IN ('validated','rendered','published')""",
                        (canonical_json(error or {"code": "repair_failed"}), now_iso(), request_row["job_id"]),
                    )
                if output is not None and request_row["job_id"]:
                    if effective_kind == "plan":
                        # A retry and a replacement batch can finish out of
                        # order. The first valid plan is authoritative; a late
                        # duplicate remains auditable on batch_requests but
                        # must not overwrite a plan that may already have a
                        # source pack or downstream article work attached.
                        connection.execute("UPDATE content_jobs SET status='planned',plan_json=?,title=?,slug=?,category=?,owned_question=?,updated_at=? WHERE job_id=? AND plan_json IS NULL", (canonical_json(output), output.get("title"), output.get("slug"), output.get("category"), output.get("owned_question"), now_iso(), request_row["job_id"]))
                    elif effective_kind == "article":
                        authoritative = is_authoritative_article_request(connection, request_row)
                        current_job = connection.execute(
                            "SELECT status FROM content_jobs WHERE job_id=?",
                            (request_row["job_id"],),
                        ).fetchone()
                        may_replace = authoritative and current_job and current_job["status"] not in {"rendered", "published"}
                        if may_replace:
                            connection.execute(
                                "DELETE FROM semantic_reviews WHERE job_id=?",
                                (request_row["job_id"],),
                            )
                        if may_replace and request_row["kind"] == "repair":
                            if any(version in custom_id for version in ("-v10-", "-v11-")) and embedded_review_result:
                                validation_json = canonical_json({
                                    "gate": "embedded_self_review_v1",
                                    "passed": True,
                                    "checks": embedded_review_result,
                                    "revision": 1,
                                })
                                connection.execute(
                                    "UPDATE content_jobs SET status='validated',article_json=?,title=?,slug=?,category=?,owned_question=?,validation_json=?,updated_at=? WHERE job_id=?",
                                    (
                                        canonical_json(output), output.get("title"), output.get("slug"), output.get("category"),
                                        output.get("owned_question"), validation_json, now_iso(), request_row["job_id"],
                                    ),
                                )
                            else:
                                revised_plan_json = None
                                if job and job["plan_json"]:
                                    revised_plan = json.loads(job["plan_json"])
                                    for field in ("title", "h1", "description", "slug", "category", "owned_question"):
                                        revised_plan[field] = output.get(field)
                                    revised_plan["angle"] = output.get("owned_question")
                                    headings = re.findall(r"^##\s+(.+)$", output.get("body_markdown", ""), re.MULTILINE)
                                    revised_plan["section_roles"] = [f"repaired_section_{index}" for index, _ in enumerate(headings, 1)]
                                    revised_plan["outline"] = [
                                        {
                                            "h2": heading,
                                            "purpose": "Answer this bounded section using only the attached source pack.",
                                            "section_role": revised_plan["section_roles"][index],
                                            "points": ["Preserve the accepted evidence scope and state unresolved fields explicitly."],
                                        }
                                        for index, heading in enumerate(headings)
                                    ]
                                    revised_plan["internal_link_targets"] = [
                                        link.get("target_job_id")
                                        for link in output.get("internal_links", [])
                                        if link.get("target_job_id")
                                    ]
                                    revised_plan_json = canonical_json(revised_plan)
                                connection.execute("UPDATE content_jobs SET status='awaiting_semantic_review',article_json=?,plan_json=COALESCE(?,plan_json),title=?,slug=?,category=?,owned_question=?,validation_json='{}',updated_at=? WHERE job_id=?", (canonical_json(output), revised_plan_json, output.get("title"), output.get("slug"), output.get("category"), output.get("owned_question"), now_iso(), request_row["job_id"]))
                        elif may_replace:
                            embedded_review = any(version in custom_id for version in ("-v10-", "-v11-"))
                            validation_json = canonical_json({
                                "gate": "embedded_self_review_v1",
                                "passed": True,
                                "checks": embedded_review_result,
                            }) if embedded_review else "{}"
                            connection.execute(
                                "UPDATE content_jobs SET status=?,article_json=?,title=?,slug=?,category=?,owned_question=?,validation_json=?,updated_at=? WHERE job_id=?",
                                (
                                    "validated" if embedded_review else "awaiting_semantic_review",
                                    canonical_json(output), output.get("title"), output.get("slug"), output.get("category"),
                                    output.get("owned_question"), validation_json, now_iso(), request_row["job_id"],
                                ),
                            )
                    else:
                        job = connection.execute(
                            "SELECT * FROM content_jobs WHERE job_id=?",
                            (request_row["job_id"],),
                        ).fetchone()
                        if job and job["article_json"]:
                            output = reconcile_review_deterministic_checks(
                                output, json.loads(job["article_json"]), config
                            )
                        if is_authoritative_review_request(connection, request_row):
                            passed = bool(output.get("passed"))
                            connection.execute("INSERT INTO semantic_reviews(job_id,custom_id,passed,review_json,created_at,updated_at) VALUES(?,?,?,?,?,?) ON CONFLICT(job_id) DO UPDATE SET custom_id=excluded.custom_id,passed=excluded.passed,review_json=excluded.review_json,updated_at=excluded.updated_at", (request_row["job_id"], custom_id, int(passed), canonical_json(output), now_iso(), now_iso()))
                            connection.execute(
                                "UPDATE content_jobs SET status=?,validation_json=?,updated_at=? WHERE job_id=? AND status NOT IN ('rendered','published')",
                                ("validated" if passed else "semantic_review_failed", canonical_json(output), now_iso(), request_row["job_id"]),
                            )
            if usage and request_row["model"] == "gpt-6-luna":
                rates = config["pricing_usd_per_million_tokens"]["gpt-6-luna_batch"]
                details = usage.get("input_tokens_details") or {}
                input_tokens = int(usage.get("input_tokens") or 0)
                cached_tokens = int(details.get("cached_tokens") or 0)
                cache_write_tokens = int(details.get("cache_write_tokens") or details.get("cache_creation_tokens") or 0)
                output_tokens = int(usage.get("output_tokens") or 0)
                uncached_tokens = max(0, input_tokens - cached_tokens - cache_write_tokens)
                estimated_cost = (uncached_tokens * rates["input"] + cached_tokens * rates["cached_input"] + cache_write_tokens * rates["cache_write"] + output_tokens * rates["output"]) / 1_000_000
                store.record_cost(request_row["run_id"], "openai", f"batch_{request_row['kind']}", estimated_cost, None, custom_id, input_tokens + output_tokens, {"pricing": "gpt-6-luna_batch", "usage": usage})
            parsed_rows.append({"custom_id": custom_id, "status": status, "output": output, "error": error})
        destination = args.output or paths.outputs / f"ingested-{datetime_stamp()}.jsonl"
        from core import write_jsonl

        write_jsonl(destination, parsed_rows)
        print(canonical_json({"rows": len(parsed_rows), "failures": failures, "output": str(destination)}))
        return 1 if failures else 0
    if args.command == "validate-article":
        return validate_article_file(args.input, paths, config)
    if args.command == "render":
        errors = validate_article_file(args.input, paths, config, quiet=True)
        if errors:
            return 1
        article = load_json(args.input)
        publish_date = date.fromisoformat(args.date)
        destination = args.output or paths.root / "_posts" / f"{publish_date.isoformat()}-{article['slug']}.md"
        if destination.exists():
            print(f"refusing to overwrite existing post: {destination}", file=sys.stderr)
            return 1
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(
            render_post(article, publish_date, config["site"]["author"], config["site"]["timezone"]),
            encoding="utf-8",
        )
        print(destination)
        return 0
    result = dispatch(args, paths, config, store, skill_text, skill_hash)
    if result is not None:
        return result
    raise AssertionError(args.command)


def validate_article_file(path: Path, paths: Paths, config: dict[str, Any], quiet: bool = False) -> int:
    article = load_json(path)
    schema = load_json(paths.pipeline / "schemas" / "article.schema.json")
    errors = validate_schema(article, schema)
    if not errors:
        errors.extend(article_policy_errors(article, config))
    if not quiet:
        print(json.dumps({"valid": not errors, "errors": errors}, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


def audit(paths: Paths, config: dict[str, Any], store: Store, skill_hash: str, config_hash: str) -> int:
    checks = []

    def add(name: str, ok: bool, detail: str) -> None:
        checks.append({"name": name, "ok": ok, "detail": detail})

    required = [
        paths.pipeline / "schema.sql",
        paths.pipeline / "schemas" / "article-plan.schema.json",
        paths.pipeline / "schemas" / "article.schema.json",
        paths.root / "_drafts" / "article-template.md",
        paths.root / "bin" / "site",
    ]
    for path in required:
        add(f"file:{path.relative_to(paths.root)}", path.is_file(), "present" if path.is_file() else "missing")
    try:
        store.initialize()
        with store.connect() as connection:
            connection.execute("PRAGMA integrity_check").fetchone()
            source_count = connection.execute("SELECT COUNT(*) FROM sources").fetchone()[0]
            claim_count = connection.execute("SELECT COUNT(*) FROM claims WHERE status='accepted'").fetchone()[0]
            unsupported_accepted = connection.execute(
                """SELECT COUNT(DISTINCT c.claim_id)
                   FROM claims c JOIN claim_sources cs ON cs.claim_id=c.claim_id
                   JOIN sources s ON s.source_id=cs.source_id
                   WHERE c.status='accepted'
                     AND s.source_type NOT IN ('standard','regulator','government','intergovernmental','academic','encyclopedia',
                                               'manufacturer','technical_guide','commercial_technical','patent')"""
            ).fetchone()[0]
        add("sqlite", True, str(paths.db))
        add("core_fact_library", source_count >= 3 and claim_count >= 4, f"sources={source_count}, accepted_claims={claim_count}")
        add("supported_source_types", unsupported_accepted == 0, f"unsupported_accepted_claims={unsupported_accepted}")
    except (sqlite3.Error, OSError) as exc:
        add("sqlite", False, str(exc))
    add("skill_hash", len(skill_hash) == 64, skill_hash)
    add("config_hash", len(config_hash) == 64, config_hash)

    layout = (paths.root / "_layouts" / "post.html").read_text(encoding="utf-8")
    add("zero_brand_layout", "official_url" not in layout and "ZINGEAR" not in layout, "no commercial insertion block")
    renderer = (paths.pipeline / "core.py").read_text(encoding="utf-8")
    add("external_links_nofollow", 'rel="nofollow noopener noreferrer"' in renderer, "renderer enforces nofollow")

    credential_names = ["DATAFORSEO_LOGIN", "DATAFORSEO_PASSWORD", "OPENAI_API_KEY", "QDRANT_URL", "QDRANT_API_KEY", "GITHUB_TOKEN"]
    credentials = effective_credentials(paths.state / "secrets.env")
    missing = [name for name in credential_names if not credentials.get(name)]
    add("runtime_credentials", not missing, "configured" if not missing else "missing env: " + ", ".join(missing))
    if config["models"].get("embedding_provider") == "local":
        try:
            from sentence_transformers import SentenceTransformer  # noqa: F401
            add("local_embedding_runtime", True, config["models"]["embedding"])
        except ImportError:
            add("local_embedding_runtime", False, "run ./bin/bootstrap-embeddings")

    result = {"ready": all(check["ok"] for check in checks), "checks": checks}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ready"] else 1


def datetime_stamp() -> str:
    return now_iso().replace(":", "").replace("-", "")


if __name__ == "__main__":
    raise SystemExit(main())
