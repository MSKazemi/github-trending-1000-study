# Enterprise PR review outcome and no-loss disposition — 2026-10-13

**Snapshot:** live connected GitHub API during this review; the repository is concurrently edited by other workflows. This is a **point-in-time engineering review decision log**, not a scientific result or an assertion that every draft PR has received line-by-line source/fact review. Recheck live heads, merge states, relevant policies and CI before *every* subsequent merge.

**Repository:** [MSKazemi/github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study). **Baseline before this review:** several overlapping CI/evidence proposals on moving `main`. **Observed after engineering integrations:** `main` SHA `8dd51d82c98810a4e3190829b2b030c095c08931`; 39 open PRs, **all 39 Draft**; no non-draft PR left in that snapshot.

## Reviewed and integrated (exact-head checks plus post-merge verification)

| PR and commit | Decision | Verification / preservation |
|---|---|---|
| [#261](https://github.com/MSKazemi/github-trending-1000-study/pull/261), `d6f6cff50bee30450e746084c490d25764c4c715` | **Merged concurrently by another workflow while being examined**; do not claim this review initiated the merge | Earlier candidate diff briefly showed unrelated historical changes; final merged commit contains only canonical research integrity code, its nested-symlink regression and docs. The five **postmerge main** check jobs passed. |
| [#268](https://github.com/MSKazemi/github-trending-1000-study/pull/268), `c565cdaabd31ea765ac0de0168d6fc5a50d04921` | **Merged by this review**, squash with expected head `9772ca8402a706632fb06185be2f4e794fa6ed68` | Only a new *broken nested alias* negative test, preserving the distinct scenario not covered by #261. PR-head and postmerge main checks passed: Python 3.10/3.12/3.13/3.14 and `research-artifacts`. No data or CI workflow touched. |
| [#257](https://github.com/MSKazemi/github-trending-1000-study/pull/257), `8dd51d82c98810a4e3190829b2b030c095c08931` | **Merged by this review**, squash with expected head `91f716c1ad38bc37abd5b1740fb7461e147155a3` | Original PR branch history preserved; current `main` merged non-destructively into the branch, with exactly 2 additive files in final diff. Source code for both existing energy models inspected; synthetic parity tests strengthened for opposite/zero sign, unknown components and unaccepted tasks. Five exact-head and five postmerge main CI jobs passed. **No empirical energy/carbon result claimed.** |

**Verified CI configuration:** [`.github/workflows/ci.yml`](https://github.com/MSKazemi/github-trending-1000-study/blob/main/.github/workflows/ci.yml) compiles source, exercises offline unit tests and CLI entrypoints under Python 3.10/3.12/3.13/3.14 and executes both canonical and supplementary research-artifact integrity checks. The check is a **technical regression gate**, **not** a license/citation/source/participant-approval/causal-validity gate. Immutable action SHA pins and `persist-credentials: false` are retained.

## Superseded without deleting useful material

| PR | Decision and cause | Preservation |
|---|---|---|
| [#267](https://github.com/MSKazemi/github-trending-1000-study/pull/267) | Closed without merge: created to isolate #261's originally oversized branch but conflicted when #261 merged in the meantime | Production symlink code, docs, positive test merged by #261; the additional broken-link negative test ported and merged via #268; prior branch/discussion remain accessible. |
| [#263](https://github.com/MSKazemi/github-trending-1000-study/pull/263) | Closed without merge: obsolete canonical CSV implementation against current main | Current canonical validator already has strict CSV and symlink checks and added budgets. The stale branch expected removed output key `validated_csv_rows` instead of current `csv_data_rows`; would also regress BOM/header-only/file-budget safeguards. Unique historical commentary, tests and commit lineage remain visible. |

No manual branch deletion, force push, raw evidence rewrite, speculative sample backfill or user-data export was performed.

## Active unmerged queue: research collisions

**Exact file-path scan of the 39 open drafts:** 37 company intelligence PRs plus [#59](https://github.com/MSKazemi/github-trending-1000-study/pull/59) news-corpus work and [#225](https://github.com/MSKazemi/github-trending-1000-study/pull/225) employment/hiring intelligence. The table lists **10 pairs (20 PRs)** that add a **same-named Markdown company report** from distinct branches. These are *semantic/content preservation hazards*, even where GitHub reports each individual head mergeable. **Do not merge either member of a pair without first diffing source citations, verified event dates, missingness, features, and disclaimers into a reconciled report.**

| Company report path suffix under `research/company-intelligence/2026-04-12_2026-10-12/` | Conflicting PRs | Additional distinct artifact in one PR |
|---|---|---|
| `005-meta.md` | [#191](https://github.com/MSKazemi/github-trending-1000-study/pull/191) vs [#228](https://github.com/MSKazemi/github-trending-1000-study/pull/228) | #191 has `.events.csv` |
| `006-amazon.md` | [#192](https://github.com/MSKazemi/github-trending-1000-study/pull/192) vs [#229](https://github.com/MSKazemi/github-trending-1000-study/pull/229) | #192 has `.events.csv` |
| `014-replit.md` | [#212](https://github.com/MSKazemi/github-trending-1000-study/pull/212) vs [#230](https://github.com/MSKazemi/github-trending-1000-study/pull/230) | #212 has `.events.csv` |
| `016-amp-inc.md` | [#197](https://github.com/MSKazemi/github-trending-1000-study/pull/197) vs [#231](https://github.com/MSKazemi/github-trending-1000-study/pull/231) | #197 has `.events.json` |
| `018-qodo.md` | [#213](https://github.com/MSKazemi/github-trending-1000-study/pull/213) vs [#232](https://github.com/MSKazemi/github-trending-1000-study/pull/232) | #213 has `.events.csv` |
| `019-tabnine.md` | [#215](https://github.com/MSKazemi/github-trending-1000-study/pull/215) vs [#233](https://github.com/MSKazemi/github-trending-1000-study/pull/233) | #215 has `.events.csv` |
| `020-augment-code.md` | [#200](https://github.com/MSKazemi/github-trending-1000-study/pull/200) vs [#234](https://github.com/MSKazemi/github-trending-1000-study/pull/234) | #200 has `.events.json` |
| `021-factory.md` | [#201](https://github.com/MSKazemi/github-trending-1000-study/pull/201) vs [#236](https://github.com/MSKazemi/github-trending-1000-study/pull/236) | #201 has `.events.json` |
| `023-cline.md` | [#202](https://github.com/MSKazemi/github-trending-1000-study/pull/202) vs [#237](https://github.com/MSKazemi/github-trending-1000-study/pull/237) | #202 has `.events.json` |
| `024-zed-industries.md` | [#203](https://github.com/MSKazemi/github-trending-1000-study/pull/203) vs [#238](https://github.com/MSKazemi/github-trending-1000-study/pull/238) | #203 has `.events.json` |

**Other 17 single-company PRs (noncollision in this snapshot, still Draft):** [#172](https://github.com/MSKazemi/github-trending-1000-study/pull/172), [#173](https://github.com/MSKazemi/github-trending-1000-study/pull/173), [#174](https://github.com/MSKazemi/github-trending-1000-study/pull/174), [#175](https://github.com/MSKazemi/github-trending-1000-study/pull/175), [#176](https://github.com/MSKazemi/github-trending-1000-study/pull/176), [#177](https://github.com/MSKazemi/github-trending-1000-study/pull/177), [#178](https://github.com/MSKazemi/github-trending-1000-study/pull/178), [#179](https://github.com/MSKazemi/github-trending-1000-study/pull/179), [#180](https://github.com/MSKazemi/github-trending-1000-study/pull/180), [#181](https://github.com/MSKazemi/github-trending-1000-study/pull/181), [#193](https://github.com/MSKazemi/github-trending-1000-study/pull/193), [#194](https://github.com/MSKazemi/github-trending-1000-study/pull/194), [#195](https://github.com/MSKazemi/github-trending-1000-study/pull/195), [#204](https://github.com/MSKazemi/github-trending-1000-study/pull/204), [#205](https://github.com/MSKazemi/github-trending-1000-study/pull/205), [#207](https://github.com/MSKazemi/github-trending-1000-study/pull/207), [#209](https://github.com/MSKazemi/github-trending-1000-study/pull/209). **Absence of a path conflict is not source validation or merge permission.**

## Research and governance blockers

1. **All remaining 39 were Draft in the observed inventory**. Neither passing Python tests nor the appearance of a citation proves a six-month systematic search, verified original event date, independent factual reviewer, correct licensing/permissions, or M1–M7 empirical software reuse.
2. **Overlapping research sources:** reconcile primary vs independent URLs, duplicates, any source updates/corrections, event versus publication dates, model/API licenses and explicit zero-result/missing-month logs. Preserve both versions until a reviewed union is committed. A final report must not invent NEWS IDs or imply press events measured downstream software reuse.
3. **Human approval:** research methods, sampling/preregistration, live GitHub Trending access, privacy and material company/security claims require qualified, genuine human approval as specified in protocol/issue. An AI-assisted engineering review cannot impersonate independent scientific adjudication.
4. **Current workflow lacks an independently observed mandatory human-review gate.** The main-branch GitHub API previously returned `protected: false`; this is an incomplete visibility signal (organization-level enforcement may not be fully readable by the integration). A repository administrator should review branch/ruleset protections, require exact-head CI, review threads, signed/verified contribution policy as appropriate, no direct push/force push, and protected `main`.
5. **Project energy accounting is hypothetical until measured:** #257 checks synthetic sign parity, not carbon intensity, full supply-chain impact, upstream cost, rebound or human task equality. For private repositories, never turn GitHub star counters into independently verified adoption.

## Deterministic next-merge procedure

For **each** candidate: fetch live head/base and changed file patches; list all open PRs modifying the same paths and cross-check artifacts; isolate one logical change; examine negative, malformed and permission-risk cases; preserve all distinct sources and valid tests; inspect exact dependency identity and license; demand qualified independent review where methods/sources/rights require it; ensure actual current-head `pull_request` checks (Python 3.10/3.12/3.13/3.14 plus integrity) **all completed successful**; ensure branch is no longer Draft, clean and target main is current; **merge with expected head SHA**, then confirm exact new `main` and full **push-triggered** CI; record and resolve failures before proceeding to the next candidate.

Do not use a single CI screenshot or check on an ancestor SHA to justify a series of batch merges. Where two research PRs touch the same path, use a dedicated reconciliation PR against current main with a lossless event/claim/source table, and link both parents rather than force-merging either incomplete report.

## Practical lessons for the maintainer's other repositories

- One stable, tested public contract is usually safer than two overlapping frameworks; reuse a canonical validator and import missing test ideas instead of reinventing it.
- Make PRs small and make source/evidence provenance explicit, including unknowns and negative tests. Record exact review SHA and postmerge CI SHA.
- Pin code/tool versions and real package licenses; model claims, URLs and self-written review checklists do not authorize security/privacy or scientific conclusions.
- Track successful external **task acceptance and downstream reuse** separately from attention, generated code volume and repository count; capture full human/operational costs before any green-computing claim.
