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

from core import Paths, Store, load_json, load_jsonl, now_iso, stable_id
from operations import build_batches_action, jobs_create, jobs_export, keywords_filter, publication_select, source_packs_build


class WorkflowTests(unittest.TestCase):
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
