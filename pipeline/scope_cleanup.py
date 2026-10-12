from __future__ import annotations

import argparse
import csv
import json
import sqlite3
from datetime import date
from pathlib import Path

from content_ops import apply_authoritative_internal_links, authoritative_internal_links, build_internal_links
from core import load_json, now_iso, render_post
from topic_scope import CLASSIFIER_VERSION, classify_keyword


ROOT = Path(__file__).resolve().parents[1]


def find_post(slug: str) -> Path | None:
    matches = [
        path for path in (ROOT / "_posts").glob("*.md")
        if path.name[11:-3] == slug
    ]
    if len(matches) > 1:
        raise RuntimeError(f"multiple posts found for slug {slug}")
    return matches[0] if matches else None


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    fields = ["job_id", "keyword", "slug", "title", "action", "reason_codes", "post_path"]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({**row, "reason_codes": "|".join(row["reason_codes"])})


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit or apply strict-direct article cleanup")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "pipeline/state/outputs/strict-direct-v1-articles")
    args = parser.parse_args()

    config = load_json(ROOT / "pipeline/config.json")
    brands = config["program"].get("excluded_brand_terms", [])
    args.output_dir.mkdir(parents=True, exist_ok=True)
    database = ROOT / "pipeline/state/content-pipeline.db"
    connection = sqlite3.connect(database)
    connection.row_factory = sqlite3.Row
    rows = connection.execute(
        """SELECT j.*,k.keyword,k.intent FROM content_jobs j
           JOIN keywords k ON k.keyword_id=j.keyword_id
           WHERE j.status='published' ORDER BY j.slug"""
    ).fetchall()

    groups: dict[str, list[dict[str, object]]] = {
        "retain": [], "hold": [], "reject": [], "source_gap": [],
    }
    retained_jobs: list[dict[str, object]] = []
    for row in rows:
        decision = classify_keyword(row["keyword"], brands, row["intent"])
        pack = json.loads(row["source_pack_json"] or "{}")
        uncovered = list((pack.get("coverage") or {}).get("uncovered_terms") or [])
        if decision.decision == "hold":
            action, reasons = "hold", list(decision.reason_codes)
        elif decision.decision == "reject":
            action, reasons = "reject", list(decision.reason_codes)
        elif uncovered:
            action, reasons = "source_gap", ["uncovered_terms:" + ",".join(uncovered)]
        else:
            action, reasons = "retain", []
            plan = json.loads(row["plan_json"] or "{}")
            retained_jobs.append({
                "job_id": row["job_id"], "title": row["title"], "category": row["category"],
                "owned_question": row["owned_question"], "primary_keyword": row["keyword"],
                "page_type": plan.get("page_type"),
            })
        post = find_post(row["slug"])
        groups[action].append({
            "job_id": row["job_id"], "keyword": row["keyword"], "slug": row["slug"],
            "title": row["title"], "action": action, "reason_codes": reasons,
            "post_path": str(post.relative_to(ROOT)) if post else "",
        })

    for name, items in groups.items():
        write_csv(args.output_dir / f"articles-{name}.csv", items)

    if args.apply:
        now = now_iso()
        with connection:
            # Remove all old derived clusters. Accepted keywords will be
            # embedded into the versioned Qdrant collection and reclustered.
            connection.execute("UPDATE keywords SET cluster_id=NULL")
            connection.execute("DELETE FROM clusters")
            for action, status in (
                ("hold", "quarantined_topic_scope"),
                ("reject", "retracted_topic_scope"),
                ("source_gap", "blocked_missing_sources"),
            ):
                connection.executemany(
                    "UPDATE content_jobs SET status=?,published_url=NULL,updated_at=? WHERE job_id=?",
                    [(status, now, item["job_id"]) for item in groups[action]],
                )
            # Apply the same production gate to every historical or queued
            # job, not only pages that happened to be published today.
            connection.execute(
                """UPDATE content_jobs SET status='quarantined_topic_scope',published_url=NULL,updated_at=?
                   WHERE keyword_id IN (
                     SELECT keyword_id FROM keyword_scope_decisions
                     WHERE classifier_version=? AND decision='hold'
                   )""",
                (now, CLASSIFIER_VERSION),
            )
            connection.execute(
                """UPDATE content_jobs SET status='retracted_topic_scope',published_url=NULL,updated_at=?
                   WHERE keyword_id IN (
                     SELECT keyword_id FROM keyword_scope_decisions
                     WHERE classifier_version=? AND decision='reject'
                   )""",
                (now, CLASSIFIER_VERSION),
            )
            connection.execute("DELETE FROM internal_links")
            links = build_internal_links(
                retained_jobs,
                config["program"]["internal_links_min"],
                config["program"]["internal_links_max"],
            )
            for link in links:
                connection.execute(
                    "INSERT INTO internal_links(source_job_id,target_job_id,relation,anchor_text,status) VALUES(?,?,?,?,?)",
                    tuple(link[key] for key in ("source_job_id", "target_job_id", "relation", "anchor_text", "status")),
                )

            for item in retained_jobs:
                row = connection.execute("SELECT article_json,slug FROM content_jobs WHERE job_id=?", (item["job_id"],)).fetchone()
                article = json.loads(row["article_json"])
                article = apply_authoritative_internal_links(
                    article, authoritative_internal_links(connection, item["job_id"])
                )
                connection.execute(
                    "UPDATE content_jobs SET article_json=?,updated_at=? WHERE job_id=?",
                    (json.dumps(article, ensure_ascii=False, sort_keys=True, separators=(",", ":")), now, item["job_id"]),
                )
                post = find_post(row["slug"])
                publish_date = date.fromisoformat(post.name[:10]) if post else date.today()
                destination = post or ROOT / "_posts" / f"{publish_date.isoformat()}-{row['slug']}.md"
                destination.write_text(
                    render_post(article, publish_date, config["site"]["author"], config["site"]["timezone"]),
                    encoding="utf-8",
                )

        for action in ("hold", "reject", "source_gap"):
            for item in groups[action]:
                post = find_post(str(item["slug"]))
                if post:
                    post.unlink()

    summary = {
        "classifier_version": CLASSIFIER_VERSION,
        "applied": args.apply,
        "published_before": len(rows),
        "counts": {name: len(items) for name, items in groups.items()},
        "published_after": len(groups["retain"]),
        "output_dir": str(args.output_dir),
    }
    (args.output_dir / "articles-scope-summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
