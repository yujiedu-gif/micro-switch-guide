#!/usr/bin/env python3
"""Set unpublished, untracked Jekyll posts to their actual launch date.

Only files under _posts that Git has never tracked are eligible. The command
validates every target before changing anything, and defaults to a dry run.
"""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
import subprocess


DATE_LINE = re.compile(r"(?m)^date: \d{4}-\d{2}-\d{2} 09:00:00 \+0800$")
FILENAME = re.compile(r"^\d{4}-\d{2}-\d{2}-(.+\.md)$")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", required=True, type=date.fromisoformat)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    result = subprocess.run(
        ["git", "ls-files", "--others", "--exclude-standard", "-z", "--", "_posts"],
        cwd=root,
        check=True,
        capture_output=True,
    )
    files = [root / raw.decode() for raw in result.stdout.split(b"\0") if raw]
    if not files:
        raise SystemExit("No untracked posts to redate")
    moves: list[tuple[Path, Path, str]] = []
    destinations: set[Path] = set()
    for source in files:
        match = FILENAME.fullmatch(source.name)
        if not match:
            raise SystemExit(f"Unexpected post name: {source.name}")
        content = source.read_text(encoding="utf-8")
        if not content.startswith("---\n") or len(DATE_LINE.findall(content)) != 1:
            raise SystemExit(f"Unexpected date front matter: {source.name}")
        destination = source.with_name(f"{args.date.isoformat()}-{match.group(1)}")
        if destination in destinations or (destination.exists() and destination != source):
            raise SystemExit(f"Destination collision: {destination.name}")
        destinations.add(destination)
        updated = DATE_LINE.sub(f"date: {args.date.isoformat()} 09:00:00 +0800", content)
        moves.append((source, destination, updated))
    print(f"Validated {len(moves)} unpublished posts for {args.date.isoformat()}")
    if args.apply:
        for source, destination, updated in moves:
            if source != destination:
                source.rename(destination)
            destination.write_text(updated, encoding="utf-8")
        print(f"Redated {len(moves)} posts")
    else:
        print("Dry run only; pass --apply to change files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
