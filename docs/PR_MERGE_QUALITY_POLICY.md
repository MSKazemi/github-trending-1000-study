# Enterprise-grade pull request review and merge policy

**Effective proposal: 2026-10-13.** This is a human/assistant operating policy and documented CI configuration. **It is not equivalent to GitHub enforced branch protection or a required reviewer setting**; the account's repository administrators must explicitly enable those protections. It applies to all code, methods and external research evidence PRs in this repository.

## Mandatory merge decision

1. **Current base and ownership:** Read `AGENTS.md`, `README.md`, issue/PR rationale and exact changed files. Identify duplicate or overlapping open PRs. Verify diff against **current `main`**, not only the original stale branch base. Inspect proposed deletion/rename and links so accepted material is not lost. Keep the original issue open unless its actual empirical acceptance criteria were met.
2. **Reviewer-verified code:** Review all modified Python and tests (including edge cases and failure modes); reject uncertain external commands, dynamic installs or unchecked network. Check API/backward compatibility, upstream source identity, deterministic behavior, type validation, immutable measurements, missing/unknown handling, timezones, scientific denominators, privacy/rights and non-atomic file output. Prefer an existing module/interface over duplicates.
3. **Security:** Least-privilege GitHub workflow `contents: read`; avoid exposing tokens to untrusted PRs; full commit SHA-pin all official actions; never execute suggested third-party code in CI; inspect new dependencies and sources. Use no unreviewed download/install steps. If a candidate package has unknown license/identity/provenance, do not claim it is safe.
4. **Scientific evidence:** Clearly separate synthetic tests, copied public metadata, first-party vendor claims, actual independently verified results and prospective protocols. Validate support for factual source claims when possible. Never claim 1,000 real repositories, agent attribution, environmental savings or independent human approval without source evidence, consent and appropriate methods review.
5. **Specific mandatory CI:** Check **the latest PR head SHA**, not just a prior commit. Require successful current workflow for each declared Python version, including syntax compile, unittest suite and smoke test. Check the associated job matrix, not merely a green badge or a workflow triggered by a different head. Wait until GitHub reports no conflicts and base compatibility. If head/base changes, re-evaluate and rerun as necessary.
6. **Review and regression tests:** Any observed defect requires a targeted regression test, user-facing documentation/schema update and new CI run. When a PR is draft or requests independent review, **leave draft** until the stated requirement is addressed. A passed synthetic test cannot replace ethics consent, actual live-data permission or a human scientific audit. For documentation-only PRs, verify links, source chronology, scope and non-fabricated counts; run link/structured-data checks where applicable.
7. **Safe merge:** Use squash merge after review and **exact expected head SHA**. Recheck main after merging, verify intended files and CI on the main commit, and record merged commit plus any unresolved external-science blockers on the issue. Do not delete/copy over open work without noting which valuable portions were carried forward and why.
8. **Fail closed:** Conflicts, running/failing CI, unreviewed risks, future unsupported dates, missing data/provenance, surprising scientific claims, unauthorized capture or incompatible duplicate schema => **do not merge**. Provide concrete actionable review feedback and retain the PR while being fixed.

## Expected PR metadata and review evidence
- PR issue, concrete user/research need, before/after acceptance, exact modified paths, changed protocol/schema, reviewer identities where appropriate, dependency reuse decision.
- Link to GitHub Actions workflow run for the **current head SHA**, all matrix job results, static checks, and negative tests.
- Documentation/architecture/README impact, reproducible offline commands and input-output samples with synthetic labels.
- Data source/license/ethics/consent, privacy-safe source citations and null/unknown handling. A methodology-only PR must mark human/source approvals pending.
- Cross-PR conflict matrix (superseded/compatible/complementary), with links and a deliberate choice of **one canonical public interface**.

## Why some drafts remain blocked
The repo intentionally has a pipeline of partial scientific instruments and unscreened provider/company evidence. Draft is not an indicator of poor code but it is a **reliable release blocker** until its stated independent source verification and protocol checks are done. Quality means preserving useful source material without inflating certainty.

### Code versus scientific acceptance
A standard-library pilot tool can be safely merged if independently reviewed, regression-tested and clearly labeled self-reported, even before empirical validation. It **cannot** close an issue whose deliverable requires a real data sample, independently recruited annotators, calibrated energy or publication-grade evidence. Prefer explicitly partial merges with open follow-up work.

## CI configuration decisions
- Pinned `actions/checkout@v7.0.1` to immutable commit `3d3c42e5aac5ba805825da76410c181273ba90b1`; pinned `actions/setup-python@v7.0.0` to `5fda3b95a4ea91299a34e894583c3862153e4b97`, verified via official public GitHub tag refs on 2026-10-13. See [checkout release](https://github.com/actions/checkout/releases/tag/v7.0.1) and [setup-python release](https://github.com/actions/setup-python/releases/tag/v7.0.0).
- Three supported interpreter checks: Python 3.10, 3.12 and 3.14. PR and `main` events, instead of duplicating push and PR runs for every development branch, plus `cancel-in-progress` for superseded commit jobs; reduces redundant build work while preserving protected-main integration signals.
- Non-fast-fail test matrix, read-only permissions, 15-minute job limit, compileall+full unittest+CLI help. These are **necessary not sufficient** conditions; they do not imply static security analysis, vulnerability scan, branch protection, lint/type coverage or scientific reproducibility on real sources.
- Action-version changes require separate CI test and a specific release review; tag names in comments are for provenance and **not mutable execution references**.
