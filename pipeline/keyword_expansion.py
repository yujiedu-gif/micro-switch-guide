from __future__ import annotations

import re
from collections import defaultdict
from typing import Any, Iterable

from core import normalize_keyword, stable_id


MATERIAL_VERSION = "keyword-materials-v1"
GENERATOR_VERSION = "keyword-expansion-v1"
RELATION_VERSION = "micro-relation-v1"


DENY_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("keyboard", re.compile(
        r"\b(?:keyboard|keychron|cherry mx|gateron|wooting|kailh|topre|keycap|"
        r"mechanical key|keyboard switch)\b", re.I)),
    ("household_wiring", re.compile(
        r"\b(?:light switch|wall switch|outlet|gfci|dimmer|receptacle|junction box|"
        r"wireless kinetic switch)\b", re.I)),
    ("distribution_switchgear", re.compile(
        r"\b(?:transfer switch|disconnect switch|circuit breaker|breaker switch|switchgear|"
        r"distribution panel)\b", re.I)),
    ("gaming", re.compile(r"\b(?:nintendo|switch game|zelda|switch dock|switch case)\b", re.I)),
    ("guitar", re.compile(r"\b(?:guitar|humbucker|telecaster|stratocaster|pickup switch)\b", re.I)),
    ("generic_panel", re.compile(r"\b(?:marine|boat|auxbeam|switch panel)\b", re.I)),
)


APPLIANCE_ENTITIES = (
    "clothes dryer", "dryer", "dishwasher", "washer", "washing machine", "microwave",
    "oven", "refrigerator", "freezer", "air fryer", "rice cooker",
)
INDUSTRIAL_ENTITIES = (
    "cnc", "conveyor", "elevator", "linear actuator", "valve", "robot",
    "vending machine", "machine tool",
)
AUTOMOTIVE_ENTITIES = (
    "brake pedal", "clutch pedal", "door jamb", "power window", "power seat", "hood latch",
)
SENSOR_ALTERNATIVES = (
    "hall effect sensor", "hall effect switch", "reed switch", "proximity switch",
    "optical switch", "photoelectric switch",
)


TASK_TEMPLATES: dict[str, tuple[tuple[str, str, str], ...]] = {
    "application": (
        ("explain_function", "{base} function", "low"),
        ("explain_mechanism", "how does {base} work", "low"),
        ("diagnose_symptoms", "{base} symptoms", "low"),
        ("diagnose_causes", "{base} failure causes", "low"),
        ("test_continuity", "how to test {base}", "medium"),
        ("continuity_test", "{base} continuity test", "medium"),
    ),
    "industrial": (
        ("explain_function", "{base} function", "low"),
        ("explain_mechanism", "how does {base} work", "low"),
        ("diagnose_symptoms", "{base} symptoms", "low"),
        ("diagnose_causes", "{base} failure causes", "low"),
        ("test_continuity", "how to test {base}", "medium"),
        ("adjust", "{base} adjustment", "medium"),
        ("select", "how to select {base}", "medium"),
    ),
    "technical": (
        ("explain_function", "{base} function", "low"),
        ("explain_mechanism", "how does {base} work", "low"),
        ("test_continuity", "how to test {base}", "low"),
        ("adjust", "{base} adjustment", "medium"),
        ("select", "how to select {base}", "medium"),
        ("diagnose_causes", "{base} failure causes", "low"),
        ("maintain", "{base} maintenance", "low"),
    ),
    "comparison": (
        ("compare", "{base}", "low"),
        ("select_for_position_detection", "{base} for position detection", "low"),
    ),
}


def _normalize_words(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", normalize_keyword(value)).strip()


def blocked_context(value: str) -> str | None:
    normalized = _normalize_words(value)
    for reason, pattern in DENY_PATTERNS:
        if pattern.search(normalized):
            return reason
    return None


def _first_term(value: str, terms: Iterable[str]) -> str | None:
    for term in sorted(terms, key=len, reverse=True):
        if re.search(r"(?<!\w)" + re.escape(term) + r"(?!\w)", value):
            return term
    return None


def extract_material(keyword_id: str, keyword: str) -> dict[str, Any]:
    normalized = _normalize_words(keyword)
    denied = blocked_context(normalized)
    symptom = _first_term(normalized, (
        "intermittent", "not working", "no continuity", "stuck", "clicking", "failure", "fault", "symptoms",
    ))
    parameter = _first_term(normalized, (
        "operating force", "differential travel", "pretravel", "overtravel", "contact rating",
        "mechanical life", "electrical life", "temperature", "voltage", "current", "ip rating",
    ))
    environment = _first_term(normalized, (
        "high temperature", "low temperature", "waterproof", "dust", "vibration", "outdoor", "humid",
    ))
    reader_task = None
    for task, pattern in (
        ("test", r"\b(?:test|continuity|check)\b"),
        ("adjust", r"\b(?:adjust|adjustment)\b"),
        ("replace", r"\b(?:replace|replacement)\b"),
        ("diagnose", r"\b(?:symptom|fault|failure|troubleshoot|not working)\b"),
        ("wire", r"\b(?:wire|wiring)\b"),
        ("select", r"\b(?:select|selection|choose)\b"),
        ("explain", r"\b(?:what is|how does|function|working principle)\b"),
    ):
        if re.search(pattern, normalized):
            reader_task = task
            break
    record: dict[str, Any] = {
        "keyword_id": keyword_id,
        "keyword": keyword,
        "normalized_keyword": normalize_keyword(keyword),
        "material_version": MATERIAL_VERSION,
        "entity": None,
        "component": None,
        "function": None,
        "symptom": symptom,
        "parameter": parameter,
        "environment": environment,
        "reader_task": reader_task,
        "relation_type": None,
        "base_keyword": None,
        "decision": "reject",
        "reason_codes": [],
    }
    if denied:
        record["reason_codes"] = [f"blocked_context:{denied}"]
        return record

    entity = _first_term(normalized, APPLIANCE_ENTITIES)
    component = _first_term(normalized, ("door", "lid", "interlock", "safety"))
    if entity and component:
        canonical_entity = "clothes dryer" if entity in {"dryer", "clothes dryer"} else entity
        if component in {"interlock", "safety"}:
            component = {
                "clothes dryer": "door", "dishwasher": "door", "microwave": "door",
                "oven": "door", "refrigerator": "door", "freezer": "door",
                "rice cooker": "lid",
            }.get(canonical_entity)
        if component is None:
            record["reason_codes"] = ["ambiguous_application_component"]
            return record
        if component == "lid" and canonical_entity not in {"washer", "washing machine", "rice cooker"}:
            record["reason_codes"] = ["unsupported_application_component"]
            return record
        record.update({
            "entity": canonical_entity.replace(" ", "_"),
            "component": "door_interlock" if component == "door" else "lid_interlock",
            "function": "detect_closed_state",
            "relation_type": "direct_application",
            "base_keyword": f"{canonical_entity} {component} micro switch",
            "decision": "accept",
        })
        return record

    entity = _first_term(normalized, INDUSTRIAL_ENTITIES)
    if entity and re.search(r"\b(?:limit switch|travel limit|end ?stop|position)\b", normalized):
        record.update({
            "entity": entity.replace(" ", "_"),
            "component": "travel_limit",
            "function": "position_or_end_of_travel_detection",
            "relation_type": "direct_application",
            "base_keyword": f"{entity} micro limit switch",
            "decision": "accept",
        })
        return record

    entity = _first_term(normalized, AUTOMOTIVE_ENTITIES)
    if entity and re.search(r"\b(?:switch|sensor|position|interlock)\b", normalized):
        record.update({
            "entity": entity.replace(" ", "_"),
            "component": entity.replace(" ", "_"),
            "function": "mechanical_state_detection",
            "relation_type": "direct_application",
            "base_keyword": f"{entity} micro switch",
            "decision": "accept",
        })
        return record

    alternative = _first_term(normalized, SENSOR_ALTERNATIVES)
    if alternative:
        record.update({
            "entity": alternative.replace(" ", "_"),
            "function": "position_detection",
            "relation_type": "bounded_comparison",
            "base_keyword": f"micro switch vs {alternative}",
            "decision": "accept",
        })
        return record

    if re.search(r"\b(?:limit switch|travel limit|end ?stop)\b", normalized):
        modifier = _first_term(normalized, (
            "roller lever", "heavy duty", "adjustable", "waterproof", "miniature",
            "precision", "plunger", "sealed", "roller", "lever", "end stop", "travel",
        ))
        base = f"{modifier} micro limit switch" if modifier else "micro limit switch"
        record.update({
            "entity": "micro_limit_switch",
            "component": (modifier or "general").replace(" ", "_"),
            "function": "position_or_end_of_travel_detection",
            "relation_type": "direct_technical",
            "base_keyword": base,
            "decision": "accept",
        })
        return record

    record["reason_codes"] = ["no_supported_relation_pattern"]
    return record


def material_rows(rows: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    return [extract_material(str(row["keyword_id"]), str(row["keyword"])) for row in rows]


def _template_group(material: dict[str, Any]) -> str:
    if material["relation_type"] == "bounded_comparison":
        return "comparison"
    if material["relation_type"] == "direct_technical":
        return "technical"
    if material.get("entity") in {item.replace(" ", "_") for item in INDUSTRIAL_ENTITIES}:
        return "industrial"
    return "application"


def _canonical_base(material: dict[str, Any]) -> str:
    entity = str(material.get("entity") or "").replace("_", " ")
    component = str(material.get("component") or "")
    relation = material.get("relation_type")
    if relation == "direct_application":
        if component == "door_interlock":
            return f"{entity} door micro switch"
        if component == "lid_interlock":
            return f"{entity} lid micro switch"
        if component == "travel_limit":
            return f"{entity} micro limit switch"
        return f"{entity} micro switch"
    return str(material["base_keyword"])


def expansion_candidates(
    materials: Iterable[dict[str, Any]], existing_normalized: set[str]
) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str, str, str, str], set[str]] = defaultdict(set)
    variants: dict[tuple[str, str, str, str, str], set[str]] = defaultdict(set)
    metadata: dict[tuple[str, str, str, str, str], dict[str, Any]] = {}
    for material in materials:
        if material.get("decision") != "accept" or not material.get("base_keyword"):
            continue
        group = _template_group(material)
        for reader_task, template, risk in TASK_TEMPLATES[group]:
            keyword = template.format(base=_canonical_base(material))
            normalized = normalize_keyword(keyword)
            if blocked_context(normalized):
                continue
            key = (
                str(material.get("entity") or ""),
                str(material.get("component") or ""),
                str(material.get("function") or ""),
                reader_task,
                str(material["relation_type"]),
            )
            grouped[key].add(str(material["keyword_id"]))
            variants[key].add(str(material["base_keyword"]))
            metadata[key] = {
                "candidate_keyword": keyword,
                "normalized_keyword": normalized,
                "entity": material.get("entity"),
                "component": material.get("component"),
                "function": material.get("function"),
                "reader_task": reader_task,
                "answer_type": reader_task,
                "relation_type": material["relation_type"],
                "template_id": f"{group}:{reader_task}:v1",
                "risk_level": risk,
            }

    candidates: list[dict[str, Any]] = []
    for key in sorted(grouped):
        item = metadata[key]
        normalized = item["normalized_keyword"]
        origins = sorted(grouped[key])
        already_exists = normalized in existing_normalized
        decision = "reject" if already_exists else ("accept" if item["risk_level"] == "low" else "hold")
        reasons = ["already_exists"] if already_exists else ([] if decision == "accept" else ["requires_authoritative_evidence"])
        signature = "|".join([
            str(item.get("entity") or ""), str(item.get("component") or ""),
            str(item.get("function") or ""), str(item["reader_task"]), str(item["answer_type"]),
        ])
        candidates.append({
            "candidate_id": stable_id("kwc", f"{GENERATOR_VERSION}:{normalized}"),
            **item,
            "origin_keyword_ids": origins,
            "source_variants": sorted(variants[key]),
            "content_signature": signature,
            "generator_version": GENERATOR_VERSION,
            "relation_version": RELATION_VERSION,
            "decision": decision,
            "reason_codes": reasons,
            "validation_status": "pending_demand_and_evidence" if decision == "accept" else decision,
        })
    return candidates
