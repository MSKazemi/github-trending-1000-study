# Sourcegraph (015) — seven-segment source-query and inclusion audit, 2026-10-16

> **Provisional source-lead screen (upgraded 2026-10-16):** this search log, the [report](015-sourcegraph.md), the [event ledger](015-sourcegraph.events.csv) and the [source-QC note](015-sourcegraph.source-qc-2026-10-16.md) are **provisional, AI-assisted documentary source leads**. They are **unreviewed by a qualified human**; factual/link, source-access/rights and methods review pending. Merging is not scientific or security sign-off; issue [#81](https://github.com/MSKazemi/github-trending-1000-study/issues/81) was closed on maintainer instruction (2026-10-16) with these review gates still open — reopen it if review finds a defect.

**Earlier log (preserved, untouched):** [015-sourcegraph.screen-log.md](015-sourcegraph.screen-log.md) records the 2026-10-14 bounded screen (PR #178). This file adds the 2026-10-16 upgrade pass; it does not replace or rewrite that log.

**Window:** 2026-04-12…2026-10-12 inclusive (UTC calendar dates). **Session:** 2026-10-16, single AI-assisted session; per-query UTC times not recorded. **Tools:** (1) plain `curl` fetches of public `sourcegraph.com` pages with a generic User-Agent containing no personal identifier; (2) the public [featured changelog RSS](https://sourcegraph.com/changelog/featured.rss) and [blog RSS](https://sourcegraph.com/blog/feed.rss), parsed locally for date/title/link only; (3) read-only `gh api` calls for GitHub repository, release and advisory metadata; (4) six general web-search calls (provider-ranked; result totals are **not exposed**, so search hit counts are **unknown**, not zero); (5) narrow page-summary fetches of four pages. No login, paywall, cookies, bulk crawl or github.com/trending access. No page hashes or archives were stored.

## A. Official index census (one fetch each, 2026-10-16)

| Source | What was counted | In-window count | Per segment (Apr 12–30 / May / Jun / Jul / Aug / Sep / Oct 1–12) |
|---|---|---:|---|
| [Changelog index p.1](https://sourcegraph.com/changelog) + [p.2](https://sourcegraph.com/changelog?page=2) | dated cards (weekly roll-ups + standalone featured posts) | 35 | 3 / 6 / 7 / 7 / 7 / 4 / 1 (+Oct 13 card, **excluded**) — Sep shows 4 weekly roll-ups; the Sep 14 Batch Changes notice is a highlight inside one |
| [Featured changelog RSS](https://sourcegraph.com/changelog/featured.rss) | `<item>` with in-window `pubDate` | 29 of 30 | feed starts 2026-05-14, so April and early May are **not covered by the feed**; one post-window item (Oct 13) |
| [Blog RSS](https://sourcegraph.com/blog/feed.rss) | `<item>` with in-window `pubDate` | 22 of 30 | 2 / 5 / 6 / 5 / 1 / 3 / 0 |
| [Self-hosted release register](https://sourcegraph.com/changelog/releases) | minor/patch releases dated in window | 10 | 7.2.0 Apr 24 / 7.2.1943 May 5, 7.3.0 May 18 / 7.3.2527 Jun 2, 7.4.0 Jun 11, 7.4.2513 Jun 25 / 7.5.0 Jul 8, 7.5.4453 Jul 9 / 7.6.0 Aug 6, 7.7.0 Aug 26, 7.7.359 Aug 27 / 8.0.0 Sep 17 / none (8.1.0 dated **Oct 14, excluded**) |
| `gh api repos/sourcegraph/src-cli/releases` | GitHub releases published in window | 13 | 7.1.0 Apr 16 … 8.0.0 2026-09-17T01:54Z (Apache-2.0) |
| `gh api repos/sourcegraph/scip` | redirect check | — | resolves to `scip-code/scip` (org created 2026-01-09, pre-window); releases v0.7.1 Apr 14, v0.8.0 Jun 2, v0.8.1 Jun 4, v0.9.0 Jun 29, v0.10.0 Sep 3 |
| `gh api orgs/sourcegraph/repos` (sort=created) | public repos created in window | 11 | includes `EnterpriseBench` (Sep 14), `codeprobe` (Sep 8, a field copy of an externally hosted upstream), `fosite` fork (Apr 17) |
| `gh api orgs/sourcegraph/security-advisories` | org-level repository advisories | unavailable | HTTP 404 (endpoint requires org permissions); global advisory DB query for `github.com/sourcegraph/sourcegraph` returned only a 2021 item. **2026 advisory count: unknown, not zero** |

These are **index/feed counts from a single fetch**, not a census of shipped capability; indexes are mutable and the RSS `pubDate` was converted to a UTC date.

## B. Per-segment log — queries/fetches actually run

| Segment | Exact query or fetch | Pages opened (date read on page) | Decision |
|---|---|---|---|
| Apr 12–30 | fetch [2026-04-13](https://sourcegraph.com/changelog/2026-04-13), [2026-04-20](https://sourcegraph.com/changelog/2026-04-20), [2026-04-27](https://sourcegraph.com/changelog/2026-04-27) (QC); release register | Apr 20: smart hover summaries **Beta**, Deep Search search contexts, Git-graph search; Apr 24: self-hosted 7.2.0 | Keep CI2026-015-001; add leads L-010 (Apr 20) and L-011 (7.2.0). Apr 13 bulk-sync changesets and rename conversations: screened, not added (minor) |
| May | fetch [new-compare-page](https://sourcegraph.com/changelog/new-compare-page) (QC), [2026-05-18](https://sourcegraph.com/changelog/2026-05-18), [changelog-search](https://sourcegraph.com/changelog/changelog-search) | May 18: granular admin RBAC (eight permission namespaces); 7.3.0 same day | Keep -002; add L-012 (RBAC). May 14 changelog search: screened, excluded (site feature). Blog posts May 4–28 (5): titles screened only, not opened |
| June | fetch [deep-search-finder](https://sourcegraph.com/changelog/deep-search-finder), [agentic-batch-changes-beta](https://sourcegraph.com/changelog/agentic-batch-changes-beta) (QC), [2026-06-15](https://sourcegraph.com/changelog/2026-06-15), [smart-hover-summaries-ga](https://sourcegraph.com/changelog/smart-hover-summaries-ga); narrow fetch [MCP benchmark blog](https://sourcegraph.com/blog/sourcegraph-mcp-and-a-cheaper-model-beat-a-mythos-class-model-alone); [Jun 30 beta blog](https://sourcegraph.com/blog/agentic-batch-changes-public-beta) | Jun 15 auto-compaction; Jun 16 vendor benchmark (9 tasks); Jun 18 hover summaries **GA** | Keep -003/-004; add L-013 (benchmark), L-014 (hover GA). Jun 30 blog = same launch as -004 (dedup) |
| July | fetch [2026-07-20](https://sourcegraph.com/changelog/2026-07-20), [search-jobs-external-api](https://sourcegraph.com/changelog/search-jobs-external-api) (QC), [2026-07-27](https://sourcegraph.com/changelog/2026-07-27), [deep-search-topic-analytics](https://sourcegraph.com/changelog/deep-search-topic-analytics), [user-credits-cohort-analytics](https://sourcegraph.com/changelog/user-credits-cohort-analytics); narrow fetch of [Business Wire syndication on TechIntelPro](https://techintelpro.com/news/ai/enterprise-ai/sourcegraph-launches-agentic-batch-changes-for-ai-powered-large-scale-code-changes) | Jul 2 wire copy of beta launch; Jul 20 **Compare GA** on same page as Code Finder beta; Jul 27 context filters (`experimentalFeatures`) | Keep -005/-006; add L-015 (wire copy, dedup group of -004), L-016 (Compare GA), L-017 (context filters). Analytics posts screened, excluded (admin analytics). [Jul 23 Code Finder blog](https://sourcegraph.com/blog/code-finder-fast-code-search-for-agents) = same event as -005 (not opened) |
| August | fetch [2026-08-03](https://sourcegraph.com/changelog/2026-08-03), [geographic-access-restrictions](https://sourcegraph.com/changelog/geographic-access-restrictions), [2026-08-17](https://sourcegraph.com/changelog/2026-08-17), [code-finder-ga](https://sourcegraph.com/changelog/code-finder-ga), [2026-08-31](https://sourcegraph.com/changelog/2026-08-31) (QC) | Aug 3 Deep Search guidance/skills + downloadable reports; Aug 4 geo-restriction enforcement; Aug 17 guided diff tour **Beta**; Aug 20 Code Finder **GA** (durable URL now verified) | Keep -007; add L-018, L-019, L-020, L-021 |
| September | fetch [agentic-batch-changes-ga](https://sourcegraph.com/changelog/agentic-batch-changes-ga) (QC), [2026-09-14](https://sourcegraph.com/changelog/2026-09-14), [releases/8.0](https://sourcegraph.com/changelog/releases/8.0), [2026-09-28](https://sourcegraph.com/changelog/2026-09-28); narrow fetch [pricing blog](https://sourcegraph.com/blog/agentic-batch-changes-pricing), [autonomous codebase blog](https://sourcegraph.com/blog/the-autonomous-codebase); `gh api repos/sourcegraph/EnterpriseBench` (+README) | Sep 14 EnterpriseBench repo ("RESULTS NOT VALIDATED"); Sep 16 per-merged-changeset pricing; Sep 17 8.0.0; Sep 21 direction essay | Keep -008; add L-022 … L-025. Sep 28 dictation: screened, excluded (UI) |
| Oct 1–12 | fetch [codeintel-in-compare](https://sourcegraph.com/changelog/codeintel-in-compare) (QC), [2026-10-05](https://sourcegraph.com/changelog/2026-10-05) | Oct 5 commit-signing keys for Batch Changes; guided code-host wizards | Keep -009; add L-026. [Oct 13 update](https://sourcegraph.com/changelog/latest) and self-hosted 8.1.0 (Oct 14) **excluded** (post-window) |

## C. Web-search calls (6 of the shared budget)

| # | Exact query | Useful results actually used | Count |
|---|---|---|---|
| 1 | `Sourcegraph 2026 news Agentic Batch Changes OR "Code Finder" OR "Deep Search"` | Business Wire syndications ([Jul 8 copy](https://cyprusshippingnews.com/2026/07/08/sourcegraph-launches-agentic-batch-changes-in-public-beta-bringing-ai-powered-large-scale-code-change-to-enterprise-engineering-teams/) — not opened; [TechIntelPro Jul 2](https://techintelpro.com/news/ai/enterprise-ai/sourcegraph-launches-agentic-batch-changes-for-ai-powered-large-scale-code-changes) — opened); otherwise sourcegraph.com pages | unknown |
| 2 | `Sourcegraph Amp independent company 2026 Sourcegraph CEO layoffs OR funding OR acquisition` | Only the Dec 2025 split coverage (out of window); no 2026 funding/layoff/acquisition item surfaced (**not proof of absence**) | unknown |
| 3 | `"Sourcegraph" press release 2026 businesswire OR prnewswire` | No wire-domain hit; secondary directories only (not used) | unknown |
| 4 | `Sourcegraph Cody Enterprise 2026 deprecated OR sunset OR "end of life"` | Results point to the 2025 Cody Free/Pro change (out of window) and third-party pricing trackers (not used); no in-window Cody EOL surfaced | unknown |
| 5 | `Sourcegraph Deep Search OR "Agentic Batch Changes" review 2026 site:thenewstack.io OR site:infoq.com OR site:theregister.com OR site:devops.com OR site:sdtimes.com` | **No** article from the five named outlets returned | unknown |
| 6 | `Sourcegraph vulnerability CVE-2026 OR "security advisory" 2026 Sourcegraph` | Only 2021–2022 CVEs and a third-party tracker; **no 2026 CVE surfaced** (not proof of none) | unknown |

## D. Planned but not executed

- Per-outlet independent searches (The New Stack, InfoQ, The Register, SD Times, DevOps.com separately) — **not executed** (shared search budget).
- Hacker News / Reddit discussion search for practitioner criticism — **not executed**.
- NVD keyword query for 2026 Sourcegraph CVEs — **not executed** (no API key; out of budget).
- Corporate-registry/ownership filing check for Sourcegraph Inc. and Amp Inc. — **not executed**.
- Blog posts not opened beyond titles: May 4, 8, 13, 22, 28; Jun 5, 24, 26; Jul 10, 13, 27, 31; Aug 28; Apr 21, 22 — **titles screened only**.
- Docs pages for Agentic Batch Changes, MCP server and supported countries — **not opened**.

## E. Inclusion/exclusion summary

- **Existing ledger rows kept:** 9 (all QC'd, see [source-QC](015-sourcegraph.source-qc-2026-10-16.md)).
- **New verified leads:** 17 (L-010 … L-026), recorded in [report §3b](015-sourcegraph.md) — **not appended to the CSV** because `tests/test_sourcegraph_source_screen.py` pins the ledger at 9 first-party changelog rows and tests may not be edited in this upgrade.
- **Deduplicated:** Jun 30 blog and Jul 2/Jul 8 wire copies → same beta launch as -004; Jul 23 Code Finder blog → same as -005; Sep 14 blog "Introducing Agentic Batch Changes" → same as -008.
- **Excluded (out of window):** Dec 2 2025 Sourcegraph/Amp separation (context only), Mar 2026 changelog entries, Oct 13 changelog, self-hosted 8.1.0 (Oct 14), Cody Free/Pro changes (2025).
- **Amp (watchlist 016):** no Amp Inc. product events are counted here; see [016-amp-inc.md](016-amp-inc.md).
- **Embedded instructions aimed at AI agents:** none observed in the pages read.
