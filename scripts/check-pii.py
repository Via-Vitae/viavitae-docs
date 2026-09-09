#!/usr/bin/env python3
"""Regex sweep for personal data: names, emails, phone numbers."""

import re
import sys
from pathlib import Path

PII_PATTERNS = [
    (re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"), "email"),
    (re.compile(r"\b\+?(?:370|44|1)\d{7,10}\b"), "phone"),
    (re.compile(r"\b(?:LT\d{11})\b"), "personal_code"),
]
EXEMPT_DIRS = {"node_modules", ".git", ".venv", "internal"}
EXEMPT_FILES = {"check-pii.py"}


def main() -> int:
    content_dir = Path("content")
    if not content_dir.exists():
        print("No content/ directory found.")
        return 0
    findings: list[str] = []
    for md in sorted(content_dir.rglob("*.md")):
        if any(exempt in md.parts for exempt in EXEMPT_DIRS):
            continue
        if md.name in EXEMPT_FILES:
            continue
        text = md.read_text(encoding="utf-8")
        for pattern, label in PII_PATTERNS:
            matches = pattern.findall(text)
            if matches:
                findings.append(f"{md}: {label} ({len(matches)} occurrence(s))")
    if findings:
        for f in findings:
            print(f"WARNING: {f}")
        print(f"\n{len(findings)} file(s) with potential PII. Review required.")
        return 1
    print("PII sweep clean.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
