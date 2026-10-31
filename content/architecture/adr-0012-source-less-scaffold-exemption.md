---
title: "ADR-0012: Coverage-gate exemption for source-less scaffold repositories"
description: "Architecture Decision Record ADR-0012: exemption from the coverage gate for the ten viavitae-landing-* repositories that contain no source code, and the recorded release scope (D1)."
owner: "@JourneyOfLife"
review_date: 2027-03-09
version: "1.0.0"
language: "en"
sensitivity: "public"
---

# ADR-0012: Coverage-gate exemption for source-less scaffold repositories

> **Language note:** the rest of this registry is written in Lithuanian. This record is
> written in English because its evidence is quoted from the English-language audit
> register, and a machine-translated compliance document is a worse artifact than a
> bilingual one. Translate it and set `language: "lt"` if the registry must be uniform.

| Field | Value |
| --- | --- |
| **Statusas / Status** | Priimtas (decided by the organisation owner on 2026-11-01; this record captures it) |
| **Savininkas / Owner** | @JourneyOfLife |
| **Data / Date** | 2026-11-01 |
| **Sprendėjai / Deciders** | @JourneyOfLife (sole owner, acting as platform owner and DPO) |
| **Konsultuotasi / Consulted** | Independent audit session — evidence E45–E52 in `viavitae-control/docs/security/pre-deployment-independent-audit-2026-10-26.md` |

## Kontekstas (Context)

Ten `viavitae-landing-*` repositories are red in CI: `Lint (python)`, `Test (python)`,
`Typecheck (python)` and the required `CI status` all fail. The cause is not a quality
problem. These repositories **contain no application code at all**.

Measured 2026-10-27 and re-verified 2026-10-31 (live API reads at `ref=main`, never from a
local clone):

| Measurement | Value | Instrument |
| --- | --- | --- |
| Repositories | 10, named in full: `viavitae-landing-basilica`, `viavitae-landing-cathedral`, `viavitae-landing-cemetery-services`, `viavitae-landing-churches-orthodox`, `viavitae-landing-churches-other`, `viavitae-landing-churches-protestant`, `viavitae-landing-deaneries`, `viavitae-landing-diocese`, `viavitae-landing-funeral-services`, `viavitae-landing-parish-church` | `orgs/Via-Vitae/repos`, cross-checked against `repos_data.tf` |
| Files per repository | 19 (18 in `basilica` after its stub removal) | `git/trees/main?recursive=1` |
| Python files | **1** — `main.py`, 528 bytes, the PyCharm sample (`print_hi`); the **identical blob `5596b447…`** in all nine others | tree census + contents API |
| Test files | **0** — no `tests/`, no `test_*.py` | tree census |
| js / ts / jsx / vue | **0** | tree census |
| Deployable web artifacts | **none** — no `index.html`, `package.json`, `hugo.toml`, `netlify.toml` or `Dockerfile` | tree census |
| Declared coverage floor | `COVERAGE_MIN: "80"` in all ten | `ci.yml` |
| Required status checks | only `CI status` and `Compliance status` (classic protection; zero rulesets) | `branches/main/protection` |

CI is therefore behaving **correctly**: the gate is objecting to IDE debris. Writing tests
for `print_hi` would produce exactly the artifact this audit exists to remove — a green gate
that proves nothing (VV-2026-10-017, VV-2026-10-014).

## Sprendimas (Decision)

**Release scope — option D1.** These ten repositories remain **governance scaffold
containers**. They ship nothing, are not built into sites, and are not part of any release.
Actual landing-page content lives in `viavitae-demos/templates`.

**The exemption is defined by a class predicate, not by a name list.** A repository is in
scope while all three conditions hold:

1. the stack-detection rule in `ci.yml` finds no source (`has_source=false`): no
   `pyproject.toml`, no `requirements*.txt`, and no `*.py` file;
2. no other language sources exist (js/ts/jsx/vue) and no deployable artifact exists;
3. the repository's purpose is documents and governance files, not running code.

The ten repositories named in the table above are the current members. **A new repository that
satisfies the predicate joins the class without needing a new ADR**; one that fails it is not
covered. This matters because a list-only exemption silently stops applying at the eleventh
repository.

**Implementation.** Delete `main.py` (IDE debris — not a test, not a gate, not a control) and
reduce `.github/dependabot.yml` to the single ecosystem that can read anything in a
source-less repository: `github-actions`. The other four (`pip`, `npm`, `terraform`,
`docker`) are declared in the template as a superset that the generated repository is
instructed to trim — that step was never performed anywhere (tracked as VV-2026-10-026).

## Pasekmės (Consequences)

**Easier:** `main` becomes green honestly — green because there is nothing to test, and that
is now a documented statement rather than an inference. Roughly 40 weekly failing Dependabot
update attempts across these ten repositories stop.

**Harder, and the accepted risk stated plainly:**

- **`COVERAGE_MIN: "80"` remains declared but unenforced** in these repositories. This is a
  known claim-versus-behaviour mismatch (the VV-2026-10-021 family) and it is recorded here
  rather than left implicit.
- **The legs do not disappear.** They remain visible as `skipped` check runs whose names are
  the unexpanded expressions, e.g. `Lint (${{ matrix.stack }})`. A green `CI status` in these
  repositories means "no source", **not** "source tested".
- **Re-arm condition.** Adding any `*.py`, `pyproject.toml` or `requirements*.txt` makes CI
  detection re-enable the Python legs and the 80 % floor automatically, so the exemption
  cannot smuggle real code past the gate. **One asymmetry to remember:** Dependabot does
  **not** re-arm itself — if a `package.json`, `Dockerfile` or `.tf` is ever added, the
  matching `dependabot.yml` entry must be re-added by hand.
- **Sequencing defect acknowledged.** `viavitae-landing-basilica` was already merged and
  green on `main` **before** this ADR existed — precisely the "silent green" the decision
  package forbids in its own §4. It is recorded here as an open process deviation, not
  presented as if the order had been followed.

## Alternatyvos (Alternatives)

| Alternative | Why rejected |
| --- | --- |
| C. Write tests for `print_hi` to reach 80 % | Satisfies a number while creating the false-assurance artifact this audit exists to remove (VV-2026-10-017, -014); plus ongoing maintenance in ten repositories |
| D2. Turn them into real landing sites | The single largest engineering item in the estate roadmap, with no product decision requiring it today |
| D3. Archive or delete the redundant ones | Requires a `terraform apply` (outside this session's authority) and destroys history with no reversal path |
| Lower `COVERAGE_MIN` to 0 | Would rewrite the declaration to match a misleading state instead of explaining why the state is what it is |

## Atitikties poveikis (Compliance impact)

- **SOC 2 CC8.1 / ISO 27001 A.14 (change management):** a coverage gate on a repository with
  no code is **not** evidence of operating effectiveness. After this exemption the evidence
  set is honest: either a leg runs and reports results, or an approved exemption names the
  class and the reason.
- **GDPR / DPIA:** no personal data is touched; these repositories hold markdown governance
  documents only. No Article 9 processing is created or removed by this decision.
- **Supply chain:** trimming Dependabot to `github-actions` **reduces declared coverage**, and
  that is stated rather than glossed: the other four ecosystems could never resolve a
  manifest here. Org-level Dependabot alerts and security updates remain enabled regardless,
  because they follow the repository's manifests — of which there are none.
- **Configuration management:** `repos_data.tf` sets `manage_files = false` for these
  repositories, so these file edits are **not** performed or reconciled by Terraform. The
  changes are safe to make out of band, but they are unguarded: drift between the ten will not
  be detected automatically. The detective control is `scripts/check_dependabot_scope.py`
  (read-only, operator-run, deliberately not in CI so no credential has to be widened).
- **Evidence:** `viavitae-control/docs/security/pre-deployment-independent-audit-2026-10-26.md`
  (E45–E52; findings VV-2026-10-020, -024, -026) and
  `docs/superpowers/specs/2026-10-27-viavitae-landing-repos-decision-package.md`.

## Patikrinimas (Verification)

```bash
# 1. no Python may remain in the repository
gh api "repos/Via-Vitae/<repo>/git/trees/main?recursive=1" \
  --jq '[.tree[].path | select(endswith(".py"))]'
#    expect: []

# 2. Dependabot must declare exactly one ecosystem, github-actions
gh api "repos/Via-Vitae/<repo>/contents/.github/dependabot.yml" --method GET -f ref=main \
  --jq .content | base64 -d | grep -c "package-ecosystem"
#    expect: 1

# 3. the required contexts must be green on the branch head
gh pr checks <n> -R Via-Vitae/<repo>
#    expect: CI status and Compliance status = pass
```
