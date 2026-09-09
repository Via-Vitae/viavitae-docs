# Pull Request

<!--
Pull request template for viavitae-docs.

Complete every box. A box that genuinely does not apply is annotated "n/a" with a
reason — it is not left blank.
-->

## Summary

<!-- One or two sentences: what changed, and why. -->

## Linked issue

Closes #

## Type of change

- [ ] `docs` — content or documentation only
- [ ] `feat` — a new section or feature
- [ ] `fix` — a correction (broken link, wrong procedure, outdated reference)
- [ ] `chore` — maintenance, tooling, dependencies
- [ ] `ci` — CI configuration only
- [ ] **Breaking change** — describe the migration below

## Checklist

### Content quality

- [ ] **Conventional Commit title** — `<type>(<scope>): <imperative summary>`, per CONTRIBUTING.md
- [ ] **Linked issue** — `Closes #nnn` above, or "n/a" with a reason
- [ ] **Front-matter complete** — every new or changed `.md` has `owner`, `review_date`, `version`, `language`, `sensitivity`
- [ ] **Review date valid** — `review_date` is at most six months from today
- [ ] **No secrets in diff** — Gitleaks run locally, no credential or token anywhere
- [ ] **No PII in diff** — `check-pii.py` reports no personal names, emails, phone numbers

### Compliance

- [ ] **GDPR impact assessed** — if personal data is touched, a DPIA reference is given; otherwise "n/a — no personal data"
- [ ] **i18n parity LT/EN/RU** — if user-facing content is touched, all three locales updated; PL/DE exempt as stubs
- [ ] **Sensitivity correct** — `internal/` content marked `sensitivity: internal`; public content marked `sensitivity: public`

### Documentation

- [ ] **CHANGELOG entry** — follows from the commit type
- [ ] **Links verified** — `check-links.py` passes locally
- [ ] **Owner assigned** — front-matter `owner` field names the responsible person

## GDPR and DPIA

| Field | Value |
| --- | --- |
| Personal data affected | none / identify which |
| DPIA reference | n/a / DPIA-nnn |
| Data residency | EEA-only confirmed |

## AI assistance

- [ ] No AI assistance was used
- [ ] AI assistance was used — I have reviewed every line and take responsibility

## Verification

<!-- How did you prove this works? Commands run and relevant output. -->
