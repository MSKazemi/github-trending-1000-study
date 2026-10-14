# Ten-issue enterprise quality and branch-evidence checkpoint — 2026-10-14

**Scope and provenance:** This is a *read-only GitHub repository governance audit*, linked to canonical issue [#240](https://github.com/MSKazemi/github-trending-1000-study/issues/240), not a study finding, approval certificate, authorization to scrape, or permission to merge/delete unreviewed work. GitHub API checks were performed on 2026-10-14; values below are a **moving snapshot**, not a long-term census.

## Observed, reproducible baseline

| Check | Observed evidence | Interpretation |
|---|---|---|
| Default branch | `main` at `1a9464f030572968d1590c268dc60c3e9b57e6a7` (commit timestamp 2026-10-14 09:34:17 UTC) | Exact inspected revision only |
| Post-push workflow | [Tests run 38543322932](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38543322932) completed **success** for that revision | Five jobs all succeeded: `test (3.10)`, `test (3.12)`, `test (3.13)`, `test (3.14)`, and `research-artifacts` |
| Existing CI contract | [CI workflow](../.github/workflows/ci.yml) | Pinned official checkout/setup-python SHAs, `ubuntu-24.04`, `contents: read`, Python compilation, offline unit tests and two separate artifact validators |
| Server-side `main` enforcement | GitHub `GET /branches/main`: `protected=false`; `GET /rulesets`: `[]` | **P0 open**: successful jobs are not required by an enforceable branch rule |
| Branch inventory | `GET /branches?per_page=100&page=1`: **70** refs | A time-bounded list; old histories are not proven redundant |
| Open PRs | `GET /pulls?state=open&per_page=100&page=1`: **12** (11 drafts, one non-draft) | Drafts must not be promoted solely because CI is green |
| Archive-tag refs | `GET /git/refs/tags/branch-archive/2026-10-13`: **59** | Ref existence is not proof tags are protected/immutable or each SHA was independently validated in this checkpoint |
| Safety-change PR | [#280](https://github.com/MSKazemi/github-trending-1000-study/pull/280) at `6423e85d6265db80a528dad63b853d2d14f6b900` | [Run 38511397655](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38511397655) has five successful jobs, **but qualified security/admin approval is not recorded** |

**Status follow-up, 2026-10-14:** The ten issues were selected while they were open. A later live issue-status check found **#169, #242 and #254 closed**, while the other seven remain open. Those closures reflect technical consolidation or deduplication; they do **not** establish independent scientific approval or enforced GitHub branch protection. The branch/PR counts and revision SHAs above remain the original observation, not an automatically refreshed dashboard.\n\nThe baseline and audit runbook are in [the canonical merge-quality gate](PR_MERGE_QUALITY_GATE_2026_10_13.md). The current retirement workflow on `main` is a **manual-only read-only safety hold**; it must remain so until a separately reviewed SHA-leased replacement is allowed. The historical [59-retirement evidence](BRANCH_RETIREMENT_AUDIT_SUPPLEMENT_2026-10-13.md) is a dated prior run and must not be mistaken for new retirements.

## Ten tracked issues checked and bounded dispositions

| Issue | Verified current engineering state | Remaining obligation and proposed tracker |
|---|---|---|
| [#169](https://github.com/MSKazemi/github-trending-1000-study/issues/169) — one page-audit CLI | Canonical `trending_study.page_audit` supports optional distinct C adjudication, a derived Markdown report, and offline negative tests. No competing CLI was added. | Technical consolidation was subsequently **closed**; **#2** still needs lawful real captures, actual independent adjudicators and signed scientific review |
| [#240](https://github.com/MSKazemi/github-trending-1000-study/issues/240) — canonical PR quality | Python 3.10/3.12/3.13/3.14, syntax, JSON/JSONL/CSV checks, a PR template, provenance review policy and main CI now exist. | Remain canonical for new quality gaps, comparison against latest `main`, preserved overlapping evidence, and explicit human technical/scientific approvals |
| [#242](https://github.com/MSKazemi/github-trending-1000-study/issues/242) — merge QA | Compileall, template, checklist and dated merge audit already exist. | Subsequently **closed** as technically integrated / tracked under #240; do **not** assert human review was granted retroactively |
| [#244](https://github.com/MSKazemi/github-trending-1000-study/issues/244) — tracked-artifact QA | Both existing artifact validators plus compileall and negative tests run in CI. | **Coverage distinction remains:** this is bounded project-directory coverage, not independent proof that *every* possible tracked `.py` or `.json` anywhere in a new PR was inspected. Resolve through one reviewed canonical extension, not another competing CLI |
| [#248](https://github.com/MSKazemi/github-trending-1000-study/issues/248) — branch rules | Workflow jobs already succeed; issue body preserves the exact negative-enforcement criteria from #254. | **P0 owner/admin action:** require PR, qualified non-self review, fresh merge-result checks, no direct pushes/force/delete, protected recovery tags and observed failing/insufficient-review/stale-PR rejection |
| [#254](https://github.com/MSKazemi/github-trending-1000-study/issues/254) — parallel branch rules | Its unique strict acceptance tests are already copied into #248. | Subsequently **closed as duplicate** of #248, not as protection implemented |
| [#273](https://github.com/MSKazemi/github-trending-1000-study/issues/273) — historical consolidation | 59 exact-head retirement outcomes with archive tags are documented; no claim of 60/60 success. | Draft source crosswalk and held branches remain #279; retirement security and SHA leases remain #277 |
| [#276](https://github.com/MSKazemi/github-trending-1000-study/issues/276) — SHA-pinned inventory | Existing `scripts/branch_lifecycle_audit.py`, offline tests and [checkpoint](BRANCH_CONSOLIDATION_CHECKPOINT_2026_10_13.md) provide dated read-only classification; active branches still exceed goal. | Treat as phase tracker under #279/#277, not as proof that all 70 present refs can be deleted |
| [#277](https://github.com/MSKazemi/github-trending-1000-study/issues/277) — safe deletion | #280 implements manual dispatch + SHA-leased Git deletion proposal and offline adversarial tests; five head jobs passed at checkpoint. | **DO NOT execute or merge solely from CI**: qualified independent security review, current-base review, `main`/archive tag enforcement, manual preflight and verified recovery are outstanding |
| [#279](https://github.com/MSKazemi/github-trending-1000-study/issues/279) — remaining unique source work | At this snapshot, 11 of 12 PRs are drafts; multiple existing company-intelligence branches overlap. | Preserve each unique URL, dated claim, correction, null result, code/test and origin SHA in accepted crosswalks *before* any PR closure or branch retirement |

**Duplicate/closure policy:** #169, #242 and #254 have been closed since the initial audit. Closing a tracker as `duplicate` means its requirements are retained in named canonical issues. It never means the unmet branch/security/scientific gates have passed. In particular, do not silently close #277, #248 or #279.

## Operator actions before claiming enterprise merge control

1. In GitHub **Settings → Rules → Rulesets**, an authorized repository administrator must protect `main` with PR-only integration, independent non-self approval (including stale-review invalidation), resolved conversations, no force/deletion and required checks for **all five exact current job names**. Choose up-to-date merge results or a supported merge queue; re-evaluate the named checks if the workflow changes.
2. Configure protection for `refs/tags/branch-archive/**` against deletion/force updates. Document genuine owner privileges and a logged, time-bounded break-glass procedure. A repository Markdown file does not enforce either rule.
3. In authorized throwaway PRs, independently **observe** rejection of a failing check, missing independent review, stale success after head/base changes, and attempted force/delete. Save rule IDs, test PRs and outcomes. No synthetic checkboxes count as server enforcement.
4. Have a qualified human review the entire #280 diff, exact current head and security token transport. If it passes, run a fresh SHA-pinned read-only preflight before separately confirming *each* proposed deletion. Avoid rewriting an old plan's expected SHA to fit a newly moved branch.
5. Consolidate duplicate provisional company drafts only after a source-by-source, date-by-date no-loss crosswalk; public company claims are not independently confirmed product releases, downstream reuse, human productivity or measured energy savings.

## Practical repository lessons

- **Enforce rather than request quality:** maintainers should test server-side rejected merges, not infer enforcement from green CI or a contributor policy.
- **Reuse reviewed modules, preserve negative tests:** a second JSON parser or page-QA CLI expands risk unless independent task acceptance supports a change.
- **Archive before ref cleanup:** keep immutable original commit refs, track unresolved source evidence and recheck exact SHA leases at destructive execution.
- **Measure software value with independent tasks:** accepted user outcomes, downstream reuse with license/security checks, maintainer costs and measured lifecycle boundaries; not stars, PR counts, branch counts or guessed CO₂.
- **Keep unknown as unknown:** the 1,000-repository cohort, real-page parser validation, consented human evaluations and environmental effects are not established by this checkpoint.
