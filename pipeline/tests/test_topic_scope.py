from __future__ import annotations

import sys
import unittest
from pathlib import Path

PIPELINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE))

from topic_scope import classify_keyword, off_topic_reason


class TopicScopeTests(unittest.TestCase):
    def test_approved_direct_terms_are_accepted(self) -> None:
        for keyword in (
            "air fryer micro switch",
            "micro switch in a car",
            "snap-action switch operating force",
            "miniature basic switch travel",
        ):
            self.assertEqual(classify_keyword(keyword).decision, "accept", keyword)

    def test_non_direct_and_explicit_drift_are_rejected(self) -> None:
        for keyword in (
            "wireless kinetic switch",
            "marine push button switch panel",
            "frigidaire affinity dryer door switch",
            "hall effect limit switch",
        ):
            self.assertEqual(classify_keyword(keyword).decision, "reject", keyword)

    def test_explicit_drift_precedes_direct_allow_rule(self) -> None:
        result = classify_keyword("wireless kinetic switch with micro switch")
        self.assertEqual(result.decision, "reject")
        self.assertEqual(result.scope_class, "explicit_drift")

    def test_models_brands_and_commercial_terms_are_held(self) -> None:
        self.assertEqual(classify_keyword("F4T7UL micro switch").decision, "hold")
        self.assertEqual(classify_keyword("Acme micro switch", ["acme"]).decision, "hold")
        self.assertEqual(classify_keyword("best micro switch to buy").decision, "hold")
        self.assertEqual(classify_keyword("ip67 micro switch").decision, "accept")


if __name__ == "__main__":
    unittest.main()
