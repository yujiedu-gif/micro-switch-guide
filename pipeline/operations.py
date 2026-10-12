from __future__ import annotations

import argparse
import csv
import difflib
import json
import os
import re
import sqlite3
import subprocess
import tempfile
import time
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date
from pathlib import Path
from typing import Any

from batch import build_batch_requests, extract_response_json, schema_for_kind, write_batch
from content_ops import (
    apply_authoritative_internal_links,
    assemble_article_draft,
    authoritative_internal_links,
    build_internal_links,
    build_source_pack,
    cluster_vectors,
    cosine_similarity,
    exclusion_reason,
    ingest_source_pack,
    minhash_signature,
    minhash_similarity,
    missing_source_terms,
    report_for_run,
    serp_overlap,
    simhash,
)
from core import canonical_json, load_json, load_jsonl, normalize_keyword, now_iso, render_post, sha256_bytes, stable_id, write_jsonl
from credentials import REQUIRED, credential_status, effective_credentials, import_credentials
from providers import DataForSEOClient, GitHubClient, LocalEmbeddingClient, OpenAIClient, OpenRouterClient, ProviderError, QdrantClient
from validators import article_policy_errors, normalize_plan_metadata, source_pack_errors, validate_schema
from topic_scope import CLASSIFIER_VERSION, classify_keyword


REQUEST_VERSION = "v10"
REVIEW_GATE_VERSION = "logic-gate-v5-stable-advisory-context"
REVIEW_INSTRUCTION = (
    "Concentrate the hard review on logical consistency, parameter accuracy, definition accuracy, and zero-brand compliance. "
    "Verify every number, unit, state reference, rating condition, scope qualifier, and technical definition against the accepted source-pack claims. "
    "Treat reader-task alignment, H2 coverage, and ownership uniqueness as advisory because deterministic structure and duplicate systems enforce them separately. "
    "A statement that supplied evidence does not establish a fact is an allowed boundary, not an unsupported positive claim."
)


def _review_article(article: dict[str, Any]) -> dict[str, Any]:
    """Remove deterministic internal-link routing from model review identity.

    The logic reviewer audits prose, facts, parameters, and definitions. Link
    destinations are validated locally and may be reconciled after candidate
    selection without changing any factual sentence. Replacing the complete
    Markdown link (including its anchor) with a marker keeps that operation
    from creating another paid review request.
    """
    normalized = json.loads(canonical_json(article))
    body = str(normalized.get("body_markdown", ""))
    normalized["body_markdown"] = re.sub(
        r"\[[^\]]+\]\(/guides/[^)]+\)",
        "[internal reference]",
        body,
    )
    normalized.pop("internal_links", None)
    return normalized


def _review_plan(plan: dict[str, Any]) -> dict[str, Any]:
    normalized = json.loads(canonical_json(plan))
    normalized.pop("internal_link_targets", None)
    return normalized


def _review_payload(connection: sqlite3.Connection, row: Any) -> dict[str, Any]:
    return {
        "job_id": row["job_id"],
        "plan": _review_plan(json.loads(row["plan_json"])),
        "article": _review_article(json.loads(row["article_json"])),
        "source_pack": json.loads(row["source_pack_json"]),
        "nearby_owned_questions": [
            item[0]
            for item in connection.execute(
                """SELECT owned_question FROM content_jobs
                   WHERE created_run_id=? AND job_id<>? AND owned_question IS NOT NULL
                   ORDER BY job_id LIMIT 20""",
                (row["created_run_id"], row["job_id"]),
            )
        ],
        "review_instruction": REVIEW_INSTRUCTION,
    }


def _review_custom_id(run_id: str, job_id: str, article_json: str, payload: dict[str, Any]) -> str:
    # The normalized payload contains the complete review-relevant article.
    # Raw article_json is intentionally excluded because link routing is local.
    # Nearby ownership questions are advisory and can grow as future jobs are
    # planned, so they must not invalidate a completed factual review.
    identity_payload = json.loads(canonical_json(payload))
    identity_payload.pop("nearby_owned_questions", None)
    version_material = f"{run_id}:{job_id}:review:{REQUEST_VERSION}:{REVIEW_GATE_VERSION}"
    return f"msg-review-{REQUEST_VERSION}-{sha256_bytes((version_material + ':' + canonical_json(identity_payload)).encode())[:16]}"


def add_commands(commands: argparse._SubParsersAction) -> None:
    credentials = commands.add_parser("credentials", help="import or check local credential mappings")
    credentials.add_argument("action", choices=["check", "import"])
    credentials.add_argument("--source-dir", type=Path, default=Path("/Users/yujiedu/Desktop/未命名文件夹"))
    credentials.add_argument("--qdrant-url")

    smoke = commands.add_parser("providers-smoke-test", help="check provider credentials; --live performs network calls")
    smoke.add_argument("--live", action="store_true")

    discover = commands.add_parser("keywords-discover", help="discover keyword ideas through DataForSEO")
    discover.add_argument("--run-id", required=True)
    discover.add_argument("--limit", type=int, default=15_000)
    discover.add_argument("--seed", action="append", default=[], help="override configured seeds; repeat up to 20 times")

    discover_collect = commands.add_parser("keywords-discover-collect", help="collect a posted asynchronous keyword-discovery task")
    discover_collect.add_argument("--run-id", required=True)
    discover_collect.add_argument("--limit", type=int, default=15_000)

    enrich = commands.add_parser("keywords-enrich", help="add intent for selected candidates and sample organic SERPs")
    enrich.add_argument("--run-id", required=True)
    enrich.add_argument("--serp-sample", type=int, default=800)

    collect_serp = commands.add_parser("keywords-serp-collect", help="collect ready Standard SERP tasks without another charge")
    collect_serp.add_argument("--run-id", required=True)

    filtering = commands.add_parser("keywords-filter", help="apply commercial, brand, and relevance exclusions")
    filtering.add_argument("--brand", action="append", default=[])

    scope_audit = commands.add_parser("keywords-scope-audit", help="audit strict topic eligibility without changing SQLite")
    scope_audit.add_argument("--output-dir", type=Path, required=True)
    scope_audit.add_argument("--brand", action="append", default=[])
    scope_audit.add_argument("--samples-per-reason", type=int, default=10)

    scope_apply = commands.add_parser("keywords-scope-apply", help="apply a versioned strict topic decision to keyword eligibility")
    scope_apply.add_argument("--output-dir", type=Path, required=True)
    scope_apply.add_argument("--brand", action="append", default=[])

    jobs = commands.add_parser("jobs-create", help="create one idempotent article job per selected intent cluster")
    jobs.add_argument("--run-id", required=True)
    jobs.add_argument("--limit", type=int, default=10_000)
    jobs.add_argument("--keyword", action="append", default=[], help="create jobs only for these exact normalized keywords")
    jobs.add_argument("--keyword-file", type=Path, help="CSV/JSONL input whose keyword column limits job creation")
    jobs.add_argument("--new-only", action="store_true", help="skip intent clusters that already have a content job")

    requeue = commands.add_parser("jobs-requeue-articles", help="clear invalid drafts and requeue a bounded article candidate pool")
    requeue.add_argument("--run-id", required=True)
    requeue.add_argument("--limit", type=int, default=60)
    requeue.add_argument("--output", type=Path, help="backup JSONL; defaults to pipeline state outputs")

    export = commands.add_parser("jobs-export", help="export plan or article inputs from the job state machine")
    export.add_argument("--run-id", required=True)
    export.add_argument("--source-batch-id", help="export only jobs completed in this provider batch")
    export.add_argument("--kind", choices=["plan", "article", "review"], required=True)
    export.add_argument("--output", type=Path, required=True)
    export.add_argument("--limit", type=int, default=10_000)

    qinit = commands.add_parser("qdrant-init", help="verify embedding dimensions and create Qdrant collections")
    qinit.add_argument("--skip-embedding-check", action="store_true")
    qinit.add_argument("--provider", choices=["local", "openrouter"])

    embed = commands.add_parser("embed", help="embed JSONL objects and upsert them into Qdrant")
    embed.add_argument("--input", type=Path, required=True)
    embed.add_argument("--output", type=Path, required=True)
    embed.add_argument("--object-type", choices=["topic", "article_plan", "section_plan", "chunk"], required=True)
    embed.add_argument("--batch-size", type=int, default=64)
    embed.add_argument("--provider", choices=["local", "openrouter"])

    embedding_export = commands.add_parser("embedding-export", help="export canonical topic, plan, section, or article text for embedding")
    embedding_export.add_argument("--run-id", help="limit plan/section/chunk exports to one run")
    embedding_export.add_argument("--batch-id", help="limit plan/section/chunk exports to jobs in one provider batch")
    embedding_export.add_argument("--object-type", choices=["topic", "article_plan", "section_plan", "chunk"], required=True)
    embedding_export.add_argument("--granularity", choices=["article", "section"], default="article", help="for chunk exports, embed whole articles or individual H2 sections")
    embedding_export.add_argument("--output", type=Path, required=True)
    embedding_export.add_argument("--limit", type=int, default=10_000)
    embedding_export.add_argument("--only-unclustered", action="store_true", help="for topics, export only selected keywords without a cluster")
    embedding_export.add_argument("--status", action="append", help="for plans or chunks, export only jobs with this status")

    cluster = commands.add_parser("cluster", help="cluster embedded keyword JSONL and update SQLite")
    cluster.add_argument("--input", type=Path, required=True)
    cluster.add_argument("--threshold", type=float)
    cluster.add_argument("--local", action="store_true", help="use the quadratic local implementation only for small fixtures")
    cluster.add_argument("--incremental", action="store_true", help="attach new topics to existing Qdrant-backed clusters without moving locked topics")
    cluster.add_argument("--new-version", action="store_true", help="rebuild assignments into the configured versioned topic collection while preserving historical jobs")

    calibration = commands.add_parser("similarity-calibrate", help="import at least 200 labeled pairs and select the best cosine threshold")
    calibration.add_argument("--input", type=Path, required=True, help="JSONL with left_id, right_id, score, and label same/different")

    calibration_sample = commands.add_parser("similarity-calibration-sample", help="export a conservative deterministic calibration set without merging topics")
    calibration_sample.add_argument("--output", type=Path, required=True)
    calibration_sample.add_argument("--limit", type=int, default=200)

    similarity_review = commands.add_parser("similarity-review", help="label borderline topic pairs and apply safe same-intent merges")
    similarity_review.add_argument("--input", type=Path, required=True, help="JSONL with left_id, right_id, and label same/different")

    sources = commands.add_parser("sources", help="ingest or retrieve source packs")
    sources.add_argument("action", choices=["ingest", "build-pack", "quarantine-commercial"])
    sources.add_argument("--input", type=Path)
    sources.add_argument("--topic-id")
    sources.add_argument("--job-id")
    sources.add_argument("--term", action="append", default=[])
    sources.add_argument("--output", type=Path)

    source_packs = commands.add_parser("source-packs-build", help="build and attach source packs for planned jobs")
    source_packs.add_argument("--run-id", help="limit source-pack work to one run")
    source_packs.add_argument("--batch-id", help="limit work to successfully ingested plans from one provider batch")
    source_packs.add_argument("--limit", type=int, default=10_000)
    source_packs.add_argument("--force", action="store_true", help="rebuild and revalidate already attached source packs")

    render_run = commands.add_parser("render-run", help="render every validated job in a run without overwriting posts")
    render_run.add_argument("--run-id", required=True)
    render_run.add_argument("--date", default=date.today().isoformat())
    render_run.add_argument("--limit", type=int, default=10_000)

    submit = commands.add_parser("batch-submit", help="upload a prepared JSONL and create an OpenAI batch")
    submit.add_argument("--run-id", required=True)
    submit.add_argument("--input", type=Path, required=True)
    submit.add_argument("--kind", choices=["plan", "article", "review", "repair"], required=True)

    submit_dir = commands.add_parser("batch-submit-dir", help="submit every prepared Batch file in a manifest directory")
    submit_dir.add_argument("--run-id", required=True)
    submit_dir.add_argument("--input-dir", type=Path, required=True)
    submit_dir.add_argument("--kind", choices=["plan", "article", "review"], required=True)

    preflight = commands.add_parser("batch-preflight", help="run up to three synchronous schema and skill checks before Batch submission")
    preflight.add_argument("--run-id", required=True)
    preflight.add_argument("--kind", choices=["plan", "article", "review", "repair"], required=True)
    preflight.add_argument("--input", type=Path, required=True)
    preflight.add_argument("--output", type=Path, help="write Batch-compatible raw responses so successful preflight work can be ingested")

    batch_status = commands.add_parser("batch-status", help="refresh one OpenAI batch and download terminal outputs")
    batch_status.add_argument("--batch-id", required=True)

    retry = commands.add_parser("batch-retry", help="prepare only failed requests for an exact retry")
    retry.add_argument("--run-id", required=True)
    retry.add_argument("--input", type=Path, required=True, help="original request JSONL")
    retry.add_argument("--output", type=Path, required=True)

    semantic_repair = commands.add_parser("semantic-repair", help="prepare article repairs from failed adversarial reviews")
    semantic_repair.add_argument("--run-id", required=True)
    semantic_repair.add_argument("--input", type=Path, required=True, help="original prepared article request JSONL")
    semantic_repair.add_argument("--output", type=Path, required=True)

    local_repair = commands.add_parser(
        "article-local-repair",
        help="ingest a deterministic local article repair after full validation",
    )
    local_repair.add_argument("--run-id", required=True)
    local_repair.add_argument("--job-id", required=True)
    local_repair.add_argument("--input", type=Path, required=True)

    review_enforce = commands.add_parser("review-enforce", help="require a matching passed OpenAI semantic review and retract unapproved posts")
    review_enforce.add_argument("--run-id", required=True)
    review_enforce.add_argument("--retract", action="store_true", help="remove rendered files whose current article revision lacks a passed review")

    publication_select = commands.add_parser("publication-select", help="select an exact accepted publication set and retain excess reviewed articles as reserve")
    publication_select.add_argument("--run-id", required=True)
    publication_select.add_argument("--target", type=int, choices=[50, 250, 1000, 10000], required=True)

    build_batches = commands.add_parser("build-batches", help="split up to 10,000 jobs into cache-friendly Batch files")
    build_batches.add_argument("--run-id", required=True)
    build_batches.add_argument("--kind", choices=["plan", "article", "review"], required=True)
    build_batches.add_argument("--input", type=Path, required=True)
    build_batches.add_argument("--output-dir", type=Path, required=True)
    build_batches.add_argument("--chunk-size", type=int, default=500)
    build_batches.add_argument("--model")

    links = commands.add_parser("links-build", help="build an internal-link graph for eligible jobs")
    links.add_argument("--run-id", required=True)
    links.add_argument("--source-batch-id", help="build links only among jobs completed in this provider batch")
    links.add_argument("--limit", type=int, default=10_000)
    links.add_argument("--output", type=Path)

    reconcile_links = commands.add_parser("links-reconcile", help="replace article links whose targets are not in the accepted publication set")
    reconcile_links.add_argument("--run-id", required=True)
    reconcile_links.add_argument("--all-accepted", action="store_true", help="reconcile across every accepted run in the publication set")

    dedupe = commands.add_parser("dedupe", help="detect exact, MinHash, and SimHash near-duplicate articles")
    dedupe.add_argument("--input", type=Path, required=True)
    dedupe.add_argument("--output", type=Path)
    dedupe.add_argument("--apply", action="store_true")

    articles_export = commands.add_parser("articles-export", help="export generated article JSONL for duplicate audits")
    articles_export.add_argument("--run-id", help="limit the export to one run")
    articles_export.add_argument("--output", type=Path, required=True)
    articles_export.add_argument("--limit", type=int, default=10_000)
    articles_export.add_argument("--status", action="append", help="export only jobs with this status; repeat for multiple statuses")

    semantic_dedupe = commands.add_parser("dedupe-semantic", help="mark semantic duplicates from embedded article or section JSONL")
    semantic_dedupe.add_argument("--run-id", help="record an acceptance audit for one run")
    semantic_dedupe.add_argument("--object-type", choices=["chunk", "article_plan", "section_plan"], default="chunk")
    semantic_dedupe.add_argument("--input", type=Path, required=True)
    semantic_dedupe.add_argument("--output", type=Path, required=True)
    semantic_dedupe.add_argument("--threshold", type=float)
    semantic_dedupe.add_argument("--apply", action="store_true", help="apply duplicate_of to matching content jobs")

    report = commands.add_parser("report", help="write a run manifest and acceptance metrics")
    report.add_argument("--run-id", required=True)
    report.add_argument("--output", type=Path)

    benchmark = commands.add_parser("benchmark", help="benchmark 1k, 5k, and 10k local pipeline operations")
    benchmark.add_argument("--sizes", type=int, nargs="+", default=[1000, 5000, 10000])
    benchmark.add_argument("--output", type=Path)

    acceptance = commands.add_parser("acceptance-check", help="enforce rollout gates before increasing volume")
    acceptance.add_argument("--run-id", required=True)
    acceptance.add_argument("--target", type=int, choices=[50, 250, 1000, 10000], required=True)
    acceptance.add_argument("--build-site", action="store_true")

    publish = commands.add_parser("prepare-pr", help="build, commit a batch branch, push, and open a PR")
    publish.add_argument("--run-id", required=True)
    publish.add_argument("--title")
    publish.add_argument("--branch")
    publish.add_argument("--dry-run", action="store_true")


def dispatch(args: argparse.Namespace, paths: Any, config: dict[str, Any], store: Any, skill_text: str, skill_hash: str) -> int | None:
    secrets_path = paths.state / "secrets.env"
    if args.command == "credentials":
        status = import_credentials(args.source_dir, secrets_path) if args.action == "import" else credential_status(effective_credentials(secrets_path))
        if args.action == "import" and args.qdrant_url:
            values = effective_credentials(secrets_path)
            values["QDRANT_URL"] = args.qdrant_url.rstrip("/")
            from credentials import write_credentials
            write_credentials(secrets_path, values)
            status = credential_status(values)
        print(json.dumps({"path": str(secrets_path), "mode": _mode(secrets_path), "credentials": status}, indent=2))
        return 0 if all(status.get(name) == "configured" for name in REQUIRED) else 1
    if args.command == "providers-smoke-test":
        return provider_smoke_test(effective_credentials(secrets_path), config, args.live)
    if args.command == "keywords-discover":
        return keywords_discover(args, paths, config, store, effective_credentials(secrets_path))
    if args.command == "keywords-discover-collect":
        return keywords_discover_collect(args, paths, config, store, effective_credentials(secrets_path))
    if args.command == "keywords-enrich":
        return keywords_enrich(args, config, store, effective_credentials(secrets_path))
    if args.command == "keywords-serp-collect":
        return keywords_serp_collect(args, config, store, effective_credentials(secrets_path))
    if args.command == "keywords-filter":
        return keywords_filter(args, config, store)
    if args.command == "keywords-scope-audit":
        return keywords_scope_audit(args, config, store, apply=False)
    if args.command == "keywords-scope-apply":
        return keywords_scope_audit(args, config, store, apply=True)
    if args.command == "jobs-create":
        return jobs_create(args, config, store)
    if args.command == "jobs-requeue-articles":
        return jobs_requeue_articles(args, paths, store)
    if args.command == "jobs-export":
        return jobs_export(args, store)
    if args.command == "qdrant-init":
        return qdrant_init(args, config, effective_credentials(secrets_path))
    if args.command == "embed":
        return embed_objects(args, config, store, effective_credentials(secrets_path))
    if args.command == "embedding-export":
        return embedding_export(args, store)
    if args.command == "cluster":
        return cluster_keywords(args, config, store, effective_credentials(secrets_path))
    if args.command == "similarity-calibrate":
        return similarity_calibrate(args, config, store)
    if args.command == "similarity-calibration-sample":
        return similarity_calibration_sample(args, store)
    if args.command == "similarity-review":
        return similarity_review_apply(args, store)
    if args.command == "sources":
        return source_action(args, paths, config, store)
    if args.command == "source-packs-build":
        return source_packs_build(args, store)
    if args.command == "render-run":
        return render_run(args, paths, config, store)
    if args.command == "batch-submit":
        return batch_submit(args, store, effective_credentials(secrets_path))
    if args.command == "batch-submit-dir":
        return batch_submit_dir(args, store, effective_credentials(secrets_path))
    if args.command == "batch-preflight":
        return batch_preflight(args, paths, config, store, effective_credentials(secrets_path))
    if args.command == "batch-status":
        return batch_status(args, paths, store, effective_credentials(secrets_path))
    if args.command == "batch-retry":
        return batch_retry(args, config, store)
    if args.command == "semantic-repair":
        return semantic_repair_prepare(args, config, store)
    if args.command == "article-local-repair":
        return article_local_repair(args, paths, config, store)
    if args.command == "review-enforce":
        return review_enforce(args, paths, store)
    if args.command == "publication-select":
        return publication_select(args, store)
    if args.command == "build-batches":
        return build_batches_action(args, paths, config, store, skill_text, skill_hash)
    if args.command == "links-build":
        return links_build(args, paths, config, store)
    if args.command == "links-reconcile":
        return links_reconcile(args, config, store)
    if args.command == "dedupe":
        return dedupe_articles(args, paths, config, store)
    if args.command == "articles-export":
        return articles_export(args, store)
    if args.command == "dedupe-semantic":
        return dedupe_semantic(args, config, store, effective_credentials(secrets_path))
    if args.command == "report":
        return write_report(args, paths, store)
    if args.command == "benchmark":
        return benchmark_pipeline(args, paths)
    if args.command == "acceptance-check":
        return acceptance_check(args, paths, config, store)
    if args.command == "prepare-pr":
        return prepare_pr(args, paths, config, store, effective_credentials(secrets_path))
    return None


def article_local_repair(args: argparse.Namespace, paths: Any, config: dict[str, Any], store: Any) -> int:
    """Replace a draft revision without another generation call, but never bypass gates."""
    store.ensure_run(args.run_id)
    article = load_json(args.input)
    schema = load_json(paths.pipeline / "schemas" / "article.schema.json")
    with store.connect() as connection:
        job = connection.execute(
            """SELECT j.*,k.keyword,k.normalized_keyword
               FROM content_jobs j JOIN keywords k ON k.keyword_id=j.keyword_id
               WHERE j.job_id=?""",
            (args.job_id,),
        ).fetchone()
    if job is None:
        raise ValueError(f"unknown job_id: {args.job_id}")
    if job["created_run_id"] != args.run_id:
        raise ValueError(f"job {args.job_id} does not belong to run {args.run_id}")
    if job["status"] in {"rendered", "published"}:
        raise ValueError(f"cannot locally repair job in status {job['status']}")
    current = json.loads(job["article_json"]) if job["article_json"] else None
    expected_keyword = (current or {}).get("primary_keyword") or job["keyword"]
    if normalize_keyword(article.get("primary_keyword", "")) != normalize_keyword(expected_keyword):
        raise ValueError("local repair cannot change the primary keyword")
    errors = validate_schema(article, schema)
    if not errors:
        errors.extend(article_policy_errors(article, config))
    if not errors:
        if not job["source_pack_json"]:
            errors.append("article job has no attached source pack")
        else:
            errors.extend(source_pack_errors(article, json.loads(job["source_pack_json"])))
    if errors:
        print(canonical_json({"accepted": False, "errors": errors}))
        return 1

    revised_plan_json = job["plan_json"]
    if revised_plan_json:
        revised_plan = json.loads(revised_plan_json)
        for field in ("title", "h1", "description", "slug", "category", "owned_question"):
            revised_plan[field] = article.get(field)
        revised_plan["angle"] = article.get("owned_question")
        revised_plan["outline"] = [
            {
                "h2": heading,
                "purpose": "Answer this bounded section using only the attached source pack.",
                "points": ["Preserve the accepted evidence scope and state unresolved fields explicitly."],
            }
            for heading in re.findall(r"^##\s+(.+)$", article.get("body_markdown", ""), re.MULTILINE)
        ]
        revised_plan["internal_link_targets"] = [
            link.get("target_job_id")
            for link in article.get("internal_links", [])
            if link.get("target_job_id")
        ]
        revised_plan_json = canonical_json(revised_plan)

    previous_sha256 = sha256_bytes((job["article_json"] or "").encode()) if job["article_json"] else None
    article_json = canonical_json(article)
    article_sha256 = sha256_bytes(article_json.encode())
    provenance = canonical_json(
        {
            "local_repair": {
                "article_sha256": article_sha256,
                "previous_sha256": previous_sha256,
                "input": str(args.input),
                "created_at": now_iso(),
            }
        }
    )
    with store.connect() as connection:
        connection.execute(
            """UPDATE content_jobs
               SET status='awaiting_semantic_review',article_json=?,plan_json=?,title=?,slug=?,category=?,owned_question=?,validation_json=?,updated_at=?
               WHERE job_id=?""",
            (
                article_json,
                revised_plan_json,
                article.get("title"),
                article.get("slug"),
                article.get("category"),
                article.get("owned_question"),
                provenance,
                now_iso(),
                args.job_id,
            ),
        )
    print(
        canonical_json(
            {
                "accepted": True,
                "job_id": args.job_id,
                "previous_sha256": previous_sha256,
                "article_sha256": article_sha256,
                "status": "awaiting_semantic_review",
            }
        )
    )
    return 0


def provider_smoke_test(credentials: dict[str, str], config: dict[str, Any], live: bool) -> int:
    results: dict[str, Any] = {"credentials": credential_status(credentials), "live": live, "providers": {}}
    if not live:
        print(json.dumps(results, indent=2))
        return 0 if all(credentials.get(name) for name in REQUIRED) else 1
    checks = {
        "dataforseo": (("DATAFORSEO_LOGIN", "DATAFORSEO_PASSWORD"), lambda: DataForSEOClient(credentials["DATAFORSEO_LOGIN"], credentials["DATAFORSEO_PASSWORD"]).ping()),
        "openai": (("OPENAI_API_KEY",), lambda: OpenAIClient(credentials["OPENAI_API_KEY"]).list_models()),
        "qdrant": (("QDRANT_URL", "QDRANT_API_KEY"), lambda: QdrantClient(credentials["QDRANT_URL"], credentials["QDRANT_API_KEY"]).ping()),
        "local_embeddings": ((), lambda: LocalEmbeddingClient(config["models"]["embedding"]).embed(["micro switch"], "query")),
        "github": (("GITHUB_TOKEN",), lambda: GitHubClient(credentials["GITHUB_TOKEN"], config["github"]["owner"], config["github"]["repo"]).repository()),
    }
    failed = False
    for name, (required, callback) in checks.items():
        missing = [key for key in required if not credentials.get(key)]
        if missing:
            failed = True
            results["providers"][name] = {"ok": False, "detail": "missing credentials: " + ", ".join(missing)}
            continue
        try:
            result = callback()
            detail = f"dimension={len(result[0])}" if name == "local_embeddings" else "reachable"
            results["providers"][name] = {"ok": True, "detail": detail}
        except Exception as exc:
            failed = True
            results["providers"][name] = {"ok": False, "detail": str(exc)[:300]}
    print(json.dumps(results, indent=2))
    return 1 if failed else 0


def keywords_discover(args: argparse.Namespace, paths: Any, config: dict[str, Any], store: Any, credentials: dict[str, str]) -> int:
    store.ensure_run(args.run_id)
    if args.limit > 15_000:
        raise ValueError("initial discovery is capped at 15,000 candidates")
    seeds = args.seed or load_json(paths.pipeline / "seeds.json")["seeds"]
    seeds = list(dict.fromkeys(seed.strip() for seed in seeds if seed.strip()))
    if not 1 <= len(seeds) <= 20:
        raise ValueError("keyword discovery requires 1-20 unique seed keywords")
    _ensure_dataforseo_budget(store, args.run_id, config, config["budgets_usd"]["dataforseo_discovery_reserve"])
    client = DataForSEOClient(credentials["DATAFORSEO_LOGIN"], credentials["DATAFORSEO_PASSWORD"])
    local_id = args.run_id
    with store.connect() as connection:
        existing = connection.execute("SELECT remote_id,status FROM provider_objects WHERE provider='dataforseo' AND object_type='keyword_discovery' AND local_id=?", (local_id,)).fetchone()
    if existing and existing["remote_id"] and existing["status"] in {"posted", "complete"}:
        print(canonical_json({"run_id": args.run_id, "task_id": existing["remote_id"], "status": existing["status"], "idempotent": True}))
        return 0
    result = client.post_keywords_for_keywords_task(seeds, config["site"]["location_code"], config["site"]["language"])
    accepted = []
    for task in result.get("tasks", []):
        task_id = str(task.get("id") or "")
        if task.get("status_code") != 20100 or not task_id:
            continue
        accepted.append(task_id)
        cost = float(task.get("cost") or 0)
        if cost:
            store.record_cost(args.run_id, "dataforseo", "keywords_for_keywords_standard", cost, config["budgets_usd"]["dataforseo_run_hard_limit"], task_id, len(seeds))
    if len(accepted) != 1:
        raise RuntimeError(f"DataForSEO did not accept exactly one keyword discovery task: {accepted}")
    with store.connect() as connection:
        connection.execute("INSERT INTO provider_objects(provider,object_type,local_id,remote_id,status,payload_sha256,metadata_json,created_at,updated_at) VALUES('dataforseo','keyword_discovery',?,?, 'posted',?,?,?,?) ON CONFLICT(provider,object_type,local_id) DO UPDATE SET remote_id=excluded.remote_id,status='posted',payload_sha256=excluded.payload_sha256,metadata_json=excluded.metadata_json,updated_at=excluded.updated_at", (local_id, accepted[0], sha256_bytes(canonical_json(seeds).encode()), canonical_json({"run_id": args.run_id, "limit": args.limit, "seed_count": len(seeds)}), now_iso(), now_iso()))
    print(canonical_json({"run_id": args.run_id, "task_id": accepted[0], "status": "posted", "collect_command": f"keywords-discover-collect --run-id {args.run_id} --limit {args.limit}"}))
    return 0


def keywords_discover_collect(args: argparse.Namespace, paths: Any, config: dict[str, Any], store: Any, credentials: dict[str, str]) -> int:
    store.ensure_run(args.run_id)
    with store.connect() as connection:
        task = connection.execute("SELECT * FROM provider_objects WHERE provider='dataforseo' AND object_type='keyword_discovery' AND local_id=?", (args.run_id,)).fetchone()
    if not task or not task["remote_id"]:
        raise ValueError("no asynchronous keyword discovery task is registered for this run")
    response = DataForSEOClient(credentials["DATAFORSEO_LOGIN"], credentials["DATAFORSEO_PASSWORD"]).get_keywords_for_keywords_task(task["remote_id"])
    rows, pending, failed = [], False, []
    for remote in response.get("tasks", []):
        if remote.get("status_code") == 20000 and remote.get("result") is not None:
            for item in remote.get("result") or []:
                keyword = item.get("keyword")
                if keyword and len(rows) < args.limit:
                    rows.append({
                        "keyword": keyword, "source_endpoint": "keywords_data/google_ads/keywords_for_keywords/task_get",
                        "search_volume": item.get("search_volume"), "cpc": item.get("cpc"),
                        "competition": item.get("competition"), "intent": None,
                        "trend": item.get("monthly_searches") or {},
                    })
        elif remote.get("status_code") in {20100, 40601, 40602}:
            pending = True
        else:
            failed.append({"status_code": remote.get("status_code"), "status_message": remote.get("status_message")})
    if pending:
        print(canonical_json({"run_id": args.run_id, "task_id": task["remote_id"], "status": "pending"}))
        return 2
    if failed:
        print(canonical_json({"run_id": args.run_id, "task_id": task["remote_id"], "status": "failed", "errors": failed}))
        return 1
    output = paths.outputs / f"{args.run_id}-keywords.jsonl"
    write_jsonl(output, rows)
    inserted, duplicates = store.import_keywords(output, config["site"]["location_code"], config["site"]["language"])
    with store.connect() as connection:
        connection.execute("UPDATE provider_objects SET status='complete',payload_sha256=?,metadata_json=?,updated_at=? WHERE provider='dataforseo' AND object_type='keyword_discovery' AND local_id=?", (sha256_bytes(canonical_json(rows).encode()), canonical_json({"run_id": args.run_id, "received": len(rows), "inserted": inserted, "duplicates": duplicates}), now_iso(), args.run_id))
    print(canonical_json({"run_id": args.run_id, "status": "complete", "received": len(rows), "inserted": inserted, "duplicates": duplicates, "output": str(output)}))
    return 0


def keywords_enrich(args: argparse.Namespace, config: dict[str, Any], store: Any, credentials: dict[str, str]) -> int:
    store.ensure_run(args.run_id)
    reserve = config["budgets_usd"]["dataforseo_intent_reserve"] + config["budgets_usd"]["dataforseo_serp_reserve"]
    _ensure_dataforseo_budget(store, args.run_id, config, reserve)
    client = DataForSEOClient(credentials["DATAFORSEO_LOGIN"], credentials["DATAFORSEO_PASSWORD"])
    with store.connect() as connection:
        intent_rows = connection.execute("SELECT keyword_id,keyword FROM keywords WHERE selected=1 AND exclusion_reason IS NULL AND intent IS NULL ORDER BY COALESCE(search_volume,0) DESC").fetchall()
        serp_rows = connection.execute(
            """SELECT k.keyword_id,k.keyword FROM keywords k
               WHERE k.selected=1 AND k.exclusion_reason IS NULL
                 AND json_array_length(k.serp_signature_json)=0
                 AND NOT EXISTS (
                   SELECT 1 FROM provider_objects p
                   WHERE p.provider='dataforseo' AND p.object_type='serp'
                     AND p.local_id=k.keyword_id AND p.status='complete'
                 )
               ORDER BY COALESCE(k.search_volume,0) DESC"""
        ).fetchall()
    by_keyword = {row["keyword"].casefold(): row["keyword_id"] for row in intent_rows}
    intent_updates = 0
    for offset in range(0, len(intent_rows), 1000):
        chunk = [row["keyword"] for row in intent_rows[offset:offset + 1000]]
        response = client.search_intent(chunk)
        for task in response.get("tasks", []):
            cost = float(task.get("cost") or 0)
            if cost:
                store.record_cost(args.run_id, "dataforseo", "search_intent", cost, config["budgets_usd"]["dataforseo_run_hard_limit"], str(task.get("id")), len(chunk))
            for group in task.get("result") or []:
                for item in group.get("items") or []:
                    keyword_id = by_keyword.get(str(item.get("keyword", "")).casefold())
                    label = (item.get("keyword_intent") or {}).get("label")
                    if keyword_id and label:
                        with store.connect() as connection:
                            connection.execute("UPDATE keywords SET intent=?,updated_at=? WHERE keyword_id=?", (label, now_iso(), keyword_id))
                        intent_updates += 1
    sample = serp_rows[: max(0, min(args.serp_sample, len(serp_rows)))]
    posted = failures = 0
    for offset in range(0, len(sample), 100):
        chunk = sample[offset:offset + 100]
        response = client.post_organic_serp_tasks([(row["keyword_id"], row["keyword"]) for row in chunk], config["site"]["location_code"], config["site"]["language"], config["site"]["device"])
        for task in response.get("tasks", []):
            keyword_id = (task.get("data") or {}).get("tag")
            task_id = str(task.get("id") or "")
            if task.get("status_code") != 20100 or not keyword_id or not task_id:
                failures += 1
                continue
            cost = float(task.get("cost") or 0)
            if cost:
                store.record_cost(args.run_id, "dataforseo", "organic_serp_standard", cost, config["budgets_usd"]["dataforseo_run_hard_limit"], task_id, 1)
            with store.connect() as connection:
                connection.execute("INSERT INTO provider_objects(provider,object_type,local_id,remote_id,status,payload_sha256,metadata_json,created_at,updated_at) VALUES('dataforseo','serp',?,?,?,?,?,?,?) ON CONFLICT(provider,object_type,local_id) DO UPDATE SET remote_id=excluded.remote_id,status=excluded.status,metadata_json=excluded.metadata_json,updated_at=excluded.updated_at", (keyword_id, task_id, "posted", None, canonical_json({"run_id": args.run_id}), now_iso(), now_iso()))
            posted += 1
    print(canonical_json({"intent_updates": intent_updates, "serp_tasks_posted": posted, "serp_failures": failures, "collection_command": f"keywords-serp-collect --run-id {args.run_id}"}))
    return 0 if failures == 0 else 2


def keywords_serp_collect(args: argparse.Namespace, config: dict[str, Any], store: Any, credentials: dict[str, str]) -> int:
    store.ensure_run(args.run_id)
    client = DataForSEOClient(credentials["DATAFORSEO_LOGIN"], credentials["DATAFORSEO_PASSWORD"])
    with store.connect() as connection:
        tasks = connection.execute("SELECT * FROM provider_objects WHERE provider='dataforseo' AND object_type='serp' AND status='posted' AND json_extract(metadata_json,'$.run_id')=?", (args.run_id,)).fetchall()
    def fetch(task: Any) -> tuple[Any, dict[str, Any] | None]:
        try:
            return task, client.get_organic_serp_task(task["remote_id"])
        except ProviderError:
            return task, None

    collected = pending = failed = 0
    with ThreadPoolExecutor(max_workers=12) as executor:
        results = (future.result() for future in as_completed([executor.submit(fetch, task) for task in tasks]))
        for task, response in results:
            if response is None:
                pending += 1
                continue
            urls = []
            ready = False
            for remote in response.get("tasks", []):
                if remote.get("status_code") == 20000 and remote.get("result"):
                    ready = True
                    for group in remote.get("result") or []:
                        for item in group.get("items") or []:
                            if item.get("type") == "organic" and item.get("url"):
                                urls.append(item["url"])
                elif remote.get("status_code") not in {20100, 40601, 40602}:
                    failed += 1
            if not ready:
                pending += 1
                continue
            with store.connect() as connection:
                connection.execute("UPDATE keywords SET serp_signature_json=?,updated_at=? WHERE keyword_id=?", (canonical_json(urls[:10]), now_iso(), task["local_id"]))
                connection.execute("UPDATE provider_objects SET status='complete',metadata_json=?,updated_at=? WHERE provider='dataforseo' AND object_type='serp' AND local_id=?", (canonical_json({"run_id": args.run_id, "urls": len(urls[:10])}), now_iso(), task["local_id"]))
            collected += 1
    print(canonical_json({"collected": collected, "pending": pending, "failed": failed}))
    return 1 if failed else (2 if pending else 0)


def keywords_filter(args: argparse.Namespace, config: dict[str, Any], store: Any) -> int:
    store.initialize()
    known_brands = list(config["program"].get("excluded_brand_terms", [])) + list(args.brand)
    counts: dict[str, int] = {}
    with store.connect() as connection:
        rows = connection.execute("SELECT keyword_id,keyword,intent FROM keywords").fetchall()
        for row in rows:
            decision = classify_keyword(row["keyword"], known_brands, row["intent"])
            reason = None if decision.decision == "accept" else f"scope_{decision.decision}:{decision.reason_codes[0]}"
            selected = 0 if reason else 1
            connection.execute("UPDATE keywords SET exclusion_reason=?,selected=?,updated_at=? WHERE keyword_id=?", (reason, selected, now_iso(), row["keyword_id"]))
            stamp = now_iso()
            connection.execute(
                """INSERT INTO keyword_scope_decisions(keyword_id,classifier_version,decision,scope_class,reason_codes_json,created_at,updated_at)
                   VALUES(?,?,?,?,?,?,?) ON CONFLICT(keyword_id,classifier_version) DO UPDATE SET
                   decision=excluded.decision,scope_class=excluded.scope_class,
                   reason_codes_json=excluded.reason_codes_json,updated_at=excluded.updated_at""",
                (row["keyword_id"], CLASSIFIER_VERSION, decision.decision, decision.scope_class,
                 canonical_json(decision.reason_codes), stamp, stamp),
            )
            counts[reason or "selected"] = counts.get(reason or "selected", 0) + 1
    print(json.dumps({"keywords": len(rows), "results": counts}, indent=2))
    return 0


def keywords_scope_audit(
    args: argparse.Namespace, config: dict[str, Any], store: Any, *, apply: bool
) -> int:
    """Export deterministic eligibility lists and optionally apply them.

    The audit path is deliberately read-only.  The apply path only updates
    eligibility fields and the versioned decision table; raw keyword evidence
    is never removed.
    """
    store.initialize()
    version = config["program"].get("topic_scope_classifier_version", CLASSIFIER_VERSION)
    if version != CLASSIFIER_VERSION:
        raise ValueError(f"unsupported topic classifier version: {version}")
    known_brands = list(config["program"].get("excluded_brand_terms", [])) + list(args.brand)
    with store.connect() as connection:
        rows = connection.execute(
            "SELECT keyword_id,keyword,normalized_keyword,intent,search_volume,selected,exclusion_reason FROM keywords ORDER BY keyword_id"
        ).fetchall()

    decisions: list[dict[str, Any]] = []
    for row in rows:
        result = classify_keyword(row["keyword"], known_brands, row["intent"])
        decisions.append({
            "keyword_id": row["keyword_id"], "keyword": row["keyword"],
            "normalized_keyword": row["normalized_keyword"], "intent": row["intent"],
            "search_volume": row["search_volume"], **result.to_dict(),
        })

    args.output_dir.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "keyword_id", "keyword", "normalized_keyword", "intent", "search_volume",
        "decision", "scope_class", "reason_codes", "classifier_version",
    ]
    for decision_name, filename in (
        ("accept", "keywords-accepted.csv"),
        ("hold", "keywords-held.csv"),
        ("reject", "keywords-rejected.csv"),
    ):
        with (args.output_dir / filename).open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames)
            writer.writeheader()
            for item in decisions:
                if item["decision"] != decision_name:
                    continue
                writer.writerow({**item, "reason_codes": "|".join(item["reason_codes"])})

    counts: dict[str, int] = {}
    reasons: dict[str, int] = {}
    samples: dict[str, list[str]] = {}
    for item in decisions:
        counts[item["decision"]] = counts.get(item["decision"], 0) + 1
        for reason in item["reason_codes"]:
            reasons[reason] = reasons.get(reason, 0) + 1
            samples.setdefault(reason, [])
            if len(samples[reason]) < getattr(args, "samples_per_reason", 10):
                samples[reason].append(item["keyword"])

    if apply:
        now = now_iso()
        with store.connect() as connection:
            for item in decisions:
                reason = None if item["decision"] == "accept" else (
                    f"scope_{item['decision']}:" + item["reason_codes"][0]
                )
                connection.execute(
                    "UPDATE keywords SET selected=?,exclusion_reason=?,updated_at=? WHERE keyword_id=?",
                    (1 if item["decision"] == "accept" else 0, reason, now, item["keyword_id"]),
                )
                connection.execute(
                    """INSERT INTO keyword_scope_decisions(keyword_id,classifier_version,decision,scope_class,reason_codes_json,created_at,updated_at)
                       VALUES(?,?,?,?,?,?,?) ON CONFLICT(keyword_id,classifier_version) DO UPDATE SET
                       decision=excluded.decision,scope_class=excluded.scope_class,
                       reason_codes_json=excluded.reason_codes_json,updated_at=excluded.updated_at""",
                    (item["keyword_id"], version, item["decision"], item["scope_class"],
                     canonical_json(item["reason_codes"]), now, now),
                )

    summary = {
        "classifier_version": version, "mode": "apply" if apply else "audit",
        "keywords": len(decisions), "counts": counts, "reasons": reasons,
        "samples": samples, "output_dir": str(args.output_dir),
    }
    (args.output_dir / "keywords-scope-summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


def _ensure_dataforseo_budget(store: Any, run_id: str, config: dict[str, Any], reserve: float) -> None:
    with store.connect() as connection:
        spent = float(connection.execute("SELECT COALESCE(SUM(amount_usd),0) FROM api_costs WHERE run_id=? AND provider='dataforseo'", (run_id,)).fetchone()[0])
    limit = float(config["budgets_usd"]["dataforseo_run_hard_limit"])
    if spent + reserve > limit + 1e-9:
        raise RuntimeError(f"dataforseo preflight blocked: spent ${spent:.4f} + reserve ${reserve:.4f} exceeds ${limit:.4f}")


def jobs_create(args: argparse.Namespace, config: dict[str, Any], store: Any) -> int:
    store.ensure_run(args.run_id)
    limit = min(args.limit, config["program"]["daily_job_limit"])
    now = now_iso()
    inserted = existing = 0
    with store.connect() as connection:
        requested_keywords = list(getattr(args, "keyword", []) or [])
        keyword_file = getattr(args, "keyword_file", None)
        if keyword_file:
            if keyword_file.suffix.casefold() == ".csv":
                with keyword_file.open(encoding="utf-8-sig", newline="") as handle:
                    requested_keywords.extend(str(row.get("keyword", "")) for row in csv.DictReader(handle))
            elif keyword_file.suffix.casefold() == ".jsonl":
                requested_keywords.extend(str(row.get("keyword", "")) for row in load_jsonl(keyword_file))
            else:
                raise ValueError("--keyword-file must be a .csv or .jsonl file")
            requested_keywords = [keyword for keyword in requested_keywords if keyword.strip()]
        if requested_keywords:
            normalized = sorted({normalize_keyword(keyword) for keyword in requested_keywords})
            connection.execute("CREATE TEMP TABLE requested_keywords(normalized_keyword TEXT PRIMARY KEY)")
            connection.executemany(
                "INSERT OR IGNORE INTO requested_keywords(normalized_keyword) VALUES(?)",
                ((keyword,) for keyword in normalized),
            )
            rows = connection.execute(
                """SELECT c.cluster_id,k.keyword_id,k.normalized_keyword
                    FROM keywords k JOIN clusters c ON c.cluster_id=k.cluster_id
                    JOIN requested_keywords r ON r.normalized_keyword=k.normalized_keyword
                    WHERE k.selected=1 AND k.exclusion_reason IS NULL
                      AND EXISTS (SELECT 1 FROM keyword_scope_decisions sd
                                  WHERE sd.keyword_id=k.keyword_id AND sd.classifier_version=? AND sd.decision='accept')
                      AND NOT EXISTS (
                        SELECT 1 FROM similarity_reviews sr
                        WHERE sr.object_type='topic' AND sr.status='needs_review'
                          AND k.keyword_id IN (sr.left_id,sr.right_id)
                      )
                    ORDER BY COALESCE(k.search_volume,0) DESC,k.normalized_keyword LIMIT ?""",
                (CLASSIFIER_VERSION, limit),
            ).fetchall()
            found = {row["normalized_keyword"] for row in rows}
            missing = sorted(set(normalized) - found)
            if missing:
                raise ValueError(f"requested keywords are not selected clustered topics: {missing}")
        else:
            rows = connection.execute(
                """SELECT c.cluster_id,k.keyword_id,k.normalized_keyword,COALESCE(k.search_volume,0) search_volume
                   FROM clusters c JOIN keywords k ON k.keyword_id=c.primary_keyword_id
                   WHERE k.selected=1 AND k.exclusion_reason IS NULL
                     AND EXISTS (SELECT 1 FROM keyword_scope_decisions sd
                                 WHERE sd.keyword_id=k.keyword_id AND sd.classifier_version=? AND sd.decision='accept')
                   ORDER BY COALESCE(k.search_volume,0) DESC,k.normalized_keyword"""
                , (CLASSIFIER_VERSION,)
            ).fetchall()
            blocked = {
                item_id
                for review in connection.execute(
                    "SELECT left_id,right_id FROM similarity_reviews WHERE object_type='topic' AND status='needs_review'"
                ).fetchall()
                for item_id in (review["left_id"], review["right_id"])
            }
            rows = [row for row in rows if row["keyword_id"] not in blocked]
            if getattr(args, "new_only", False):
                existing_job_ids = {row[0] for row in connection.execute("SELECT job_id FROM content_jobs")}
                rows = [row for row in rows if stable_id("job", row["cluster_id"]) not in existing_job_ids]
            rows = rows[:limit]
        for row in rows:
            already_owned = connection.execute(
                "SELECT 1 FROM content_jobs WHERE keyword_id=? LIMIT 1", (row["keyword_id"],)
            ).fetchone()
            if already_owned:
                existing += 1
                continue
            job_id = stable_id("job", row["cluster_id"])
            custom_id = stable_id("article", row["cluster_id"])
            cursor = connection.execute(
                """INSERT OR IGNORE INTO content_jobs(job_id,created_run_id,keyword_id,custom_id,status,created_at,updated_at)
                   VALUES(?,?,?,?,?,?,?)""", (job_id, args.run_id, row["keyword_id"], custom_id, "queued_for_plan", now, now)
            )
            inserted += cursor.rowcount
            existing += int(cursor.rowcount == 0)
    print(canonical_json({"eligible_clusters": len(rows), "created": inserted, "existing": existing, "daily_limit": limit}))
    return 0


def jobs_requeue_articles(args: argparse.Namespace, paths: Any, store: Any) -> int:
    """Create a fresh bounded candidate wave without deleting its audit trail."""
    store.ensure_run(args.run_id)
    with store.connect() as connection:
        rows = connection.execute(
            """SELECT j.*,k.keyword,k.normalized_keyword,k.intent,sr.custom_id review_custom_id,
                      sr.review_json,sr.passed review_passed
               FROM content_jobs j JOIN keywords k ON k.keyword_id=j.keyword_id
               LEFT JOIN semantic_reviews sr ON sr.job_id=j.job_id
               WHERE j.created_run_id=? AND j.status='blocked_missing_sources'
                 AND j.plan_json IS NOT NULL AND j.duplicate_of_job_id IS NULL
               ORDER BY CASE WHEN k.keyword GLOB '*[0-9]*' THEN 1 ELSE 0 END,
                        COALESCE(k.search_volume,0) DESC,k.normalized_keyword,j.job_id
               LIMIT ?""",
            (args.run_id, args.limit),
        ).fetchall()
    destination = args.output or paths.outputs / f"{args.run_id}-pre-requeue-backup.jsonl"
    backup = [{key: row[key] for key in row.keys()} for row in rows]
    write_jsonl(destination, backup)
    job_ids = [row["job_id"] for row in rows]
    now = now_iso()
    if job_ids:
        marks = ",".join("?" for _ in job_ids)
        with store.connect() as connection:
            connection.execute(f"DELETE FROM semantic_reviews WHERE job_id IN ({marks})", job_ids)
            connection.execute(
                f"DELETE FROM internal_links WHERE source_job_id IN ({marks}) OR target_job_id IN ({marks})",
                (*job_ids, *job_ids),
            )
            connection.execute(
                f"DELETE FROM embeddings WHERE object_type='chunk' AND object_id IN ({marks})",
                job_ids,
            )
            connection.execute(
                f"""UPDATE content_jobs
                    SET status='planned',article_json=NULL,source_pack_json=NULL,
                        validation_json='{{}}',retry_count=0,text_fingerprint=NULL,
                        semantic_score=NULL,git_commit=NULL,published_url=NULL,updated_at=?
                    WHERE job_id IN ({marks})""",
                (now, *job_ids),
            )
    print(canonical_json({"requeued": len(job_ids), "backup": str(destination)}))
    return 0


def jobs_export(args: argparse.Namespace, store: Any) -> int:
    store.ensure_run(args.run_id)
    required_status = {"plan": "queued_for_plan", "article": "planned", "review": "awaiting_semantic_review"}[args.kind]
    with store.connect() as connection:
        completeness = {
            "plan": "",
            "article": " AND j.plan_json IS NOT NULL AND j.source_pack_json IS NOT NULL",
            "review": " AND j.plan_json IS NOT NULL AND j.source_pack_json IS NOT NULL AND j.article_json IS NOT NULL",
        }[args.kind]
        scope = "j.created_run_id=?"
        scope_params: tuple[Any, ...] = (args.run_id,)
        if getattr(args, "source_batch_id", None):
            # A batch-scoped rebuild is also the recovery path for drafts that
            # failed only because their derived link graph was missing.  Do
            # not require the request itself to have passed ingestion, or the
            # jobs that need local link repair can never enter the graph.
            scope = "EXISTS (SELECT 1 FROM batch_requests br WHERE br.job_id=j.job_id AND br.batch_id=?)"
            scope_params = (args.source_batch_id,)
        rows = connection.execute(
            """SELECT j.*,k.keyword,k.normalized_keyword,k.intent,c.cluster_id
               FROM content_jobs j JOIN keywords k ON k.keyword_id=j.keyword_id
               LEFT JOIN clusters c ON c.cluster_id=k.cluster_id
               WHERE j.status=? AND """ + scope + " AND j.duplicate_of_job_id IS NULL" + completeness + " ORDER BY j.job_id LIMIT ?",
            (required_status, *scope_params, args.limit),
        ).fetchall()
        output = []
        for row in rows:
            version_material = f"{args.run_id}:{row['job_id']}:{args.kind}:{REQUEST_VERSION}"
            suffix = sha256_bytes(version_material.encode())[:16]
            custom_id = f"msg-{args.kind}-{REQUEST_VERSION}-{suffix}"
            if args.kind == "plan":
                secondary = [item[0] for item in connection.execute("SELECT keyword FROM keywords WHERE cluster_id=? AND keyword_id<>? AND exclusion_reason IS NULL ORDER BY COALESCE(search_volume,0) DESC LIMIT 12", (row["cluster_id"], row["keyword_id"]))]
                payload = {
                    "job_id": row["job_id"], "primary_keyword": row["keyword"], "secondary_keywords": secondary,
                    "search_intent": row["intent"] or "informational", "target_market": "United States",
                    "requirements": {"one_owned_question": True, "zero_brand": True, "educational_only": True},
                }
            elif args.kind == "article":
                if not row["plan_json"] or not row["source_pack_json"]:
                    continue
                plan = json.loads(row["plan_json"])
                source_pack = json.loads(row["source_pack_json"])
                uncovered = list((source_pack.get("coverage") or {}).get("uncovered_terms") or [])
                if uncovered:
                    connection.execute(
                        "UPDATE content_jobs SET status='blocked_missing_sources',validation_json=?,updated_at=? WHERE job_id=?",
                        (canonical_json({"error": "source pack has uncovered center-topic terms", "uncovered_terms": uncovered}), now_iso(), row["job_id"]),
                    )
                    continue
                h2_count = max(1, len(plan.get("outline", [])))
                introduction_words = 130
                target_total_words = 1200
                each_h2_words = max(180, (target_total_words - introduction_words + h2_count - 1) // h2_count)
                compact_plan = {
                    key: plan.get(key)
                    for key in (
                        "primary_keyword", "secondary_keywords", "owned_question",
                        "topic_scope", "excluded_questions", "angle", "outline", "must_cover",
                    )
                }
                compact_claims = [
                    {
                        key: claim.get(key)
                        for key in ("claim_id", "subject", "predicate", "value", "unit", "conditions", "scope")
                    }
                    for claim in source_pack.get("claims", [])
                    if claim.get("status") == "accepted"
                ]
                payload = {
                    "plan": compact_plan,
                    "claims": compact_claims,
                    "word_budget": {
                        "target_total_words": target_total_words,
                        "introduction_words": introduction_words,
                        "each_h2_words": each_h2_words,
                        "h2_count": h2_count,
                    },
                }
                # Article inputs can legitimately change after a failed draft
                # when evidence or the approved link graph is repaired. Keep
                # identical inputs idempotent while versioning changed inputs.
                custom_id = f"msg-{args.kind}-{REQUEST_VERSION}-{sha256_bytes((version_material + ':' + canonical_json(payload)).encode())[:16]}"
            else:
                if not row["article_json"] or not row["plan_json"] or not row["source_pack_json"]:
                    continue
                payload = _review_payload(connection, row)
                # Review identity covers the article and its complete review
                # context so changed evidence or plans cannot collide.
                custom_id = _review_custom_id(args.run_id, row["job_id"], row["article_json"], payload)
            output.append({"custom_id": custom_id, "job_id": row["job_id"], "payload": payload})
    write_jsonl(args.output, output)
    print(canonical_json({"kind": args.kind, "exported": len(output), "output": str(args.output)}))
    return 0


def qdrant_init(args: argparse.Namespace, config: dict[str, Any], credentials: dict[str, str]) -> int:
    expected = config["models"]["embedding_dimensions"]
    if not args.skip_embedding_check:
        provider = args.provider or config["models"]["embedding_provider"]
        vectors = _embedding_client(provider, config, credentials).embed(["micro switch operating principle"], "query")
        actual = len(vectors[0]) if vectors else 0
        if actual != expected:
            raise RuntimeError(f"embedding dimension mismatch: expected {expected}, received {actual}")
    client = QdrantClient(credentials["QDRANT_URL"], credentials["QDRANT_API_KEY"])
    results = {}
    for kind, name in config["qdrant"]["collections"].items():
        try:
            client.create_collection(name, expected, config["qdrant"]["distance"])
            results[kind] = "created"
        except Exception as exc:
            if "already exists" in str(exc).casefold():
                results[kind] = "exists"
            else:
                raise
    print(canonical_json({"dimensions": expected, "collections": results}))
    return 0


def embedding_export(args: argparse.Namespace, store: Any) -> int:
    output: list[dict[str, str]] = []
    with store.connect() as connection:
        statuses = getattr(args, "status", None) or []
        run_id = getattr(args, "run_id", None)
        status_filter = ""
        status_params: tuple[Any, ...] = ()
        if statuses:
            status_filter = f" AND j.status IN ({','.join('?' for _ in statuses)})"
            status_params = tuple(statuses)
        run_filter = " AND j.created_run_id=?" if run_id else ""
        run_params: tuple[Any, ...] = (run_id,) if run_id else ()
        batch_id = getattr(args, "batch_id", None)
        batch_filter = " AND EXISTS (SELECT 1 FROM batch_requests br WHERE br.job_id=j.job_id AND br.batch_id=? AND br.status='completed')" if batch_id else ""
        batch_params: tuple[Any, ...] = (batch_id,) if batch_id else ()
        if args.object_type == "topic":
            cluster_filter = " AND cluster_id IS NULL" if args.only_unclustered else ""
            rows = connection.execute(f"SELECT keyword_id,normalized_keyword,intent,serp_signature_json FROM keywords WHERE selected=1 AND exclusion_reason IS NULL{cluster_filter} ORDER BY keyword_id LIMIT ?", (args.limit,)).fetchall()
            output = [{"id": row["keyword_id"], "text": f"{row['normalized_keyword']}\nintent: {row['intent'] or 'informational'}", "intent": row["intent"] or "informational", "serp_urls": json.loads(row["serp_signature_json"] or "[]")} for row in rows]
        elif args.object_type in {"article_plan", "section_plan"}:
            rows = connection.execute(f"SELECT j.job_id,j.plan_json FROM content_jobs j JOIN keywords k ON k.keyword_id=j.keyword_id WHERE j.plan_json IS NOT NULL AND j.duplicate_of_job_id IS NULL{status_filter}{run_filter}{batch_filter} ORDER BY COALESCE(k.search_volume,0) DESC,j.job_id LIMIT ?", (*status_params, *run_params, *batch_params, args.limit)).fetchall()
            for row in rows:
                plan = json.loads(row["plan_json"])
                if args.object_type == "article_plan":
                    outline = "\n".join(item.get("h2", "") for item in plan.get("outline", []))
                    output.append({"id": row["job_id"], "job_id": row["job_id"], "granularity": "plan", "text": f"{plan.get('owned_question','')}\n{plan.get('angle','')}\n{outline}"})
                else:
                    for index, section in enumerate(plan.get("outline", [])):
                        output.append({"id": f"{row['job_id']}:{index}", "job_id": row["job_id"], "granularity": "section_plan", "text": f"{section.get('h2','')}\n{section.get('purpose','')}\n{' '.join(section.get('points',[]))}"})
        else:
            rows = connection.execute(f"SELECT j.job_id,j.article_json FROM content_jobs j WHERE j.article_json IS NOT NULL AND j.duplicate_of_job_id IS NULL{status_filter}{run_filter}{batch_filter} ORDER BY j.job_id LIMIT ?", (*status_params, *run_params, *batch_params, args.limit)).fetchall()
            for row in rows:
                body = json.loads(row["article_json"]).get("body_markdown", "")
                if getattr(args, "granularity", "article") == "section":
                    sections = [part.strip() for part in re.split(r"(?=^##\s+)", body, flags=re.MULTILINE) if part.strip()]
                    for index, section in enumerate(sections):
                        output.append({
                            "id": f"{row['job_id']}:section:{index}",
                            "job_id": row["job_id"],
                            "granularity": "section",
                            "text": section[:6000],
                        })
                else:
                    # Article-level IDs retain the content job id so an
                    # applied duplicate decision can update the authoritative row.
                    output.append({"id": row["job_id"], "job_id": row["job_id"], "granularity": "article", "text": body[:12000]})
    write_jsonl(args.output, output)
    print(canonical_json({"object_type": args.object_type, "exported": len(output), "output": str(args.output)}))
    return 0


def embed_objects(args: argparse.Namespace, config: dict[str, Any], store: Any, credentials: dict[str, str]) -> int:
    rows = load_jsonl(args.input)
    for row in rows:
        if not row.get("id") or not row.get("text"):
            raise ValueError("every embedding input needs id and text")
    provider = args.provider or config["models"]["embedding_provider"]
    embedder = _embedding_client(provider, config, credentials)
    qdrant = QdrantClient(credentials["QDRANT_URL"], credentials["QDRANT_API_KEY"])
    output = []
    expected = config["models"]["embedding_dimensions"]
    for offset in range(0, len(rows), args.batch_size):
        chunk = rows[offset:offset + args.batch_size]
        vectors = embedder.embed([row["text"] for row in chunk], "document")
        if len(vectors) != len(chunk) or any(len(vector) != expected for vector in vectors):
            raise RuntimeError("embedding response count or dimensions do not match request")
        points = []
        for row, vector in zip(chunk, vectors):
            point_id = str(uuid.uuid5(uuid.NAMESPACE_URL, f"msg:{args.object_type}:{row['id']}"))
            payload = {"local_id": row["id"], "text": row["text"], "object_type": args.object_type}
            for field in ("job_id", "granularity"):
                if row.get(field) is not None:
                    payload[field] = row[field]
            points.append({"id": point_id, "vector": vector, "payload": payload})
            output.append({**row, "vector": vector, "qdrant_point_id": point_id})
            with store.connect() as connection:
                connection.execute("""INSERT INTO embeddings(object_type,object_id,model,dimensions,vector_sha256,qdrant_point_id,created_at)
                    VALUES(?,?,?,?,?,?,?) ON CONFLICT(object_type,object_id,model) DO UPDATE SET dimensions=excluded.dimensions,vector_sha256=excluded.vector_sha256,qdrant_point_id=excluded.qdrant_point_id""",
                    (args.object_type, row["id"], config["models"]["embedding"], expected, sha256_bytes(canonical_json(vector).encode()), point_id, now_iso()))
        qdrant.upsert(config["qdrant"]["collections"][args.object_type], points)
    write_jsonl(args.output, output)
    print(canonical_json({"embedded": len(output), "output": str(args.output)}))
    return 0


def _embedding_client(provider: str, config: dict[str, Any], credentials: dict[str, str]) -> Any:
    model = config["models"]["embedding"]
    if provider == "local":
        return LocalEmbeddingClient(model)
    if provider == "openrouter":
        if not credentials.get("OPENROUTER_API_KEY"):
            raise RuntimeError("OPENROUTER_API_KEY is required only when --provider openrouter is selected")
        return OpenRouterClient(credentials["OPENROUTER_API_KEY"], model)
    raise ValueError(f"unsupported embedding provider: {provider}")


def cluster_keywords(args: argparse.Namespace, config: dict[str, Any], store: Any, credentials: dict[str, str]) -> int:
    threshold = args.threshold
    if threshold is None:
        with store.connect() as connection:
            calibrated = connection.execute("SELECT metadata_json FROM provider_objects WHERE provider='local' AND object_type='similarity_calibration' AND local_id='topic:v1' AND status='complete'").fetchone()
        threshold = json.loads(calibrated[0])["threshold"] if calibrated else config["similarity"]["near_duplicate"]
    rows = load_jsonl(args.input)
    if args.local and args.incremental:
        raise ValueError("incremental clustering requires Qdrant; do not combine --incremental with --local")
    cluster_records: list[tuple[list[dict[str, Any]], str | None]]
    if args.local or (len(rows) <= 200 and not args.incremental):
        clusters = cluster_vectors(rows, threshold)
        cluster_records = [(members, None) for members in clusters]
        review_pairs: list[dict[str, Any]] = []
    else:
        qdrant = QdrantClient(credentials["QDRANT_URL"], credentials["QDRANT_API_KEY"])
        by_id = {str(row["id"]): row for row in rows}
        parent = {item_id: item_id for item_id in by_id}
        with store.connect() as connection:
            existing_clusters = {
                row["keyword_id"]: row["cluster_id"]
                for row in connection.execute("SELECT keyword_id,cluster_id FROM keywords WHERE cluster_id IS NOT NULL")
            }

        def find(item_id: str) -> str:
            while parent[item_id] != item_id:
                parent[item_id] = parent[parent[item_id]]
                item_id = parent[item_id]
            return item_id

        def union(left: str, right: str) -> None:
            a, b = find(left), find(right)
            if a != b:
                parent[max(a, b)] = min(a, b)

        def query_batch(chunk: list[dict[str, Any]]) -> list[tuple[str, list[dict[str, Any]]]]:
            results = qdrant.query_batch(
                config["qdrant"]["collections"]["topic"],
                [row["vector"] for row in chunk],
                config["similarity"]["neighbors"],
                config["similarity"]["same_topic_lower"],
            )
            if len(results) != len(chunk):
                raise RuntimeError(f"Qdrant batch query returned {len(results)} result sets for {len(chunk)} vectors")
            return [(str(row["id"]), neighbors) for row, neighbors in zip(chunk, results)]

        review_pairs = []
        external_candidates: dict[str, list[tuple[float, str, str]]] = {}
        query_chunks = [rows[offset:offset + 64] for offset in range(0, len(rows), 64)]
        with ThreadPoolExecutor(max_workers=8) as executor:
            futures = [executor.submit(query_batch, chunk) for chunk in query_chunks]
            for future in as_completed(futures):
                for left_id, neighbors in future.result():
                    left = by_id[left_id]
                    for neighbor in neighbors:
                        right_id = str((neighbor.get("payload") or {}).get("local_id", ""))
                        if not right_id or right_id == left_id:
                            continue
                        score = float(neighbor.get("score") or 0)
                        if right_id in existing_clusters and right_id not in by_id:
                            if score >= threshold:
                                external_candidates.setdefault(left_id, []).append((score, existing_clusters[right_id], right_id))
                            else:
                                review_pairs.append({"left_id": left_id, "right_id": right_id, "score": score, "serp_overlap": 0.0})
                            continue
                        if right_id not in by_id or left_id > right_id:
                            continue
                        if score >= threshold:
                            union(left_id, right_id)
                        else:
                            right = by_id[right_id]
                            overlap = serp_overlap(left.get("serp_urls", []), right.get("serp_urls", []))
                            same_intent = left.get("intent") == right.get("intent")
                            if same_intent and overlap >= 0.6:
                                union(left_id, right_id)
                            else:
                                review_pairs.append({"left_id": left_id, "right_id": right_id, "score": score, "serp_overlap": overlap})
        grouped: dict[str, list[dict[str, Any]]] = {}
        for item_id, row in by_id.items():
            grouped.setdefault(find(item_id), []).append(row)
        clusters = list(grouped.values())
        cluster_records = []
        for root, members in grouped.items():
            candidates = [candidate for member in members for candidate in external_candidates.get(str(member["id"]), [])]
            target_cluster = max(candidates, default=None, key=lambda item: item[0])[1] if candidates else None
            cluster_records.append((members, target_cluster))
    now = now_iso()
    with store.connect() as connection:
        item_ids = [str(row["id"]) for row in rows]
        placeholders = ",".join("?" for _ in item_ids)
        if item_ids:
            existing_jobs = connection.execute(
                f"""SELECT COUNT(*) FROM content_jobs j JOIN keywords k ON k.keyword_id=j.keyword_id
                    WHERE k.keyword_id IN ({placeholders})""",
                item_ids,
            ).fetchone()[0]
            if existing_jobs and not getattr(args, "new_version", False):
                raise RuntimeError("topic reclustering is blocked after article jobs exist; create a new versioned topic set")
            old_cluster_ids = [row[0] for row in connection.execute(
                f"SELECT DISTINCT cluster_id FROM keywords WHERE keyword_id IN ({placeholders}) AND cluster_id IS NOT NULL",
                item_ids,
            )]
            connection.execute(f"UPDATE keywords SET cluster_id=NULL,updated_at=? WHERE keyword_id IN ({placeholders})", (now, *item_ids))
            if old_cluster_ids:
                old_placeholders = ",".join("?" for _ in old_cluster_ids)
                connection.execute(f"DELETE FROM clusters WHERE cluster_id IN ({old_placeholders})", old_cluster_ids)
        for members, target_cluster_id in cluster_records:
            ids = sorted(str(item["id"]) for item in members)
            cluster_id = target_cluster_id or stable_id("cluster", "|".join(ids))
            keyword_rows = [connection.execute("SELECT keyword_id,search_volume FROM keywords WHERE keyword_id=?", (item_id,)).fetchone() for item_id in ids]
            keyword_rows = [row for row in keyword_rows if row]
            primary = max(keyword_rows, key=lambda row: row["search_volume"] or 0)["keyword_id"] if keyword_rows else None
            if not target_cluster_id:
                connection.execute("INSERT INTO clusters(cluster_id,algorithm_version,threshold,primary_keyword_id,label,created_at) VALUES(?,?,?,?,?,?) ON CONFLICT(cluster_id) DO UPDATE SET threshold=excluded.threshold,primary_keyword_id=excluded.primary_keyword_id", (cluster_id, "greedy-cosine-v1", threshold, primary, None, now))
            connection.executemany("UPDATE keywords SET cluster_id=?,updated_at=? WHERE keyword_id=?", [(cluster_id, now, item_id) for item_id in ids])
        for pair in review_pairs:
            connection.execute("INSERT INTO similarity_reviews(object_type,left_id,right_id,cosine_score,serp_overlap,label,status,created_at,updated_at) VALUES('topic',?,?,?,?,NULL,'needs_review',?,?) ON CONFLICT(object_type,left_id,right_id) DO UPDATE SET cosine_score=excluded.cosine_score,serp_overlap=excluded.serp_overlap,updated_at=excluded.updated_at", (pair["left_id"], pair["right_id"], pair["score"], pair["serp_overlap"], now, now))
    print(canonical_json({"items": len(rows), "clusters": len(cluster_records), "threshold": threshold, "needs_review": len(review_pairs), "attached_existing": sum(1 for _, target in cluster_records if target), "engine": "qdrant-incremental" if args.incremental else ("local" if args.local or len(rows) <= 200 else "qdrant")}))
    return 0


def similarity_calibration_sample(args: argparse.Namespace, store: Any) -> int:
    if args.limit < 1:
        raise ValueError("limit must be positive")
    with store.connect() as connection:
        existing = connection.execute(
            """SELECT sr.left_id,sr.right_id,sr.cosine_score,sr.label,
                      kl.normalized_keyword left_keyword,kr.normalized_keyword right_keyword
               FROM similarity_reviews sr
               JOIN keywords kl ON kl.keyword_id=sr.left_id
               JOIN keywords kr ON kr.keyword_id=sr.right_id
               WHERE sr.object_type='topic' AND sr.label IN ('same','different')
               ORDER BY sr.cosine_score DESC,left_id,right_id"""
        ).fetchall()
        candidates = connection.execute(
            """SELECT sr.left_id,sr.right_id,sr.cosine_score,
                      kl.normalized_keyword left_keyword,kr.normalized_keyword right_keyword
               FROM similarity_reviews sr
               JOIN keywords kl ON kl.keyword_id=sr.left_id
               JOIN keywords kr ON kr.keyword_id=sr.right_id
               WHERE sr.object_type='topic' AND sr.status='needs_review'
               ORDER BY sr.cosine_score DESC,left_id,right_id"""
        ).fetchall()

    stop = {
        "a", "an", "the", "what", "is", "are", "does", "do", "how", "to",
        "meaning", "definition", "defined", "explained", "explanation", "guide",
        "micro", "switch", "switches",
    }

    def tokens(value: str) -> list[str]:
        result = []
        for token in re.findall(r"[a-z0-9]+", normalize_keyword(value)):
            if token in stop:
                continue
            if len(token) > 4 and token.endswith("s") and not token.endswith("ss"):
                token = token[:-1]
            result.append(token)
        return result

    def conservative_label(left: str, right: str) -> str:
        left_tokens, right_tokens = tokens(left), tokens(right)
        if not left_tokens or not right_tokens:
            return "different"
        left_set, right_set = set(left_tokens), set(right_tokens)
        if left_set == right_set:
            return "same"
        union = left_set | right_set
        jaccard = len(left_set & right_set) / len(union)
        sequence = difflib.SequenceMatcher(None, " ".join(left_tokens), " ".join(right_tokens)).ratio()
        return "same" if jaccard >= 0.9 and sequence >= 0.9 else "different"

    rows: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    for row in existing:
        key = (row["left_id"], row["right_id"])
        if key in seen or len(rows) >= args.limit:
            continue
        seen.add(key)
        rows.append({
            "left_id": row["left_id"], "right_id": row["right_id"],
            "left_keyword": row["left_keyword"], "right_keyword": row["right_keyword"],
            "score": float(row["cosine_score"]), "label": row["label"], "label_source": "existing_review",
        })
    needed = args.limit - len(rows)
    if needed > 0 and candidates:
        # Evenly sample the score-sorted boundary population rather than taking
        # only the most similar pairs. Labels are conservative: uncertain pairs
        # remain separate, which prevents model-code keywords from being lost.
        indexes = [min(len(candidates) - 1, int(index * len(candidates) / needed)) for index in range(needed)]
        for index in indexes:
            row = candidates[index]
            key = (row["left_id"], row["right_id"])
            if key in seen:
                continue
            seen.add(key)
            rows.append({
                "left_id": row["left_id"], "right_id": row["right_id"],
                "left_keyword": row["left_keyword"], "right_keyword": row["right_keyword"],
                "score": float(row["cosine_score"]),
                "label": conservative_label(row["left_keyword"], row["right_keyword"]),
                "label_source": "conservative_lexical_adjudication",
            })
    if len(rows) < args.limit:
        raise RuntimeError(f"only {len(rows)} unique calibration pairs are available")
    rows = rows[:args.limit]
    write_jsonl(args.output, rows)
    counts = {label: sum(row["label"] == label for row in rows) for label in ("same", "different")}
    print(canonical_json({"pairs": len(rows), "labels": counts, "output": str(args.output), "merges_applied": 0}))
    return 0


def similarity_calibrate(args: argparse.Namespace, config: dict[str, Any], store: Any) -> int:
    rows = load_jsonl(args.input)
    minimum = config["similarity"]["calibration_pairs"]
    if len(rows) < minimum:
        raise ValueError(f"calibration requires at least {minimum} labeled pairs")
    for row in rows:
        if row.get("label") not in {"same", "different"}:
            raise ValueError("each calibration label must be same or different")
        if not 0 <= float(row.get("score", -1)) <= 1:
            raise ValueError("each calibration score must be between 0 and 1")
    candidates = sorted({float(row["score"]) for row in rows})
    best = None
    for threshold in candidates:
        tp = fp = fn = 0
        for row in rows:
            predicted = float(row["score"]) >= threshold
            actual = row["label"] == "same"
            tp += int(predicted and actual)
            fp += int(predicted and not actual)
            fn += int(not predicted and actual)
        precision = tp / (tp + fp) if tp + fp else 0
        recall = tp / (tp + fn) if tp + fn else 0
        f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0
        candidate = (f1, precision, recall, threshold)
        if best is None or candidate > best:
            best = candidate
    assert best is not None
    f1, precision, recall, threshold = best
    now = now_iso()
    with store.connect() as connection:
        for row in rows:
            left, right = sorted((str(row["left_id"]), str(row["right_id"])))
            connection.execute("INSERT INTO similarity_reviews(object_type,left_id,right_id,cosine_score,serp_overlap,label,status,created_at,updated_at) VALUES('topic',?,?,?,?,?,'labeled',?,?) ON CONFLICT(object_type,left_id,right_id) DO UPDATE SET cosine_score=excluded.cosine_score,label=excluded.label,status='labeled',updated_at=excluded.updated_at", (left, right, float(row["score"]), row.get("serp_overlap"), row["label"], now, now))
        metadata = {"threshold": threshold, "f1": f1, "precision": precision, "recall": recall, "pairs": len(rows)}
        connection.execute("INSERT INTO provider_objects(provider,object_type,local_id,status,metadata_json,created_at,updated_at) VALUES('local','similarity_calibration','topic:v1','complete',?,?,?) ON CONFLICT(provider,object_type,local_id) DO UPDATE SET status='complete',metadata_json=excluded.metadata_json,updated_at=excluded.updated_at", (canonical_json(metadata), now, now))
    print(canonical_json(metadata))
    return 0


def similarity_review_apply(args: argparse.Namespace, store: Any) -> int:
    labels = load_jsonl(args.input)
    applied = different = conflicts = 0
    now = now_iso()
    with store.connect() as connection:
        for item in labels:
            left_id, right_id = str(item.get("left_id", "")), str(item.get("right_id", ""))
            label = item.get("label")
            if not left_id or not right_id or left_id == right_id or label not in {"same", "different"}:
                raise ValueError("each similarity review needs distinct left_id/right_id and label same/different")
            review = connection.execute(
                "SELECT * FROM similarity_reviews WHERE object_type='topic' AND ((left_id=? AND right_id=?) OR (left_id=? AND right_id=?))",
                (left_id, right_id, right_id, left_id),
            ).fetchone()
            if not review:
                raise ValueError(f"unknown similarity review pair: {left_id}, {right_id}")
            db_left, db_right = review["left_id"], review["right_id"]
            if label == "different":
                connection.execute(
                    "UPDATE similarity_reviews SET label='different',status='labeled',updated_at=? WHERE object_type='topic' AND left_id=? AND right_id=?",
                    (now, db_left, db_right),
                )
                different += 1
                continue
            clusters = connection.execute(
                "SELECT keyword_id,cluster_id FROM keywords WHERE keyword_id IN (?,?)",
                (left_id, right_id),
            ).fetchall()
            cluster_by_keyword = {row["keyword_id"]: row["cluster_id"] for row in clusters}
            left_cluster, right_cluster = cluster_by_keyword.get(left_id), cluster_by_keyword.get(right_id)
            if not left_cluster or not right_cluster:
                raise ValueError(f"similarity pair contains an unclustered topic: {left_id}, {right_id}")
            if left_cluster != right_cluster:
                job_counts = {}
                for cluster_id in (left_cluster, right_cluster):
                    job_counts[cluster_id] = connection.execute(
                        "SELECT COUNT(*) FROM content_jobs j JOIN keywords k ON k.keyword_id=j.keyword_id WHERE k.cluster_id=?",
                        (cluster_id,),
                    ).fetchone()[0]
                if job_counts[left_cluster] and job_counts[right_cluster]:
                    conflicts += 1
                    continue
                target = left_cluster if job_counts[left_cluster] else (right_cluster if job_counts[right_cluster] else min(left_cluster, right_cluster))
                source = right_cluster if target == left_cluster else left_cluster
                connection.execute("UPDATE keywords SET cluster_id=?,updated_at=? WHERE cluster_id=?", (target, now, source))
                primary = connection.execute(
                    "SELECT keyword_id FROM keywords WHERE cluster_id=? ORDER BY COALESCE(search_volume,0) DESC,normalized_keyword LIMIT 1",
                    (target,),
                ).fetchone()
                connection.execute("UPDATE clusters SET primary_keyword_id=? WHERE cluster_id=?", (primary[0], target))
                connection.execute("DELETE FROM clusters WHERE cluster_id=?", (source,))
            connection.execute(
                "UPDATE similarity_reviews SET label='same',status='applied',updated_at=? WHERE object_type='topic' AND left_id=? AND right_id=?",
                (now, db_left, db_right),
            )
            applied += 1
    print(canonical_json({"reviews": len(labels), "same_applied": applied, "different_labeled": different, "job_conflicts": conflicts}))
    return 1 if conflicts else 0


def source_action(args: argparse.Namespace, paths: Any, config: dict[str, Any], store: Any) -> int:
    if args.action == "quarantine-commercial":
        allowed = ("standard", "regulator", "government", "intergovernmental", "academic", "encyclopedia")
        placeholders = ",".join("?" for _ in allowed)
        now = now_iso()
        with store.connect() as connection:
            commercial_claims = [
                row[0]
                for row in connection.execute(
                    f"""SELECT DISTINCT cs.claim_id
                        FROM claim_sources cs JOIN sources s ON s.source_id=cs.source_id
                        WHERE s.source_type NOT IN ({placeholders})
                           OR s.editorial_block_names_json <> '[]'""",
                    allowed,
                )
            ]
            if commercial_claims:
                claim_marks = ",".join("?" for _ in commercial_claims)
                connection.execute(
                    f"UPDATE claims SET status='blocked',updated_at=? WHERE claim_id IN ({claim_marks})",
                    (now, *commercial_claims),
                )
            invalid_job_ids = []
            for row in connection.execute(
                "SELECT job_id,source_pack_json FROM content_jobs WHERE article_json IS NOT NULL AND source_pack_json IS NOT NULL"
            ):
                pack = json.loads(row["source_pack_json"])
                if any(
                    source.get("source_type") not in allowed or source.get("editorial_block_names")
                    for source in pack.get("sources", [])
                ):
                    invalid_job_ids.append(row["job_id"])
            invalidated = 0
            if invalid_job_ids:
                job_marks = ",".join("?" for _ in invalid_job_ids)
                invalidated = connection.execute(
                    f"""UPDATE content_jobs
                        SET status='blocked_missing_sources',source_pack_json=NULL,
                            validation_json=?,updated_at=?
                        WHERE job_id IN ({job_marks})""",
                    (canonical_json({"error": "source policy changed; rebuild from noncommercial sources"}), now, *invalid_job_ids),
                ).rowcount
        print(canonical_json({"commercial_claims_blocked": len(commercial_claims), "articles_invalidated": invalidated}))
        return 0
    schema = load_json(Path(config["skill"]["root"]) / "references" / "source-pack.schema.json")
    if args.action == "ingest":
        if not args.input:
            raise ValueError("sources ingest requires --input")
        result = ingest_source_pack(store, load_json(args.input), schema)
        print(canonical_json(result))
        return 0
    if not args.topic_id or not args.term:
        raise ValueError("sources build-pack requires --topic-id and at least one --term")
    pack = build_source_pack(store, args.topic_id, args.term)
    destination = args.output or paths.outputs / f"source-pack-{args.topic_id}.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(pack, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.job_id:
        with store.connect() as connection:
            cursor = connection.execute("UPDATE content_jobs SET source_pack_json=?,updated_at=? WHERE job_id=?", (canonical_json(pack), now_iso(), args.job_id))
            if cursor.rowcount != 1:
                raise ValueError(f"unknown job_id: {args.job_id}")
    print(canonical_json({"claims": len(pack["claims"]), "sources": len(pack["sources"]), "output": str(destination)}))
    return 0 if pack["claims"] else 2


def source_packs_build(args: argparse.Namespace, store: Any) -> int:
    attached = blocked = 0
    run_id = getattr(args, "run_id", None)
    run_filter = " AND created_run_id=?" if run_id else ""
    run_params: tuple[Any, ...] = (run_id,) if run_id else ()
    batch_id = getattr(args, "batch_id", None)
    batch_filter = " AND job_id IN (SELECT job_id FROM batch_requests WHERE batch_id=? AND status='completed')" if batch_id else ""
    batch_params: tuple[Any, ...] = (batch_id,) if batch_id else ()
    with store.connect() as connection:
        rows = connection.execute(
            f"""SELECT job_id,plan_json FROM content_jobs
               WHERE status IN ('planned','blocked_missing_sources') AND plan_json IS NOT NULL
                 AND (?=1 OR source_pack_json IS NULL OR status='blocked_missing_sources')
                 {run_filter}{batch_filter}
               ORDER BY job_id LIMIT ?""",
            (int(args.force), *run_params, *batch_params, args.limit),
        ).fetchall()
    for row in rows:
        plan = json.loads(row["plan_json"])
        terms = plan.get("source_pack_terms") or [plan["primary_keyword"]]
        retrieval_terms = list(dict.fromkeys([plan["primary_keyword"], *terms]))
        pack = build_source_pack(store, row["job_id"], retrieval_terms)
        missing_terms = missing_source_terms(pack, terms)
        model_tokens = [
            token.casefold()
            for token in re.findall(r"[a-z0-9-]+", plan.get("primary_keyword", "").casefold())
            if len(token) >= 4 and re.search(r"[a-z]", token) and re.search(r"\d", token)
        ]
        exact_model_verified = True
        if model_tokens:
            accepted_model_ids = {
                str((claim.get("conditions") or {}).get("model_identifier", "")).casefold()
                for claim in pack.get("claims", [])
                if claim.get("status") == "accepted" and claim.get("scope") == "model"
            }
            exact_model_verified = all(model_token in accepted_model_ids for model_token in model_tokens)
        missing_terms = list(dict.fromkeys(missing_terms))
        pack["coverage"] = {
            "requested_terms": terms,
            "uncovered_terms": missing_terms,
            "model_identifiers": model_tokens,
            "exact_model_verified": exact_model_verified,
        }
        pack["writing_constraints"] = [
            "Use only accepted claims in this source pack for factual assertions.",
            "Treat every uncovered evidence term as unknown rather than filling the gap by inference.",
        ]
        if model_tokens and not exact_model_verified:
            pack["writing_constraints"].append(
                "No exact-model source is present. Write an identifier-verification page: do not assert the model's identity, ratings, dimensions, terminals, compatibility, manufacturer, or application."
            )
        if not pack["claims"] or missing_terms:
            blocked += 1
            with store.connect() as connection:
                connection.execute(
                    "UPDATE content_jobs SET status='blocked_missing_sources',source_pack_json=?,validation_json=?,updated_at=? WHERE job_id=?",
                    (canonical_json(pack), canonical_json({"error": "source pack has uncovered center-topic terms", "terms": terms, "missing_terms": missing_terms}), now_iso(), row["job_id"]),
                )
            continue
        with store.connect() as connection:
            connection.execute("UPDATE content_jobs SET status='planned',source_pack_json=?,validation_json='{}',updated_at=? WHERE job_id=?", (canonical_json(pack), now_iso(), row["job_id"]))
        attached += 1
    print(canonical_json({"planned_jobs": len(rows), "source_packs_attached": attached, "blocked_missing_sources": blocked}))
    return 0 if blocked == 0 else 2


def review_enforce(args: argparse.Namespace, paths: Any, store: Any) -> int:
    """Require a passed review for the exact current article revision."""
    store.ensure_run(args.run_id)
    with store.connect() as connection:
        rows = connection.execute(
            """SELECT j.job_id,j.status,j.slug,j.article_json,j.plan_json,j.source_pack_json,j.validation_json,
                      sr.custom_id review_custom_id,
                      sr.passed review_passed,sr.review_json
               FROM content_jobs j LEFT JOIN semantic_reviews sr ON sr.job_id=j.job_id
               WHERE j.created_run_id=? AND j.article_json IS NOT NULL
               ORDER BY j.job_id""",
            (args.run_id,),
        ).fetchall()
    passed = failed = awaiting = retracted = 0
    now = now_iso()
    with store.connect() as connection:
        for row in rows:
            embedded = json.loads(row["validation_json"] or "{}")
            embedded_checks = embedded.get("checks") or {}
            if (
                embedded.get("gate") == "embedded_self_review_v1"
                and embedded.get("passed") is True
                and embedded_checks
                and all(value is True for value in embedded_checks.values())
            ):
                passed += 1
                next_status = row["status"] if row["status"] in {"rendered", "published"} else "validated"
                connection.execute(
                    "UPDATE content_jobs SET status=?,updated_at=? WHERE job_id=?",
                    (next_status, now, row["job_id"]),
                )
                continue
            version_material = (
                f"{args.run_id}:{row['job_id']}:review:{REQUEST_VERSION}:{REVIEW_GATE_VERSION}:"
                + sha256_bytes(row["article_json"].encode())
            )
            legacy_custom_id = f"msg-review-{REQUEST_VERSION}-{sha256_bytes(version_material.encode())[:16]}"
            expected_custom_ids = {legacy_custom_id}
            if row["plan_json"] and row["source_pack_json"]:
                payload = _review_payload(connection, row)
                expected_custom_ids.add(
                    _review_custom_id(args.run_id, row["job_id"], row["article_json"], payload)
                )
            exact_review = row["review_custom_id"] in expected_custom_ids
            approved = exact_review and bool(row["review_passed"])
            if approved:
                passed += 1
                next_status = row["status"] if row["status"] in {"rendered", "published"} else "validated"
                connection.execute("UPDATE content_jobs SET status=?,validation_json=?,updated_at=? WHERE job_id=?", (next_status, row["review_json"], now, row["job_id"]))
                continue
            if exact_review:
                failed += 1
                next_status = "semantic_review_failed"
                validation = row["review_json"] or "{}"
            else:
                awaiting += 1
                next_status = "awaiting_semantic_review"
                validation = "{}"
            if args.retract and row["status"] in {"rendered", "published"}:
                for post in paths.posts.glob(f"*-{row['slug']}.md"):
                    post.unlink()
                    retracted += 1
            connection.execute("UPDATE content_jobs SET status=?,validation_json=?,updated_at=? WHERE job_id=?", (next_status, validation, now, row["job_id"]))
    print(canonical_json({
        "run_id": args.run_id,
        "articles": len(rows),
        "passed_exact_revision": passed,
        "failed_exact_revision": failed,
        "awaiting_current_revision_review": awaiting,
        "retracted_posts": retracted,
    }))
    return 0


def publication_select(args: argparse.Namespace, store: Any) -> int:
    """Choose the exact publication cohort before links and rendering.

    The pilot intentionally generates reserve candidates.  Keeping every
    passed candidate in `validated` would let the selected pages link to a
    passed-but-unrendered reserve page.  Selection therefore precedes link
    reconciliation and rendering.
    """
    store.ensure_run(args.run_id)
    eligible_statuses = ("validated", "reserve_validated", "rendered", "published")
    placeholders = ",".join("?" for _ in eligible_statuses)
    with store.connect() as connection:
        rows = connection.execute(
            f"""SELECT j.job_id,j.status,COALESCE(k.search_volume,0) search_volume
                FROM content_jobs j JOIN keywords k ON k.keyword_id=j.keyword_id
                WHERE j.created_run_id=? AND j.status IN ({placeholders})
                  AND j.article_json IS NOT NULL AND j.duplicate_of_job_id IS NULL
                ORDER BY CASE WHEN j.status IN ('rendered','published') THEN 0 ELSE 1 END,
                         COALESCE(k.search_volume,0) DESC,j.job_id""",
            (args.run_id, *eligible_statuses),
        ).fetchall()
        locked = [row for row in rows if row["status"] in {"rendered", "published"}]
        if len(locked) > args.target:
            raise RuntimeError(f"publication target {args.target} is below {len(locked)} already rendered/published articles")
        if len(rows) < args.target:
            raise RuntimeError(f"publication target requires {args.target} accepted articles; only {len(rows)} are eligible")
        selected_ids = {row["job_id"] for row in rows[:args.target]}
        now = now_iso()
        promoted = reserved = 0
        for row in rows:
            if row["status"] in {"rendered", "published"}:
                continue
            next_status = "validated" if row["job_id"] in selected_ids else "reserve_validated"
            connection.execute(
                "UPDATE content_jobs SET status=?,updated_at=? WHERE job_id=?",
                (next_status, now, row["job_id"]),
            )
            promoted += int(next_status == "validated")
            reserved += int(next_status == "reserve_validated")
    result = {
        "run_id": args.run_id,
        "target": args.target,
        "eligible": len(rows),
        "selected": len(selected_ids),
        "already_rendered_or_published": len(locked),
        "promoted_to_validated": promoted,
        "retained_as_reviewed_reserve": reserved,
    }
    print(canonical_json(result))
    return 0


def render_run(args: argparse.Namespace, paths: Any, config: dict[str, Any], store: Any) -> int:
    publish_date = date.fromisoformat(args.date)
    rendered = skipped = failed = 0
    schema = load_json(paths.pipeline / "schemas" / "article.schema.json")
    (paths.root / "_posts").mkdir(parents=True, exist_ok=True)
    with store.connect() as connection:
        rows = connection.execute(
            """SELECT job_id,article_json FROM content_jobs
               WHERE created_run_id=? AND status='validated'
                 AND article_json IS NOT NULL AND duplicate_of_job_id IS NULL
               ORDER BY job_id LIMIT ?""",
            (args.run_id, args.limit),
        ).fetchall()
    for row in rows:
        article = json.loads(row["article_json"])
        errors = validate_schema(article, schema) + article_policy_errors(article, config)
        if errors:
            failed += 1
            with store.connect() as connection:
                connection.execute("UPDATE content_jobs SET status='validation_failed',validation_json=?,updated_at=? WHERE job_id=?", (canonical_json({"errors": errors}), now_iso(), row["job_id"]))
            continue
        destination = paths.root / "_posts" / f"{publish_date.isoformat()}-{article['slug']}.md"
        rendered_text = render_post(article, publish_date, config["site"]["author"], config["site"]["timezone"])
        if destination.exists():
            if destination.read_text(encoding="utf-8") == rendered_text:
                with store.connect() as connection:
                    connection.execute("UPDATE content_jobs SET status='rendered',updated_at=? WHERE job_id=?", (now_iso(), row["job_id"]))
                rendered += 1
            else:
                failed += 1
                with store.connect() as connection:
                    connection.execute("UPDATE content_jobs SET status='validation_failed',validation_json=?,updated_at=? WHERE job_id=?", (canonical_json({"errors": [f"existing post differs: {destination.name}"]}), now_iso(), row["job_id"]))
            continue
        destination.write_text(rendered_text, encoding="utf-8")
        with store.connect() as connection:
            connection.execute("UPDATE content_jobs SET status='rendered',updated_at=? WHERE job_id=?", (now_iso(), row["job_id"]))
        rendered += 1
    print(canonical_json({"jobs": len(rows), "rendered": rendered, "skipped_existing": skipped, "failed": failed}))
    return 1 if failed else 0


def batch_submit(args: argparse.Namespace, store: Any, credentials: dict[str, str]) -> int:
    store.ensure_run(args.run_id)
    rows = load_jsonl(args.input)
    custom_ids = [row.get("custom_id") for row in rows]
    if not rows or any(not value for value in custom_ids) or len(set(custom_ids)) != len(custom_ids):
        raise ValueError("batch input must contain unique custom_id values")
    with store.connect() as connection:
        known = {row[0] for row in connection.execute(f"SELECT custom_id FROM batch_requests WHERE custom_id IN ({','.join('?' for _ in custom_ids)})", custom_ids)}
    if known != set(custom_ids):
        raise ValueError("all batch requests must be prepared locally before submission")
    # Preflight remains available as an explicit diagnostic, but it is not a
    # paid production blocker. Deterministic schema and policy gates run again
    # at ingestion, and only failed items receive the single allowed repair.
    client = OpenAIClient(credentials["OPENAI_API_KEY"])
    uploaded = client.upload_batch_file(args.input)
    batch = client.create_batch(uploaded["id"], {"run_id": args.run_id, "kind": args.kind})
    with store.connect() as connection:
        connection.executemany("UPDATE batch_requests SET batch_id=?,input_file_id=?,status='submitted',updated_at=? WHERE custom_id=?", [(batch["id"], uploaded["id"], now_iso(), cid) for cid in custom_ids])
        submitted_status = {"plan": "plan_submitted", "article": "article_submitted", "review": "review_submitted"}.get(args.kind)
        if submitted_status:
            connection.execute(
                f"""UPDATE content_jobs SET status=?,updated_at=? WHERE job_id IN (
                    SELECT job_id FROM batch_requests WHERE custom_id IN ({','.join('?' for _ in custom_ids)}) AND job_id IS NOT NULL
                )""",
                (submitted_status, now_iso(), *custom_ids),
            )
    print(canonical_json({"batch_id": batch["id"], "input_file_id": uploaded["id"], "requests": len(rows), "status": batch.get("status")}))
    return 0


def batch_preflight(args: argparse.Namespace, paths: Any, config: dict[str, Any], store: Any, credentials: dict[str, str]) -> int:
    store.ensure_run(args.run_id)
    all_rows = load_jsonl(args.input)
    if len(all_rows) < 3:
        custom_ids = [row.get("custom_id") for row in all_rows]
        if not custom_ids or any(not value for value in custom_ids):
            raise ValueError("preflight requires at least three prepared requests")
        with store.connect() as connection:
            kinds = {
                row[0]
                for row in connection.execute(
                    f"SELECT kind FROM batch_requests WHERE custom_id IN ({','.join('?' for _ in custom_ids)})",
                    custom_ids,
                )
            }
            completed_article_jobs = connection.execute(
                "SELECT COUNT(*) FROM content_jobs WHERE created_run_id=? AND article_json IS NOT NULL",
                (args.run_id,),
            ).fetchone()[0]
        if kinds != {"repair"} and completed_article_jobs < 3:
            raise ValueError("preflight requires at least three prepared requests; only targeted repair requests may run with fewer")
    rows = all_rows[:3]
    client = OpenAIClient(credentials["OPENAI_API_KEY"])
    effective_kind = args.kind
    if args.kind == "repair":
        # `repair` covers both semantic article revisions and exact transport
        # retries. Follow the parent request when this is a transport retry.
        first_custom_id = rows[0].get("custom_id")
        with store.connect() as connection:
            request = connection.execute(
                "SELECT parent_custom_id FROM batch_requests WHERE custom_id=?",
                (first_custom_id,),
            ).fetchone()
            parent = connection.execute(
                "SELECT kind FROM batch_requests WHERE custom_id=?",
                (request["parent_custom_id"],),
            ).fetchone() if request and request["parent_custom_id"] else None
        effective_kind = parent["kind"] if parent and parent["kind"] in {"plan", "article", "review"} else "article"
    compact_article = effective_kind == "article" and args.kind == "article" and all(
        "-v10-" in str(row.get("custom_id", "")) for row in rows
    )
    response_schema = load_json(paths.pipeline / "schemas" / "article-draft.schema.json") if compact_article else schema_for_kind(paths.pipeline, effective_kind)
    final_schema = schema_for_kind(paths.pipeline, effective_kind)
    failures, results, raw_responses = 0, [], []
    prefix = rows[0]["body"]["input"][0]["content"][0]["text"]
    prefix_hash = sha256_bytes(prefix.encode())
    for row in rows:
        try:
            body = client.create_response(row["body"])
            raw_responses.append({"custom_id": row["custom_id"], "response": {"status_code": 200, "body": body}, "error": None})
            custom_id, output, error = extract_response_json({"custom_id": row["custom_id"], "response": {"status_code": 200, "body": body}})
            if effective_kind == "plan" and output is not None:
                output = normalize_plan_metadata(output)
            draft_errors: list[str] = []
            if effective_kind == "article" and output is not None:
                with store.connect() as connection:
                    request = connection.execute(
                        "SELECT job_id FROM batch_requests WHERE custom_id=?",
                        (custom_id,),
                    ).fetchone()
                    links = authoritative_internal_links(connection, request["job_id"]) if request and request["job_id"] else []
                    job = connection.execute(
                        "SELECT plan_json,source_pack_json FROM content_jobs WHERE job_id=?",
                        (request["job_id"],),
                    ).fetchone() if request and request["job_id"] else None
                if compact_article and job and job["plan_json"] and job["source_pack_json"]:
                    draft_errors = validate_schema(output, response_schema)
                    self_review = output.get("self_review") or {}
                    draft_errors.extend(
                        f"embedded self-review failed: {key}"
                        for key, value in self_review.items()
                        if value is not True
                    )
                    if not draft_errors:
                        output = assemble_article_draft(
                            output,
                            json.loads(job["plan_json"]),
                            json.loads(job["source_pack_json"]),
                            links,
                        )
                else:
                    output = apply_authoritative_internal_links(output, links)
            errors = list(draft_errors) if effective_kind == "article" and output is not None and compact_article else []
            if output is not None and not errors:
                errors.extend(validate_schema(output, final_schema))
            if effective_kind == "plan" and output is not None and not errors:
                from validators import plan_policy_errors
                errors.extend(plan_policy_errors(output, config))
            if effective_kind == "article" and output is not None and not errors:
                errors.extend(article_policy_errors(output, config))
            if error or errors:
                failures += 1
            results.append({"custom_id": custom_id, "ok": not error and not errors, "error": error, "validation_errors": errors, "usage": body.get("usage", {})})
            usage = body.get("usage") or {}
            if usage:
                rates = config["pricing_usd_per_million_tokens"]["gpt-6-luna_standard"]
                details = usage.get("input_tokens_details") or {}
                input_tokens = int(usage.get("input_tokens") or 0)
                cached_tokens = int(details.get("cached_tokens") or 0)
                cache_write_tokens = int(details.get("cache_write_tokens") or 0)
                output_tokens = int(usage.get("output_tokens") or 0)
                uncached = max(0, input_tokens - cached_tokens - cache_write_tokens)
                cost = (uncached * rates["input"] + cached_tokens * rates["cached_input"] + cache_write_tokens * rates["cache_write"] + output_tokens * rates["output"]) / 1_000_000
                store.record_cost(args.run_id, "openai", f"preflight_{args.kind}", cost, None, f"preflight:{custom_id}", input_tokens + output_tokens, {"usage": usage})
        except Exception as exc:
            failures += 1
            results.append({"custom_id": row["custom_id"], "ok": False, "error": str(exc)[:500]})
            raw_responses.append({"custom_id": row["custom_id"], "response": None, "error": {"code": "preflight_exception", "message": str(exc)[:500]}})
    status = "complete" if failures == 0 and len(rows) == min(3, len(all_rows)) else "failed"
    local_id = f"{args.kind}:{prefix_hash}"
    with store.connect() as connection:
        connection.execute("""INSERT INTO provider_objects(provider,object_type,local_id,status,payload_sha256,metadata_json,created_at,updated_at)
            VALUES('openai','preflight',?,?,?,?,?,?)
            ON CONFLICT(provider,object_type,local_id) DO UPDATE SET
              status=CASE WHEN provider_objects.status='complete' OR excluded.status='complete' THEN 'complete' ELSE excluded.status END,
              metadata_json=excluded.metadata_json,updated_at=excluded.updated_at""", (local_id, status, prefix_hash, canonical_json({"run_id": args.run_id, "results": results}), now_iso(), now_iso()))
    if args.output:
        write_jsonl(args.output, raw_responses)
    print(json.dumps({"kind": args.kind, "checked": len(rows), "failures": failures, "status": status, "results": results}, indent=2))
    return 0 if status == "complete" else 1


def batch_submit_dir(args: argparse.Namespace, store: Any, credentials: dict[str, str]) -> int:
    manifest_path = args.input_dir / "manifest.json"
    manifest = load_json(manifest_path)
    if manifest.get("run_id") != args.run_id or manifest.get("kind") != args.kind:
        raise ValueError("manifest run_id or kind does not match command")
    submitted = []
    for item in manifest.get("files", []):
        child = argparse.Namespace(run_id=args.run_id, input=Path(item["path"]), kind=args.kind)
        batch_submit(child, store, credentials)
        submitted.append(item["path"])
    print(canonical_json({"submitted_files": len(submitted), "run_id": args.run_id, "kind": args.kind}))
    return 0


def build_batches_action(args: argparse.Namespace, paths: Any, config: dict[str, Any], store: Any, skill_text: str, skill_hash: str) -> int:
    store.ensure_run(args.run_id)
    inputs = load_jsonl(args.input)
    if len(inputs) > config["program"]["daily_job_limit"]:
        raise ValueError(f"daily job limit is {config['program']['daily_job_limit']}")
    if not 1 <= args.chunk_size <= config["batch"]["requests_per_file"]:
        raise ValueError(f"chunk size must be 1-{config['batch']['requests_per_file']}")
    schema = load_json(paths.pipeline / "schemas" / "article-draft.schema.json") if args.kind == "article" else schema_for_kind(paths.pipeline, args.kind)
    model = args.model or config["models"]["generation"]
    max_tokens = 4500 if args.kind == "article" else (1500 if args.kind == "review" else 2500)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    manifest = []
    for index, offset in enumerate(range(0, len(inputs), args.chunk_size), 1):
        chunk = inputs[offset:offset + args.chunk_size]
        rows = build_batch_requests(args.kind, chunk, model, skill_text, schema, max_tokens)
        destination = args.output_dir / f"{args.kind}-{index:03d}.jsonl"
        result = write_batch(destination, rows)
        with store.connect() as connection:
            for source, row in zip(chunk, rows):
                input_hash = sha256_bytes(canonical_json(row).encode())
                existing = connection.execute("SELECT input_sha256 FROM batch_requests WHERE custom_id=?", (row["custom_id"],)).fetchone()
                if existing and existing["input_sha256"] != input_hash:
                    raise ValueError(f"custom_id already exists with different input: {row['custom_id']}")
                connection.execute("INSERT INTO batch_requests(custom_id,run_id,kind,job_id,endpoint,model,input_sha256,status,created_at,updated_at) VALUES(?,?,?,?,?,?,?,?,?,?) ON CONFLICT(custom_id) DO UPDATE SET updated_at=excluded.updated_at", (row["custom_id"], args.run_id, args.kind, source.get("job_id") or (source.get("payload") or {}).get("job_id"), "/v1/responses", model, input_hash, "prepared", now_iso(), now_iso()))
        manifest.append(result)
    manifest_path = args.output_dir / "manifest.json"
    manifest_path.write_text(json.dumps({"run_id": args.run_id, "kind": args.kind, "model": model, "skill_hash": skill_hash, "input_requests": len(inputs), "files": manifest}, indent=2) + "\n", encoding="utf-8")
    print(canonical_json({"requests": len(inputs), "batch_files": len(manifest), "manifest": str(manifest_path)}))
    return 0


def batch_status(args: argparse.Namespace, paths: Any, store: Any, credentials: dict[str, str]) -> int:
    client = OpenAIClient(credentials["OPENAI_API_KEY"])
    batch = client.get_batch(args.batch_id)
    status = batch.get("status", "unknown")
    output_paths = {}
    for label, key in (("output", "output_file_id"), ("errors", "error_file_id")):
        file_id = batch.get(key)
        if file_id:
            destination = paths.outputs / f"batch-{args.batch_id}-{label}.jsonl"
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(client.download_file(file_id))
            output_paths[label] = str(destination)
    with store.connect() as connection:
        connection.execute("UPDATE batch_requests SET status=?,output_file_id=?,error_file_id=?,updated_at=? WHERE batch_id=?", (status, batch.get("output_file_id"), batch.get("error_file_id"), now_iso(), args.batch_id))
    print(canonical_json({"batch_id": args.batch_id, "status": status, "files": output_paths, "request_counts": batch.get("request_counts")}))
    return 0 if status not in {"failed", "expired", "cancelled"} else 1


def batch_retry(args: argparse.Namespace, config: dict[str, Any], store: Any) -> int:
    original = {row["custom_id"]: row for row in load_jsonl(args.input)}
    retries = []
    with store.connect() as connection:
        failed = connection.execute(
            """SELECT parent.* FROM batch_requests parent
               WHERE parent.run_id=? AND parent.status IN ('failed','expired')
                 AND NOT EXISTS (
                   SELECT 1 FROM content_jobs accepted
                   WHERE accepted.job_id=parent.job_id
                     AND accepted.status IN ('validated','rendered','published')
                 )
                 AND NOT EXISTS (
                   SELECT 1 FROM batch_requests child
                   WHERE child.parent_custom_id=parent.custom_id
                     AND child.status IN ('prepared','submitted','validating','in_progress','finalizing','completed')
                 )""",
            (args.run_id,),
        ).fetchall()
        for row in failed:
            if row["custom_id"] not in original:
                continue
            request = json.loads(canonical_json(original[row["custom_id"]]))
            failure = json.loads(row["error_json"] or "{}")
            is_content_failure = (
                row["kind"] == "article"
                and "-v10-" in row["custom_id"]
                and failure.get("code") == "validation_failed"
            )
            if is_content_failure:
                prior_revisions = connection.execute(
                    "SELECT COUNT(*) FROM batch_requests WHERE parent_custom_id=? AND custom_id LIKE ?",
                    (row["custom_id"], row["custom_id"] + "-s%"),
                ).fetchone()[0]
                if prior_revisions >= config["batch"]["content_revision_retries"]:
                    continue
                retry_count = prior_revisions + 1
                request["custom_id"] = f"{row['custom_id']}-s{retry_count}"
                messages = request.get("body", {}).get("input", [])
                if messages and messages[-1].get("role") == "user":
                    payload = json.loads(messages[-1].get("content") or "{}")
                    payload["repair_errors"] = failure.get("errors", [])
                    payload["repair_instruction"] = "Correct every listed error in one final revision, rerun the four self-review checks, and return the compact response schema."
                    messages[-1]["content"] = canonical_json(payload)
            else:
                prior_retries = connection.execute(
                    "SELECT COUNT(*) FROM batch_requests WHERE parent_custom_id=? AND custom_id LIKE ?",
                    (row["custom_id"], row["custom_id"] + "-r%"),
                ).fetchone()[0]
                if prior_retries >= config["batch"]["transport_retries"]:
                    continue
                retry_count = prior_retries + 1
                request["custom_id"] = f"{row['custom_id']}-r{retry_count}"
                # Transport retries resend the exact same body. They recover
                # provider failures and never become content rewrites.
            retries.append(request)
            connection.execute("INSERT INTO batch_requests(custom_id,run_id,kind,job_id,endpoint,model,input_sha256,status,parent_custom_id,retry_count,created_at,updated_at) VALUES(?,?,?,?,?,?,?,?,?,?,?,?) ON CONFLICT(custom_id) DO NOTHING", (request["custom_id"], args.run_id, "repair", row["job_id"], row["endpoint"], row["model"], sha256_bytes(canonical_json(request).encode()), "prepared", row["custom_id"], retry_count, now_iso(), now_iso()))
    result = write_batch(args.output, retries)
    print(canonical_json(result | {"retry_requests": len(retries)}))
    return 0


def semantic_repair_prepare(args: argparse.Namespace, config: dict[str, Any], store: Any) -> int:
    original = {row["custom_id"]: row for row in load_jsonl(args.input)}
    repairs = []
    now = now_iso()
    with store.connect() as connection:
        jobs = connection.execute(
            """SELECT j.job_id,j.article_json,s.review_json
               FROM content_jobs j JOIN semantic_reviews s ON s.job_id=j.job_id
               WHERE j.created_run_id=? AND j.status='semantic_review_failed'
                 AND j.article_json IS NOT NULL AND s.passed=0
               ORDER BY j.job_id""",
            (args.run_id,),
        ).fetchall()
        for job in jobs:
            parent = connection.execute(
                """SELECT * FROM batch_requests
                   WHERE job_id=? AND run_id=? AND kind='article'
                   ORDER BY updated_at DESC, created_at DESC LIMIT 1""",
                (job["job_id"], args.run_id),
            ).fetchone()
            if not parent or parent["custom_id"] not in original:
                continue
            prior = connection.execute(
                "SELECT custom_id,status FROM batch_requests WHERE parent_custom_id=? AND custom_id LIKE ? ORDER BY custom_id",
                (parent["custom_id"], parent["custom_id"] + "-s%"),
            ).fetchall()
            # A completed repair may still fail the subsequent adversarial review.
            # Block only work that is still active; completed attempts count toward
            # content_revision_retries below and may be followed by the next bounded repair.
            if any(row["status"] in {"prepared", "submitted", "validating", "in_progress", "finalizing"} for row in prior):
                continue
            attempt = len(prior) + 1
            if attempt > config["batch"]["content_revision_retries"]:
                continue
            request = json.loads(canonical_json(original[parent["custom_id"]]))
            request["custom_id"] = f"{parent['custom_id']}-s{attempt}"
            # A semantic failure can expose a defect in the approved plan
            # itself (for example, a title promising a mechanism that the
            # attached source pack does not establish).  The ordinary article
            # contract correctly freezes an approved plan, but a bounded
            # semantic repair must be able to narrow that plan instead of
            # repeatedly reproducing the same unsupported promise.
            repair_override = """

# Semantic-repair override
- Preserve primary_keyword and slug exactly. Title and H1 must remain identical and contain the complete primary keyword.
- You may revise title, H1, description, owned_question, category, headings, and the article angle when the adversarial review shows that the prior plan promised facts absent from the source pack.
- When central topic-specific evidence is absent, turn the page into a useful evidence-boundary or identifier-verification task. State what the supplied evidence establishes, what remains unresolved, and exactly which documentation fields must be checked. Do not assert even a plausible mechanism, application, symptom, fit criterion, or safety instruction unless an accepted claim establishes it.
- Keep 3-8 supplied internal links, but omit unrelated links or links that introduce an unapproved model identifier. Every returned internal_links URL must occur exactly once in body_markdown.
- Reframe every H2 so its promise can be fully answered from accepted claims or explicit evidence boundaries. Delete tangents and duplicated neighboring questions.
- The repaired metadata and body are the revised approved plan and must be mutually consistent.
""".rstrip()
            developer_input = request.get("body", {}).get("input", [])
            if developer_input:
                developer_content = developer_input[0].get("content")
                if isinstance(developer_content, list) and developer_content:
                    developer_content[-1]["text"] = str(developer_content[-1].get("text", "")).rstrip() + "\n" + repair_override
                    prefix = developer_content[-1]["text"]
                    request["body"]["prompt_cache_key"] = f"microswitchguide:semantic-repair:{sha256_bytes(prefix.encode('utf-8'))[:20]}"
            feedback = {
                "semantic_review": json.loads(job["review_json"]),
                "current_article": json.loads(job["article_json"]),
            }
            contents = request.get("body", {}).get("input", [])
            if contents and contents[-1].get("role") == "user":
                text_content = contents[-1].get("content")
                addition = (
                    "\n\nRevise the current article to fix every adversarial review failure. "
                    "Preserve valid material, use only the supplied source pack, and return the complete repaired article. "
                    "If the old plan itself is unsupported, use the semantic-repair override to narrow its promises and make the metadata, owned question, headings, and body agree. "
                    "The repaired body must contain 1,000-2,000 English words. Keep the explanation as concise as the topic allows. "
                    "Keep 3-4 genuinely relevant supplied internal links exactly once, but remove unrelated links and any link that introduces another model identifier. "
                    "Do not introduce claims beyond the supplied claim IDs: "
                    + canonical_json(feedback)
                )
                if isinstance(text_content, str):
                    contents[-1]["content"] = text_content + addition
                elif isinstance(text_content, list) and text_content:
                    text_content[-1]["text"] = str(text_content[-1].get("text", "")) + addition
            repairs.append(request)
            connection.execute(
                """INSERT INTO batch_requests(custom_id,run_id,kind,job_id,endpoint,model,input_sha256,status,parent_custom_id,retry_count,created_at,updated_at)
                   VALUES(?,?,?,?,?,?,?,?,?,?,?,?)""",
                (request["custom_id"], args.run_id, "repair", job["job_id"], parent["endpoint"], parent["model"], sha256_bytes(canonical_json(request).encode()), "prepared", parent["custom_id"], attempt, now, now),
            )
    result = write_batch(args.output, repairs)
    print(canonical_json(result | {"semantic_repair_requests": len(repairs)}))
    return 0


def links_build(args: argparse.Namespace, paths: Any, config: dict[str, Any], store: Any) -> int:
    with store.connect() as connection:
        scope = "j.created_run_id=?"
        scope_params: tuple[Any, ...] = (args.run_id,)
        if getattr(args, "source_batch_id", None):
            # Include every request in the provider batch. Failed ingestion is
            # exactly when the derived link graph may need to be rebuilt.
            scope = "EXISTS (SELECT 1 FROM batch_requests br WHERE br.job_id=j.job_id AND br.batch_id=?)"
            scope_params = (args.source_batch_id,)
        rows = []
        for row in connection.execute(
            """SELECT j.job_id,j.title,j.category,j.owned_question,j.status,j.plan_json,k.keyword AS primary_keyword
               FROM content_jobs j JOIN keywords k ON k.keyword_id=j.keyword_id
               WHERE """ + scope + """
                 AND j.status IN ('planned','article_submitted','validated','rendered','published')
                 AND j.plan_json IS NOT NULL AND j.source_pack_json IS NOT NULL
                 AND j.duplicate_of_job_id IS NULL ORDER BY j.job_id LIMIT ?""",
            (*scope_params, args.limit),
        ):
            item = dict(row)
            item["page_type"] = json.loads(row["plan_json"]).get("page_type") if row["plan_json"] else None
            rows.append(item)
    links = build_internal_links(rows, config["program"]["internal_links_min"], config["program"]["internal_links_max"])
    with store.connect() as connection:
        # The graph is derived state. Replace it atomically so links to jobs
        # that later fail review cannot remain marked valid after a rebuild.
        if getattr(args, "source_batch_id", None):
            connection.execute(
                """DELETE FROM internal_links
                   WHERE source_job_id IN (
                     SELECT job_id FROM batch_requests WHERE batch_id=?
                   )""",
                (args.source_batch_id,),
            )
        else:
            connection.execute(
                """DELETE FROM internal_links
                   WHERE source_job_id IN (
                     SELECT job_id FROM content_jobs WHERE created_run_id=?
                   )""",
                (args.run_id,),
            )
        for link in links:
            connection.execute("INSERT INTO internal_links(source_job_id,target_job_id,relation,anchor_text,status) VALUES(?,?,?,?,?) ON CONFLICT(source_job_id,target_job_id) DO UPDATE SET relation=excluded.relation,anchor_text=excluded.anchor_text,status=excluded.status", tuple(link[key] for key in ("source_job_id", "target_job_id", "relation", "anchor_text", "status")))
    destination = args.output or paths.outputs / "internal-links.jsonl"
    write_jsonl(destination, links)
    print(canonical_json({"jobs": len(rows), "links": len(links), "output": str(destination)}))
    return 0


def links_reconcile(args: argparse.Namespace, config: dict[str, Any], store: Any) -> int:
    """Make every generated article link resolve inside the accepted batch.

    Generation can race ahead of a target article that later fails.  Replace
    only those unavailable targets, preserving the number and placement of
    links so the prose and exact-keyword layout remain stable.
    """
    accepted_statuses = ("validated", "rendered", "published")
    placeholders = ",".join("?" for _ in accepted_statuses)
    with store.connect() as connection:
        run_scope = "" if getattr(args, "all_accepted", False) else "j.created_run_id=? AND"
        run_params: tuple[Any, ...] = () if getattr(args, "all_accepted", False) else (args.run_id,)
        rows = connection.execute(
            f"""SELECT j.job_id,j.status,j.slug,j.category,j.article_json,j.plan_json,k.keyword
                FROM content_jobs j JOIN keywords k ON k.keyword_id=j.keyword_id
                WHERE {run_scope} j.status IN ({placeholders})
                  AND j.duplicate_of_job_id IS NULL AND j.article_json IS NOT NULL
                ORDER BY j.job_id""",
            (*run_params, *accepted_statuses),
        ).fetchall()
    accepted = {row["job_id"]: dict(row) for row in rows}
    rewritten_articles = replaced_links = 0
    now = now_iso()
    with store.connect() as connection:
        for row in rows:
            article = json.loads(row["article_json"])
            links = list(article.get("internal_links", []))
            used = {link.get("target_job_id") for link in links if link.get("target_job_id") in accepted}
            candidates = [
                candidate for candidate in rows
                if candidate["job_id"] != row["job_id"]
                and candidate["job_id"] not in used
            ]
            candidates.sort(key=lambda item: (
                item["category"] != row["category"],
                bool(re.search(r"\d", item["keyword"] or "")),
                item["keyword"].casefold(),
                item["job_id"],
            ))
            body = article.get("body_markdown", "")
            changed = False
            new_links = []
            for link in links:
                target = accepted.get(link.get("target_job_id"))
                expected_url = f"/guides/{target['slug']}/" if target else None
                if target and link.get("url") == expected_url:
                    new_links.append(link)
                    continue
                old_anchor_words = len(re.findall(r"[A-Za-z0-9]+(?:['’-][A-Za-z0-9]+)*", str(link.get("anchor_text", ""))))
                eligible = [item for item in candidates if item["job_id"] not in used]
                eligible.sort(key=lambda item: (
                    len(re.findall(r"[A-Za-z0-9]+(?:['’-][A-Za-z0-9]+)*", item["keyword"] or "")) < old_anchor_words,
                    item["category"] != row["category"],
                    bool(re.search(r"\d", item["keyword"] or "")),
                    item["keyword"].casefold(),
                    item["job_id"],
                ))
                replacement = eligible[0] if eligible else None
                if replacement is None:
                    raise RuntimeError(f"no accepted replacement link is available for {row['job_id']}")
                used.add(replacement["job_id"])
                anchor = replacement["keyword"]
                replacement_url = f"/guides/{replacement['slug']}/"
                old_markdown = f"[{link.get('anchor_text', '')}]({link.get('url', '')})"
                new_markdown = f"[{anchor}]({replacement_url})"
                if old_markdown in body:
                    body = body.replace(old_markdown, new_markdown, 1)
                else:
                    # The prose generator may capitalize or lightly restyle an
                    # anchor while preserving its planned URL.  The URL is the
                    # stable link identity, so reconcile by URL before treating
                    # the structured/body mismatch as a missing link.
                    url_pattern = re.compile(
                        r"\[[^\]]+\]\(" + re.escape(str(link.get("url", ""))) + r"\)"
                    )
                    if not url_pattern.search(body):
                        raise RuntimeError(
                            f"article body is missing the stored link URL {link.get('url')!r} "
                            f"for {row['job_id']}"
                        )
                    body = url_pattern.sub(lambda _match: new_markdown, body, count=1)
                new_links.append({
                    "target_job_id": replacement["job_id"],
                    "relation": "supporting" if replacement["category"] == row["category"] else "related",
                    "anchor_text": anchor,
                    "url": replacement_url,
                })
                replaced_links += 1
                changed = True
            if not changed:
                continue
            article["body_markdown"] = body
            article["internal_links"] = new_links
            errors = article_policy_errors(article, config)
            if errors:
                raise RuntimeError(f"link reconciliation made {row['job_id']} invalid: {errors}")
            plan = json.loads(row["plan_json"]) if row["plan_json"] else None
            if plan is not None:
                plan["internal_link_targets"] = [link["target_job_id"] for link in new_links]
            connection.execute(
                "UPDATE content_jobs SET article_json=?,plan_json=COALESCE(?,plan_json),updated_at=? WHERE job_id=?",
                (canonical_json(article), canonical_json(plan) if plan is not None else None, now, row["job_id"]),
            )
            rewritten_articles += 1
    print(canonical_json({
        "run_id": args.run_id,
        "accepted_articles": len(rows),
        "rewritten_articles": rewritten_articles,
        "replaced_links": replaced_links,
    }))
    return 0


def articles_export(args: argparse.Namespace, store: Any) -> int:
    with store.connect() as connection:
        statuses = getattr(args, "status", None) or []
        run_id = getattr(args, "run_id", None)
        run_filter = " AND created_run_id=?" if run_id else ""
        run_params: tuple[Any, ...] = (run_id,) if run_id else ()
        if statuses:
            placeholders = ",".join("?" for _ in statuses)
            rows = connection.execute(
                f"SELECT job_id,article_json FROM content_jobs WHERE article_json IS NOT NULL AND status IN ({placeholders}){run_filter} ORDER BY job_id LIMIT ?",
                (*statuses, *run_params, args.limit),
            ).fetchall()
        else:
            rows = connection.execute(
                f"SELECT job_id,article_json FROM content_jobs WHERE article_json IS NOT NULL{run_filter} ORDER BY job_id LIMIT ?",
                (*run_params, args.limit),
            ).fetchall()
    output = []
    for row in rows:
        article = json.loads(row["article_json"])
        article["job_id"] = row["job_id"]
        output.append(article)
    write_jsonl(args.output, output)
    print(canonical_json({"exported": len(output), "output": str(args.output)}))
    return 0


def dedupe_articles(args: argparse.Namespace, paths: Any, config: dict[str, Any], store: Any) -> int:
    articles = load_jsonl(args.input)
    seen_slugs, seen_questions = {}, {}
    fingerprints: dict[str, tuple[int, tuple[int, ...]]] = {}
    simhash_buckets: dict[tuple[int, int], set[str]] = {}
    minhash_buckets: dict[tuple[int, tuple[int, ...]], set[str]] = {}
    results = []
    max_distance = config["similarity"]["simhash_max_distance"]
    min_similarity = config["similarity"]["minhash_min_similarity"]
    for article in articles:
        duplicate_of = None
        reasons = []
        slug = article.get("slug", "")
        question = article.get("owned_question", "").casefold().strip()
        body = article.get("body_markdown", "")
        fingerprint = simhash(body)
        minhash = minhash_signature(body)
        if slug in seen_slugs:
            duplicate_of, reasons = seen_slugs[slug], ["duplicate_slug"]
        elif question in seen_questions:
            duplicate_of, reasons = seen_questions[question], ["duplicate_owned_question"]
        else:
            candidates: set[str] = set()
            for band in range(8):
                candidates.update(simhash_buckets.get((band, (fingerprint >> (band * 8)) & 0xFF), set()))
            for band in range(16):
                start = band * 4
                candidates.update(minhash_buckets.get((band, minhash[start:start + 4]), set()))
            for prior_id in sorted(candidates):
                prior_fingerprint, prior_minhash = fingerprints[prior_id]
                distance = (fingerprint ^ prior_fingerprint).bit_count()
                if distance <= max_distance:
                    duplicate_of, reasons = prior_id, [f"simhash_distance:{distance}"]
                    break
                similarity = minhash_similarity(minhash, prior_minhash)
                if similarity >= min_similarity:
                    duplicate_of, reasons = prior_id, [f"minhash_similarity:{similarity:.4f}"]
                    break
        article_id = article.get("job_id") or stable_id("article", slug or question or canonical_json(article))
        seen_slugs.setdefault(slug, article_id)
        seen_questions.setdefault(question, article_id)
        fingerprints[article_id] = (fingerprint, minhash)
        for band in range(8):
            simhash_buckets.setdefault((band, (fingerprint >> (band * 8)) & 0xFF), set()).add(article_id)
        for band in range(16):
            start = band * 4
            minhash_buckets.setdefault((band, minhash[start:start + 4]), set()).add(article_id)
        results.append({"job_id": article_id, "duplicate_of": duplicate_of, "reasons": reasons, "fingerprint": f"{fingerprint:016x}", "minhash": [f"{value:016x}" for value in minhash]})
    destination = args.output or paths.outputs / "dedupe-results.jsonl"
    write_jsonl(destination, results)
    if args.apply:
        with store.connect() as connection:
            for row in results:
                if row["duplicate_of"]:
                    connection.execute("UPDATE content_jobs SET duplicate_of_job_id=?,status='duplicate',text_fingerprint=?,updated_at=? WHERE job_id=?", (row["duplicate_of"], row["fingerprint"], now_iso(), row["job_id"]))
                else:
                    connection.execute("UPDATE content_jobs SET text_fingerprint=?,updated_at=? WHERE job_id=?", (row["fingerprint"], now_iso(), row["job_id"]))
    print(canonical_json({"articles": len(results), "duplicates": sum(bool(row["duplicate_of"]) for row in results), "output": str(destination)}))
    return 0


def dedupe_semantic(args: argparse.Namespace, config: dict[str, Any], store: Any, credentials: dict[str, str]) -> int:
    rows = load_jsonl(args.input)
    threshold = args.threshold or config["similarity"]["near_duplicate"]
    clusters = cluster_vectors(rows, threshold)
    output = []
    by_id = {str(row["id"]): row for row in rows}
    for cluster in clusters:
        owner = cluster[0]["id"]
        for index, item in enumerate(cluster):
            score = cosine_similarity(cluster[0]["vector"], item["vector"])
            output.append({"id": item["id"], "job_id": item.get("job_id", item["id"]), "granularity": item.get("granularity", "article"), "duplicate_of": owner if index else None, "cluster_owner": owner, "similarity": score, "threshold": threshold, "source": "current_input"})
    # Query Qdrant after upsert so the same operation also checks against the
    # previously accepted corpus. Current-input pairs are already handled by
    # deterministic local clustering above.
    external_by_id: dict[str, tuple[str, str, float]] = {}
    if rows and credentials.get("QDRANT_URL") and credentials.get("QDRANT_API_KEY"):
        qdrant = QdrantClient(credentials["QDRANT_URL"], credentials["QDRANT_API_KEY"])
        current_ids = set(by_id)
        for offset in range(0, len(rows), 64):
            chunk = rows[offset:offset + 64]
            batches = qdrant.query_batch(
                config["qdrant"]["collections"][args.object_type],
                [row["vector"] for row in chunk],
                limit=config["similarity"]["neighbors"],
                score_threshold=threshold,
            )
            for row, neighbors in zip(chunk, batches):
                for neighbor in neighbors:
                    payload = neighbor.get("payload") or {}
                    neighbor_id = str(payload.get("local_id") or "")
                    if not neighbor_id or neighbor_id == str(row["id"]) or neighbor_id in current_ids:
                        continue
                    if payload.get("granularity", "article") != row.get("granularity", "article"):
                        continue
                    neighbor_job = str(payload.get("job_id") or neighbor_id.split(":section:", 1)[0])
                    if neighbor_job == str(row.get("job_id", row["id"])):
                        continue
                    with store.connect() as connection:
                        accepted = connection.execute(
                            "SELECT 1 FROM content_jobs WHERE job_id=? AND status IN ('validated','reserve_validated','rendered','published')",
                            (neighbor_job,),
                        ).fetchone()
                    if accepted:
                        score = float(neighbor.get("score") or 0.0)
                        previous = external_by_id.get(str(row["id"]))
                        if previous is None or score > previous[2]:
                            external_by_id[str(row["id"])] = (neighbor_id, neighbor_job, score)
                        break
    output_by_id = {str(item["id"]): item for item in output}
    for item_id, (neighbor_id, neighbor_job, score) in external_by_id.items():
        item = output_by_id[item_id]
        if not item["duplicate_of"]:
            item.update({"duplicate_of": neighbor_id, "duplicate_of_job_id": neighbor_job, "similarity": score, "source": "qdrant_existing_corpus"})
    write_jsonl(args.output, output)
    if args.apply:
        with store.connect() as connection:
            for row in output:
                if row["duplicate_of"] and row.get("granularity") in {"article", "plan"}:
                    duplicate_job = row.get("duplicate_of_job_id") or by_id.get(str(row["duplicate_of"]), {}).get("job_id") or row["duplicate_of"]
                    connection.execute("UPDATE content_jobs SET duplicate_of_job_id=?,status='duplicate',semantic_score=?,updated_at=? WHERE job_id=?", (duplicate_job, row["similarity"], now_iso(), row["job_id"]))
    duplicate_count = sum(bool(row["duplicate_of"]) for row in output)
    granularities = sorted({row.get("granularity", "article") for row in rows}) or ["article"]
    if args.run_id:
        with store.connect() as connection:
            for granularity in granularities:
                count = sum(bool(row["duplicate_of"]) for row in output if row.get("granularity", "article") == granularity)
                local_id = f"{args.run_id}:{granularity}"
                metadata = {"run_id": args.run_id, "granularity": granularity, "items": sum(row.get("granularity", "article") == granularity for row in output), "duplicates": count, "threshold": threshold, "output": str(args.output)}
                connection.execute(
                    """INSERT INTO provider_objects(provider,object_type,local_id,status,metadata_json,created_at,updated_at)
                       VALUES('local','semantic_dedupe',?,'complete',?,?,?)
                       ON CONFLICT(provider,object_type,local_id) DO UPDATE SET status='complete',metadata_json=excluded.metadata_json,updated_at=excluded.updated_at""",
                    (local_id, canonical_json(metadata), now_iso(), now_iso()),
                )
    print(canonical_json({"items": len(rows), "semantic_clusters": len(clusters), "duplicates": duplicate_count, "qdrant_external_duplicates": len(external_by_id), "granularities": granularities, "output": str(args.output)}))
    return 0


def write_report(args: argparse.Namespace, paths: Any, store: Any) -> int:
    report = report_for_run(store, args.run_id)
    destination = args.output or paths.outputs / f"{args.run_id}-report.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with store.connect() as connection:
        connection.execute("INSERT INTO run_reports(run_id,report_json,created_at,updated_at) VALUES(?,?,?,?) ON CONFLICT(run_id) DO UPDATE SET report_json=excluded.report_json,updated_at=excluded.updated_at", (args.run_id, canonical_json(report), now_iso(), now_iso()))
    print(canonical_json({"output": str(destination), **report}))
    return 0


def benchmark_pipeline(args: argparse.Namespace, paths: Any) -> int:
    invalid = [size for size in args.sizes if size <= 0 or size > 10_000]
    if invalid:
        raise ValueError(f"benchmark sizes must be between 1 and 10,000: {invalid}")
    results = []
    with tempfile.TemporaryDirectory(prefix="msg-benchmark-", dir=paths.root / "work") as directory:
        base = Path(directory)
        for size in args.sizes:
            rows = [{"id": f"bench-{index}", "keyword": f"micro switch benchmark topic {index}", "status": "planned"} for index in range(size)]
            started = time.perf_counter()
            jsonl_path = base / f"{size}.jsonl"
            write_jsonl(jsonl_path, rows)
            jsonl_seconds = time.perf_counter() - started

            started = time.perf_counter()
            database = base / f"{size}.db"
            connection = sqlite3.connect(database)
            connection.execute("CREATE TABLE bench(id TEXT PRIMARY KEY, keyword TEXT NOT NULL, status TEXT NOT NULL)")
            connection.executemany("INSERT INTO bench VALUES(:id,:keyword,:status)", rows)
            connection.commit()
            sqlite_seconds = time.perf_counter() - started
            count = connection.execute("SELECT COUNT(*) FROM bench").fetchone()[0]
            connection.close()

            started = time.perf_counter()
            posts_dir = base / f"posts-{size}"
            posts_dir.mkdir()
            template = "---\nlayout: post\ntitle: Micro Switch Benchmark {index}\n---\n\nBenchmark content {index}.\n"
            for index in range(size):
                (posts_dir / f"2026-01-01-micro-switch-benchmark-{index}.md").write_text(template.format(index=index), encoding="utf-8")
            render_seconds = time.perf_counter() - started
            results.append({
                "size": size, "jsonl_seconds": round(jsonl_seconds, 4), "sqlite_seconds": round(sqlite_seconds, 4),
                "render_seconds": round(render_seconds, 4), "sqlite_rows": count,
                "jsonl_bytes": jsonl_path.stat().st_size, "rendered_files": size,
            })
    output = {"benchmarks": results, "note": "Qdrant latency is measured separately by providers-smoke-test and production query telemetry."}
    destination = args.output or paths.outputs / "scale-benchmark.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(destination), **output}, indent=2))
    return 0


def acceptance_check(args: argparse.Namespace, paths: Any, config: dict[str, Any], store: Any) -> int:
    report = report_for_run(store, args.run_id)
    with store.connect() as connection:
        rendered = connection.execute("SELECT COUNT(*) FROM content_jobs WHERE created_run_id=? AND status IN ('rendered','published')", (args.run_id,)).fetchone()[0]
        duplicates = connection.execute("SELECT COUNT(*) FROM content_jobs WHERE created_run_id=? AND duplicate_of_job_id IS NOT NULL AND status IN ('validated','rendered','published')", (args.run_id,)).fetchone()[0]
        duplicate_slugs = connection.execute(
            """SELECT COUNT(*) FROM (
                 SELECT slug FROM content_jobs
                 WHERE created_run_id=? AND slug IS NOT NULL
                 GROUP BY slug HAVING COUNT(*)>1
               )""",
            (args.run_id,),
        ).fetchone()[0]
        duplicate_custom_ids = connection.execute(
            """SELECT COUNT(*) FROM (
                 SELECT custom_id FROM batch_requests
                 WHERE run_id=? GROUP BY custom_id HAVING COUNT(*)>1
               )""",
            (args.run_id,),
        ).fetchone()[0]
        dataforseo_spend = float(connection.execute(
            "SELECT COALESCE(SUM(amount_usd),0) FROM api_costs WHERE run_id=? AND provider='dataforseo'",
            (args.run_id,),
        ).fetchone()[0])
        source_missing = connection.execute("SELECT COUNT(*) FROM content_jobs WHERE created_run_id=? AND status IN ('awaiting_semantic_review','validated','rendered','published') AND source_pack_json IS NULL", (args.run_id,)).fetchone()[0]
        commercial_selected = connection.execute(
            """SELECT COUNT(*) FROM content_jobs j JOIN keywords k ON k.keyword_id=j.keyword_id
               WHERE j.created_run_id=? AND j.status IN ('rendered','published')
                 AND k.exclusion_reason IS NOT NULL""",
            (args.run_id,),
        ).fetchone()[0]
        non_accept_jobs = connection.execute(
            """SELECT COUNT(*) FROM content_jobs j
               LEFT JOIN keyword_scope_decisions sd
                 ON sd.keyword_id=j.keyword_id AND sd.classifier_version=?
               WHERE j.created_run_id=? AND j.status NOT IN ('retracted_topic_scope','quarantined_topic_scope')
                 AND COALESCE(sd.decision,'missing')<>'accept'""",
            (CLASSIFIER_VERSION, args.run_id),
        ).fetchone()[0]
        published_non_accept = connection.execute(
            """SELECT COUNT(*) FROM content_jobs j
               LEFT JOIN keyword_scope_decisions sd
                 ON sd.keyword_id=j.keyword_id AND sd.classifier_version=?
               WHERE j.created_run_id=? AND j.status IN ('rendered','published')
                 AND COALESCE(sd.decision,'missing')<>'accept'""",
            (CLASSIFIER_VERSION, args.run_id),
        ).fetchone()[0]
        calibration_pairs = connection.execute("SELECT COUNT(*) FROM similarity_reviews WHERE object_type='topic' AND status IN ('labeled','applied')").fetchone()[0]
        semantic_audits: dict[str, dict[str, Any] | None] = {}
        for granularity in ("article", "section"):
            row = connection.execute(
                "SELECT metadata_json FROM provider_objects WHERE provider='local' AND object_type='semantic_dedupe' AND local_id=? AND status='complete'",
                (f"{args.run_id}:{granularity}",),
            ).fetchone()
            semantic_audits[granularity] = json.loads(row[0]) if row else None
    article_schema = load_json(paths.pipeline / "schemas" / "article.schema.json")
    final_validation_errors = []
    final_brand_failures = 0
    final_source_failures = 0
    exact_revision_review_failures = 0
    published_uncovered_terms = 0
    published_topic_purity_failures = 0
    with store.connect() as connection:
        final_rows = connection.execute(
            """SELECT j.*,sr.custom_id review_custom_id,sr.passed review_passed
               FROM content_jobs j LEFT JOIN semantic_reviews sr ON sr.job_id=j.job_id
               WHERE j.created_run_id=? AND j.status IN ('rendered','published')""",
            (args.run_id,),
        ).fetchall()
    for row in final_rows:
        article = json.loads(row["article_json"])
        errors = validate_schema(article, article_schema) + article_policy_errors(article, config)
        if not row["source_pack_json"]:
            errors.append("article job has no attached source pack")
        else:
            source_pack = json.loads(row["source_pack_json"])
            source_errors = source_pack_errors(article, source_pack)
            errors.extend(source_errors)
            final_source_failures += int(bool(source_errors))
            published_uncovered_terms += int(bool((source_pack.get("coverage") or {}).get("uncovered_terms")))
        final_validation_errors.append(errors)
        final_brand_failures += int(any(error.startswith("zero-brand violation:") for error in errors))
        embedded = json.loads(row["validation_json"] or "{}")
        checks_passed = embedded.get("checks") or {}
        # Legacy articles predate this self-review field.  They are still
        # subject to the deterministic direct-keyword and prose validators;
        # an explicit false is always a publication blocker.  New drafts must
        # include the field because article-draft.schema.json requires it.
        published_topic_purity_failures += int(checks_passed.get("topic_purity") is False)
        embedded_approved = (
            embedded.get("gate") == "embedded_self_review_v1"
            and embedded.get("passed") is True
            and checks_passed
            and all(value is True for value in checks_passed.values())
        )
        if not embedded_approved:
            expected_review_ids: set[str] = set()
            if row["plan_json"] and row["source_pack_json"]:
                with store.connect() as connection:
                    payload = _review_payload(connection, row)
                expected_review_ids.add(_review_custom_id(args.run_id, row["job_id"], row["article_json"], payload))
            exact_revision_review_failures += int(
                not row["review_passed"] or row["review_custom_id"] not in expected_review_ids
            )
    final_valid = sum(not errors for errors in final_validation_errors)
    schema_rate = final_valid / rendered if rendered else 0.0
    cache_rate = report["fixed_prefix_cache_hit_rate"]
    checks = {
        "volume": rendered >= args.target,
        "schema_pass_rate_gte_99_5": schema_rate >= 0.995,
        "cache_hit_rate_gte_99": cache_rate is not None and cache_rate >= 0.99,
        "zero_brand": final_brand_failures == 0,
        "no_commercial_sources": final_source_failures == 0,
        "no_unresolved_duplicates": duplicates == 0,
        "zero_duplicate_slugs": duplicate_slugs == 0,
        "zero_duplicate_custom_ids": duplicate_custom_ids == 0,
        "no_commercial_selected": commercial_selected == 0,
        "all_jobs_use_accepted_keywords": non_accept_jobs == 0,
        "zero_hold_or_reject_published": published_non_accept == 0,
        "source_pack_coverage": source_missing == 0,
        "zero_uncovered_center_facts_published": published_uncovered_terms == 0,
        "topic_purity_self_review": published_topic_purity_failures == 0,
        "semantic_or_embedded_review_matches_current_revision": exact_revision_review_failures == 0,
        "similarity_calibration": calibration_pairs >= config["similarity"]["calibration_pairs"],
        "article_semantic_dedupe_complete_and_zero": bool(semantic_audits["article"]) and semantic_audits["article"].get("duplicates") == 0,
        "section_semantic_dedupe_complete_and_zero": bool(semantic_audits["section"]) and semantic_audits["section"].get("duplicates") == 0,
        "dataforseo_within_hard_budget": dataforseo_spend <= config["budgets_usd"]["dataforseo_run_hard_limit"] + 1e-9,
    }
    if args.build_site:
        try:
            subprocess.run([str(paths.root / "bin" / "site"), "build"], cwd=paths.root, check=True, capture_output=True, text=True)
            checks["jekyll_build"] = True
        except (subprocess.CalledProcessError, FileNotFoundError):
            checks["jekyll_build"] = False
    result = {"run_id": args.run_id, "target": args.target, "passed": all(checks.values()), "checks": checks, "metrics": {"rendered": rendered, "final_articles_validated": final_valid, "schema_pass_rate": schema_rate, "cache_hit_rate": cache_rate, "calibration_pairs": calibration_pairs, "duplicate_slugs": duplicate_slugs, "duplicate_custom_ids": duplicate_custom_ids, "non_accept_jobs": non_accept_jobs, "published_non_accept": published_non_accept, "published_uncovered_terms": published_uncovered_terms, "published_topic_purity_failures": published_topic_purity_failures, "semantic_audits": semantic_audits, "exact_revision_review_failures": exact_revision_review_failures, "dataforseo_spend_usd": dataforseo_spend, "dataforseo_hard_limit_usd": config["budgets_usd"]["dataforseo_run_hard_limit"]}}
    print(json.dumps(result, indent=2))
    return 0 if result["passed"] else 1


def prepare_pr(args: argparse.Namespace, paths: Any, config: dict[str, Any], store: Any, credentials: dict[str, str]) -> int:
    report = report_for_run(store, args.run_id)
    branch = args.branch or f"content/{args.run_id}"
    title = args.title or f"Content batch {args.run_id}"
    posts = _git(paths.root, "status", "--porcelain", "--", "_posts").stdout.splitlines()
    if not posts:
        raise RuntimeError("no generated posts are ready for a PR")
    _git(paths.root, "diff", "--check")
    subprocess.run([str(paths.root / "bin" / "site"), "build"], cwd=paths.root, check=True)
    if args.dry_run:
        print(canonical_json({"dry_run": True, "branch": branch, "title": title, "posts": len(posts), "report": report}))
        return 0
    if _git(paths.root, "branch", "--show-current").stdout.strip() == config["github"]["base_branch"]:
        _git(paths.root, "switch", "-c", branch)
    _git(paths.root, "add", "--", "_posts")
    _git(paths.root, "commit", "-m", title)
    _git(paths.root, "push", "-u", "origin", branch)
    body = "Automated content batch. Human merge required.\n\n```json\n" + json.dumps(report, indent=2) + "\n```"
    pr = GitHubClient(credentials["GITHUB_TOKEN"], config["github"]["owner"], config["github"]["repo"]).create_pull_request(title, branch, config["github"]["base_branch"], body)
    print(canonical_json({"pull_request": pr.get("html_url"), "number": pr.get("number"), "branch": branch}))
    return 0


def _git(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["git", *args], cwd=root, check=True, text=True, capture_output=True)


def _mode(path: Path) -> str | None:
    return oct(path.stat().st_mode & 0o777) if path.exists() else None
