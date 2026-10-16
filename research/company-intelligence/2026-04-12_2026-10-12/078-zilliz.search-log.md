# Zilliz (078) — provisional source-query and inclusion log

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** This log accompanies the [report](078-zilliz.md) and [event ledger](078-zilliz.events.csv) for [#146](https://github.com/MSKazemi/github-trending-1000-study/issues/146). Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

**Window:** 2026-04-12…2026-10-12 inclusive (UTC dates). **Accessed:** 2026-10-16.

**Method:**
- Official pages were fetched as raw HTML with `curl`, using the generic `Mozilla/5.0` User-Agent. No personal identifier, email or credential was sent to any site.
- Text was extracted locally and checked with `grep`.
- Release dates and licences came from `gh api`, the PyPI JSON API and the npm registry.
- Independent coverage came from the Hacker News Algolia API and two web searches.
- Every number, version, date and quote in a ledger row was confirmed against raw text or API JSON, except where the row says otherwise.

**This is not exhaustive retrieval.** Search-engine result totals were not exposed and are recorded as unknown, not zero. No page snapshots or hashes were archived in the repository, and pages may change after access.

## Query and source log by segment

| Date | Segment | Exact query or source request | Opened / decision | Found / screened / excluded |
|---|---|---|---|---|
| 2026-10-16 | all | `GET https://zilliz.com/`, `/sitemap.xml` (+ `sitemap-0..8.xml`), `/blog`, `/news` | Blog index embeds `__NEXT_DATA__` with 654 posts and display dates. All sitemap `lastmod` values for blog URLs were 2026-10-15 (build time), so they were not used as publication dates. `/rss.xml` and `/blog/rss.xml` returned 404. `/blog?page=2` returned page 1 content | 16 in-window blog posts; 4 in-window company-news items |
| 2026-10-16 | all | `GET https://docs.zilliz.com/docs/release-notes` and `/release-notes-2604`, `-2605`, `-2606`, `-2607`, `-2609` | Changelog summary plus monthly pages read | Apr 11 (pre-window), Apr 27, May 7/9, May 13, Jun 3, Jun 17, Jun 24, Jul 6, Jul 15, Jul 30, Aug 3, Aug 6, Sep 3. No August monthly page exists in the sidebar |
| 2026-10-16 | all | `gh api repos/milvus-io/milvus/releases`; `/security-advisories`; release bodies for v3.0-beta, v3.0.0, v3.0.1, v3.0.2, v2.6.16, v2.6.25 | 3.0-beta May 9; 3.0.0 Jul 29; 3.0.1 Sep 9; 3.0.2 Sep 20; 2.6.15–2.6.25; client/v3.0.0 Sep 18. The v2.6.25 body read "Release note is coming soon." | 23 releases since 2026-03-15; 1 in-window repo advisory |
| 2026-10-16 | all | `gh api /advisories?ecosystem=go&affects=github.com/milvus-io/milvus`; `/advisories/GHSA-jh6h-v6mp-h22v`; `/advisories/GHSA-jh4h-22hq-x74p` | CVE-2026-10814 (published 2026-06-04) included. The GHSA-jh4h global endpoint returned **404** (repo-level advisory only, no CVE at access). Keyword query `keywords=milvus` returned unrelated advisories and was discarded | 3 advisories (2 pre-window) |
| 2026-10-16 | all | `GET https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch=milvus` | **HTTP 429** (rate limit): inaccessible, not used | — |
| 2026-10-16 | all | `gh api orgs/zilliztech/repos` and `orgs/milvus-io/repos` sorted by creation | New in-window repos: mfs (Apache-2.0), zilliz-launchpad, gemini-cli-extension (NOASSERTION), milvus-catalog (no licence), zilliz-cloud-onboarding (no licence), adk-milvus, vortex/lance forks, dsh-milvus, milvus-io/talon | 12 listed; 2 ledgered (adk-milvus, dsh-milvus) |
| 2026-10-16 | all | `gh api repos/<r>/releases` for zilliztech/{claude-context, VectorDBBench, attu, mfs, zilliz-cli, deep-searcher, memsearch, GPTCache, milvus-backup, dsh-milvus} and milvus-io/{pymilvus, milvus-lite, milvus-sdk-node, milvus-sdk-go, milvus-sdk-java} | claude-context, deep-searcher and GPTCache had **no** in-window GitHub release (GPTCache last 0.1.44 on 2024-08-01) | — |
| 2026-10-16 | all | `gh api repos/zilliztech/attu/license` and `commits?path=LICENSE` | LICENSE says proprietary from 2.6.0; changed 2025-10-27 | licence conflict ledgered |
| 2026-10-16 | all | PyPI JSON: pymilvus, zilliz-cli, milvus-lite, memsearch, vectordb-bench; npm: @zilliz/claude-context-mcp, @zilliz/claude-context-core, @zilliz/milvus2-sdk-node | Upload times used as independent checks | — |
| 2026-10-16 | all | `GET https://status.zilliz.com/api/v2/incidents.json`, `/history.rss`, `/incidents/8j0lx6wqvw99` | One in-window incident (Jul 22, posted Jul 24); 3 older incidents | 4 / 4 / 3 pre-window |
| 2026-10-16 | all | `GET https://milvus.io/blog`, `/blog/<slug>.md` | **302 to itself with a `milvus_challenge` cookie** (bot challenge). Treated as an access gate and not passed. Inaccessible as HTML | — |
| 2026-10-16 | all | `gh api repos/milvus-io/community/commits?path=blog/en&since=2026-04-12&until=2026-10-13`; added files fetched via `contents/` (raw) | Apache-2.0 source markdown with `date:` frontmatter used as the citable first-party copy | 22 new blog files |
| 2026-10-16 | Apr 12–30 | Zilliz blog `inside-zilliz-two-claude-code-skills` (Apr 24), `zilliz-cloud-now-available-in-aws-asia-pacific-seoul` (Apr 28); Milvus blog `interview-with-rabitq-authors-…` (Apr 17), `claude-context-reduce-claude-code-token-usage` (Apr 30) | 4 rows; zilliz-cli v1.1.0 row from GitHub | Excluded: `notion-vector-search-next-problem` (Apr 16, opinion); Milvus blog `vector-graph-rag-without-graph-database`, `anthropic-managed-agents-memory-milvus`, `hermes-agent-learning-loop-milvus-hybrid-search`, `deepseek-v4-vs-gpt-55-vs-qwen36…`, `how-robobrain-builds-longterm-robot-memory-with-milvus` (tutorials/model comparisons) |
| 2026-10-16 | Apr 12–30 | PR Newswire MarketsandMarkets release (linked from the newsroom) | Included; date conflict with the newsroom (Apr 30) recorded | — |
| 2026-10-16 | May | Zilliz blog `from-vector-database-to-vector-lakebase` (May 11), `zilliz-cloud-on-demand` (May 21) | On-demand row included; May 11 used as a date-conflict source | Excluded: `we-spent-8-years…` (May 12), `vector-lakebase-ai-data-silo` (May 14), `why-we-built-vector-lakebase` (May 26) as positioning essays; Milvus blog `claude-code-context-management-tools` (May 7, listicle) |
| 2026-10-16 | June | Zilliz blog `why-we-built-loon…` (Jun 5), `vdbbench-adds-cost-aware…` (Jun 10); news `zilliz-launches-vector-lakebase…` (Jun 10), `pr-loon-…` (Jun 29); Milvus blog `attu-3-0-beta` (Jun 11) | 5 rows (+ CVE and mfs rows from GitHub) | Excluded: `what-is-a-vector-lakebase` (Jun 2), `stop-building-ai-data-infra…` (Jun 10), `getting-started-with-zilliz-cloud` (Jun 26), `databricks-data-ai-summit-2026-data-layer` (Jun 30); Milvus blog `25-million-vectors-1gb-memory-milvus-flat` (Jun 3), `when-ai-agents-do-the-work…` (Jun 21) |
| 2026-10-16 | June | web search `Zilliz "Vector Lakebase" June 2026` | Results were the vendor page, syndicated copies (BigDATAwire, TechNode/PRNAsia, Las Vegas Sun, theatdb) and a Malay outlet. BigDATAwire **HTTP 403**; Las Vegas Sun **HTTP 410**. The search tool's summary mentioned an HPCwire "June 22" date: **unconfirmed (E0), not used** | unknown / 10 / 10 |
| 2026-10-16 | July | Zilliz blog `migrate-self-managed-milvus-to-zilliz-cloud` (Jul 16); Milvus blog `open-source-claude-tag-mfs` (Jul 2), `recover-milvus-data-after-etcd-corruption` (Jul 22), `announcing-milvus-3-…` (frontmatter Jul 27; publish commit Jul 29) | 3 rows + Milvus 3.0 release row | Excluded: `build-multimodal-search-3d-assets-tripo-zilliz-cloud` (Jul 2, community tutorial); `force-merge-compaction-milvus-qps` (Jul 1); `milvus-snapshots` (Jul 30, feature explainer) |
| 2026-10-16 | Jul–Aug | web search `Milvus 3.0 Zilliz siliconangle OR thenewstack OR theregister OR infoworld 2026` | No SiliconANGLE/The New Stack/The Register/InfoWorld result. A Business Wire copy (swoknews AP feed) returned a 1,122-byte page without article text: **inaccessible**; its "Jul 31" date is snippet-only (E0). Wikipedia, techintelpro and traeai results were not used (secondary/aggregator) | unknown / 9 / 9 |
| 2026-10-16 | August | news `milvus-3-0-lake-native-vector-database` (newsroom Aug 01), `vdbbench-cost-aware-vector-database-benchmarking` (Aug 5) | Both included as same-event rows | Milvus blog `milvus-3-0-regex-filtering` (Aug 5), `from-retrieval-to-structured-results…` (Aug 7), `milvus-3-0-structarray` (Aug 19), `milvus-3-0-external-collection` (Aug 24) excluded as feature explainers. **No Zilliz blog post dated Aug–Oct** in the index |
| 2026-10-16 | September | Zilliz Cloud Sep notes; zilliz-cli v1.5.0, Attu v3.0.0/3.0.1, VectorDBBench v2.0.0, memsearch v0.4.21, Milvus v3.0.1/v3.0.2/v2.6.24/v2.6.25 bodies | 7 rows | No Zilliz newsroom item in September |
| 2026-10-16 | Oct 1–12 | Milvus blog `jev-vs-llms-in-agentic-search` (Oct 9), `jevs-cheap-decisions-make-semantic-caching-worth-another-try` (Oct 12) | 2 rows | No changelog entry, release or status incident found Oct 1–12. Milvus 3.0.3 (Oct 14) and milvus-lite 3.2.2 (Oct 13) are post-window |
| 2026-10-16 | cross-window | HN Algolia `search_by_date` with `query=Zilliz`, `query=Milvus`, `query=claude-context` (`tags=story`) and `query=Milvus` (`tags=comment`), `created_at_i` 1775952000–1792022400 | 12, 4, 2 and 14 hits. Zilliz/Milvus stories were mostly vendor blog links with 1–6 points. Unrelated: "Zillionaires" (35 points), "Zillion Encodings of NOP". One critical comment (2026-04-22, item 47868969) in a 3-point text post "We mapped unauthenticated Vector DBs exposing corporate AI data" cited the pre-window Milvus auth CVEs: **E0 sentiment, not ledgered**; commenter not identified here | — |
| 2026-10-16 | baseline | news `zilliz-achieves-aws-agentic-ai-specialization` (Dec 1, 2025), `zilliz-cloud-is-now-available-in-the-new-aws-marketplace-…` (Jul 16, 2025); `https://zilliz.com/about`; `https://lfaidata.foundation/projects/milvus/` | Pre-window context only | — |

## Inclusion, deduplication and conflicts

**Included:** 35 rows (Apr 6, May 3, Jun 6, Jul 8, Aug 3, Sep 7, Oct 2). Every row cites a URL that was fetched as raw text or queried by API. No row relies on a search snippet alone. Milvus blog rows cite the GitHub source file, because the milvus.io HTML was challenge-gated.

**Duplicate groups:**
- `078-lakebase`: changelog May 7, on-demand blog, press release Jun 10, billing start Jul 15.
- `078-milvus3`: 3.0-beta, 3.0.0 release, 3.0 press release, 3.0.1.
- `078-vdbbench`: blog Jun 10, PR Aug 5, v2.0.0 Sep 10.
- `078-attu`: licence-conflict blog, 3.0.0 release.
- `078-mfs`: v0.4.0, Open Tag.
- `078-zilliz-cli`: v1.1.0, v1.5.0.
- `078-agent-integrations`: adk-milvus, dsh-milvus.
- `078-jev`: Oct 9 and Oct 12 posts.
- `078-loon`: one row; the Jun 29 press release is noted in its limitation.

**Date conflicts recorded, not resolved:**
- Vector Lakebase launch: May 7 / May 9 / May 11 / Jun 10.
- Milvus 3.0: Jul 16 (PR dateline), Jul 27 (blog frontmatter), Jul 29 (GitHub release, blog publish commit 2026-07-29T11:41Z), Jul 31 (Business Wire, E0 snippet), Aug 1 (newsroom).
- MarketsandMarkets: Apr 22 (PR Newswire) vs Apr 30 (newsroom).
- Seoul region: Apr 27 (changelog) vs Apr 28 (blog).
- pymilvus 3.0.0 PyPI 2026-05-07 vs server 3.0-beta 2026-05-09.
- Status incident Jul 22 posted Jul 24.

**Figure and identity conflicts:**
- Milvus star count: "over 43,000" (Apr 22), "44,000+" (Jun 29), "45,000+" (Aug 5); GitHub API showed 46,389 at access.
- James Luan is "Co-founder and CTO" (Milvus 3.0 PR) vs "VP of Engineering" (VDBBench PR).
- zilliz-cli: PyPI 1.0.2 vs GitHub zilliz-v1.5.0.

**Rights conflict:** Attu is "open-source" in the Milvus blog but proprietary per its LICENSE (≥2.6.0).

**Figures confirmed against raw text** (grep of saved text or API JSON):
- 39.4% / 36.1% (claude-context); 6x/8x quoted TurboQuant claims; "did not outperform our internal RaBitQ version in most of the cases" (RaBitQ interview).
- 43,000 stars / 10,000 deployments / Apr 22, 2026 10:30 ET (PR Newswire); 31 regions (Seoul).
- 16,384 → 1,000,000 top-K (changelog); $7,000 / $10,800 / under $500 (on-demand); 1,000+ / 100–500 / 10–50 QPS, $318 / $4,937, >10,000 enterprises, >30 regions (Lakebase PR).
- 9.4 MB → 0.07 MB, "roughly 135 times", 3 million rows / 128-dim / 256 readers, BM25 "roughly 3 times smaller", roadmap sentence (Milvus 3.0 blog).
- $9.50 / $302 / $1,180, May 10, 2026, us-west-2 (VDBBench blog); "more than 30 vector databases", "demonstration, not a ranking", "VP of Engineering" (VDBBench PR); "Co-founder and CTO", "July 16, 2026" dateline, "Aug 01, 2026" (Milvus 3.0 PR).
- 25 ms vs 3,112 ms (migration).
- 09:00–10:07 UTC and posting time 2026-07-24T20:11Z (status).
- CVSS 4.5 and 6.5, CWE-22/863, fix versions 2.6.25 / 3.0.3, ImportBinlog (advisories).
- "silent data loss during mix compaction" #52200 and #52554 (3.0.1 notes); hidden ACL commands (zilliz-cli 1.5.0).
- 364 / 1 / 99.7% / 72.1%, 401 / 477 / 45.7% / 79.4%, ">8,200 GitHub stars" (GPTCache post).
- All release and upload timestamps (GitHub API, PyPI, npm).

All of these remain **vendor or press statements**, not verified measurements.

**Untrusted-content note:** fetched pages were treated as data. No page was found to contain instructions directed at an AI agent. The milvus.io challenge redirect was not circumvented. Search-tool summaries were treated as leads only; one summary's claimed HPCwire date was not confirmed and was not used. Personal data was minimized: the external reporter credited in GHSA-jh4h, commit-message email addresses in milvus-io/community, and HN commenter handles were seen but deliberately not copied.

## Missing, inaccessible or not attempted

**Inaccessible or not attempted:**
- milvus.io HTML (challenge); NVD API (429); BigDATAwire (403); Las Vegas Sun copies (410); Business Wire syndication (no article text).
- Zilliz Cloud pricing pages for the on-demand rates; an August monthly release-notes page; a Zilliz Cloud status history before 2025 beyond the 4 incidents the API returns.
- Independent trade-press articles: none found by two searches; the web-search budget was nearly exhausted, so this is a coverage limit, not a null finding.
- Third-party reproductions of VDBBench; customer-side confirmations; investor/funding records; filing-level corporate data; archived (Wayback) copies of mutable pages.
- No product was executed, no account was created, no paywall was circumvented, and no energy was measured.

**Reproduction:** Re-run the requests above with UTC timestamps and save raw-HTML hashes. Then have an independent human spot-check:
- the licence-conflict rows (CI2026-078-014, 029);
- both advisory rows (010, 033);
- the Milvus 3.0 date cluster (008, 023, 024);
- the Vector Lakebase date cluster (007, 012);

before any evidence is promoted beyond provisional status.

## Spot-check access note (2026-10-16)

- status.zilliz.com robots.txt (`User-agent: *`) disallows `/api/`. The status API request above was made against that rule. The independent spot-check used only the incident HTML page and `/history.rss`, which show 2026-07-22 timestamps. The 2026-07-24T20:11Z posting time is therefore unverified (row 022).
