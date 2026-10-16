# Replit (014): search and inclusion log, seven-segment upgrade, 2026-10-16

> **Provisional source-lead screen (upgraded 2026-10-16):** this search log, the [report](014-replit.md), the [event ledger](014-replit.events.csv) and the [source-QC note](014-replit.source-qc-2026-10-16.md) are **provisional, AI-assisted documentary source leads**. No qualified human has reviewed them. Factual/link review, source-access/rights review and methods review are still pending. Merging this is not scientific or security sign-off. Issue #80 was closed on maintainer instruction (2026-10-16) with these review gates still open; reopen it if review finds a defect.

**Window:** 2026-04-12 to 2026-10-12, inclusive. **Inspection date:** 2026-10-16, one session. Exact UTC times per query were not recorded.

**Provenance.** Sources used:
- the official [Replit blog index](https://replit.com/blog), pages 1–3 of the "all" category, read with an AI web reader;
- the official weekly [Replit docs changelog](https://docs.replit.com/updates). The in-window weekly pages were found in the index page's HTML and fetched once each as public `.md` files with a generic user agent;
- direct reads of individual official posts;
- five general web searches (provider-ranked; result totals not exposed);
- read-only GitHub REST API calls for licence and advisory metadata.

**Limits.** This is not an exhaustive internet search. Search-engine result totals are **unknown**, not zero, and so is the full set of excluded hits. No snapshots or hashes were stored.

**Earlier logs (left unchanged):** the [2026-10-14 bounded query checkpoint and 2026-10-15 secondary-source supplement](source-audits/014-replit.2026-10-14-qa.md) list the seven `site:replit.com/blog/` queries run on 2026-10-14. The queries recorded in the [PR #196](source-archives/014-replit.2026-10-12-pr-196-original-report.md) and [first-screen](source-archives/014-replit.2026-10-13-first-screen.md) archives were also run, but their hit counts were not kept.

## Official index screens (census of the two first-party channels)

| Channel | What was fetched | In-window items (Apr 12–30 / May / Jun / Jul / Aug / Sep / Oct 1–12) | Total in window | Notes |
|---|---|---|---|---|
| [Replit blog, all categories](https://replit.com/blog) (pages [1](https://replit.com/blog), [2](https://replit.com/blog/category/all/2), [3](https://replit.com/blog/category/all/3)) | Lists of title, slug and displayed date | 6 / 4 / 9 / 2 / 5 / 3 / **0** | 29 posts | Page 3 starts at Apr 8 (before the window), so pages 1–2 cover the whole window. The Oct 13 "Introducing Replit Solutions Partners" post is **excluded** as post-window. The Aug 18 Free Mode post is pinned as "featured" on every page and was counted once. |
| [Replit docs changelog](https://docs.replit.com/updates) (weekly pages `/updates/YYYY/MM/DD/changelog`) | 26 weekly pages, Apr 17 to Oct 9; `###` item headings counted | 12 / 23 / 17 / 18 / 22 / 14 / 7 | 113 items | The Apr 10 page is before the window. Items are vendor change notes, and one feature can appear in both a blog post and a changelog entry. This is a vendor index, not proof of availability. |

**Zero-result segment.** The blog index shows **no posts dated Oct 1–12**. October is covered only by the weekly changelog (Oct 2 and Oct 9) and by one independent report. This is a property of the channel, not evidence that nothing happened.

## Query and fetch log, by segment

| Segment | Query or fetch actually run (2026-10-16) | Pages opened and decision | Found / screened / excluded |
|---|---|---|---|
| all | Re-opened all 11 existing ledger URLs (see [QC](014-replit.source-qc-2026-10-16.md)) | All reachable; dates match | n/a |
| Apr 12–30 | (fetch) [changelog Apr 17](https://docs.replit.com/updates/2026/04/17/changelog) and [Apr 24](https://docs.replit.com/updates/2026/04/24/changelog) | **Included** -005 (Google Cloud Marketplace MCP listing and Opus 4.7 Power mode). The Apr 24 Security Agent and Auto-Protect entries are already rows -001/-004; the iOS/Android preview and Plaid connector were not included. | 12 items / 12 / 10 not added |
| Apr 12–30 | (fetch) [App Monitoring, Apr 29](https://replit.com/blog/app-monitoring); [Defense in Depth, Apr 20](https://replit.com/blog/defense-in-depth-how-replit-secures-every-layer-of-the-vibe-coding-stack) | **Included** -006. Defense in Depth was **read but not added as a row**: it mostly describes existing controls. Its statement that microVMs are "currently rolling out" is quoted in the report §5. The Google Cloud partner award (Apr 21) and the Replit Animation tutorial (Apr 15) were **excluded** as non-product items. | 6 posts / 6 / 3 not added |
| May | (fetch) [Security Center 2.0, May 7](https://replit.com/blog/security-center); [Enterprise self-serve, May 21](https://replit.com/blog/enterprise-self-serve); changelogs [May 8](https://docs.replit.com/updates/2026/05/08/changelog) and [May 15](https://docs.replit.com/updates/2026/05/15/changelog) | **Included** -007 and -008. May 15 vs May 21 date discrepancy recorded. "Mothers who build" (May 10) **excluded** as a community post. | 4 posts + 23 items / all titles screened |
| May | WebSearch `Replit vibe coding apps security exposed data research 2026` | Returned eWeek, Axios, Freevacy/WIRED, aggregator sites. eWeek and Axios returned **HTTP 403** on fetch. Opened [Freevacy summary of WIRED](https://www.freevacy.com/news/wired/study-finds-security-gaps-in-thousands-of-vibe-coded-apps/7362) and **included** it as -023 (low confidence). A Replit CEO quote that appeared only in search-result text is **not used as evidence**. Aggregator "weekly" and "graveyard" sites **excluded**. | unknown |
| May | WebSearch `Replit funding valuation revenue 2026 news` | Results point to the **March 2026** $400M / $9B round, which is **pre-window** and **excluded**. A "Visa investment May 2026" claim appeared only on an aggregator (komo.ai), was **not opened**, and is **not included**. Conflicting revenue estimates (Sacra, multiples.vc) were not used. | unknown |
| June | (fetch) [Microsoft Fabric, Jun 1](https://replit.com/blog/microsoft-fabric); [SEO Agent, Jun 3](https://replit.com/blog/seo-agent); [Databricks preview, Jun 10](https://replit.com/blog/databricksjune2026); [Replit in Claude, Jun 17](https://replit.com/blog/replit-claude); [Vibecon, Jun 22](https://replit.com/blog/vibecon); changelogs [Jun 5](https://docs.replit.com/updates/2026/06/05/changelog), [Jun 19](https://docs.replit.com/updates/2026/06/19/changelog) | **Included** -009, -010, -011, -012. Vibecon was **excluded** because the post announces no product. The Shopify tutorial (Jun 4) was **excluded**. | 9 posts + 17 items |
| June | GitHub API `search/repositories?q=rayfin+in:name` | `microsoft/rayfin` (MIT, created 2026-05-13) used as the licence/independent-check URL for -009 | 5 results |
| July | (fetch) [Self-Driving Company, Jul 16](https://replit.com/blog/self-driving-company); changelogs [Jul 3](https://docs.replit.com/updates/2026/07/03/changelog), [Jul 24](https://docs.replit.com/updates/2026/07/24/changelog), [Jul 31](https://docs.replit.com/updates/2026/07/31/changelog) | **Included** -013 (stated direction) and -014 (Aug 1 cloud price cut). The redesigned Desktop App (Jul 3) was **not added**; it is mentioned in the report. Replit Design is already CI-014-04, and the Jul 31 changelog confirms it. | 2 posts + 18 items |
| August | (fetch) [Govern Replit at scale, Aug 16](https://replit.com/blog/new-enterprise-governance-tools); [Black-box pen tests, Aug 17](https://replit.com/blog/black-box-pen-tests); "AI adoption starts with truth" (`/blog/ai-adoption`, Aug 3; index entry only); changelogs [Aug 14](https://docs.replit.com/updates/2026/08/14/changelog), [Aug 21](https://docs.replit.com/updates/2026/08/21/changelog), [Aug 28](https://docs.replit.com/updates/2026/08/28/changelog) | **Included** -015, -016, -017, -018. "AI adoption starts with truth" (Aug 3) appears in the index and was **not opened**. The Aug 28 routing changelog entry duplicates 014-E03 and was **deduplicated**. | 5 posts + 22 items |
| August | (fetch) [docs llms.txt](https://docs.replit.com/llms.txt) to look for changelog URLs | No `/updates` links. Found the [Aug 2026 cloud billing page](https://docs.replit.com/billing/aug-cloud-billing-updates) and used it as the check URL for -014; **the page was not opened**. | n/a |
| September | (fetch) [Atta acquisition, Sep 25](https://replit.com/blog/replit-acquires-atta); changelogs [Sep 4](https://docs.replit.com/updates/2026/09/04/changelog), [Sep 11](https://docs.replit.com/updates/2026/09/11/changelog), [Sep 18](https://docs.replit.com/updates/2026/09/18/changelog), [Sep 25](https://docs.replit.com/updates/2026/09/25/changelog) | **Included** -019 (Compliance API) and -020 (Atta). Meta devices/Muse (Sep 25), scheduled backups (Sep 4) and custom APIs (Sep 18) were **screened, not added**. | 3 posts + 14 items |
| September | WebSearch `Replit acquires Atta business analysis September 2026` | Opened [TheCondia (Oct 2, updated Oct 7)](https://thecondia.com/replit-acquires-atta-egypts-ai-startup/) and [Zawya](https://www.zawya.com/en/special-coverage/technology-telecom/us-based-replit-acquires-ai-analytics-startup-atta-1369565) (no date shown; content behind a sign-up wall). TheCondia is used as the independent check. LinkedIn posts and the autobound.ai aggregator **excluded**. *TheCondia contained an embedded instruction aimed at AI readers; it was ignored.* | unknown |
| Oct 1–12 | (fetch) changelogs [Oct 2](https://docs.replit.com/updates/2026/10/02/changelog) and [Oct 9](https://docs.replit.com/updates/2026/10/09/changelog) | **Included** -021 and -022. TikTok Ads and the "work across projects from a chat" item (Oct 9) were **not added**. | 0 posts + 7 items |
| Oct 1–12 | WebSearch `Replit Desktop Windows NVIDIA OpenShell Microsoft preview October 2026` | Opened [RuntimeWire, Oct 7](https://runtimewire.com/article/replit-windows-desktop-app-preview-local-builds) and used it as the independent check and event-date source for -022. The translated docs mirrors (fr/ja/ko/pt) were **deduplicated**. | 10 results |
| cross-window adverse | WebSearch `Replit Agent outage OR incident OR lawsuit OR criticism 2026` | Main result: the July 2025 production-database deletion incident, **pre-window, excluded**. Outage aggregators (isdown.app, pingoru.io) **excluded** as non-authoritative; Replit's own status-page history was **not checked**. No lawsuit found in the results. | unknown |
| rights/security | GitHub API `orgs/replit/repos` (pushed ≥ 2026-04-12); `repos/replit/{replit-cursor-plugin,replit-gemini-extension}`; `repos/replit/{upm,river,crosis}/security-advisories`; `repos/replit/upm/license` | Licences recorded in report §2. The only advisory found (crosis GHSA-7w54-gp8x-f33m) is from **2022, pre-window, excluded**. `replit/replit-cursor-plugin` (MIT) was created 2026-09-30 and is mentioned in the report, not added as a row. | 30 repos pushed in window |

## Queries planned but not executed

- `"Replit" status incident 2026` against Replit's own status page: **not executed** (search budget).
- An independent search for the Visa strategic investment (May 2026): **not executed**. The claim is unverified and not included.
- Counterparty pages (Anthropic for the Claude connector, Microsoft/NVIDIA for the Windows preview, Meta for Meta Connect, Databricks for GA): **not opened**.
- Independent coverage of Free Mode, Intelligent Model Routing and Replit Design: **not executed**.

## Inclusion summary

- **Ledger: 30 rows.** 11 pre-existing and 19 new. Per segment: Apr 12–30: 4; May: 4; Jun: 7; Jul: 3; Aug: 6; Sep: 4; Oct 1–12: 2. Every segment has at least one dated official record.
- **Deduplicated groups:**
  - `014-databricks`: Jun 10 preview → Sep 10 GA.
  - `014-governance`: Aug 16 plan → Sep 11 Compliance API → Oct 2 Workspace settings.
  - `014-mcp-distribution`: Apr 17 Marketplace MCP, Jun 17 Claude connector, Aug 14 MCP server.
  - `014-security-tooling`: May 7 Security Center, Aug 17 pen tests.
  - `014-skills`: Aug 21 import from GitHub. Related to CI-014-02 but kept in a separate group, because the original row's group is preserved.
  - Changelog entries that repeat a blog post were not counted as separate rows.
- **Primary vs independent:**
  - Independent secondary sources exist for only three rows (-020, -022, -023), and all three relay vendor or third-party claims.
  - **No E3 evidence** was found, meaning no independent controlled test or audit of any Replit feature.
- **Access:** public pages and public API metadata only. No login, paywall, private dashboard, participant data or github.com/trending access. No e-mail address or personal identifier was sent in any request.
