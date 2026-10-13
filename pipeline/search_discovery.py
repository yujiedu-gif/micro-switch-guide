"""Post-deploy IndexNow notifications and Search Console BigQuery readout."""

from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import subprocess
import sys
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlparse
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
SITE = "https://www.microswitchguide.com"
INDEXNOW_ENDPOINT = "https://api.indexnow.org/indexnow"
KEY_RE = re.compile(r"^[A-Za-z0-9-]{8,128}$")
POST_RE = re.compile(r"^_posts/\d{4}-\d{2}-\d{2}-(.+)\.md$")
PROJECT_RE = re.compile(r"^[a-z][a-z0-9-]{4,28}[a-z0-9]$")
DATASET_RE = re.compile(r"^searchconsole[A-Za-z0-9_]*$")


def read_key(root: Path = ROOT) -> str:
    matches = [(p, p.stem) for p in root.glob("*.txt") if KEY_RE.fullmatch(p.stem)]
    matches = [(p, key) for p, key in matches if p.read_text(encoding="utf-8").strip() == key]
    if len(matches) != 1:
        raise ValueError("Expected exactly one root IndexNow key file; run indexnow-key-init")
    return matches[0][1]


def git_post_change_rows(before: str, after: str = "HEAD", root: Path = ROOT) -> dict[str, int]:
    for value in (before, after):
        if not re.fullmatch(r"[A-Za-z0-9_./^~-]{1,100}", value):
            raise ValueError("Invalid Git ref")
    result = subprocess.run(
        ["git", "diff", "--name-status", "--no-renames", before, after, "--", "_posts"],
        cwd=root, capture_output=True, text=True, check=True,
    )
    urls: dict[str, int] = {}
    for line in result.stdout.splitlines():
        fields = line.split("\t")
        if len(fields) != 2 or fields[0][:1] not in {"A", "M", "D"}:
            continue
        match = POST_RE.fullmatch(fields[1])
        if match:
            urls[f"{SITE}/guides/{match.group(1)}/"] = 404 if fields[0].startswith("D") else 200
    return dict(sorted(urls.items()))


def git_post_changes(before: str, after: str = "HEAD", root: Path = ROOT) -> list[str]:
    return list(git_post_change_rows(before, after, root))


def validate_urls(urls: list[str]) -> list[str]:
    host = urlparse(SITE).netloc
    validated = []
    for url in dict.fromkeys(urls):
        parsed = urlparse(url)
        if parsed.scheme != "https" or parsed.netloc != host or not parsed.path.startswith("/guides/") or parsed.fragment:
            raise ValueError(f"URL is outside the article host or path: {url}")
        validated.append(url)
    return validated


def get_status(url: str, timeout: int = 15) -> tuple[int, str]:
    request = Request(url, headers={"User-Agent": "MicroSwitchGuide-IndexNow/1.0"})
    try:
        with urlopen(request, timeout=timeout) as response:
            return response.status, response.read(4096).decode("utf-8", errors="replace")
    except HTTPError as error:
        return error.code, ""


def wait_for_deploy(urls: dict[str, int], key: str, timeout: int) -> None:
    key_url = f"{SITE}/{key}.txt"
    deadline = time.monotonic() + timeout
    while True:
        code, content = get_status(key_url)
        key_ready = code == 200 and content.strip() == key
        pages_ready = key_ready and all(
            get_status(url)[0] in ({404, 410} if expected == 404 else {200})
            for url, expected in urls.items()
        )
        if pages_ready:
            return
        if time.monotonic() >= deadline:
            raise TimeoutError("Live IndexNow key or changed article URLs were not deployed in time")
        time.sleep(min(20, max(1, deadline - time.monotonic())))


def wait_for_pages_build(commit: str, token: str, timeout: int) -> None:
    if not re.fullmatch(r"[a-f0-9]{40}", commit) or not token:
        raise ValueError("A full commit SHA and GitHub token are required to wait for Pages")
    url = "https://api.github.com/repos/yujiedu-gif/micro-switch-guide/pages/builds/latest"
    deadline = time.monotonic() + timeout
    while True:
        request = Request(url, headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"})
        with urlopen(request, timeout=15) as response:
            build = json.load(response)
        if build.get("commit") == commit:
            if build.get("status") == "built":
                return
            if build.get("status") == "errored":
                raise RuntimeError("GitHub Pages build failed for the deployed commit")
        if time.monotonic() >= deadline:
            raise TimeoutError("GitHub Pages has not built the target commit")
        time.sleep(min(20, max(1, deadline - time.monotonic())))


def submit_indexnow(urls: list[str], key: str, endpoint: str = INDEXNOW_ENDPOINT) -> list[dict]:
    urls = validate_urls(urls)
    if not KEY_RE.fullmatch(key):
        raise ValueError("Invalid IndexNow key")
    results = []
    for start in range(0, len(urls), 10000):
        chunk = urls[start:start + 10000]
        payload = json.dumps({"host": urlparse(SITE).netloc, "key": key,
                              "keyLocation": f"{SITE}/{key}.txt", "urlList": chunk}).encode()
        request = Request(endpoint, data=payload, headers={"Content-Type": "application/json; charset=utf-8"}, method="POST")
        try:
            with urlopen(request, timeout=30) as response:
                code = response.status
        except HTTPError as error:
            code = error.code
        results.append({"count": len(chunk), "http_status": code, "accepted": code in {200, 202}})
        if code not in {200, 202}:
            raise RuntimeError(f"IndexNow returned HTTP {code} for {len(chunk)} URLs")
    return results


def bigquery_sql(project: str, dataset: str, site: str = SITE) -> str:
    if not PROJECT_RE.fullmatch(project) or not DATASET_RE.fullmatch(dataset):
        raise ValueError("Invalid Google Cloud project ID or Search Console dataset")
    # Search Console can emit several rows per URL/day; always aggregate metrics.
    return f"""SELECT url, SUM(clicks) AS clicks, SUM(impressions) AS impressions,
  SAFE_DIVIDE(SUM(sum_position), SUM(impressions)) + 1 AS average_position,
  MIN(data_date) AS first_seen_date, MAX(data_date) AS last_seen_date
FROM `{project}.{dataset}.searchdata_url_impression`
WHERE data_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY)
  AND site_url IN ('sc-domain:microswitchguide.com', '{site}/')
  AND search_type = 'web' AND STARTS_WITH(url, '{site}/guides/')
GROUP BY url
ORDER BY impressions DESC"""


def bigquery_readout(project: str, dataset: str, location: str) -> dict:
    try:
        import google.auth
        from google.auth.transport.requests import AuthorizedSession
    except ImportError as error:
        raise RuntimeError("Install google-auth and requests to query BigQuery") from error
    credentials, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/bigquery.readonly"])
    session = AuthorizedSession(credentials)
    url = f"https://bigquery.googleapis.com/bigquery/v2/projects/{project}/queries"
    response = session.post(url, json={"query": bigquery_sql(project, dataset), "useLegacySql": False, "maxResults": 10000,
                                       "location": location, "maximumBytesBilled": "1000000000"}, timeout=60)
    response.raise_for_status()
    body = response.json()
    reference = body.get("jobReference", {})
    rows = list(body.get("rows", []))
    for _ in range(120):
        if body.get("jobComplete") and not body.get("pageToken"):
            break
        job_id = reference.get("jobId")
        if not job_id:
            raise RuntimeError("BigQuery did not provide a job ID for pagination or polling")
        next_url = f"https://bigquery.googleapis.com/bigquery/v2/projects/{project}/queries/{quote(job_id, safe='')}"
        params = {"location": location, "maxResults": 10000, "timeoutMs": 30000}
        if body.get("pageToken"):
            params["pageToken"] = body["pageToken"]
        response = session.get(next_url, params=params, timeout=45)
        response.raise_for_status()
        body = response.json()
        rows.extend(body.get("rows", []))
    else:
        raise TimeoutError("BigQuery result polling exceeded the bounded wait")
    result = [[cell.get("v") for cell in row.get("f", [])] for row in rows]
    if any(len(row) != 6 for row in result):
        raise RuntimeError("Unexpected Search Console BigQuery query schema")
    return {"rows": len(rows), "total_rows": body.get("totalRows"),
            "project": project, "dataset": dataset, "location": location,
            "result": result}


def sync_bigquery_rows(database: Path, readout: dict) -> int:
    database.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(database) as connection:
        connection.execute("""CREATE TABLE IF NOT EXISTS search_console_url_performance (
            canonical_url TEXT PRIMARY KEY, clicks INTEGER NOT NULL, impressions INTEGER NOT NULL,
            average_position REAL, first_seen_date TEXT, last_seen_date TEXT,
            source_project TEXT NOT NULL, source_dataset TEXT NOT NULL, synced_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )""")
        connection.executemany("""INSERT INTO search_console_url_performance
            (canonical_url,clicks,impressions,average_position,first_seen_date,last_seen_date,source_project,source_dataset)
            VALUES (?,?,?,?,?,?,?,?) ON CONFLICT(canonical_url) DO UPDATE SET
            clicks=excluded.clicks, impressions=excluded.impressions,
            average_position=excluded.average_position, first_seen_date=excluded.first_seen_date,
            last_seen_date=excluded.last_seen_date, source_project=excluded.source_project,
            source_dataset=excluded.source_dataset, synced_at=CURRENT_TIMESTAMP""",
            [(row[0], int(row[1]), int(row[2]), float(row[3]) if row[3] is not None else None,
              row[4], row[5], readout["project"], readout["dataset"]) for row in readout["result"]])
        connection.execute("CREATE TEMP TABLE current_search_urls(canonical_url TEXT PRIMARY KEY)")
        connection.executemany("INSERT INTO current_search_urls VALUES (?)", [(row[0],) for row in readout["result"]])
        connection.execute("""DELETE FROM search_console_url_performance
            WHERE source_project=? AND source_dataset=?
              AND canonical_url NOT IN (SELECT canonical_url FROM current_search_urls)""",
                           (readout["project"], readout["dataset"]))
    return len(readout["result"])


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    key_init = sub.add_parser("indexnow-key-init", help="create a tracked root verification file")
    key_init.add_argument("--key", help="optional pre-existing key")
    notify = sub.add_parser("indexnow-submit", help="notify changed deployed posts")
    notify.add_argument("--before", required=True, help="Git commit before deployment")
    notify.add_argument("--after", default="HEAD")
    notify.add_argument("--wait-seconds", type=int, default=900)
    notify.add_argument("--wait-pages-build", action="store_true")
    notify.add_argument("--dry-run", action="store_true")
    bq = sub.add_parser("bigquery-check", help="query Search Console bulk export")
    bq.add_argument("--project", default=os.environ.get("MSG_BIGQUERY_PROJECT"))
    bq.add_argument("--dataset", default=os.environ.get("MSG_BIGQUERY_DATASET", "searchconsole"))
    bq.add_argument("--location", default=os.environ.get("MSG_BIGQUERY_LOCATION", "US"))
    bq.add_argument("--show-sql", action="store_true")
    sync = sub.add_parser("bigquery-sync", help="copy URL performance aggregates into pipeline SQLite")
    sync.add_argument("--project", default=os.environ.get("MSG_BIGQUERY_PROJECT"))
    sync.add_argument("--dataset", default=os.environ.get("MSG_BIGQUERY_DATASET", "searchconsole"))
    sync.add_argument("--location", default=os.environ.get("MSG_BIGQUERY_LOCATION", "US"))
    args = parser.parse_args(argv)
    try:
        if args.command == "indexnow-key-init":
            from secrets import token_hex
            key = args.key or token_hex(16)
            if not KEY_RE.fullmatch(key):
                raise ValueError("Invalid IndexNow key")
            path = ROOT / f"{key}.txt"
            if path.exists() and path.read_text(encoding="utf-8").strip() != key:
                raise ValueError("Key file exists with different content")
            path.write_text(key + "\n", encoding="utf-8")
            print(json.dumps({"key_file": path.name, "verification_url": f"{SITE}/{path.name}"}))
        elif args.command == "indexnow-submit":
            changes = git_post_change_rows(args.before, args.after)
            urls = list(changes)
            if args.dry_run:
                print(json.dumps({"count": len(urls), "urls": urls}))
            elif urls:
                key = read_key()
                if args.wait_pages_build:
                    wait_for_pages_build(args.after, os.environ.get("GITHUB_TOKEN", ""), args.wait_seconds)
                wait_for_deploy(changes, key, args.wait_seconds)
                print(json.dumps({"submitted": submit_indexnow(urls, key)}))
            else:
                print(json.dumps({"submitted": 0, "reason": "no changed posts"}))
        elif args.command in {"bigquery-check", "bigquery-sync"}:
            if not args.project:
                raise ValueError("Set MSG_BIGQUERY_PROJECT or provide --project")
            if args.command == "bigquery-check" and args.show_sql:
                print(bigquery_sql(args.project, args.dataset))
            else:
                readout = bigquery_readout(args.project, args.dataset, args.location)
                if args.command == "bigquery-sync":
                    count = sync_bigquery_rows(ROOT / "pipeline/state/content-pipeline.db", readout)
                    print(json.dumps({"synced": count, "project": args.project, "dataset": args.dataset}))
                else:
                    print(json.dumps({key: value for key, value in readout.items() if key != "result"}))
        return 0
    except (ValueError, RuntimeError, TimeoutError, URLError, subprocess.CalledProcessError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
