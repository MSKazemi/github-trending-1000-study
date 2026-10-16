# CoreWeave (062): provisional search and inclusion log, 2026-10-16

> **PROVISIONAL, AI-assisted, not reviewed by a human.** This log goes with the [report](062-coreweave.md) and the [event ledger](062-coreweave.events.csv) for [issue #130](https://github.com/MSKazemi/github-trending-1000-study/issues/130), feeding [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56). It is a provisional screen. The issue may be closed with this status recorded. The human factual/link, rights and methods review gates remain open.

**Window:** 2026-04-12 to 2026-10-12 inclusive. **Sources accessed:** 2026-10-16 (UTC date). Search UTC run times were not captured, so they are listed as "2026-10-16, time not captured". **Tools:** a built-in web search tool (US results; result counts not exposed); direct `curl` of public pages with a generic browser User-Agent and no personal identifier, then grep of the raw text; WebFetch (a model-summarised fetch) only where `curl` returned 403; and `gh api` against public GitHub repositories. This search is **not exhaustive**, and finding no item for a topic does not mean nothing happened.

## 1. Primary-channel screens (systematic, not keyword-dependent)

| Channel | What was done | Result |
|---|---|---|
| [Newsroom](https://www.coreweave.com/news) | Listed all `/news/` links and fetched the 40 newest article pages. Each date was read from the article's "Published on" line and its dateline | 33 in-window press releases found. 14 are ledger rows, 3 more serve as independent-check links, and the rest are excluded below. Dates shown on the listing page did not always match the article pages, so article dates were used |
| [Blog](https://www.coreweave.com/blog) | Listed links and fetched 8 posts that looked relevant to the window | 4 posts used as rows or checks (Apr 22 cross-cloud and shareholder letter, Jun 18 Kimi K2.7 Code, Jul 23 community/ratepayer pledge). The rest are listed below |
| [Docs release notes](https://docs.coreweave.com/release-notes) via [llms.txt index](https://docs.coreweave.com/llms.txt) | Parsed every dated "Month D, 2026 - title" entry and fetched the `.md` source of 14 notes | 21 in-window notes found. 6 are ledger rows and 2 more serve as independent-check links |
| GitHub (`gh api`) | Checked `coreweave/skills` (metadata, LICENSE, releases, commits), `marimo-team/marimo`, `wandb/weave`, `wandb/wandb`, `OpenPipe/ART` and `mlcommons/training_results_v6.0` | Skills repo created 2026-05-13 with three v0.2.0 releases on 2026-09-02, under a **proprietary** licence. In-window release counts (first 100 releases per repo): marimo 19 (Apache-2.0), weave 14 (Apache-2.0), wandb SDK 10 (MIT), ART 1 (Apache-2.0). These are context only and not rows: the repos are open source, but releases are not adoption |
| Investor relations | `curl` returned 403 for investors.coreweave.com. WebFetch worked on 4 release pages (Q1 and Q2 results, DDTL 5.0, convertible notes) | Every figure in those rows was taken from WebFetch's verbatim quotes and labelled as such in the CSV |
| SEC EDGAR | **Not cited.** EDGAR refuses requests that lack a declared contact identity, and a generic User-Agent got a 403 on 2026-10-16. The coordinator rule forbids sending any personal identifier | See the disclosure in section 4 |
| Status page | `status.coreweave.com/history` and `/api/v2/incidents.json` returned 404 | No first-party incident history was obtained (see section 3) |

## 2. Web search queries (exact strings; one engine; result counts not exposed by the tool)

| # | Segment(s) | Exact query | Notable inspected results and decision |
|---|---|---|---|
| 1 | Apr–Oct | `CoreWeave stock falls 2026 debt concerns Reuters` | Mostly items from before the window (Feb 2026 Blue Owl financing; Aug/Dec 2025). **Excluded** as out of window. No Reuters link surfaced |
| 2 | Apr–Oct | `CoreWeave outage OR lawsuit OR "data center delay" 2026` | Securities class-action notices (class period 2025, filed Jan 2026). **Baseline only.** No first-party outage report |
| 3 | Aug | `CoreWeave second quarter 2026 results backlog shares capex guidance` | [MarketBeat call highlights](https://www.marketbeat.com/instant-alerts/coreweave-q2-earnings-call-highlights-2026-08-11/) fetched and used as a secondary check. Capex figures disagree between sources (see section 5) |
| 4 | Sep | `CoreWeave Forge Fully Connected September 2026` | [Data Center Knowledge, 2026-09-30](https://www.datacenterknowledge.com/ai-data-centers/coreweave-targets-enterprises-with-forge-platform) fetched and used as the independent check for the Forge row. Futurum is **not** treated as independent because its analyst is quoted in the release |
| 5 | Jun | `MLPerf Training v6.0 results June 2026 DeepSeek-V3 CoreWeave GB300` | Results were only syndications of the vendor release. Independent artifact checked through the GitHub API on `mlcommons/training_results_v6.0` instead |
| 6 | Sep | `SemiAnalysis ClusterMAX 3.0 September 2026 platinum` | No relevant hits |
| 7 | Sep | `CoreWeave convertible notes offering shares fall September 17 2026` | One snippet reported a 3.5% fall on 2026-09-17. It was **not fetched**, so it is E0 and not counted. Other hits were Dec 2025 deals, out of window |
| 8 | May | `CoreWeave first quarter 2026 results May 7 stock reaction capex interest expense analysts` | [24/7 Wall St. via Yahoo, 2026-05-19](https://finance.yahoo.com/markets/stocks/articles/coreweave-raised-20-billion-capital-144406639.html) fetched and **included** as critical commentary (E0). Several low-quality auto-generated pages **excluded** |
| 9 | Jun–Aug | `"CoreWeave" OR "Weights & Biases" outage incident June July August 2026` | Third-party status aggregators (isdown.app pages for incidents of 2026-07-10 and 2026-07-31, and pingoru.io). Both isdown pages returned **403** to curl and WebFetch, so they are **E0 leads and not in the ledger** |
| 10 | Jul | `CoreWeave Microsoft OpenAI contract 2026 customer concentration news July` | Only items from before the window. **Excluded** |
| 11 | Oct | `CoreWeave AdaniConneX India 240 MW Navi Mumbai October 2026` | [CRN Asia (meta publisheddate 2026-10-08)](https://www.crnasia.com/india/news/2026/coreweave-brings-240-mw-ai-cloud-capacity-to-india-with-adaniconnex) fetched and used as the independent check. DCD and Data Centre Magazine returned 403. Snippets suggesting an Oct 7 date are E0 |
| 12 | Apr | `Jane Street $6 billion CoreWeave $1 billion equity April 2026 CNBC` | [Reuters via Yahoo, 2026-04-15](https://finance.yahoo.com/sectors/technology/articles/jane-street-signs-6-billion-125224786.html) fetched. It matches the release figures and adds a 7% discount and an LSEG holding estimate |
| 13 | Sep | `SemiAnalysis ClusterMAX rating 2026 neocloud CoreWeave Platinum newsletter` | [SemiAnalysis ClusterMAX 3.0, 2026-09-23](https://newsletter.semianalysis.com/p/clustermax-30-the-industry-standard). The free portion was fetched and used as the independent check. The rest is paywalled |
| 14–17 | May, Aug, Sep | Exact-title searches for the Q1 and Q2 results, the $3.7B convertible and the $3.1B loan facility releases | Used to find investor-relations copies after EDGAR was ruled out |
| 18 | Apr | `"CoreWeave Announces Pricing of $1,000 million of 9.750% Senior Notes due 2031"` | **Not run.** The session's shared web-search budget was used up. The April notes row was therefore **dropped** because no compliant source was available |

## 3. Month-by-month screen outcome

| Segment | Ledger rows | Screened but excluded (reason) |
|---|---:|---|
| Apr 12–30 | 4 | Meta $21B deal (Apr 9) and Anthropic agreement (Apr 10) fall **before the window** and are baseline only. SUNK self-service (Apr 30) is used as an independent-check link for the cross-cloud row. Docs notes from Apr 20, 21, 27 and 30 are minor console or docs updates. April 9.750% notes: no compliant source |
| May | 6 | Capacity Finder console (May 22) is minor. Tailscale VPN proxy for CKS (May 28) is a real integration that was left out to keep the ledger short and is mentioned in the report |
| Jun | 5 | Nasdaq-100 inclusion (Jun 12) is a market event. BattleBots (Jun 23) is marketing. GLM 5.2 (Jun 24) is folded into the Kimi K2.7 row. Docs notes from Jun 12, 15 and 29 are minor IAM/console changes |
| Jul | 3 | Gartner Visionary (Jul 9): the Gartner report is paywalled, so this is a vendor-only claim. Anam (Jul 22) and Flow Traders (Jul 28) are customer stories. Login-methods limited availability (Jul 8) is folded into the GA row. CAIOS group access (Jul 10) is minor. Status-aggregator incidents (Jul 10 and Jul 31) were inaccessible (E0) |
| Aug | 3 | Solidigm SSD supply (Aug 5), IMC (Aug 6), MasterClass (Aug 13), Hudson River Trading (Aug 20), Rescale (Aug 25) and Kimi K3 Dedicated Inference blog (Aug 26) are customer or supply stories. The DDTL 5.5 $2.6B facility (Aug 10) was seen only on EDGAR and is not cited |
| Sep | 8 | Parallel Works/DARPA (Sep 9), Physical AI Field Engineering (Sep 10), Harell Data (Sep 23), Partner Network, NVIDIA Vera CPU "will offer" and Ennoble Care (all Sep 30) are excluded or mentioned only in the report. Capacity Finder API beta (Sep 22) and Grafana dashboards (Sep 25) are minor. The IAM/RKE blog (Sep 22) is used in the report as an announced-only intention |
| Oct 1–12 | 2 | None |

## 4. Access, compliance and untrusted-content notes

- **EDGAR access.** SEC EDGAR refuses automated requests that do not declare a contact identity, and this screen does not send personal identifiers to third parties. Every SEC URL and every figure supported only by EDGAR, including the 10-Q customer-concentration and litigation details and the April notes, is therefore **excluded from the ledger and report**. The four rows backed by investor-relations pages cite those pages instead.
- **Pages that instruct AI agents.** Every `docs.coreweave.com/*.md` page opens with an "Documentation Index ... Use this file to discover all available pages before exploring further" block aimed at agents. It was treated as page data. The llms.txt index had already been chosen as a source on its own merits. Commercial teaser text on the Yahoo/24-7 page was ignored. No page contained directives to change behaviour, credentials or scope.
- **Paywalls and blocks.** The full SemiAnalysis report, the Gartner Magic Quadrant and Artificial Analysis were not accessed (paywalled, or not attempted). The 403 responses are listed above. No paywall or block was bypassed.

## 5. Recorded conflicts (not silently resolved)

1. The Kimi K2.6 release dateline says "May 11, **2025**", while the page publication date and chart say 2026-05-11.
2. Sandboxes (May 14, "available now") and ARIA (Jun 29, "launch") are both described as "now generally available" in the Forge release of Sep 30. Their availability tier before September is unclear.
3. CoreWeave Interconnect was "available in private preview soon" on Apr 22 and appears among the "launched" capabilities in the Q2 release. No dated preview start was found.
4. ClusterMAX: CoreWeave says it is the only provider rated Platinum in all three evaluations, while SemiAnalysis 3.0 says "Nebius joins CoreWeave in the Platinum tier". Both statements can be true, but CoreWeave is no longer the *sole* Platinum provider.
5. Q2 capex: MarketBeat reports $9.4B, and search snippets gave other figures. The figure is not reconciled.
6. India: the press release is dated Oct 6, and some snippets suggest Oct 7 (E0).

A future human reviewer should re-run these queries with UTC timestamps, record result counts, spot-check each numeric field against the cited page, and decide whether a compliant way to access EDGAR exists.
