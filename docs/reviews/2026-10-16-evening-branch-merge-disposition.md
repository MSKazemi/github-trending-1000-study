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

## 2026-10-16 later audit: all eleven open PRs and safe merge holds

**Snapshot:** the GitHub branch search returned 41 named refs including `main`. The live PR search returned eleven open PRs (#290, #293, #298, #302, #417, #418, #425, #426, #427, #428, #429), all targeting main at `1e656cfcbceb4995467280b796e77e870c6c5f39` at inspection. Every PR reported `mergeable=true`; #302 remains a draft. The submitted GitHub review list for all eleven was empty. The inline review thread lists checked for #290, #293, #302, #417, #418 and #429 were empty. **Empty reviews do not constitute human signoff.**

| PR | Exact head inspected | Five-job PR Actions run (successful at inspection) | Current disposition |
| --- | --- | --- | --- |
| #290 | `8853ff5da8da63468a11a3b80d9c2cd44ba892d1` | [38931512003](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38931512003) | HOLD: denominators/rank-proxy methods approval |
| #293 | `0c520b7fadb9cb952b1d73214d66d903e88587bf` | [38931125246](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38931125246) | HOLD: registry/source and methods approval |
| #298 | `4aa3ccce7e9431369973a41abda6a846c6c5d238` | [38931060295](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38931060295) | HOLD: genuine blinded reviewer evidence and methods approval |
| #302 | `80a2fdd1fd7940d87befc6613d2dc71147505a46` | [38932139921](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38932139921) | DRAFT/HOLD: security and administrator enforcement (rulesets endpoint returned `[]`) |
| #417 | `a6f23bba1db3b3f3859aff69d1fbb4d7f3baab3e` | [38931707439](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38931707439) | HOLD: human maintainer inspection of destructive-prune advice boundary |
| #418 | `cbd70f0e46e4321c17c9542ec2dcf8c264283498` | [38931180599](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38931180599) | HOLD: bibliographic/source-rights review |
| #425 | `69d02f95664fafd74d85b640036bbb7c4074bd86` | [38930766286](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38930766286) | HOLD: privacy/security maintainer review |
| #426 | `477141bc4c246a203901e3b7514cf990c2052b64` | [38930663841](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38930663841) | HOLD: news-source identity and methods review |
| #427 | `eede47a1daa408182a7fbbe42a97724307e5cf87` | [38929707071](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38929707071) | This audit-documentation PR: updated after this run; **new exact-head CI and human review required** |
| #428 | `bf67a94a267c0107fc2c3d933ef267e501e12ebc` | [38930904561](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38930904561) | Additional lexical numeric-host hardening committed later to head `114d76b02c401bcec27b7bf2b84da9c1eb04254c`; previous CI is **stale**. New CI and security review required |
| #429 | `865f0d1b2047e94059a41d29476cc464df3ed226` | [38931239853](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38931239853) | HOLD: source-security review and explicit URL validator's no-network-safety limit |

The job API was inspected for all eleven listed runs: each then reported completed success for `test (3.10)`, `test (3.12)`, `test (3.13)`, `test (3.14)`, and `research-artifacts`. This is technical evidence, not an independent code/methods or security review. #428 received three direct branch commits for source, tests and documentation after the run cited above; update its check record before merge consideration. The #427 head changes by this documentation update too. No claims of successful new-head CI on either are made.

The current open-PR changed paths show no immediate same-file overlap across the small URL/privacy/news patches (#425, #426, #428, #429), but PR #298 changes shared JSON integrity code and #290 alters CI/README/data dictionary; take current-base integration and full-diff preservation checks before any future merge. No branch or tag deletion, force push, source promotion, human approval, or research issue closure is authorized. Rulesets list was empty, while detailed main protection read was denied (403), so server enforcement could not be established.

**Practical maintainer takeaway:** one successful PR run is pinned to one head SHA. A single follow-up security fix invalidates that merge-ready claim until a new run passes, and an automated agent cannot approve its own changes. Protect main through actual server settings and have a separate reviewer inspect the full, final patch.
