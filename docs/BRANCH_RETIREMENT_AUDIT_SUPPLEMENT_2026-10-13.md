# Supplemental branch inventory and preservation decisions — 2026-10-13

**Dated GitHub snapshot; no new data collection or scientific signoff.** The [immutable 124-ref inventory](../research-notes/branch-retirement-2026-10-13.json) records the original 123 branches plus the temporary audit branch, exact source commit SHA for every branch, PR linkage and why it was eligible for retirement or held.

The historical JSON now uses the actual `branch-archive/2026-10-13` tag namespace, consistent with the canonical allowlist and the 59 recovery tags observed in the audited run. That namespace is a reference for restoration, not permission to delete any branch.

This snapshot is **not a second deletion allowlist**. The existing, separately merged [canonical 60-branch retirement plan](../ops/branch-retirement/approved-merged-pr-branches-2026-10-13.json), [script](../scripts/retire_merged_branches.py), [recovery procedure](BRANCH_RETIREMENT_AND_NO_LOSS_2026_10_13.md) and GitHub Actions [retirement run 38463086727](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38463086727) take precedence. The run status and final counts must be checked; this inventory does not imply the job succeeded or every deletion is reversible until matching recovery tag refs have been verified.

## Snapshot classification

| Group | Refs | Action |
|---|---:|---|
| Same exact head SHA as an already **merged** PR | 60 | Candidate for SHA-pinned, verified archive-before-retirement only |
| Open draft PR with provisional AI company/news/hiring research | 39 | **Hold**; retain source URLs, version and reporting dates, negative results and limitations, and independently review before canonical publication |
| Closed but unmerged PR | 17 | **Hold**; inspect actual source diff, tests and citations before declaring it superseded |
| Merged PR branch tip changed after merge | 5 | **Hold**; original merge does not certify added commits |
| Unmapped original branch | 1 | **Hold**; establish provenance and whether any tested unique code remains |
| Default main + this temporary audit branch | 2 | **Never** part of the 60-head retirement allowlist |
| **Total at snapshot** | **124** | No broad delete wildcard is permitted |

The five post-merge-moved refs are `ci/research-json-integrity-247`, `ci/restore-canonical-integrity-gate-20261013`, `research/issue6-trending-overlap-audit-20261012`, `research/issue-7-literature-ledger-oct2026` and `research/issue-22-supply-chain-gate-oct2026`. Compare each **tip** to current main at the file level and retain genuinely unique improvements before archiving the historical source SHA.

The unmapped source ref at capture was `fix/canonical-nested-symlink-audit-20261013`. A subsequent file-level inspection found that the current `trending_study.data_integrity` on main already rejects nested symlinks before suffix filtering and includes two equivalent synthetic regressions. Preserve the old ref and review notes until the documented disposition is accepted; do not infer that all its historical materials are recoverable merely because the implementation looks equivalent.

## Verified execution outcome — 2026-10-13

The separately merged canonical [GitHub Actions run 38463086727](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38463086727) finished with a **non-success exit code** because one head had changed. Its log records **59 `retired_with_archive_tag`**, **zero already absent**, and **one `blocked_changed_ref`**. An independent REST comparison of the full 60-item allowlist with current GitHub refs verified **59 deleted branches each have a matching recovery tag pointing to the original expected exact commit SHA, and zero deleted branches lack an archive tag**. This verifies recoverable Git references; it does not certify any source or scientific outcome.

The held branch is `ci/enterprise-pr-qa-gates-issue-240`: the original merged PR #253 tip was `2ee638a04d335ef895c5fd981c1b039ee8188d60`, but the live branch had advanced to `4c840ae69eb01385b6e1dd014fc481dbb2ba8c4c`, also the head of **open draft [PR #272](https://github.com/MSKazemi/github-trending-1000-study/pull/272)**. GitHub compare found 12 subsequent commits with code, tests, documentation and policy work. The retirement program **correctly left that entire branch and its history intact**. Do not reset, force-delete or classify #272 as merged merely because earlier PR #253 merged.

The live branch inventory contained **68 branches** when checked after the retirement run, including new concurrently created work branches (versus 123 at the original baseline). Hence the accurate claim is **59 verified exact-head branch retirements**, not an unconditional final cap or a 60/60 success. The source inventory was not rewritten to hide blocked candidates.

## Practical no-loss branch budget

Follow [issue #273](https://github.com/MSKazemi/github-trending-1000-study/issues/273) to collapse overlapping company-screen draft work into **one canonical, explicitly provisional evidence ledger per company** with original source IDs, dated attribution and unresolved dissent. Keep issue history available, use review branches only for a bounded task, and work toward at most 5–10 genuinely active development branches. Do not mistake fewer branches for independent adoption, lower energy, higher research validity, or permission to scrape source pages.

**Do not use this manifest to force a cleanup job.** The originally proposed alternative octopus-archive/deletion implementation was intentionally not integrated: the already merged canonical implementation uses individual exact-SHA archival tags, which are easier to restore and audit. Unique review findings were retained in this read-only supplemental inventory; duplicate deletion code/workflows were not carried into main.
