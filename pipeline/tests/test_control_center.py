from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from control_center import ControlCenter


class ControlCenterCsvTests(unittest.TestCase):
    def test_csv_requires_keyword_header(self) -> None:
        with self.assertRaisesRegex(ValueError, "keyword"):
            ControlCenter.validate_csv("term,volume\nmicro switch,10\n")

    def test_csv_deduplicates_case_insensitively(self) -> None:
        rows, headers = ControlCenter.validate_csv(
            "keyword,search_volume,intent\nMicro Switch,100,informational\nmicro switch,50,informational\nNO vs NC,30,informational\n"
        )
        self.assertEqual(headers, ["keyword", "search_volume", "intent"])
        self.assertEqual([row["keyword"] for row in rows], ["Micro Switch", "NO vs NC"])

    def test_csv_rejects_empty_keyword_rows(self) -> None:
        with self.assertRaisesRegex(ValueError, "没有有效"):
            ControlCenter.validate_csv("keyword,intent\n,informational\n")
