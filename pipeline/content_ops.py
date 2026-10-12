from __future__ import annotations

import hashlib
import json
import math
import re
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable

from core import canonical_json, normalize_keyword, now_iso, stable_id
from validators import validate_schema
from topic_scope import classify_keyword


COMMERCIAL_PATTERNS = {
    "supplier_intent": r"\b(?:supplier|suppliers|distributor|distributors|vendor|vendors)\b",
    "manufacturer_intent": r"\b(?:manufacturer|manufacturers|maker|makers)\b",
    "factory_intent": r"\b(?:factory|factories|oem|odm)\b",
    "wholesale_intent": r"\b(?:wholesale|bulk buy|bulk order)\b",
    "ranking_intent": r"\b(?:best|top|leading)\b.*\b(?:micro switch|microswitch|snap[- ]action switch)(?:es)?\b|\b(?:micro switch|microswitch|snap[- ]action switch)(?:es)?\b.*\b(?:best|top|leading)\b",
    "transactional_intent": r"\b(?:buy|price|pricing|quote|for sale|near me|online|replacement)\b",
    "marketplace_intent": r"\b(?:amazon|ebay|aliexpress|alibaba|temu|walmart|grainger|digikey|mouser|newark|radioshack|radio shack|rs components)\b",
    "commercial_entity": r"\b(?:company|companies|corp|corporation|llc|ltd|limited|srl)\b|\b(?:micro switch|microswitch)(?:es)?\s+(?:usa|uk|india|china)\b",
    "non_english": r"\b(?:a leva|a rotella|bistabilny|para mouse|4 pines|vulcano)\b",
}


_TECHNICAL_ALNUM = re.compile(
    r"^(?:ip\d{2,3}|\d+(?:\.\d+)?(?:a|v|vac|vdc|w|kw|ma|mv|amp|amps|volt|volts|mm|cm|in|inch|inches))$",
    re.I,
)


def _looks_like_product_model(normalized: str) -> bool:
    """Reject model/series queries before they can become editorial subjects.

    Short electrical ratings such as ``10a`` and protection codes such as
    ``ip67`` remain eligible. Mixed letter/number part codes and long numeric
    identifiers do not.
    """
    if re.search(r"\b[a-z][a-z0-9-]*\s+\d+[a-z0-9-]*\s+series\b", normalized, re.I):
        return True
    if re.search(r"\b(?:model|part|series)\s*(?:number|no\.?|#)?\s*[a-z0-9-]*\d[a-z0-9-]*\b", normalized, re.I):
        return True
    if re.search(r"\b(?!(?:ip|ac|dc)\b)[a-z]{1,4}\s+\d{2,}\b", normalized, re.I):
        return True
    if re.search(r"\b(?:ex|op)\s+ar\b", normalized, re.I):
        return True
    for token in re.findall(r"[a-z0-9]+(?:\.[a-z0-9]+)?", normalized, re.I):
        if _TECHNICAL_ALNUM.fullmatch(token):
            continue
        if re.fullmatch(r"\d{4,}(?:\.\d+)?", token):
            return True
        if any(char.isalpha() for char in token) and any(char.isdigit() for char in token):
            return True
    return False


def exclusion_reason(keyword: str, known_brands: Iterable[str] = (), intent: str | None = None) -> str | None:
    result = classify_keyword(keyword, known_brands, intent)
    if result.decision == "accept":
        return None
    prefix = "scope_hold" if result.decision == "hold" else "scope_reject"
    return f"{prefix}:{result.reason_codes[0]}"


def cosine_similarity(left: list[float], right: list[float]) -> float:
    if len(left) != len(right) or not left:
        raise ValueError("vectors must be non-empty and have equal dimensions")
    numerator = sum(a * b for a, b in zip(left, right))
    denominator = math.sqrt(sum(a * a for a in left)) * math.sqrt(sum(b * b for b in right))
    return numerator / denominator if denominator else 0.0


def cluster_vectors(items: list[dict[str, Any]], threshold: float) -> list[list[dict[str, Any]]]:
    """Deterministic greedy clustering; input order is the tie-breaker."""
    clusters: list[list[dict[str, Any]]] = []
    centroids: list[list[float]] = []
    for item in items:
        vector = item["vector"]
        best_index = -1
        best_score = -1.0
        for index, centroid in enumerate(centroids):
            score = cosine_similarity(vector, centroid)
            if score > best_score:
                best_index, best_score = index, score
        if best_score >= threshold:
            clusters[best_index].append(item)
            count = len(clusters[best_index])
            centroids[best_index] = [((old * (count - 1)) + new) / count for old, new in zip(centroids[best_index], vector)]
        else:
            clusters.append([item])
            centroids.append(list(vector))
    return clusters


def serp_overlap(left: Iterable[str], right: Iterable[str]) -> float:
    a, b = set(left), set(right)
    return len(a & b) / len(a | b) if a or b else 0.0


def simhash(text: str) -> int:
    tokens = re.findall(r"[a-z0-9]+", text.casefold())
    features = [" ".join(tokens[index:index + 3]) for index in range(max(1, len(tokens) - 2))]
    weights = [0] * 64
    for feature in features:
        value = int.from_bytes(hashlib.blake2b(feature.encode(), digest_size=8).digest(), "big")
        for bit in range(64):
            weights[bit] += 1 if value & (1 << bit) else -1
    result = 0
    for bit, weight in enumerate(weights):
        if weight >= 0:
            result |= 1 << bit
    return result


def hamming_distance(left: int, right: int) -> int:
    return (left ^ right).bit_count()


def minhash_signature(text: str, permutations: int = 64) -> tuple[int, ...]:
    """Return a deterministic MinHash signature over five-token shingles."""
    tokens = re.findall(r"[a-z0-9]+", text.casefold())
    width = 5
    shingles = {" ".join(tokens[index:index + width]) for index in range(max(1, len(tokens) - width + 1))}
    if not shingles:
        shingles = {""}
    signature = []
    for seed in range(permutations):
        salt = seed.to_bytes(4, "big")
        signature.append(min(int.from_bytes(hashlib.blake2b(salt + shingle.encode(), digest_size=8).digest(), "big") for shingle in shingles))
    return tuple(signature)


def minhash_similarity(left: tuple[int, ...], right: tuple[int, ...]) -> float:
    if not left or len(left) != len(right):
        raise ValueError("MinHash signatures must be non-empty and have equal length")
    return sum(a == b for a, b in zip(left, right)) / len(left)


def ingest_source_pack(store: Any, pack: dict[str, Any], schema: dict[str, Any]) -> dict[str, int]:
    errors = validate_schema(pack, schema)
    if errors:
        raise ValueError("invalid source pack: " + "; ".join(errors))
    sources = {source["source_id"]: source for source in pack["sources"]}
    allowed_source_types = {"standard", "regulator", "government", "intergovernmental", "academic", "encyclopedia"}
    for source in pack["sources"]:
        if source["source_type"] not in allowed_source_types:
            raise ValueError(f"commercial or unsupported source type is prohibited: {source['source_id']}")
        if source.get("editorial_block_names"):
            raise ValueError(f"commercial source publisher is prohibited: {source['source_id']}")
    for claim in pack["claims"]:
        missing = set(claim["source_ids"]) - sources.keys()
        if missing:
            raise ValueError(f"claim {claim['claim_id']} references missing sources: {sorted(missing)}")
        if claim["scope"] in {"manufacturer", "series"} and claim["status"] == "accepted":
            raise ValueError(f"first-10,000 source pack cannot accept brand-specific claim {claim['claim_id']}")
        if claim["scope"] == "model" and claim["status"] == "accepted":
            model_identifier = str((claim.get("conditions") or {}).get("model_identifier", "")).strip()
            if not model_identifier:
                raise ValueError(f"accepted model claim requires conditions.model_identifier: {claim['claim_id']}")
    now = now_iso()
    with store.connect() as connection:
        for source in pack["sources"]:
            connection.execute(
                """INSERT INTO sources(source_id,title,publisher,url,source_type,document_version,document_date,page_or_section,retrieved_at,content_hash,editorial_block_names_json,evidence_summary)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?) ON CONFLICT(source_id) DO UPDATE SET
                title=excluded.title,publisher=excluded.publisher,url=excluded.url,source_type=excluded.source_type,
                document_version=excluded.document_version,document_date=excluded.document_date,page_or_section=excluded.page_or_section,
                retrieved_at=excluded.retrieved_at,content_hash=excluded.content_hash,
                editorial_block_names_json=excluded.editorial_block_names_json,evidence_summary=excluded.evidence_summary""",
                (source["source_id"], source["title"], source["publisher"], source["url"], source["source_type"],
                 source.get("document_version"), source.get("document_date"), source.get("page_or_section"), source["retrieved_at"],
                 source["content_hash"], canonical_json(source.get("editorial_block_names", [])), source.get("evidence_summary")),
            )
        for claim in pack["claims"]:
            connection.execute(
                """INSERT INTO claims(claim_id,subject,predicate,value_json,unit,conditions_json,scope,confidence,status,conflicts_with_json,supersedes_json,created_at,updated_at)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?) ON CONFLICT(claim_id) DO UPDATE SET
                subject=excluded.subject,predicate=excluded.predicate,value_json=excluded.value_json,unit=excluded.unit,
                conditions_json=excluded.conditions_json,scope=excluded.scope,confidence=excluded.confidence,status=excluded.status,
                conflicts_with_json=excluded.conflicts_with_json,supersedes_json=excluded.supersedes_json,updated_at=excluded.updated_at""",
                (claim["claim_id"], claim["subject"], claim["predicate"], canonical_json(claim["value"]), claim.get("unit"),
                 canonical_json(claim.get("conditions", {})), claim["scope"], claim["confidence"], claim["status"],
                 canonical_json(claim.get("conflicts_with", [])), canonical_json(claim.get("supersedes", [])), now, now),
            )
            connection.execute("DELETE FROM claim_sources WHERE claim_id=?", (claim["claim_id"],))
            connection.executemany("INSERT INTO claim_sources(claim_id,source_id) VALUES(?,?)", [(claim["claim_id"], sid) for sid in claim["source_ids"]])
    return {"sources": len(pack["sources"]), "claims": len(pack["claims"])}


_EVIDENCE_STOP = {"about", "guide", "micro", "switch", "switches", "explained", "what", "when", "with", "from", "into", "general", "specific", "device", "applicable", "technical"}


def _evidence_tokens(value: Any) -> set[str]:
    raw = re.findall(r"[a-z0-9]+", canonical_json(value).casefold())
    normalized = set()
    for token in raw:
        if token in _EVIDENCE_STOP or len(token) < 3:
            continue
        if token.endswith("ies") and len(token) > 4:
            token = token[:-3] + "y"
        elif token.endswith("s") and len(token) > 4:
            token = token[:-1]
        normalized.add(token)
    return normalized


def build_source_pack(store: Any, topic_id: str, terms: list[str], limit: int = 24) -> dict[str, Any]:
    search_terms: set[str] = set()
    for term in terms:
        normalized = normalize_keyword(term)
        if normalized:
            search_terms.add(normalized)
        search_terms.update(_evidence_tokens(normalized))
    patterns = [f"%{term}%" for term in sorted(search_terms)]
    if not patterns:
        raise ValueError("at least one retrieval term is required")
    where = " OR ".join("lower(c.subject || ' ' || c.predicate || ' ' || c.value_json) LIKE ?" for _ in patterns)
    with store.connect() as connection:
        candidates = connection.execute(
            f"SELECT c.* FROM claims c WHERE c.status='accepted' AND c.scope IN ('general','standard','model') AND ({where}) LIMIT ?",
            (*patterns, max(100, limit * 10)),
        ).fetchall()
        requested_text = " ".join(normalize_keyword(term) for term in terms)
        candidates = [
            row for row in candidates
            if row["scope"] != "model"
            or normalize_keyword(str(json.loads(row["conditions_json"] or "{}").get("model_identifier", ""))) in requested_text
        ]
        selected: dict[str, Any] = {}
        for term in terms:
            needed = _evidence_tokens(term)
            threshold = min(2, len(needed))
            ranked = []
            for row in candidates:
                document = f"{row['subject']} {row['predicate']} {row['value_json']} {row['conditions_json']}"
                available = _evidence_tokens(document)
                overlap = len(needed & available)
                if needed and overlap >= threshold:
                    exact = int(normalize_keyword(term) in normalize_keyword(document))
                    ranked.append((exact, overlap / len(needed), overlap, row["confidence"] == "high", row["claim_id"], row))
            if ranked:
                best = max(ranked, key=lambda item: item[:-1])[-1]
                selected[best["claim_id"]] = best
        claims = list(selected.values())[:limit]
        output_claims, source_ids = [], set()
        for row in claims:
            ids = [r[0] for r in connection.execute("SELECT source_id FROM claim_sources WHERE claim_id=?", (row["claim_id"],))]
            source_ids.update(ids)
            output_claims.append({
                "claim_id": row["claim_id"], "subject": row["subject"], "predicate": row["predicate"],
                "value": json.loads(row["value_json"]), "unit": row["unit"], "conditions": json.loads(row["conditions_json"]),
                "scope": row["scope"], "source_ids": ids, "confidence": row["confidence"], "status": row["status"],
                "conflicts_with": json.loads(row["conflicts_with_json"]), "supersedes": json.loads(row["supersedes_json"]),
            })
        sources = []
        for source_id in sorted(source_ids):
            row = connection.execute("SELECT * FROM sources WHERE source_id=?", (source_id,)).fetchone()
            sources.append({key: row[key] for key in ("source_id", "title", "publisher", "url", "source_type", "document_version", "document_date", "page_or_section", "retrieved_at", "content_hash", "evidence_summary")} | {"editorial_block_names": json.loads(row["editorial_block_names_json"])})
    return {"topic_id": topic_id, "retrieved_at": now_iso(), "claims": output_claims, "sources": sources}


def missing_source_terms(pack: dict[str, Any], terms: list[str]) -> list[str]:
    """Return requested evidence concepts not represented by an accepted claim.

    This is deliberately conservative: a source pack must cover every planning
    term with either its only meaningful token or at least two meaningful
    tokens. It prevents a generic switch claim from satisfying an unrelated
    evidence request merely because both contain the word ``switch``.
    """
    claim_token_sets = [_evidence_tokens(claim) for claim in pack.get("claims", []) if claim.get("status") == "accepted"]
    missing = []
    for term in terms:
        needed = _evidence_tokens(term)
        threshold = min(2, len(needed))
        if not needed or not any(len(needed & available) >= threshold for available in claim_token_sets):
            missing.append(term)
    return missing


def build_internal_links(jobs: list[dict[str, Any]], minimum: int = 3, maximum: int = 8) -> list[dict[str, str]]:
    by_category: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for job in jobs:
        by_category[job.get("category", "")].append(job)
    links: list[dict[str, str]] = []
    for source in jobs:
        candidates = [item for item in by_category[source.get("category", "")] if item["job_id"] != source["job_id"]]
        candidates += [item for item in jobs if item["job_id"] != source["job_id"] and item not in candidates]
        desired = min(maximum, max(minimum, min(len(candidates), maximum)))
        for index, target in enumerate(candidates[:desired]):
            relation = "pillar" if index == 0 and target.get("page_type") == "pillar" else ("supporting" if target.get("category") == source.get("category") else "related")
            links.append({"source_job_id": source["job_id"], "target_job_id": target["job_id"], "relation": relation, "anchor_text": target.get("primary_keyword") or target.get("title", "related guide"), "status": "valid"})
    return links


def authoritative_internal_links(connection: Any, job_id: str) -> list[dict[str, str]]:
    rows = connection.execute(
        """SELECT l.target_job_id,l.relation,l.anchor_text,j.slug
           FROM internal_links l JOIN content_jobs j ON j.job_id=l.target_job_id
           WHERE l.source_job_id=? AND l.status='valid'
           ORDER BY l.target_job_id""",
        (job_id,),
    ).fetchall()
    return [
        {
            "target_job_id": row["target_job_id"],
            "relation": row["relation"],
            "anchor_text": row["anchor_text"],
            "url": f"/guides/{row['slug']}/",
        }
        for row in rows
    ]


def apply_authoritative_internal_links(article: dict[str, Any], links: list[dict[str, str]]) -> dict[str, Any]:
    """Replace fallible model link placement with the approved local graph."""
    normalized = json.loads(canonical_json(article))
    body = str(normalized.get("body_markdown", ""))
    # Delete the complete derived block before rebuilding it. Removing only
    # the Markdown link leaves orphan bullets and repeated headings when the
    # operation is rerun, which violates idempotence.
    body = re.sub(
        r"\n*^### Related guides\s*$.*?(?=^##\s+|\Z)",
        "\n",
        body,
        flags=re.MULTILINE | re.DOTALL,
    )
    body = re.sub(r"\s*\[[^\]]+\]\(/guides/[^)]+\)", "", body)
    link_block = "\n\n### Related guides\n\n" + "\n".join(
        f"- [{link['anchor_text']}]({link['url']})" for link in links
    ) + "\n"
    headings = list(re.finditer(r"^##\s+.+$", body, re.MULTILINE))
    if headings:
        insertion = headings[-1].start()
        body = body[:insertion].rstrip() + link_block + "\n" + body[insertion:].lstrip()
    else:
        body = body.rstrip() + link_block
    body = body.strip()
    keyword = str(normalized.get("primary_keyword", "")).strip()
    headings = list(re.finditer(r"^##\s+.+$", body, re.MULTILINE))
    if keyword and headings:
        heading = headings[-1]
        content_start = heading.end()
        prefix, closing = body[:content_start], body[content_start:]
        matches = list(re.finditer(re.escape(keyword), closing, re.IGNORECASE))
        if not matches:
            closing = closing.rstrip() + f"\n\nThis concludes the explanation of {keyword}."
        elif len(matches) > 1:
            replacement = "this identifier" if re.search(r"\d", keyword) else "this topic"
            pieces = []
            cursor = 0
            for index, match in enumerate(matches):
                pieces.append(closing[cursor:match.start()])
                pieces.append(match.group(0) if index == 0 else replacement)
                cursor = match.end()
            pieces.append(closing[cursor:])
            closing = "".join(pieces)
        body = prefix + closing
    normalized["body_markdown"] = body
    normalized["internal_links"] = links
    return normalized


def assemble_article_draft(
    draft: dict[str, Any],
    plan: dict[str, Any],
    source_pack: dict[str, Any],
    links: list[dict[str, str]],
) -> dict[str, Any]:
    """Join a small model draft with authoritative local metadata.

    Plans, evidence metadata, and the link graph have already passed their own
    gates. Asking the model to repeat them adds tokens and creates avoidable
    mismatches, so V10 model output contains only prose and used claim IDs.
    """
    used_claim_ids = list(dict.fromkeys(str(item) for item in draft.get("used_claim_ids", [])))
    claims = {claim.get("claim_id"): claim for claim in source_pack.get("claims", [])}
    source_ids = {
        source_id
        for claim_id in used_claim_ids
        for source_id in claims.get(claim_id, {}).get("source_ids", [])
    }
    sources = [
        {
            "source_id": source["source_id"],
            "title": source["title"],
            "publisher": source["publisher"],
            "url": source["url"],
        }
        for source in source_pack.get("sources", [])
        if source.get("source_id") in source_ids
    ]
    primary_keyword = str(plan.get("primary_keyword", ""))
    category = str(plan.get("category", "Basics"))
    article = {
        "primary_keyword": primary_keyword,
        "secondary_keywords": list(plan.get("secondary_keywords", [])),
        "owned_question": plan.get("owned_question", ""),
        "title": plan.get("title", ""),
        "h1": plan.get("h1", plan.get("title", "")),
        "description": plan.get("description", ""),
        "slug": plan.get("slug", ""),
        "category": category,
        "tags": list(dict.fromkeys([primary_keyword, "micro switches", category])),
        "body_markdown": draft.get("body_markdown", ""),
        "used_claim_ids": used_claim_ids,
        "internal_links": links,
        "source_manufacturer_names": [],
        "sources": sources,
    }
    return apply_authoritative_internal_links(article, links)


def report_for_run(store: Any, run_id: str) -> dict[str, Any]:
    with store.connect() as connection:
        run = connection.execute("SELECT * FROM runs WHERE run_id=?", (run_id,)).fetchone()
        if not run:
            raise ValueError(f"unknown run_id: {run_id}")
        costs = {row["provider"]: round(row["amount"], 6) for row in connection.execute("SELECT provider,SUM(amount_usd) amount FROM api_costs WHERE run_id=? GROUP BY provider", (run_id,))}
        requests = {row["status"]: row["n"] for row in connection.execute("SELECT status,COUNT(*) n FROM batch_requests WHERE run_id=? GROUP BY status", (run_id,))}
        usage_rows = connection.execute("SELECT custom_id,kind,parent_custom_id,usage_json,created_at FROM batch_requests WHERE run_id=? AND usage_json != '{}' ORDER BY created_at,custom_id", (run_id,)).fetchall()
        input_tokens = cached_tokens = cache_hits = cache_eligible_requests = 0
        steady_cache_hits = steady_cache_eligible_requests = 0
        requests_by_id = {row["custom_id"]: row for row in usage_rows}
        warmup_requests = 0

        for row in usage_rows:
            usage = json.loads(row["usage_json"])
            request_input = int(usage.get("input_tokens", 0))
            details = usage.get("input_tokens_details", {})
            request_cached = int(details.get("cached_tokens", 0))
            request_cache_write = int(details.get("cache_write_tokens", 0))
            input_tokens += request_input
            cached_tokens += request_cached
            if request_input:
                cache_eligible_requests += 1
                cache_hits += int(request_cached > 0)
                # Explicit prompt caching reports cache population separately
                # from a hit. Every cache-write request is the warmup for its
                # exact fixed prefix (including a newly versioned Skill).
                if request_cache_write > 0:
                    warmup_requests += 1
                else:
                    steady_cache_eligible_requests += 1
                    steady_cache_hits += int(request_cached > 0)
        raw_cache_rate = cache_hits / cache_eligible_requests if cache_eligible_requests else None
        cache_rate = steady_cache_hits / steady_cache_eligible_requests if steady_cache_eligible_requests else None
        cached_token_rate = cached_tokens / input_tokens if input_tokens else None
        jobs = {row["status"]: row["n"] for row in connection.execute("SELECT status,COUNT(*) n FROM content_jobs WHERE created_run_id=? GROUP BY status", (run_id,))}
        exclusions = {row["exclusion_reason"]: row["n"] for row in connection.execute("SELECT exclusion_reason,COUNT(*) n FROM keywords WHERE exclusion_reason IS NOT NULL GROUP BY exclusion_reason")}
        article_total = connection.execute("SELECT COUNT(*) FROM content_jobs WHERE created_run_id=? AND article_json IS NOT NULL", (run_id,)).fetchone()[0]
        source_covered = connection.execute("SELECT COUNT(*) FROM content_jobs WHERE created_run_id=? AND article_json IS NOT NULL AND source_pack_json IS NOT NULL", (run_id,)).fetchone()[0]
        duplicates = connection.execute("SELECT COUNT(*) FROM content_jobs WHERE created_run_id=? AND duplicate_of_job_id IS NOT NULL", (run_id,)).fetchone()[0]
        reviews = connection.execute("SELECT COUNT(*) total,COALESCE(SUM(sr.passed),0) passed FROM semantic_reviews sr JOIN content_jobs j ON j.job_id=sr.job_id WHERE j.created_run_id=?", (run_id,)).fetchone()
    return {
        "run_id": run_id, "stage": run["stage"], "status": run["status"], "costs_usd": costs,
        "batch_requests": requests, "content_jobs": jobs, "keyword_exclusions": exclusions,
        "input_tokens": input_tokens, "cached_tokens": cached_tokens,
        "fixed_prefix_cache_hit_rate": cache_rate, "raw_cache_hit_rate": raw_cache_rate,
        "cache_warmup_requests_excluded": warmup_requests, "cached_input_token_rate": cached_token_rate,
        "source_coverage_rate": source_covered / article_total if article_total else None,
        "duplicate_count": duplicates, "duplicate_rate": duplicates / article_total if article_total else None,
        "semantic_review_pass_rate": reviews["passed"] / reviews["total"] if reviews["total"] else None,
    }
