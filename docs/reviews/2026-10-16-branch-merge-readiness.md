# Open-branch merge checkpoint — 2026-10-16

**Scope:** Read-only review of branch/PR merge eligibility for [issue #240](https://github.com/MSKazemi/github-trending-1000-study/issues/240), plus this dated checkpoint. This is **not** source verification, a scientific approval, human review, a green-light to delete branches, or evidence that a research cohort exists. All snapshots can change concurrently. Substantial AI assistance was used to gather and write this checkpoint.

## Authoritative safeguards

Follow [the canonical merge quality gate](../PR_MERGE_QUALITY_GATE_2026_10_13.md) and [repository agent instructions](../../AGENTS.md). A full actual diff, no-loss comparison, independent qualified review when applicable, exact-head **pull_request** CI and post-merge **push** CI are separate gates. Do not merge a draft or interpret Python unit tests as research/source authentication. Expected-head merges must be rechecked against the current base.

## Observed GitHub state (point-in-time, 2026-10-16)

- At readback, `main` was `b87a6a76f51a40d4122e04eba9a3f90ee7ef9a4b`; its [push workflow 38867087553](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38867087553) completed successfully. An earlier pass during this review saw the same base.
- `GET /branches/main` reported `protected: false`; `GET /rulesets` returned `[]`. The repository is **not server-enforcing** the documented merge requirements.
- Open PRs at the inspected snapshot: **four**, of which **one draft** (#302). A branch search initially returned **92 refs** and a later readback, independently confirmed by `GET /branches?per_page=100&page=1`, returned **40** before this checkpoint branch was created. These are two observations, **not** evidence of the cause, intent, backup, or correctness of any intervening ref change. This review performed **no branch deletion**. Recheck and reconcile branch-retirement evidence before any destructive action.
- Both submitted review lists and inline review-thread lists for PRs #290, #293, #298 and #302 were empty when checked; this does **not** authenticate any independent review outside GitHub.

## Pull-request head and check matrix

| PR | Observed head SHA | Exact-head pull_request CI | Technical integration | Blocking decision |
|---|---|---|---|---|
| [#290](https://github.com/MSKazemi/github-trending-1000-study/pull/290), issue #6 | `1417ceeb4d9b296ea09605fa7e2a49d44392a260` | [38867449051](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38867449051), all five jobs successful | At this snapshot ahead of `main` with zero commits behind; GitHub reported mergeable | Qualified **independent methodological** signoff on the proposed coverage denominator/rank proxy, chronology and holdout remains unrecorded; the PR has an explicit merge hold. Do not infer permission to capture GitHub Trending. |
| [#293](https://github.com/MSKazemi/github-trending-1000-study/pull/293), issue #15 | `2cd3af391414e259169d485de7a682f7b90ae99f` | [38867341573](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38867341573), all five successful | Ahead of `main`, zero behind; mergeable | Registry-source rights/coverage, true independent package-to-task judgment and qualified methods review remain pending. A pinned index slice and synthetic tests are not independently certified reuse evidence. |
| [#298](https://github.com/MSKazemi/github-trending-1000-study/pull/298), issue #223 | `e539566b156e73591c52f41f3b07702c31a7b648` | [38867404414](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38867404414), all five successful | Ahead of `main`, zero behind; mergeable | Human coder independence, blind inter-rater review, consent/rights and qualified methods signoff are unverified. The prospective agreement frame and fictional labels do not complete the pilot. |
| [#302](https://github.com/MSKazemi/github-trending-1000-study/pull/302), issue #248 | `1cdf9e2d9b03b7cfaed676dab2917394422d700e` | [38768396016](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38768396016), all five successful on that head | Draft, older base (117 commits behind at comparison); GitHub reported mergeable in a later status read | Keep draft: actual admin application of rulesets failed with integration HTTP 403; genuine security/admin review, current-main preflight and server-side negative enforcement checks are not completed. Do not claim protection exists. |

All five checks refer to `test (3.10)`, `test (3.12)`, `test (3.13)`, `test (3.14)` and `research-artifacts`. The table is a **technical-status snapshot**, not an independently line-by-line-reviewed or scientifically approved release. CI after the recent `main` integrations is particularly valuable but does not replace required human gates.

## Branch-only no-loss notes

- We compared **30 non-company named branch refs** with `main` at separate points in the review, including the active PR heads and older CI/fix/quality branches. A nonzero `ahead_by` for an old branch does **not** prove novel work: squash merges and divergent ancestry can leave commits ahead even when a file is already present on `main`. Check file contents and provenance before creating replacement PRs.
- On the historical `ci/enterprise-pr-qa-gates-issue-240` branch, `docs/BRANCH_RECONCILIATION_2026_10_14.md`, `docs/TEN_ISSUE_QUALITY_AND_BRANCH_CHECKPOINT_2026_10_14.md`, `ops/branch-retirement/review-only-2026-10-14.json` and `tests/test_branch_reconciliation_snapshot.py` **all already exist on main**. This verifies presence, **not bytewise equivalence**. Do not resurrect the old branch wholesale or overwrite newer safeguards.
- `research/issue-100-github-changelog-ledger-20261016` compared as one ahead/one behind in this review, while the current `main` already includes PR #414's GitHub screen. That branch needs a source-line/content comparison, not an automatic merge. It may have changed or disappeared since the comparison.
- Remaining company/legacy branches were **not** independently source-audited in full. No mass branch merge, conflict override, forced update, branch deletion or blanket claims of supersession are authorized here.

## Next release steps and decisions

1. For #290, #293 and #298: obtain dated, issue-relevant independent qualified review; resolve factual/method objections and document source/ethics state. If review causes a revision, rerun all checks on the **new** head.
2. For #302: retain draft until approved administrator credentials and server enforcement can be verified through readback plus deliberate negative tests; refresh the stale base and admin runbook state. Never put tokens in public files.
3. Before any merge, inspect the **complete current diff**, no-loss dependencies, comments, live mergeability, head SHA, current base and five exact-head CI jobs. Reject stale or uncertain status.
4. Merge with an `expected_head_sha` only after **all applicable gates** are satisfied; confirm `main` file readback and successful push-triggered CI. Preserve original research artifacts and report unresolved empirical limitations.

## Practical repository-maintainer lessons

- **Do not use merge count as a quality KPI.** A red human-methods gate remains red even when five test jobs are green.
- **Compare file contents, not only ancestry.** Old squash-merged branches can report commits ahead yet contain previously integrated work.
- **Keep research truth labels separate from engineering status.** Synthetic frame validation cannot establish authentic sources, reviewers, rights, consent, or effect sizes.
- **Enforce decisions server-side.** Documented merge rules alone will not prevent unsafe merges while `main` is unprotected.
- **Keep timestamped, non-destructive audit checkpoints.** Concurrent branch-list changes require fresh API verification and no-loss readback; do not infer causality from two snapshots.

**Disposition for this checkpoint:** The existing four PRs remain intentionally unmerged under their recorded gates. The checkpoint itself is documentation-only, makes no protocol/method change, does not run a capture, and can be separately reviewed and merged when its exact-head CI is green.
