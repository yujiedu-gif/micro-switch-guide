from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

PIPELINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE))

from content_ops import cluster_vectors, exclusion_reason, hamming_distance, minhash_signature, minhash_similarity, simhash
from core import Paths, Store, nofollow_external_links, normalize_keyword, render_post, slugify


class CoreTests(unittest.TestCase):
    def test_external_links_are_nofollow(self) -> None:
        markdown = (
            "[source](https://example.com/reference) and "
            "[internal](https://www.microswitchguide.com/guides/example/)"
        )
        rendered = nofollow_external_links(markdown)
        self.assertIn(
            '[source](https://example.com/reference){: rel="nofollow noopener noreferrer" }',
            rendered,
        )
        self.assertIn(
            "[internal](https://www.microswitchguide.com/guides/example/)",
            rendered,
        )
        self.assertNotIn(
            '[internal](https://www.microswitchguide.com/guides/example/){:',
            rendered,
        )

    def test_rendered_sources_are_nofollow(self) -> None:
        article = {
            "title": "Example",
            "description": "Example description",
            "category": "Basics",
            "tags": ["micro switch"],
            "body_markdown": "Body.",
            "sources": [{"publisher": "Authority", "title": "Reference", "url": "https://example.com/reference"}],
        }
        rendered = render_post(article, __import__("datetime").date(2026, 10, 11), "editorial_team", "+0800")
        self.assertIn(
            '[Reference](https://example.com/reference){: rel="nofollow noopener noreferrer" }',
            rendered,
        )

    def test_render_post_removes_duplicate_leading_h1(self) -> None:
        article = {
            "title": "Micro Switch Troubleshooting",
            "description": "Example description",
            "category": "Basics",
            "tags": ["micro switch"],
            "body_markdown": "# Micro Switch Troubleshooting\n\nIntroduction.\n\n## First check\n\nDetails.",
        }
        rendered = render_post(article, __import__("datetime").date(2026, 10, 11), "editorial_team", "+0800")
        self.assertNotIn("# Micro Switch Troubleshooting", rendered)
        self.assertIn("Introduction.\n\n## First check", rendered)

    def test_keyword_normalization(self) -> None:
        self.assertEqual(normalize_keyword(" MicroSwitch—Wiring "), "micro switch-wiring")
        self.assertEqual(slugify("Micro Switch Wiring"), "micro-switch-wiring")

    def test_commercial_and_off_topic_filters(self) -> None:
        for keyword in (
            "best micro switch manufacturers", "micro switch wholesale price",
            "best micro switch for mouse", "micro switches amazon",
            "u83161 3 micro switch", "micro switch AML 20 series",
            "micro switch 91929", "mqs 216 microswitch", "83170.4 microswitch",
            "micro switches srl", "microswitch a leva",
        ):
            self.assertTrue(exclusion_reason(keyword).startswith("scope_hold:"), keyword)
        self.assertTrue(exclusion_reason("weather tomorrow").startswith("scope_reject:"))
        self.assertIsNone(exclusion_reason("micro switch operating force explained"))
        self.assertIsNone(exclusion_reason("10a 250vac micro switch"))
        self.assertIsNone(exclusion_reason("ip67 micro switch"))
        self.assertIsNone(exclusion_reason("what is a snap-action switch"))
        self.assertIsNone(exclusion_reason("micro limit switch wiring"))
        self.assertIsNone(exclusion_reason("miniature basic switch"))
        self.assertIsNone(exclusion_reason("electromechanical snap action switches"))
        self.assertTrue(exclusion_reason("furnace limit switch wiring").startswith("scope_reject:"))

    def test_greedy_clustering(self) -> None:
        rows = [
            {"id": "a", "vector": [1.0, 0.0]},
            {"id": "b", "vector": [0.99, 0.01]},
            {"id": "c", "vector": [0.0, 1.0]},
        ]
        clusters = cluster_vectors(rows, 0.93)
        self.assertEqual([[item["id"] for item in cluster] for cluster in clusters], [["a", "b"], ["c"]])

    def test_simhash_is_deterministic(self) -> None:
        text = "A micro switch uses a snap action mechanism. " * 20
        self.assertEqual(simhash(text), simhash(text))
        self.assertEqual(hamming_distance(simhash(text), simhash(text)), 0)

    def test_minhash_detects_reused_passages(self) -> None:
        original = " ".join(f"A micro switch example {index} explains snap action contact behavior." for index in range(100))
        lightly_edited = original + "This final sentence is new."
        unrelated = "Marine weather patterns and cloud formation vary across oceans. " * 20
        self.assertGreaterEqual(minhash_similarity(minhash_signature(original), minhash_signature(lightly_edited)), 0.85)
        self.assertLess(minhash_similarity(minhash_signature(original), minhash_signature(unrelated)), 0.3)

    def test_budget_is_idempotent_and_blocks_overage(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "pipeline").mkdir()
            (root / "pipeline" / "schema.sql").write_text((PIPELINE / "schema.sql").read_text())
            store = Store(Paths(root))
            store.initialize()
            run_id = store.create_run("c" * 64, "s" * 64)
            self.assertEqual(store.record_cost(run_id, "dataforseo", "x", 1.5, 4, "req-1"), 1.5)
            self.assertEqual(store.record_cost(run_id, "dataforseo", "x", 1.5, 4, "req-1"), 1.5)
            with self.assertRaises(RuntimeError):
                store.record_cost(run_id, "dataforseo", "x", 3.0, 4, "req-2")


if __name__ == "__main__":
    unittest.main()
