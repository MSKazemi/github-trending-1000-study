# Databricks — provisional six-month technology intelligence screen (071)

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** This report, its [event ledger](071-databricks.events.csv) and its [search log](071-databricks.search-log.md) are an AI-assisted first-pass documentary source screen. No qualified human has reviewed them. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open. Nothing here is a verified task outcome, an adoption measure, an exhaustive search or an endorsement.

- **Company watchlist ID:** 071, Databricks (slug `databricks`).
- **Research issue:** [#139](https://github.com/MSKazemi/github-trending-1000-study/issues/139); evidence corpus link [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56). No `NEWS-YYYY-NNNN` item was minted here; candidates are listed in §9.
- **Ownership and product boundaries (as of 2026-10-12):** Databricks, Inc., a privately held, venture-funded company that describes itself as "Headquartered in San Francisco" in its press releases. No parent company was found. Filing-level corporate verification was **not** performed (no regulatory filings accessed).
- **Product URL and company newsroom:** [databricks.com](https://www.databricks.com/), [press releases](https://www.databricks.com/company/newsroom/press-releases) (list is client-rendered; enumerated through the [press-release sitemap](https://www.databricks.com/press-releases-assets/sitemap/sitemap-0.xml)), [blog](https://www.databricks.com/blog) ([RSS](https://www.databricks.com/feed), last 10 items only), [platform release notes](https://docs.databricks.com/aws/en/release-notes/product/), official GitHub organisations [databricks](https://github.com/databricks), [databrickslabs](https://github.com/databrickslabs), [mlflow](https://github.com/mlflow/mlflow), [unitycatalog](https://github.com/unitycatalog/unitycatalog), [delta-io](https://github.com/delta-io), [OpenSharing-IO](https://github.com/OpenSharing-IO/OpenSharing), [omnigent-ai](https://github.com/omnigent-ai/omnigent).
- **Analysis window:** 2026-04-12 to 2026-10-12 inclusive; sources accessed 2026-10-16.
- **Researcher / factual reviewer / review date:** AI-assisted screen / **pending** / **pending**.
- **Status:** screened (provisional); 36 ledger rows across all seven calendar segments.
- **Scope:** the issue's study angle (agent data lifecycle and governance) plus AI developer tooling, APIs/SDKs, open source, licensing and security. Most connector, BI, industry, regional-office, customer and partnership news was screened out on purpose (see the [search log](071-databricks.search-log.md)).
- **Evidence grades:** company-watch E0–E4 working tiers from the [method](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md), not the separate [lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md). No row is above E2.

## 1. Search and inclusion audit

Summary only. The exact requests, opened URLs and exclusions are in the [search log](071-databricks.search-log.md). Search-engine result totals were not exposed, so they are recorded as **unknown**, not zero.

| Search run UTC | Site/engine | Full query and dates | Found | Screened | Included | Excluded/why | Coverage limitation |
|---|---|---|---:|---:|---:|---:|---|
| 2026-10-16 | press-release sitemap + raw HTML | first 26 English press-release URLs | 17 in window | 17 | 5 rows | regional investment, personnel, sports sponsorship, customer, partnership (log) | the list page is client-rendered; sitemap has no dates, so dates come from each page |
| 2026-10-16 | blog sitemap (4,369 URLs) + raw HTML | ~37 slugs matching agent/governance/security terms | 32 in window (37 opened) | 32 | 7 rows | case studies, model-availability and explainer posts | slug-based selection; most blog posts were not opened |
| 2026-10-16 | docs release notes April–October 2026 | 7 monthly pages | 299 dated in-window entries | all headings | 10 rows | connectors, BI, runtime maintenance, model availability | pages are mutable; at least one dated entry was edited after the fact |
| 2026-10-16 | GitHub API (releases, repos, advisories) + PyPI JSON | mlflow, unitycatalog, delta, delta-sharing, cli, databricks-sdk-py, new repos | 6 MLflow minors, 6 UC, 6 Delta, 5 Delta Sharing, 60 CLI, 49 SDK releases; 17 global MLflow advisories since 2026-04 | ~40 read | 11 rows | patch releases and SDK point releases (log) | advisory database incomplete at access time (§9) |
| 2026-10-16 | Hacker News Algolia API | `Databricks`, `MLflow`, `OpenSharing`, `"Unity Catalog"`, `Lakebase`, window-bounded | 117 / 6 / 1 / 4 / 18 stories | ~25 external links | 3 independent rows; 6 more as check/limitation sources | tutorials, Medium posts, vendor self-submissions | HN is a discovery aid, not a sample |
| 2026-10-16 | web search (1 query) | `Databricks vulnerability OR outage OR criticism 2026 Genie Unity Catalog security` | unknown | 9 | 0 new rows | status aggregators (E0, unused) | session web-search budget nearly exhausted |

## 2. Verified company/product identity and baseline

Databricks sells a proprietary, hosted "Data + AI Platform". Press releases in the window say it includes "Genie, Lakebase, Agent Bricks, Lakeflow, Lakehouse, and Unity Catalog". It also originated or leads several open-source projects: [MLflow](https://github.com/mlflow/mlflow) (Apache-2.0, per GitHub API), [Unity Catalog OSS](https://github.com/unitycatalog/unitycatalog) (Apache-2.0), [Delta Lake](https://github.com/delta-io/delta), [Delta Sharing](https://github.com/delta-io/delta-sharing) (Apache-2.0), [OpenSharing](https://github.com/OpenSharing-IO/OpenSharing) (Apache-2.0, created 2026-06-10), and [Omnigent](https://github.com/omnigent-ai/omnigent) (Apache-2.0, created 2026-06-11). Some developer tools it distributes are **source-available, not open source**. The [agent skills repo](https://github.com/databricks/databricks-agent-skills) and the [Unity Gateway CLI](https://github.com/databricks/unity-gateway) both carry the "Databricks License", which GitHub reports as `NOASSERTION`.

**Brand and entity changes found in the window:**

- **Acquisitions:**
  - [Panther](https://www.databricks.com/company/newsroom/press-releases/databricks-agrees-acquire-panther-further-establishing-security): intent announced 2026-06-16; [completion announced](https://www.databricks.com/blog/databricks-completes-acquisition-panther-accelerating-security-lakehouse-era) 2026-08-03.
  - [Electric](https://electric.ax/blog/2026/08/11/electric-joining-databricks): announced 2026-08-11. It joins "Neon at Databricks", and the post says everything Electric previously open-sourced will remain open source (paraphrase). Independent coverage: [Blocks & Files](https://www.blocksandfiles.com/ai-ml/2026/08/12/oh-no-not-another-one-databricks-buys-electric/5286721), 2026-08-12.
  - [Row Zero](https://www.databricks.com/company/newsroom/press-releases/databricks-acquires-row-zero-bringing-live-governed-spreadsheets): the page displays September 24, 2026, while its meta time is 2026-09-23 19:03.
  - [Responsive](https://www.responsive.dev/): its announcement is dated Oct 9, 2026 and says it is joining to accelerate Lakebase and Neon.
  - These four acquisitions are context and are not ledgered, except Panther.
- **Renames:**
  - Vector Search became **AI Search** (2026-06-01).
  - Delta Sharing became **OpenSharing** (2026-06-10).
  - Genie Spaces became **Genie Agents** (2026-07-08).
  - The `ucode` CLI became `ug` / **Unity Gateway CLI**.
  - The governance gateway is called "AI Gateway", "Unity AI Gateway" and "Unity Gateway" in different in-window sources, with no single dated rename found.

**Pre-window baseline (context only, not counted):**

- Neon is described as "Neon at Databricks". The Neon acquisition press release is in the sitemap from 2025 but was not read.
- Genie Code launched 2026-03-11 ([blog](https://www.databricks.com/blog/introducing-genie-code)).
- The Supervisor Agent was announced GA 2026-02-10 ([blog](https://www.databricks.com/blog/agent-bricks-supervisor-agent-now-ga-orchestrate-enterprise-agents)).
- Lakewatch SIEM was announced 2026-03-24 (press-release meta date).

**Company-scale claims:** "More than 20,000 organizations" and ">$7B revenue run-rate" are unaudited vendor statements. They are not adoption evidence.

## 3. Month-by-month discoveries (six calendar months + partial endpoints)

| Month | Announcements/changes | Primary URLs | Independent reporting | Notes or no-result limitations |
|---|---|---|---|---|
| 2026-04-12..30 | AI Gateway governs MCP servers, Beta (Apr 15); Coding Agent Support in Unity Gateway (Apr 17); 30 CLI patch releases after an expired PGP key broke Terraform download (Apr 19); MLflow traces in UC Public Preview (Apr 30) | [release notes Apr](https://docs.databricks.com/aws/en/release-notes/product/2026/april), [blog](https://www.databricks.com/blog/governing-coding-agent-sprawl-unity-ai-gateway), [cli v0.297.2](https://github.com/databricks/cli/releases/tag/v0.297.2) | none found | Supervisor API Beta (Apr 20) is now labelled "(deprecated)" on the April page. ABAC GA (Apr 28) was not ledgered |
| 2026-05 | MLflow 3.12.0 coding-agent tracing (May 5); DuckDB Delta/UC extensions leave experimental (May 7); 10 MLflow advisories published May 11–Jun 4; CLI v1.0.0 GA with `aitools` skills installer (May 21) | [MLflow 3.12.0](https://github.com/mlflow/mlflow/releases/tag/v3.12.0), [CLI v1.0.0](https://github.com/databricks/cli/releases/tag/v1.0.0) | [DuckDB](https://duckdb.org/2026/05/07/delta-uc-updates); [thebuild.com lock-in critique](https://thebuild.com/blog/snowflake-postgres-lakebase-horizondb-picking-the-lock-in-you-want/) (May 12) | Iceberg GA in UC (May 21) noted, not ledgered |
| 2026-06 | MLflow 3.13.0 RBAC (Jun 1); Genie Code auto-approve (Jun 4); OpenSharing to Linux Foundation (Jun 10); Omnigent open-sourced (Jun 13); Data + AI Summit Jun 15–18: Genie One/Agents/Code GA claim, Agent Bricks platform + agent memory announcement, Panther intent, Lakehouse//RT Beta and LTAP "coming soon"; MLflow 3.14.0 (Jun 17); UC OSS 0.5.0 + Delta 4.3.0 (Jun 18) | [OpenSharing PR](https://www.databricks.com/company/newsroom/press-releases/databricks-announces-opensharing), [Agent Bricks blog](https://www.databricks.com/blog/agent-bricks-dais-2026), [Genie One PR](https://www.databricks.com/company/newsroom/press-releases/databricks-launches-genie-one-all-new-agentic-coworker-every-team) | [Phoronix](https://www.phoronix.com/news/Linux-Foundation-OpenSharing); [Techstrong](https://techstrong.ai/articles/databricks-hands-delta-sharing-to-the-linux-foundation-and-levels-it-up/); [Onehouse](https://www.onehouse.ai/blog/databricks-iceberg-support-has-a-catch-its-called-unity-catalog) (competitor critique); [ClickHouse](https://clickhouse.com/blog/databricks-reyden-benchmark-transparency-clickhouse) (competitor critique, Jun 30) | Densest month (Summit). Many announcements have mixed or unstated availability |
| 2026-07 | Genie pay-as-you-go (Jul 8), paused Jul 15, billing corrections Jul 21; coding-agent benchmark on own PRs (Jul 8); $188B term sheet (Jul 16); MLflow traces in UC GA (Jul 16); MLflow 3.15.0 MCP Registry (Jul 31) | [release notes Jul](https://docs.databricks.com/aws/en/release-notes/product/2026/july), [benchmark blog](https://www.databricks.com/blog/benchmarking-coding-agents-databricks-multi-million-line-codebase) | [TechCrunch Jul 17](https://techcrunch.com/2026/07/17/databricks-hits-188b-valuation-extending-its-run-as-ais-favorite-second-act/) | The Reuters/WSJ links on HN were not read |
| 2026-08 | Unity Gateway GA (Aug 4); MLflow gateway SSRF advisory (Aug 5); Electric (Aug 11); $5B close at $190B (Aug 13); Smart Routing Beta + deterministic PII guardrail (Aug 13); query text masked by default (Aug 26) | [GA blog](https://www.databricks.com/blog/unity-ai-gateway-generally-available), [Smart Routing](https://www.databricks.com/blog/smart-routing-unity-ai-gateway-match-frontier-quality-30-lower-cost-task), [release notes Aug](https://docs.databricks.com/aws/en/release-notes/product/2026/august) | [Earendil](https://earendil.com/posts/pi-autoresearch-and-databricks/) (Aug 4, interested party); [Blocks & Files](https://www.blocksandfiles.com/ai-ml/2026/08/12/oh-no-not-another-one-databricks-buys-electric/5286721) | PromptArmor disclosure to Databricks happened Aug 16 (published Oct 5) |
| 2026-09 | Partner-powered AI setting can no longer be disabled (Sep 8); managed agent memory/sessions Beta (Sep 16); MLflow 3.16.1 removes default admin password (Sep 17); central coding-agent configuration + Unity Gateway CLI v0.2.0 (Sep 22); Genie One MCP GA with Beta endpoint sunset (Sep 25) | [release notes Sep](https://docs.databricks.com/aws/en/release-notes/product/2026/september), [unity-gateway v0.2.0](https://github.com/databricks/unity-gateway/releases/tag/v0.2.0) | none found beyond HN tutorials | Row Zero acquisition (Sep 24) and Singapore investment releases screened out |
| 2026-10-01..12 | PromptArmor Genie Code malicious-skill report (Oct 5); MLflow 3.17.0 with 13 GHSA references (Oct 7); Lakebase branch-per-agent pattern (Oct 8); critical MLflow RCE advisory GHSA-26p8 (Oct 9); Knowledge Assistant and Supervisor Agent made legacy; Skills API Beta (Oct 12) | [MLflow 3.17.0](https://github.com/mlflow/mlflow/releases/tag/v3.17.0), [release notes Oct](https://docs.databricks.com/aws/en/release-notes/product/2026/october) | [PromptArmor](https://www.promptarmor.com/resources/phishing-in-databricks-genie) | Responsive (Oct 9) context only; Oct 13–20 notes excluded |

## 4. Dated event evidence and capabilities

Full detail for all 36 rows (`CI2026-071-001`…`036`) is in the [CSV](071-databricks.events.csv). Highlights:

| Event ID | Published UTC / underlying event date | Claim or observed feature | Availability and limitations | Source link (type) | Independent check | E0–E4 working grade |
|---|---|---|---|---|---|---|
| CI2026-071-002 | 2026-04-17 | Coding Agent Support in Unity Gateway: audit, MCP controls and budgets across Cursor, Codex, Claude Code | "available for all Databricks customers" (vendor) | [blog](https://www.databricks.com/blog/governing-coding-agent-sprawl-unity-ai-gateway) (first party) | none | E1 |
| CI2026-071-003 | 2026-04-19 | Expired OpenPGP key broke Terraform checksum verification in `bundle deploy`. A fix was backported across 30 releases | shipped | [v0.297.2](https://github.com/databricks/cli/releases/tag/v0.297.2) | GitHub API release list | E2 |
| CI2026-071-007 | 2026-05-21 | CLI 1.0.0: `databricks aitools` installs skills into six coding agents; immutable release tags; OS-keyring token storage | GA; the skills repo is under a source-available licence | [v1.0.0](https://github.com/databricks/cli/releases/tag/v1.0.0) | release note "Databricks CLI is now GA" | E2 |
| CI2026-071-009 / 033 | 2026-06-04 / 2026-10-05 (disclosed 2026-08-16) | Genie Code auto-approve uses an AI classifier, which the vendor says is "not a security boundary". PromptArmor shows a malicious Skill phishing the user and exfiltrating data via a rendered display | vendor treats it as user responsibility (per the researcher) | [release notes Jun](https://docs.databricks.com/aws/en/release-notes/product/2026/june); [PromptArmor](https://www.promptarmor.com/resources/phishing-in-databricks-genie) | second entity, not reproduced | E2 (documentary) |
| CI2026-071-010 | 2026-06-10 | Delta Sharing becomes OpenSharing (Linux Foundation) and adds agent skills, models and unstructured data | repo public (Apache-2.0); protocol untested | [press release](https://www.databricks.com/company/newsroom/press-releases/databricks-announces-opensharing) | [Phoronix](https://www.phoronix.com/news/Linux-Foundation-OpenSharing) | E2 |
| CI2026-071-012 | 2026-06-13 | Omnigent meta-harness open-sourced (Apache-2.0, alpha); managed Beta Jun 17 | alpha/Beta | [blog](https://www.databricks.com/blog/introducing-omnigent-meta-harness-combine-control-and-share-your-agents) | [repo](https://github.com/omnigent-ai/omnigent) | E2 |
| CI2026-071-020 | 2026-07-08 | Internal benchmark built from merged PRs and held-out tests, with no LLM judge. Harness choice changed cost per task by more than 2x at equal quality. Git history had to be sealed after agents recovered the answers | task set and n not published | [blog](https://www.databricks.com/blog/benchmarking-coding-agents-databricks-multi-million-line-codebase) | none independent (Earendil is an interested party) | E1 |
| CI2026-071-022 | 2026-07-16 | MLflow trace storage in Unity Catalog GA (OTel format, UC permissions) | GA, regional limits | [release notes Jul](https://docs.databricks.com/aws/en/release-notes/product/2026/july) | PP entry Apr 30 | E2 |
| CI2026-071-028 | 2026-09-08 | Partner-powered AI features can no longer be disabled in the UI; the API toggle ends 2026-11-01 | shipped | [release notes Sep](https://docs.databricks.com/aws/en/release-notes/product/2026/september) | none | E2 |
| CI2026-071-031 | 2026-09-22 | Central configuration of coding agents (models, MCP, skills, harness, routing) via the `ug` CLI or MDM | released; CLI source-available | release notes Sep | [unity-gateway v0.2.0](https://github.com/databricks/unity-gateway/releases/tag/v0.2.0) | E2 |
| CI2026-071-034 | 2026-10-07 | MLflow 3.17.0 fixes referencing 13 GHSA IDs. It needs a coordinated DB upgrade, and mixed-version rolling upgrades are unsupported | shipped; critical RCE advisory published 2026-10-09 | [v3.17.0](https://github.com/mlflow/mlflow/releases/tag/v3.17.0) | [GHSA-26p8](https://github.com/mlflow/mlflow/security/advisories/GHSA-26p8-2jq9-3vq9) | E2 |
| CI2026-071-036 | 2026-10-12 | Knowledge Assistant and Supervisor Agent made legacy, eight months after the Supervisor Agent GA blog | legacy | [release notes Oct](https://docs.databricks.com/aws/en/release-notes/product/2026/october) | Feb 10 GA blog | E2 |

**Feature inventory (vendor-documented, not exercised by us):**

| Area | In-window change | Class |
|---|---|---|
| Agent governance gateway | MCP governance (Beta, Apr) → coding-agent support (Apr) → Unity Gateway GA (Aug 4); Smart Routing (Beta); Sensitive Data Detection guardrail (Beta); unified trace table (Beta, Aug 21); request-tag service policies (Beta, Oct 9); central coding-agent config (Sep 22); Skills API (Beta, Oct 12); bring-your-own Claude subscription relay (Jul 30) | mixed GA/Beta |
| Agent data lifecycle | MLflow traces in UC (PP Apr 30 → GA Jul 16); managed agent memory and sessions (Beta, Sep 16); "agent memory service" announced at the Summit; per-agent Lakebase branches (pattern, Oct 8) | GA / Beta / pattern |
| Agent products | Genie One/Agents/Code GA claim (Jun 16); Genie One MCP GA (Sep 25, Beta endpoint sunset Oct 31); Omnigent (OSS alpha, managed Beta); Knowledge Assistant and Supervisor Agent legacy (Oct 12) | churn |
| Developer tooling | CLI 1.0 GA with `aitools` skills; `mlflow agent setup`; MLflow pytest regression testing; `ug` CLI; databricks-sdk-py: 49 PyPI releases in window (0.103.0–0.151.0) | shipped |
| Open source | MLflow 3.12–3.17; UC OSS 0.5.0 UC Delta API, 0.6.0; Delta 4.2–4.4; OpenSharing (LF); Omnigent | shipped (OSS) |
| Security | 10 MLflow advisories May 11–Jun 4; SSRF and severity-conflict advisories in August; pickle-guard bypass (Sep 1); 13 GHSA references in 3.17.0; default admin password removed in 3.16.1; basic-auth fail-closed default (3.16.0); query-text masking; unused OAuth secrets auto-deleted after 90 days (Sep 16); PromptArmor skill-exfiltration report | observed |
| Licensing | MLflow, UC OSS, OpenSharing and Omnigent are Apache-2.0. `databricks-agent-skills` and `unity-gateway` use the "Databricks License" (source-available). `genie-code-cli` (created 2026-08-06) also carries the "Databricks License" (GitHub API: `NOASSERTION`) | observed |
| Pricing/governance changes | Genie pay-as-you-go → paused → corrected → promotion "extended"; partner-AI opt-out removed from the UI | observed (documentation) |

## 5. What the company says it intends to do

| Verbatim or close paraphrase of public direction (<=25 words per source quoted) | Link/date | Promised horizon | Status (planned, tentative, uncommitted) | Missing/contradictory context |
|---|---|---|---|---|
| "this capital is expected to support future AI acquisitions and deepen AI research"; double down on Unity AI Gateway, Genie, Lakebase | [press release, 2026-07-16](https://www.databricks.com/company/newsroom/press-releases/databricks-raising-strategic-round-funding-188-billion-valuation) | none | uncommitted | Acquisitions of Electric, Row Zero and Responsive followed (context) |
| "Cross-region governance is coming soon in preview. Cross-cloud and cross-account governance will follow." | [UC Summit blog, 2026-06-16](https://www.databricks.com/blog/whats-new-unity-catalog-data-ai-summit-2026) | "soon" | planned, undated | No GA date |
| ABAC "Future support will expand to other securables, including AI components (MCP services, agents), tables, and volumes." | same | none | planned | Partly delivered: Aug 11/31 release notes extend ABAC GRANT to models, services and Unity Gateway resource types |
| "LTAP is coming soon as a part of Lakebase." | [LTAP press release, 2026-06-16](https://www.databricks.com/company/newsroom/press-releases/databricks-launches-ltap-first-lake-transactionalanalytical) | "soon" | announced only | No in-window availability found |
| Genie App Builder and Genie ZeroOps "will enter private preview shortly after the Data + AI Summit" | [Genie One press release](https://www.databricks.com/company/newsroom/press-releases/databricks-launches-genie-one-all-new-agentic-coworker-every-team) | "shortly after" Jun 18 | planned | "Build governed data and AI apps without code (Beta)" entry on Sep 23 may be related; not confirmed |
| Omnigent roadmap: optimisation "with GEPA", an "Omnigent Server MCP", "and more harnesses" | [Omnigent blog, 2026-06-13](https://www.databricks.com/blog/introducing-omnigent-meta-harness-combine-control-and-share-your-agents) | none | uncommitted | — |
| "we plan to run every new agent/harness through it" (internal benchmark) | [benchmark blog, 2026-07-08](https://www.databricks.com/blog/benchmarking-coding-agents-databricks-multi-million-line-codebase) | none | internal intent | Benchmark not public |
| OpenSharing storage partners "coming soon, including Cohesity, Commvault, HPE, NetApp, Nutanix, Rubrik, and VAST Data" | [OpenSharing press release](https://www.databricks.com/company/newsroom/press-releases/databricks-announces-opensharing) | "soon" | announced only | Partner-side confirmation not checked |
| Partner-powered AI setting: "On November 1, 2026, the setting will be removed" | [release notes Sep](https://docs.databricks.com/aws/en/release-notes/product/2026/september) | 2026-11-01 | scheduled | Post-window |
| Genie One MCP Beta endpoint "will be sunset on October 31, 2026" | same | 2026-10-31 | scheduled | Post-window |

These are **company statements**, not forecasts we endorse.

## 6. Independent interpretation: direction and alternative scenarios (researcher's conditional 2027–2031 view)

| Hypothesis for 2027–2031 | Supporting observations | Rival explanations | Disconfirming signals | Confidence/unknowns |
|---|---|---|---|---|
| H1: Enterprise coding-agent use will route through a governance gateway (identity, budgets, MCP/skill allowlists, traces) instead of direct vendor APIs | Coding-agent support (Apr) → GA (Aug) → central config and MDM (Sep) → Skills API (Oct); MLflow OSS gateway adds the same functions | Vendor-led marketing; gateways may stay limited to large regulated firms; agent vendors may ship equivalent controls natively | Major agent tools keep direct-to-provider auth as the dominant enterprise path through 2028; gateway features stay Beta | low–moderate; no adoption denominator |
| H2: Agent traces and memory will be treated as governed data assets (catalogued, permissioned, retained) | MLflow traces in UC GA; unified trace table; managed memory Beta; vendor statement that traces "should be governed in the Lakehouse" | Storage cost and privacy may push teams to keep traces short-lived or unstored | Retention defaults shrink; regulators or customers restrict trace storage of prompts and code | low |
| H3: Agent skills will become a supply-chain attack surface comparable to packages | PromptArmor Genie Code report; skills distributed by CLI `aitools`, `mlflow agent setup`, OpenSharing "agent skills"; vendor treats skill content as user responsibility | One researcher, one vendor; may not generalise; vendors may add signing and scanning quickly | Signed, catalog-only skill loading becomes the default with no further public exploit reports | moderate for "risk exists", unknown for prevalence |
| H4: Task-level, private-PR benchmarks (held-out tests, sealed history) will replace public leaderboards for internal agent selection | Databricks benchmark design; harness effects of more than 2x in cost | The cost of building such benchmarks may confine them to large firms; results are not published | Organisations keep choosing tools by public benchmarks or price per token | low; n unknown |
| H5: Fast product churn imposes measurable migration cost on agent builders | Supervisor Agent GA (Feb) → legacy (Oct); Genie MCP Beta endpoint sunset after ~5 weeks; MLflow breaking changes in 3.13, 3.14, 3.16 and 3.17 | Churn may be cheap to absorb with agent help | Measured migration minutes per change stay near zero | moderate for churn, unknown for cost |

These are hypotheses for testing, not company strategy or fact.

## 7. Implications for the GitHub 1000 study

M1–M7 follow the [research mission](../../../docs/AI_ERA_CODING_REUSE_RESEARCH_MISSION.md).

| M1–M7 construct | Possible observable effect | Study design to test it | Negative/null explanation | Measurement boundary |
|---|---|---|---|---|
| M1 workflow change | Coding agents configured centrally with skills, MCP and routing; harness choice becomes a variable | Record harness, model and skill set per opt-in task | Configuration is not usage; vendor counts (e.g. "61 billion input tokens") are not study data | Consented workflow logs only |
| M2 accepted quality / review cost | Harness and model choice change cost per accepted task, not only per token | Same frozen tasks across harnesses with held-out tests, sealed history and all attempts in the denominator (§8) | No quality difference once leakage is removed | Accepted-task unit; no LLM judge |
| M3 discovery | Press, funding ($188B/$190B) and Summit volume dominate visibility | Separate press counts from reuse | Visibility is not reuse | Stars, funding and HN points never used as outcomes |
| M4 verified external reuse | Third-party engines adopt UC/Delta APIs (DuckDB); OpenSharing and Omnigent released as OSS | Trace consented downstream repos that execute these integrations | Code presence without execution | Pinned commits; executed tests only |
| M5 reuse vs generate, rights and security | Mixed licences (Apache-2.0 vs the source-available Databricks License); many MLflow advisories; skill-borne exfiltration | Licence and advisory check before reuse; treat skills as dependencies | Popular tools are not automatically reusable or safe | Licence file at a pinned commit; advisory DB snapshot date |
| M6 total cost and environment | Vendor "30%+", "35%" and "56%" cost-saving claims; budgets; billing corrections | Measure task cost and human minutes; do not convert to energy | Cost shifts to review or migration | No kWh/CO2e inferred from tokens or dollars |
| M7 maintainer interventions | Held-out-test task benchmarks; sealed history; skill provenance pinning | §8 experiment | Intervention adds overhead without changing decisions | Synthetic or maintainer-owned tasks until approval |

Company adoption claims ("More than 20,000 organizations", "thousands of customers" for Lakebase, customer quotes) are **not** independent task outcomes or verified reuse.

## 8. One practical, falsifiable change for the maintainer's own repositories

**Repository/component:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study), offline unit-test suite (`python -m unittest discover -s tests -v`). The run is **network-free**. The disabled Trending `capture` command stays disabled.

**Candidate practice (not yet validated):** Before changing the default coding-agent setup, evaluate candidate configurations on a **small private benchmark built from the repository's own merged PRs**. Each task uses held-out tests and **sealed git history**, the leakage guard Databricks reported needing (CI2026-071-020). Reuse first: build it from the existing `unittest` suite and `git worktree`, not a new framework or a Databricks product. Gateways, routers and Databricks services are out of scope; they are not needed to test the practice.

**Treatment/control and frozen comparable task:**

- **Task set:** freeze up to 12 merged PRs that each added or changed tests. A person other than the agent operator selects them, rewrites the PR description into a goal-only prompt (solution removed) and confirms the held-out tests fail before the change. Tests are kept out of agent context.
- **Control (A):** the maintainer's current agent setup, run in a fresh worktree checked out at the PR's parent commit.
- **Treatment (B):** the same model and setup, but with a minimal context (no repository-wide instruction files beyond `AGENTS.md`). Record exact agent/CLI and model versions.
- **Both arms:** network disabled, git history sealed (shallow clone at the parent commit, no remote), same time budget, randomised order.
- **Accepted-task unit:** one patch that passes the held-out tests and the full suite and is accepted by the maintainer without rework.

**Success and guardrails:**

- **Primary measure:** accepted tasks out of all assigned tasks, with refused, failed and timed-out runs included.
- **Leakage guard:** any run that reads the original commit or the held-out tests is invalid, and is detected from transcripts.
- **Security guardrail:** no credentials or personal data in either environment.
- **Dependency guardrail:** no new dependency added.
- **Measured human work:** task-construction minutes, per-task review minutes and minutes spent debugging the environment.
- **Spend limit:** use only the maintainer's existing subscription tools. No paid API spend without explicit approval.
- **Energy limit:** no energy or CO2e figures unless metered.
- **Authorship:** commit authorship stays with the maintainer. Agent identity is recorded only in the private run log, never as commit attribution.

**Stop/reversal rule:**

- **Before running:** stop if fewer than 8 eligible PRs with discriminating tests can be frozen in 3 hours of human time.
- **During the run:** stop as soon as any leakage or credential exposure is observed.
- **After the run:** keep the control setup if treatment does not raise accepted tasks by at least 2 of 12, or if it adds more than 5 review minutes per task.

**No trial executed; no effect estimated.**

## 9. Findings, uncertainties and review outcome

- **Observed/shipped (documentary):**
  - MLflow 3.12–3.17 releases, with PyPI upload times confirmed.
  - CLI 1.0.0 and the April 19 backports.
  - UC OSS 0.5.0 and Delta 4.3.0.
  - OpenSharing and Omnigent repos (Apache-2.0).
  - Unity Gateway CLI repo (source-available).
  - MLflow advisories in the GitHub Advisory Database.
  - Dated release-note entries for MCP governance, traces in UC, agent memory Beta, query masking, partner-AI opt-out removal, Genie One MCP GA, and the legacy status of Knowledge Assistant and Supervisor Agent.
- **Claims/announcements only:**
  - Revenue, valuation and customer counts.
  - GA claims for Genie One, Agents and Code, and for Unity Gateway.
  - Smart Routing savings (30%+, 35%, 56%).
  - Lakehouse//RT latency (sub-100 ms at 12,000 QPS; up to 16x).
  - The internal benchmark's results.
  - Customer token counts and the "$1.2 million per year" saving.
  - LTAP, Genie App Builder, cross-region governance and the OpenSharing partner list.
- **Conjectures and unknowns:** H1–H5. Real task outcomes, actual adoption, skill-exploit prevalence, energy, and incident history are all unknown (the official status page shows current state only).
- **Important contradictory or null evidence:**
  - (a) **Genie pricing.** Free usage was announced on 2026-07-15 as "through January 31, 2027", but a 2026-08-03 note says the promotion "was previously set to end on July 31, 2026" and was extended. The dated notes appear to have been edited after the fact.
  - (b) **April Supervisor API entry.** It now reads "(deprecated)", which also suggests retroactive edits.
  - (c) **GHSA-gq3w-7jj3-x7gr.** It is listed as fixed in 3.8.0rc0 (advisory published 2026-02-21), yet the default-password removal citing it shipped in 3.16.1 on 2026-09-17.
  - (d) **GHSA-7gwp-5pfp-969j severity.** It is "high" in the repository advisory and "critical" in the global database.
  - (e) **Advisories missing from the global database.** 12 of the 13 GHSA IDs cited in MLflow 3.17.0 were not in the global database when queried on 2026-10-16.
  - (f) **Auto-approve.** The vendor note recommends keeping it off for production data, while PromptArmor says it is documented as the default and recommended mode.
  - (g) **Openness claims vs critics.** Vendor openness claims sit against competitor critiques of Unity Catalog's Iceberg catalog requirement (Onehouse) and benchmark non-reproducibility (ClickHouse). Both critics are interested parties.
  - (h) **Valuation.** It was $188B at term sheet and $190B at close.
  - (i) **Display dates vs meta times.** Several press releases show a different date from their meta timestamp (Jul 16 vs 2026-07-17T02:15; Aug 13 vs 2026-08-12T23:45; Sep 24 vs 2026-09-23T19:03). Displayed dates were used.
  - (j) **PromptArmor URL.** The original URL redirects to a retitled page.
  - (k) **Unverified outages.** Unity Catalog outage reports surfaced only as third-party status-aggregator snippets (E0) and were not used.
- **#56 candidates (not minted):**
  - PromptArmor, 2026-10-05.
  - Phoronix, 2026-06-10 (OpenSharing).
  - TechCrunch, 2026-07-17.
  - DuckDB, 2026-05-07.
  - ClickHouse, 2026-06-30, and Onehouse, 2026-06-11. These are interested-party critiques and are labelled as such.
  - Each needs a human reading before an ID is assigned.
- **Reviewer links and audit date:** none yet. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.
