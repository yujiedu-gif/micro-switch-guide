from __future__ import annotations

import json
import shutil
import stat
import sys
import tempfile
import unittest
from pathlib import Path

PIPELINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE))

from batch import build_batch_requests, extract_response_json, write_batch
from cli import is_authoritative_article_request, is_authoritative_review_request
from core import Paths, Store, now_iso
from operations import _review_custom_id, _review_payload
from credentials import github_token_from_credential_helper, import_credentials, load_env_file


class BatchTests(unittest.TestCase):
    def test_only_newest_article_lineage_is_authoritative(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(PIPELINE, root / "pipeline", ignore=shutil.ignore_patterns("state", "__pycache__"))
            store = Store(Paths(root))
            store.initialize()
            run_id = store.create_run("c" * 64, "s" * 64)
            now = now_iso()
            with store.connect() as connection:
                connection.execute(
                    """INSERT INTO keywords(keyword_id,keyword,normalized_keyword,location_code,language_code,selected,created_at,updated_at)
                       VALUES('kw','micro switch','micro switch',2840,'en',1,?,?)""",
                    (now, now),
                )
                connection.execute(
                    """INSERT INTO content_jobs(job_id,created_run_id,keyword_id,custom_id,status,created_at,updated_at)
                       VALUES('job',?,'kw','job-custom','article_submitted',?,?)""",
                    (run_id, now, now),
                )
                for custom_id, created_at in (("old", "2026-01-01T00:00:00+00:00"), ("new", "2026-01-02T00:00:00+00:00")):
                    connection.execute(
                        """INSERT INTO batch_requests(custom_id,run_id,kind,job_id,endpoint,model,input_sha256,status,created_at,updated_at)
                           VALUES(?,?,'article','job','/v1/responses','test',?,'submitted',?,?)""",
                        (custom_id, run_id, custom_id, created_at, created_at),
                    )
                connection.execute(
                    """INSERT INTO batch_requests(custom_id,run_id,kind,job_id,endpoint,model,input_sha256,status,parent_custom_id,created_at,updated_at)
                       VALUES('new-s1',?,'repair','job','/v1/responses','test','repair','submitted','new',?,?)""",
                    (run_id, now, now),
                )
                old = connection.execute("SELECT * FROM batch_requests WHERE custom_id='old'").fetchone()
                new = connection.execute("SELECT * FROM batch_requests WHERE custom_id='new'").fetchone()
                repair = connection.execute("SELECT * FROM batch_requests WHERE custom_id='new-s1'").fetchone()
                self.assertFalse(is_authoritative_article_request(connection, old))
                self.assertTrue(is_authoritative_article_request(connection, new))
                self.assertTrue(is_authoritative_article_request(connection, repair))
                connection.execute(
                    "UPDATE content_jobs SET plan_json='{}',article_json='{}',source_pack_json='{}' WHERE job_id='job'"
                )
                job = connection.execute("SELECT * FROM content_jobs WHERE job_id='job'").fetchone()
                payload = _review_payload(connection, job)
                expected = _review_custom_id(run_id, "job", job["article_json"], payload)
                for custom_id in ("old-review", expected):
                    connection.execute(
                        """INSERT INTO batch_requests(custom_id,run_id,kind,job_id,endpoint,model,input_sha256,status,created_at,updated_at)
                           VALUES(?,?,'review','job','/v1/responses','test',?,'submitted',?,?)""",
                        (custom_id, run_id, custom_id, now, now),
                    )
                old_review = connection.execute("SELECT * FROM batch_requests WHERE custom_id='old-review'").fetchone()
                current_review = connection.execute("SELECT * FROM batch_requests WHERE custom_id=?", (expected,)).fetchone()
                self.assertFalse(is_authoritative_review_request(connection, old_review))
                self.assertTrue(is_authoritative_review_request(connection, current_review))

    def test_fixed_prefix_and_unique_ids(self) -> None:
        schema = {"type": "object", "required": ["answer"], "properties": {"answer": {"type": "string"}}, "additionalProperties": False}
        rows = build_batch_requests("plan", [{"custom_id": "run-job-plan-v1", "payload": {"keyword": "micro switch"}}], "test-model", "fixed skill", schema, 100)
        self.assertEqual(rows[0]["url"], "/v1/responses")
        self.assertEqual(rows[0]["body"]["input"][0]["role"], "system")
        self.assertNotIn("fixed skill", rows[0]["body"]["input"][0]["content"][0]["text"])
        self.assertIn("Plan contract", rows[0]["body"]["input"][0]["content"][0]["text"])
        self.assertIn("nonempty source_pack_terms", rows[0]["body"]["input"][0]["content"][0]["text"])
        self.assertEqual(rows[0]["body"]["input"][0]["content"][0]["prompt_cache_breakpoint"], {"mode": "explicit"})
        self.assertEqual(rows[0]["body"]["prompt_cache_options"], {"mode": "explicit", "ttl": "30m"})
        self.assertEqual(rows[0]["body"]["text"]["format"]["type"], "json_schema")
        with self.assertRaises(ValueError):
            build_batch_requests("plan", [{"custom_id": "same"}, {"custom_id": "same"}], "m", "s", schema, 10)

    def test_strict_schema_keeps_title_and_description_property_names(self) -> None:
        schema = {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "title": "Schema metadata",
            "type": "object",
            "required": ["title", "description"],
            "properties": {
                "title": {"type": "string", "minLength": 2},
                "description": {"type": "string", "minLength": 2},
            },
            "additionalProperties": False,
        }
        row = build_batch_requests("plan", [{"custom_id": "x", "payload": {}}], "m", "skill", schema, 10)[0]
        strict = row["body"]["text"]["format"]["schema"]
        self.assertNotIn("$schema", strict)
        self.assertNotIn("title", {key for key in strict if key != "properties"})
        self.assertEqual(set(strict["properties"]), {"title", "description"})

    def test_response_reconciles_by_custom_id(self) -> None:
        line = {"custom_id": "b", "response": {"status_code": 200, "body": {"output": [{"type": "message", "content": [{"type": "output_text", "text": "{\"ok\":true}"}]}]}}}
        custom_id, output, error = extract_response_json(line)
        self.assertEqual(custom_id, "b")
        self.assertEqual(output, {"ok": True})
        self.assertIsNone(error)

    def test_credential_import_never_requires_printing_values(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "dataforseo.txt").write_text("Name: user\nAPI KEY: pass\n")
            (root / "qdrant.txt").write_text("x" * 80)
            (root / "gptbatchapi.txt").write_text("sk-proj-" + "a" * 40)
            destination = root / "state" / "secrets.env"
            status = import_credentials(root, destination)
            self.assertEqual(status["DATAFORSEO_LOGIN"], "configured")
            self.assertEqual(status["QDRANT_API_KEY"], "configured")
            self.assertEqual(stat.S_IMODE(destination.stat().st_mode), 0o600)
            self.assertEqual(load_env_file(destination)["DATAFORSEO_PASSWORD"], "pass")

    def test_github_credential_helper_extracts_password_without_logging(self) -> None:
        from unittest.mock import patch
        completed = type("Completed", (), {"returncode": 0, "stdout": "protocol=https\nhost=github.com\npassword=secret-token\n"})()
        with patch("credentials.subprocess.run", return_value=completed):
            self.assertEqual(github_token_from_credential_helper(), "secret-token")


if __name__ == "__main__":
    unittest.main()
