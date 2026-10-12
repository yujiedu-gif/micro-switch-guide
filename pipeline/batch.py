from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from core import canonical_json, load_json, sanitize_schema_for_strict, sha256_bytes, write_jsonl


SYSTEM_PROMPTS = {
    "plan": """You plan neutral, evidence-bound educational pages for MicroSwitchGuide.

# Plan contract
- Copy primary_keyword from the payload exactly; do not reorder, rewrite, or change it.
- Set topic_scope.primary_entity=micro_switch, relation=direct, and owned_question_is_direct=true. The owned question must directly ask about the micro switch itself, not merely an adjacent device that might contain one.
- title and h1 must be identical and must contain the complete primary_keyword contiguously.
- description must target 150-155 characters (the hard acceptance range is 140-160). It must begin with primary_keyword copied as one contiguous literal substring, followed immediately by a colon, and that complete substring must occur exactly once. Do this even when the keyword is phrased as a question; never omit, reorder, or grammatically rewrite one of its words.
- slug must contain the complete lowercase hyphenated primary_keyword. Do not drop its words.
- At least one outline h2 must contain the complete primary_keyword contiguously.
- Set reader_task and answer_type to short lowercase snake_case identifiers, not prose sentences. Build content_signature as normalized_primary_keyword|reader_task|answer_type, using the complete primary keyword in lowercase snake_case as the first segment and copying reader_task and answer_type exactly as the second and third segments. Local normalization is authoritative.
- Supply at least two differentiation_anchors that require this page to use a distinct mechanism, failure path, parameter boundary, or verification path. A title variation is not an anchor.
- Give every outline item a section_role and copy those roles, in order, to section_roles. Do not reuse a generic outline merely by replacing the equipment name.
- When the payload says conditional_language_required, describe only designs that use the stated micro switch; never generalize the component to every device in that class.
- Keep all editorial fields educational and free of brands, manufacturers, suppliers, factories, marketplaces, and commercial series. An exact model identifier is allowed only when it appears in the supplied primary keyword; do not introduce other models.
Count description characters including spaces and punctuation, then verify every rule. Return only JSON matching the response schema.""",
    "article": """You write neutral, precise American-English educational articles for MicroSwitchGuide.

# Evidence and scope
- Use only accepted claims supplied by the user. Preserve every number, unit, AC/DC distinction, load type, state reference, test condition, definition, and scope qualifier.
- If evidence is insufficient, omit or qualify the claim. Never invent a specification, compatibility statement, certification, safety instruction, model identity, or application.
- Do not rank, recommend, promote, or make a manufacturer, supplier, distributor, brand, factory, marketplace, or commercial series the editorial subject. Commercial technical evidence may be used only within the supplied claim scope; source attribution is assembled locally.
- An approved model identifier may appear only when it is in the supplied keyword. Without exact-model evidence, leave identity, rating, dimensions, terminals, compatibility, manufacturer, and application unresolved.

# Writing contract
- Work in two internal passes: draft, then audit the draft for logical consistency, parameter support, definition accuracy, zero-brand compliance, and topic purity. Silently fix every issue before returning the final JSON.
- Follow the approved outline and owned question. Do not answer excluded questions in depth.
- Preserve the approved reader_task, answer_type, differentiation_anchors, and section_roles. Do not reproduce the owned question or section-role combination listed in avoid_content_identities.
- Shared definitions may be concise, but the mechanism, failure path, verification path, and conclusion must follow this plan's differentiation anchors rather than a reusable equipment-name template.
- Follow word_budget. The local validator accepts 1,000-2,000 English words. Do not use an em dash, generic industry opening, marketing CTA, or exposed workflow note.
- Use the complete primary_keyword in sentence 1 or 2, within the first 150 words, in at least one H2, and exactly once in the closing section.
- Return only body_markdown, the unique IDs of claims actually used, and the five self_review booleans. Set a boolean true only after the final prose passes that check. Return only JSON matching the response schema.""",
    "review": """You are the final semantic auditor for MicroSwitchGuide. Review only; never rewrite the article.

# Review contract
- The hard pass gate is logical_consistency, parameter_accuracy, definition_accuracy, and zero_brand. reader_task_alignment, h2_fulfillment, and owned_question_uniqueness are advisory signals because deterministic structure and duplicate systems enforce them separately.
- For logical_consistency, fail contradictions, invalid causal steps, incompatible premises and conclusions, state-sequence errors, or sections whose conclusions do not follow from their stated evidence.
- For parameter_accuracy, audit every number, unit, tolerance, range, rating, AC/DC distinction, load type, temperature, test method, duration, operating state, and applicability condition. Fail omitted or transferred conditions.
- For definition_accuracy, compare every technical definition with the supplied claim scope. Fail altered meanings, missing state references, category/model generalization, or the use of one defined term as another.
- Unsupported positive factual claims are hard failures under the most relevant of those three checks. Style, repetition, heading quality, and breadth are not hard failures unless they create a logical or definitional contradiction.
- A statement that supplied evidence does not establish a fact is an allowed epistemic boundary, not an unsupported positive claim. An identifier-verification page may explain which fields remain unknown without external evidence for the mere absence of evidence.
- Do not fail on internal-link existence or uniqueness; those are validated by the link graph and duplicate pipeline.
- Commercial publishers may appear in structured source metadata. Fail zero_brand only when the editorial prose ranks, recommends, promotes, or uses a source name outside neutral attribution. Source metadata is assembled locally and all rendered external links are `nofollow`.
- Return only JSON matching the response schema.""",
    "repair": """You repair one MicroSwitchGuide article exactly once. Correct only the supplied validation failures, preserve the approved owned question, and use only supplied evidence.

# Repair contract
- Repair every supplied validation failure while preserving the approved owned_question and using only supplied evidence.
- Recheck exact-keyword placement, description length, word count, internal links, source mapping, zero-brand policy, and prohibited phrasing. Return only JSON matching the response schema.""",
}


def build_batch_requests(
    kind: str,
    inputs: list[dict[str, Any]],
    model: str,
    skill_text: str,
    schema: dict[str, Any],
    max_output_tokens: int,
) -> list[dict[str, Any]]:
    if kind not in {"plan", "article", "review", "repair"}:
        raise ValueError("kind must be plan, article, review, or repair")
    strict_schema = sanitize_schema_for_strict(schema)
    # The complete repository Skill remains the human-readable operating
    # policy. Batch requests use a compact stage-specific compilation so the
    # model does not repeatedly receive publishing, tooling, and workflow text.
    del skill_text
    fixed_prefix = SYSTEM_PROMPTS[kind]
    cache_key = f"microswitchguide:{kind}:{sha256_bytes(fixed_prefix.encode('utf-8'))[:20]}"
    rows = []
    seen = set()
    for index, item in enumerate(inputs, 1):
        custom_id = item.get("custom_id") or f"msg-{kind}-{index:06d}"
        if custom_id in seen:
            raise ValueError(f"duplicate custom_id: {custom_id}")
        seen.add(custom_id)
        payload = item.get("payload", item)
        user_text = canonical_json(payload)
        rows.append(
            {
                "custom_id": custom_id,
                "method": "POST",
                "url": "/v1/responses",
                "body": {
                    "model": model,
                    "input": [
                        {
                            "role": "system",
                            "content": [{"type": "input_text", "text": fixed_prefix, "prompt_cache_breakpoint": {"mode": "explicit"}}],
                        },
                        {"role": "user", "content": user_text},
                    ],
                    "prompt_cache_key": cache_key,
                    "prompt_cache_options": {"mode": "explicit", "ttl": "30m"},
                    "text": {
                        "format": {
                            "type": "json_schema",
                            "name": f"microswitchguide_{kind}",
                            "schema": strict_schema,
                            "strict": True,
                        }
                    },
                    "reasoning": {"effort": "none"},
                    "max_output_tokens": max_output_tokens,
                },
            }
        )
    return rows


def write_batch(path: Path, rows: list[dict[str, Any]]) -> dict[str, Any]:
    count = write_jsonl(path, rows)
    size = path.stat().st_size
    if count > 50_000:
        raise ValueError("batch exceeds 50,000 requests")
    if size > 200 * 1024 * 1024:
        raise ValueError("batch exceeds 200 MB")
    return {
        "path": str(path),
        "requests": count,
        "bytes": size,
        "sha256": sha256_bytes(path.read_bytes()),
    }


def extract_response_json(line: dict[str, Any]) -> tuple[str, dict[str, Any] | None, dict[str, Any] | None]:
    custom_id = line.get("custom_id")
    if not custom_id:
        raise ValueError("batch output line lacks custom_id")
    if line.get("error"):
        return custom_id, None, line["error"]
    response = line.get("response") or {}
    if response.get("status_code") != 200:
        return custom_id, None, {"code": "http_error", "response": response}
    body = response.get("body") or {}
    for output in body.get("output", []):
        if output.get("type") != "message":
            continue
        for content in output.get("content", []):
            if content.get("type") == "refusal":
                return custom_id, None, {"code": "refusal", "message": content.get("refusal")}
            if content.get("type") == "output_text" and content.get("text"):
                try:
                    return custom_id, json.loads(content["text"]), None
                except json.JSONDecodeError as exc:
                    return custom_id, None, {"code": "invalid_json", "message": str(exc)}
    return custom_id, None, {"code": "missing_output_text", "body_status": body.get("status")}


def schema_for_kind(pipeline_root: Path, kind: str) -> dict[str, Any]:
    filename = {"plan": "article-plan.schema.json", "article": "article.schema.json", "review": "article-review.schema.json"}.get(kind, "article.schema.json")
    return load_json(pipeline_root / "schemas" / filename)
