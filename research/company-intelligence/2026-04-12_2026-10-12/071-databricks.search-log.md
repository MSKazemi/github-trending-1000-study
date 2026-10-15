# Databricks (071) — provisional source-query and inclusion log

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** Companion to the [report](071-databricks.md) and [event ledger](071-databricks.events.csv) for [#139](https://github.com/MSKazemi/github-trending-1000-study/issues/139). Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

**Window:** 2026-04-12 to 2026-10-12 inclusive (UTC dates). **Accessed:** 2026-10-16.

**Method:**
- Raw HTML of official pages was retrieved with `curl` using a generic `Mozilla/5.0` User-Agent. No personal identifier, email or credential was sent to any site, and no regulatory filing system was contacted.
- Text was extracted locally and every number, version, date and quote used in a ledger row was confirmed with `grep`.
- Release dates, licences and advisories came from the GitHub REST API (`gh api`, read-only) and the PyPI JSON API.
- Independent coverage was found through the Hacker News Algolia API, plus one web search.

**This is not exhaustive retrieval.** Pages were not archived or hashed in the repository and may change after access. One dated release-note entry demonstrably changed after publication.

## Query and source log by segment

| Date | Segment | Exact query or source request | Opened / decision | Found / screened / excluded |
|---|---|---|---|---|
| 2026-10-16 | all | `GET https://www.databricks.com/robots.txt`, `/feed`, `/sitemap.xml` → `press-releases-assets/sitemap/sitemap-0.xml`, `en-blog-assets/sitemap/sitemap-0.xml` | robots `Allow: /`. The RSS feed holds only the 10 newest posts (Oct 13–15, all post-window). The sitemaps carry no `<lastmod>`, so each page's `article:published_time` / JSON-LD `datePublished` and its displayed date were read | blog sitemap 4,369 URLs |
| 2026-10-16 | all | `GET https://www.databricks.com/company/newsroom/press-releases` | The list is client-rendered and gives no items in raw HTML, so the first 26 English URLs from the press-release sitemap were fetched instead | 26 fetched / 17 in window / 5 ledgered |
| 2026-10-16 | all | 37 blog URLs selected from the sitemap by slug terms (gateway, agent, MCP, skills, Genie Code, Lakebase, governance, OpenSharing, Panther, Summit 2026, coding agents) | 32 in window. Excluded: Kimi/GPT/Claude/Muse model-availability posts, customer case studies, Azure/AWS partner Summit posts, Lakebase engineering series, convert-code-to-ANSI-SQL post | 37 / 32 / 7 ledgered (others used as checks or limitations) |
| 2026-10-16 | all | `GET https://docs.databricks.com/aws/en/release-notes/product/2026/{april..october}` | Every h2/h3 heading listed with its date; sections for in-scope items read in full. Out of scope: connectors, BI/dashboards, runtime maintenance, model-availability entries | 299 in-window entries / headings screened / 10 ledgered |
| 2026-10-16 | all | `gh api repos/mlflow/mlflow/releases`; `releases/tags/v3.12.0 … v3.17.0, v3.15.2, v3.16.1, v2.11.5, ts/v0.2.0`; `GET https://pypi.org/pypi/mlflow/json` | 6 minor releases ledgered. Patch releases 3.15.1/3.15.2/3.17.1 (3.17.1 is post-window) and the 2.11.5 backport (2026-09-23, UC registry opt-in) were not ledgered | 11 releases in window |
| 2026-10-16 | all | `gh api repos/mlflow/mlflow/security-advisories`; `gh api /advisories?ecosystem=pip&affects=mlflow&published=2026-04-01..2026-10-16`; `gh api /advisories/<GHSA>` for the 13 IDs in 3.17.0 and for GHSA-gq3w-7jj3-x7gr | 10 repository advisories returned; 17 global advisories (3 before Apr 12). 12 of the 13 IDs cited in 3.17.0 were absent from the global DB on access | 4 ledger rows (batch, SSRF, 3.16.1, 3.17.0) |
| 2026-10-16 | all | `gh api` releases for `databricks/cli`, `databricks/databricks-sdk-py`, `unitycatalog/unitycatalog`, `delta-io/delta`, `delta-io/delta-sharing`; PyPI `databricks-sdk` | CLI: 30 releases on 2026-04-19, v1.0.0 on 2026-05-21. SDK: 49 in-window releases (point releases not ledgered). UC: 0.4.1, ai-v0.4.0, 0.5.0, 0.5.1, 0.6.0 (0.7.0 is 2026-10-13, post-window). Delta: 4.2.0–4.4.1 and 3.3.3 | 4 rows |
| 2026-10-16 | all | `gh api orgs/databricks/repos?sort=created`, `orgs/databrickslabs/repos?sort=created`; `repos/databricks/{unity-gateway,genie-code-cli,databricks-agent-skills}` + LICENSE files; `repos/OpenSharing-IO/OpenSharing`; `repos/omnigent-ai/omnigent` + README | New in-window repos: `unity-gateway` (2026-04-17), `genie-code-cli` (2026-08-06), `appkit-registry`, `databricks-sql-kernel-bindings`; labs `coding-agents-databricks-apps`, `lakemeter-oss` and others. Licence files were read; "Databricks License" is a source-available licence | used in rows 007, 012, 031 |
| 2026-10-16 | Apr 12–30 | release notes April; blogs `ai-gateway-how-connect-agents-external-mcps-securely`, `ai-gateway-governance-layer-agentic-ai` (Apr 15), `agent-bricks-governed-enterprise-agent-platform` (Apr 14), `governing-coding-agent-sprawl-unity-ai-gateway` (Apr 17), `openai-gpt-55-now-available…` (Apr 24, excluded: model availability) | 3 rows. Press releases Apr 17 (APJ appointment) excluded as personnel | — |
| 2026-10-16 | May | blogs `whats-new-unity-ai-gateway-service-policies…`, `how-safeguard-ai-workloads-unity-ai-gateway-guardrails` (May 19; context); press release May 4 (ANZ investment, excluded); `https://duckdb.org/2026/05/07/delta-uc-updates`; `https://thebuild.com/blog/2026/05/12/…` | DuckDB ledgered; thebuild.com used as a limitation source | — |
| 2026-10-16 | June | press releases Jun 2 (Summit lineup: dates Jun 15–18, context), Jun 10 OpenSharing, Jun 16 Panther / Genie One / LTAP / Lakehouse//RT / CustomerLake (marketing CDP, excluded); blogs `introducing-omnigent…` (Jun 13), `agent-bricks-dais-2026`, `whats-new-unity-catalog-data-ai-summit-2026`, `ai-governance-data-ai-summit-2026-whats-new-unity-ai-gateway`, `introducing-opensharing-next-evolution…`, `announcing-new-opensharing-and-marketplace…`, `whats-new-genie-code-data-ai-summit-2026`, `whats-new-databricks-platform-security-and-compliance…`, `announcing-lakebase-search…`, `personalizing-genie-code-instructions-skills-memory-and-mcp` (Jun 1) | 11 rows. The several Summit blogs were folded into rows 014 and §5 rather than separate rows | — |
| 2026-10-16 | June | Phoronix, Techstrong, Onehouse and ClickHouse pages (links from HN); Onehouse date from `<time datetime="2026-06-11…">` | Phoronix used as independent check (OpenSharing). Onehouse ledgered as a competitor critique. ClickHouse (competitor) used as check on row 016. Techstrong read, not separately cited in the ledger | — |
| 2026-10-16 | July | press releases Jul 16 ($188B), Jul 23 (Microsoft partnership: excluded as corporate partnership; Azure-specific); blogs `benchmarking-coding-agents…` (Jul 8), `why-frontier-data-agent-outperforms-general-coding-agents…` (Jul 23, context), `introducing-ai-spend-controls-unity-ai-gateway` (Jul 23, context), `how-databricks-manages-its-own-coding-agent-spend…` (Jul 28, context: $500 default limit, $2500 manual review), `convert-proprietary-code-open-ansi-sql-genie-code` (Jul 30, excluded) | 5 rows | — |
| 2026-10-16 | July | `https://techcrunch.com/2026/07/17/databricks-hits-188b-valuation…` | Read raw (`datePublished` 2026-07-17T22:12:56Z). The Reuters and WSJ links surfaced on HN were **not read** | independent check, row 021 |
| 2026-10-16 | August | blogs `unity-ai-gateway-generally-available` (Aug 4), `databricks-completes-acquisition-panther…` (Aug 3), `smart-routing-unity-ai-gateway…` (Aug 13), `introducing-governance-hub…` (Aug 26, context); press release Aug 13 ($7B / $5B at $190B); `https://electric.ax/blog/2026/08/11/electric-joining-databricks`, `https://neon.com/blog/electric-joins-neon`, Blocks & Files 2026-08-12; `https://earendil.com/posts/pi-autoresearch-and-databricks/` | 4 rows. Electric is context only. Earendil (maker of the Pi harness) is an interested party, used as a limitation | — |
| 2026-10-16 | September | release notes September; blogs `genie-one-mcp-now-generally-available` (Sep 22), `genie-one-mcp-give-any-ai-agent-right-business-context` (Sep 22), `deploy-and-manage-coding-agents-scale-unity-gateway-cli` (Sep 24); press releases Sep 14/15 (Singapore, excluded), Sep 24 Row Zero (context), Sep 24 Cal Athletics (excluded) | 5 rows | — |
| 2026-10-16 | Oct 1–12 | release notes October (entries Oct 13–20 excluded); blog `lakebase-and-agentic-sdlc-branching-databases-coding-agents` (Oct 8); press release Oct 6 (Fox Corporation, customer, excluded); `https://www.responsive.dev/` (Oct 9, context); PromptArmor page | 4 rows | — |
| 2026-10-16 | cross-window | HN Algolia `search_by_date` with `numericFilters=created_at_i>1775952000,created_at_i<1792022400`, `tags=story`, queries `Databricks` (117 hits), `MLflow` (6), `OpenSharing` (1), `"Unity Catalog"` (4), `Lakebase` (18) | External links screened. Medium tutorials, Show HN products and vendor self-posts excluded. The Medium article on MLflow default credentials returned **HTTP 403** (inaccessible); the issue was covered from MLflow release notes and GHSA instead | ~25 external / 9 opened |
| 2026-10-16 | cross-window | web search `Databricks vulnerability OR outage OR criticism 2026 Genie Unity Catalog security` | Returned PromptArmor (already read), status aggregators (isdown.app, pingoru.io) and a ToolNavs rewrite of PromptArmor. The aggregator outage snippets (Unity Catalog on Jun 8 AWS us-east-1, Jul 15 and Aug 25 Azure) are **E0, not used**: no official incident history was reachable | unknown / 9 / 9 |
| 2026-10-16 | cross-window | `GET https://status.databricks.com/`, `/history`, `/api/v2/incidents.json` | The front page shows current state only. History and API returned HTTP 404: **inaccessible** | — |
| 2026-10-16 | cross-window | `GET https://docs.databricks.com/aws/en/security/privacy/security-bulletins`, `https://www.databricks.com/trust/security-features/security-bulletins` | Both returned HTTP 404 (guessed URLs). No official Databricks platform security-bulletin index was located | — |

## Inclusion, deduplication and conflicts

- **Included:** 36 rows (Apr 3, May 4, Jun 11, Jul 5, Aug 4, Sep 5, Oct 4). Every row cites a URL that was fetched as raw text or queried through an API. No row relies on a search snippet alone.
- **Duplicate groups:**

  | Group | What it joins |
  |---|---|
  | `071-001` | Unity Gateway lineage: MCP governance, coding-agent support, GA, Smart Routing, central config |
  | `071-004` | MLflow minor releases |
  | `071-006` | MLflow security advisories and fixes |
  | `071-009` | Genie Code auto-approve and the PromptArmor report |
  | `071-013` | Genie One GA claim and Genie One MCP GA |
  | `071-014` | Agent memory announcement (Jun) and Beta (Sep) |

  Syndicated or secondary reports of one announcement (Phoronix and Techstrong on OpenSharing; TechCrunch on the round) were treated as one event.
- **Date conflicts recorded, not resolved:**
  - Press-release display date vs `article:published_time`: Jul 16 vs 2026-07-17 02:15; Aug 13 vs 2026-08-12 23:45; Sep 24 vs 2026-09-23 19:03.
  - MLflow GitHub release vs PyPI upload: 3.12.0 at 23:48Z vs 10:28Z on May 5; 3.16.1 at 2026-09-17T02:40Z vs PyPI 2026-09-16T23:14Z.
  - Genie One MCP GA blog dated Sep 22 vs release note dated Sep 25.
- **Mutable-documentation evidence:**
  - The April release-note entry for the Supervisor API now reads "(deprecated)".
  - The Jul 15 Genie note says "through January 31, 2027", while an Aug 3 note says the promotion was previously set to end Jul 31, 2026.
  - The PromptArmor URL `four-databricks-genie-controls-that-dont-stop-malicious-skills` now redirects to `phishing-in-databricks-genie`.
- **Figure conflicts:**
  - $188B (term sheet) vs $190B (close).
  - Smart Routing savings stated as 30%+, 35% and 56% in one post.
  - GHSA-7gwp severity is high (repository advisory) vs critical (global database).
  - GHSA-gq3w is listed as fixed in 3.8.0rc0, yet a related fix shipped in 3.16.1.
- **Figures confirmed against raw text** (grep of saved text):
  - Press releases: $188B, Coatue; $5B, $190B, $7B, >80%, >$100M Lakebase; "third security acquisition"; 100+ integrations; "$10 free for every user every month"; "12,000 queries per second", "16x"; Summit dates "June 15-18".
  - Benchmark blog: $1.28 / $1.94 / $2.09 per task, 81% / 87%, ~1.7x, 1.9x, "more than 2x", "3x less context", "about a quarter" low-complexity and "~60%" medium.
  - Smart Routing post: "65% of the cost per task", "35% savings", "56% cost savings", "under 50 ms for a 100-turn conversation".
  - Unity Gateway CLI post: "61 billion input tokens across roughly 360,000 requests", "$1.2 million per year".
  - Genie release notes: 150 DBUs, about $10.50.
  - CLI: 0.299.x security patches through May 20, 2027.
  - Counts from API output: 30 CLI releases on 2026-04-19; 49 SDK releases; 10 advisories May 11–Jun 4; 13 GHSA IDs in 3.17.0.
  - All of these remain **vendor, press or registry statements**, not verified measurements.
- **Untrusted-content notes:** fetched pages were treated as data, and none contained instructions that were followed.
  - `electric.ax` embeds an LLM-directed note ("Are you an LLM? You can read better optimized documentation at …md"). It was not followed.
  - The `databricks/unity-gateway` repository contains `AGENTS.md` and `CLAUDE.md` agent-instruction files. These were **not read or executed**; only `README.md`, `LICENSE.md` and release metadata were read.
  - ClickHouse pages offer "Open in ChatGPT/Claude" links, which were ignored.
  - No command suggested by any page was run.
- **Interested parties flagged:** PromptArmor (security vendor), Onehouse and ClickHouse (competitors), Earendil (Pi harness maker), Electric and Responsive (acquired companies).

## Missing, inaccessible or not attempted

- **Inaccessible or not read:**
  - Status-page incident history (HTTP 404) and any official Databricks security-bulletin index.
  - The Medium article on MLflow default credentials (HTTP 403).
  - Reuters, WSJ and Yahoo Finance originals (Yahoo returned 404; the others were not attempted).
  - The Neon acquisition press release (pre-window).
  - Databricks terms for partner-powered AI features and agent-memory retention.
  - Regulatory or filing-level corporate records.
- **Not exhaustively screened:**
  - Most of the 4,369 blog URLs. Selection was by slug, so posts with non-obvious slugs may be missed.
  - Non-English blogs.
  - Azure and GCP documentation variants.
- **Not done:** no product was executed, no account created, no paywall circumvented, no energy measurement.
- **No empty months:** every calendar segment had in-scope events.
- **Reproduction:** re-run the requests above with UTC timestamps and save raw HTML hashes. An independent human should spot-check the security rows (CI2026-071-006, 025, 030, 033, 034), the governance-change rows (028, 019, 036) and the benchmark row (020) before any evidence is promoted beyond provisional status.
