# Branch and PR integration checkpoint — 2026-10-16 (evening)

**Scope:** AI-assisted, time-bound GitHub API review of 35 branch refs (main plus 34 others), seven open PRs, file-level ancestry comparisons, CI, review threads and recorded scientific/security holds. This checkpoint is not independent human methodological review or a waiver of the canonical [merge gate](../PR_MERGE_QUALITY_GATE_2026_10_13.md).

## Verified engineering integration

- **PR #416 (issue #100)**: integrated the then-current `main@8461a3ab7ffa1dff7e91dade0069922d43c7b3a9` with the archival PR head `9e8f97478f456f1c6b0ba83dd2fd7a5e04e4682f`. New head `f67990a82fdf15629bba926a7dc6a08cbb145d6b` has both as parents and retained exactly three new paths.
- Historical candidate CSV under `docs/reviews/2026-10-16-issue-100-provisional-changelog-ledger.csv` was confirmed to have original Git blob SHA `0e12d6d668423379f4aaf72d4c5da6938ca4c98c` (19 candidate rows). Canonical 63-row `033-github.events.csv` remained at blob `a93f703f16fc30ed5e1b2759848b4532ef1ef686` before integration; no canonical ledger edit in the three-file compare.
- Exact integrated PR-head `pull_request` Actions run [38919149179](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38919149179) completed with five successful jobs: Python 3.10, 3.12, 3.13, 3.14, research-artifacts. Merge with expected head returned commit **`1e656cfcbceb4995467280b796e77e870c6c5f39`**; GitHub readback confirmed PR merged and main at that SHA.
- Post-merge [push run 38929509754](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38929509754) reported all five jobs completed **success** on inspection; verify full run conclusion again for release decisions. Issue #100 remains open: archived candidate vendor announcements are not independently authenticated scientific results.

## Six open PR holds (observed at audit start)

| PR | Branch | Decision and required independent gate |
| --- | --- | --- |
| [#417](https://github.com/MSKazemi/github-trending-1000-study/pull/417) | `fix/279-branch-tip-recheck-20261016` | Keep open for independent maintainer review of branch-tip race safety and recovery; no destructive prune authorization. |
| [#293](https://github.com/MSKazemi/github-trending-1000-study/pull/293) | `research/issue-15-registry-cohort-pilot-20261014` | Hold for registry-rights, provenance, real task–package independent judgments, qualified methods review. |
| [#298](https://github.com/MSKazemi/github-trending-1000-study/pull/298) | `research/issue-223-hiring-blind-agreement` | Hold for genuine two-human blinded rating, employer-source rights and codebook methods signoff. Synthetic labels do not establish independent agreement. |
| [#418](https://github.com/MSKazemi/github-trending-1000-study/pull/418) | `research/issue-7-literature-source-screen-20261016` | Hold for independent bibliography/rights/protocol and full reproducible screening audit; 11 leads are not a systematic review. |
| [#302](https://github.com/MSKazemi/github-trending-1000-study/pull/302) | `chore/248-reviewable-ruleset-payloads-20261014` | **Draft; do not merge.** Owner/security approval and administrator-enforced rulesets plus negative enforcement tests outstanding. |
| [#290](https://github.com/MSKazemi/github-trending-1000-study/pull/290) | `research/issue-6-coverage-chronological-proxy-20261014` | Hold for qualified scientific review of denominators/ranking proxy, source-access policy and holdout design. |

At review start the above six heads were all behind the moving main by five commits despite successful older head CI, and every inspected GitHub PR review list and inline thread list was empty. A clean automatic mergeability flag alone is insufficient. Fresh checks and current-base reconciliation are mandatory after any change. The separate branch `integration/five-pr-no-loss-20261016` also contained overlapping proposed work; do not mass-merge it over reviewed issue-scoped PRs.

## Branch-only reconciliation notes

- The GitHub first-page branch list returned 35 refs. Of 27 non-PR/non-main branches, many old CI, quality, and issue branches had large behind counts but nonzero ahead commits; **ahead counts are not evidence of unique changes after squash merges**. Do not delete them or resurrect outdated files without bytewise equivalence checks.
- Historical `research/issue-100-github-changelog-ledger-20261016` remains distinct from the quarantined documentation archive; the archival merge deliberately did not replace the canonical source ledger.
- Main branch reported `protected=false` and repository ruleset list `[]`. GitHub enforcement is not installed; this operational gap remains P0, regardless of green checks. The branch-protection REST endpoint was inaccessible to the GitHub App (403), but independent branch/ruleset readbacks were available.
- Do not force-push, delete branches/tags, claim source permission, mark scientific issues complete, or substitute automated review for a qualified independent reviewer.

## Practical lessons for repository maintenance

1. Preserve uniquely authored historical candidate data in a **noncanonical archive** when row identifiers collide; require reviewed source-event reconciliation before promotion.
2. Merge against the actual moving base, use expected-head SHA, and require a **new five-job PR run and separate successful main push run**.
3. Separate software-validating CI from human methods, legal/source, security, scientific and participant approvals.
4. Do not equate ahead-commit count, branch age, or checkmarks with no-loss equivalence, deletion safety, or reusable task value.
5. Enable tested server-side main protection so that a future agent/Claude Code workflow cannot bypass the documented gates simply because GitHub reports mergeable.
