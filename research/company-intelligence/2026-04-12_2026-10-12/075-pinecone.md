# Pinecone — provisional six-month technology intelligence screen (075)

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** This report, its [event ledger](075-pinecone.events.csv) and [search log](075-pinecone.search-log.md) are an AI-assisted first-pass documentary source screen. No qualified human has reviewed them. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open. Nothing here is a verified task outcome, an adoption measure or an endorsement.

- **Company watchlist ID:** 075
- **Research issue:** [#143](https://github.com/MSKazemi/github-trending-1000-study/issues/143); evidence corpus link [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56) (no `NEWS-YYYY-NNNN` item minted here; candidates listed in §9).
- **Ownership and product boundaries (as of 2026-10-12):** Pinecone Systems, Inc. ("© Pinecone Systems, Inc. | San Francisco, CA" in the site footer; press-release datelines vary: New York, San Francisco, Singapore). Privately held and venture-funded. No acquisition of Pinecone, and no acquisition by Pinecone, was found in the window. Pre-window baseline: Calcalist (31 Aug 2025), citing The Information, reported that Pinecone was [exploring a potential sale](https://www.calcalistech.com/ctechnews/article/rz31q82b5). No in-window source reports a sale. Ash Ashutosh is CEO. His [2026-08-26 post](https://www.pinecone.io/blog/one-year-in-just-getting-started/) marks one year in the role and says founder Edo Liberty "is now stepping back from his day-to-day responsibilities" but stays a shareholder and board member. Filing-level corporate verification was **not** performed.
- **Product URL and company newsroom:** [pinecone.io](https://www.pinecone.io/), [blog](https://www.pinecone.io/blog/), [newsroom](https://www.pinecone.io/newsroom/), [2026 changelog](https://docs.pinecone.io/release-notes), [status page](https://status.pinecone.io/) (Atlassian Statuspage), [pinecone-io GitHub org](https://github.com/pinecone-io), [PyPI `pinecone`](https://pypi.org/project/pinecone/), [npm `@pinecone-database/pinecone`](https://www.npmjs.com/package/@pinecone-database/pinecone).
- **Analysis window:** 2026-04-12 to 2026-10-12 inclusive; accessed 2026-10-16.
- **Researcher / factual reviewer / review date:** AI-assisted screen / **pending** / **pending**.
- **Status:** screened (provisional). The ledger has 36 rows covering all seven calendar segments.
- **Source coverage:** the full 2026 changelog (33 in-window entries), 32 in-window blog and newsroom pages (27 posts and 5 press releases, fetched as raw HTML), GitHub release metadata for 9 official repositories, PyPI and npm upload times, and the full Statuspage incident API (it reaches back to Aug 2025). Independent sources were SiliconANGLE, one independent practitioner benchmark, and Hacker News via the Algolia API. Web search returned mostly vendor pages and aggregators. No in-window TechCrunch, Reuters or Register story about Pinecone was found. VentureBeat returned HTTP 429. See the [search log](075-pinecone.search-log.md).

## 1. Search and inclusion audit

This is a summary. Exact requests, opened URLs and exclusions are in the [search log](075-pinecone.search-log.md). Search engines did not expose result totals, so those totals are recorded as **unknown**, not zero.

| Search run UTC | Site/engine | Full query and dates | Found | Screened | Included | Excluded/why | Coverage limitation |
|---|---|---|---:|---:|---:|---:|---|
| 2026-10-16 | docs.pinecone.io/release-notes | all 2026 entries, 2026-04-12..10-12 | 33 in-window entries | 33 | 14 rows cite it as source (some combine entries) | minor entries folded into limitation text (log) | page is mutable; no per-entry edit history |
| 2026-10-16 | pinecone.io blog + newsroom (embedded Sanity JSON with `publishDate`) | all posts dated in window | 27 posts + 5 press releases | 32 opened (+1 post-window) | 10 rows | engineering explainers and customer stories (log) | the blog index shows "Load More"; post list taken from embedded page data |
| 2026-10-16 | `gh api` releases, PyPI JSON, npm registry | python-sdk, ts-client, go, java, terraform, mcp, cli, cultivar, vq-bench | 24 in-window GitHub releases (+PyPI/npm uploads) | 24 | 8 rows (+1 repo-based row) | patch and RC releases (log) | release notes are vendor text |
| 2026-10-16 | status.pinecone.io `/api/v2/incidents.json` | in-window incidents | 19 | 19 | 1 row | 18 availability incidents listed in §3 | no postmortems published |
| 2026-10-16 | HN Algolia, WebSearch (3 queries), outlet tag pages | "Pinecone" stories; Nexus/KnowQL; funding/layoffs/acquisition | 18 HN hits; search totals unknown | ~35 | 2 rows | name collisions (PINE64 etc.), aggregators (E0), competitor leaderboard | weak independent coverage; VentureBeat 429 |

## 2. Verified company/product identity and baseline

Pinecone sells a managed vector database. It runs serverless "on-demand" indexes, provisioned Dedicated Read Nodes and pod-based indexes (now legacy), and supports dense, sparse and (in the window) full-text fields. It also offers **Pinecone Assistant** (managed RAG/chat), hosted **Inference** (embedding and rerank models, including third-party models), and from the window onward **Nexus** (an agent "knowledge engine") with the **KnowQL** query language. The SDKs are open source and the service is proprietary. The SDKs are Apache-2.0 (Python, Node, Go and Java per the GitHub API), the Terraform provider is MPL-2.0, and many example and tooling repos are MIT. The database, Nexus and Assistant backends are closed and hosted, or run as a vendor-operated data plane in the customer's cloud (BYOC). An Apache-2.0 client gives no rights to the backend. The REST API is date-versioned (`YYYY-MM`). Per the [versioning page](https://docs.pinecone.io/reference/api/versioning), a new stable version ships quarterly and each is supported for at least 12 months. In the window the stable version moved from `2026-04` to `2026-07`.

Pre-window baseline (context only, not counted): BYOC early access; sparse-only indexes (March 2025, per the vendor's [Sparse V3 post](https://www.pinecone.io/blog/sparse-v3/)); Python SDK 8.1.1/8.1.2 (2026-04-02/08); Node SDK 7.2.0 (2026-04-10); the [Assistant usage-based pricing](https://docs.pinecone.io/release-notes) change of 2026-04-01. **Post-window, excluded:** the changelog entries for BYOC on-demand indexes (2026-10-15), the usage-export Admin API (2026-10-14) and the cross-region restore fee (2026-10-13), plus a `llama-text-embed-v2` incident (2026-10-14).

## 3. Month-by-month discoveries (six calendar months + partial endpoints)

| Month | Announcements/changes | Primary URLs | Independent reporting | Notes or no-result limitations |
|---|---|---|---|---|
| 2026-04-12..30 | Dedicated Read Nodes GA (Apr 15); Assistant custom file IDs and async file operations (Apr 21, API only); fetch by metadata GA (Apr 28) | [DRN blog](https://www.pinecone.io/blog/dedicated-read-nodes-ga/), [changelog](https://docs.pinecone.io/release-notes) | none found | Load-balancing engineering post (Apr 14) and ZoomInfo customer release (Apr 15) excluded |
| 2026-05 | Frankfurt and Singapore regions (May 1); **Nexus + KnowQL early access**, Builder plan, full-text search public preview, Python SDK v9 rewrite (all May 4); Marketplace preview (May 5); Python 9.0.1 (May 19) | [Nexus launch](https://www.pinecone.io/blog/knowledge-infrastructure-for-agents/), [Python v9](https://github.com/pinecone-io/python-sdk/releases/tag/v9.0.0) | HN story of the launch post (6 points, 0 comments) only | Status page: 4 incidents (May 6 ×2, May 13, May 25), not ledgered |
| 2026-06 | Bulk import $1→$0.25/GB (Jun 1); Builder in all GA regions and Nexus–OneLake at Microsoft Build (Jun 3); open "monitoring stack" (Jun 9); Node SDK v8 (Jun 16); CLI v1.0.0 (Jun 17); empty-results correctness incident (Jun 18) | [changelog](https://docs.pinecone.io/release-notes), [OneLake release](https://www.pinecone.io/newsroom/microsoft-onelake-nexus/), [status](https://status.pinecone.io/incidents/0trwz267s120) | [independent cost/latency comparison, Jun 1](https://darryl-ruggles.cloud/the-real-cost-of-vector-storage-s3-vectors-vs-opensearch-vs-pgvector-vs-pinecone/) | AskData dogfooding post (Jun 2, ">92%" token claim) and EA benchmarks post (Jun 5) used as context only |
| 2026-07 | **Nexus public preview** and Cohere rerank 3.5→4-fast redirect notice (Jul 1); cross-region restore preview (Jul 2); expanded RBAC (Jul 13); SAML/SCIM (Jul 20); FTS fuzzy/n-gram and Go SDK v6 (Jul 21) | [Nexus PP](https://www.pinecone.io/blog/pinecone-nexus-public-preview/), [changelog](https://docs.pinecone.io/release-notes) | [SiliconANGLE, Jul 2](https://siliconangle.com/2026/07/02/pinecone-releases-nexus-public-preview-bring-business-knowledge-ai-agents/) | Status: Jul 9, 12, 20, 21 (critical, Azure eastus2) incidents not ledgered |
| 2026-08 | Terraform v4 (Aug 1); **Nexus GA** + press release + KnowQL 0.1.0 spec (Aug 6); MCP server v0.3.0 security release (Aug 7); cultivar v0.3.0 (Aug 10); agent-friendly API principles (Aug 12); BYOC GA (Aug 25); CEO one-year post with founder stepping back (Aug 26); **Marketplace end of life** (Aug 31) | [Nexus GA](https://www.pinecone.io/blog/pinecone-nexus-generally-available/), [spec](https://spec.knowql.org/0.1.0), [changelog](https://docs.pinecone.io/release-notes) | none in-window beyond vendor (the IDC quote sits inside the vendor release) | Status: Aug 25 GCP incident not ledgered |
| 2026-09 | Egress metering and import-credit withdrawal (Sep 1); **FTS GA / Documents API** (Sep 2; blog Sep 9); Python v10 (Sep 3); Node v9 (Sep 9); 1M-namespace Enterprise limit (Sep 13); Assistant model auto-routing (Sep 15); VQ-bench (Sep 17); BYOC GA blog (Sep 23); Go v7 (Sep 28); namespace aliases (Sep 29) | [changelog](https://docs.pinecone.io/release-notes), [VQ-bench](https://www.pinecone.io/blog/vq-bench/) | none found | Status: Sep 1, 17, 22, 28 incidents not ledgered |
| 2026-10-01..12 | **Pinecone Local end of life** (Oct 7); Terraform v5 (Oct 12); Python 10.1.0rc1 (Oct 7) and Node 9.1.0-rc (Oct 8) | [changelog](https://docs.pinecone.io/release-notes), [Terraform v5](https://github.com/pinecone-io/terraform-provider-pinecone/releases/tag/v5.0.0) | none found | Status: Oct 7 GCP index-initialisation incident not ledgered |

## 4. Dated event evidence and capabilities

Full detail for all 36 rows (`CI2026-075-001`…`036`) is in the [CSV](075-pinecone.events.csv). Highlights:

| Event ID | Published UTC / underlying event date | Claim or observed feature | Availability and limitations | Source link (type) | Independent check | E0–E4 working grade |
|---|---|---|---|---|---|---|
| CI2026-075-004 | 2026-05-04 | Nexus (context compiler + composable retriever) and KnowQL (six primitives) | Early access by application; performance claims have no task set | [launch post](https://www.pinecone.io/blog/knowledge-infrastructure-for-agents/) | none | E1 |
| CI2026-075-007 | 2026-05-04 | Python SDK v9: total rewrite, 3 runtime deps, Rust gRPC extension, Python 3.10+ | PyPI 2026-05-04T11:05Z; vendor speed-ups "directional" | [release](https://github.com/pinecone-io/python-sdk/releases/tag/v9.0.0) | PyPI JSON | E2 |
| CI2026-075-015 | 2026-06-18 | Some initial queries to infrequently read namespaces returned empty results (multi-cloud) | Resolved the same day; API timestamps of the updates are Jun 22 (possible retroactive posting) | [status](https://status.pinecone.io/incidents/0trwz267s120) | Statuspage API | E2 (first-party) |
| CI2026-075-016/018 | 2026-07-01 / 07-02 | Nexus public preview (Box, OneLake, local upload connectors) | Customer eval of n=20 questions | [blog](https://www.pinecone.io/blog/pinecone-nexus-public-preview/) | [SiliconANGLE](https://siliconangle.com/2026/07/02/pinecone-releases-nexus-public-preview-bring-business-knowledge-ai-agents/) (vendor-sourced) | E1 |
| CI2026-075-020/021 | 2026-08-06 | Nexus GA in the customer's cloud; τ-Knowledge results; own support agent 24.6%→55.1% | 74% vs 77% cost-cut conflict; 47.4% vs 46.4% is about 1 task in 97 | [blog](https://www.pinecone.io/blog/pinecone-nexus-generally-available/), [press](https://www.pinecone.io/newsroom/general-availability-of-pinecone-nexus-proves-knowledge-drives-real-outcomes-for-agentic-ai/) | MIT fork [pinecone-io/tau2-bench](https://github.com/pinecone-io/tau2-bench) exists; harness not run | E1 |
| CI2026-075-022 | 2026-08-06 | KnowQL 0.1.0 working draft under OWFa 1.0 | Stated GitHub repo `pinecone-io/knowql-spec` returns 404 | [spec](https://spec.knowql.org/0.1.0) | none | E2 (document readable) |
| CI2026-075-028 | 2026-08-31 | Marketplace end of life, under 4 months after preview | reversed/cancelled | [changelog](https://docs.pinecone.io/release-notes) | — | E2 |
| CI2026-075-030 | 2026-09-02 | Full-text search GA; `POST /indexes` schema-only on `2026-07` | REST breaking change; blog dated Sep 9 | [changelog](https://docs.pinecone.io/release-notes) | SDKs v10/v9/v7 and Terraform v5 adopt it | E2 |
| CI2026-075-035 | 2026-10-07 | Pinecone Local (Docker emulator) end of life | Offline test path removed | [changelog](https://docs.pinecone.io/release-notes) | — | E2 |

**Feature inventory (vendor-documented, not exercised by us):**

| Area | In-window change | Class |
|---|---|---|
| Retrieval | Full-text search: BM25, Lucene syntax, phrase and text-match filters, fuzzy and n-gram matching, preview→GA; fetch by metadata GA; per-query recall/performance control on DRN; namespace aliases; Sparse V3 index layout (vendor engineering post) | shipped / preview |
| Agent surfaces | Nexus (EA→public preview→GA); KnowQL spec 0.1.0; Nexus MCP server (docs); `pinecone-mcp` v0.3.0; agent skills repo; Claude Code, Cursor, Codex and Gemini CLI plugin repos; cultivar skill-testing CLI; "agent-friendly API" principles with a turns-to-first-successful-call metric | mixed |
| SDKs/IaC | Python v9 (rewrite) and v10; Node v8 and v9; Go v6 and v7; CLI 1.0.0; Terraform v4 and v5. **Five major SDK/IaC versions** in six months move to schema-based indexes | shipped |
| Deployment/governance | DRN GA; BYOC GA (Enterprise; FoundationDB metadata in cluster); new regions; expanded RBAC; SAML/SCIM; service accounts in Admin API | shipped, plan-gated |
| Pricing | Builder $20 flat plan; bulk import $0.25/GB (credit added, then withdrawn); egress metering with **blocked reads** on Starter/Builder; Assistant usage-based (Apr 1, baseline) | shipped |
| Model substitution | cohere-rerank-3.5 auto-served by 4-fast (scores and billing units change); Assistant auto-routes deprecated model names to other models | shipped |
| Withdrawals | Marketplace EOL (Aug 31); Pinecone Local EOL (Oct 7); pod-based index creation removed from new SDK majors | observed |
| Licensing | SDKs Apache-2.0; Terraform MPL-2.0; vq-bench, cultivar and plugin repos MIT; KnowQL spec OWFa 1.0; `pinecone-field/pinecone-monitoring` has **no license detected** despite "open-source" framing; `pinecone-io/pinecone-api` has none detected | observed via GitHub API 2026-10-16 |

## 5. What the company says it intends to do

| Verbatim or close paraphrase of public direction (<=25 words per source quoted) | Link/date | Promised horizon | Status (planned, tentative, uncommitted) | Missing/contradictory context |
|---|---|---|---|---|
| Nexus connectors: "Google Drive, Slack, GitHub, Notion, Confluence, and S3 close behind" | [2026-07-01](https://www.pinecone.io/blog/pinecone-nexus-public-preview/) | none stated | planned | Not confirmed shipped in the window |
| Marketplace: "Partner-built commercial solutions coming soon" | [2026-05-04](https://www.pinecone.io/blog/knowledge-infrastructure-for-agents/) | none | **reversed**: Marketplace EOL 2026-08-31 | — |
| KnowQL as "the standard interface the agentic ecosystem has been waiting for" (partner quote); spec "published so agent frameworks … can implement the same contract" | [2026-05-04](https://www.pinecone.io/blog/knowledge-infrastructure-for-agents/), [spec](https://spec.knowql.org/0.1.0) | none | aspiration | No second implementation found; spec repo not public |
| "more in the pipeline as we execute our 'Pinecone Everywhere' strategy" | [2026-08-26](https://www.pinecone.io/blog/one-year-in-just-getting-started/) | none | uncommitted | Undefined |
| Singapore region "joining existing serverless regions … with additional regions planned" | [2026-05-04 press](https://www.pinecone.io/newsroom/Pinecone-Launches-First-Serverless-Region-in-Asia/) | none | planned | — |
| Agent-surface metrics run "as evaluations in CI … with a TTFSC regression treated like any other broken build" | [2026-08-12](https://www.pinecone.io/blog/designing-agent-friendly-apis/) | ongoing | stated practice | Not observable externally |

These are **company statements**, not forecasts we endorse.

## 6. Independent interpretation: direction and alternative scenarios (researcher's conditional 2027–2031 view)

| Hypothesis for 2027–2031 | Supporting observations | Rival explanations | Disconfirming signals | Confidence/unknowns |
|---|---|---|---|---|
| H1: Vector databases converge into hybrid retrieval engines (BM25 + dense + sparse in one index), shrinking the separate search cluster | FTS preview→GA; Documents API; Sparse V3; competitor posts make similar claims | Dedicated engines remain better on relevance for lexical-heavy workloads | Independent relevance benchmarks (e.g., BEIR-style, with denominators) show no gain over BM25 engines plus a vector store | moderate for "convergence of features", unknown for quality |
| H2: Retrieval vendors move up-stack to precompiled, agent-facing "knowledge layers" with their own query languages | Nexus, KnowQL, OneLake/Box connectors, CEO "platform" framing | Positioning against commoditised vector search; Marketplace withdrawal shows up-stack bets can be reversed quickly | KnowQL gets no third-party implementation by 2028; Nexus is withdrawn or folded back like Marketplace | low–moderate |
| H3: SDK churn tied to date-versioned APIs imposes recurring migration costs on downstream reusers | 5 SDK/IaC major versions; schema-only `POST /indexes`; pod-creation removal; emulator EOL | Old API lines stay supported ≥12 months, so the cost can be deferred; agents may absorb migrations cheaply | Measured migration minutes for a pinned example stay near zero across v8→v10 | moderate for churn, unknown for cost |
| H4: Agent-oriented API metrics (turns-to-first-successful-call) become a design target alongside human DX | Vendor TTFSC metric; MCP schema fixes "for Claude tools"; cultivar; plugin repos | Marketing for agent channels; the 3-run vendor smoke test is not evidence | Controlled tasks show no change in accepted-task rate when API error messages are improved | low; untested |
| H5: Silent model substitution inside managed retrieval services will complicate provenance and reproducibility | rerank 3.5→4-fast redirect (scores change); Assistant model auto-routing | Vendors may expose pinned model versions on request | Vendors adopt explicit model-version pinning and failure-on-retire by default | moderate for occurrence |

These are hypotheses for testing, not company strategy or fact.

## 7. Implications for the GitHub 1000 study

| M1–M7 construct | Possible observable effect | Study design to test it | Negative/null explanation | Measurement boundary |
|---|---|---|---|---|
| M1 AI coding-agent change | Vendors ship agent-facing surfaces (MCP, skills, plugins, KnowQL) and measure agent onboarding (TTFSC) | Count consented repos whose agents call vector stores via MCP vs SDK; log turns-to-first-success | Agent channels unused outside demos | Consented logs only; no inference from repo counts |
| M2 accepted task quality | Hybrid lexical+vector retrieval may change accepted-answer rates on identifier-heavy queries | Frozen query set with hidden relevance labels, BM25-only vs hybrid | No difference beyond noise | All queries in the denominator; labels authored independently |
| M3 discoverability | Very little independent press; launch HN post got 6 points | Separate press counts from use | Press is not reuse | Stars, funding and press are never outcomes |
| M4 verified third-party reuse | Open specs and benchmark repos (KnowQL, VQ-bench, tau2-bench fork) could enable reuse | Trace downstream repos that execute them at pinned commits | Code or spec presence without execution | Pinned commits; executed tests only |
| M5 rights/security/provenance | Mixed licensing (an unlicensed "open-source" monitoring repo); MCP CVE fixes; silent model routing | License and dependency audit before reuse; record the effective model per call | Unlicensed repos are not reusable regardless of popularity | License files at a pinned commit |
| M6 review/maintenance and lifecycle cost | Major-version churn; emulator EOL; egress metering blocks reads on low plans | Measure migration minutes and test-infrastructure changes per SDK major | Agents absorb migrations cheaply | No kWh/CO2e from tokens or GPU-hours |
| M7 actionable interventions | Offline mocks replace a withdrawn emulator; actionable error contracts | See §8 | Mocks drift from the real API | Synthetic tasks only until approval |

Company adoption claims ("1M developers", "10,000 customers", ">90% task completion") are **not** independent task outcomes or verified reuse.

## 8. One practical, falsifiable change for the maintainer's own repositories

**Repository/component:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study). The task is local retrieval over its own `docs/` corpus (for example, "which document defines the merge gate for X?"), run fully offline. No Pinecone account, no paid API and no network access are needed for the control or the main treatment. The disabled Trending `capture` command stays disabled.

**Candidate practice (not yet validated):** Reuse first. Answer maintainer and contributor "where is this rule defined?" questions with **hybrid lexical + dense retrieval** instead of lexical-only search. This idea comes from Pinecone's full-text search GA claim (CI2026-075-030), tested here with already-available open-source components (for example SQLite FTS5 BM25, usually reachable through the Python stdlib `sqlite3` (verify the FTS5 compile option first), plus an existing small open embedding model that is pinned by version and hash). Do not build a new retrieval engine. A hosted Pinecone arm is **optional** and needs explicit owner approval because of account, metered-cost and data-transfer implications. It must not be mocked as if it were evidence about Pinecone.

**Treatment/control and frozen comparable task:** Before any runs, a person other than the operator freezes 40 questions and their gold document/section labels, and keeps them out of any agent context. Include identifier-style queries (issue numbers, CLI flag names, file names) and paraphrased conceptual queries. Arm A: BM25 (FTS5) only. Arm B: BM25 + dense with reciprocal-rank fusion. Same corpus commit SHA, same tokenizer settings, same top-k=5. The accepted-task unit is a question whose top-5 contains the gold section **and** that a human reviewer accepts as answering it. Count unanswerable or no-gold questions in the denominator.

**Success and guardrails:** The primary measure is accepted questions out of 40 per arm, reported with a paired exact (McNemar) test and no claim beyond this corpus. Guardrails: no new runtime dependency is added to the repo's package (the experiment lives in a scratch environment); the model licence is checked before use; no network calls; the full unit suite stays green; no personal data is in the corpus. Measured human work: label-authoring minutes, setup minutes and per-question review minutes. Do not estimate energy or CO2e. Commits stay authored by the maintainer.

**Stop/reversal rule:** Keep Arm A and stop if Arm B gains fewer than 4 accepted questions (10 percentage points) or loses on the identifier subset. Also stop if setup plus review costs more than 3 hours in total, or if the embedding model's licence or provenance cannot be confirmed. **No trial executed; no effect estimated.**

## 9. Findings, uncertainties and review outcome

- **Observed/shipped (documentary, vendor-sourced):** 33 in-window changelog entries. 24 SDK/IaC/tool GitHub releases with GitHub, PyPI and npm timestamps, including Python v9 (rewrite) and v10, Node v8 and v9, Go v6 and v7, CLI 1.0.0, Terraform v4 and v5, and `pinecone-mcp` v0.3.0. DRN, fetch-by-metadata, FTS, BYOC and Nexus GA claims. RBAC/SAML/SCIM. Pricing changes. Two product withdrawals (Marketplace, Pinecone Local). Two automatic model substitutions.
- **Claims/announcements only:** Nexus performance (">90% task completion", "30x faster", "up to 90%" / ">90%" / "95%+" token reduction), the τ-Knowledge top-score claim, the 24.6%→55.1% support resolution, DRN "77–97%" savings, SDK speed-ups, Sparse V3 "151×" I/O reduction, and the CEO's financial metrics are all unaudited vendor statements. Future direction items are in §5.
- **Conjectures and unknowns:** H1–H5 in §6; actual retrieval quality; Nexus behaviour; whether KnowQL gets external implementers; the reasons for both EOLs.
- **Important contradictory or null evidence:**
  - (a) Nexus GA cost reduction for GPT-5.5 is 77% (blog) vs 74% (press release). The "top score" margin is 47.4% vs 46.4% on a 97-task domain.
  - (b) Builder namespaces per index: 100 (changelog) vs 1,000 (blog).
  - (c) The May 4 launch post lists FTS as "generally available" on May 7, while the changelog and the May 7 blog say public preview. GA came Sep 2 (changelog) or Sep 9 (blog). The GA post speaks of "months of private preview".
  - (d) BYOC GA: Aug 25 (changelog) vs Sep 23 (blog).
  - (e) New regions: May 1 (changelog), May 4/5 (press releases), May 8 (launch post).
  - (f) Marketplace is presented as part of the platform on Aug 6 and Aug 26, then reaches EOL Aug 31.
  - (g) KnowQL spec names a GitHub repo that returns 404.
  - (h) A monitoring stack called "open-source" has no licence.
  - (i) Customer and developer counts change from "9,000+ paying customers / 800,000+ active developers" (May 4) to "more than 10,000 customers and 1M developers" (Aug 6). Definitions differ and are not audited.
  - (j) Status page shows a correctness incident (empty results) whose updates are API-timestamped four days after the displayed times.
  - (k) No in-window independent evaluation of Nexus or FTS relevance was found. The only independent measurement found is a small single-author cost/latency comparison.
- **#56 candidates (not minted):** SiliconANGLE 2026-07-02 (Nexus public preview); darryl-ruggles.cloud 2026-06-01 (independent cost comparison). Each needs human reading before a `NEWS-YYYY-NNNN` ID is assigned.
- **Reviewer links and audit date:** none yet. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.
