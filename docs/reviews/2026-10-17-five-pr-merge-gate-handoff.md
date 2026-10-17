# Five-PR merge gate handoff — 2026-10-17

**Scope:** GitHub API read-only check and prioritization of five existing non-draft PRs for [MSKazemi/github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study). This is a dated **AI-assisted technical triage**, **not** a submitted independent GitHub code review, merge authorization by a qualified external reviewer, completed research study, or a claim that five PRs were merged. It follows the [canonical merge gate](../PR_MERGE_QUALITY_GATE_2026_10_13.md).

## Five candidates, inspected exact PR heads

Each candidate reported `mergeable=true`, no open inline review threads, **zero submitted GitHub reviews**, and five completed successful **pull_request** checks on the exact head listed. The checks were: `test (3.10)`, `test (3.12)`, `test (3.13)`, `test (3.14)`, and `research-artifacts`. A successful test suite does not authenticate studies, participant consent, source access, licenses, real measurements, or privacy/security review.

| Review order | PR | Main change and independent reviewer priority | Head SHA at inspection | Completed passing PR Actions run | Gate |
| --- | --- | --- | --- | --- | --- |
| 1 | [#425](https://github.com/MSKazemi/github-trending-1000-study/pull/425) | Offline goldset private-ID/CLI diagnostic hardening; independently inspect complete exception chains, malformed input, allowed result fields and security/privacy implications | `fc21f35a9d51e9ad2f8d9362f26cd9d89a388ecf` | [39055806890](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/39055806890) | **HOLD: no qualified non-author privacy/code review** |
| 2 | [#426](https://github.com/MSKazemi/github-trending-1000-study/pull/426) | Conservative offline news URL dedup and lexical source-host checks; human reviewer must check query selectors, false dedup, provenance and no network-authority claims | `b137d301805418c15d335f30b4eb22bcaf00bc7a` | [38983636487](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38983636487) | **HOLD: no qualified non-author source/privacy review** |
| 3 | [#428](https://github.com/MSKazemi/github-trending-1000-study/pull/428) | Hiring-record source URL and timestamp validation; examine lexical public-host checks, traceback privacy, source rights and no inferred job-fill claims | `43246acd6dc63b8550f1927d07ad0374a6c2ebcb` | [38983852246](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38983852246) | **HOLD: no qualified non-author source/privacy review** |
| 4 | [#429](https://github.com/MSKazemi/github-trending-1000-study/pull/429) | Package evidence URL numeric host and error-chain validation; verify no-auto-install, credentials, license/provenance boundaries and security with independent reviewer | `db8db8077560f8c90a5ddcdd38569999735af5a6` | [38983916869](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38983916869) | **HOLD: no qualified non-author security review** |
| 5 | [#427](https://github.com/MSKazemi/github-trending-1000-study/pull/427) | Dated branch/PR disposition and 20-issue evidence handoff; check against contemporaneous state, historical SHAs and no false scientific/closure assertions | `9fd72ea69d6035ced62521bdc4fe2548ee9ec8fa` | [39056510665](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/39056510665) | **HOLD: no submitted reviewer; self-authored governance handoff explicitly disclaims merge authority** |

The five PRs touch **16 distinct file paths** across their changed-file inventories, with no identical changed path among these five at the initial preflight: #425 (3), #426 (3), #428 (3), #429 (3), #427 (4). That reduces direct file conflicts but does **not** establish semantic compatibility, fully reviewed privacy implications or successful testing of the **combined** merge tree. Other open PRs must still be cross-checked before integration.

## Repository state and review requirements

- Observed `main`: `1e656cfcbceb4995467280b796e77e870c6c5f39`, `protected=false`. Repository rulesets returned `[]`. An open [issue #248](https://github.com/MSKazemi/github-trending-1000-study/issues/248) and draft [PR #302](https://github.com/MSKazemi/github-trending-1000-study/pull/302) contain a proposed enforcement plan, but **no live server enforcement has been installed or verified**.
- All **13** open PRs were checked for submitted review records in this checkpoint; each had **zero**. The selected five each had **zero** inline threads. Missing comments are not human approval.
- No `CODEOWNERS` was found at `.github/CODEOWNERS`, `CODEOWNERS` or `docs/CODEOWNERS`. Do not invent a reviewer identity or request an unknown stranger. A reviewer who is the PR's author or an AI writing about its own changes does **not** satisfy a qualified **independent human** review.
- Neither the repository being unprotected nor an explicit instruction to an AI to “merge ready PRs” replaces the independently approved methodological/privacy/security gates recorded in the canonical policy. Do **not** silently bypass the policy merely because GitHub's merge API permits a merge.
- Exact-head Actions success is necessary, **not sufficient**; green source-format tests do not permit restricted scraping or authenticate source content or license rights.

## Operator handoff: unblock and merge, one at a time

1. Identify an actual independent human maintainer qualified for the relevant scope and request a real GitHub review of the exact complete diff, including synthetic negative tests and source/ethics/security limits. Existing authors, simulated reviewers and AI-generated review checklists cannot self-approve.
2. Obtain explicit approval with a dated GitHub submission; verify no `CHANGES_REQUESTED`, unresolved inline conversations or outstanding missing legal/security/source reviews.
3. Have the administrator install and test source-appropriate `main` and archive-tag protections under issue #248: required current GitHub Actions checks, no self-approval, stale-review invalidation, no force pushes/deletion and scoped bypass policies.
4. Immediately before each merge, **re-fetch** `main` SHA, PR base/head, draft/mergeable status, all review submissions/threads and the successful **pull_request** run for that exact commit. Reconcile any moved base and run updated integration CI. A passing run for the *old* PR head must not certify a merged tree containing new base changes.
5. Use the GitHub pull-request merge endpoint with an exact expected-head SHA lease (`sha`), a reviewed method that preserves meaningful historical research provenance, and no force push. Merge **sequentially**, not in parallel. Stop on any changed head, failed CI, review dismissal or conflict.
6. After every merge, verify the new main commit, every expected file and full **push** CI; document source/rights/methods decisions and rollback strategy. Keep linked research issues open until their original human/evidence acceptance criteria are actually satisfied.
7. If no independent reviewer is available, leave all five PRs open. Recording **zero actual merges** is scientifically and operationally preferable to falsely labeling self-reviewed changes as accepted.

## Practical lessons for your repositories

- A “mergeable” GitHub flag measures conflict compatibility, **not** scientific, privacy or security correctness; require explicit review records.
- Tests must be tied to both the exact PR head and the post-merge combined main tree; do not rely on historical green badges.
- Disjoint changed filenames remove one kind of conflict, not schema or methodological dependency.
- Set enforceable server-side rules so future coding-agent workflows cannot silently bypass well-written merge policies.
- Optimize independently accepted useful changes rather than the raw number of merged PRs or closed research issues.

**Outcome of this checkpoint:** Five candidates technically green; **zero candidates independently reviewed and fully policy-eligible for merge**, hence **zero merges or issue closures authorized from this checkpoint**.
