from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

PIPELINE = Path(__file__).resolve().parents[1]
SKILL = Path("/Users/yujiedu/.codex/skills/microswitchguide-content")
sys.path.insert(0, str(PIPELINE))

from content_ops import assemble_article_draft, build_internal_links, ingest_source_pack, missing_source_terms
from core import Paths, Store
from validators import article_policy_errors, normalize_plan_metadata, plan_policy_errors, reconcile_review_deterministic_checks, source_pack_errors, validate_schema


class SourceAndValidationTests(unittest.TestCase):
    def test_compact_draft_is_joined_with_authoritative_local_metadata(self) -> None:
        plan = {
            "primary_keyword": "micro switch basics", "secondary_keywords": [],
            "owned_question": "How does a micro switch work?", "title": "micro switch basics",
            "h1": "micro switch basics", "description": "x" * 145,
            "slug": "micro-switch-basics", "category": "Basics",
        }
        pack = {
            "claims": [{"claim_id": "c1", "source_ids": ["s1"], "status": "accepted"}],
            "sources": [{"source_id": "s1", "title": "Terms", "publisher": "Public Body", "url": "https://example.org/terms"}],
        }
        links = [{"target_job_id": "j2", "relation": "related", "anchor_text": "related guide", "url": "/guides/related/"}]
        article = assemble_article_draft(
            {"body_markdown": "micro switch basics begins.\n\n## micro switch basics—what it means\n\nText.\n\n## Final note\n\nmicro switch basics.", "used_claim_ids": ["c1"]},
            plan, pack, links,
        )
        self.assertEqual(article["title"], plan["title"])
        self.assertEqual(article["sources"][0]["source_id"], "s1")
        self.assertEqual(article["internal_links"], links)
        self.assertEqual(article["source_manufacturer_names"], [])
        self.assertNotIn("—", article["body_markdown"])
        self.assertIn("micro switch basics, what it means", article["body_markdown"])

    def test_commercial_source_name_is_kept_as_citation_guard_metadata(self) -> None:
        plan = {
            "primary_keyword": "micro switch basics", "secondary_keywords": [],
            "owned_question": "How does a micro switch work?", "title": "micro switch basics",
            "h1": "micro switch basics", "description": "x" * 145,
            "slug": "micro-switch-basics", "category": "Basics",
        }
        pack = {
            "claims": [{"claim_id": "c1", "source_ids": ["s1"], "status": "accepted"}],
            "sources": [{
                "source_id": "s1", "title": "Technical manual", "publisher": "Example Brand",
                "url": "https://example.com/manual", "source_type": "manufacturer",
                "editorial_block_names": ["Example Brand"],
            }],
        }
        article = assemble_article_draft(
            {"body_markdown": "micro switch basics.\n\n## micro switch basics\n\nText.\n\n## Final note\n\nmicro switch basics.", "used_claim_ids": ["c1"]},
            plan, pack, [],
        )
        self.assertEqual(article["source_manufacturer_names"], ["Example Brand"])
        self.assertEqual(article["sources"][0]["publisher"], "Example Brand")

    def test_plan_description_is_repaired_without_another_model_call(self) -> None:
        plan = {
            "primary_keyword": "what is a micro switch actuator",
            "description": "Learn what a micro switch actuator does and how movement affects operation.",
        }
        repaired = normalize_plan_metadata(plan)
        description = repaired["description"]
        self.assertTrue(140 <= len(description) <= 160)
        self.assertEqual(description.casefold().count(plan["primary_keyword"].casefold()), 1)
        self.assertTrue(description.startswith(plan["primary_keyword"] + ":"))

    def test_plan_identity_and_keyword_h2_are_normalized_locally(self) -> None:
        plan = {
            "primary_keyword": "assembly robot travel limit micro switch failure causes",
            "description": "assembly robot travel limit micro switch failure causes: " + "x" * 90,
            "reader_task": "diagnose_limit_switch_fault",
            "answer_type": "failure_diagnosis",
            "content_signature": "micro_switch|failure_diagnosis|failure_diagnosis",
            "outline": [{"h2": "What the travel-limit switch detects"}],
        }
        repaired = normalize_plan_metadata(plan)
        self.assertEqual(
            repaired["content_signature"],
            "assembly_robot_travel_limit_micro_switch_failure_causes|diagnose_limit_switch_fault|failure_diagnosis",
        )
        self.assertEqual(repaired["outline"][0]["h2"], plan["primary_keyword"])

    def test_article_cannot_rewrite_authoritative_source_metadata(self) -> None:
        pack = {
            "claims": [{"claim_id": "c", "status": "accepted", "source_ids": ["s"]}],
            "sources": [{
                "source_id": "s", "title": "Public terminology record",
                "publisher": "Public Standards Institution", "url": "https://example.org/public",
                "source_type": "standard", "editorial_block_names": [],
            }],
        }
        article = {
            "used_claim_ids": ["c"],
            "sources": [{
                "source_id": "s", "title": "Commercial product page",
                "publisher": "Example Brand", "url": "https://brand.example/product",
            }],
        }
        errors = source_pack_errors(article, pack)
        self.assertTrue(any("metadata differs" in error for error in errors))

    def test_uncovered_terms_are_allowed_only_with_explicit_evidence_boundaries(self) -> None:
        article = {"used_claim_ids": [], "sources": []}
        pack = {
            "coverage": {"uncovered_terms": ["device-specific adjustment procedure"]},
            "claims": [],
            "sources": [],
        }
        errors = source_pack_errors(article, pack)
        self.assertTrue(any("uncovered center-topic terms" in error for error in errors))

        pack["writing_constraints"] = [
            "Treat every uncovered evidence term as unknown rather than filling the gap by inference."
        ]
        errors = source_pack_errors(article, pack)
        self.assertFalse(any("uncovered center-topic terms" in error for error in errors))

    def test_configured_manufacturer_names_are_blocked_in_plan_and_article(self) -> None:
        config = {
            "program": {
                "article_word_min": 1,
                "article_word_max": 2000,
                "excluded_brand_terms": ["Omron"],
            }
        }
        plan = {
            "primary_keyword": "micro switch basics",
            "title": "Micro Switch Basics from Omron",
            "h1": "Micro Switch Basics from Omron",
            "description": "Micro switch basics explained with Omron examples.",
            "slug": "micro-switch-basics",
            "outline": [{"h2": "Micro switch basics"}],
        }
        self.assertTrue(any("zero-brand violation" in error for error in plan_policy_errors(plan, config)))
        article = {
            "primary_keyword": "micro switch basics",
            "title": "Micro Switch Basics",
            "h1": "Micro Switch Basics",
            "description": "Micro switch basics explains operating states, terminology, and practical interpretation for readers reviewing a simple switching mechanism.",
            "slug": "micro-switch-basics",
            "body_markdown": "Micro switch basics starts here.\n\n## Micro switch basics\n\nOmron is named.\n\n## Closing notes\n\nUse micro switch basics carefully.",
            "source_manufacturer_names": [],
            "internal_links": [],
        }
        self.assertTrue(any("zero-brand violation" in error for error in article_policy_errors(article, config)))

    def store(self, root: Path) -> Store:
        (root / "pipeline").mkdir()
        (root / "pipeline" / "schema.sql").write_text((PIPELINE / "schema.sql").read_text())
        store = Store(Paths(root))
        store.initialize()
        return store

    def test_source_pack_requires_scope_condition_for_manufacturer_claim(self) -> None:
        schema = json.loads((SKILL / "references" / "source-pack.schema.json").read_text())
        pack = {
            "topic_id": "t", "retrieved_at": "2026-10-09T00:00:00+00:00",
            "sources": [{"source_id": "s", "title": "Guide", "publisher": "Example", "url": "https://example.com/x", "source_type": "technical_guide", "retrieved_at": "2026-10-09T00:00:00+00:00", "content_hash": "a" * 64}],
            "claims": [{"claim_id": "c", "subject": "switch", "predicate": "rating", "value": 1, "scope": "manufacturer", "source_ids": ["s"], "confidence": "high", "status": "accepted"}],
        }
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                ingest_source_pack(self.store(Path(directory)), pack, schema)

    def test_source_pack_accepts_exact_model_claim_from_permitted_noncommercial_source(self) -> None:
        schema = json.loads((SKILL / "references" / "source-pack.schema.json").read_text())
        pack = {
            "topic_id": "t", "retrieved_at": "2026-10-09T00:00:00+00:00",
            "sources": [{"source_id": "s", "title": "Public Standard Record", "publisher": "International Standards Body", "url": "https://example.org/model-x1", "source_type": "standard", "retrieved_at": "2026-10-09T00:00:00+00:00", "content_hash": "a" * 64}],
            "claims": [{"claim_id": "c", "subject": "model X1", "predicate": "rating", "value": 1, "conditions": {"model_identifier": "X1"}, "scope": "model", "source_ids": ["s"], "confidence": "high", "status": "accepted"}],
        }
        with tempfile.TemporaryDirectory() as directory:
            result = ingest_source_pack(self.store(Path(directory)), pack, schema)
        self.assertEqual(result["claims"], 1)

    def test_internal_links_are_bounded_and_have_no_self_links(self) -> None:
        jobs = [{"job_id": str(i), "title": f"Article {i}", "primary_keyword": f"micro switch {i}", "category": "Basics"} for i in range(10)]
        links = build_internal_links(jobs, 3, 8)
        counts = {job["job_id"]: 0 for job in jobs}
        for link in links:
            self.assertNotEqual(link["source_job_id"], link["target_job_id"])
            counts[link["source_job_id"]] += 1
        self.assertTrue(all(3 <= count <= 8 for count in counts.values()))

    def test_source_pack_requires_each_evidence_concept(self) -> None:
        pack = {"claims": [{
            "status": "accepted", "subject": "snap-action mechanism", "predicate": "definition",
            "value": "an actuator moves a contact rapidly between fixed contacts",
        }]}
        self.assertEqual(missing_source_terms(pack, ["snap-action mechanism", "terminal identification"]), ["terminal identification"])

    def test_article_policy_allows_generic_role_but_blocks_marketing_language(self) -> None:
        article = {
            "primary_keyword": "micro switch wiring", "title": "Micro Switch Wiring Guide", "h1": "Micro Switch Wiring Guide",
            "description": "Micro switch wiring is explained with terminal roles, safe verification steps, practical checks, and clear guidance for reliable circuit planning.",
            "slug": "micro-switch-wiring-guide", "body_markdown": "## Micro switch wiring basics\n\nMicro switch wiring is useful. " + ("Neutral technical sentence. " * 1250) + "\n## Practical next step\n\nAsk the manufacturer about micro switch wiring.",
            "source_manufacturer_names": [], "internal_links": [],
        }
        config = {"program": {"article_word_min": 1200, "article_word_max": 1800}}
        errors = article_policy_errors(article, config)
        self.assertFalse(any("commercial entity" in error for error in errors))

        article["body_markdown"] += " The best micro switch manufacturers are ranked here."
        errors = article_policy_errors(article, config)
        self.assertTrue(any("ranking" in error for error in errors))

    def test_review_allows_source_publisher_metadata_but_not_editorial_promotion(self) -> None:
        article = {
            "primary_keyword": "micro switch mechanical life",
            "title": "Micro Switch Mechanical Life Explained",
            "h1": "Micro Switch Mechanical Life Explained",
            "description": "Micro switch mechanical life is explained through operating cycles, stated conditions, and careful interpretation of technical specifications.",
            "slug": "micro-switch-mechanical-life-explained",
            "body_markdown": "## Micro switch mechanical life basics\n\nMicro switch mechanical life is a defined durability measure. " + ("Neutral technical sentence. " * 400) + "\n## Reading the specification\n\nUse the stated conditions for micro switch mechanical life.",
            "source_manufacturer_names": ["Example Publisher"],
            "internal_links": [],
        }
        review = {
            "checks": {
                "logical_consistency": True,
                "parameter_accuracy": True,
                "definition_accuracy": True,
                "h2_fulfillment": True,
                "owned_question_uniqueness": True,
                "reader_task_alignment": True,
                "zero_brand": False,
            },
            "issues": ["Zero-brand failure? No blocked manufacturer name appears in editorial prose, so zero_brand passes."],
            "passed": False,
        }
        config = {"program": {"article_word_min": 1200, "article_word_max": 1800}}
        reconciled = reconcile_review_deterministic_checks(review, article, config)
        self.assertTrue(reconciled["checks"]["zero_brand"])
        self.assertTrue(reconciled["passed"])
        article["body_markdown"] += " Example Publisher is the best manufacturer."
        reconciled = reconcile_review_deterministic_checks(review, article, config)
        self.assertFalse(reconciled["checks"]["zero_brand"])
        self.assertFalse(reconciled["passed"])

    def test_source_pack_accepts_scoped_commercial_technical_source(self) -> None:
        schema = json.loads((SKILL / "references" / "source-pack.schema.json").read_text())
        pack = {
            "topic_id": "t", "retrieved_at": "2026-10-09T00:00:00+00:00",
            "sources": [{"source_id": "s", "title": "Commercial Guide", "publisher": "Example Brand", "url": "https://example.com/guide", "source_type": "technical_guide", "retrieved_at": "2026-10-09T00:00:00+00:00", "content_hash": "a" * 64, "editorial_block_names": ["Example Brand"]}],
            "claims": [{"claim_id": "c", "subject": "switch", "predicate": "definition", "value": "text", "scope": "manufacturer", "conditions": {"manufacturer": "Example Brand"}, "source_ids": ["s"], "confidence": "high", "status": "accepted"}],
        }
        with tempfile.TemporaryDirectory() as directory:
            result = ingest_source_pack(self.store(Path(directory)), pack, schema)
        self.assertEqual(result["claims"], 1)

    def test_review_treats_noncritical_structure_signals_as_advisory(self) -> None:
        article = {
            "primary_keyword": "micro switch basics", "title": "Micro Switch Basics",
            "h1": "Micro Switch Basics", "description": "Micro switch basics explained.",
            "slug": "micro-switch-basics", "body_markdown": "## Micro switch basics\n\nNeutral explanation.",
            "source_manufacturer_names": [], "internal_links": [],
        }
        review = {
            "checks": {
                "logical_consistency": True,
                "parameter_accuracy": True,
                "definition_accuracy": True,
                "h2_fulfillment": False,
                "owned_question_uniqueness": False, "reader_task_alignment": True,
                "zero_brand": True,
            },
            "issues": ["An outline heading could be more direct."], "passed": False,
        }
        config = {"program": {"article_word_min": 1, "article_word_max": 1800}}
        reconciled = reconcile_review_deterministic_checks(review, article, config)
        self.assertTrue(reconciled["passed"])


if __name__ == "__main__":
    unittest.main()
