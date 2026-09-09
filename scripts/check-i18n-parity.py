#!/usr/bin/env python3
"""Check LT/EN/RU parity for content files. PL/DE are exempt (stubs)."""

import sys
from pathlib import Path

REQUIRED_LANGS = {"lt", "en", "ru"}
LANG_SUFFIXES = {".lt.md", ".en.md", ".ru.md"}


def main() -> int:
    content_dir = Path("content")
    if not content_dir.exists():
        print("No content/ directory found.")
        return 0
    errors: list[str] = []
    lt_files = sorted(content_dir.rglob("*.lt.md"))
    for lt_file in lt_files:
        stem = str(lt_file)
        base = stem.replace(".lt.md", "")
        siblings = {
            "lt": lt_file.exists(),
            "en": Path(f"{base}.en.md").exists(),
            "ru": Path(f"{base}.ru.md").exists(),
        }
        missing = [lang for lang, present in siblings.items() if not present]
        if missing:
            errors.append(f"{lt_file}: missing siblings: {', '.join(missing)}")
    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        return 1
    print(f"i18n parity OK for {len(lt_files)} LT files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
