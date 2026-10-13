#!/usr/bin/env python3
"""Restore current posts to their auditable first public deployment dates.

The four source commits are the publication records for every currently live
post.  Artificial editorial-calendar dates and unverifiable modification
fields are removed.  Dry-run is the default; --apply writes and renames files.
"""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
import re
import subprocess


ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "_posts"
COHORTS = (
    ("651052f1", "2026-10-11 18:01:49 +0800", 260),
    ("1e32842", "2026-10-12 16:49:35 +0800", 525),
    ("ef9af29", "2026-10-12 17:55:05 +0800", 255),
    ("35d9f67", "2026-10-13 11:27:16 +0800", 4211),
    ("3c9af12", "2026-10-13 13:45:35 +0800", 380),
)
DATE_LINE = re.compile(r"(?m)^date: .+$")
REMOVED_FIELDS = re.compile(
    r"(?m)^(?:last_updated|last_modified_at|sitemap_omit_lastmod|publication_date_only):.*\n?"
)
DATED_NAME = re.compile(r"^\d{4}-\d{2}-\d{2}-(.+\.md)$")


def slug_from_path(path: str | Path) -> str:
    match = DATED_NAME.fullmatch(Path(path).name)
    if not match:
        raise SystemExit(f"Unexpected post filename: {path}")
    return Path(match.group(1)).stem


def added_slugs(commit: str) -> set[str]:
    output = subprocess.check_output(
        [
            "git",
            "diff-tree",
            "--root",
            "--no-commit-id",
            "--name-only",
            "-r",
            "--diff-filter=A",
            commit,
            "--",
            "_posts",
        ],
        cwd=ROOT,
        text=True,
    )
    return {slug_from_path(line) for line in output.splitlines() if line.endswith(".md")}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    publication: dict[str, tuple[str, str]] = {}
    for commit, timestamp, _expected_current in COHORTS:
        for slug in added_slugs(commit):
            if slug in publication:
                raise SystemExit(f"Slug appears in multiple publication cohorts: {slug}")
            publication[slug] = (timestamp, commit)

    changes: list[tuple[Path, Path, str, str]] = []
    counts: Counter[str] = Counter()
    destinations: set[Path] = set()
    for source in sorted(POSTS.glob("*.md")):
        slug = slug_from_path(source)
        if slug not in publication:
            raise SystemExit(f"No publication record for {source.name}")
        timestamp, commit = publication[slug]
        expected_date = timestamp[:10]
        destination = source.with_name(f"{expected_date}-{slug}.md")
        if destination in destinations:
            raise SystemExit(f"Destination collision: {destination.name}")
        destinations.add(destination)

        original = source.read_text(encoding="utf-8")
        front_matter, separator, body = original.partition("\n---\n")
        if not separator or not front_matter.startswith("---\n"):
            raise SystemExit(f"Invalid front matter: {source.name}")
        if len(DATE_LINE.findall(front_matter)) != 1:
            raise SystemExit(f"Expected one date field: {source.name}")
        cleaned = REMOVED_FIELDS.sub("", front_matter)
        cleaned = DATE_LINE.sub(f"date: {timestamp}", cleaned, count=1)
        updated = cleaned + separator + body
        changes.append((source, destination, updated, commit))
        counts[commit] += 1

    expected_total = sum(item[2] for item in COHORTS)
    if len(changes) != expected_total:
        raise SystemExit(f"Expected {expected_total} current posts; found {len(changes)}")
    for commit, _timestamp, expected in COHORTS:
        if counts[commit] != expected:
            raise SystemExit(f"Expected {expected} current posts from {commit}; found {counts[commit]}")

    print(
        {
            "posts": len(changes),
            "cohorts": dict(counts),
            "apply": args.apply,
        }
    )
    if args.apply:
        temporary: list[tuple[Path, Path, str]] = []
        for index, (source, destination, updated, _commit) in enumerate(changes):
            temp = source.with_name(f".publication-date-migration-{index}.md")
            source.rename(temp)
            temporary.append((temp, destination, updated))
        for temp, destination, updated in temporary:
            temp.rename(destination)
            destination.write_text(updated, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
