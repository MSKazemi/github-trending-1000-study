# Sourcegraph (015) — source QC of existing ledger rows, 2026-10-16

> **Provisional source-lead screen (upgraded 2026-10-16):** this QC note, the [report](015-sourcegraph.md), the [event ledger](015-sourcegraph.events.csv) and the [search log](015-sourcegraph.search-log.md) are **provisional, AI-assisted documentary source leads**. They are **unreviewed by a qualified human**; factual/link, source-access/rights and methods review pending. Merging is not scientific or security sign-off; issue [#81](https://github.com/MSKazemi/github-trending-1000-study/issues/81) was closed on maintainer instruction (2026-10-16) with these review gates still open — reopen it if review finds a defect.

**Method.** On 2026-10-16 every existing `source_url` in [015-sourcegraph.events.csv](015-sourcegraph.events.csv) was fetched once over public HTTPS (plain `curl`, generic User-Agent with no personal identifier, no login, no cookies). The displayed on-page date and body text were read and compared with `published_utc`, `claim_summary`, `availability` and `status`. HTTP 200 means only that public text was returned on that day; no byte-hash archive was stored and the pages are mutable. This is an **AI-performed** check, not independent human verification.

## Existing rows (9) — outcome

| event_id | URL | Reachable (2026-10-16) | Displayed date == `published_utc`? | Claim / status supported? | Action |
|---|---|---|---|---|---|
| CI2026-015-001 | [2026-04-27](https://sourcegraph.com/changelog/2026-04-27) | yes (HTTP 200) | yes — "April 27, 2026" | yes — "Quantitative answers in Deep Search" plus a sandboxed Lua "evaluator" tool; roll-up page has no "Included in" version line | none |
| CI2026-015-002 | [new-compare-page](https://sourcegraph.com/changelog/new-compare-page) | yes | yes — "May 05, 2026" | yes — "now in Beta"; page adds "Included in Sourcegraph Cloud and Sourcegraph self-hosted 7.3" | none (GA follow-up on Jul 20 recorded as a new lead, see report §3) |
| CI2026-015-003 | [deep-search-finder](https://sourcegraph.com/changelog/deep-search-finder) | yes | yes — "June 15, 2026" | yes — scoped file-finding subagent; page also states an earlier 2026 attempt was **reverted** for latency/agent-behaviour issues; "Included in … self-hosted 7.5" | none (revert noted in report as vendor-disclosed negative evidence) |
| CI2026-015-004 | [agentic-batch-changes-beta](https://sourcegraph.com/changelog/agentic-batch-changes-beta) | yes | yes — "June 29, 2026" | yes — "available now in Beta", "available upon request"; Cloud first, "Self-hosted availability arrives July 8, 2026 with Sourcegraph 7.5" (release list shows 7.5.0 dated Jul 08) | none |
| CI2026-015-005 | [2026-07-20](https://sourcegraph.com/changelog/2026-07-20) | yes | yes — "July 20, 2026" | yes — Code Finder "now available in Beta" through the MCP server, free in Beta; vendor benchmark table (1.00× vs 1.14×/2.19× duration). Page carries a later "Update: … now generally available" line (retrospective edit). The same page also announces **Compare page GA** — not captured by any existing row | none (Compare GA recorded as a new lead) |
| CI2026-015-006 | [search-jobs-external-api](https://sourcegraph.com/changelog/search-jobs-external-api) | yes | yes — "July 27, 2026" | yes — versioned `/api/` endpoints, `externalapi:read`/`externalapi:write` scopes, JSONL results; "Included in … self-hosted 7.6" | none |
| CI2026-015-007 | [2026-08-31](https://sourcegraph.com/changelog/2026-08-31) | yes | yes — "August 31, 2026" | yes — Code Finder searches a branch, tag or commit; same page drops GitHub Enterprise Server ≤3.3 and switches Deep Search default model | none |
| CI2026-015-008 | [agentic-batch-changes-ga](https://sourcegraph.com/changelog/agentic-batch-changes-ga) | yes | yes — "September 14, 2026" | **partly** — body says "available for everyone to try" and "available today for Sourcegraph Cloud customers, on by default for customers with access to AI features"; the literal phrase "generally available" does not appear in the body (GA is signalled only by the URL slug and the index anchor `#agentic-batch-changes-ga`). Page says self-hosted arrives **Sep 16** with 8.0, while the release register dates **8.0.0 on Sep 17** | `limitation` amended (see below); `status` stays `shipped`, `confidence` unchanged |
| CI2026-015-009 | [codeintel-in-compare](https://sourcegraph.com/changelog/codeintel-in-compare) | yes | yes — "October 05, 2026" | **partly** — feature claim supported, but the `availability` value "cloud-only per dated notice" is **not supported** by the page as read on 2026-10-16, which says "Included in Sourcegraph Cloud and Sourcegraph self-hosted 8.1" (8.1.0 is dated Oct 14, after the window). Whether the page said "Cloud only" on 2026-10-14 cannot be checked (no archive) | `limitation` amended (see below); `availability` column left unchanged per no-edit rule; `status` stays `shipped` (Cloud, in-window) |

**Summary:** 9/9 reachable; 9/9 displayed dates match `published_utc`; 7/9 fully supported; 2/9 partly supported and corrected through `limitation` only (no event_id, URL, date or other column changed; no row deleted).

### Exact corrections applied to existing rows

- **CI2026-015-008 `limitation`** — old: "Customer merged-change counts and outcomes are vendor-reported; no independent verification or full cost audit." → new: "QC 2026-10-16: body says 'available for everyone to try' / Cloud customers with AI features; literal 'generally available' wording absent (GA only in slug/anchor); self-hosted promised Sep 16 but 8.0.0 release dated Sep 17. Customer merged-change counts are vendor-reported; no independent verification or full cost audit."
- **CI2026-015-009 `limitation`** — old: "Cloud-only vendor report; functionality and quality not independently tested." → new: "QC 2026-10-16: availability column says cloud-only but page now reads 'Included in Sourcegraph Cloud and Sourcegraph self-hosted 8.1' (8.1.0 dated 2026-10-14, post-window); in-window availability is Cloud. Functionality and quality not independently tested."

### Ledger extension

The first upgrade commit kept the CSV at 9 rows because `tests/test_sourcegraph_source_screen.py` pinned it. On orchestrator authorisation a follow-up commit narrowed that test (all original strict checks now apply to the 9 listed original event_ids; added rows get schema/scope/unique-ID checks) and appended the 17 leads as CI2026-015-010 … -026. Ledger total: 26 rows, sorted by `published_utc`.

## Spot-check of new leads (6 of 17, re-read 2026-10-16)

| Lead | URL | Reachable | Displayed date | Claim/status check |
|---|---|---|---|---|
| L-010 | [2026-04-20](https://sourcegraph.com/changelog/2026-04-20) | yes | "Apr 20, 2026" (index card) | Smart hover summaries "a Beta feature" → `preview` ok; page now also carries an "Update: … generally available" line (retrospective edit) |
| L-016 | [2026-07-20](https://sourcegraph.com/changelog/2026-07-20) | yes | "July 20, 2026" | "the redesigned compare page is now generally available" → `shipped` ok; distinct from -005 on the same page |
| L-019 | [geographic-access-restrictions](https://sourcegraph.com/changelog/geographic-access-restrictions) | yes | "August 04, 2026" | Brownout Aug 14, block after Aug 24 (PDT) stated as future → `announced_only` ok |
| L-021 | [code-finder-ga](https://sourcegraph.com/changelog/code-finder-ga) | yes | "August 20, 2026" | "now generally available through the Sourcegraph MCP server" → `shipped` ok; closes the 2026-10-14 durable-URL gap |
| L-024 | [releases/8.0](https://sourcegraph.com/changelog/releases/8.0) | yes | "September 17, 2026" | Register date Sep 17; `gh api` src-cli 8.0.0 `published_at` 2026-09-17T01:54:16Z; -008 promised Sep 16 → discrepancy recorded, not resolved |
| L-022 | [sourcegraph/EnterpriseBench](https://github.com/sourcegraph/EnterpriseBench) | yes (`gh api`) | `created_at` 2026-09-14T17:09:44Z (no displayed publication date) | README banner "WORK IN PROGRESS — RESULTS NOT VALIDATED" → `reported_undetermined` ok; repo-creation date is not a publication date |

All six matched the values recorded in the [ledger](015-sourcegraph.events.csv) (rows -010, -016, -019, -021, -024, -022). Spot-checks were performed by the same AI session that drafted the leads, so they are **not independent**; a human reviewer should re-open them.

**Embedded instructions:** no text aimed at AI agents was observed in any page read.
