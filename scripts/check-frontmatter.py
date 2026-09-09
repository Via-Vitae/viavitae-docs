#!/usr/bin/env python3
"""Validate front-matter on every content .md file against frontmatter.schema.json."""

import json
import sys
from datetime import date, timedelta
from pathlib import Path

import yaml

REQUIRED_FIELDS = {"owner", "review_date", "version", "language", "sensitivity"}
VALID_LANGUAGES = {"lt", "en", "ru", "pl", "de"}
VALID_SENSITIVITIES = {"public", "clients-only", "internal"}
MAX_REVIEW_DAYS = 183  # ~6 months


def check_file(path: Path) -> list[str]:
    errors = []
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return [f"{path}: missing front-matter"]
    parts = text.split("---", 2)
    if len(parts) < 3:
        return [f"{path}: malformed front-matter"]
    try:
        fm = yaml.safe_load(parts[1])
    except yaml.YAMLError as e:
        return [f"{path}: YAML parse error: {e}"]
    if not isinstance(fm, dict):
        return [f"{path}: front-matter is not a mapping"]
    missing = REQUIRED_FIELDS - set(fm.keys())
    if missing:
        errors.append(f"{path}: missing fields: {', '.join(sorted(missing))}")
    lang = fm.get("language")
    if lang and lang not in VALID_LANGUAGES:
        errors.append(f"{path}: invalid language '{lang}'")
    sens = fm.get("sensitivity")
    if sens and sens not in VALID_SENSITIVITIES:
        errors.append(f"{path}: invalid sensitivity '{sens}'")
    rd = fm.get("review_date")
    if rd:
        if isinstance(rd, date):
            max_date = date.today() + timedelta(days=MAX_REVIEW_DAYS)
            if rd > max_date:
                errors.append(f"{path}: review_date {rd} exceeds 6 months")
        else:
            errors.append(f"{path}: review_date is not a date")
    return errors


def main() -> int:
    content_dir = Path("content")
    if not content_dir.exists():
        print("No content/ directory found.")
        return 0
    all_errors: list[str] = []
    for md in sorted(content_dir.rglob("*.md")):
        all_errors.extend(check_file(md))
    if all_errors:
        for e in all_errors:
            print(f"ERROR: {e}")
        return 1
    print(f"Front-matter OK on {len(list(content_dir.rglob('*.md')))} files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
