from __future__ import annotations

import argparse
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

PIPELINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE))

from core import Paths, Store, load_json, load_jsonl, now_iso, stable_id
from operations import build_batches_action, dedupe_semantic, embed_objects, jobs_create, jobs_export, keywords_filter, publication_select, same_plan_content_identity, source_packs_build


class WorkflowTests(unittest.TestCase):
    def test_embedding_resumes_after_transient_qdrant_failure(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "pipeline").mkdir()
            (root / "pipeline" / "schema.sql").write_text((PIPELINE / "schema.sql").read_text())
            store = Store(Paths(root))
            store.initialize()
            source = root / "input.jsonl"
            source.write_text("".join(json.dumps({"id": str(i), "text": f"micro switch {i}"}) + "\n" for i in range(3)))
            output = root / "vectors.jsonl"
            config = {"models": {"embedding_provider": "local", "embedding_dimensions": 2, "embedding": "test"}, "qdrant": {"collections": {"chunk": "chunks"}}}

            class FakeEmbedder:
                def __init__(self) -> None:
                    self.calls = []
                def embed(self, texts, _purpose):
                    self.calls.append(len(texts))
                    return [[1.0, 0.0] for _ in texts]

            class FakeQdrant:
                def __init__(self, fail_second: bool) -> None:
                    self.calls = 0
                    self.fail_second = fail_second
                def upsert(self, _collection, _points):
                    self.calls += 1
                    if self.fail_second and self.calls == 2:
                        raise RuntimeError("transient Qdrant failure")

            args = argparse.Namespace(input=source, output=output, provider="local", object_type="chunk", batch_size=2)
            first_embedder = FakeEmbedder()
            with patch("operations._embedding_client", return_value=first_embedder), patch("operations.QdrantClient", return_value=FakeQdrant(True)):
                with self.assertRaisesRegex(RuntimeError, "transient Qdrant failure"):
                    embed_objects(args, config, store, {"QDRANT_URL": "url", "QDRANT_API_KEY": "key"})
            self.assertEqual(len(load_jsonl(output)), 2)
            second_embedder = FakeEmbedder()
            with patch("operations._embedding_client", return_value=second_embedder), patch("operations.QdrantClient", return_value=FakeQdrant(False)):
                embed_objects(args, config, store, {"QDRANT_URL": "url", "QDRANT_API_KEY": "key"})
            self.assertEqual(second_embedder.calls, [1])
            self.assertEqual(len(load_jsonl(output)), 3)

    def test_plan_similarity_does_not_merge_distinct_reader_tasks(self) -> None:
        function = {
            "owned_question": "How does the micro switch detect position?",
            "reader_task": "explain_mechanism",
            "answer_type": "mechanism_explanation",
            "section_roles": ["mechanism", "limits"],
            "differentiation_anchors": ["actuator path", "contact state"],
        }
        rating = {
            **function,
            "owned_question": "What contact rating applies to the micro switch?",
            "reader_task": "interpret_rating",
            "answer_type": "parameter_boundary",
            "section_roles": ["rating_scope", "limits"],
            "differentiation_anchors": ["load type", "voltage condition"],
        }
        self.assertFalse(same_plan_content_identity(function, rating))
        self.assertTrue(same_plan_content_identity(function, dict(function)))

    def test_article_plan_dedupe_respects_content_identity(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(PIPELINE, root / "pipeline", ignore=shutil.ignore_patterns("state", "__pycache__"))
            store = Store(Paths(root))
            store.initialize()
            config = load_json(root / "pipeline" / "config.json")
            run_id = store.create_run("c" * 64, "s" * 64)
            now = now_iso()
            plans = (
                {"owned_question": "How does a micro switch detect position?", "reader_task": "explain_mechanism", "answer_type": "mechanism_explanation"},
                {"owned_question": "What contact rating applies to a micro switch?", "reader_task": "interpret_rating", "answer_type": "parameter_boundary"},
            )
            with store.connect() as connection:
                for index, plan in enumerate(plans):
                    keyword_id = f"kw_{index}"
                    job_id = f"job_{index}"
                    connection.execute("INSERT INTO keywords(keyword_id,keyword,normalized_keyword,location_code,language_code,selected,created_at,updated_at) VALUES(?,?,?,?,?,?,?,?)", (keyword_id, f"micro switch test {index}", f"micro switch test {index}", 2840, "en", 1, now, now))
                    connection.execute("INSERT INTO content_jobs(job_id,created_run_id,keyword_id,custom_id,status,plan_json,created_at,updated_at) VALUES(?,?,?,?,?,?,?,?)", (job_id, run_id, keyword_id, f"custom_{index}", "planned", json.dumps(plan), now, now))
            vectors = root / "plans.jsonl"
            vectors.write_text("".join(json.dumps({"id": f"job_{index}", "job_id": f"job_{index}", "granularity": "plan", "vector": [1.0, 0.0]}) + "\n" for index in range(2)))
            dedupe_semantic(argparse.Namespace(input=vectors, output=root / "dedupe.jsonl", threshold=0.93, object_type="article_plan", run_id=run_id, apply=True), config, store, {})
            with store.connect() as connection:
                self.assertEqual(connection.execute("SELECT COUNT(*) FROM content_jobs WHERE status='duplicate'").fetchone()[0], 0)


    def test_borderline_topics_require_explicit_planning_opt_in(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(PIPELINE, root / "pipeline", ignore=shutil.ignore_patterns("state", "__pycache__"))
            store = Store(Paths(root))
            store.initialize()
            config = load_json(root / "pipeline" / "config.json")
            run_id = store.create_run("c" * 64, "s" * 64)
            source = root / "keywords.jsonl"
            source.write_text("".join(json.dumps({"keyword": keyword}) + "\n" for keyword in (
                "dryer door micro switch troubleshooting",
                "dryer door latch micro switch troubleshooting",
            )))
            store.import_keywords(source, 2840, "en")
            keywords_filter(argparse.Namespace(brand=[]), config, store)
            with store.connect() as connection:
                ids = sorted(row[0] for row in connection.execute("SELECT keyword_id FROM keywords WHERE selected=1"))
                self.assertEqual(len(ids), 2)
                for keyword_id in ids:
                    cluster_id = stable_id("cluster", keyword_id)
                    connection.execute("INSERT INTO clusters(cluster_id,algorithm_version,threshold,primary_keyword_id,created_at) VALUES(?,?,?,?,?)", (cluster_id, "test", 0.93, keyword_id, now_iso()))
                    connection.execute("UPDATE keywords SET cluster_id=? WHERE keyword_id=?", (cluster_id, keyword_id))
                connection.execute("INSERT INTO similarity_reviews(object_type,left_id,right_id,cosine_score,status,created_at,updated_at) VALUES('topic',?, ?,0.9,'needs_review',?,?)", (*ids, now_iso(), now_iso()))
            jobs_create(argparse.Namespace(run_id=run_id, limit=10, new_only=True), config, store)
            with store.connect() as connection:
                self.assertEqual(connection.execute("SELECT COUNT(*) FROM content_jobs").fetchone()[0], 0)
            jobs_create(argparse.Namespace(run_id=run_id, limit=10, new_only=True, allow_borderline_topics=True), config, store)
            with store.connect() as connection:
                self.assertEqual(connection.execute("SELECT COUNT(*) FROM content_jobs").fetchone()[0], 2)

    def test_jobs_export_is_scoped_to_run(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            paths = Paths(root)
            (root / "pipeline").mkdir()
            schema_source = PIPELINE / "schema.sql"
            (root / "pipeline" / "schema.sql").write_text(schema_source.read_text(), encoding="utf-8")
            store = Store(paths)
            store.initialize()
            run_a = store.create_run("config", "skill")
            run_b = store.create_run("config", "skill")
            now = "2026-01-01T00:00:00+00:00"
            with store.connect() as connection:
                for suffix, run_id in (("a", run_a), ("b", run_b)):
                    connection.execute(
                        "INSERT INTO keywords(keyword_id,keyword,normalized_keyword,location_code,language_code,selected,created_at,updated_at) VALUES(?,?,?,?,?,?,?,?)",
                        (f"kw_{suffix}", f"micro switch {suffix}", f"micro switch {suffix}", 2840, "en", 1, now, now),
                    )
                    connection.execute(
                        "INSERT INTO content_jobs(job_id,created_run_id,keyword_id,custom_id,status,created_at,updated_at) VALUES(?,?,?,?,?,?,?)",
                        (f"job_{suffix}", run_id, f"kw_{suffix}", f"article_{suffix}", "queued_for_plan", now, now),
                    )
            output = root / "run-a.jsonl"
            jobs_export(argparse.Namespace(run_id=run_a, kind="plan", output=output, limit=10), store)
            rows = load_jsonl(output)
            self.assertEqual([row["job_id"] for row in rows], ["job_a"])

    def test_publication_selection_keeps_exact_target_and_reserves_excess(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(PIPELINE, root / "pipeline", ignore=shutil.ignore_patterns("state", "__pycache__"))
            store = Store(Paths(root))
            store.initialize()
            run_id = store.create_run("c" * 64, "s" * 64)
            now = now_iso()
            with store.connect() as connection:
                for index in range(55):
                    keyword_id = f"kw_{index:03d}"
                    job_id = f"job_{index:03d}"
                    connection.execute(
                        """INSERT INTO keywords(keyword_id,keyword,normalized_keyword,location_code,language_code,search_volume,selected,created_at,updated_at)
                           VALUES(?,?,?,?,?,?,?,?,?)""",
                        (keyword_id, f"micro switch {index}", f"micro switch {index}", 2840, "en", index, 1, now, now),
                    )
                    connection.execute(
                        """INSERT INTO content_jobs(job_id,created_run_id,keyword_id,custom_id,status,article_json,created_at,updated_at)
                           VALUES(?,?,?,?,?,?,?,?)""",
                        (job_id, run_id, keyword_id, f"custom_{index:03d}", "validated", "{}", now, now),
                    )
            publication_select(argparse.Namespace(run_id=run_id, target=50), store)
            with store.connect() as connection:
                counts = dict(connection.execute("SELECT status,COUNT(*) FROM content_jobs GROUP BY status"))
            self.assertEqual(counts["validated"], 50)
            self.assertEqual(counts["reserve_validated"], 5)

    def test_source_pack_builder_is_scoped_to_run(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(PIPELINE, root / "pipeline", ignore=shutil.ignore_patterns("state", "__pycache__"))
            store = Store(Paths(root))
            store.initialize()
            run_a = store.create_run("a" * 64, "s" * 64)
            run_b = store.create_run("b" * 64, "s" * 64)
            now = now_iso()
            plan = json.dumps({"primary_keyword": "micro switch test", "source_pack_terms": ["missing evidence term"]})
            with store.connect() as connection:
                for suffix, run_id in (("a", run_a), ("b", run_b)):
                    keyword_id = f"kw_{suffix}"
                    connection.execute(
                        """INSERT INTO keywords(keyword_id,keyword,normalized_keyword,location_code,language_code,selected,created_at,updated_at)
                           VALUES(?,?,?,?,?,?,?,?)""",
                        (keyword_id, f"micro switch test {suffix}", f"micro switch test {suffix}", 2840, "en", 1, now, now),
                    )
                    connection.execute(
                        """INSERT INTO content_jobs(job_id,created_run_id,keyword_id,custom_id,status,plan_json,created_at,updated_at)
                           VALUES(?,?,?,?,?,?,?,?)""",
                        (f"job_{suffix}", run_id, keyword_id, f"custom_{suffix}", "planned", plan, now, now),
                    )
            source_packs_build(argparse.Namespace(run_id=run_a, force=False, limit=10), store)
            with store.connect() as connection:
                statuses = dict(connection.execute("SELECT job_id,status FROM content_jobs"))
            self.assertEqual(statuses["job_a"], "blocked_missing_sources")
            self.assertEqual(statuses["job_b"], "planned")

    def test_clusters_become_idempotent_jobs_and_split_batches(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(PIPELINE, root / "pipeline", ignore=shutil.ignore_patterns("state", "__pycache__"))
            paths = Paths(root)
            store = Store(paths)
            store.initialize()
            config = load_json(root / "pipeline" / "config.json")
            run_id = store.create_run("c" * 64, "s" * 64)
            source = root / "keywords.jsonl"
            rows = [{"keyword": f"micro switch test topic {index}", "search_volume": 100 - index, "intent": "informational"} for index in range(5)]
            rows.append({"keyword": "best micro switch manufacturers", "search_volume": 999, "intent": "commercial"})
            source.write_text("".join(json.dumps(row) + "\n" for row in rows))
            store.import_keywords(source, 2840, "en")
            keywords_filter(argparse.Namespace(brand=[]), config, store)
            with store.connect() as connection:
                selected = connection.execute("SELECT keyword_id FROM keywords WHERE selected=1 ORDER BY keyword_id").fetchall()
                for row in selected:
                    cluster_id = stable_id("cluster", row["keyword_id"])
                    connection.execute("INSERT INTO clusters(cluster_id,algorithm_version,threshold,primary_keyword_id,created_at) VALUES(?,?,?,?,?)", (cluster_id, "test", 0.93, row["keyword_id"], now_iso()))
                    connection.execute("UPDATE keywords SET cluster_id=? WHERE keyword_id=?", (cluster_id, row["keyword_id"]))
            args = argparse.Namespace(run_id=run_id, limit=50)
            jobs_create(args, config, store)
            jobs_create(args, config, store)
            plan_input = root / "plan-input.jsonl"
            jobs_export(argparse.Namespace(run_id=run_id, kind="plan", output=plan_input, limit=50), store)
            lines = plan_input.read_text().splitlines()
            self.assertEqual(len(lines), 5)
            output_dir = root / "batches"
            build_batches_action(argparse.Namespace(run_id=run_id, kind="plan", input=plan_input, output_dir=output_dir, chunk_size=2, model="test-model"), paths, config, store, "fixed skill " * 200, "h" * 64)
            manifest = json.loads((output_dir / "manifest.json").read_text())
            self.assertEqual(len(manifest["files"]), 3)
            with store.connect() as connection:
                self.assertEqual(connection.execute("SELECT COUNT(*) FROM content_jobs").fetchone()[0], 5)
                self.assertEqual(connection.execute("SELECT COUNT(*) FROM batch_requests").fetchone()[0], 5)


if __name__ == "__main__":
    unittest.main()
