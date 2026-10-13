#!/usr/bin/env python3
"""Remove the unsupported shared modification time from the 4,211-post archive cohort.

The archive dates remain unchanged. These posts have no verified per-page
substantive revision time, so the sitemap intentionally omits their lastmod.
"""

from pathlib import Path
import argparse


OLD = "last_modified_at: 2026-10-13 11:46:37 +0800\n"
NEW = "sitemap_omit_lastmod: true\n"
EXPECTED = 4211


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    posts = Path(__file__).resolve().parent.parent / "_posts"
    targets = []
    already_migrated = 0
    for path in posts.glob("*.md"):
        content = path.read_text(encoding="utf-8")
        if OLD not in content:
            if NEW in content.split("\n---\n", 1)[0]:
                already_migrated += 1
            continue
        if not content.startswith("---\n") or content.count(OLD) != 1:
            raise SystemExit(f"Unexpected front matter: {path.name}")
        front_matter = content.split("\n---\n", 1)[0]
        if OLD.strip() not in front_matter or NEW.strip() in front_matter:
            raise SystemExit(f"Unexpected modified timestamp placement: {path.name}")
        targets.append((path, content))
    if len(targets) + already_migrated != EXPECTED:
        raise SystemExit(
            f"Expected {EXPECTED} archive posts; found {len(targets)} pending and {already_migrated} migrated"
        )
    if args.apply:
        for path, content in targets:
            path.write_text(content.replace(OLD, NEW, 1), encoding="utf-8")
    print({"pending": len(targets), "already_migrated": already_migrated, "applied": args.apply})


if __name__ == "__main__":
    main()
