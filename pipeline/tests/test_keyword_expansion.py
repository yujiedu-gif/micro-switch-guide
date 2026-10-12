from __future__ import annotations

import argparse
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


PIPELINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE))

from core import Paths, Store, load_json, now_iso
from keyword_expansion import GENERATOR_VERSION, expansion_candidates, extract_material
from keyword_catalog import catalog_candidates
from operations import dedupe_semantic, keywords_expand_apply
from validators import plan_policy_errors, validate_schema


class KeywordExpansionTests(unittest.TestCase):
    def test_catalog_produces_ten_thousand_strict_unique_keywords(self) -> None:
        rows = catalog_candidates(10_000, set(), [])
        self.assertEqual(len(rows), 10_000)
        self.assertEqual(len({row["normalized_keyword"] for row in rows}), 10_000)
        self.assertTrue(all(row["decision"] == "accept" for row in rows))
        self.assertFalse(any("keyboard" in row["normalized_keyword"] for row in rows))

    def test_material_gate_accepts_direct_applications_and_rejects_drift(self) -> None:
        dryer = extract_material("a", "dryer door switch symptoms")
        self.assertEqual(dryer["decision"], "accept")
        self.assertEqual(dryer["base_keyword"], "clothes dryer door micro switch")
        self.assertEqual(extract_material("b", "mechanical keyboard switch")["decision"], "reject")
        self.assertEqual(extract_material("c", "marine switch panel")["decision"], "reject")
        self.assertEqual(extract_material("d", "automotive switch symptoms")["decision"], "reject")
        self.assertEqual(extract_material("e", "dryer lid switch")["decision"], "reject")

    def test_candidates_keep_provenance_and_hold_evidence_sensitive_tasks(self) -> None:
        material = extract_material("origin", "conveyor limit switch")
        candidates = expansion_candidates([material], set())
        by_task = {item["reader_task"]: item for item in candidates}
        self.assertEqual(by_task["explain_function"]["decision"], "accept")
        self.assertEqual(by_task["adjust"]["decision"], "hold")
        self.assertEqual(by_task["adjust"]["reason_codes"], ["requires_authoritative_evidence"])
        self.assertEqual(by_task["explain_function"]["origin_keyword_ids"], ["origin"])
        self.assertEqual(by_task["explain_function"]["generator_version"], GENERATOR_VERSION)

    def test_same_content_identity_collapses_keyword_wording_variants(self) -> None:
        materials = [
            extract_material("door", "dryer door switch symptoms"),
            extract_material("interlock", "dryer interlock switch symptoms"),
            extract_material("safety", "dryer safety switch symptoms"),
        ]
        candidates = expansion_candidates(materials, set())
        functions = [item for item in candidates if item["reader_task"] == "explain_function"]
        self.assertEqual(len(functions), 1)
        self.assertEqual(functions[0]["candidate_keyword"], "clothes dryer door micro switch function")
        self.assertEqual(functions[0]["origin_keyword_ids"], ["door", "interlock", "safety"])

    def test_apply_stages_candidates_without_selecting_for_production(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(PIPELINE, root / "pipeline", ignore=shutil.ignore_patterns("state", "__pycache__"))
            store = Store(Paths(root))
            store.initialize()
            now = now_iso()
            with store.connect() as connection:
                connection.execute(
                    """INSERT INTO keywords(keyword_id,keyword,normalized_keyword,location_code,language_code,
                       exclusion_reason,selected,created_at,updated_at)
                       VALUES('origin','conveyor limit switch','conveyor limit switch',2840,'en',
                       'scope_reject:missing_direct_term',0,?,?)""",
                    (now, now),
                )
            candidates = expansion_candidates([extract_material("origin", "conveyor limit switch")], set())
            accepted = [item for item in candidates if item["decision"] == "accept"]
            source = root / "candidates.jsonl"
            source.write_text("".join(json.dumps(item) + "\n" for item in accepted), encoding="utf-8")
            config = load_json(root / "pipeline" / "config.json")
            keywords_expand_apply(argparse.Namespace(input=source, limit=100), config, store)
            with store.connect() as connection:
                row = connection.execute(
                    "SELECT selected,exclusion_reason FROM keywords WHERE source_endpoint=? LIMIT 1",
                    (f"derived:{GENERATOR_VERSION}",),
                ).fetchone()
                self.assertEqual(row["selected"], 0)
                self.assertEqual(row["exclusion_reason"], "expansion_pending:demand_and_evidence")
                self.assertGreater(connection.execute("SELECT COUNT(*) FROM keyword_derivations").fetchone()[0], 0)

    def test_plan_schema_requires_content_identity(self) -> None:
        schema = load_json(PIPELINE / "schemas" / "article-plan.schema.json")
        plan = {
            "primary_keyword": "dryer door micro switch symptoms", "secondary_keywords": [],
            "intent": "troubleshooting", "reader": "equipment owner",
            "reader_task": "diagnose_symptoms", "answer_type": "symptom_to_cause",
            "content_signature": "dryer_door|diagnose_symptoms|symptom_to_cause",
            "differentiation_anchors": ["door actuator relationship", "intermittent state detection"],
            "section_roles": ["observable_symptoms", "mechanical_causes", "verification_boundary"],
            "page_type": "spoke", "category": "Troubleshooting",
            "topic_scope": {"primary_entity": "micro_switch", "relation": "direct", "owned_question_is_direct": True},
            "owned_question": "Which symptoms can indicate a dryer door micro switch problem?",
            "excluded_questions": ["replacement compatibility"], "angle": "symptom-to-cause diagnosis",
            "title": "dryer door micro switch symptoms", "h1": "dryer door micro switch symptoms",
            "description": "dryer door micro switch symptoms: learn how mechanical actuation and intermittent state detection shape a careful verification path for service checks.",
            "slug": "dryer-door-micro-switch-symptoms",
            "outline": [
                {"h2": "dryer door micro switch symptoms", "purpose": "Identify observable behavior.", "section_role": "observable_symptoms", "points": ["state changes"]},
                {"h2": "Mechanical causes", "purpose": "Separate actuator faults.", "section_role": "mechanical_causes", "points": ["travel"]},
                {"h2": "Verification boundary", "purpose": "Define safe checks.", "section_role": "verification_boundary", "points": ["isolation"]},
            ],
            "must_cover": [], "evidence_needed": ["door interlock relationship"],
            "source_pack_terms": ["micro switch snap action mechanism"], "internal_link_targets": [],
        }
        self.assertEqual(validate_schema(plan, schema), [])
        self.assertFalse(plan_policy_errors(plan, {"program": {"excluded_brand_terms": []}}))

    def test_two_non_definition_section_matches_create_one_article_duplicate(self) -> None:
        rows = [
            {"id": "a:section:0", "job_id": "a", "granularity": "section", "section_role": "mechanical_causes", "vector": [1.0, 0.0]},
            {"id": "b:section:0", "job_id": "b", "granularity": "section", "section_role": "mechanical_causes", "vector": [1.0, 0.0]},
            {"id": "a:section:1", "job_id": "a", "granularity": "section", "section_role": "verification_path", "vector": [0.0, 1.0]},
            {"id": "b:section:1", "job_id": "b", "granularity": "section", "section_role": "verification_path", "vector": [0.0, 1.0]},
        ]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(PIPELINE, root / "pipeline", ignore=shutil.ignore_patterns("state", "__pycache__"))
            store = Store(Paths(root))
            store.initialize()
            source = root / "vectors.jsonl"
            output = root / "dedupe.jsonl"
            source.write_text("".join(json.dumps(item) + "\n" for item in rows), encoding="utf-8")
            config = load_json(root / "pipeline" / "config.json")
            dedupe_semantic(
                argparse.Namespace(input=source, output=output, threshold=0.93, apply=False, run_id=None, object_type="chunk"),
                config, store, {},
            )
            results = [json.loads(line) for line in output.read_text().splitlines()]
            self.assertEqual(sum(bool(item.get("content_duplicate")) for item in results), 2)

    def test_two_similar_section_plan_roles_block_reused_outline(self) -> None:
        rows = [
            {"id": "a:section_plan:0", "job_id": "a", "granularity": "section_plan", "section_role": "mechanical_causes", "vector": [1.0, 0.0]},
            {"id": "b:section_plan:0", "job_id": "b", "granularity": "section_plan", "section_role": "mechanical_causes", "vector": [1.0, 0.0]},
            {"id": "a:section_plan:1", "job_id": "a", "granularity": "section_plan", "section_role": "verification_path", "vector": [0.0, 1.0]},
            {"id": "b:section_plan:1", "job_id": "b", "granularity": "section_plan", "section_role": "verification_path", "vector": [0.0, 1.0]},
        ]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(PIPELINE, root / "pipeline", ignore=shutil.ignore_patterns("state", "__pycache__"))
            store = Store(Paths(root))
            store.initialize()
            source = root / "vectors.jsonl"
            output = root / "dedupe.jsonl"
            source.write_text("".join(json.dumps(item) + "\n" for item in rows), encoding="utf-8")
            config = load_json(root / "pipeline" / "config.json")
            dedupe_semantic(
                argparse.Namespace(input=source, output=output, threshold=0.93, apply=False, run_id=None, object_type="section_plan"),
                config, store, {},
            )
            results = [json.loads(line) for line in output.read_text().splitlines()]
            self.assertEqual(sum(bool(item.get("content_duplicate")) for item in results), 2)


if __name__ == "__main__":
    unittest.main()
