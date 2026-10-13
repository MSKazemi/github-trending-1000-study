# Safe branch retirement and research preservation — 2026-10-13

**Status: actionable engineering proposal, not yet executed.** The audit is a dated point-in-time GitHub API snapshot, not a scientific cohort observation or permission to delete unchecked work. Original work remains available by branch and PR until a separately authorized retirement run finishes.

## Why this is necessary

The repository had **123 branches** before this maintenance work began: `main`, 39 open company/news/hiring research PR heads (**all draft**), 60 branch heads matching an already merged PR's exact last reviewed SHA, five merged PR branches with changed post-merge SHAs, 17 closed-but-unmerged PR branches and one branch with no mapped PR. Creating this audit branch temporarily brought the inventory to **124 branches**. These counts will change with concurrent integrations.

The exact evidence snapshot, SHA checks and per-ref hold reasons are retained in [branch-retirement manifest](../research-notes/branch-retirement-2026-10-13.json). Branch history and PR metadata must be audited together; an open draft is NOT an eligible deletion, and a closed PR is NOT proof that its work was merged.

## Phase 1: only the 60 exact merged PR heads

`scripts/retire_merged_branches.py` is a **read-only audit by default**. It locks its target to this exact repository and verifies at execution time:

- Exact, unique branch names and 40-digit recorded branch and merge-commit SHA values; no `main`, `master` or archive namespace.
- No currently open PR points at the branch; GitHub confirms an actually **merged** PR, same recorded head, correct repository and base `main`.
- The branch still points to the same exact recorded commit and GitHub reports it as unprotected.
- GitHub compare confirms that the merged PR's merge commit is an ancestor of the current `main`; unknown or diverged history stops the entire operation.
- Every source SHA is archived **before any deletion**. Three lightweight tags under `archive/branch-retirement-2026-10-13-part-0{1,2,3}` each point to an explicitly archival Git commit. Each commit has the current `main` tree and up to 20 original branch-head commits as parents; **this does not merge these branch changes into main or alter the original evidence**. The script reads back every archive tag, validates its tree and complete ordered parent list, and checks `main` has not changed before retiring anything.
- Immediately before each deletion it rechecks the remote branch/PR/ancestry and verifies that the ref disappeared. It never forces a push and never removes a tag, main or a non-allowlisted ref.

The delete endpoint has no atomic SHA-lease parameter, so a tiny update-versus-delete race remains between the final read and deletion. Do **not** execute while parallel writers are modifying archived branch heads. Preserving their commit ancestry in the archival tags substantially limits accidental loss, but cannot replace the source/PR audit.

## Safe operator procedure

1. Read this page, the exact manifest and all 60 PR references. Confirm no ongoing work or unreviewed post-merge commits and arrange a short pause on pushes to the retiring branches.
2. Review [manual workflow](../.github/workflows/manual-branch-retirement.yml) and its tests. On GitHub choose **Actions → Manual verified merged-branch retirement → Run workflow** on `main`, mode `audit`. It needs the repository's default `GITHUB_TOKEN` for read-only API checks; **any failure means stop and update the snapshot**, not bypass the guard.
3. Only after reviewing the successful live audit, run the same workflow on `main` with mode `retire` and exact confirmation `RETIRE_VERIFIED_MERGED_BRANCHES`. The workflow does not automatically run on PR merges, schedules or branch pushes, and grants write permission only inside this privileged manual job.
4. Review the workflow's exact branch deletion report and **three archive tag refs**. Verify the recorded originals can be restored from the tagged parents using `git cat-file -p` / `git show`. Record the Actions URL, completed UTC time, retired count and any failures in this page or an append-only follow-up. Protect `archive/branch-retirement-*` tag names in a repository ruleset so their ancestry cannot be casually deleted.
5. Enable GitHub's **Automatically delete head branches** option for future merged PRs if your repository policies permit. Require main PR reviews and current-head CI through an administrator-controlled ruleset, not by relying on this cleanup script.

Manual local equivalent for a **read-only** preflight (do not put a token in a shell command or checked-in file):

```bash
GITHUB_TOKEN="$GITHUB_TOKEN" python scripts/retire_merged_branches.py \
  --manifest research-notes/branch-retirement-2026-10-13.json --mode audit
python -m unittest tests.test_branch_retirement -v
```

If a branch moved, was repurposed, gained an open PR, lacks archived ancestors or any API response is incomplete, the run must fail closed. Do not fix the error by resetting the branch, force-merging or changing the manifest SHA to make it pass.

## Phase 2: preserve unfinished scientific and engineering work

**Do not delete the other ~63 branch heads by applying the phase-1 algorithm.** Their recorded categories include 39 *open draft PRs* (company AI intelligence, hiring/news leads), 17 *closed unmerged* proposals, five *post-merge changed* heads and one *unmapped* branch, plus `main` and this temporary working branch. The correct preservation path is:

1. Group reports by the same company/issue, not by PR creation order. Maintain one canonical provisional evidence report per company, with source IDs, historical URLs, source publication/event dates, event schema, corrections, negative/unknown findings, and links to every contributing branch/PR.
2. Require independent source/date/permission and research-method review before promoting preliminary vendor statements into scientific findings. Do not call a CI-green first-pass report a verified seven-month systematic study.
3. For closed-unmerged and changed branches, compare the branch tip to current `main` at the **file/content** level. If materially unique evidence exists, transfer it into a separately reviewed PR before archiving its original SHA.
4. Reduce ongoing write branches toward a few bounded workstreams; archive and close work only after a reviewer has documented complete source/material transfer or intentionally preserved an unreviewed proposal for future reconsideration. Protect open PRs and unverified material from phase-1 deletion.

## Practical lesson for maintainers

**Branches are temporary workspaces, not the research evidence registry.** Keep immutable PR links, commit SHA provenance and a canonical evidence ledger so that repository growth depends on tested reusable components and independently confirmed value—not on accumulating dozens of agent-created branches. Under no circumstances does branch retirement imply that external research evidence, experiment outcomes or environmental benefits have been validated.
