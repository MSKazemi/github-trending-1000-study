## Change summary and issue

Related issue: #

Describe the single bounded change, affected interfaces/schema versions, and why reuse of an existing module is insufficient.

## Merge-quality checklist (complete before requesting non-draft review)

- [ ] Read `AGENTS.md`, `CONTRIBUTING.md` and relevant evidence/protocol documentation; scope remains bounded
- [ ] Inspected all changed files, related open PRs and duplicate-implementation risk; retained unique data, citations, docs and regression cases
- [ ] No secrets, unapproved scraping, private logs, unsafe dependency installation, or overwritten write-once evidence
- [ ] Added appropriate negative/error/missingness tests and updated docs for every schema/API change
- [ ] Final-head GitHub Actions (Python 3.10, 3.12 and 3.14 compile, unit and CLI smoke tests) completed successfully: **run URL:** 
- [ ] No unresolved review objections, license/security concerns, merge conflicts or unreviewed interface compatibility breaks
- [ ] If a protocol, scientific source, blinded judgment or security recommendation is affected: genuine qualified independent human approval recorded below (or **pending—not merge-ready**)
- [ ] Commit SHA rechecked immediately before merge; post-merge `main` CI will be verified

## Evidence, risks and non-claims

**Original sources (exact URLs/dates):**

**What was actually tested vs not independently verified:**

**Known invalid/negative/null cases and missingness:**

**Migration/other PR preservation:**

**Genuine human reviewer and approval link, when required:** pending

## Compatibility, external acceptance, and reversibility

**User-relevant task and expected behavior:**

**Existing compatible implementation or upstream alternative investigated:**

**Why a new change is justified:**

**API/schema/migration and backward-compatibility plan:**

**Affected documentation and reproducible acceptance test:**

**Potential overlapping PRs or preserved source artifacts:**

**Rollback strategy and post-merge observation:**

## Evidence classification and independent verification

**Evidence type:** [ ] synthetic only [ ] public metadata [ ] consented and registered experiment [ ] provisional methodology [ ] documentation-only.

**Source URL, publication date, event date, version/rights and uncertainty (as applicable):**

**Unverified claims, expected negative/null cases, missing denominator or observations:**

**Security, permissions, package identity and dependencies reviewed:**

**External human reviewer / ethics approval record (only if actually obtained):**

**Reviewed PR head SHA, CI run URLs and integration base:**

## Reproduction

```bash
python -m compileall -q trending_study tests
python -m unittest discover -s tests -v
```

Checklist ticks, automated reviews and green CI do not certify source authenticity, human independence, deployment safety or the research protocol. See [PR merge gate](../docs/PR_MERGE_QUALITY_GATE_2026_10_13.md).
