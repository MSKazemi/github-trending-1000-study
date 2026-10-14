# Verified merged-branch retirement — 2026-10-13

**State at initial review:** 123 branches, 39 open draft PRs, 65 merged PRs; 60 exact head-to-merged-PR branch matches are eligible for *independent revalidation*. The branch list and draft status are time-bound observations, not research findings.

## Strict no-loss retirement

The [committed allowlist](../ops/branch-retirement/approved-merged-pr-branches-2026-10-13.json) pins **each of the 60 branches** to a GitHub PR number, exact last-reviewed head SHA and merged commit SHA. It is not a wildcard or retrospective inference from a branch name. The source main SHA for this inventory is `6339775d73886b24f746139cdf55a34384f88c33`.

The [offline standard-library retirement implementation](../scripts/retire_merged_branches.py) and [negative tests](../tests/test_retire_merged_branches.py) fail closed unless each GitHub branch remains unprotected and unchanged, the PR is actually merged to `main`, and **no open PR** references the branch. Before removing the branch ref, a recovery tag `refs/tags/branch-archive/2026-10-13/<original-branch-name>` must exist and point to the exact original commit. The script verifies this recovery ref and rechecks the branch and open PR state immediately before deleting. Existing tags with different SHAs block deletion. Partial failures remain logged and do **not** authorize further deletions outside the plan. No study dataset or source document is rewritten.

The [separate one-time GitHub Actions job](../.github/workflows/retire-verified-branches.yml) runs on approved plan introduction to `main` and has isolated `contents: write` permission; normal tests stay read-only. This is not a general cleanup bot: only explicit PR-reviewed allowed candidates can be retired. It supports manual re-execution for idempotent recovery, but does not continually delete new branches.

**Recovery:** The original code/commit is reachable via its archival tag, original merged PR and GitHub history. A branch can be recreated from the tag if required. A squash merge does not make pre-squash history an ancestor of `main`; archiving the original source SHA protects that history rather than assuming squash preservation alone is enough. Tags should not be deleted without a separate recovery/retention decision.

## Exclusions and safety boundaries

- **39 open draft PR branches:** retain; source/claim review and overlapping company reports are incomplete. Do not bulk-merge or delete them.
- **5 branches advanced since their PR merged:** quarantine for diff and provenance review; an old green check does not attest newer commits.
- **18 other branches without an open or currently merged PR:** investigate individually, including 17 closed-unmerged PR branches and any unmatched branch. Do not infer supersession from a title alone.
- **`main`** is never eligible. Protected branches, mismatched head SHA, current open PRs, insufficient token permissions or unverified archival refs fail closed.

Remaining branches after full success: approximately **63**, including draft and unresolved research branches. The strategic target is at most 5–10 focused **active** development branches at a time once open company intelligence drafts have genuine source verification and are combined into coherent evidence ledgers. Fewer branches is a maintainability goal, **not** evidence of improved software usefulness or lower electricity use.

## Next branch consolidation phase

1. Group overlapping company screens into canonical per-company evidence registers and one or two review PRs. Preserve every distinct source lead and its provenance; do not treat vendor statements as independent measurements.
2. Compare post-merge changed branch heads to original merged PR heads; cherry-pick unique, tested improvements into a focused PR or archive those commits with an explicit review record before pruning.
3. For closed-unmerged alternatives, retain meaningful security/measurement tests and source references in canonical modules. Use the original PR discussion as a supersession crosswalk.
4. Enable branch protection and required checks/review in GitHub repository settings; workflow policies are not an enforced human-approval substitute.
5. Avoid automatically opening one branch per company or hypothesis without a real reviewer and an acceptance plan. Track future research leads as issues or immutable data entries until implementation is warranted.

**Scientific caution:** This is repository housekeeping. It does not establish GitHub Trending collection permission, the 1,000-project cohort, external human task acceptance, verified adoption or carbon savings.

## Temporary destructive-workflow safety hold — 2026-10-14

**Control change, not a scientific result.** On 2026-10-14 the default branch still exposed the older retirement workflow with a `push` trigger and job-wide `contents: write`. That version deletes GitHub branch refs via REST after a separate read, leaving a time-of-check/time-of-use race. The original [2026-10-13 cleanup run](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38463086727) preserved and retired 59 exact heads and blocked the 60th changed head; those recovery tags are **historical** and are not being changed by this safety hold.

Until the SHA-leased manual-only replacement in [PR #280](https://github.com/MSKazemi/github-trending-1000-study/pull/280) completes **independent qualified security/administrative review**, this workflow is intentionally **manual-only, read-only, and fails with an explicit safety-hold error**. It has no branch-retirement API call, Git credential, ref mutation, `contents: write`, or automatic event trigger. A new small offline regression rejects any future automatic retirement workflow event, and requires explicit confirmation if an execution command is introduced.

**Re-enablement gates:** separately review the exact PR head and full integration diff, verify passing Python 3.10/3.12/3.13/3.14 and research-artifacts CI, require SHA-lease deletion and a confirmed original-SHA archive tag, arrange an independent security review and enforce `main` plus recovery-tag rulesets. Only then replace this hold with a manual, read-only `audit` and separately confirmed `retire` mode. Do not rerun the old 60-item allowlist merely to reach 60/60; its altered branch must remain held pending provenance checks. The recorded October 14 snapshot was 69 refs and 30 open PRs (29 draft), and may change concurrently.

**Practical lesson:** stop a dangerous automatic workflow first, then review and deploy its safe replacement. Passing synthetic CI and fewer branches do not demonstrate human review, valid study sources, software reuse, or environmental savings.
