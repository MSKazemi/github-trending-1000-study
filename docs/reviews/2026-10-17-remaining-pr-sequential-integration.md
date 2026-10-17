# Remaining PR sequential integration checkpoint — 2026-10-17

**Repository:** [MSKazemi/github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study). This is a dated, AI-assisted engineering ledger and **not** an independent human review, real research outcome, credential approval, authenticated licence/security verdict or permission for destructive branch cleanup.

## Exact read-only preflight and explicit merge-policy deviation

At task start, `main` was `8b6816b7c5de944f10866adf9e45aa049a0cb9ff` with five successful post-merge checks, unprotected and with zero repository rulesets. Eight PRs were open: non-draft #417, #418, #298, #293, #290; drafts #432, #431, #302. During the task a concurrent agent opened draft #433 and a separate legal-documentation commit `12d72e6a550aa848174cdd378bb409e9bb489df6` landed on top of the #417 merge. That legal commit changed only `DISCLAIMER.md`. Its full five-job main push CI later passed. Each merge was refreshed against its then-current `main`.

The user previously explicitly directed **not to wait for human review** and requested merging PRs when technically ready. The normal mandatory independent non-author review gate was therefore **openly waived for these individual user-directed offline engineering merges**, never marked completed. This is not a standing amendment to `docs/PR_MERGE_QUALITY_GATE_2026_10_13.md`. Every merged PR used GitHub `merge` (not squash/force push) and an `expected_head_sha` lease. The new integrated `main` is separately checked with Python 3.10, 3.12, 3.13, 3.14 and `research-artifacts` before another merge.

## Verified GitHub merge and test evidence

| Step | PR and narrow deliverable | Exact source head | Actual merge on main | Push CI on exact merge commit |
| --- | --- | --- | --- | --- |
| 1 | [#417](https://github.com/MSKazemi/github-trending-1000-study/pull/417): read-only branch tip/open-PR/full inventory race checks, no deletions | `85f76b0a5a6f7fbb8d3fcf8e367c703d32ea4e8a` | `d0f5625fddbcc3caf3e581a549f494193a028679` | [39058547035](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/39058547035), **5/5 success** |
| 2 | [#418](https://github.com/MSKazemi/github-trending-1000-study/pull/418): bounded self-reported literature screen and new full-traceback privacy regression | `fcd28b373073c1a9ee9fdc164561eee7585c05ea` | `144918c39cb1185996b02aee6bd5c45e7b6ccb6e` | [39059073181](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/39059073181), **5/5 success** |
| 3 | [#298](https://github.com/MSKazemi/github-trending-1000-study/pull/298): offline hiring two-coder agreement instrument, missingness and full-error privacy | `397f76044c62c92eb2427d36660255b7c9198cf0` | `0be5840f4acfba1839e117f1193ddfd47eb801e9` | [39059244870](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/39059244870), **5/5 success** |
| 4 | [#293](https://github.com/MSKazemi/github-trending-1000-study/pull/293): offline pinned crates index / pair review and error privacy; external source listing cross-check | `1f02a5c58fc854c26892122b6697173fb6b95437` | `2cf08feb1d96b625a4e257aea236c868f0a3225c` | [39059428431](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/39059428431): **pending at this record's authoring checkpoint; do not call passing until verified** |
| 5 | [#290](https://github.com/MSKazemi/github-trending-1000-study/pull/290): offline explicit-frame coverage and displayed-page chronological rank proxy, with prior-feature cross-page evidence and traceback guards | **Final head must be captured after this documentation addition** | **Pending** | **Pending** |

All four completed merges were reported successful by GitHub and remained on main at the respective readback. All four exact source heads passed five `pull_request` checks before merge; one post-merge CI job is never borrowed from a different head/base. The fifth result must be recorded separately in PR #290's final discussion after rechecking its exact head and post-merge CI.

## Bounded independent public provenance check for issue #15

The crate-name manifest `research-notes/issue-15-crates-index-bounded-listing-2026-10-14.json` declares index commit `9b349b77adb46425be15e386ef38f31061be3ca9` and two path slices. Fresh read-only calls to the upstream `rust-lang/crates.io-index` Contents API at **that exact commit** compared all `name` / Git blob `sha` pairs:

- `contents/2`: all 725/725 names and SHA values matched, zero omissions/extras
- `contents/3/a`: all 282/282 matched, zero omissions/extras

Together, **1,007/1,007 entries matched** their pinned published manifest within the *two declared slices only*. No crates were installed, fetched as source code or executed. This does **not** authenticate a full-registry representative cohort, any actual GitHub repository crosswalk, release licences, security, 50 human adjudicated task/package pairs, or historical registry consent. The offline CLI deliberately reports externally authenticated human pairs as zero. The step-by-step check and limitations are also recorded in `docs/QUIET_REUSE_REGISTRY_PAIR_INTEGRITY.md`.

## Explicit unchanged research and privileged-workflow blockers

- Issue [#279](https://github.com/MSKazemi/github-trending-1000-study/issues/279) still needs no-loss lineage review/approved immutable recovery; no branches were retired by #417.
- Issue [#7](https://github.com/MSKazemi/github-trending-1000-study/issues/7) still needs complete reproducible database searches, rights verification, actual independent screening and reconciliation. Eleven candidate records are **not** PRISMA evidence.
- Issue [#223](https://github.com/MSKazemi/github-trending-1000-study/issues/223) still needs two independently verified blinded human coders, approved employer source rights and accepted study methods. The candidate 24/9 frame and coder fixtures are not real hiring signals.
- Issue [#15](https://github.com/MSKazemi/github-trending-1000-study/issues/15) still needs 50 independently accepted task-component pairs and valid selection/inference. Matching 1,007 upstream **package names** is not validation of any such pair.
- Issue [#6](https://github.com/MSKazemi/github-trending-1000-study/issues/6) still requires authorized actual Trending captures and an independently frozen chronological holdout. Synthetic ranking proxy scores cannot reveal GitHub's ranking algorithm.
- Drafts #431 (privileged retirement) and #302 (server protection configuration) are **not** implicit permission to delete refs or apply admin rules. Issue [#248](https://github.com/MSKazemi/github-trending-1000-study/issues/248) is still P0: the main branch was not protected and rulesets were empty at this audit. Drafts #432 (human burden) and #433 (newer hiring host checks) also require their own exact-head review/gates. No human enrolment, consent, scientific claim, external installation or admin setting was changed by this PR integration.

## Practical lessons for maintaining other repositories

1. Perform **one SHA-leased PR merge at a time** and verify the combined `main` push tests before proceeding, especially with concurrent agents editing branches.
2. Test complete exception objects and formatted tracebacks: fixed stderr messages still leave private values in chained low-level causes.
3. Cross-check **declared content-addressed evidence against exact version-pinned public upstream data**; label precisely what the check proves and what it cannot.
4. Preserve the full candidate/missingness denominator and distinguish candidate source syntax/identity from actual independent peer review, licence permission or downstream reuse.
5. Never treat a draft PR or a disabled privileged workflow as production approval; install real server-side protection, keep recoverable evidence, and never retire branches based on GitHub status alone.
6. Count independently accepted useful software tasks and measured maintenance burden instead of stars, synthetic research outputs or PR merge volume.

**Checkpoint completion status:** four new merges verified. Fifth PR #290 is pending exact-head and post-merge checks, not silently represented as already integrated.
