"""Remove duplicate leading Markdown H1s from Jekyll posts.

The post layout already renders front-matter title as the sole H1. This
one-time migration is dry-run by default and accepts explicit file paths.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


LEADING_H1 = re.compile(r"\A(---\n.*?\n---\n\n)#\s+[^\n]+\n+(?=\S)", re.DOTALL)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    changed = []
    for path in args.paths:
        original = path.read_text(encoding="utf-8")
        updated, count = LEADING_H1.subn(r"\1", original, count=1)
        if count:
            changed.append(str(path))
            if args.apply:
                path.write_text(updated, encoding="utf-8")
    print(f"scanned={len(args.paths)} changed={len(changed)} applied={args.apply}")
    for path in changed:
        print(path)


if __name__ == "__main__":
    main()
