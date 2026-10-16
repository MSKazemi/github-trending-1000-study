# ClickHouse — provisional six-month technology intelligence screen (079)

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** This report, its [event ledger](079-clickhouse.events.csv) and [search log](079-clickhouse.search-log.md) are an AI-assisted first-pass documentary source screen. No qualified human has reviewed them. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open. Nothing here is a verified task outcome, an adoption measure or an endorsement.

- **Company watchlist ID:** 079
- **Research issue:** [#147](https://github.com/MSKazemi/github-trending-1000-study/issues/147); evidence corpus link [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56). No `NEWS-YYYY-NNNN` item was minted here. Candidates are listed in §9.
- **Ownership and product boundaries (as of 2026-10-12):** ClickHouse, Inc. ("ClickHouse Inc" in the blog feed copyright) is a privately held, venture-funded company. It develops the Apache-2.0 [ClickHouse](https://github.com/ClickHouse/ClickHouse) database and sells ClickHouse Cloud, BYOC, Managed Postgres, Managed ClickStack and Langfuse Cloud. Acquisitions announced in the official blog feed are pre-window baseline unless marked otherwise: PeerDB (2024-07-30), HyperDX (2025-03-13; it became the ClickStack UI), LibreChat (2025-11-04; the base of ClickHouse Agents), Langfuse (2026-01-16) and, **in window**, RunReveal (2026-09-01). **Langfuse is watchlist row 059 with the same parent.** Its product events are screened there and are not duplicated here, and the two rows are not independent ownership groups. Filing-level corporate verification was **not** performed, and no SEC/EDGAR source was contacted.
- **Product URL and company newsroom:** [clickhouse.com](https://clickhouse.com/), [blog](https://clickhouse.com/blog) ([RSS](https://clickhouse.com/rss.xml)), [docs changelog](https://clickhouse.com/docs/whats-new/changelog), [security changelog](https://clickhouse.com/docs/whats-new/security-changelog), [status](https://status.clickhouse.com/), [GitHub org](https://github.com/ClickHouse).
- **Analysis window:** 2026-04-12 to 2026-10-12 inclusive. Accessed 2026-10-16.
- **Researcher / factual reviewer / review date:** AI-assisted screen / **pending** / **pending**.
- **Status:** screened (provisional). 39 ledger rows cover all seven calendar segments.
- **Source coverage:** the full blog RSS (212 in-window items listed, about 55 opened as raw HTML), the docs changelog and security changelog, GitHub releases, repos, advisories and issue search via `gh api`, PyPI JSON, the NVD CVE API, the status-page RSS (last 15 incidents only, Jul 22 to Oct 12), and Hacker News Algolia story search (258 in-window "ClickHouse" stories reported; third-party links screened). Independent sources read: PostHog, Let's Encrypt, Grafana Labs, VulnCheck, NVD and the RunReveal blog. Web search was not used (budget exhausted). See the [search log](079-clickhouse.search-log.md).

## 1. Search and inclusion audit

Summary only. Exact requests, opened URLs and exclusions are in the [search log](079-clickhouse.search-log.md).

| Search run UTC | Site/engine | Full query and dates | Found | Screened | Included | Excluded/why | Coverage limitation |
|---|---|---|---:|---:|---:|---:|---|
| 2026-10-16 | clickhouse.com RSS + raw HTML | all blog items 2026-04-12..10-12 | 212 | ~55 opened | 28 rows | customer stories, tutorials, Postgres internals, competitive comparisons (log) | `datePublished` metadata often later than the displayed date |
| 2026-10-16 | GitHub API | ClickHouse/ClickHouse releases, advisories, org repos, issue search; clickhousectl, mcp-clickhouse, hyperdx, walshadow, CostBench | 164 server release objects in window; 0 server GHSAs in window | first `x.1` release per series + key repos | 9 rows (+ checks) | patch releases not ledgered individually | issue-close counts are as of access |
| 2026-10-16 | NVD CVE API | `keywordSearch=clickhouse`, pubStart/End in window (two ranges) | 20 CVEs | 20 | 2 rows + 1 advisory row | 17 concern third-party apps that use ClickHouse (pattern noted in §9) | keyword search only |
| 2026-10-16 | HN Algolia | `query=ClickHouse`, `tags=story`, window bounds; `query=RunReveal` | 258 stories | third-party URLs | 2 rows | show-HN projects, forks, competitor launches | a security-claim post returned 404 (§9) |
| 2026-10-16 | status.clickhouse.com RSS | incident history | 15 incidents (Jul 22..Oct 12) | 15 | 0 rows | summarised in §3 | Apr..mid-Jul not shown |

## 2. Verified company/product identity and baseline

ClickHouse is a column-oriented OLAP database (Apache-2.0 per GitHub API; repo created 2016-06-02) with a hosted service, ClickHouse Cloud. During the window ClickHouse described itself as building an "Agentic Data Stack": the database; ClickStack observability (OpenTelemetry + HyperDX UI, MIT); Langfuse for LLM/agent tracing; LibreChat-based ClickHouse Agents; the open-source `mcp-clickhouse` MCP server and Agent Skills (Apache-2.0); `clickhousectl` (Apache-2.0); and chDB (embedded engine). The site also serves an Apache-2.0 [`SKILL.md`](https://clickhouse.com/SKILL.md) agent skill and a docs `llms.txt` index (undated, not ledgered).

Pre-window baseline (context only): the $400M Series D in January 2026, referenced in [the Open House press post](https://clickhouse.com/blog/clickhouse-tops-250m-arr-and-4000-customers) (displayed May 27, 2026), and the acquisitions listed above. The latest entry in the official security changelog is CVE-2025-1385 (fixed 2025-01-05). It credits RunReveal staff for the earlier CVE-2024-22412, which links the in-window acquisition to prior security work.

**Relevance to the study angle (agent telemetry storage and analytics):** ClickHouse is the storage engine under Langfuse, ClickStack and the in-window [tokenomics-viewer](https://github.com/ClickHouse/tokenomics-viewer) (coding-agent token/cost logs). ClickHouse also publishes how it uses coding agents on its own C++ codebase (CI agents and ClickGap).

## 3. Month-by-month discoveries (six calendar months + partial endpoints)

| Month | Announcements/changes | Primary URLs | Independent reporting | Notes or no-result limitations |
|---|---|---|---|---|
| 2026-04-12..30 | Agentic-coding demo (Apr 14); mcp-clickhouse 0.3.0 write-mode guard (Apr 14); clickhousectl tutorial (Apr 16) | [blog](https://clickhouse.com/blog/agentic-coding-app), [release](https://github.com/ClickHouse/mcp-clickhouse/releases/tag/v0.3.0), [blog](https://clickhouse.com/blog/getting-started-clickhousectl) | none found | Google Cloud collaboration (Apr 21, BYOC, Axion, MCP + Antigravity) and Grafana plugin "not a committed roadmap" vision (Apr 15) read, not ledgered (§5) |
| 2026-05 | 26.4 release (May 8); CTO sponsored post on AI coding (May 24); Open House: $250M ARR claim (attributed to the serverless cloud offering), ClickHouse Agents, CostBench, ClickStack MCP/Cloud (May 27) | [26.4](https://clickhouse.com/blog/clickhouse-release-26-04), [TNS](https://thenewstack.io/clickhouse-ai-coding-agents/), [press](https://clickhouse.com/blog/clickhouse-tops-250m-arr-and-4000-customers) | The New Stack item is **sponsored** (first-party) | Managed Postgres beta and executable UDF beta (May 27/30) not ledgered separately |
| 2026-06 | 26.5 (Jun 1); ClickHouse Agents public beta (Jun 9); Stripe Projects agent provisioning (Jun 10); AI-assisted bug-bounty guest post (Jun 26); Databricks benchmark dispute (Jun 29); PostHog moves warehouse to DuckDB (Jun 29) | [agents](https://clickhouse.com/blog/clickhouse-agents-beta), [stripe](https://clickhouse.com/blog/stripe-projects), [dispute](https://clickhouse.com/blog/databricks-reyden-benchmark-transparency-clickhouse) | [PostHog](https://posthog.com/blog/why-we-rebuilt-our-data-warehouse) | 10-year open-source post (Jun 15) used as baseline/context |
| 2026-07 | 26.6 (Jul 3); tokenomics-viewer repo (Jul 6); Docker Hardened Images (Jul 10); WalShadow AGPL-3.0 licence commit (Jul 14); mcp-clickhouse 0.4.1 server-level agent instructions (Jul 17); HyperDX SSRF CVE (Jul 20); hdx-evals MCP benchmark (Jul 22); docs relaunch (Jul 27); rejected CVE (Jul 29); Open Secure AI Alliance (Jul 30); clickhousectl 0.4.0 telemetry (Jul 31) | see CSV | [NVD](https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-63731), [VulnCheck](https://www.vulncheck.com/advisories/hyperdx-ssrf-via-clickhouse-proxy-test-endpoint) | Status page: Jul 22 CDC ClickPipes stuck, Jul 24 ap-southeast-1 monitoring/billing impact (not ledgered) |
| 2026-08 | 26.7 (Aug 6); ClickGap autonomous QA disclosure (Aug 25); Grafana ClickHouse plugin TLS CVE (Aug 27) | [ClickGap](https://clickhouse.com/blog/clickgap-autonomous-qa-for-clickhouse), [Grafana](https://grafana.com/security/security-advisories/cve-2026-19854) | Grafana Labs advisory; GitHub issue search for the bot account | ClickHouse Labs with Andy Pavlo (Aug 3) read, not ledgered (§5). Status: Aug 2 Azure eastus2, Aug 14 AWS us-east-1 connectivity, Aug 17, Aug 23 |
| 2026-09 | RunReveal acquisition, data-agent-mnist benchmark, mcp-clickhouse 0.5.0 hardening (Sep 1); 26.8 LTS, ChatGPT Work/Codex plugin, WalShadow launch (Sep 10); AI Functions (Sep 11); Let's Encrypt self-hosted adoption (Sep 17); 26.9 with `CREATE TOKEN` (Sep 23) | [RunReveal](https://clickhouse.com/blog/clickhouse-welcomes-runreveal), [26.9](https://clickhouse.com/blog/clickhouse-release-26-09) | [RunReveal blog](https://blog.runreveal.com/runreveal-is-joining-clickhouse/) (acquired party), [Let's Encrypt](https://letsencrypt.org/2026/09/17/clickhouse.html) | Microsoft Fabric (Sep 29) and SCIM (Sep 30) read, not ledgered. Status: 8 incidents Sep 1–24 |
| 2026-10-01..12 | Executable UDFs GA with LLM-token example (Oct 5); JWT auth (Oct 8) | [UDF](https://clickhouse.com/blog/executable-udfs-generally-available-on-clickhouse-cloud), [JWT](https://clickhouse.com/blog/introducing-jwt-authentication-in-clickhouse-cloud) | none found | Oct 12 status: support-case creation unavailable |

Per-segment ledger counts: Apr 3, May 5, Jun 6, Jul 11, Aug 3, Sep 9, Oct 2.

## 4. Dated event evidence and capabilities

Full row detail is in the [CSV](079-clickhouse.events.csv) (39 rows, IDs `CI2026-079-001`…`039`). Highlights:

| Event ID | Published UTC / underlying event date | Claim or observed feature | Availability and limitations | Source link (type) | Independent check | E0–E4 working grade |
|---|---|---|---|---|---|---|
| CI2026-079-005 | 2026-05-24 | CTO: ~700 agent-assisted test/CI PRs in Jan–Feb 2026; CI findings ~200/day → 3–5 per 10M runs; review bot on Copilot CLI | practice report; **sponsored post** | [The New Stack](https://thenewstack.io/clickhouse-ai-coding-agents/) (sponsored, first party) | none | E1 |
| CI2026-079-007 | 2026-05-27 | CostBench presented as "open" | LICENSE is CC BY-NC-SA 4.0 (non-commercial) | [blog](https://clickhouse.com/blog/costbench-data-warehouse-cost-performance) | [LICENSE](https://github.com/ClickHouse/CostBench/blob/main/LICENSE) | E2 (licence) |
| CI2026-079-010 | 2026-06-09 | ClickHouse Agents beta: LibreChat-based, sandboxed interpreter, Claude Sonnet/Haiku default | Cloud-only beta; launch-date wording conflicts | [blog](https://clickhouse.com/blog/clickhouse-agents-beta) | none | E1 |
| CI2026-079-016 | 2026-07-06 | tokenomics-viewer: local-first token/cost analytics for coding-agent logs on ClickHouse | ISC; README installer uses pre-transfer namespace | [repo](https://github.com/ClickHouse/tokenomics-viewer) | GitHub API | E2 |
| CI2026-079-018/034 | 2026-07-14 / 2026-09-10 | WalShadow licensed AGPL-3.0; launch post says "open-source" without naming licence | copyleft differs from Apache-2.0 core | [commit](https://github.com/ClickHouse/walshadow/commit/4225a9b87f), [blog](https://clickhouse.com/blog/introducing-walshadow) | GitHub API spdx | E2 |
| CI2026-079-020 | 2026-07-20 / fix 2026-07-17 | HyperDX (ClickStack UI) SSRF CVE-2026-63731, fixed 2.31.0 | NVD "Deferred"; third-party CNA | [NVD](https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-63731) | [VulnCheck](https://www.vulncheck.com/advisories/hyperdx-ssrf-via-clickhouse-proxy-test-endpoint), GitHub release/issue/PR | E2 |
| CI2026-079-025 | 2026-07-31 | clickhousectl opt-out telemetry records whether it ran under a detected coding agent | payload not inspected | [blog](https://clickhouse.com/blog/clickhousectl-v0-4-0) | [release](https://github.com/ClickHouse/clickhousectl/releases/tag/v0.4.0) | E2 |
| CI2026-079-027 | 2026-08-25 | ClickGap autonomous QA agent files issues/PRs without per-item human approval; ~500 issues / ~200 PRs | `clickgapai` (GitHub type User): 506 issues and 244 PRs created ≤ Aug 25 | [blog](https://clickhouse.com/blog/clickgap-autonomous-qa-for-clickhouse) | GitHub search API | E2 (counts), E1 (quality) |
| CI2026-079-028 | 2026-08-27 | Grafana ClickHouse plugin dropped TLS over PDC (CVSS 6.1), fixed ≥4.21.1 | plugin in grafana org, co-developed | [Grafana advisory](https://grafana.com/security/security-advisories/cve-2026-19854) | NVD | E2 |
| CI2026-079-031 | 2026-09-01 | mcp-clickhouse 0.5.0: Host/Origin validation default; destructive-op gate widened | breaking; 0.6.0 and 0.7.0 followed within three weeks | [release](https://github.com/ClickHouse/mcp-clickhouse/releases/tag/v0.5.0) | PyPI upload times | E2 |
| CI2026-079-036 | 2026-09-17 | Let's Encrypt runs self-hosted open-source ClickHouse warehouse | adopter account | [Let's Encrypt](https://letsencrypt.org/2026/09/17/clickhouse.html) | — | E2 (independent documentary) |
| CI2026-079-037 | 2026-09-23 | 26.9 `CREATE TOKEN` scoped, time-limited credentials for apps/CI/agents (default TTL 30 min per changelog) | not exercised | [blog](https://clickhouse.com/blog/clickhouse-release-26-09) | [changelog](https://clickhouse.com/docs/whats-new/changelog) | E2 |

**Feature inventory (vendor-documented, not exercised by us):**

| Area | In-window change | Class |
|---|---|---|
| Agent tooling (OSS) | mcp-clickhouse 0.3.0 → 0.7.0 (write gating, OAuth/OIDC, MCP Registry, server-level Agent Skills instructions, Host/Origin validation, FastMCP 4); clickhousectl 0.1.18 → 0.4.2 (agent-aware defaults, telemetry); ClickStack MCP server; Agent Skills; hdx-evals; data-agent-mnist | shipped (Apache-2.0 / MIT) |
| Agent products (Cloud) | ClickHouse Agents beta (Claude, LibreChat), Agents for Managed Postgres, AI Notebooks beta, ClickStack AI dashboard generation, ChatGPT Work/Codex plugin, Stripe Projects provisioning (preview) | beta / preview |
| Agent telemetry and memory | Langfuse (row 059), tokenomics-viewer, chDB "local agent memory" and "durable layer" posts (Jul 7, Sep 28), llm-token-udf | mixed; vendor posts |
| AI in SQL | AI Functions (`aiGenerate` … `aiSimilarity`), beta; Cloud private preview; executable UDFs GA | beta / GA |
| Identity/security | `CREATE TOKEN` (26.9), SCIM 2.0 (Sep 30), JWT/OIDC (Oct 8), Docker Hardened Images (Jul 10) | shipped per vendor |
| Licensing | Core Apache-2.0; WalShadow AGPL-3.0; CostBench CC BY-NC-SA 4.0; HyperDX MIT; tokenomics-viewer ISC; `silk` reports NOASSERTION | observed via GitHub API/LICENSE |
| Release cadence | Monthly server releases 26.4–26.9 (26.8 LTS); 164 GitHub release objects in window, including daily backport patches | observed |

## 5. What the company says it intends to do

| Verbatim or close paraphrase of public direction (<=25 words per source quoted) | Link/date | Promised horizon | Status (planned, tentative, uncommitted) | Missing/contradictory context |
|---|---|---|---|---|
| "During private preview, we are building automatic schema tuning … with dedicated query compute for agentic workloads planned after preview completes." | [ClickStack Cloud, 2026-05-27](https://clickhouse.com/blog/clickstack-cloud-private-preview) | after preview | planned | no date |
| In the alliance "we're building open instrumentation for agent forensics, open evaluation pipelines … and reference architectures for air-gapped agent observability." | [2026-07-30](https://clickhouse.com/blog/open-secure-ai-alliance) | none | announced only | no deliverables dated |
| Grafana plugin ideas "reflect what we've been exploring and prototyping, not a defined or committed roadmap." | [2026-04-15](https://clickhouse.com/blog/grafana-plugin-vision) | none | explicitly uncommitted | partly shipped per [Aug 13 post](https://clickhouse.com/blog/clickhouse-grafana-plugin-4-20) |
| ClickHouse Labs to advance database technology and share "its work openly with the broader community", for ClickHouse and PostgreSQL | [2026-08-03](https://clickhouse.com/blog/andy-pavlo-founding-clickhouse-labs) | none | planned | no output yet in window |
| RunReveal: "We remain a neutral foundation" for companies building security products on ClickHouse | [2026-09-01](https://clickhouse.com/blog/clickhouse-welcomes-runreveal) | none | stated position | acquisition of an ISV built on ClickHouse is in tension with neutrality claims |
| AI Functions "are currently in Beta and functionality is constantly being added" | [2026-09-11](https://clickhouse.com/blog/ai-functions-in-clickhouse) | none | tentative | Cloud remains private preview |

These are **company statements**, not forecasts we endorse.

## 6. Independent interpretation: direction and alternative scenarios (researcher's conditional 2027–2031 view)

| Hypothesis for 2027–2031 | Supporting observations | Rival explanations | Disconfirming signals | Confidence/unknowns |
|---|---|---|---|---|
| H1: Columnar analytics stores become a default backend for agent telemetry (traces, token/cost logs, tool calls) | Langfuse, ClickStack MCP, tokenomics-viewer, llm-token-udf, clickhousectl agent-detection telemetry all store or emit agent telemetry into ClickHouse | Vendor portfolio choice, not industry convergence; DuckDB/SQLite-local or Postgres may serve small teams better (cf. PostHog) | Major agent-observability tools keep row-store or proprietary backends through 2028; local-first tools standardise on DuckDB | low–moderate; no market denominator |
| H2: Mature OSS projects will run autonomous agents that file public issues/PRs, gated by evidence rules rather than per-item human approval | ClickGap (506 issues/244 PRs by Aug 25), ClickGap/Groene AI accounts in contributor lists, CTO's "two autonomous agents opening PRs" | One very well-tested codebase with a large CI budget; may not generalise; maintainers elsewhere reject bot reports (the ClickGap post itself cites curl ending its bug bounty) | Maintainer surveys or repo policies banning autonomous bot PRs spread; ClickGap issue closure-as-not-planned share rises | moderate for "happens at ClickHouse", low for generality |
| H3: Vendor "open" agent tooling will carry heterogeneous licences that reusers must check per component | Apache-2.0 core vs AGPL-3.0 WalShadow vs CC BY-NC-SA CostBench vs ISC/MIT tools | Licence choice may be deliberate per component and stable | ClickHouse relicenses components to one permissive licence, or publishes a licence matrix | moderate (observed now) |
| H4: MCP servers become a security surface with breaking hardening cycles | mcp-clickhouse 0.4.0/0.5.0/0.6.0/0.7.0 within ~4 months; Host/Origin validation and destructive-op gates added; server-level instructions to agents | Normal early-protocol churn that will settle | Two consecutive minor releases without breaking security changes by 2027 | moderate for churn; unknown for incident rate |

These are hypotheses for testing, not company strategy or fact.

## 7. Implications for the GitHub 1000 study

| M1–M7 construct | Possible observable effect | Study design to test it | Negative/null explanation | Measurement boundary |
|---|---|---|---|---|
| M1 coding-workflow change | Agents as visible public contributors (ClickGap; AI-labelled contributor names) and agent-detection telemetry in CLIs | Count bot-authored issues/PRs per repo-month with an audited classifier | Labels are self-declared; human-run accounts may use agents invisibly | Never infer undisclosed AI authorship from style |
| M2 accepted quality / review cost | Vendor claims of fewer CI findings and higher MCP accuracy | Independent replication on frozen tasks with hidden acceptance tests | Gains are codebase- or vendor-scenario-specific | Self-evaluations (hdx-evals, data-agent-mnist) are not independent |
| M3 discoverability | MCP Registry, ChatGPT/Codex plugin directory, `SKILL.md`, llms.txt, "half of docs traffic from agents" | Track agent-facing discovery channels separately from stars | Listings ≠ use; traffic claim unsourced | No traffic data accessible |
| M4 first-use and verified reuse | Let's Encrypt self-hosted adoption; PostHog partial move away | Audit named downstream deployments with dates and versions | Single accounts; selection toward success stories | Only public adopter write-ups |
| M5 reuse vs build; rights/security | Mixed licences; SSRF/TLS CVEs in ClickStack UI and Grafana plugin; many third-party SQL-injection CVEs in apps that build ClickHouse SQL strings | Licence + advisory check before reuse; prefer parameterised query APIs | CVE counts reflect disclosure activity, not intrinsic risk | NVD keyword search is incomplete |
| M6 lifecycle cost and environment | CostBench and per-question $ costs; AI Functions and token-pricing UDFs | Record invoices/API spend only where actually billed | Dollar cost ≠ energy; vendor benchmark design bias | No kWh/CO2e inferred |
| M7 maintainer interventions | Agent-oriented CLI defaults, skills files and MCP servers as onboarding | See §8 for a small telemetry-storage test | Agent-facing docs may not change human first-use success | Synthetic tasks only until approval |

Company adoption claims ($250M ARR and 4,000 customers, both stated for the serverless cloud offering; 100M+ Docker pulls, ~48k stars) are **not** independent task outcomes or verified reuse.

## 8. One practical, falsifiable change for the maintainer's own repositories

**Repository/component:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study). The task-cost ledger (`trending_study.task_costs`) and offline unit suite are used **only** with synthetic, network-free fixtures. Trending `capture` stays disabled. No real provider, Copilot/Codex/Claude or human traces are collected without consent and explicit human scientific approval.

**Candidate practice (not yet validated):** Store per-task agent-run records (synthetic fixtures) in a local, embedded analytics engine for querying, instead of the current write-once JSON/CSV files plus ad-hoc Python aggregation. Reuse first: compare **chDB** (embedded ClickHouse, Apache-2.0, exact PyPI version pinned and recorded) against **DuckDB** (MIT) and the **status quo** (standard-library `csv`/`json`). Do not build a new store, and do not adopt a hosted service.

**Treatment/control and frozen comparable task:** Freeze 10 analysis questions over a synthetic ledger fixture (e.g., accepted tasks by arm, missing-record counts kept as missing, per-task review minutes). A person other than the implementer writes hidden expected answers. Arms: A = status quo Python, B = DuckDB, C = chDB. Each arm is implemented by the maintainer under the same time budget. Accepted-task unit: one question whose answer matches the hidden expectation **and** treats missing values as missing (never 0).

**Success and guardrails:** Primary: accepted questions / 10 per arm, with every attempt in the denominator. Guardrails: no network I/O (verified by running offline); the write-once artifacts are never modified; no new runtime dependency in `pyproject.toml` unless it wins; the licence and wheel provenance are recorded; the full unit suite stays green. Measured human work: setup minutes, minutes per question, and review minutes by a second person. No energy or CO2e estimate is made unless it is metered. No paid API is used.

**Stop/reversal rule:** Keep arm A if neither B nor C answers more questions correctly, or if either adds more than 15 setup minutes, more than 50 MB of installed dependencies, or any silent zero-filling of missing values. Stop immediately if a candidate needs network access or alters fixture files. **No trial executed; no effect estimated.**

## 9. Findings, uncertainties and review outcome

- **Observed/shipped (documentary):** monthly server releases 26.4–26.9 (GitHub release timestamps); mcp-clickhouse 0.3.0–0.7.0 (PyPI upload times); clickhousectl releases through v0.4.2; new public repos and their licences (GitHub API); HyperDX SSRF fix 2.31.0 and CVE-2026-63731; Grafana plugin CVE-2026-19854 fix ≥4.21.1; CVE-2026-51992 rejected; RunReveal acquisition (both parties' posts); ClickGap account activity counts (GitHub search).
- **Claims/announcements only:** ARR/customer counts, CostBench "23x", MCP benchmark (18% / 26% / 2.4x), agent benchmark scores and $ costs, CTO CI-finding reductions, "more than half of developer docs traffic comes from coding agents", WalShadow latency/throughput, Docker pull counts, and the forward statements in §5.
- **Conjectures and unknowns:** H1–H4 in §6; actual quality of agent-generated contributions; energy use; status history before 2026-07-22.
- **Important contradictory or null evidence:**
  - (a) PostHog (2026-06-29) moved its general-purpose warehouse to DuckDB while keeping ClickHouse for analytics.
  - (b) The Databricks–ClickHouse benchmark dispute (only ClickHouse's side was read).
  - (c) A guest post claims "a few real vulnerabilities" found with AI, but no in-window entry appears in the security changelog or the server GHSA list (null public trace).
  - (d) An HN story dated 2026-09-18, "ClickHouse permission system has a trivial bypass", links to a Substack post that returned **HTTP 404** and is absent from the blog's post API. It is **unverifiable (E0) and not ledgered**.
  - (e) Date conflicts: the 26.4 changelog says 2026-04-30, the GitHub release 2026-05-05 and the blog 2026-05-08. Several blog posts carry `datePublished` metadata weeks after their displayed date. ClickHouse Agents' launch is described as both May 27 (Open House) and "June 2026".
  - (f) Contributor and star figures: "more than 2000 contributors" (Jun 15 post) vs "over 2.6k contributors and nearly 48k stars" (May 28 post).
  - (g) "Open" CostBench is non-commercial CC BY-NC-SA 4.0. The WalShadow launch post omits its AGPL-3.0 licence.
  - (h) The NVD keyword search found 17 in-window CVEs in **third-party** applications that build ClickHouse SQL unsafely (SigNoz, OpenPanel, OpenMeter, Aptabase and others). These are not ClickHouse defects, but they are a reuse-security pattern.
- **#56 candidates (not minted):** The New Stack 2026-05-24 (sponsored, so not independent); PostHog 2026-06-29; Let's Encrypt 2026-09-17; Grafana advisory 2026-08-27; RunReveal blog 2026-09-01. Each needs human reading before a `NEWS-YYYY-NNNN` ID is assigned.
- **Reviewer links and audit date:** none yet. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

## Independent source spot-check (2026-10-16)

An independent reviewer re-fetched the cited sources on 2026-10-16. Pages were retrieved as raw HTML with a generic browser User-Agent after checking each host's robots.txt. GitHub, PyPI and NVD were queried through their APIs. No personal identifier was sent to any site.

| Row | Outcome | Note |
|---|---|---|
| CI2026-079-002 | confirmed | Release notes list `CLICKHOUSE_WRITE_ACCESS` with DROP/TRUNCATE protection, `CLICKHOUSE_SNI` and lazy-loaded/optional chDB. GitHub release 2026-04-14T17:26:46Z; PyPI upload 2026-04-14T17:28:40Z; PyPI `license_expression` Apache-2.0. |
| CI2026-079-004 | confirmed | 39 / 45 / 238 and the new-contributor names "ClickGap AI Bot" and "Groene AI" appear in the raw text. Displayed date May 8, 2026; GitHub release v26.4.1.1141-stable 2026-05-05T18:25:17Z. |
| CI2026-079-005 | confirmed | `datePublished` 2026-05-24T14:00Z. The page says "ClickHouse sponsored this post" and names Insight Partners as a shared investor. The text also has "Since Opus 4.5", ~700 PRs, ~200 findings a day to 3–5 per 10 million test runs, a bot that "invokes Copilot CLI", and two autonomous agents. |
| CI2026-079-006 | **corrected** | The press text reads "ClickHouse's serverless cloud offering has crossed over $250 million in annual run-rate revenue … bringing its total to 4,000". The row and report §3/§7 now attribute both figures to the serverless cloud offering rather than to the company as a whole. "Full-text search is generally available" is confirmed. |
| CI2026-079-014 | confirmed | Displayed Jun 29, 2026. Raw text has "about 420 QPS", one 30 vCPU node, 15,000 QPS and "roughly 30 to 40 untuned nodes". |
| CI2026-079-017 | confirmed | Displayed Jul 10, 2026. Raw text has "100M+ pulls" and the Ubuntu 22.04 base. |
| CI2026-079-018 | confirmed | Commit 4225a9b87f dated 2026-07-14T16:11Z. Its message reads "AGPLv3 / clickhouse-c-rs stays Apache v2" and it touches LICENSE. GitHub API spdx is AGPL-3.0. |
| CI2026-079-020 | confirmed | NVD: published 2026-07-20, VulnCheck CVSS 3.1 7.7 HIGH and 4.0 6.3 MEDIUM (status Deferred). `@hyperdx/app@2.31.0` was released 2026-07-17T22:31:31Z; issue #2588 was opened 2026-07-03; PR #2593 was merged 2026-07-17T18:14:58Z. |
| CI2026-079-021 | confirmed | Displayed Jul 22, 2026. Raw text has 18% / 26% / 2.4x, seeded synthetic telemetry, Claude agents and blind scoring. |
| CI2026-079-022 | confirmed | Displayed Jul 27, 2026. The quote "more than half of developer docs traffic comes from coding agents" is verbatim. |
| CI2026-079-023 | confirmed | NVD: published 2026-07-29, last modified 2026-08-06, status Rejected. The CNA text matches the summary; the permission it names is `pg_execute_server_program`. |
| CI2026-079-027 | confirmed | Displayed Aug 25, 2026. The vendor text has "roughly 500 issues", "around 200 pull requests" and "more than half … closed". A fresh GitHub search (author `clickgapai`, created ≤ 2026-08-25) gives 506 issues, 244 PRs and 333 closed issues. The account was created 2026-03-26. |
| CI2026-079-028 | confirmed | Advisory published 2026-08-27; CVSS 3.1 6.1; fixed >=4.21.1. The library "talks to ClickHouse in the clear". |
| CI2026-079-030 | confirmed | Displayed Sep 1, 2026. Raw text has 201 questions, 29 models, 76.6% and $1 vs $52. The repo is Apache-2.0 and was created 2026-08-24. |
| CI2026-079-032 | confirmed | 98 / 128 / 556, LTS. GitHub release v26.8.1.2041-lts 2026-08-30T13:47:42Z. |
| CI2026-079-034 | confirmed | Displayed Sep 10, 2026. Raw text has ~200 ms and 289K rows/sec. The post never mentions "AGPL", which confirms note (g). |
| CI2026-079-036 | confirmed | Dated September 17, 2026. Three PowerEdge R7715 servers, a "log search SaaS product" and "open source" all appear. |
| CI2026-079-037 | confirmed | 56 / 135 / 464 and CREATE TOKEN appear. GitHub release v26.9.1.1629-stable 2026-09-21T21:25:45Z. |
| CI2026-079-007 (licence check) | confirmed | The CostBench repo was created 2026-05-25. GitHub spdx is NOASSERTION, and LICENSE is CC BY-NC-SA 4.0. |

**Counts:** 19 rows checked: 18 confirmed, 1 corrected, 0 wrong, 0 unverifiable.

**Robots.txt audit:** the search log fetched no path that robots.txt disallows for a generic User-Agent. clickhouse.com, thenewstack.io, posthog.com, letsencrypt.org, grafana.com, blog.runreveal.com and the Substack `/p/` path are all allowed. NVD, HN Algolia and status.clickhouse.com serve no robots.txt.

**Qualification of the search log's "every number … confirmed with grep" statement:** every number re-checked here matched its source. Row 006, however, attributed a figure scoped to one product (the cloud offering) to the whole company. So "confirmed" in the log means the numerals matched, not that their scope was reviewed.

*This is an AI-assisted spot-check, not qualified human review.*
