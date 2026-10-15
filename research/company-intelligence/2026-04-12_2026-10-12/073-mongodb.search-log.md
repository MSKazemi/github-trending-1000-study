# MongoDB (073) — provisional source-query and inclusion log

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** Companion to the [report](073-mongodb.md) and [event ledger](073-mongodb.events.csv) for [#141](https://github.com/MSKazemi/github-trending-1000-study/issues/141). Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

**Window:** 2026-04-12…2026-10-12 inclusive (UTC dates). **Accessed:** 2026-10-16.

**Method:**
- Official pages were retrieved as raw HTML with `curl` and a generic `Mozilla/5.0` User-Agent. No personal identifier, email or credential was sent to any site.
- Publication dates were taken from each page's JSON-LD `datePublished` or, for press releases, the dateline. Every number, version, date and quote used in a ledger row was confirmed with `grep` against the saved text.
- Machine sources: the NVD CVE API 2.0, the Atlas Statuspage API, `gh api` (releases, tags, licences, commits), the PyPI JSON and npm registry/download APIs, and the Hacker News Algolia API.
- Web search was used once.
- SEC/EDGAR was **not** contacted, and EDGAR-derived mirrors returned by search were not used.

**This is not exhaustive retrieval.** Search-engine result totals were recorded as unknown, not zero. No page snapshots or hashes were archived in the repository, and pages may change after access.

## Query and source log by segment

| Date | Segment | Exact query or source request | Opened / decision | Found / screened / excluded |
|---|---|---|---|---|
| 2026-10-16 | all | `GET https://www.mongodb.com/company/newsroom` and `/company/newsroom/press-releases` (also `?page=2`) | Only the 8 newest press releases render server-side (Aug 13–Sep 29); pagination is client-side | 8 / 8 / 2 (Hope Cochran page is a 2016 release; APJ hire not ledgered) |
| 2026-10-16 | all | `GET https://www.mongodb.com/company/blog/rss` | Feed is incomplete and non-chronological (latest item Jun 25, 2026); used as a lead only | 50 items |
| 2026-10-16 | all | `GET https://www.mongodb.com/sitemap-index.xml`, `sitemap-press-releases-pages.xml`, `sitemap-blog-pages.xml` | `lastmod` values reflect a CMS migration (hundreds of 2011–2025 posts re-touched in Apr–Jun 2026), so each candidate page was opened and its `datePublished` read | 291 PR URLs; 1,406 blog URLs; 65 candidate pages opened |
| 2026-10-16 | all | `GET https://www.mongodb.com/robots.txt` | No disallow for the newsroom, blog, docs or alerts paths used | — |
| 2026-10-16 | all | `GET https://investors.mongodb.com/news-releases` | **HTTP 403: inaccessible**. The Q2 release came from a `webassets.mongodb.com` PDF linked on the newsroom; Q1 came from a PR Newswire copy on placera.se | — |
| 2026-10-16 | all | NVD `cves/2.0?keywordSearch=MongoDB&pubStartDate=2026-04-12…&pubEndDate=2026-08-10…` and `…2026-08-10…2026-10-12T23:59:59.999` | 55 + 142 = 197 keyword hits; filtered to records whose `sourceIdentifier` is MongoDB's CNA identifier = **153** (Apr 2, May 12, Jun 6, Jul 10, Aug 53, Sep 56, Oct 1–12 14). Per-CVE API reads: 6914, 8431, 9740, 18705, 82067, 88029 | 153 / 153 / 148 counted only |
| 2026-10-16 | all | `GET https://www.mongodb.com/resources/products/alerts` | Corroborates CVE-2026-18705 and CVE-2026-82067 with affected/fixed version ranges | — |
| 2026-10-16 | all | `GET https://status.mongodb.com/api/v2/incidents.json`; incident pages `hlhym701zs9m`, `2zp8gbb9dtf7`, `279h4bcrcrlr` | 50 incidents back to 2026-02-26 (covers the whole window); 12 in-window marked "major"; 3 ledgered | 12 / 12 / 9 summarized in the report only |
| 2026-10-16 | all | `gh api repos/mongodb-js/mongodb-mcp-server/releases?per_page=100` (+ bodies of v1.10.0, 1.11.0, 1.12.0, 1.13.0, 1.14.0, 2.0.0, 2.1.0, 3.0.0, 3.0.2; `compare/v2.1.0...v3.0.0`); `GET https://registry.npmjs.org/mongodb-mcp-server` | 45 in-window releases (15 non-prerelease); licence Apache-2.0; v3.0.0 and v3.0.2 have empty bodies | 45 / 9 read / 41 not ledgered |
| 2026-10-16 | all | `GET https://api.npmjs.org/downloads/range/2026-07-06:2026-08-16/mongodb-mcp-server` | Weekly downloads 54,761; 97,555; 75,432; 62,448; 206,191; 93,536. Used only to contextualize the vendor "30,000 installs a week" claim | — |
| 2026-10-16 | all | `gh api repos/mongodb/mongo/git/matching-refs/tags/r8.3`, `…/r9` and tag objects | r8.3.0 tagged 2026-06-03T20:05Z; r9.0.0-alpha1 2026-07-08; r9.0.2 and r9.0.4 2026-10-14 (post-window); no r9.0.0/r9.0.1 tag found; repo licence "Other" (SSPL) | — |
| 2026-10-16 | all | `GET https://www.mongodb.com/docs/manual/release-notes/8.3/` and `/9.0/` (+ `9.0-changelog`) | 8.3.0 dated May 4, 2026; 9.0.0 and 9.0.1 (CVE-2026-89099 fix) dated Sept 28, 2026; 9.0.4 dated Oct 13 (post-window) | — |
| 2026-10-16 | all | PyPI JSON `pymongo`, `langchain-mongodb`, `voyageai`; npm `mongodb` | In-window: pymongo 4.17.0–4.18.3; langchain-mongodb 0.12.0–0.12.1; voyageai 0.4.0–0.5.0 (MIT); Node driver 7.2.0–7.7.0 (Apache-2.0). Context only, not ledgered | — |
| 2026-10-16 | all | `gh api search/repositories?q=org:mongodb+created:2026-04-12..2026-10-12` (and `org:mongodb-js`) | 14 new repos; `skill-gate` (Apache-2.0) ledgered; `pr-review-routine` and `agent-engine-client-libraries` show no detected licence (used as limitations); a personal sandbox repo was ignored | 14 / 14 / 13 |
| 2026-10-16 | all | `gh api repos/mongodb/mongot` + `contents/LICENSE`; `repos/mongodb/agent-skills` (+ releases) | mongot LICENSE = SSPL v1 (API: NOASSERTION); agent-skills Apache-2.0, releases v1.0.0/v1.1.0 pre-window | — |
| 2026-10-16 | all | HN Algolia `search_by_date?query=MongoDB&tags=story&numericFilters=created_at_i>1775952000,created_at_i<1792022400&hitsPerPage=100` (pages 0–1) | 104 stories. Many were false hits (Mongabay, Mongolia) or GUI-vendor marketing (visualeaf.com, excluded) | 104 / 104 / 98 |
| 2026-10-16 | Apr 12–30 | blog `new-research-reveals-overcoming-legacy-tech-issues-key-ai-success` (Apr 14) | Excluded: vendor-commissioned survey, no product change | — |
| 2026-10-16 | Apr 12–30 | status incident `hlhym701zs9m`; NVD CVE-2026-6914 | Both ledgered. Product news was thin; `simplify-security-at-scale-resource-policies` turned out to be from 2025-02-10 (excluded) | — |
| 2026-10-16 | May | press release `mongodb-makes-enterprise-ai-production-ready` (dateline "LONDON, 7 May 2026"); blogs `ai-changing-what-customers-need-from-database-mongodb-8-3-built-for-it`, `bottleneck-in-enterprise-ai-isnt-model-its-data` (May 7), `ai-search-for-agents-announcing-automated-embedding-atlas` (May 11), `fighting-tool-sprawl-case-for-ai-tool-registries` (May 11) | London PR and May 11 post ledgered; 8.3 blog used as a cross-check; tool-registry post excluded (opinion); `intelligent-proactive-resizing…` is dated 2026-02-19 (excluded) | — |
| 2026-10-16 | May | web search `MongoDB first quarter fiscal 2027 financial results June 2026` | Q1 release dated May 28 found; read raw from [placera.se](https://www.placera.se/pressmeddelanden/mongodb-mongodb-inc-announces-first-quarter-fiscal-2027-financial-results-20260528); investors.mongodb.com (403), app.edgar.tools and boardroomalpha (EDGAR-derived) **not opened** | unknown / 9 / 8 |
| 2026-10-16 | June | blogs `production-ready-agents-need-production-ready-data-platform` (Jun 9), `build-trust-in-agentic-ai-from-poc-to-production` (Jun 23), `10-years-mongodb-atlas-built-for-whats-next` (Jun 25), `retrieval-accuracy-is-now-competitive-advantage`, `run-ai-wherever-your-compliance-framework-demands`, `mongodb-upskill-two-million-builders-india-by-2030` (Jun 30); `search-way-you-model-nested-embeddings-in-atlas` (datePublished May 14, modified Jun 29) | Jun 30 retrieval post ledgered; thought-leadership and anniversary posts excluded; nested-embeddings post not ledgered (feature detail not read) | — |
| 2026-10-16 | June | [InfoWorld 2026-06-30](https://www.infoworld.com/article/4191046/mongodb-embeds-reranking-into-atlas-as-enterprises-look-to-simplify-ai-stacks-for-scale.html) (linked from newsroom "In the news") | Read raw; used as the independent check (preview status, "up to 30%" vendor claim, lock-in critique) | — |
| 2026-10-16 | July | blogs `mongodb-search-vector-search-now-run-anywhere` (Jul 1), `improving-agent-retrieval-native-reranking-hybrid-search` (Jul 2), `state-persistence-the-problem-of-agent-reliability`, `atlas-stream-processing-brings-operational-data-to-apache-iceberg` (Jul 6), `introducing-atlas-gen2-on-aws-m30-dedicated-clusters` (Jul 7), `mongodb-atlas-delivers-greater-capacity-reliability-operational-confidence` (Jul 14), `three-questions-agent-security-has-to-answer` (Jul 16), `atlas-10-years-celebrating-customers-behind-platform` (Jul 29) | 2 rows. The Iceberg and capacity posts were not ledgered (outside the study angle and for brevity). `how-mongodb-protects-against-supply-chain-vulnerabilities` dates from 2022 (excluded) | — |
| 2026-10-16 | July | [Shuji Sado 2026-07-15](https://shujisado.org/2026/07/15/mongodb-v-ferretdb-when-open-source-compatibility-becomes-a-patent-risk/) (via HN) | Ledgered as an independent analysis reporting the Apr 28, 2026 court order; court docket not read | — |
| 2026-10-16 | July | [Fathom 2026-07-27](https://usefathom.com/blog/migrating-gauges-from-mongodb) (via HN) | Excluded: a migration of an acquired product's data to the acquirer's existing ClickHouse stack, which is not evidence about MongoDB quality | — |
| 2026-10-16 | August | blogs `catch-mongodb-anti-patterns-on-every-pr-with-claude-routines` (Aug 3), `mongodb-for-agentic-era-built-for-developers-ai-agents`, `closing-gap-between-agentic-promise-impact-industry-leading-retrieval` (Aug 13), `close-database-blind-spot-with-atlas-observability` (Aug 14), `agent-memory-inside-harness` (Aug 18), `how-we-used-ai-bring-mongodb-to-dynamodb` (Aug 24), `mongodb-atlas-joins-google-cloud-foundation-fabric…` (Aug 26), `cheapest-token-you-never-send…` (Aug 27); press releases (dateline "SAN FRANCISCO—Aug. 13, 2026") | 5 rows. Observability, Google FAST and tutorial posts excluded. `amp-ai-driven-approach-modernization` (2025) and `enhancing-atlas-online-archive…` (2022) excluded as pre-window | — |
| 2026-10-16 | August | `gh api repos/ExtendDB/extenddb` (Apache-2.0), commits for `docs/design/13-storage-mongodb.md` and `docs/rfcs/0000-mongodb-backend.md`, PR search `mongodb` | First commits 2026-08-11T16:57Z; follow-up MongoDB fixes merged in Sep | independent upstream artifact |
| 2026-10-16 | August | [TechTarget 2026-08-13](https://www.techtarget.com/data-technologies/news/366649199/MongoDB-intros-latest-features-to-fuel-AI-development); [RECON 2026-08-12](https://hellorecon.com/blog/cve-2026-18690-mongodb-symbol-type-authz-bypass) | Both read raw. RECON's "four Server CVEs" conflicts with the 24 MongoDB Server CVEs NVD lists for Aug 11 | — |
| 2026-10-16 | September | press releases `mongodb-announces-ceo-transition` ("NEW YORK, Sept. 28, 2026"), `mongodb-launches-mongodb-9-0…`, `mongodb-launches-atlas-agent-engine…` ("September 29, 2026"), `cognition-and-mongodb-partner…` ("Sept. 29, 2026"), `mongodb-names-richard-scott…` ("Sept. 2, 2026"); Q2 PDF (`pdftotext`) | All but the APJ hire ledgered | — |
| 2026-10-16 | September | blogs `vfs-langchain-deep-agents-searchable-filesystem-agents` (Sep 3), `build-fraud-review-agent-atlas-claude-managed-agents` (Sep 9), `analyze-atlas-data-openai-chatgpt-work` (Sep 10), `same-query-same-score…stabletfl…` (Sep 25), `your-database-just-became-your-ai-control-point`, `intelligent-data-platform-for-ai-era` (Sep 29), `introducing-rerank-3-and-native-rerank`, `everything-announced-mongodb-local-nyc-2026`, `how-atlas-agent-engine-powers-mongodbs-internal-ai-strategy` (Sep 30), `europe-data-residency-for-atlas-embedding-reranking` (datePublished Sep 1) | ChatGPT and NYC-roundup posts ledgered; the others were folded in or excluded as tutorials and positioning. `introducing-the-embedding-and-reranking-api-on-mongodb-atlas` has datePublished 2026-01-15 (pre-window, modified Aug 13). `announcing-a-modernization-toolkit` resolves to a 2025 post | — |
| 2026-10-16 | September | [Silicon Republic 2026-09-29](https://www.siliconrepublic.com/business/meta-enterprise-platform-to-be-led-by-outgoing-mongodb-boss-ai), [TIKR 2026-09-28](https://www.tikr.com/blog/meta-poaches-mongodb-ceo-effective-immediately-stock-sinks-24), [Economic Times 2026-09-28](https://economictimes.indiatimes.com/tech/technology/mongodb-ceo-chirantan-desai-steps-down-to-lead-metas-enterprise-platform/articleshow/134543554.cms); Reuters article | Reuters **HTTP 401: inaccessible**. TIKR's 24% (headline, premarket) vs 15% (body) conflict was recorded | unknown / 5 / 2 |
| 2026-10-16 | Oct 1–12 | blogs `queryable-encryption-prefix-suffix-substring-queries-are-now-ga` (Oct 6), `mongodb-9-0-this-is-what-a-database-should-be` (Oct 5), `9-0-observability-capabilities-less-hunting-more-resolving` (Oct 7), `code-mode-without-interpreter-agents-that-write-aggregation-pipelines`, `intelligent-workload-management-keeping-your-clusters-available-when-it-matters` (Oct 8); status incident `279h4bcrcrlr` (Oct 9) | 3 rows; the others were folded into the 9.0 row. `extension-for-hibernate-orm-now-ga` is datePublished Oct 13 (post-window) | — |
| 2026-10-16 | post-window | 9.0.4 (Oct 13), r9.0.2/r9.0.4 tags (Oct 14), pymongo 4.19.0 (Oct 14), MCP v3.1.0 (Oct 15), Hibernate GA blog (Oct 13), Oct 13–15 blog posts | **Excluded** as out of window; tag dates noted only as a limitation on the 9.0 GA row | — |

## Inclusion, deduplication and conflicts

- **Included:** 35 rows (Apr 2, May 5, Jun 4, Jul 3, Aug 8, Sep 10, Oct 3). Every row cites a URL that was fetched as raw text or queried by API. No row relies on a search snippet alone.
- **Duplicate groups:**
  - `073-004`: Automated Embedding, public preview (May 11) and GA (Aug 13).
  - `073-011`: Native Reranking, preview (Jun 30) and GA (Sep 30).
  - `073-018`: the Aug 11 CVE batch and the independent CVE-2026-18690 write-up.
  - `073-020`: the Atlas Managed MCP Server launch and the ChatGPT Work connector it powers.
  - `073-029`: the 9.0 GA and the Queryable Encryption substring GA write-up.
- **Date conflicts recorded, not resolved:**
  - 8.3.0: release notes May 4, GA press release May 7, GitHub tag Jun 3.
  - 9.0.0: release notes Sep 28, press release Sep 29, public GitHub tags (r9.0.2/r9.0.4) Oct 14.
  - The Sep 29 press releases name the Investor Day at Nasdaq MarketSite as the launch venue, while the Sep 30 roundup frames the same items as MongoDB.local NYC announcements.
  - Hibernate ORM GA is listed in the Sep 30 roundup, but its own blog post is dated Oct 13.
- **Figure conflicts:**
  - RECON reports "four" Server CVEs on Aug 11; NVD lists 24 MongoDB Server CVEs published Aug 11.
  - CVE-2026-6914 is scored CVSS 3.1 6.5 by the CNA and 7.5 by NVD.
  - TIKR reports both a 24% premarket fall and a 15% fall in the share price.
  - Customer counts differ by release: 65,200+ (May), 67,000 (Aug) and 70,000 (Sep).
  - The install claim reads "30,000 installs a week" in the press release and "30,000 npm installs per week" in the blog; npm downloads are not installs.
- **Figures confirmed against raw text (grep of saved text):**
  - 8.3: 45% reads / 35% writes / 15% ACID.
  - 9.0: 35% find-one, 30% update-one, up to 2x throughput, 20% transactional throughput.
  - Q1 FY2027: $687.6M, 25%, more than 29% Atlas growth.
  - Q2 FY2027: $771.8M, 30%, about 29% Atlas growth, $2.99B–$3.03B guidance.
  - "$35 million to more than $2.3 billion" (CEO release).
  - 15–20% CPU reduction (Gen2); "up to 30%" (InfoWorld); rerank-3-lite "40% of the price"; "three trillion queries a day"; PicPay "4x its normal peak".
  - CVSS scores of the six individually read CVEs; status-page timestamps; npm weekly download sums.
  - All remain **vendor or press statements**, not verified measurements.
- **Not every figure in every vendor page was checked.** Only the figures used in the ledger and report were checked.
- **Untrusted-content note:** fetched pages were treated as data. No page contained instructions directed at the researcher or at AI agents. The `skill-gate` README and the Claude Routines tutorial describe agent prompts as subject matter; none of their commands were run. Search-tool summaries were treated as leads only.

## Missing, inaccessible or not attempted

- **Inaccessible:** investors.mongodb.com (HTTP 403) and Reuters (HTTP 401).
- **Not read:** the FerretDB court docket, the Axios and Bloomberg originals, the OpenAI-side Data Plugin documentation, Cognition-side terms, Voyage AI model cards and RTEB leaderboard snapshots, the MongoDB community-forum release threads, and archived (Wayback) copies of mutable pages.
- **Not performed:** a CVE-by-CVE fixed-version check for drivers, any test of the products, account creation, network scanning or energy measurement.
- No months were empty. April 12–30 had little product news; only an incident and a CVE were ledgered.
- **Reproduction:** re-run the requests above with UTC timestamps and save raw HTML hashes. An independent human should spot-check at least these rows before any evidence is promoted beyond provisional status:
  - the 9.0 GA versus public tag dates (CI2026-073-029);
  - the CVE batch count (018/019);
  - the MCP 2.0/3.0 breaking-change rows (017, 027);
  - the ExtendDB upstream artifact (022);
  - the FerretDB court order date (014).
