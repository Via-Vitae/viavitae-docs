#!/usr/bin/env python3
"""Check internal link integrity across content files."""

import re
import sys
from pathlib import Path

LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")


def main() -> int:
    content_dir = Path("content")
    if not content_dir.exists():
        print("No content/ directory found.")
        return 0
    all_files = {p.relative_to(content_dir.parent) for p in content_dir.rglob("*.md")}
    errors: list[str] = []
    for md in sorted(content_dir.rglob("*.md")):
        text = md.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            target = match.group(2)
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            if target.startswith("/"):
                resolved = Path("content") / target.lstrip("/")
            else:
                resolved = md.parent / target
            resolved = resolved.resolve()
            if not resolved.exists() and not resolved.with_suffix(".md").exists():
                errors.append(f"{md}: broken link -> {target}")
    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        return 1
    print(f"Link check OK across {len(list(content_dir.rglob('*.md')))} files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
