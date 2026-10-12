from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from supervisor import Supervisor


class SupervisorPaidSafetyTests(unittest.TestCase):
    def test_active_batch_blocks_prepare_and_duplicate_submit(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            supervisor = Supervisor(root, "test")
            supervisor.base.mkdir(parents=True)
            supervisor.profile_path.write_text(json.dumps({
                "run_id": "run_test", "target": 1, "poll_seconds": 300,
                "tracked_batches": [{"batch_id": "batch_live", "kind": "article", "status": "in_progress"}],
                "prepared": {"article": {"batch_dir": str(root / "missing")}}, "events": [],
            }), encoding="utf-8")
            with self.assertRaisesRegex(RuntimeError, "still active"):
                supervisor.prepare("article", 1)
            with self.assertRaisesRegex(RuntimeError, "duplicate paid submit blocked"):
                supervisor.submit("article", True)
