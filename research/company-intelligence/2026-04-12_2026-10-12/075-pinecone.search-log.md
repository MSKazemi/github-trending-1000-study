# Pinecone (075) — provisional source-query and inclusion log

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** This log accompanies the [report](075-pinecone.md) and [event ledger](075-pinecone.events.csv) for [#143](https://github.com/MSKazemi/github-trending-1000-study/issues/143). Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

**Window:** 2026-04-12…2026-10-12 inclusive (UTC dates). **Accessed:** 2026-10-16.

**Method:**
- Official pages were fetched as raw HTML with `curl` using a generic `Mozilla/5.0` User-Agent. No personal identifier, email or credential was sent to any site.
- Text was extracted locally. Every number, version, date and quote used in a ledger row was confirmed by `grep` of the extracted raw text.
- Blog `publishDate` and `datePublished` values were taken from the page's embedded JSON and JSON-LD.
- `gh api`, the PyPI JSON API and the npm registry supplied release dates and licences.
- The Hacker News Algolia API and three web searches were used for independent and critical coverage. WebFetch summaries were not used for any figure.

**This is not exhaustive retrieval.** Search-engine result totals were not exposed and are recorded as unknown, not zero. No page snapshots or hashes were archived in the repository, and pages may change after access.

## Query and source log by segment

| Date | Segment | Exact query or source request | Opened / decision | Found / screened / excluded |
|---|---|---|---|---|
| 2026-10-16 | all | `GET https://www.pinecone.io/` and `/sitemap.xml` | Sitemap lists 622 URLs, all with one identical `lastmod`, so it was not usable for dating | — |
| 2026-10-16 | all | `GET https://www.pinecone.io/blog/` and `/newsroom/`; parsed the embedded page JSON (`publishDate`, `slug`, `categories`) | 51 blog and 144 newsroom/blog entries in the embedded data. In-window: 27 blog posts and 5 press releases | 32 / 32 opened / see exclusions |
| 2026-10-16 | all | `GET https://docs.pinecone.io/release-notes` (the "Pinecone 2026 changelog") | All 2026 entries read. 33 in-window entries. Oct 13–15 entries excluded as post-window | 33 / 33 / most minor entries folded into limitation text |
| 2026-10-16 | all | `GET https://docs.pinecone.io/llms.txt`, `/reference/api/versioning`, `/guides/nexus/overview.md` | Used for the product map and the API versioning policy (quarterly stable versions, at least 12 months' support) | context only |
| 2026-10-16 | all | `gh api orgs/pinecone-io/repos?sort=pushed` | 60 repos listed with licences. New in-window repos include cultivar (MIT), vq-bench (MIT), tau2-bench (MIT fork of sierra-research/tau2-bench), pinecone-codex-plugin (MIT) and nexus-installer (Apache-2.0) | context; licences recorded in the report |
| 2026-10-16 | all | `gh api repos/pinecone-io/{python-sdk,pinecone-ts-client,go-pinecone,pinecone-java-client,terraform-provider-pinecone,pinecone-mcp,cli,cultivar}/releases` | 24 in-window GitHub releases (Java: none in window; v6.2.0 is dated 2026-04-01) | 24 / 24 / patch and minor releases not ledgered (Python 9.0.1, 9.1.0; Node 8.1.0, 8.2.0; Go 6.1.0; CLI 0.4.6, 1.0.1; cultivar after v0.3.0) |
| 2026-10-16 | all | `GET https://pypi.org/pypi/pinecone/json`; `GET https://registry.npmjs.org/@pinecone-database/pinecone` | Upload times recorded. PyPI licence expression Apache-2.0, requires-python >=3.10. npm licence Apache-2.0 | — |
| 2026-10-16 | all | `GET https://status.pinecone.io/api/v2/incidents.json` (Atlassian Statuspage) | 50 incidents returned, oldest 2025-08-26. 19 fall in the window. The Jun 18 empty-results incident is ledgered. The rest are listed in report §3 | 19 / 19 / 18 not ledgered |
| 2026-10-16 | Apr 12–30 | posts `load-balancing`, `dedicated-read-nodes-ga`, `dedicated-read-nodes-ga-features`; newsroom `zoominfo-pinecone-drn` | DRN GA included. Load-balancing engineering post excluded (no dated product change). ZoomInfo release excluded as a customer case study | — |
| 2026-10-16 | May | posts `knowledge-infrastructure-for-agents`, `introducing-nexus-knowledge-engine`, `marketplace`, `builder-plan`, `full-text-search`, `full-text-search-architecture`, `turn-azure-data-into-an-ai-ready-knowledge-base`; press `Pinecone-Launches-First-Serverless-Region-in-Asia`, `Pinecone-Expands-in-Europe-with-New-Frankfurt-Cloud-Region` | Launch post, Builder, FTS and Marketplace included. The engineering companion post and FTS architecture post were used as context. The Azure Blob ingestion template post (May 27) was excluded as a tutorial. The region press releases were folded into the changelog row as a date conflict | — |
| 2026-10-16 | June | posts `bulk-import-promo`, `inside-askdata`, `nexus-ea-benchmarks`, `open-source-monitoring-stack`, `generating-test-data-for-pinecone`; press `microsoft-onelake-nexus` | Bulk import, OneLake and the monitoring stack were included. AskData (dogfooding, ">92%" token claim) and EA benchmarks were used as context. The test-data post was excluded as a tutorial | — |
| 2026-10-16 | June | `gh api repos/pinecone-field/pinecone-monitoring` and `/contents` | No licence detected and no LICENSE file in the repo root | rights limitation recorded |
| 2026-10-16 | June | `GET` darryl-ruggles.cloud cost comparison (found via HN Algolia) | Read raw. datePublished 2026-06-01. Included as a small independent measurement | 1 / 1 / 0 |
| 2026-10-16 | July | posts `pinecone-nexus-public-preview`, `sparse-v3`, `text-match-filters`, `behind-the-benchmarking-pipeline` | Nexus PP included. Sparse V3 (vendor 151× I/O claim), text-match filters and the benchmarking pipeline were excluded as engineering explainers (inventory context only) | — |
| 2026-10-16 | July | `GET https://siliconangle.com/tag/pinecone/` (pages 1–2), then the 2026-07-02 article | One in-window Pinecone-specific article (Nexus public preview, datePublished 2026-07-02T15:55Z), read raw and included. Other tag-page items are general columns, not opened | ~11 / 1 / 10 |
| 2026-10-16 | Aug | posts `the-ceiling-was-never-the-model`, `pinecone-nexus-generally-available`, `designing-agent-friendly-apis`, `one-year-in-just-getting-started`; press `general-availability-of-pinecone-nexus-…` | All except the "Ceiling" opinion essay were included. The "Ceiling" essay was excluded as opinion | — |
| 2026-10-16 | Aug | `GET https://spec.knowql.org/` and `/0.1.0`; `gh api repos/pinecone-io/knowql-spec`; anonymous `GET https://github.com/pinecone-io/knowql-spec` | Spec read (OWFa 1.0, dated Aug 6, 2026). The named repo returned **404** to both requests | conflict recorded |
| 2026-10-16 | Sep | posts `support-agent-nexus`, `full-text-search-generally-available`, `vq-bench`, `byoc-generally-available` | FTS GA and BYOC GA were used as date-conflict checks on the changelog rows. VQ-bench was included. The support-agent post was used as context (its figures repeat the Nexus GA post) | — |
| 2026-10-16 | Oct 1–12 | changelog entries 2026-10-07; Terraform v5 release | Both included. The `byoc-on-demand` post (Oct 15) and changelog entries Oct 13–15 were excluded as post-window | — |
| 2026-10-16 | cross-window | HN Algolia `search_by_date?query=Pinecone&tags=story&numericFilters=created_at_i>1775952000,created_at_i<1792022400&hitsPerPage=100` | 18 hits. Most are name collisions (PINE64 devices, an Arduino "Pinecone DAISY-1" computer) or Show HN projects. The vendor launch post had 6 points and 0 comments. A competitor-run VDBBench leaderboard (zilliz.com) was fetched but **excluded**: it is vendor-operated by a competitor, the page is undated, and no Pinecone figure was used | 18 / 18 / 17 |
| 2026-10-16 | cross-window | WebSearch `Pinecone Nexus KnowQL launch 2026 news` | Returned pinecone.io event pages, an aggregator (autobound.ai) and a personal blog. All were treated as E0 and not used | unknown / 10 / 10 |
| 2026-10-16 | cross-window | WebSearch `Pinecone vector database 2026 siliconangle OR techcrunch OR theregister Nexus knowledge engine` | No outlet coverage returned (only vendor event pages and an aggregator), so outlet tag pages were fetched directly instead | unknown / 10 / 10 |
| 2026-10-16 | cross-window (critical) | WebSearch `Pinecone Systems 2026 layoffs OR acquisition OR sale OR funding vector database startup` | No 2026 layoff, sale or funding report found. The Calcalist article (31.08.25, citing The Information on a possible sale) was read raw and used as **pre-window baseline only**. 2023 funding articles and Blind/TrueUp pages were not used | unknown / 9 / 8 |
| 2026-10-16 | cross-window | `GET https://techcrunch.com/tag/pinecone/`, `https://www.theregister.com/Tag/Pinecone/` (404), `https://venturebeat.com/tag/pinecone/` (**HTTP 429**), `https://www.prnewswire.com/news/pinecone/` (404) | The TechCrunch tag page lists only unrelated recent stories, and no in-window Pinecone story was found. VentureBeat was **inaccessible** (rate-limited) and not retried. PR Newswire was not used because the vendor newsroom carries the same releases | — |

## Inclusion, deduplication and conflicts

- **Included:** 36 rows (Apr 2, May 6, Jun 7, Jul 4, Aug 9, Sep 6, Oct 2). Every row cites a URL that was fetched as raw text or queried by API. No row relies on a search snippet alone.
- **Duplicate groups:**
  - `075-008`: Marketplace preview (May 5) and Marketplace end of life (Aug 31).
  - `075-006`: FTS public preview (May 4) and FTS GA (Sep 2).
  - `075-016`: Nexus public preview (vendor) and SiliconANGLE's report of it.
  - `075-020`: Nexus GA blog and Nexus GA press release (one event, two vendor documents).
- **Empty months:** none. April (partial) and October (partial) have the fewest rows (2 each). No in-window independent news coverage was found for April, May, August, September or October.
- **Date conflicts recorded, not resolved:**
  - Regions: May 1 (changelog), May 4/5 (press), May 8 (launch post).
  - FTS GA: Sep 2 (changelog), Sep 9 (blog).
  - BYOC GA: Aug 25 (changelog), Sep 23 (blog).
  - Builder: May 4 (changelog), May 6 (blog).
  - FTS shown as "generally available" on May 7 in the May 4 launch post, but as preview in the changelog and the May 7 blog.
  - Jun 18 incident: displayed post times are Jun 18, but API update timestamps are Jun 22.
  - Release vs registry times (for example, Node 8.0.0: npm 18:51Z, GitHub 21:29Z; Python 9.0.0: PyPI 11:05Z, GitHub 12:03Z).
- **Figure conflicts:**
  - Nexus GA cost reduction for GPT-5.5: 77% (blog) vs 74% (press release).
  - Builder namespaces per index: 100 (changelog) vs 1,000 (blog).
  - Token reduction claims: "up to 90%" (May 4), "95%+" (Jun 3), "more than 90%" (Aug 6), ">92%" (AskData, Jun 2).
  - Customer and developer counts: 9,000+ / 800,000+ (May 4) vs 10,000 / 1M (Aug 6 and Aug 26).
- **Figures confirmed against raw text** (grep of extracted page text or API JSON):
  - DRN "77-97%".
  - Launch post "800,000+", "9,000+", "85%", "50–60%", "above 90%", "30x", "up to 90%".
  - Builder "$20", "10 indexes", "1,000 namespaces" (blog) and "100 namespaces … (up from 20)" (changelog).
  - Import "$1/GB" → "$0.25/GB" and "$250"; egress allowances "1 GB / 10 GB / 100 GB".
  - Rerank "$2.00 per 1,000".
  - Python v9 "3.3×", "~17×", "~210 ms to ~45 ms", "3 runtime dependencies".
  - Nexus PP "F1 Score 95%" and "20 questions".
  - Nexus GA "97 tasks", "$1.45 … $0.53", "24.6% / 55.1%", "77%", "12% more accuracy", "80%".
  - Press release "46.4%", "47.4%", "74%".
  - Namespaces "1,000,000" (Enterprise); migration "500 million".
  - Agent-API post "three cold trials", "median 6 turns", "$0.30".
  - CEO post "above 130%", "roughly 40%", "more than 60%".
  - darryl-ruggles "61ms", "672ms", "200 samples", "50K".
  - Every release timestamp from `gh api`, PyPI and npm.
  - All of these remain **vendor or press statements**, not verified measurements.
- **Not every figure on every page was checked.** Figures in pages used only as context (Sparse V3, AskData, EA benchmarks) were spot-read, not systematically verified.

## Untrusted content and embedded agent-directed text

- Pages were treated as data. A grep of all fetched pages for agent-addressed phrasing ("if you are an AI/LLM/agent", "instructions for AI", "note to LLM") found no matches.
- Two pieces of agent-oriented text were seen and logged, and **not acted on**:
  - Pinecone's Markdown docs (`/guides/nexus/overview.md`) begin with a block telling the reader to "Fetch the complete documentation index at … llms.txt … before exploring further". This is a documentation-navigation hint. `llms.txt` had already been fetched for the product map, independently of that hint.
  - Vendor posts and READMEs contain install commands (`npx skills add pinecone-io/skills`, `npx skills add https://github.com/pinecone-io/cultivar …`, `curl -fsSL https://pinecone.io/install.sh | sh`). **None was executed.**
- Search-tool summaries were treated as leads only.

## Missing, inaccessible or not attempted

- VentureBeat (HTTP 429), and Reuters, Bloomberg and The Information originals (not attempted).
- `pinecone-io/knowql-spec` (404).
- Any Nexus/τ-Knowledge harness code (only the fork's existence was checked).
- Pinecone terms of service, DPA and data-processing regions for Nexus/BYOC.
- Postmortems for any in-window incident (none published on the status page).
- Wayback snapshots of mutable pages as of 2026-10-12.
- Filing-level corporate records. SEC/EDGAR was deliberately not contacted.
- No product was executed, no account was created, no paywall was bypassed and no energy was measured.
- **Reproduction:** re-run the requests above with UTC timestamps and save raw HTML hashes. Before any row is promoted beyond provisional status, an independent human should spot-check:
  - the Nexus GA rows (CI2026-075-020/021) against the τ-Knowledge leaderboard;
  - the Builder namespace conflict (005);
  - the incident row (015);
  - two SDK rows against PyPI/npm.
