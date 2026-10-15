# Atlassian (035): search and inclusion audit for the provisional first-pass screen, 2026-10-16

> **PROVISIONAL, AI-assisted first-pass screen, not reviewed by a human.** This log, the [report](035-atlassian.md) and the [event ledger](035-atlassian.events.csv) are documentary source leads only. Factual/link review, source-access/rights review and methods review are all **pending**. Issue [#102](https://github.com/MSKazemi/github-trending-1000-study/issues/102) stays open.

**Window:** 2026-04-12 to 2026-10-12 inclusive. **Search and source inspection date:** 2026-10-16 (this is the `accessed_utc` for every row). **Tools:** a public web-search tool (provider-ranked results, US index), direct page fetches converted to text, the public SEC EDGAR submissions JSON and full-text search endpoints, and the public GitHub REST API (`gh api`) for one Atlassian repository. **Limits:** the search tool returns provider-ranked results without total hit counts, so found, screened and excluded totals are **unknown, not zero**. Query run times were not captured at UTC precision. No page snapshots or hashes were archived. No account login, paywall, private data or GitHub Trending page was accessed. **This is not an exhaustive search.**

## 1. Query log

"Ext." means the search tool's extended mode. The "Segment" column gives the month segment each query was aimed at; most results cover more than one segment.

| # | Segment | Exact query or direct source | What it surfaced, and the decision |
|---|---|---|---|
| Q1 | all | `Atlassian announces Rovo Dev 2026` | Japanese trade titles and community pages (snippets only). No dated in-window primary source. Led to the Rovo Dev product and licensing pages, which carry no dates and so are context only. |
| Q2 | Apr/May | `Atlassian newsroom May 2026` | Q3 FY26 earnings references and the earnings-date notice for Aug 6. Led to SEC EDGAR. |
| Q3 | May | `Atlassian Team '26 Anaheim announcements` | Event listings and partner recaps (ACE, K15t). No primary content. |
| Q4 | May | `atlassian.com blog company-news team26 Rovo Dev Jira coding agents May 2026` (ext.) | DevOps.com Rovo Dev GA story (**2025-10-09, excluded: outside window**), Rovo Dev product page (undated), dev.to Team '26 Europe write-up (used as a conflicted secondary check). |
| Q5 | May | `"Team '26" Atlassian Anaheim Rovo announcements TechCrunch OR "The Register" OR SiliconANGLE OR "The New Stack"` (ext.) | **Included:** Atlassian founder post and Teamwork Collection post (May 6). Partner recaps (elegancegroup, ikuteam, onpointserv, buzzclan, schneider.im) were excluded as secondary partner marketing. |
| Q6 | May | `atlassian.com blog Team '26 software collection Rovo Dev Jira agents announcement May 6 2026` | Nasdaq copy of the May 6 press release (fetch **timed out**), Business Wire copy (fetch **HTTP 403**), and heise (May 8, fetched and used as an independent check). |
| Q7 | all | `Atlassian security bulletin 2026 critical vulnerability Confluence Data Center CVE-2026` | Monthly bulletins dated Apr 21, May 19, Jun 16, Jul 21 and Aug 18, plus BleepingComputer on CVE-2026-21589. **Included:** the Apr 21 bulletin and the CVE-2026-21589 advisory. **Fetched but excluded:** the May 19 bulletin (third-party-dependency CVEs only), left out to avoid inflating the count with routine monthly bulletins. **Seen only as titles:** Jun 16, Jul 21 and Aug 18 (not fetched). |
| Q8 | Oct | `"Hackers exploit critical Atlassian flaw after public PoC release"` | **Included:** SecurityWeek, Oct 8 (independent). eSecurityPlanet, secnews.gr and Penligent appeared but were not fetched; they repeat the same exploitation story. |
| Q9 | Jun/Jul | `Atlassian Rovo Dev June 2026 OR July 2026 announcement Jira coding agent general availability` (ext.) | Jira Coding Agent support doc (undated; context only), Rovo Dev VS Code GA blog (pre-window per snippet; not fetched). |
| Q10 | identity | `Atlassian acquires 2026 acquisition announced` | No acquisition **announced** in the window. The Browser Company and DX were announced in 2025 and completed in FY26 (baseline). The Secoda item is a MarketScreener snippet only and is unverified. |
| Q11 | Aug | `Atlassian fourth quarter fiscal 2026 results August 6 2026 Rovo` | Futurum and Techzine commentary. Figures were cross-checked against the SEC 8-K exhibit, which was **included**. |
| Q12 | May/Jun | `Bitbucket "Agentic Pipelines" open beta Claude Code support announcement` | **Included:** the Claude Code (May 19) post. jimiwikman.se is a third-party mirror and was excluded. |
| Q13 | Apr | `Atlassian blog April 2026 Rovo Jira Confluence announcement` (ext.) | Weekly "Atlassian Cloud changes" pages and the Futurum Apr 28 analysis. The Apr 13–20 weekly page was fetched but **excluded** because it shows no publication date. |
| Q14 | Apr | `Atlassian Google Cloud Gemini 3 Flash Rovo partnership press release April 2026` | **Included:** the Google Cloud Press Corner copy of the Apr 22 joint release. The Business Wire copy was not fetched. The Google customer-story metrics (200k invocations, 80% task success) were seen in a snippet only, not fetched and not used. |
| Q15 | May/Oct | `Atlassian Rovo MCP server Teamwork Graph CLI general availability 2026` | SiliconANGLE, May 6 (fetched; used as an independent check). A ChatForest review claims core MCP server GA on 2026-02-04; that is **outside the window and third-party**, so it was not used. |
| Q16 | Jul | `"Atlassian Cloud changes" July 2026 agent sessions Jira` | A community post and a pricing-diff tracker (not fetched). No dated official July agent-session GA source was found. The dev.to claim that agent sessions became GA on "8 July 2026" therefore stays **unverified**. |
| Q17 | Jul | `Atlassian July 15 2026 Jira assign work Claude Code Cursor GitHub Copilot agents announcement` (ext.) | DevOps.com (fetch **HTTP 403**, Cloudflare), Deeplink blog (**included**, Jun 16), Claude Agent for Jira pages, and cloudnews.tech (undated byline, so excluded). |
| Q18 | Jul | `atlassian.com/blog Jira "coding agent" every paid plan Planner July 2026` | **Included:** DEVOPSdigest, Jul 16, a relay of the Jul 15 release. The New Stack article body was not retrieved. Dealroom summaries were excluded as aggregators. |
| Q19 | Jul | `"Jira has been the system of record for software teams for two decades" Atlassian` | No hit. The quote is attributed only through the DEVOPSdigest relay, so the report does not reuse it. |
| Q20 | Oct | `Atlassian "Agentic Multiplayer Protocol" AMP open specification` | **Used as the AMP independent check:** Techzine, Oct 7. nand-research, runtimewire, itdaily, winzheng and saasrise were seen as snippets only and not fetched. No AMP specification, repository or license was found. |
| Q21 | Jun | `"Claude Agent for Jira" Atlassian Anthropic launch June 2026` | **Included:** Atlassian blog (Jun 18), with the Jira release note (Jun 24) as a check. The API Evangelist and community pages were not used. |
| Q22 | all | `Atlassian layoffs OR job cuts OR outage OR lawsuit 2026 Reuters` | Layoff of about 10% (about 1,600 roles), reported 2026-03-11: **outside the window**, baseline context only. No lawsuit was found. |
| Q23 | Oct | `Rovo Dev standalone end of life announcement Jira subscriptions Code Reviewer December 3 2026` | The Rovo Dev licensing page (fetched) carries **no publication date**, so it is context only and not a ledger row. |
| Q24 | all | `github.com atlassian MCP server open source repository atlassian/atlassian-mcp-server` | Aggregator star counts were excluded, because stars are not adoption. The repository itself was then checked through the GitHub API. |
| Q25 | Jul | `Atlassian Jira coding agent "every paid plan" announcement July 15 2026 siliconangle OR "the new stack" OR techcrunch` | **Used as the Jul 15 independent check:** IT Brief UK, Jul 16. The Business Wire URL `20260715176442` was seen in results; the fetch returned 403. |
| Q26 | May/Jul/Aug | `Atlassian cloud outage Jira Confluence 2026 incident postmortem` | **Included:** the May 14 and Jul 6 status-page postmortems. The Aug 27 global outage was seen only as a snippet stating that a postmortem was pending; it was not fetched, so it is **not included**. Pingoru aggregator pages were not used. |

### Direct source listings opened

| Source | Result |
|---|---|
| [atlassian.com/blog/announcements](https://www.atlassian.com/blog/announcements) (company news, page 1) | No dates on the listing page. Oct and Sep posts were identified there and their dates were confirmed on the individual post pages. `/page/2` returned **404**. |
| [atlassian.com/blog/bitbucket](https://www.atlassian.com/blog/bitbucket) and [atlassian.com/blog/developer](https://www.atlassian.com/blog/developer) | Listings give image-path month hints only. Dates were confirmed on each post. **The month hint is unreliable:** the Merge Queues post hinted 2026/04 but displays Jun 30. |
| [jirareleases.atlassian.com](https://jirareleases.atlassian.com/) (root, `?date=2026-06-01`, `?date=2026-07-01`, `&page=3`) | Dated Jira release announcements from Apr 27 to Sep 16. A primary dated source. Not every page was paginated, so some Jul 1–26 items may have been missed. |
| [developer.atlassian.com/changelog](https://developer.atlassian.com/changelog/) | Only items from **Oct 6 onward** were visible, because the page renders with JavaScript and `/changelog/rss/` returned 404. Apr–Sep developer-changelog coverage is a **gap**. Oct 13–15 items (Rovo MCP rich UI cards, Teamwork Graph API Preview, Git Credential Manager deprecation) fall **outside the window and were excluded**. |
| SEC EDGAR submissions JSON (CIK 0001650372) and full-text search | In-window filings were listed: 8-K Apr 30 (Q3), 10-Q May 1, 8-K Aug 6 (Q4), 10-K Aug 14, and Forms 4/144/13G. **Included:** the Q4 exhibit. The 10-K (Aug 14) was used for entity verification only. The Q3 exhibit was fetched and excluded because it contains no product-usage metric relevant to M1–M7. |
| GitHub API: `repos/atlassian/atlassian-mcp-server` and its in-window commits | Created 2025-08-01, Apache-2.0, not archived, 62 commits from 2026-04-12 to 2026-10-12. The repository holds client plugins, configs, skills and MCP Registry metadata, not the hosted server. **Included:** PR #197 (SSE endpoint removal) and the Sep 1 v2-endpoint commit. The Apr 14 revert commit was excluded as minor. |
| `investors.atlassian.com/news-events/press-releases` | **404.** SEC EDGAR was used instead. |

## 2. Month-segment coverage

| Segment | Ledger rows | Notes |
|---|---:|---|
| Apr 12–30 | 3 (001–003) | The Apr 13–20 weekly cloud-changes page was excluded because it has no publication date. Q3 FY26 earnings (Apr 30) was screened and excluded. |
| May | 5 (004–008) | Team '26 Anaheim (May 5–7, per event listings) yields two first-party posts in **one duplicate group**. Press-release copies (Business Wire, Nasdaq) were inaccessible. |
| June | 4 (009–012) | The Bamboo-to-Pipelines migration GA (Jun 29) was screened and excluded (lower relevance; it remains available as a lead). |
| July | 4 (013–016) | The Jul 1 flaky-test actions post was screened and excluded because it overlaps row 007's flaky-test agent. The "agent sessions GA 8 July" claim is unverified. |
| August | 4 (017–020) | The Aug 5 Jira Summer release roundup was screened and excluded. Its GA-by-end-of-August expectation was not followed up. |
| September | 4 (021–024) | The Sep 10 built-in Pipelines agents post (status unstated) and the Sep 17 Rovo Chat features post were screened and excluded. |
| Oct 1–12 | 6 (025–030) | This is Team '26 Europe. CVE-2026-21589 has two rows in **one duplicate group** (vendor advisory plus independent exploitation report). |

**No segment had zero findings.** Coverage is still uneven. The weakest areas are developer-changelog items for Apr–Sep and July items before Jul 27 in the Jira release feed.

## 3. Inclusion rules applied

- **Included:** 30 ledger rows. Each has a source page that was opened or read on 2026-10-16 and a displayed or recorded publication date inside the window.
- **Deduplication:** Team '26 posts (004/005) and the CVE-2026-21589 advisory plus SecurityWeek (025/030) each share a `duplicate_event_group`. Press-release relays (DEVOPSdigest, IT Brief) count as **one** event, not as independent confirmation.
- **Same-company corroboration is not independent.** Where `independent_check_url` points to another Atlassian page (009, 010), it is documentary corroboration only.
- **Third-party checks:** heise, SiliconANGLE, IT Brief, Futurum and Techzine mostly relay vendor claims and do no testing. The dev.to write-up is by an Atlassian consultant with products to sell (a conflict of interest). SecurityWeek and BleepingComputer report independent security research (watchTowr, Previdian), but those figures were not re-verified here.
- **Excluded as outside the window:** Rovo Dev GA (2025-10-09), the Data Center end-of-life announcement (Sep 2025), the March 2026 layoffs, the 2025 Browser Company and DX acquisitions, and developer-changelog items from Oct 13–15.
- **Excluded as undated:** the Rovo Dev licensing/EOL FAQ, the Jira Coding Agent support doc, the Rovo Dev product page, and the Apr 13–20 cloud-changes page. These are cited in the report only as context, with their undated status stated.

A future reviewer should re-run these queries, record UTC times and result totals, page through the developer changelog and the Jira release feed for every month, and try to retrieve the Business Wire originals before any final closure.
