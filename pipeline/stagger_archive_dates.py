#!/usr/bin/env python3
"""Deterministically spread one dated post cohort over an archival window.

This changes presentation dates, not the historical fact that the cohort first
went live on ``--source-date``. Keep ``last_modified_at`` at the current update
time so sitemap <lastmod> and article dateModified do not falsely move backward.
Dry-run is the default; --apply is required for any file changes.
"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import date, datetime, timedelta
import hashlib
from pathlib import Path
import random
import re
import subprocess
from zoneinfo import ZoneInfo


DATE_LINE = re.compile(r"(?m)^date: (\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) \+0800$")


def digest_number(value: str) -> int:
    return int.from_bytes(hashlib.sha256(value.encode("utf-8")).digest()[:8], "big")


def daily_quotas(days: list[date], total: int, minimum: int = 18, maximum: int = 30) -> list[int]:
    if not days or not minimum * len(days) <= total <= maximum * len(days):
        raise ValueError("article count is incompatible with daily limits")
    extras = total - minimum * len(days)
    weights = [(digest_number(f"msg-archive-v1|{day}") + 1) / 2**64 for day in days]
    weight_sum = sum(weights)
    raw = [extras * weight / weight_sum for weight in weights]
    allocated = [min(maximum - minimum, int(value)) for value in raw]
    remaining = extras - sum(allocated)
    preference = sorted(range(len(days)), key=lambda i: (raw[i] - int(raw[i]), weights[i]), reverse=True)
    while remaining:
        changed = False
        for index in preference:
            if allocated[index] < maximum - minimum:
                allocated[index] += 1
                remaining -= 1
                changed = True
                if remaining == 0:
                    break
        if not changed:
            raise ValueError("could not allocate all articles")
    return [minimum + value for value in allocated]


def times_for_day(day: date, count: int) -> list[str]:
    rng = random.Random(digest_number(f"msg-archive-time-v1|{day}"))
    seconds: set[int] = set()
    while len(seconds) < count:
        second = rng.randrange(8 * 3600 + 5 * 60, 21 * 3600 + 55 * 60)
        if second % 60:
            seconds.add(second)
    return [f"{value // 3600:02d}:{value // 60 % 60:02d}:{value % 60:02d}" for value in sorted(seconds)]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-date", required=True, type=date.fromisoformat)
    parser.add_argument("--days", type=int, default=180)
    parser.add_argument("--expected", type=int, default=4211)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    if args.days <= 0:
        parser.error("--days must be positive")
    root = Path(__file__).resolve().parent.parent
    files = subprocess.check_output(["git", "ls-files", "-z", "--", "_posts"], cwd=root).split(b"\0")
    prefix = args.source_date.isoformat() + "-"
    sources = sorted(root / item.decode("utf-8") for item in files if item and Path(item.decode("utf-8")).name.startswith(prefix))
    if len(sources) != args.expected:
        raise SystemExit(f"Expected {args.expected} source posts; found {len(sources)}")
    dates = [args.source_date - timedelta(days=i) for i in range(args.days - 1, -1, -1)]
    quotas = daily_quotas(dates, len(sources))
    ordered = sorted(sources, key=lambda path: (digest_number(path.name), path.name))
    modified = datetime.now(ZoneInfo("Asia/Shanghai")).strftime("%Y-%m-%d %H:%M:%S %z")
    moves: list[tuple[Path, Path, str]] = []
    destinations: set[Path] = set()
    position = 0
    for day, quota in zip(dates, quotas):
        for clock_time in times_for_day(day, quota):
            source = ordered[position]
            position += 1
            slug = source.name[len(prefix):]
            destination = source.with_name(f"{day.isoformat()}-{slug}")
            if destination in destinations or (destination.exists() and destination not in sources):
                raise SystemExit(f"Destination collision: {destination.name}")
            original = source.read_text(encoding="utf-8")
            matches = list(DATE_LINE.finditer(original))
            if not original.startswith("---\n") or len(matches) != 1 or matches[0].group(1) != args.source_date.isoformat():
                raise SystemExit(f"Unexpected date front matter: {source.name}")
            if "last_modified_at:" in original:
                raise SystemExit(f"Already has last_modified_at: {source.name}")
            replacement = f"date: {day.isoformat()} {clock_time} +0800\nlast_modified_at: {modified}"
            updated = DATE_LINE.sub(replacement, original, count=1)
            destinations.add(destination)
            moves.append((source, destination, updated))
    counts = Counter(destination.name[:10] for _, destination, _ in moves)
    print({"posts": len(moves), "days": len(counts), "first_date": min(counts), "last_date": max(counts),
           "daily_min": min(counts.values()), "daily_max": max(counts.values()),
           "daily_average": round(len(moves) / len(counts), 3), "modified_at": modified,
           "apply": args.apply})
    if args.apply:
        for source, destination, updated in moves:
            source.rename(destination)
            destination.write_text(updated, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
