from datetime import date, timedelta
import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from stagger_archive_dates import daily_quotas, times_for_day


class ArchiveDateTests(unittest.TestCase):
    def test_180_day_quotas_are_exact_and_varied(self) -> None:
        end = date(2026, 10, 13)
        days = [end - timedelta(days=i) for i in range(179, -1, -1)]
        quotas = daily_quotas(days, 4211)
        self.assertEqual(quotas, daily_quotas(days, 4211))
        self.assertEqual(sum(quotas), 4211)
        self.assertEqual(len(quotas), 180)
        self.assertGreater(len(set(quotas)), 2)
        self.assertGreaterEqual(min(quotas), 18)
        self.assertLessEqual(max(quotas), 30)

    def test_article_times_are_unique_and_not_round_seconds(self) -> None:
        times = times_for_day(date(2026, 4, 17), 30)
        self.assertEqual(len(times), len(set(times)))
        self.assertEqual(times, sorted(times))
        self.assertTrue(all(not value.endswith(":00") for value in times))
        today_times = times_for_day(date(2026, 10, 13), 30, 11 * 3600 + 45 * 60)
        self.assertTrue(all(value < "11:45:00" for value in today_times))


if __name__ == "__main__":
    unittest.main()
