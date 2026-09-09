# Contributing

Thank you for contributing to `viavitae-docs`. This document describes the workflow
that applies to this repository.

Read [QODER.md](QODER.md) before contributing with AI assistance, and
[SECURITY.md](SECURITY.md) before reporting anything security-related. Security reports
never go through a public issue or pull request.

---

## Code of conduct

Contributors, reviewers and maintainers are expected to treat each other with respect, to
critique work rather than people, and to assume good faith. Harassment, discrimination and
personal attacks are not accepted in any ViaVitae space.

Report a concern to `legal@viavitae.com`. Reports are handled confidentially.

Because ViaVitae serves religious communities, contributors additionally commit to
respecting the confidentiality and dignity of data subjects — many of whom are members of a
congregation and never consented to their data being discussed in a public forum.

## Development model: trunk-based

We work trunk-based. `main` is always deployable, always protected, and always moving.

- Branch from `main`, merge back to `main`. No long-lived feature branches.
- Force-pushes to `main` are disabled. Review dismissal is disabled. Administrators are
  not exempt from branch protection.

## Branch naming

| Prefix | Use | Example |
| --- | --- | --- |
| `docs/` | Documentation content changes | `docs/dpia-003-cemetery-map` |
| `feat/` | A new feature or section | `feat/seo-keyword-clusters` |
| `fix/` | A correction (broken link, wrong procedure) | `fix/broken-adr-link` |
| `chore/` | Maintenance, tooling, dependencies | `chore/update-doks-theme` |
| `ci/` | CI configuration only | `ci/add-frontmatter-check` |

Keep names lowercase, hyphen-separated, and under 50 characters.

## Conventional Commits

Every commit message follows [Conventional Commits](https://www.conventionalcommits.org/).

```text
<type>(<scope>): <imperative summary, max 72 characters>

Signed-off-by: Your Name <you@viavitae.com>
```

Rules:

- Use the imperative mood: "add runbook", not "added runbook".
- Scope is the content area: `docs(gdpr):`, `docs(security):`, `docs(runbooks):`.
- Never mention a credential, customer name or personal data in a commit message.

## Developer Certificate of Origin

Every commit carries a DCO sign-off line:

```text
Signed-off-by: Your Name <you@viavitae.com>
```

Add it with `git commit -s`.

## Pull request rules

A pull request may be merged only when **all** of the following hold:

1. **One approving review** from a CODEOWNERS-listed owner.
2. **Green CI** — markdown lint, link check, front-matter schema check.
3. **Green compliance** — no secret found, every licence allow-listed, governance files
   present.
4. **Clean CodeQL** — no new finding in the JS analysis of site theme and scripts.
5. **Front-matter complete** — every new or changed `.md` carries `owner`, `review_date`,
   `version`, `language` and `sensitivity`.
6. **Trilingual parity** — LT/EN/RU siblings are present for every user-facing page.
7. **PII sweep clean** — `check-pii.py` reports no personal data in the diff.

## Documentation-specific conventions

- **LT is the source language.** EN and RU translations must reach parity in the same PR.
  PL and DE are stubs and are exempt.
- **Front-matter is mandatory** on every doc page. See `frontmatter.schema.json`.
- **Internal content** (`internal/`) is never published to the docs site.
- **No real client PII** in any content file, diagram, screenshot or commit message.
- **Review dates** are at most six months from the date of writing or last review.

## Getting help

| Question | Where |
| --- | --- |
| Workflow, review, branch or commit rules | This document |
| Architecture or design decisions | Record as an ADR in `docs/architecture.md` |
| Personal data, DPIA, retention, processors | `dpo@viavitae.com` |
| Vulnerabilities and security incidents | `security@viavitae.com` — private, per [SECURITY.md](SECURITY.md) |
