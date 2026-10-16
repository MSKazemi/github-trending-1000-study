# Glean — provisional six-month technology intelligence screen (087)

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** This report, its [event ledger](087-glean.events.csv) and [search log](087-glean.search-log.md) are an AI-assisted first-pass documentary source screen. No qualified human has reviewed them. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open. Nothing here is a verified task outcome, an adoption measure or an endorsement.

- **Company watchlist ID:** 087
- **Research issue:** [#155](https://github.com/MSKazemi/github-trending-1000-study/issues/155); evidence corpus link [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56) (no `NEWS-YYYY-NNNN` item minted here; candidates listed in §9).
- **Ownership and product boundaries (as of 2026-10-12):** Glean Technologies, Inc. (legal name in the [docs.glean.com](https://docs.glean.com/release-notes) footer; "Glean Technologies Inc." in [SiliconANGLE, 2026-08-26](https://siliconangle.com/2026/08/26/glean-unveils-tau-desktop-workspace-claims-token-cost-edge-over-claude/)). Privately held and venture-backed; TechCrunch and SiliconANGLE both report the last round as a $150M Series F at a $7.2B valuation in June 2025 (pre-window baseline). No parent company, acquisition of Glean or brand rename was found. In-window the company formalised local entities in Australia and (per the May 28 release) Canada. Press-release datelines say Mountain View, CA (and San Francisco for Glean:GO); the press page footer gives a San Francisco address. Filing-level corporate verification was **not** performed.
- **Product URL and company newsroom:** [glean.com](https://www.glean.com/), [press](https://www.glean.com/press), [blog](https://www.glean.com/blog), [developer changelog](https://developers.glean.com/changelog), [API deprecation list](https://developers.glean.com/deprecations), [product release notes](https://docs.glean.com/release-notes), [gleanwork GitHub org](https://github.com/gleanwork), PyPI [`glean-api-client`](https://pypi.org/project/glean-api-client/), [`glean-indexing-sdk`](https://pypi.org/project/glean-indexing-sdk/), [`glean-agent-toolkit`](https://pypi.org/project/glean-agent-toolkit/).
- **Analysis window:** 2026-04-12 to 2026-10-12 inclusive; accessed 2026-10-16.
- **Researcher / factual reviewer / review date:** AI-assisted screen / **pending** / **pending**.
- **Status:** screened (provisional); 39 ledger rows across all seven calendar segments.
- **Source coverage:** press index (11 in-window releases, all fetched as raw HTML), blog index (~60 in-window posts listed, 25 fetched), developer changelog and deprecation list, GitHub org metadata/releases via `gh api`, PyPI JSON and npm registry, NVD and GitHub Advisory queries, Hacker News Algolia, two web searches, and independent coverage (TechCrunch, SiliconANGLE, The Register, IT Brief UK, No Jitter, ITPro, CRN Australia). The status page (HTTP 403), AI Business (HTTP 403) and The Information (paywall) were inaccessible. See the [search log](087-glean.search-log.md).

## 1. Search and inclusion audit

Summary only; exact requests, opened URLs and exclusions are in the [search log](087-glean.search-log.md). Search-engine totals were not exposed and are recorded as **unknown**, not zero.

| Search run UTC | Site/engine | Full query and dates | Found | Screened | Included | Excluded/why | Coverage limitation |
|---|---|---|---:|---:|---:|---:|---|
| 2026-10-16 | glean.com/press (raw HTML) | press releases and "media coverage" list, 2026-04-12..10-12 | 11 releases + ~70 coverage items | 11 releases | 10 rows | Gartner placement (award), Oct 13 appointment (out of window) | coverage list is vendor-curated |
| 2026-10-16 | glean.com/blog (raw HTML) | blog index with displayed dates | ~60 in window | 25 | 19 rows | SEO/listicle, events, customer stories, awards | pages show "Last updated", not a separate first-publication date |
| 2026-10-16 | developers.glean.com changelog + deprecations | all entries in window | ~40 dated entries | all | 5 rows | routine generated SDK bumps | mutable pages |
| 2026-10-16 | `gh api` gleanwork org, PyPI, npm | repos created/archived/released in window | 11 new repos; 31 Python-client releases | ~15 | 9 rows | sample-app repos, minor SDK versions | releases ≠ use |
| 2026-10-16 | NVD, GitHub Advisory DB, HN Algolia, 2 web searches | Glean security/critical coverage | 1 CVE (name collision), 0 advisories, 15 HN hits | all | 0 rows | unrelated products named "Glean" | snippet-only results graded E0, unused |

## 2. Verified company/product identity and baseline

Glean sells a hosted "Work AI" platform: permission-aware enterprise search over what the vendor calls "more than 250 connectors", an Enterprise Graph/index, Glean Assistant (chat), Glean Agents (no-code and API-built agents), Glean Protect (governance), a model hub (30+ models per the vendor), and remote MCP servers. The core service is **proprietary SaaS**. The open-source surface is client tooling in the [gleanwork](https://github.com/gleanwork) org: generated API clients (Python, TypeScript, Go, Java; MIT), the Glean CLI (MIT), the Indexing SDK (MIT), the agent toolkit (MIT), MCP configuration packages (MIT), coding-agent plugins (MIT/Apache-2.0), and in-window `pluginpack` (MIT). Some repos (`open-api`, `glean-cookbook`, `glean-developer-site`) show **no detected licence** via the GitHub API on 2026-10-16.

Pre-window baseline (context only, not counted): $200M ARR in December 2025 (restated in the May 3 release); remote MCP server and MCP-in-Glean launched earlier (blog "Introducing MCP in Glean", 2026-03-10); Glean Skills launched 2026-02-09; the local npm MCP server was already deprecated in favour of the remote server and the Glean CLI before the window.

## 3. Month-by-month discoveries (six calendar months + partial endpoints)

| Month | Announcements/changes | Primary URLs | Independent reporting | Notes or no-result limitations |
|---|---|---|---|---|
| 2026-04-12..30 | Waldo search-planning model (Apr 28); harness write-up: skills loaded progressively (Apr 29) | [blog](https://www.glean.com/blog/waldo-launch), [blog](https://www.glean.com/blog/harness-context-manager) | AI Business (Apr 29) returned HTTP 403 | Thin month for dated releases; minor SDK bumps (Python client 0.12.21–0.12.24, Indexing SDK 1.0.0b2) not ledgered |
| 2026-05 | Local MCP path dropped from mcp-config (May 2); ANZ entity (May 3/4); May release + Skills beta, Gainsight, CLI skill consolidation (May 5); ADLC, agent sandbox, access policies (May 12); breaking REST rename (May 12); MCP benchmark (May 13); Custom Metadata API GA (May 18); $300M ARR (May 28) | [press](https://www.glean.com/press), [dev changelog](https://developers.glean.com/changelog) | [No Jitter](https://www.nojitter.com/ai-automation/glean-unveils-framework-for-controlling-ai-agents) May 12; [IT Brief UK](https://itbrief.co.uk/story/glean-says-remote-mcp-server-beats-rivals-in-tests) May 15; [TechCrunch](https://techcrunch.com/2026/05/28/gleans-top-line-crosses-300m-as-ai-budget-cutting-becomes-its-major-selling-point/) May 28 | DevOps Digest returned HTTP 406 |
| 2026-06 | Snowflake in Assistant GA, `pluginpack` (Jun 2); MCP Gateway (Jun 3); Nemotron 3 Ultra (Jun 4); Work AI Index (Jun 10); coding-agent plugin repo (Jun 11); FS MCP partners (Jun 16); independent agents beta; local MCP server archived (Jun 30) | [blog](https://www.glean.com/blog/introducing-glean-mcp-gateway), [repo](https://github.com/gleanwork/mcp-server) | [The Register](https://www.theregister.com/ai-and-ml/2026/06/10/brit-workers-waste-nearly-six-hours-a-week-botsitting/5253483) Jun 10 | Meeting notes GA (Jun 9) and Gartner placement (Jun 22) excluded |
| 2026-07 | Python client 0.15.0 breaking (Jul 2); AI Gateway private beta (Jul 8); programmatic-tool-calling harness (Jul 9); sales connectors (Jul 14); agent identity public beta (Jul 15); Databricks GA (Jul 17) | [blog](https://www.glean.com/blog/glean-ai-gateway), [blog](https://www.glean.com/blog/introducing-agent-identity) | none found beyond vendor-curated list | |
| 2026-08 | Triggers API experimental (Aug 20); Partner Network and Client-API agent-endpoint deprecation (Aug 25); Glean:GO: Tau (coming soon), usage controls GA, Cowork benchmark, agent scanning/evals (Aug 26); Indexing SDK 1.0.0 (Aug 27) | [press](https://www.glean.com/press/glean-takes-on-enterprise-ais-biggest-bottlenecks-context-gaps-rising-costs-and-ai-sprawl), [deprecations](https://developers.glean.com/deprecations) | [SiliconANGLE](https://siliconangle.com/2026/08/26/glean-unveils-tau-desktop-workspace-claims-token-cost-edge-over-claude/) Aug 26; [ITPro](https://www.itpro.com/business/business-strategy/glean-expands-enterprise-ai-ecosystem-with-new-partner-program) Aug 27; The Information (paywalled) | |
| 2026-09 | SDKs remove streaming from `chat.create()` (Sep 2); OpenAI B2B marketplace launch partner (Sep 29) | [release](https://github.com/gleanwork/api-client-python/releases/tag/v0.17.0), [blog](https://www.glean.com/blog/glean-openai-b2b-marketplace) | none read; OpenAI-side source not read | Interactive artifacts (Sep 9; no availability stated) and the Jev research post (Sep 29) excluded |
| 2026-10-01..12 | Platform Skills API GA (Oct 2); agent toolkit 0.9.0 (Oct 7); Skills governance GA (Oct 8) | [dev changelog](https://developers.glean.com/changelog), [blog](https://www.glean.com/blog/skills-governance-2026) | none found | Oct 13–15 posts and appointment excluded (out of window) |

## 4. Dated event evidence and capabilities

Full row detail is in the [CSV](087-glean.events.csv) (39 rows, IDs `CI2026-087-001`…`039`). Highlights:

| Event ID | Published UTC / underlying event date | Claim or observed feature | Availability and limitations | Source link (type) | Independent check | E0–E4 working grade |
|---|---|---|---|---|---|---|
| CI2026-087-003 | 2026-05-02 | mcp-config v5.0.0 drops the local MCP path (breaking) | GitHub release | [release](https://github.com/gleanwork/mcp-config/releases/tag/v5.0.0) | dev changelog | E2 |
| CI2026-087-008 | 2026-05-12 | ADLC framework; GA trace views, agent sandbox; beta access policies | mixed GA/beta | [press](https://www.glean.com/press/glean-introduces-the-enterprise-agent-development-lifecycle-codifying-how-enterprises-build-govern-and-measure-ai-agents) | No Jitter (restatement) | E1 |
| CI2026-087-010 | 2026-05-13 | Remote MCP preferred ~2.5x; rivals used ~30% more tokens (~175 queries) | vendor benchmark | [blog](https://www.glean.com/blog/cowork-mcp-eval) | IT Brief UK restates vendor claim | E1 |
| CI2026-087-014 | 2026-06-02 | `pluginpack` packages one skill/MCP source for several AI hosts | npm 0.5.0, MIT, prerelease | [repo](https://github.com/gleanwork/pluginpack) | npm registry | E2 |
| CI2026-087-021 | 2026-06-30 | Local open-source MCP server archived; managed remote server is the supported path | archived | [repo](https://github.com/gleanwork/mcp-server) | npm deprecation messages | E2 |
| CI2026-087-026 | 2026-07-15 | Agents act through their own scoped identities (incl. a GitHub App whose PRs face branch protection) | public beta | [blog](https://www.glean.com/blog/introducing-agent-identity) | none | E1 |
| CI2026-087-030 | 2026-08-25 | Client API agent endpoints deprecated; removal 2027-04-15 | announced | [deprecations](https://developers.glean.com/deprecations) | none | E2 (documentary) |
| CI2026-087-031/033 | 2026-08-26 | Tau desktop workspace "built on an open-source harness"; agent scanning, evals, Claude Code/Cursor authoring | Tau coming soon; betas | [press](https://www.glean.com/press/glean-takes-on-enterprise-ais-biggest-bottlenecks-context-gaps-rising-costs-and-ai-sprawl), [blog](https://www.glean.com/blog/glean-agents-go-2026) | SiliconANGLE: "Tau is not out yet" | E1 |
| CI2026-087-032 | 2026-08-26 | 78% preferred; $0.58 vs $2.98 per task vs Claude Cowork (180+ synthetic queries) | vendor benchmark | [blog](https://www.glean.com/blog/go-glean-cowork) | SiliconANGLE re-expresses figures | E1 |
| CI2026-087-035 | 2026-09-02 | SDKs remove `chat.create()` streaming (breaking) | PyPI 2026-09-02T19:23Z | [release](https://github.com/gleanwork/api-client-python/releases/tag/v0.17.0) | PyPI JSON | E2 |
| CI2026-087-039 | 2026-10-08 | Skill scanning, credential broker, GitHub skill imports GA | GA per vendor | [blog](https://www.glean.com/blog/skills-governance-2026) | none | E1 |

**Feature inventory (vendor-documented, not exercised by us):**

| Area | In-window change | Class |
|---|---|---|
| Models/routing | Waldo search-planning model (Nemotron 3 Nano base); Nemotron 3 Ultra in model hub; auto routing (beta) | vendor claim / shipped |
| Agents | Auto Mode builder, trace views, sub-agents, agent sandbox in VPC, triggers; independent agents (beta); agent identity (public beta); agent scanning (beta); agent evals (private beta); authoring from Claude Code/Cursor | mixed |
| MCP and gateways | MCP Gateway (available); AI Gateway (private beta → beta; LLM support first for Claude Code and Codex); FS and sales MCP/connector partners; memory via MCP GA; skills via MCP coming soon | mixed |
| Developer APIs/SDKs | Custom Metadata API GA; Platform Triggers API experimental; Platform Skills API GA; Indexing SDK 1.0.0; 31 Python-client releases in window with breaking changes in 0.13.0, 0.15.0, 0.16.0, 0.17.0 | shipped (observed) |
| Open-source tooling | `pluginpack` (MIT), coding-agent plugins (`glean-plugins-vnext` Apache-2.0; `codex-plugins` MIT), `glean-auth` (MIT), `glean-cookbook` (no licence detected) | observed |
| Retirements/deprecations | local MCP path removed from config tooling (May 2); local MCP server repo archived (Jun 30); Client API agent endpoints deprecated (Aug 25, removal 2027-04-15) | observed |
| Governance/security | Agent Access Policies (beta); AI usage limits GA; context-aware threat detection (coming soon); skills governance GA | vendor claim |
| Security advisories | none found for Glean packages (NVD keyword and GitHub Advisory DB, 2026-10-16) | null result, not proof of absence |

## 5. What the company says it intends to do

| Verbatim or close paraphrase of public direction (<=25 words per source quoted) | Link/date | Promised horizon | Status (planned, tentative, uncommitted) | Missing/contradictory context |
|---|---|---|---|---|
| Glean Tau, Glean Transform, context-aware threat detection, task management and skills via MCP listed as "Coming soon" | [press, 2026-08-26](https://www.glean.com/press/glean-takes-on-enterprise-ais-biggest-bottlenecks-context-gaps-rising-costs-and-ai-sprawl) | none stated | planned | No date; Tau's open-source harness is unnamed |
| "independent agents will extend proactive AI to longer-running work" | same | none | planned (beta) | No outcome data |
| Client API agent endpoints to be removed 2027-04-15; use Platform API | [deprecations](https://developers.glean.com/deprecations) | 2027-04-15 | committed schedule (vendor) | Page is mutable |
| "Published user-facing local MCP packages are being retired in favor of the managed Glean MCP server." | [mcp-server README](https://github.com/gleanwork/mcp-server) | none | in progress | Moves users from self-run OSS to hosted service |
| "we will invest alongside them" (partners) | [press, 2026-08-25](https://www.glean.com/press/glean-launches-global-partner-network-to-scale-its-growing-enterprise-ai-ecosystem) | none | uncommitted | — |
| Plans to "nearly double its in-market team this year" in ANZ | [press, 2026-05-03](https://www.glean.com/press/glean-expands-to-australia-as-anz-demand-grows-for-secure-enterprise-ai) | 2026 | tentative | — |

These are **company statements**, not forecasts we endorse.

## 6. Independent interpretation: direction and alternative scenarios (researcher's conditional 2027–2031 view)

| Hypothesis for 2027–2031 | Supporting observations | Rival explanations | Disconfirming signals | Confidence/unknowns |
|---|---|---|---|---|
| H1: Enterprise retrieval vendors will reach coding agents mainly through hosted MCP/gateway endpoints, not self-run open-source servers | Local MCP server archived (Jun 30); MCP Gateway; plugins for Claude Code/Codex/Cursor; AI Gateway LLM support "initially for Claude Code and Codex" | Hosting may be chosen for revenue and support cost, not user benefit; self-hosted alternatives may grow elsewhere | Major vendors re-open or maintain self-hostable servers; regulated buyers reject hosted gateways | moderate for Glean; low for the sector |
| H2: Vendor "context reduces tokens" benchmarks will stay unreplicated | May 13 and Aug 26 benchmarks are vendor-designed and vendor-graded on vendor data; press restates them | Proprietary data makes public replication hard even if the effect is real | An independent, pre-registered comparison with a published query set reproduces (or refutes) the cost gap | low; no independent data |
| H3: Agent "skills" become a supply-chain surface needing scanning like packages | Skills governance GA with scanning and GitHub imports; agent scanning beta; CLI consolidated 17 skills; `pluginpack` | Vendor marketing of a threat it sells controls for | No reported skill-borne incidents across vendors by 2028; scanners show negligible detection | low–moderate |
| H4: Generated-SDK churn imposes real migration cost on API reusers | 31 Python-client releases in window; at least four minors (0.13.0, 0.15.0, 0.16.0, 0.17.0) contain changes marked breaking; endpoint renamed within five days | Breaking flags may mark small, rarely used fields | Pinned example repo migrates 0.12→0.17 in minutes with no behaviour change | moderate for churn, unknown for cost |

These are hypotheses for testing, not company strategy or fact.

## 7. Implications for the GitHub 1000 study

| M1–M7 construct | Possible observable effect | Study design to test it | Negative/null explanation | Measurement boundary |
|---|---|---|---|---|
| M1 AI coding-agent change | Coding agents fetch org context through hosted MCP/plugins | Count consented agent sessions that call an MCP context server vs repo-only context | Context servers used only in large enterprises | Consented logs only; vendor "78% of customers adopted MCP and APIs" is not a measure |
| M2 accepted task quality | Context layers may change correctness or only verbosity | Same tasks with/without a context server; hidden acceptance tests | No accepted-task difference | All attempts in denominator; vendor preference rates excluded |
| M3 discoverability | Heavy vendor PR (ARR, benchmarks, partner programme) | Separate press counts from verified reuse | Press is not reuse | Funding/ARR never an outcome |
| M4 verified third-party reuse | OSS clients/SDKs exist (MIT); reuse by third parties unknown | Trace consented downstream repos that import and run `glean-api-client` or `pluginpack` | Packages exist but are used only by Glean customers' internal code | Executed imports at pinned commits only |
| M5 rights/security/provenance | Mixed licences; some repos unlicensed; agent identity for agent-authored PRs; skill scanning | Licence check before reuse; record agent identity on PRs | Unlicensed repos are not reusable regardless of popularity | Licence files at pinned commits |
| M6 review/maintenance and lifecycle cost | Frequent breaking SDK changes; vendor survey reports 6.4 h/week "botsitting" (self-reported) | Measure migration minutes per SDK minor; measure review minutes directly | Self-reported hours do not transfer to our tasks | No kWh/CO2e from tokens or dollars |
| M7 actionable interventions | Progressive-disclosure skills and tool-output truncation as low-cost context practices | See §8 | Practice adds friction without accuracy gain | Synthetic tasks until approval |

Company adoption claims ($300M ARR, customer counts, preference rates) are **not** independent task outcomes or verified reuse.

## 8. One practical, falsifiable change for the maintainer's own repositories

**Repository/component:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study), offline documentation and unit-test suite only (`python -m unittest discover -s tests -v`). The disabled Trending `capture` command stays disabled.

**Candidate practice (not yet validated):** Replace one long, always-loaded agent instruction file with a short core file plus progressively loaded, task-specific "skill" files (the pattern Glean describes in CI2026-087-002 and -024), using plain Markdown already supported by the coding agent in use. Reuse first: no Glean account, no MCP server, no new dependency and no paid API spend without explicit approval.

**Treatment/control and frozen comparable task:** Freeze 10 small synthetic maintenance tasks (e.g., a validator edge case, a CSV-schema check, a docs cross-link fix), each with **hidden acceptance tests written by someone other than the agent operator** and kept out of agent context. Arm A (control): the current `AGENTS.md` unchanged. Arm B: an `AGENTS.md` cut to its mandatory rules, plus 3–4 topic files that the agent is told to open only when the task touches that topic. Same agent, model version, prompt template and time budget; randomized task order. Accepted-task unit: a patch that passes the hidden tests and the full unit suite, and is accepted by the human reviewer without rule violations.

**Success and guardrails:** Primary: accepted tasks / all 10 assigned (refused, failed, timed-out included). Guardrails: zero violations of mandatory rules (capture stays disabled, no network I/O in tests, no write-once evidence overwritten, correct commit author identity); no new dependency; no credentials in agent context. Measured human work: reviewer minutes per task and minutes spent correcting rule violations. Record token counts only if the tool reports them; do not convert them to energy or carbon.

**Stop/reversal rule:** Stop and keep Arm A if Arm B shows any mandatory-rule violation not seen in Arm A, or a lower accepted-task count, or more than 5 extra reviewer minutes per task on average. **No trial executed; no effect estimated.**

## 9. Findings, uncertainties and review outcome

- **Observed/shipped (documentary):** mcp-config 5.0.0 (May 2); glean-cli 0.17.0 (May 5); REST endpoint rename (May 12); Custom Metadata API GA (May 18); `pluginpack` on npm (Jun 2); local MCP server archived (Jun 30); Python-client releases incl. breaking 0.15.0 (Jul 2) and 0.17.0 (Sep 2) with PyPI times confirmed; Triggers API experimental (Aug 20); agent-endpoint deprecation (Aug 25); Indexing SDK 1.0.0 (Aug 27); Platform Skills API GA (Oct 2); agent toolkit 0.9.0 (Oct 7).
- **Claims/announcements only:** Waldo latency/token gains; harness token reductions (45%+ prompt, 24% fewer tokens); MCP benchmark (~2.5x, ~30%); Cowork benchmark (78%, $0.58 vs $2.98, 81%); $300M ARR and customer metrics; "78% of customers have adopted Glean MCP and APIs"; >2,000 partner accreditations; Work AI Index survey figures; all GA/beta statements for hosted features; Tau and other "coming soon" items; OpenAI marketplace partnership.
- **Conjectures and unknowns:** H1–H4 in §6; the identity of Tau's "open-source harness"; actual accepted-task quality; service status/incident history (status page HTTP 403); energy use.
- **Important contradictory or null evidence:** (a) ANZ release shows "Published May 03, 2026" but the dateline reads "May 4, 2026"; (b) Aug 26 press release lists interactive-dashboard refresh as beta/coming soon, while the companion blog lists interactive dashboards as GA and refresh as beta; (c) the AI Gateway was "entering private beta" on Jul 8 and listed as "Beta" on Aug 26; (d) the Cowork benchmark is "per query" in the press release and "per task" in the blog, and SiliconANGLE re-expresses 81%/78% as "5.2-times" and "3.6 times"; (e) TechCrunch's `datePublished` is 2026-05-29T00:44Z for a May 28 PDT article; (f) no in-window Glean security advisory was found; the only NVD "Glean" CVE (CVE-2026-54339) concerns an unrelated self-hosted RSS reader of the same name and was excluded; (g) web search found no reported layoffs, lawsuits, outages or incidents, a null result from snippets only (E0).
- **#56 candidates (not minted):** TechCrunch 2026-05-28; The Register 2026-06-10; IT Brief UK 2026-05-15; SiliconANGLE 2026-08-26; ITPro 2026-08-27. Each restates vendor claims; a human must read each before a `NEWS-YYYY-NNNN` ID is assigned, and syndicated copies must not be counted twice.
- **Reviewer links and audit date:** none yet. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

## Independent source spot-check (2026-10-16)

A second agent re-fetched the cited sources (raw HTML via `curl`, GitHub REST API, PyPI and npm registry JSON) and compared dates, figures and quotes with the raw text. 24 ledger rows checked: 24 confirmed, 0 corrected, 0 unverifiable, 0 wrong. No CSV or report change was needed.

| Row | Outcome | Note |
|---|---|---|
| CI2026-087-001 | confirmed | "Last updated Apr 28, 2026"; "reinforcement-learned agentic search model that runs before a frontier model"; Nemotron 3 Nano base; ~250 ms vs ~3s; ~50% lower latency, ~25% fewer tokens, "no quality regression" |
| CI2026-087-002 | confirmed | "Last updated Apr 29, 2026"; "reduced our own system prompt by 45%+" |
| CI2026-087-003 | confirmed | GitHub release 2026-05-02T23:44Z; "drop local MCP path; add cliVersion pin support"; repo MIT |
| CI2026-087-004 | confirmed | "Published May 03, 2026" with dateline "May 4, 2026"; >$200M ARR in December 2025; ANZ customer base "more than 60 percent"; "nearly double its in-market team" |
| CI2026-087-007 | confirmed | GitHub release 2026-05-05T18:40Z; "consolidate 17 Agent Skills into one skill with reference files" |
| CI2026-087-009 | confirmed | Changelog May 12 2026 breaking change replaces `/actions/{actionPackId}/auth`; the old path is listed as added on May 7 2026 |
| CI2026-087-010 | confirmed | "Last updated May 13, 2026"; Claude Cowork harness with Claude Sonnet 4.6; ~175 queries; ~2.5x preference; ~30% more tokens |
| CI2026-087-011 | confirmed | Changelog May 18 2026: Custom Metadata API generally available |
| CI2026-087-012 | confirmed | "Published May 28, 2026"; $300M ARR 15 months after $100M; >250 features; Fortune 500 nearly doubled; 85%+ in 5+ departments; 45% wDAU/wMAU; Canada and Australia entities; TechCrunch `datePublished` 2026-05-29T00:44Z, $7.2B at $150M Series F |
| CI2026-087-014 | confirmed | Repo created 2026-05-30, MIT; npm first version 0.5.0 at 2026-06-02T00:15Z |
| CI2026-087-016 | confirmed | "Published Jun 04, 2026"; 30+ models; Waldo 50%/25%; "91% of frontier LLM completeness" |
| CI2026-087-017 | confirmed | "Published Jun 10, 2026"; 6,000 workers (US/UK/Australia); 87%, 13%, ~11 hours, 6.4 hours botsitting; The Register reports UK subset of 1,500 and attributes the institute to Glean |
| CI2026-087-018 | confirmed | Repo created 2026-06-11, Apache-2.0; latest default-branch commit 2026-08-20 |
| CI2026-087-021 | confirmed | Archive README commit authored 2026-06-29, merge 2026-06-30; repo archived; npm `modified` 2026-06-30T15:09Z; latest version carries a deprecation message |
| CI2026-087-022 | confirmed | GitHub release 2026-07-02T19:19Z; PyPI 0.15.0 2026-07-02T19:19Z; 31 GitHub releases of api-client-python in the window |
| CI2026-087-024 | confirmed | "Last updated Jul 09, 2026"; 100% programmatic tool calling; 24% fewer tokens |
| CI2026-087-029 | confirmed | "Published Aug 25, 2026"; "more than 2,000 Glean accreditations" |
| CI2026-087-030 | confirmed | Deprecation list: Client API agent endpoints "Deprecation introduced on 2026-08-25", removal date 2027-04-15 |
| CI2026-087-031 | confirmed | "Published Aug 26, 2026"; Tau "built on an open-source harness"; GA/Beta/Coming soon lists match; SiliconANGLE "Tau is not out yet", $7.2B Series F |
| CI2026-087-032 | confirmed | "Last updated Aug 26, 2026"; 180+ synthetic queries on Glean's own production data; 78% preference; $0.58 vs $2.98; 81%; SiliconANGLE 5.2x and 3.6x. The comparison model named in the post is Claude Sonnet 5 |
| CI2026-087-034 | confirmed | GitHub release 2026-08-27T19:07Z; PyPI 1.0.0 2026-08-27T19:07Z; MIT |
| CI2026-087-035 | confirmed (dates) | GitHub release 2026-09-02T19:22Z; PyPI 0.17.0 2026-09-02T19:23Z; release body not re-read |
| CI2026-087-037 | confirmed | Changelog October 2 2026: Skills API GA, no X-Glean-Include-Experimental header; TypeScript v0.20.16 (Oct 3) and Java v0.17.17 (Oct 5) remove the text/event-stream response from `skills.previewsource()` |
| CI2026-087-038 | confirmed (upload and licence) | PyPI 0.9.0 2026-10-07T01:09Z; licence MIT; developer-changelog wording not re-read |

This is an AI-assisted source spot-check, not qualified human factual review; the human review gates listed above remain open.
