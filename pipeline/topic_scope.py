from __future__ import annotations

import re
from dataclasses import asdict, dataclass
from typing import Iterable


CLASSIFIER_VERSION = "strict-direct-v1"


def normalize_scope_text(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.casefold()).strip()


DIRECT_TERM = re.compile(
    r"\b(?:micro switch(?:es)?|microswitch(?:es)?|micro limit switch(?:es)?|"
    r"snap action switch(?:es)?|(?:miniature|subminiature) basic switch(?:es)?)\b",
    re.IGNORECASE,
)


EXPLICIT_DRIFT: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("keyboard_or_keyboard_switch", re.compile(
        r"\b(?:keyboards?|keycaps?|mechanical keyboard|keyboard switch(?:es)?|key switch tester|"
        r"wooting|keychron|epomaker|topre|gateron|romer g|cherry mx|akko|kailh|outemu|"
        r"holy panda|magic refiner)\b", re.I)),
    ("guitar_electronics", re.compile(
        r"\b(?:humbuckers?|telecaster|stratocaster|guitars?|les paul|guitar kill switch|"
        r"pickups?|footswitch wiring|way blade switch)\b", re.I)),
    ("household_lighting_or_outlet_wiring", re.compile(
        r"\b(?:light switch(?:es)?|light fixture(?:s)?|outlet box(?:es)?|electrical outlet(?:s)?|"
        r"wall outlet(?:s)?|receptacle(?:s)?|gfci|junction box(?:es)?|dimmer switch(?:es)?|"
        r"wall switch(?:es)?|wireless kinetic switch(?:es)?|wireless light switch(?:es)?|"
        r"lighting circuit|lamp cord|pull chain switch|inline switch for lamp)\b", re.I)),
    ("gaming_or_entertainment_drift", re.compile(
        r"\b(?:nintendo|switch dock|switch carrying case|switch game|force academy|"
        r"shining force|thunder force|bro force|game travel case)\b", re.I)),
    ("unrelated_micro_term", re.compile(
        r"\b(?:micro machines|arduino pro micro|micro sd card switcher|micro bit|kvm switch)\b", re.I)),
)


COMMERCIAL_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("supplier_intent", re.compile(r"\b(?:supplier|suppliers|distributor|distributors|vendor|vendors)\b", re.I)),
    ("manufacturer_intent", re.compile(r"\b(?:manufacturer|manufacturers|factory|factories|oem|odm)\b", re.I)),
    ("transactional_intent", re.compile(r"\b(?:buy|price|pricing|quote|for sale|near me|wholesale|bulk order)\b", re.I)),
    ("ranking_intent", re.compile(r"\b(?:best|top|leading)\b", re.I)),
    ("marketplace_intent", re.compile(r"\b(?:amazon|ebay|aliexpress|alibaba|temu|walmart|grainger|digikey|mouser|newark)\b", re.I)),
    ("commercial_entity", re.compile(r"\b(?:company|companies|corp|corporation|llc|ltd|limited|srl)\b", re.I)),
    ("non_english", re.compile(r"\b(?:a leva|a rotella|bistabilny|para mouse|4 pines|vulcano)\b", re.I)),
)


_TECHNICAL_ALNUM = re.compile(
    r"^(?:ip\d{2,3}|\d+(?:\.\d+)?(?:a|v|vac|vdc|w|kw|ma|mv|amp|amps|volt|volts|mm|cm|in|inch|inches))$",
    re.I,
)


def looks_like_product_model(normalized: str) -> bool:
    if re.search(r"\b(?:model|part|series)\s*(?:number|no)?\s*[a-z0-9]*\d[a-z0-9]*\b", normalized, re.I):
        return True
    if re.search(r"\b[a-z][a-z0-9 ]*\s+\d+[a-z0-9 ]*\s+series\b", normalized, re.I):
        return True
    if re.search(r"\b(?!(?:ip|ac|dc)\b)[a-z]{1,4}\s+\d{2,}\b", normalized, re.I):
        return True
    for token in re.findall(r"[a-z0-9]+(?:\.[a-z0-9]+)?", normalized, re.I):
        if _TECHNICAL_ALNUM.fullmatch(token):
            continue
        if re.fullmatch(r"\d{4,}(?:\.\d+)?", token):
            return True
        if any(char.isalpha() for char in token) and any(char.isdigit() for char in token):
            return True
    return False


@dataclass(frozen=True)
class ScopeDecision:
    decision: str
    scope_class: str
    reason_codes: tuple[str, ...]
    classifier_version: str = CLASSIFIER_VERSION

    def to_dict(self) -> dict[str, object]:
        value = asdict(self)
        value["reason_codes"] = list(self.reason_codes)
        return value


def classify_keyword(keyword: str, known_brands: Iterable[str] = (), intent: str | None = None) -> ScopeDecision:
    normalized = normalize_scope_text(keyword)
    for reason, pattern in EXPLICIT_DRIFT:
        if pattern.search(normalized):
            return ScopeDecision("reject", "explicit_drift", (reason,))
    if not DIRECT_TERM.search(normalized):
        return ScopeDecision("reject", "non_direct", ("missing_direct_term",))

    reasons: list[str] = []
    for reason, pattern in COMMERCIAL_PATTERNS:
        if pattern.search(normalized):
            reasons.append(reason)
    # DataForSEO intent is retained as evidence but is not a hard gate.  It
    # frequently labels educational component queries (for example operating
    # force or actuator types) as commercial.  Explicit words in the query are
    # deterministic and auditable, so only those patterns create a hold.
    for brand in known_brands:
        normalized_brand = normalize_scope_text(brand)
        if normalized_brand and re.search(r"(?<!\w)" + re.escape(normalized_brand) + r"(?!\w)", normalized):
            reasons.append("brand_navigation")
            break
    if looks_like_product_model(normalized):
        reasons.append("product_model")
    if reasons:
        return ScopeDecision("hold", "model_or_brand", tuple(dict.fromkeys(reasons)))
    return ScopeDecision("accept", "direct_micro_switch", ())


def off_topic_reason(keyword: str) -> str | None:
    decision = classify_keyword(keyword)
    return decision.reason_codes[0] if decision.decision == "reject" else None


def scope_decision(keyword: str) -> tuple[str, str | None]:
    result = classify_keyword(keyword)
    return result.decision, result.reason_codes[0] if result.reason_codes else None
