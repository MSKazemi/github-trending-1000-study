# Branch-audit tracker consolidation — 2026-10-15

**Disposition:** read-only evidence and issue de-duplication, **not** completed branch cleanup. Related #273, #276, canonical #277 (safe retirement), #279 (no-loss source reconciliation), #248 (administrator-enforced protection). This file is a proposed addition on draft PR #300; it is not a human approval.

## Fresh GitHub API snapshot (observed 2026-10-15, exact UTC not captured)

- `GET /repos/MSKazemi/github-trending-1000-study/branches?per_page=100&page=1`: **97** rows; page 2 **0**.
- `GET /repos/MSKazemi/github-trending-1000-study/pulls?state=open&per_page=100&page=1`: **23** open PR rows; page 2 **0**. The returned PRs included **11 drafts** and **12 non-drafts**, none made merge-eligible by this inventory.
- `GET /repos/MSKazemi/github-trending-1000-study/branches/main`: main SHA **`b6ece720220297e78f47720beadd8947638dfaac`**, `protected=false`; `GET /repos/MSKazemi/github-trending-1000-study/rulesets` returned **`[]`**. A read-only response is **not** an attempt to configure rules.
- Branch/PR counts can change concurrently; these are **not** proof of no-loss classification, authorization to retire a ref, or comparability of differing historical date snapshots. **No remote branches were deleted or PRs merged** by this consolidation.

### #276: verified preservation of the distinct audit implementation on main

The historical branch `chore/276-branch-lifecycle-audit` remains available at inspected ref SHA `0a573825c1a100964f2ee653609c48fcd80e5f02`. Fetching its files and the current main versions directly by repository path gave **identical full contents and Git blob SHA**:

| Source from #276 | Exact blob SHA on the historical branch AND main |
|---|---|
| `docs/BRANCH_LIFECYCLE_AUDIT_2026-10-13.md` | `650d25cade42a2501934846fc351c4c52dd57bab` |
| `scripts/branch_lifecycle_audit.py` | `68af96750f5a2e76abb69987bf57a3531a8e0e25` |
| `tests/test_branch_lifecycle_audit.py` | `fcbfef397c5d6c504c5298c67477999c77fd4aae` |

The old branch's **diverged Git ancestry is not evidence that these files were lost**: compare uses the branch merge base, not a direct equality test against main's current blobs. Existing read-only inventory, pagination, ancestry and base-movement tests are preserved. Neither the script nor these checks authorize deleting branches. No fresh live run of the script itself was performed in this checkpoint.

### #273: historical audit and original evidence preserved

The older `chore/safe-merged-branch-retirement-20261013` still contains its historical supplementary audit and `research-notes/branch-retirement-2026-10-13.json`. Compared with `main`:

- The JSON has the **same 60 candidate entries, held entries, total 124 historical branch records and all other fields**. The **only changed JSON field** is `archive_tag_prefix`, corrected on main from `archive/branch-retirement-2026-10-13` to the actually used `branch-archive/2026-10-13` recovery-tag namespace. Do not restore the stale value or use this retrospective artifact as an execution allowlist.
- Main's `docs/BRANCH_RETIREMENT_AUDIT_SUPPLEMENT_2026-10-13.md` contains the historical report with an added correction explicitly explaining the tag namespace; its old and corrected versions remain available in Git. The older supplement reports **59 archived/recovered retirements** and **one blocked changed head** for the 2026-10-13 authorized run; this checkpoint did not re-execute or independently re-verify all those archive tags.
- The 2026-10-13 counts (123/124), 2026-10-14 counts (~70) and fresh 2026-10-15 count (97) are **distinct snapshots**, not contradictory repeated measures with a fixed cohort.

## Canonical home for every unfinished acceptance gate

| Original issue | Distinct requirement | Surviving tracker / current state |
|---|---|---|
| #276 | Authenticated, paginated, SHA-aware read-only branch/PR inventory; negative tests; moving base refusal | Already implemented by byte-identical code/tests/docs on main; any fixes and richer per-ref classifications tracked in **#279** |
| #276 | Inspect ahead/behind, open PRs, protected flags; keep unique code, historical evidence, per-branch disposition | **#279**, work remains open; no mass deletions inferred from counts |
| #276 | Archive-before-delete exact-SHA lease, restore proof, compare-and-delete execution | **#277**, security/administrator approval and enforcement pending |
| #273 | Preserve 39 former draft/company streams, collisions, source chronology and dissent | **#279**; open PR #300 proposes five-company archive/crosswalk, human source verification still pending |
| #273 | Classify 17 closed-unmerged, five post-merge changed heads and unmapped branch; preserve original SHA and recovery routes | **#279** (classification) and **#277** (safe retirement), incomplete |
| #273 | Verify before/after inventories, exact archive tags, retirement run/rollback and retained CI | **#277** (safe execution evidence) and **#279** (branch budget/outcome ledger), pending current live audit |
| #273 and #276 | Protect main and archive tags, qualified review and recovery tests before mutation | **#248** (main ruleset), **#277** (archive-tag/deletion policy) and **#279** (no-loss review), still open |

**Issue-resolution rule:** mark #273 and #276 `closed / duplicate` only after retaining all requirements in the canonical issues. Such closure is **administrative consolidation, not completion of the described cleanup**. Do not close #277, #279 or #248 until their own acceptance and independent human/admin gates are met.

## Practical maintainer lessons

1. Compare *actual current blob bytes and content hashes*, not only `git compare` ahead/behind, when asking if a divergence lost code.
2. A tagged historical source is not a deletion permit; use verified immutable recovery refs and server-enforced checks before SHA-leased removal.
3. Close duplicate issue trackers to reduce ambiguous responsibility, **never** to improve the apparent completion rate. Report real branches, PRs, reviewed integrations and missing evidence separately.
