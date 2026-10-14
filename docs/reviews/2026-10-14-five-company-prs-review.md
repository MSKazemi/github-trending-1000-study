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
