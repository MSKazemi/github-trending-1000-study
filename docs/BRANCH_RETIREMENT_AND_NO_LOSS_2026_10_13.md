# Verified merged-branch retirement — 2026-10-13

**State at initial review:** 123 branches, 39 open draft PRs, 65 merged PRs; 60 exact head-to-merged-PR branch matches are eligible for *independent revalidation*. The branch list and draft status are time-bound observations, not research findings.

## Strict no-loss retirement

The [committed allowlist](../ops/branch-retirement/approved-merged-pr-branches-2026-10-13.json) pins **each of the 60 branches** to a GitHub PR number, exact last-reviewed head SHA and merged commit SHA. It is not a wildcard or retrospective inference from a branch name. The source main SHA for this inventory is `6339775d73886b24f746139cdf55a34384f88c33`.

The [offline standard-library retirement implementation](../scripts/retire_merged_branches.py) and [negative tests](../tests/test_retire_merged_branches.py) fail closed unless each GitHub branch remains unprotected and unchanged, the PR is actually merged to `main`, and **no open PR** references the branch. Before removing the branch ref, a recovery tag `refs/tags/branch-archive/2026-10-13/<original-branch-name>` must exist and point to the exact original commit. The script verifies this recovery ref and rechecks the branch and open PR state immediately before deleting. Existing tags with different SHAs block deletion. Partial failures remain logged and do **not** authorize further deletions outside the plan. No study dataset or source document is rewritten.

The original integration ([PR #275](https://github.com/MSKazemi/github-trending-1000-study/pull/275)) introduced a **push-triggered one-time cleanup**; that historical run must be audited independently, not presumed successful or race-free. The revised [GitHub Actions workflow](../.github/workflows/retire-verified-branches.yml) is **manual-dispatch only**: `audit` (default, read-only `contents: read`) checks live GitHub state; `retire` requires the exact confirmation `RETIRE_VERIFIED_MERGED_BRANCHES` and grants scoped `contents: write`. Neither normal pushes nor merging a PR may automatically retire a branch. The destructive CLI also requires `--confirm RETIRE_VERIFIED_MERGED_BRANCHES`. **An additional fail-closed deployment gate** requires an administrator to set the repository Actions variable `BRANCH_RETIREMENT_APPROVED` to the exact string `true`; when unset (the default), the write-capable job is skipped even if someone supplies the confirmation phrase. Before setting the variable, an actual qualified independent reviewer must record the approved PR head, SHA-lease threat model, main/archive-tag rulesets, restore verification, and an authorized maintenance window. Merely setting the variable is not proof those reviews occurred. Keep it unset until all conditions are demonstrated; reset it after a bounded retirement operation.

**Race-safety improvement:** a second GET before GitHub REST DELETE does **not** prevent another contributor pushing between those calls. Instead, the revised script uses an authenticated `git push --force-with-lease=refs/heads/<branch>:<expected_sha> ... :refs/heads/<branch>` for Git's server-side atomic expected-SHA comparison. A concurrent update or restricted deletion rejects the push; the script never retries with a new SHA or force-removes the altered head. It verifies the branch has disappeared after a successful lease. Immediately before the lease it also rechecks the exact archive tag SHA and open-PR count; if a tag is deleted/repointed or a PR appears during preflight, the operation fails without deleting the branch. An open PR can still appear after the final PR query without changing the branch SHA; this is not an atomic GitHub PR/ref transaction. Operators must pause creation of new PRs against the selected heads during the explicitly approved retirement window, and must enforce recovery-tag protection separately. Access tokens are sent through an ephemeral Git configuration environment variable, never embedded in the remote URL or command line. 

A current `main` ancestry check requires each verified PR merge commit to be reachable from `main`. Absent branches are treated as successfully retired **only** if their original SHA is still recoverable through the exact archive tag. A list of 100 open PR results is treated as incomplete and blocks destructive action, rather than assuming there are no other referencing PRs. Archive-tag governance still requires repository administrator rules.

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


## Read-only audit and controlled recovery

A live `audit` run also detects an archive tag that already points at a *different* commit and reports `blocked_archive_tag_conflict` without modifying any refs. A missing tag before first approved retirement is expected; it is created and verified only in the separately authorized `retire` phase. This does not replace independent source/method review or administrator protection of recovery tags.

1. Review the [no-loss branch allowlist](../ops/branch-retirement/approved-merged-pr-branches-2026-10-13.json), current base/head SHAs, and full original PR discussions. Run GitHub Actions **Retire verified merged branches** on `main` in `audit` mode. The audit does no writes; treat any blocked result as a reason to investigate, not authorization to edit expected SHAs.
2. Before any separately authorized `retire` execution, confirm the 2026-10-13 original cleanup run has fully finished, original archive tags exist and remain reachable, no active author is writing to target branches, and tag-protection/branch-protection requirements have been reviewed. Do not rerun an older unreviewed workflow implementation.
3. If approved, dispatch `retire` manually with exact confirmation. Check the resulting GitHub Actions log, statuses, original SHA-to-tag mapping, and the complete post-run branch list. A failed lease means **retain and reclassify**, not bypass.
4. Preserve open Draft PRs and closed-unmerged or changed-after-merge heads until source-level evidence, distinct tests, protocol limits, and independent approvals are reconciled. GitHub branch cleanup is an engineering operation, not validated scientific collection or sustainable-computing evidence.

## PR #284 safety-hold provenance retained during reconciliation

The following historical section records the **protective state of `main` introduced in PR #284 on 2026-10-14**. PR #280 proposes to replace the intentionally failing read-only hold with a **manual read-only audit and a separate SHA-leased retire job** only after qualified independent security review and admin ruleset enforcement. If PR #280 is eventually approved and merged, interpret the retained section as an audit record, not as a claim the intentionally failing hold remains active.

## Temporary destructive-workflow safety hold — 2026-10-14

**Control change, not a scientific result.** On 2026-10-14 the default branch still exposed the older retirement workflow with a `push` trigger and job-wide `contents: write`. That version deletes GitHub branch refs via REST after a separate read, leaving a time-of-check/time-of-use race. The original [2026-10-13 cleanup run](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38463086727) preserved and retired 59 exact heads and blocked the 60th changed head; those recovery tags are **historical** and are not being changed by this safety hold.

Until the SHA-leased manual-only replacement in [PR #280](https://github.com/MSKazemi/github-trending-1000-study/pull/280) completes **independent qualified security/administrative review**, this workflow is intentionally **manual-only, read-only, and fails with an explicit safety-hold error**. It has no branch-retirement API call, Git credential, ref mutation, `contents: write`, or automatic event trigger. A new small offline regression rejects any future automatic retirement workflow event, and requires explicit confirmation if an execution command is introduced.

**Re-enablement gates:** separately review the exact PR head and full integration diff, verify passing Python 3.10/3.12/3.13/3.14 and research-artifacts CI, require SHA-lease deletion and a confirmed original-SHA archive tag, arrange an independent security review and enforce `main` plus recovery-tag rulesets. Only then replace this hold with a manual, read-only `audit` and separately confirmed `retire` mode. Do not rerun the old 60-item allowlist merely to reach 60/60; its altered branch must remain held pending provenance checks. The recorded October 14 snapshot was 69 refs and 30 open PRs (29 draft), and may change concurrently.

**Practical lesson:** stop a dangerous automatic workflow first, then review and deploy its safe replacement. Passing synthetic CI and fewer branches do not demonstrate human review, valid study sources, software reuse, or environmental savings.

## 2026-10-14 integration security gate: read-only path only

The upgraded `git push --force-with-lease` method and its adversarial tests are integrated **as dormant code**. The workflow can be dispatched in `audit` mode with `contents: read`, but the `retire` job has an explicit unconditional `false && ...` job condition. This condition is a deliberate hard stop: **even an administrator setting `BRANCH_RETIREMENT_APPROVED=true` and entering the confirmation cannot trigger branch deletion using this workflow**. The privileged job is not approved or executable at this stage.

Enabling the job requires **another focused PR** that removes the literal `false`, with fresh exact-head tests, genuine qualified independent security review, administrator-enforced `main` branch rules and protected immutable recovery tags. A fresh SHA-pinned allowed-list and independent preflight must then be reviewed separately. No current GitHub interface used in this conversation provides those administrator protections or proof of independent approval. Never reinterpret this engineering merge as permission to retire the six changed branches, 27 closed-unmerged branches, 13 open PRs or the 23 unchanged merged-head candidates in [the October 14 snapshot](BRANCH_RECONCILIATION_2026_10_14.md).

**Scientific boundary:** these security controls and branch counts say nothing about whether AI coding increased independently verified downstream software reuse or reduced lifecycle kWh/CO2e.
