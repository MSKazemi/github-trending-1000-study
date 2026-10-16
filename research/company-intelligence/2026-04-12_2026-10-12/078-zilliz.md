# Zilliz — provisional six-month technology intelligence screen (078)

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** This report, its [event ledger](078-zilliz.events.csv) and [search log](078-zilliz.search-log.md) are an AI-assisted first-pass documentary source screen. No qualified human has reviewed them. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open. Nothing here is a verified task outcome, an adoption measure or an endorsement.

- **Company watchlist ID:** 078
- **Research issue:** [#146](https://github.com/MSKazemi/github-trending-1000-study/issues/146); evidence corpus link [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56) (no `NEWS-YYYY-NNNN` item minted here; candidates are listed in §9).
- **Ownership and product boundaries (as of 2026-10-12):** Zilliz (Zilliz Inc. per its own licence notice "Copyright © 2025 ZILLIZ INC."), headquartered in Redwood City, California per its [about page](https://zilliz.com/about). It is privately held. No parent company or acquisition of Zilliz was found in the window. Zilliz created **Milvus**, which it contributed to the LF AI & Data Foundation in January 2020; Milvus graduated in June 2021 ([LF AI & Data project page](https://lfaidata.foundation/projects/milvus/)). Milvus is Apache-2.0 and foundation-hosted. **Zilliz Cloud** is Zilliz's proprietary managed service, which uses the proprietary Cardinal index engine. Investor and funding details were not verified in-window. Filing-level corporate verification was **not** performed.
- **Product URL and company newsroom:** [zilliz.com](https://zilliz.com/), [newsroom](https://zilliz.com/news), [blog](https://zilliz.com/blog), [Zilliz Cloud changelog](https://docs.zilliz.com/docs/release-notes), [status page](https://status.zilliz.com/history), [milvus-io/milvus](https://github.com/milvus-io/milvus) (releases and security advisories), [zilliztech GitHub org](https://github.com/zilliztech), Milvus blog source in [milvus-io/community](https://github.com/milvus-io/community/tree/master/blog/en).
- **Analysis window:** 2026-04-12 to 2026-10-12 inclusive; accessed 2026-10-16.
- **Researcher / factual reviewer / review date:** AI-assisted screen / **pending** / **pending**.
- **Status:** screened (provisional). The ledger has 35 rows covering all seven calendar segments.
- **Source coverage:** We used the Zilliz blog index (via its embedded page data), the newsroom, the Zilliz Cloud changelog and its monthly release-notes pages, the status-page API, and GitHub releases and advisories through `gh api`. Release dates came from the PyPI and npm registries. Milvus blog source markdown was read through the GitHub API, because milvus.io answers with a cookie challenge redirect, which we did not pass. We also ran Hacker News Algolia queries and two web searches. NVD returned HTTP 429. BigDATAwire returned 403. Syndicated wire copies did not render. See the [search log](078-zilliz.search-log.md).

## 1. Search and inclusion audit

This is a summary. Exact requests, opened URLs and exclusions are in the [search log](078-zilliz.search-log.md). Web-search engine result totals were not exposed, so they are recorded as **unknown**, not zero.

| Search run UTC | Site/engine | Full query and dates | Found | Screened | Included | Excluded/why | Coverage limitation |
|---|---|---|---:|---:|---:|---:|---|
| 2026-10-16 | zilliz.com blog index (`__NEXT_DATA__`) + newsroom | all posts with display date 2026-04-12..10-12 | 16 blog + 4 company-news items | 7 blog + 4 news opened (+2 pre-window news) | 9 rows | opinion/explainer/community posts (log) | blog index shows no post after 2026-07-16; sitemap `lastmod` is a build time, not a publication date |
| 2026-10-16 | milvus-io/community commits (`blog/en`) | commits 2026-04-12..10-13 | 22 new blog files | 8 read in full or in part | 7 rows | model comparisons, tutorials (log) | milvus.io HTML not read (challenge) |
| 2026-10-16 | Zilliz Cloud changelog + monthly notes | Apr, May, Jun, Jul, Sep 2026 pages | ~20 dated items | all | 4 rows (+1 used as check) | minor items folded into report | no August monthly page; Aug items only in changelog summary |
| 2026-10-16 | GitHub API (releases, advisories, repos) | milvus, pymilvus, SDKs, attu, VectorDBBench, zilliz-cli, mfs, memsearch, claude-context, GPTCache, org repo lists | ~150 releases | all listed | 13 rows (incl. 2 advisories, 2 repo records) | routine 2.6.x patches and SDK point releases | release notes not read for every patch |
| 2026-10-16 | PyPI / npm JSON | pymilvus, zilliz-cli, milvus-lite, memsearch, vectordb-bench; @zilliz/claude-context-mcp, @zilliz/milvus2-sdk-node | — | all | used as checks | — | — |
| 2026-10-16 | PR Newswire + status API | MarketsandMarkets release; Statuspage incidents JSON | 1 / 4 incidents | all | 2 rows | 3 incidents pre-window | status history shows few incidents |
| 2026-10-16 | HN Algolia API | `Zilliz`, `Milvus`, `claude-context` (stories); `Milvus` (comments) | 12 / 4 / 2 / 14 | all | 0 rows (context only) | vendor-submitted links with 1–6 points; one critical comment thread (E0) | HN is not representative |
| 2026-10-16 | web search (2 queries) | Vector Lakebase June 2026; Milvus 3.0 trade press | unknown | ~19 | 0 rows | syndicated press-release copies only | no independent trade analysis found |

## 2. Verified company/product identity and baseline

Zilliz builds vector-search infrastructure. It has three parts. (a) **Milvus**, an open-source (Apache-2.0) vector database hosted by LF AI & Data. Milvus also has client SDKs (pymilvus, Node, Java, Go) and Milvus Lite. (b) **Zilliz Cloud**, a proprietary managed service with Serverless, Dedicated and BYOC options. Its proprietary Cardinal engine is not part of open-source Milvus ([migration post](https://zilliz.com/blog/migrate-self-managed-milvus-to-zilliz-cloud)). (c) A set of developer and agent tools under `zilliztech`. These include VectorDBBench (MIT), GPTCache (MIT), claude-context (MIT), memsearch (MIT), mfs (Apache-2.0), zilliz-cli (Apache-2.0), and the Attu console.

Attu's licence matters for reuse. Since 2.6.0 it is **proprietary**: the [LICENSE](https://github.com/zilliztech/attu/blob/main/LICENSE) was changed on 2025-10-27, and only versions ≤2.5.12 remain Apache-2.0.

Pre-window baseline (context only, not counted):
- Milvus 2.6 launch (June 2025).
- Critical Milvus advisories [CVE-2025-64513](https://github.com/milvus-io/milvus/security/advisories/GHSA-mhjq-8c7m-3f7p) (proxy authentication bypass, 2025-11) and [CVE-2026-26190](https://github.com/milvus-io/milvus/security/advisories/GHSA-7ppg-37fh-vcr6) (unauthenticated metrics-port REST API, 2026-02-11).
- milvus-skill and zilliz-skill repositories (created 2026-03-24/25).
- Zilliz CLI and Agent Skills blog post (2026-04-01).
- zilliz-cli v1.0.0 GitHub release (2026-04-09).

**Post-window, excluded:** Milvus v3.0.3 (2026-10-14), which carries the 3.x fix for the September advisory, and milvus-lite 3.2.2 (2026-10-13).

## 3. Month-by-month discoveries (six calendar months + partial endpoints)

| Month | Announcements/changes | Primary URLs | Independent reporting | Notes or no-result limitations |
|---|---|---|---|---|
| 2026-04-12..30 | zilliz-cli v1.1.0 (Apr 14); RaBitQ/TurboQuant dispute interview (Apr 17); MarketsandMarkets "Stars Company" (Apr 22); agent-skills explainer (Apr 24); Seoul region (Apr 27/28); claude-context 39.4% token claim (Apr 30) | [CLI release](https://github.com/zilliztech/zilliz-cli/releases/tag/zilliz-v1.1.0), [Seoul](https://zilliz.com/blog/zilliz-cloud-now-available-in-aws-asia-pacific-seoul) | none found. One critical HN comment (Apr 22) on exposed vector DBs, E0 | Notion opinion post (Apr 16) excluded |
| 2026-05 | Vector Lakebase repositioning and Milvus 3.0 private review in Zilliz Cloud (May 7/9/11); Milvus 3.0-beta (May 9) with pymilvus 3.0.0 (May 7); On-Demand cost case (May 21) | [changelog](https://docs.zilliz.com/docs/release-notes), [3.0-beta](https://github.com/milvus-io/milvus/releases/tag/v3.0-beta), [on-demand](https://zilliz.com/blog/zilliz-cloud-on-demand) | none | BYOC multi-dataplane (May 13) noted only. Opinion posts May 12/14 excluded |
| 2026-06 | CVE-2026-10814 (Jun 4); Loon storage engine (Jun 5, PR Jun 29); Vector Lakebase PR (Jun 10); VDBBench cost leaderboard (Jun 10); Attu 3.0 beta called "open-source" (Jun 11); mfs v0.4.0 (Jun 17) | [GHSA-jh6h](https://github.com/advisories/GHSA-jh6h-v6mp-h22v), [Lakebase PR](https://zilliz.com/news/zilliz-launches-vector-lakebase-unified-data-platform-for-ai), [VDBBench](https://zilliz.com/blog/vdbbench-adds-cost-aware-benchmarking-for-vector-databases) | only syndicated copies of the press releases (not independent) | Nullable vectors (Jun 3), backup scheduling (Jun 24) and version-pinned restore (Jun 17) noted only |
| 2026-07 | Open Tag on MFS (Jul 2); BYOC-I on GCP (Jul 6); on-demand/external-volume charges begin (Jul 15); adk-milvus (Jul 15); migration latency claim (Jul 16); etcd-corruption recovery write-up (Jul 22); control-plane incident (Jul 22, posted Jul 24); **Milvus 3.0.0 GA (Jul 29)** | [3.0.0](https://github.com/milvus-io/milvus/releases/tag/v3.0.0), [status](https://status.zilliz.com/incidents/8j0lx6wqvw99) | HN submissions of the 3.0 blog (6 and 4 points) | Snapshots blog (Jul 30) not ledgered |
| 2026-08 | Milvus 3.0 PR (newsroom Aug 1); VDBBench PR (Aug 5); dsh-milvus (Aug 18) | [Milvus 3.0 PR](https://zilliz.com/news/milvus-3-0-lake-native-vector-database), [VDBBench PR](https://zilliz.com/news/vdbbench-cost-aware-vector-database-benchmarking) | Business Wire copy seen only as a snippet (E0) | London (AWS, Aug 3) and Tokyo (GCP, Aug 6) regions in the changelog; Milvus 3.0 feature explainers (Aug 5/7/19/24) excluded; **no Zilliz blog post** after Jul 16 |
| 2026-09 | Zilliz Cloud custom roles/SCIM; Org Owners lose implicit project access (Sep 3); zilliz-cli v1.5.0 hidden ACL commands (Sep 3); Attu 3.0.0 (Sep 3); Milvus 3.0.1 silent-data-loss fix (Sep 9); VectorDBBench 2.0.0 (Sep 10); memsearch 0.4.21 (Sep 24); **GHSA-jh4h-22hq-x74p** import RBAC bypass (Sep 27) | [Sep notes](https://docs.zilliz.com/docs/release-notes-2609), [3.0.1](https://github.com/milvus-io/milvus/releases/tag/v3.0.1), [advisory](https://github.com/milvus-io/milvus/security/advisories/GHSA-jh4h-22hq-x74p) | none | v2.6.25 (Sep 29) release notes said "coming soon" at access |
| 2026-10-01..12 | Jev decision model in agentic search (Oct 9); GPTCache false-hit retrospective (Oct 12) | [Jev vs LLMs](https://github.com/milvus-io/community/blob/master/blog/en/jev-vs-llms-in-agentic-search.md), [GPTCache](https://github.com/milvus-io/community/blob/master/blog/en/jevs-cheap-decisions-make-semantic-caching-worth-another-try.md) | none | no Zilliz Cloud changelog entry, release or status incident found Oct 1–12 |

## 4. Dated event evidence and capabilities

Full row detail is in the [CSV](078-zilliz.events.csv) (35 rows, IDs `CI2026-078-001`…`035`; per month: Apr 6, May 3, Jun 6, Jul 8, Aug 3, Sep 7, Oct 2). Highlights:

| Event ID | Published UTC / underlying event date | Claim or observed feature | Availability and limitations | Source link (type) | Independent check | E0–E4 working grade |
|---|---|---|---|---|---|---|
| CI2026-078-006 | 2026-04-30 | claude-context cut Claude Code tokens by 39.4% and tool calls by 36.1% | Vendor benchmark; npm releases stop 2026-06-22 | [Milvus blog source](https://github.com/milvus-io/community/blob/master/blog/en/claude-context-reduce-claude-code-token-usage.md) | npm registry dates only | E1 |
| CI2026-078-007/012 | 2026-05-07 … 2026-06-10 | Vector Lakebase public preview | Four different "launch" dates | [changelog](https://docs.zilliz.com/docs/release-notes), [PR](https://zilliz.com/news/zilliz-launches-vector-lakebase-unified-data-platform-for-ai) | monthly notes 2026-05-09 | E2 / E1 |
| CI2026-078-010 | 2026-06-04 (patch 2026-06-02) | CVE-2026-10814: RBAC grantee ID uses truncated 64-bit MD5 | Low; local; Milvus ≤2.6.13 | [GHSA](https://github.com/advisories/GHSA-jh6h-v6mp-h22v) | [PR #50060](https://github.com/milvus-io/milvus/pull/50060) | E2 |
| CI2026-078-013 | 2026-06-10 (benchmark run 2026-05-10) | Vendor-run cost leaderboard of Zilliz Cloud vs Turbopuffer vs Pinecone | Vendor rates itself against competitors | [blog](https://zilliz.com/blog/vdbbench-adds-cost-aware-benchmarking-for-vector-databases) | open code, no third-party rerun found | E1 |
| CI2026-078-014/029 | 2026-06-11 / 2026-09-03 | Attu marketed as "open-source", but the LICENSE is proprietary from 2.6.0 | Rights contradiction | [blog source](https://github.com/milvus-io/community/blob/master/blog/en/attu-3-0-beta.md) | [LICENSE](https://github.com/zilliztech/attu/blob/main/LICENSE) | E2 (documentary conflict) |
| CI2026-078-022 | 2026-07-24 / 2026-07-22 | Control-plane authorization errors 09:00–10:07 UTC; rolled back | Posted retroactively | [status](https://status.zilliz.com/incidents/8j0lx6wqvw99) | status API | E2 |
| CI2026-078-023 | 2026-07-29 | Milvus 3.0.0 GA, Apache-2.0: External Collections, online schema evolution, SINDI sparse index | Internal performance figures | [release](https://github.com/milvus-io/milvus/releases/tag/v3.0.0) | PyPI pymilvus 3.0.1 same day | E2 |
| CI2026-078-030 | 2026-09-09 | Milvus 3.0.1 fixes "silent data loss during mix compaction" and revoked privileges staying effective | Affected versions not stated | [release](https://github.com/milvus-io/milvus/releases/tag/v3.0.1) | [PR #52200](https://github.com/milvus-io/milvus/pull/52200) | E2 |
| CI2026-078-033 | 2026-09-27 | Import privilege on one collection can read other collections' binlogs (CVSS 6.5) | Fixed 2.6.25 (Sep 29); 3.0.3 only on Oct 14 | [advisory](https://github.com/milvus-io/milvus/security/advisories/GHSA-jh4h-22hq-x74p) | [v2.6.25](https://github.com/milvus-io/milvus/releases/tag/v2.6.25) | E2 |
| CI2026-078-035 | 2026-10-12 | GPTCache false-hit problem conceded; Jev precision 99.7% vs reranker 45.7% on one test set | Vendor experiment | [blog source](https://github.com/milvus-io/community/blob/master/blog/en/jevs-cheap-decisions-make-semantic-caching-worth-another-try.md) | GPTCache last release 2024-08-01 | E1 |

**Feature inventory (vendor-documented, not exercised by us):**

| Area | In-window change | Class |
|---|---|---|
| Open-source engine | Milvus 3.0-beta → 3.0.0 → 3.0.1/3.0.2. Includes External Collections over Parquet/Lance/Iceberg/Vortex, Loon storage, Snapshots, Spark DataSource V2, online add/backfill/drop of fields, ORDER BY and aggregation, StructArray/multi-vector, SINDI sparse index, TEXT fields, nullable vectors, TTL and MinHash. The 2.6.x line continues in parallel (2.6.15–2.6.25) | shipped (Apache-2.0) |
| Managed service | Vector Lakebase public preview (on-demand search, external data lake search, tiered serving); BYOC multi-dataplane, BYOC-I on GCP, storage integrations, external volumes; new regions Seoul, London, Tokyo | preview / shipped, proprietary |
| Governance and security | Cluster Admin role, access logs (public preview), custom project roles + SCIM, role API, Org Owners no longer inherit project access; two in-window Milvus advisories | shipped / corrected |
| Agent tooling | zilliz-cli (14 in-window GitHub releases), milvus-skill / zilliz-skill, `generate-plugin` agent-skill output, claude-context (MCP), mfs, memsearch, Open Tag, adk-milvus, dsh-milvus, Attu built-in agent | mixed: OSS repos (MIT/Apache-2.0) and a proprietary console |
| Benchmarks | VDBBench cost cases and leaderboard; VectorDBBench 2.0.0 (MIT) | shipped; vendor-authored |
| Pricing | On-demand compute and external volumes billed from 2026-07-15; BYOC on-demand vCPU-minutes (Jul 30) | shipped |
| Licensing | Milvus/SDKs Apache-2.0; VDBBench, GPTCache, claude-context, memsearch MIT; Attu proprietary ≥2.6.0; `zilliz-cloud-onboarding` and `milvus-catalog` repos (created in window) show no licence via GitHub API | observed 2026-10-16 |

## 5. What the company says it intends to do

| Verbatim or close paraphrase of public direction (<=25 words per source quoted) | Link/date | Promised horizon | Status (planned, tentative, uncommitted) | Missing/contradictory context |
|---|---|---|---|---|
| "The Milvus roadmap builds on the 3.0 architecture with predicate pushdown for External Collections, external backfill, additional Spark operators, and support for more table formats" (Delta Lake, Apache Paimon) | [Milvus 3.0 blog, published 2026-07-29](https://github.com/milvus-io/community/blob/master/blog/en/announcing-milvus-3-lake-native-vector-search-and-a-more-powerful-retrieval-engine.md) | none stated | planned, no dates | 3.0.0 release notes list external backfill as already added; overlap not resolved |
| "Vector Lakebase is what we believe comes next: one data foundation where the same vectors can serve a production query …" (CEO quote) | [PR 2026-06-10](https://zilliz.com/news/zilliz-launches-vector-lakebase-unified-data-platform-for-ai) | none | strategic positioning (uncommitted) | Launch dated May 7, 9, 11 and Jun 10 in different first-party sources |
| "More vector lakebase features are on the way." | [Zilliz Cloud changelog, "Next releases"](https://docs.zilliz.com/docs/release-notes) | none | uncommitted | no list |
| `zilliz acl` commands "hidden … until the `/v2` ACL routes are published on the API gateway" | [zilliz-cli v1.5.0, 2026-09-03](https://github.com/zilliztech/zilliz-cli/releases/tag/zilliz-v1.5.0) | none | tentative | no date for route publication |
| Attu remains "the open-source management console for Milvus" | [Milvus blog 2026-06-11](https://github.com/milvus-io/community/blob/master/blog/en/attu-3-0-beta.md) | — | contradicted by the licence | proprietary LICENSE since 2.6.0 |

These are **company statements**, not forecasts we endorse.

## 6. Independent interpretation: direction and alternative scenarios (researcher's conditional 2027–2031 view)

| Hypothesis for 2027–2031 | Supporting observations | Rival explanations | Disconfirming signals | Confidence/unknowns |
|---|---|---|---|---|
| H1: Vector databases converge with lakehouse storage (open formats, zero-copy external tables) rather than remaining separate serving copies | Milvus 3.0 External Collections + Loon/Vortex; Zilliz rebrand to "Vector Lakebase"; roadmap adds Delta Lake/Paimon | Vendor repositioning for revenue (on-demand billing began Jul 15); lake-native performance claims are internal | Production users keep ingesting copies; External Collections stay read-only niche; no independent latency/cost replication by 2028 | low–moderate; no adoption denominator |
| H2: "Open-core drift": peripheral tools of OSS database vendors move to proprietary licences while the core remains open-source | Attu proprietary from 2.6.0 yet still marketed as open-source; proprietary Cardinal credited for managed-service gains | Commercial sustainability of a small console; Milvus core remains foundation-governed | Attu relicensed open; no further zilliztech tools relicensed | low; n=1 tool |
| H3: Vendor-authored, open-code benchmarks become the de facto comparison channel, with neutrality contested | VDBBench cost leaderboard compares the vendor with two competitors; PR calls it "vendor-neutral" | Open code allows community audit; vendor states it is "not a ranking" | Independent parties publish reproductions that diverge, or benchmark governance moves to a neutral body | moderate that vendor benchmarks persist; unknown on neutrality |
| H4: Vector-DB vendors use coding-agent context tooling (MCP servers, skills, memory layers) as a discovery funnel | claude-context, memsearch, mfs, Open Tag, adk-milvus, dsh-milvus, milvus-skill/zilliz-skill all appeared or iterated in window | These may be experiments with low sustained maintenance (claude-context npm stops Jun 22; GPTCache last release 2024) | Most repos stop releasing within 12 months, or no accepted-task gains appear in controlled tests | low; release counts ≠ use |
| H5: Authorization flaws in data-plane features (import/backup paths, privilege groups) remain the dominant Milvus security class | 2 in-window advisories plus a 3.0.1 privilege-revocation fix; pre-window auth bypasses | Disclosure volume reflects more scrutiny, not more defects | No RBAC/auth advisory in 2027 | low |

These are hypotheses for testing, not company strategy or fact.

## 7. Implications for the GitHub 1000 study

| M1–M7 construct | Possible observable effect | Study design to test it | Negative/null explanation | Measurement boundary |
|---|---|---|---|---|
| M1 AI coding-agent change | Agents get retrieval/memory sidecars (MCP code search, skill packs) instead of grep loops | Same frozen tasks with and without an indexed code-retrieval tool; count accepted patches | Token savings without any change in accepted tasks | Accepted tasks over all attempts; tokens recorded but not equated with energy |
| M2 accepted task quality | Vendor claims (39.4% fewer tokens; 99.7% cache precision) are about cost/precision, not correctness | Hidden acceptance tests, independent of the tool author | No quality difference | Independently authored tests |
| M3 discoverability | Press volume and star counts (45k+ Milvus stars, 12.6k claude-context) are high, but HN engagement for vendor posts is 1–6 points | Separate press and stars from verified reuse | Visibility ≠ use | Stars never used as outcome |
| M4 verified third-party reuse | Milvus 3.0 open formats could enable reuse of lake data without copying | Trace consented downstream repos actually running External Collections | Feature exists but is not used | Executed pinned examples only |
| M5 rights/security/provenance | Mixed licences, including a proprietary console marketed as open-source; two in-window advisories with lagging release notes | Licence check at a pinned commit before any reuse; advisory watch on pinned versions | Marketing wording ≠ licence | LICENSE file text plus advisory ranges |
| M6 review/maintenance and lifecycle cost | Parallel 2.6.x and 3.0.x lines; pre-1.0 agent tools with rapid churn (24 memsearch releases) | Measure upgrade minutes per minor version for a pinned example | Churn absorbed cheaply | Human minutes; no kWh/CO2e inferred |
| M7 actionable interventions | Licence-and-advisory gate for vector-DB dependencies; frozen-task evaluation of code retrieval | See §8 | Gate adds friction without catching issues | Synthetic tasks only until approval |

Company adoption claims ("more than 10,000 enterprises", "over 100 million Docker pulls", customer names) are **not** independent task outcomes or verified reuse.

## 8. One practical, falsifiable change for the maintainer's own repositories

**Repository/component:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study), offline, network-free documentation and code tasks. The disabled Trending `capture` command stays disabled.

**Candidate practice (not yet validated):** Give the coding agent a **local semantic code index** before it edits, instead of letting it rely only on grep and file reads. Reuse first: compare an existing open-source MCP code-retrieval server (claude-context, MIT, pinned npm `@zilliz/claude-context-mcp@0.1.15`, backed by a **local** Milvus Lite instance and a **local** embedding model, so no paid API) with the agent's built-in grep/read tools. Do not build a new retrieval tool. Do not send repository content to any hosted vector or embedding service without separate approval.

**Treatment/control and frozen comparable task:** Freeze 12 small synthetic issues. Examples: locate and fix a validator edge case, update a doc cross-reference, extend a CSV-schema test. Each issue gets **hidden acceptance tests written by a person other than the agent operator**, kept out of agent context. Arm A is grep/read only. Arm B adds the retrieval server. Both arms use the same agent, model version, prompt, time budget and repository commit, with arm order randomized per task. Accepted-task unit: one patch that passes the hidden tests and that the human reviewer accepts without rework.

**Success and guardrails:**
- **Primary outcome:** accepted tasks over all 12 assigned tasks. Refused, failed and timed-out tasks stay in the denominator.
- **Secondary outcomes:** tool calls, tokens as logged by the client, and wall-clock time.
- **Guardrails:** the full unit suite stays green. No new dependency is added to the repository; the index lives outside the repo. No network egress from the index or embedding process. No repository content leaves the machine. Licences of the pinned tool and its runtime dependencies are recorded before use.
- **Measured human work:** setup minutes, index-maintenance minutes, and per-task review minutes.
- **Cost:** no energy or CO2e estimate unless metered. No paid API spend without approval. Commit authorship stays with the maintainer, and no AI contributor attribution is recorded.

**Stop/reversal rule:** Stop and keep Arm A if any of these hold:
- Arm B does not raise the accepted-task count by at least 2 of 12.
- Arm B adds more than 10 setup/review minutes per task on average.
- Arm B requires sending code to a hosted service.
- Any pinned dependency has an unresolved licence or open advisory.

Stop immediately on any observed outbound connection from the index process. **No trial executed; no effect estimated.**

## 9. Findings, uncertainties and review outcome

- **Observed/shipped (documentary, vendor-sourced):**
  - Milvus 3.0-beta (May 9), 3.0.0 GA (Jul 29), 3.0.1 (Sep 9) and 3.0.2 (Sep 20), plus 2.6.15–2.6.25, with PyPI/npm SDK release dates confirmed.
  - Zilliz Cloud changelog items: regions, BYOC-I on GCP, billing start, access control/SCIM.
  - VectorDBBench 2.0.0, Attu 3.0.0, zilliz-cli releases, mfs and memsearch releases.
  - Two Milvus advisories with fix commits/releases.
  - One status-page incident.
- **Claims/announcements only:**
  - Vector Lakebase cost figures ($318 vs $4,937; under $500 vs $7,000/$10,800), tier QPS ranges, Loon 135× I/O reduction, sparse index ~3× smaller.
  - claude-context 39.4%/36.1%, migration 25 ms vs 3,112 ms, Jev precision figures, VDBBench cost results.
  - Customer and enterprise counts.
  - The direction statements in §5.
- **Conjectures and unknowns:** H1–H5 in §6. Actual usage of External Collections. Independent benchmark replication. Energy use. Whether claude-context is still maintained after June.
- **Important contradictory or null evidence:**
  - (a) Attu is described as "open-source" on 2026-06-11, but its LICENSE says it is "no longer open source from version 2.6.0 forward".
  - (b) Vector Lakebase "launch" is dated 2026-05-07 (changelog), 05-09 (monthly notes), 05-11 (blog "Today") and 06-10 (press release "today").
  - (c) Milvus 3.0 GA dates differ by source: PR dateline Jul 16, blog frontmatter Jul 27, GitHub release and blog publish commit Jul 29, Business Wire snippet Jul 31 (E0), newsroom Aug 1.
  - (d) MarketsandMarkets item: PR Newswire Apr 22 vs Zilliz newsroom Apr 30.
  - (e) The same executive is called "Co-founder and CTO" (Milvus 3.0 PR) and "VP of Engineering" (VDBBench PR, Aug 5).
  - (f) The PyPI `zilliz-cli` latest is 1.0.2, but GitHub tags reach zilliz-v1.5.0.
  - (g) GHSA-jh4h-22hq-x74p was published Sep 27 with no patched 3.0.x release until Oct 14. The v2.6.25 release notes still read "coming soon" at access, and the global advisory endpoint returned 404.
  - (h) The VDBBench PR calls the benchmark "vendor-neutral" while Zilliz benchmarks itself against competitors.
  - (i) Hacker News engagement with vendor submissions was minimal (1–6 points; one 35-point hit for "Zilliz" was an unrelated "Zillionaires" story). The one critical thread found was a 3-point text post about unauthenticated vector DBs (E0).
  - (j) No independent trade-press analysis was found. Search results returned only syndicated press releases.
- **#56 candidates (not minted):** none independent. All in-window press coverage found was syndicated vendor releases. Candidates for human follow-up: an independent reproduction of VDBBench cost cases (none found); third-party reporting on the Attu licence change (none found in window).
- **Reviewer links and audit date:** none yet. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.
