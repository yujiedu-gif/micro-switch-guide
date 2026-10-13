from __future__ import annotations

import subprocess
import tempfile
import unittest
import json
from pathlib import Path
from unittest.mock import patch

from search_discovery import bigquery_sql, git_post_change_rows, submit_indexnow, sync_bigquery_rows, validate_urls, wait_for_deploy


class SearchDiscoveryTests(unittest.TestCase):
    def test_changed_posts_include_add_modify_and_delete(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with patch("search_discovery.subprocess.run") as run:
                run.return_value = subprocess.CompletedProcess([], 0, "A\t_posts/2026-10-13-new-micro-switch.md\nD\t_posts/2026-10-12-old.md\nM\tREADME.md\n", "")
                result = git_post_change_rows("abc123", root=root)
        self.assertEqual(result, {
            "https://www.microswitchguide.com/guides/new-micro-switch/": 200,
            "https://www.microswitchguide.com/guides/old/": 404,
        })

    def test_foreign_url_rejected(self) -> None:
        with self.assertRaises(ValueError):
            validate_urls(["https://other.example/guides/foo/"])

    def test_indexnow_payload_uses_bing_key_location(self) -> None:
        with patch("search_discovery.urlopen") as open_url:
            open_url.return_value.__enter__.return_value.status = 200
            submit_indexnow(["https://www.microswitchguide.com/guides/example/"], "abc12345")
            payload = json.loads(open_url.call_args.args[0].data)
        self.assertEqual(payload["keyLocation"], "https://www.microswitchguide.com/abc12345.txt")

    def test_wait_requires_new_page_and_deleted_page_state(self) -> None:
        changes = {"https://www.microswitchguide.com/guides/new/": 200,
                   "https://www.microswitchguide.com/guides/old/": 404}
        with patch("search_discovery.get_status", side_effect=[(200, "key\n"), (200, ""), (404, "")]):
            wait_for_deploy(changes, "key", 0)

    def test_bigquery_query_aggregates_and_limits_billed_bytes(self) -> None:
        query = bigquery_sql("my-project-123", "searchconsole")
        self.assertIn("SUM(impressions)", query)
        self.assertIn("search_type = 'web'", query)
        with self.assertRaises(ValueError):
            bigquery_sql("bad.project", "searchconsole")

    def test_bigquery_sync_replaces_rolling_snapshot_idempotently(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            database = Path(directory) / "state.db"
            readout = {"project": "project-123", "dataset": "searchconsole", "result": [
                ["https://www.microswitchguide.com/guides/a/", "2", "10", "3.5", "2026-10-01", "2026-10-12"],
            ]}
            self.assertEqual(sync_bigquery_rows(database, readout), 1)
            self.assertEqual(sync_bigquery_rows(database, readout), 1)
            import sqlite3
            with sqlite3.connect(database) as connection:
                self.assertEqual(connection.execute("SELECT COUNT(*) FROM search_console_url_performance").fetchone()[0], 1)
            readout["result"] = []
            sync_bigquery_rows(database, readout)
            with sqlite3.connect(database) as connection:
                self.assertEqual(connection.execute("SELECT COUNT(*) FROM search_console_url_performance").fetchone()[0], 0)


if __name__ == "__main__":
    unittest.main()
