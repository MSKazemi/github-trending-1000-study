# Five company-intelligence PRs: integration and scientific merge review

**Date:** 2026-10-14. **Repository:** MSKazemi/github-trending-1000-study. **Scope:** PRs #228–#232, against `main`. **Assessment:** AI-assisted technical and documentary audit, not independent human factual or methods approval. **Merge disposition:** BLOCKED / remain draft until actual reviewer approval, full source-screen coverage and final-head checks.

## Per-PR review snapshot

| PR | Company | Canonical vendor URL leads after audit | Engineering status | Scientific blockers |
|---|---|---:|---|---|
| #228 | Meta | 6 | Earlier archival CSV URLs preserved; initial exact-head Actions Tests success | Incomplete seven-segment source search, conflicts in release/availability attribution, no independent factual/licensing review |
| #229 | Amazon/AWS | 8 | Earlier archival CSV URLs preserved; initial exact-head Actions Tests success | Incomplete source denominator/independent review; product retirement vs remaining AWS Q offerings must be kept distinct |
| #230 | Replit | 10 (formerly 9) | Preserved original #196 JSON and separate model-routing vendor source as provisional E0; new CI required | Independent check of article/date/65% vendor cost claim, search logs, availability, real results and independent review |
| #231 | Amp Inc. | 5 | Original JSON event lead URLs present in CSV; initial exact-head Actions Tests success | Independent release/access, terms, source logs and claims verification |
| #232 | Qodo | 10 (formerly 9) | Preserved original #198 JSON and vendor opinion as provisional E0; older #213 ledger/event crosswalk retained; new CI required | Source/date and permission/license checks, 10-lead reconciliation, independent review, full screen |

The counts refer **only to distinct source URL leads**, not independent findings, verified adoption, tested releases, companies or complete coverage. CSV screening checked event ID and URL uniqueness, data-field count, date bounds, and absence of lost original ledger URLs for the four branches with an archived CSV. For #231 the original 4-item JSON leads are retained in the proposed 5-row canonical index.

## Preservation actions and status

1. Copy the exact 3-event `014-replit.events.json` from closed-unmerged #196 to `source-archives/014-replit.2026-10-12-first-pass.events.json` in #230. Add its distinct 2026-08-26 model-routing URL as unreviewed `014-E03`. The vendor's 65% cost statement has **not** been replicated or accepted as a research result.
2. Copy the exact 4-event `018-qodo.events.json` from closed-unmerged #198 to `source-archives/018-qodo.2026-10-12-first-pass.events.json` in #232. Add its distinct 2026-06-30 vendor *opinion* source as unreviewed `018-E01`; not evidence that automated independent code review improves outcomes.
3. Existing #232 historical crosswalk separately preserves an older Agentic Toolbox identifier and corrected Qodo 3.0 URL. #271 is already merged on `main` with a broader cross-PR Qodo provenance crosswalk. Do **not** overwrite or double-count it.
4. The original #191, #192, #212, #197 and #213 PRs are closed **unmerged**, so do not call them independently merged scientific results. Their useful documentary material has been incorporated or archived in the five later draft proposals.

## Engineering checks and current limitations

- The earlier five PR heads had successful GitHub Actions `Tests` runs, but those runs must never be attributed to later commits.
- PR #230 and #232 acquired new branch commits on 2026-10-14; inspect the associated final-head Python 3.10/3.12/3.13/3.14 jobs plus `research-artifacts` before any merge. Also check same-head status when any additional fix is made.
- GitHub's mergeability response is changeable or transient: metadata queries returned false for multiple PRs, later `fetch_pr` returned true. Re-query immediately before merging and after each `main` advance.
- No direct local clone/test was possible in this review environment: `git ls-remote` failed because github.com DNS did not resolve. The repo-facing structural checks used the GitHub connector and do not replace running the full checkout.
- No independent human review/approval was observed for any of the five PRs; do not invent or self-approve an independent scientific review. None is promoted out of draft or merged by this audit.

## Outstanding acceptance tasks before merging

- Perform the exact, dated, recorded searches for all **seven calendar-month segments** (April partial, May, June, July, August, September, October partial), including result denominators, screening decisions and excluded URLs.
- Independently check high-impact source titles, dates, availability and page-version changes, and reconcile contradictory claims with time-scoped corrections.
- Freeze/check precise source-code or model artifact tags, licenses, data permissions and independent adverse evidence; in Qodo, the April announced Apache-2.0 transition must not override actual commit-pinned MIT evidence.
- Obtain an **actual qualified human** factual/methodological approval, retaining uncertainty and non-causal framing. CI cannot substitute for independent judgment.
- Confirm all tests and no open review blockers on exact PR head, safe sequential integration to `main`, post-merge workflow results, and that original unique source material is still available. Do not close issues #71/#72/#80/#82/#85 based on provisional source-screen integration alone.

## Practical lessons for other repositories

- Never choose the longest of overlapping AI-generated research PRs as canonical without a URL/ID crosswalk. Explicitly preserve original evidence and missing leads.
- Separate event leads, independent corroboration, and measured user outcomes in schemas and docs. Count URLs as URLs.
- Keep assertions time- and artifact-bound (release vs preview, actual license vs advertised license, offer vs effective cost).
- Couple branch-head CI with independent domain signoff, especially for research, security, licensing and adoption claims.
- Test new provenance guards on deliberately divergent archived/current inputs before enabling them as required CI.


## Updated 2026-10-14 follow-through: 50 candidate leads, no research signoff

This section supersedes the earlier 37/39-record interim count, without erasing that historical snapshot. All five draft branch working CSVs now contain **50 distinct publisher URL candidate leads in aggregate**: #228 Meta **8**, #229 Amazon/AWS **9**, #230 Replit **11**, #231 Amp **9**, #232 Qodo **13**. They are **50 links**, not 50 independently verified functional releases, unique underlying events, external adoption observations, independent companies, validated trials or environmental outcomes.

### Concrete engineering work

- Per-branch seven-period search checkpoints are stored under `research/company-intelligence/2026-04-12_2026-10-12/source-audits/NNN-*.2026-10-14-qa.md` and linked from the relevant working reports. Exact public search strings are logged; the search interface did not provide complete result-hit counts, all screened URLs, excluded URLs or archival bytes. Thus these **do not yet satisfy** the protocol's reproducible full source-search denominators.
- Added **11 uniquely dated publisher-source leads**, including Meta Muse Code beta and disclosed cyber-evaluation issue; AWS opt-in Kiro workflows; Replit opt-in Auto-Protect; Amp staged-to-broad Neo status, multi-repo, diff ordering and PR-feedback listeners; Qodo Findings Page beta, agent guidance opinion and Codex integration. Each lead retains source attribution, explicit availability classification and limitations.
- Preserved the earlier #196 Replit and #198 Qodo unmerged JSON ledgers byte-for-byte in source archives. Qodo's older first-party claim of an Apache-2.0 PR-Agent transition and the separately recorded pinned MIT license must remain distinct. Source archival labels E1 and later provisional E0 are not interchangeable scientific judgments.
- Inspected all five canonical 21-column CSVs: unique source URLs and event IDs, permitted statuses, inclusive research date bounds, and chronological order. No source row was deleted; only new records and stable date sorting were added to working indexes. Previously archived source CSV/JSON remain intact.
- Original owner-authored and AI-assisted statements are **not independent human approvals**. Each PR still needs actual qualified human factual, source-rights and methods review. No source screen or experimental benefit is certified as complete.

### Scope-specific merge decision

**Result: all five are draft / not yet authorized to merge**, despite GitHub reporting them mergeable and automated CI being available. A green unit test verifies structured file behavior, not full scholarly screen recall, independently corroborated deployment/rights or third-party experiment outcomes. Check exact-head jobs again after the last PR content commit. Do not close issues #71, #72, #80, #82 or #85 or mark any completed company study until all acceptance criteria are satisfied.

**Action for another repository:** separate merge policy into (1) reproducible code/provenance checks and (2) independently reviewed scientific interpretations. Keep a unique URL event ledger plus origin and disagreement notes; avoid counting duplicated AI-generated source lists as corroboration. A reader should always see *what was searched*, *what was found*, and *what remains unknown*.
