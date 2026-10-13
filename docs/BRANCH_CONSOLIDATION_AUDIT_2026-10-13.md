# Branch consolidation and no-loss integration audit — 2026-10-13

**Scope:** connected GitHub API point-in-time inventory of `MSKazemi/github-trending-1000-study`. This is engineering triage, not scientific evidence validation, independent source verification or permission to merge draft research PRs. Recheck heads and rules before every mutation.

## Verified snapshot

- Default branch: `main`, commit `6339775d73886b24f746139cdf55a34384f88c33` at inspection.
- **123 GitHub branches** returned across the first two GitHub REST pages (100 + 23), including `main`. **39 open PRs**, all flagged `draft: true`.
- GitHub `GET /branches/main` reported `protected: false`; repository rulesets endpoint returned `[]`. The CI workflow provides checks but not a repository merge-enforcement policy.
- On this exact main commit, GitHub Actions reported five completed successful checks: `test (3.10)`, `test (3.12)`, `test (3.13)`, `test (3.14)` and `research-artifacts`. These are engineering tests, not methodological signoff.
- Local clone/verification was unavailable in the working environment because DNS could not resolve `github.com`. GitHub API checks are not a substitute for fresh integrated-tree tests or manual claim review.

## Executed branch-safe action

Branch `ci/enterprise-pr-qa-gates-issue-240` originally pointed to `2ee638a04d335ef895c5fd981c1b039ee8188d60`. `compare(main...branch)` reported `ahead_by: 0`, `behind_by: 11`, merge base exactly equal to that branch head, and zero changed files. Accordingly, a **non-forced fast-forward** to `main` SHA `6339775d73886b24f746139cdf55a34384f88c33` was executed with `expected_sha` equal to the original head; GitHub returned success. No original commit was discarded or main changed by this action. Further work on the branch requires a separate review PR.

## Open no-loss collisions (do not blindly merge)

Each pair touches an overlapping company Markdown report **and** research events artifact, with different additions/file formats:

| Subject | Competing draft PRs | Preservation need |
|---|---|---|
| Meta | #191 / #228 | Source records, event chronology, counter-evidence |
| Amazon/AWS | #192 / #229 | Both records and source/date checks |
| Amp | #197 / #231 | JSON vs CSV event differences and distinct report claims |
| Replit | #212 / #230 | Both event registers and report sections |
| Qodo | #213 / #232 | Both event registers, license discrepancies and existing crosswalk |

All five pairs were checked for touched paths and reported CI histories; the branch reports remain **draft**. Older versions of the checks include only 3.10/3.12; some newer exact heads show the wider CI checks. **Neither state is authorization to publish externally sourced claims.** No full independent citation verification or three-way resolution was performed in this audit.

## Other branch groups

- `ci/*`, `fix/*` and `quality/*` branches often overlap `.github/workflows/ci.yml`, `trending_study/data_integrity.py` and related tests. These are not safe to co-merge unreviewed.
- Numerous `feat/*` branches diverge far behind main, including code and docs. Check whether later main commits retained their behavior; `ahead_by > 0` alone is **not** proof of remaining useful code, and cherry-picking all changes may reintroduce obsolete defects.
- Several company-intelligence branches and provisional news/hiring reports retain distinct source leads. Do not delete merely to reach a low branch count.
- In a targeted sample of legacy engineering branches, only `ci/enterprise-pr-qa-gates-issue-240` had `ahead_by: 0` and a fast-forwardable ancestral head. Other inspected branches were divergent; this is **not** an exhaustive ancestry classification of all 123 branches.

## Safe phased consolidation protocol

1. **Freeze competing work on the same canonical paths** while taking a fresh `main`/PR/branch inventory. Record full SHAs, branch owner, open PR and issue mapping, exact touched paths, review state and CI links.
2. **Classify by proofs**, not by names: (A) ancestral/fully merged; (B) unique files/tests/docs; (C) same-path conflicts; (D) unresolved provenance or required human scientific approval. Never use ahead/behind alone as a deletion proof.
3. **Preserve unique evidence**: for each collision create a source-level crosswalk with original PR/file/line/date/source URL, verified vs disputed claims, field/missingness differences, and tests. Retain provenance in a canonical artifact plus attributable original PR history.
4. **Reconcile a single bounded change** against latest main, run offline tests on the integrated candidate (Python 3.10, 3.12, 3.13, 3.14, artifact integrity, negative tests) and inspect full diff and reviews. Do not silently revive disabled live Trending capture.
5. **Merge only non-draft validated PRs** with `expected_head_sha`, all required independent reviews and qualified human methods/security/source approval where applicable; check main CI after merge.
6. **Cleanup last**: delete only branches whose exact tip is an ancestor of main **and** whose original sources/links and research decisions are preserved, with no open PR or downstream use. Use a reversible inventory and branch-tip log. GitHub API connector in this session does not expose a branch-ref delete operation.
7. Ask a repository administrator to enforce rules on `main`: review required, current required checks (all four Python versions plus research-artifacts), conversation resolution, no direct/force push, no main deletion. Verify with negative integration tests rather than treating a policy file as enforcement.

## Operational target and practical lessons

**Recommendation, not a current count or scientific result:** maintain `main` plus roughly 3–5 **active short-lived** topic/integration branches; preserve unfinished science as issues and traceable evidence artifacts rather than automatically merging or deleting drafts. Existing dormant branches should be reduced only after the proof process.

For the broader reuse-first research, apply the same lesson to software portfolios: fewer maintained implementations can lower integration/maintenance burden only if independent user-task acceptance, safety/license compatibility, developer effort and environmental/system-boundary evidence support the choice. Neither branch count, merged PRs, stars nor passing synthetic CI are measures of actual utility or green-computing impact.
