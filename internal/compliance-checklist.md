---
title: "Vidinis atitikties kontrolinis sąrašas"
description: "PR šablono elementų susiejimas su dokumentų sekcijomis."
owner: "@JourneyOfLife"
review_date: 2027-03-09
version: "1.0.0"
language: "lt"
sensitivity: "internal"
---

# Vidinis atitikties kontrolinis sąrašas

Šis dokumentas susieja PR šablono elementus su dokumentų sekcijomis. Naudojamas kaip
priėmimo šaltinis peržiūros metu.

| PR elementas | Dokumento sekcija |
| --- | --- |
| Front-matter užpildytas | `scripts/check-frontmatter.py` |
| LT/EN/RU lygiavertiškumas | `scripts/check-i18n-parity.py` |
| PII švarus | `scripts/check-pii.py` |
| Nuorodos veikia | `scripts/check-links.py` |
