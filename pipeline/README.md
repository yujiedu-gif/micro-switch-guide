# Content pipeline

This directory implements the staged MicroSwitchGuide content pipeline. Runtime databases, downloaded API output, generated JSONL, and reports belong in `pipeline/state/` and are ignored by Git.

For the Mac-local, manually controlled monitor and state machine, see [SUPERVISOR.md](SUPERVISOR.md). It never starts at login; paid submissions and PR creation remain explicit operator actions.

For the local visual UI and allowlisted command console, run `./bin/content-control serve --open` and see [CONTROL_CENTER.md](CONTROL_CENTER.md). CSV import performs safe local preparation; paid submissions still require an explicit confirmation.

## Safety invariants

- The first 10,000 articles are educational and zero-brand.
- Paid calls must be associated with a `run_id` and recorded in `api_costs`.
- DataForSEO spending is blocked above the configured per-run hard limit.
- Generated files never overwrite an existing post.
- Batch output is reconciled by `custom_id`, never line position.
- The program renders front matter; the model only returns structured JSON.
- PR preparation may create and push a content branch, but no command merges or writes directly to `main`.
- V10 production uses one article request with an embedded four-part self-review. Deterministic failure may trigger exactly one revision; a revised article that still fails is rejected and replaced from reserve candidates.
- Provider transport failures may resend the identical request up to two times; content revision retries are capped at one.

## Local smoke test

```bash
./bin/content-pipeline init
RUN_ID="$(./bin/content-pipeline create-run --stage smoke-test)"
./bin/content-pipeline status
./bin/content-pipeline audit
python3 -m unittest discover -s pipeline/tests -v
```

`audit` reports missing runtime credential environment variables without printing secret values. Paid provider calls are not part of the local smoke test.

Import supplied credentials into the ignored `0600` secrets file, then inspect only their configured/missing state:

```bash
./bin/content-pipeline credentials import --source-dir "/path/to/credentials" --qdrant-url "https://cluster.example:6333"
./bin/content-pipeline providers-smoke-test
./bin/content-pipeline providers-smoke-test --live
```

The live form performs account and collection checks plus one embedding request. It never prints secret values.

Embeddings default to the local Mac. Install the isolated Python runtime and download `all-mpnet-base-v2` once:

```bash
./bin/bootstrap-embeddings
```

After that, `qdrant-init` and `embed` calculate 768-dimensional vectors locally and upload only those vectors and their lookup payloads to Qdrant. No OpenRouter key or embedding API charge is required. OpenRouter remains an explicit fallback through `--provider openrouter`; it is never selected automatically.

## Keyword import

Input may be CSV or JSONL and must contain `keyword`. Optional fields are `source_endpoint`, `search_volume`, `cpc`, `competition`, `intent`, and `trend`.

```bash
./bin/content-pipeline import-keywords pipeline/fixtures/keywords.jsonl
```

Normalization makes `microswitch` and `micro switch` equivalent for exact deduplication while preserving the original query.

## End-to-end run

```bash
RUN_ID="$(./bin/content-pipeline create-run --stage pilot-50)"
./bin/content-pipeline keywords-discover --run-id "$RUN_ID" --limit 15000
./bin/content-pipeline keywords-discover-collect --run-id "$RUN_ID" --limit 15000
./bin/content-pipeline keywords-filter
./bin/content-pipeline keywords-enrich --run-id "$RUN_ID" --serp-sample 800
./bin/content-pipeline keywords-serp-collect --run-id "$RUN_ID"

./bin/content-pipeline qdrant-init
./bin/content-pipeline embedding-export --object-type topic --output topics.jsonl
./bin/content-pipeline embed --object-type topic --input topics.jsonl --output topic-vectors.jsonl
./bin/content-pipeline cluster --input topic-vectors.jsonl
./bin/content-pipeline jobs-create --run-id "$RUN_ID" --limit 60
./bin/content-pipeline jobs-export --run-id "$RUN_ID" --kind plan --output plan-input.jsonl --limit 60
./bin/content-pipeline build-batches --kind plan --run-id "$RUN_ID" --input plan-input.jsonl --output-dir plan-batches
# Optional diagnostic only; production submission is not blocked by preflight.
./bin/content-pipeline batch-preflight --kind plan --run-id "$RUN_ID" --input plan-batches/plan-001.jsonl
./bin/content-pipeline batch-submit-dir --kind plan --run-id "$RUN_ID" --input-dir plan-batches
```

After `batch-status` downloads a terminal output file, run `ingest-batch`. Then build source packs and links before the article pass:

```bash
./bin/content-pipeline sources quarantine-commercial
./bin/content-pipeline source-packs-build --limit 60
./bin/content-pipeline links-build --run-id "$RUN_ID" --limit 60
./bin/content-pipeline jobs-export --run-id "$RUN_ID" --kind article --output article-input.jsonl --limit 60
./bin/content-pipeline build-batches --kind article --run-id "$RUN_ID" --input article-input.jsonl --output-dir article-batches
```

V10 article requests contain only `system + user`. The model drafts, audits logic, parameters, definitions, and zero-brand compliance, silently repairs its draft, and returns `body_markdown`, `used_claim_ids`, and four `self_review` booleans. Approved plan metadata, source metadata, and internal links are joined locally. Passing outputs become `validated` without a separate OpenAI review Batch. V9 outputs retain the legacy review path.

Run local lexical and semantic duplicate checks, then select the accepted publication set. A failed V10 deterministic or embedded review gets at most one revision:

```bash
./bin/content-pipeline articles-export --output generated-articles.jsonl --limit 50
./bin/content-pipeline dedupe --input generated-articles.jsonl --apply
./bin/content-pipeline embedding-export --object-type chunk --output article-chunks.jsonl --limit 50
./bin/content-pipeline embed --object-type chunk --input article-chunks.jsonl --output article-chunk-vectors.jsonl
./bin/content-pipeline dedupe-semantic --input article-chunk-vectors.jsonl --output semantic-dedupe.jsonl --apply
./bin/content-pipeline render-run --run-id "$RUN_ID"
./bin/content-pipeline report --run-id "$RUN_ID"
./bin/content-pipeline acceptance-check --run-id "$RUN_ID" --target 50 --build-site
./bin/content-pipeline prepare-pr --run-id "$RUN_ID" --dry-run
```

Rollout gates are 50, 250, 1,000, then 10,000. Do not submit the next stage while `acceptance-check` fails.

Local duplicate checks combine exact slug/question checks, SimHash, and MinHash. Qdrant embedding checks provide the second semantic layer. Before the 10,000 stage, rerun the required local scale baselines:

```bash
./bin/content-pipeline benchmark --sizes 1000 5000 10000
```

The report includes job and request states, exclusions, costs, prompt-cache metrics, source coverage, duplicate rate, and review pass rate. V10 accepts the embedded self-review only when all four checks are true and the assembled article passes local schema, SEO, source, link, and brand validation. V9 keeps the exact-revision OpenAI review requirement. Each article has one initial generation and at most one content revision; a failed final revision is replaced from the reserve pool. Qdrant network latency remains provider telemetry rather than part of the local filesystem benchmark.

## Prepare a Batch file

Input JSONL lines contain a unique `custom_id` and a `payload` object. Preparing a file is free and does not submit it.

```bash
./bin/content-pipeline build-batch \
  --kind plan \
  --run-id "$RUN_ID" \
  --input pipeline/fixtures/plan-input.jsonl \
  --output pipeline/state/plan-smoke.jsonl
```

The file targets `/v1/responses`, preserves a fixed Skill prefix, uses Structured Outputs, and is checked against the 50,000-request and 200 MB Batch limits.

## Validate and render

```bash
./bin/content-pipeline validate-article path/to/article.json
./bin/content-pipeline render path/to/article.json --date 2026-10-09
./bin/site build
```

Rendering refuses to overwrite an existing post. A passing deterministic validation does not replace source-pack, semantic duplicate, internal-link, or build validation.
