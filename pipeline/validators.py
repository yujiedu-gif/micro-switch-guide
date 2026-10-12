from __future__ import annotations

import copy
import re
from typing import Any

from core import normalize_keyword, slugify
from topic_scope import classify_keyword


def normalize_plan_metadata(plan: dict[str, Any]) -> dict[str, Any]:
    """Repair deterministic plan identity and exact-keyword metadata locally."""
    normalized = copy.deepcopy(plan)
    keyword = str(normalized.get("primary_keyword", "")).strip()
    description = str(normalized.get("description", "")).strip()
    if not keyword:
        return normalized
    if not (140 <= len(description) <= 160 and phrase_count(description, keyword) == 1):
        prefix = f"{keyword}: "
        if len(prefix) < 140:
            source = (
                "Understand the operating idea, essential terminology, practical checks, limitations, "
                "and evidence needed for careful selection, installation, testing, maintenance, and "
                "troubleshooting decisions in real applications."
            )
            source = re.sub(re.escape(keyword), "the topic", source, flags=re.IGNORECASE)
            selected: list[str] = []
            for word in source.split():
                candidate = prefix + " ".join([*selected, word]) + "."
                if len(candidate) > 155:
                    break
                selected.append(word)
            candidate = prefix + " ".join(selected) + "."
            if len(candidate) < 140:
                for word in ("with", "clear", "scope", "and", "safe", "technical", "boundaries"):
                    attempted = candidate[:-1] + " " + word + "."
                    if len(attempted) <= 160:
                        candidate = attempted
                    if len(candidate) >= 140:
                        break
            normalized["description"] = candidate

    reader_task = str(normalized.get("reader_task", "")).strip()
    answer_type = str(normalized.get("answer_type", "")).strip()
    # The model often collapses every application to the generic entity
    # ``micro_switch``.  That makes unrelated devices collide before the
    # semantic duplicate gate can compare their actual plans.  Use the exact
    # normalized keyword as the deterministic identity segment; Qdrant still
    # handles genuine semantic overlap later in the workflow.
    entity = slugify(normalize_keyword(keyword)).replace("-", "_") or "micro_switch"
    if reader_task and answer_type:
        normalized["content_signature"] = f"{entity}|{reader_task}|{answer_type}"

    outline = normalized.get("outline") or []
    if outline and not any(phrase_count(str(item.get("h2", "")), keyword) for item in outline if isinstance(item, dict)):
        outline[0]["h2"] = keyword
    return normalized


def reconcile_review_deterministic_checks(
    review: dict[str, Any], article: dict[str, Any], config: dict[str, Any]
) -> dict[str, Any]:
    """Make deterministic editorial-policy checks authoritative.

    Semantic review remains authoritative for evidence and ownership, while
    zero-brand is calculated from the exact editorial fields and block list.
    """
    reconciled = copy.deepcopy(review)
    checks = reconciled.setdefault("checks", {})
    zero_brand_errors = [
        error for error in article_policy_errors(article, config)
        if error.startswith("zero-brand violation:")
    ]
    zero_brand_passed = not zero_brand_errors
    checks["zero_brand"] = zero_brand_passed
    if zero_brand_passed:
        pattern = re.compile(
            r"zero[- ]brand|blocked (?:publisher |manufacturer )?name|"
            r"publisher names?|manufacturer names?",
            re.IGNORECASE,
        )
        reconciled["issues"] = [
            issue for issue in reconciled.get("issues", [])
            if not pattern.search(str(issue))
        ]
    # The production promise is logical and technical validity, not stylistic
    # perfection.  The model focuses on logic, parameters, and definitions;
    # deterministic validators and duplicate systems own the other gates.
    required_checks = (
        "logical_consistency",
        "parameter_accuracy",
        "definition_accuracy",
        "zero_brand",
    )
    reconciled["passed"] = all(bool(checks.get(name)) for name in required_checks)
    return reconciled


def validate_schema(value: Any, schema: dict[str, Any], path: str = "$") -> list[str]:
    errors: list[str] = []
    expected = schema.get("type")
    if expected and not _matches_type(value, expected):
        return [f"{path}: expected {expected}, got {type(value).__name__}"]

    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: value {value!r} is not in {schema['enum']!r}")
    if isinstance(value, str):
        if len(value) < schema.get("minLength", 0):
            errors.append(f"{path}: shorter than {schema['minLength']} characters")
        if "maxLength" in schema and len(value) > schema["maxLength"]:
            errors.append(f"{path}: longer than {schema['maxLength']} characters")
        if "pattern" in schema and not re.fullmatch(schema["pattern"], value):
            errors.append(f"{path}: does not match {schema['pattern']}")
    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            errors.append(f"{path}: requires at least {schema['minItems']} items")
        if schema.get("uniqueItems") and len({repr(item) for item in value}) != len(value):
            errors.append(f"{path}: items must be unique")
        item_schema = schema.get("items")
        if item_schema:
            for index, item in enumerate(value):
                errors.extend(validate_schema(item, item_schema, f"{path}[{index}]"))
    if isinstance(value, dict):
        for key in schema.get("required", []):
            if key not in value:
                errors.append(f"{path}: missing required property {key!r}")
        properties = schema.get("properties", {})
        for key, item in value.items():
            if key in properties:
                errors.extend(validate_schema(item, properties[key], f"{path}.{key}"))
            elif schema.get("additionalProperties") is False:
                errors.append(f"{path}: unexpected property {key!r}")
    return errors


def _matches_type(value: Any, expected: str | list[str]) -> bool:
    allowed = expected if isinstance(expected, list) else [expected]
    checks = {
        "object": lambda item: isinstance(item, dict),
        "array": lambda item: isinstance(item, list),
        "string": lambda item: isinstance(item, str),
        "integer": lambda item: isinstance(item, int) and not isinstance(item, bool),
        "number": lambda item: isinstance(item, (int, float)) and not isinstance(item, bool),
        "boolean": lambda item: isinstance(item, bool),
        "null": lambda item: item is None,
    }
    return any(checks[kind](value) for kind in allowed if kind in checks)


def phrase_count(text: str, phrase: str) -> int:
    normalized_text = normalize_keyword(text)
    normalized_phrase = normalize_keyword(phrase)
    pattern = r"(?<!\w)" + re.escape(normalized_phrase) + r"(?!\w)"
    return len(re.findall(pattern, normalized_text))


def article_policy_errors(article: dict[str, Any], config: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    keyword = article.get("primary_keyword", "")
    title = article.get("title", "")
    h1 = article.get("h1", "")
    description = article.get("description", "")
    slug = article.get("slug", "")
    body = article.get("body_markdown", "")
    scope = classify_keyword(keyword, config.get("program", {}).get("excluded_brand_terms", []))
    if scope.decision != "accept":
        errors.append(f"topic purity requires an accepted direct micro-switch keyword: {scope.decision}:{','.join(scope.reason_codes)}")

    if h1 != title:
        errors.append("h1 must equal title because the Jekyll layout renders page.title as H1")
    if phrase_count(title, keyword) < 1:
        errors.append("title lacks the complete primary keyword")
    if phrase_count(h1, keyword) < 1:
        errors.append("h1 lacks the complete primary keyword")
    if phrase_count(description, keyword) != 1:
        errors.append("description must contain the complete primary keyword exactly once")
    if not 140 <= len(description) <= 160:
        errors.append(f"description length is {len(description)}, expected 140-160")
    expected_slug = slugify(keyword)
    if expected_slug and expected_slug not in slug:
        errors.append(f"slug must preserve the complete primary keyword form: expected to contain {expected_slug!r}")

    prose = _plain_markdown(body)
    sentences = re.split(r"(?<=[.!?])\s+", prose.strip())
    first_two = " ".join(sentences[:2])
    first_150 = " ".join(prose.split()[:150])
    if phrase_count(first_two, keyword) < 1:
        errors.append("first two sentences lack the complete primary keyword")
    if phrase_count(first_150, keyword) < 1:
        errors.append("first 150 words lack the complete primary keyword")

    h2s = re.findall(r"^##\s+(.+)$", body, re.MULTILINE)
    if not h2s:
        errors.append("body must contain at least one H2")
    elif not any(phrase_count(h2, keyword) for h2 in h2s):
        errors.append("at least one H2 must contain the complete primary keyword")
    if any(normalize_keyword(h2) in {"conclusion", "summary"} for h2 in h2s):
        errors.append("generic Conclusion or Summary H2 is prohibited")

    sections = re.split(r"^##\s+.+$", body, flags=re.MULTILINE)
    closing = sections[-1] if sections else body
    if phrase_count(_plain_markdown(closing), keyword) != 1:
        errors.append("closing section must contain the complete primary keyword exactly once")

    if "—" in body:
        errors.append("em dash is prohibited")

    editorial = "\n".join([title, h1, description, slug, body])
    blocked_names = {"ZINGEAR", "ZING EAR"}
    blocked_names.update(
        str(name).strip()
        for name in config.get("program", {}).get("excluded_brand_terms", [])
        if str(name).strip()
    )
    blocked_names.update(str(name).strip() for name in article.get("source_manufacturer_names", []) if str(name).strip())
    for name in sorted(blocked_names):
        pattern = re.compile(r"(?<!\w)" + re.escape(name) + r"(?!\w)", re.IGNORECASE)
        if pattern.search(editorial):
            errors.append(f"zero-brand violation: {name}")

    marketing_patterns = {
        "supplier/manufacturer ranking": r"\b(?:top|best)\s+\d*\s*(?:micro switch\s+)?(?:suppliers?|manufacturers?|brands?)\b",
        "sales CTA": r"\b(?:request a quote|get a quote|contact our sales|buy now|shop now)\b",
        "superiority claim": r"\b(?:world[- ]leading|industry[- ]leading|best-in-class|top-tier|number one|no\. ?1)\b",
    }
    for label, pattern in marketing_patterns.items():
        if re.search(pattern, editorial, re.IGNORECASE):
            errors.append(f"marketing content prohibited: {label}")

    word_count = len(re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*", prose))
    minimum = config["program"]["article_word_min"]
    maximum = config["program"]["article_word_max"]
    if not minimum <= word_count <= maximum:
        errors.append(f"body word count is {word_count}, expected {minimum}-{maximum}")

    links = article.get("internal_links", [])
    targets = [item.get("target_job_id") for item in links if isinstance(item, dict)]
    if len(targets) != len(set(targets)):
        errors.append("internal link targets must be unique")
    body_urls = set(re.findall(r"\[[^]]+\]\(([^)]+)\)", body))
    for link in links:
        if link.get("url") not in body_urls:
            errors.append(f"planned internal link is missing from body: {link.get('url')}")

    return errors


def plan_policy_errors(plan: dict[str, Any], config: dict[str, Any] | None = None) -> list[str]:
    errors: list[str] = []
    keyword = plan.get("primary_keyword", "")
    scope = plan.get("topic_scope") or {}
    if scope != {"primary_entity": "micro_switch", "relation": "direct", "owned_question_is_direct": True}:
        errors.append("plan topic_scope must declare a direct micro_switch owned question")
    decision = classify_keyword(keyword, (config or {}).get("program", {}).get("excluded_brand_terms", []))
    if decision.decision != "accept":
        errors.append(f"plan keyword is outside strict topic scope: {decision.decision}:{','.join(decision.reason_codes)}")
    if plan.get("h1") != plan.get("title"):
        errors.append("plan h1 must equal title")
    anchors = [str(item).strip().casefold() for item in plan.get("differentiation_anchors", []) if str(item).strip()]
    if len(set(anchors)) < 2:
        errors.append("plan requires at least two unique differentiation anchors")
    signature = str(plan.get("content_signature", ""))
    if len(signature.split("|")) < 3:
        errors.append("plan content_signature must include entity, reader task, and answer type")
    outline = [item for item in plan.get("outline", []) if isinstance(item, dict)]
    outline_roles = [str(item.get("section_role", "")).strip() for item in outline]
    if outline_roles != list(plan.get("section_roles", [])):
        errors.append("plan section_roles must match outline section_role values in order")
    if plan.get("reader_task") and plan.get("reader_task") not in signature.split("|"):
        errors.append("plan content_signature must include reader_task")
    if plan.get("answer_type") and plan.get("answer_type") not in signature.split("|"):
        errors.append("plan content_signature must include answer_type")
    if phrase_count(plan.get("title", ""), keyword) < 1:
        errors.append("plan title lacks the complete primary keyword")
    if phrase_count(plan.get("description", ""), keyword) != 1:
        errors.append("plan description must contain the complete primary keyword exactly once")
    expected_slug = slugify(keyword)
    if expected_slug and expected_slug not in plan.get("slug", ""):
        errors.append("plan slug does not preserve the complete primary keyword")
    h2s = [item.get("h2", "") for item in plan.get("outline", []) if isinstance(item, dict)]
    if not any(phrase_count(h2, keyword) for h2 in h2s):
        errors.append("plan requires an H2 containing the complete primary keyword")
    editorial = "\n".join([plan.get("title", ""), plan.get("h1", ""), plan.get("description", ""), plan.get("slug", ""), *h2s])
    blocked_names = {"ZINGEAR", "ZING EAR"}
    if config:
        blocked_names.update(
            str(name).strip()
            for name in config.get("program", {}).get("excluded_brand_terms", [])
            if str(name).strip()
        )
    for name in sorted(blocked_names):
        if re.search(r"(?<!\w)" + re.escape(name) + r"(?!\w)", editorial, re.IGNORECASE):
            errors.append(f"zero-brand violation: {name}")
    return errors


def has_explicit_evidence_boundary(source_pack: dict[str, Any]) -> bool:
    uncovered = list((source_pack.get("coverage") or {}).get("uncovered_terms") or [])
    constraints = " ".join(str(item) for item in source_pack.get("writing_constraints", [])).casefold()
    return bool(uncovered) and (
        "uncovered" in constraints
        and ("unknown" in constraints or "omit" in constraints or "inference" in constraints)
    )


def source_pack_errors(article: dict[str, Any], source_pack: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    uncovered = list((source_pack.get("coverage") or {}).get("uncovered_terms") or [])
    evidence_bounded = has_explicit_evidence_boundary(source_pack)
    if uncovered and not evidence_bounded:
        errors.append(f"source pack has uncovered center-topic terms: {uncovered}")
    claims = {item["claim_id"]: item for item in source_pack.get("claims", [])}
    sources = {item["source_id"]: item for item in source_pack.get("sources", [])}
    allowed_source_types = {
        "standard", "regulator", "government", "intergovernmental", "academic", "encyclopedia",
        "manufacturer", "technical_guide", "commercial_technical", "patent",
    }
    prohibited_sources = sorted(
        source_id for source_id, source in sources.items()
        if source.get("source_type") not in allowed_source_types
    )
    if prohibited_sources:
        errors.append(f"unsupported source types: {prohibited_sources}")
    used = set(article.get("used_claim_ids", []))
    unknown_claims = used - claims.keys()
    if unknown_claims:
        errors.append(f"article uses claims outside its source pack: {sorted(unknown_claims)}")
    blocked = sorted(claim_id for claim_id in used if claims.get(claim_id, {}).get("status") != "accepted")
    if blocked:
        errors.append(f"article uses non-accepted claims: {blocked}")
    article_sources = article.get("sources", [])
    article_source_ids_list = [item.get("source_id") for item in article_sources]
    article_source_ids = set(article_source_ids_list)
    if len(article_source_ids_list) != len(article_source_ids):
        errors.append("article source IDs must be unique")
    required_sources = {source_id for claim_id in used for source_id in claims.get(claim_id, {}).get("source_ids", [])}
    if not required_sources.issubset(article_source_ids):
        errors.append(f"article omits sources for used claims: {sorted(required_sources - article_source_ids)}")
    if not article_source_ids.issubset(sources.keys()):
        errors.append(f"article cites sources outside its source pack: {sorted(article_source_ids - sources.keys())}")
    for item in article_sources:
        expected = sources.get(item.get("source_id"))
        if not expected:
            continue
        changed_fields = [
            field for field in ("title", "publisher", "url")
            if item.get(field) != expected.get(field)
        ]
        if changed_fields:
            errors.append(
                f"article source metadata differs from source pack for {item.get('source_id')}: {changed_fields}"
            )
    # Scan against the authoritative source-pack aliases directly. The
    # model-provided alias list is metadata, not a second source of truth.
    required_block_names = {name for source in sources.values() for name in source.get("editorial_block_names", [])}
    editorial = "\n".join([
        str(article.get("title", "")),
        str(article.get("h1", "")),
        str(article.get("description", "")),
        str(article.get("slug", "")),
        str(article.get("body_markdown", "")),
    ])
    for name in sorted(required_block_names):
        pattern = re.compile(r"(?<!\w)" + re.escape(name) + r"(?!\w)", re.IGNORECASE)
        if pattern.search(editorial):
            errors.append(f"zero-brand violation: {name}")
    return errors


def _plain_markdown(value: str) -> str:
    value = re.sub(r"```.*?```", " ", value, flags=re.DOTALL)
    value = re.sub(r"!\[([^]]*)\]\([^)]+\)", r"\1", value)
    value = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", value)
    value = re.sub(r"^#{1,6}\s+", "", value, flags=re.MULTILINE)
    value = re.sub(r"[`*_>]", "", value)
    return re.sub(r"\s+", " ", value).strip()
