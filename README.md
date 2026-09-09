# viavitae-docs

[![CI](https://github.com/Via-Vitae/viavitae-docs/actions/workflows/ci.yml/badge.svg)](https://github.com/Via-Vitae/viavitae-docs/actions/workflows/ci.yml)
[![Compliance](https://github.com/Via-Vitae/viavitae-docs/actions/workflows/compliance-check.yml/badge.svg)](https://github.com/Via-Vitae/viavitae-docs/actions/workflows/compliance-check.yml)
[![CodeQL](https://github.com/Via-Vitae/viavitae-docs/actions/workflows/codeql.yml/badge.svg)](https://github.com/Via-Vitae/viavitae-docs/actions/workflows/codeql.yml)
[![Publish](https://github.com/Via-Vitae/viavitae-docs/actions/workflows/publish.yml/badge.svg)](https://github.com/Via-Vitae/viavitae-docs/actions/workflows/publish.yml)
[![Licence](https://img.shields.io/badge/licence-Proprietary-0E1B3D?labelColor=F7F4EC)](LICENSE)
[![EU hosted](https://img.shields.io/badge/hosted-EU-0E1B3D?labelColor=F7F4EC)](SECURITY.md)

> Single source of truth for ViaVitae compliance, architecture decisions, runbooks and
> client onboarding knowledge. Multilingual (LT/EN/RU), published as a docs site from
> public content; restricted content stays repo-internal.

`viavitae-docs` is the documentation and compliance hub for the ViaVitae organisation.
Primary audiences: auditors, security reviewers, ViaVitae engineers, and parish/diocese
clients (LT/EN/RU). Built with Hugo and the Doks theme, deployed to `docs.viavitae.com`
on self-hosted Proxmox infrastructure via Argo CD.

---

## Table of Contents

- [Repository structure](#repository-structure)
- [Local preview](#local-preview)
- [Conventions enforced by CI](#conventions-enforced-by-ci)
- [Contributing](#contributing)
- [Security and compliance](#security-and-compliance)
- [Licence](#licence)

---

## Repository structure

```text
viavitae-docs/
├── config/          # Hugo + Doks configuration (multilingual LT/EN/RU)
├── content/         # Docs site source: architecture, GDPR, security, runbooks, onboarding
├── layouts/         # Custom Hugo partials and shortcodes
├── assets/          # Images, diagrams (Excalidraw/DrawIO), JS helpers
├── docs/            # Repo-level ADR template and DPIA template (from viavitae-template)
├── internal/        # Repo-only: compliance checklists, audit evidence, meeting notes
├── scripts/         # Python validation: front-matter, i18n parity, links, PII sweep
└── .github/         # Governance, CI/CD workflows, issue and PR templates
```

## Local preview

```bash
npm install
docker compose up   # Hugo server at http://localhost:1313
```

## Conventions enforced by CI

1. **Front-matter on every doc:** `owner`, `review_date` (max +6 months), `version`,
   `language`, `sensitivity` (public / clients-only / internal).
2. **Trilingual parity:** any `*.lt.md` addition without `*.en.md` + `*.ru.md` sibling
   fails `check-i18n-parity.py` (PL/DE exempt — stubs).
3. **PII sweep:** `check-pii.py` + Gitleaks run on every PR; findings block merge.
4. **Link integrity:** `check-links.py` in CI; publish workflow rebuilds search index.
5. **Sensitivity gating:** `internal/` never built into the public site (Hugo ignore
   mounts configured in `config/_default/hugo.toml`).
6. **Publish:** `publish.yml` builds the static site, signs artefacts, deploys via Argo CD
   to `docs.viavitae.com` on Proxmox (EU).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full workflow. Documentation-specific rules:

- Branch prefix: `docs/` for content changes, `chore/` for tooling.
- Every doc page carries front-matter with `owner`, `review_date`, `version`, `language`
  and `sensitivity`.
- LT is the source language; EN and RU must reach parity in the same PR.
- Internal content (`internal/`) is never published to the docs site.

## Security and compliance

- To report a vulnerability, follow the private disclosure process in
  [SECURITY.md](SECURITY.md). Do **not** open a public issue.
- Personal-data processing requires a completed
  [DPIA](docs/DPIA-template.md) under GDPR Article 35 before processing starts.
- Architectural choices are recorded as [ADRs](docs/architecture.md).

## Licence

Proprietary — All Rights Reserved. (c) ViaVitae IT Technologies. No redistribution, no
derivative works and no commercial use by third parties without a written agreement.
Governed by the law of Lithuania (EU). See [LICENSE](LICENSE).
