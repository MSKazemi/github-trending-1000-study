# Baseten — provisional six-month technology intelligence screen (067)

> **PROVISIONAL, AI-assisted first-pass screen (2026-10-16), not reviewed by a qualified human.** This report, its [event ledger](067-baseten.events.csv) and [search log](067-baseten.search-log.md) are documentary source leads. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open. Nothing here is an independently verified task outcome, adoption measurement, security audit or energy estimate.

- **Company watchlist ID:** 067 — Baseten; research issue [#135](https://github.com/MSKazemi/github-trending-1000-study/issues/135); news-corpus link [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56).
- **Ownership and product boundaries (as of 2026-10-12):** contracting entity **Baseten Labs, Inc.** per the [Terms and Conditions](https://www.baseten.co/terms-and-conditions/) (page "Last updated September 15, 2026"). Privately held and venture-financed per its own [Series F post](https://www.baseten.co/blog/announcing-our-series-f/) and [Reuters syndication](https://www.techpartner.news/news/ai-startup-baseten-hits-13-billion-valuation-as-australias-blackbird-makes-record-bet-626878); no parent company was identified. Filing-level ownership was **not** checked. In-window acquisition: **Blaxel** (agent sandboxes), [announced 2026-09-10](https://www.baseten.co/blog/blaxel-is-joining-baseten-to-build-the-future-of-agentic-cloud/). Pre-window baseline: [Inferless acquihire, displayed 2026-02-14](https://www.baseten.co/blog/announcing-the-acquihire-of-inferless-by-baseten/).
- **Product URL and channels checked:** [baseten.co](https://www.baseten.co/), [blog](https://www.baseten.co/blog/), [changelog](https://www.baseten.co/resources/changelog/), [status page](https://status.baseten.co/), GitHub org [basetenlabs](https://github.com/basetenlabs) ([Truss](https://github.com/basetenlabs/truss), [baseten-cli](https://github.com/basetenlabs/baseten-cli), [baseten-switch](https://github.com/basetenlabs/baseten-switch), [baseten-skills](https://github.com/basetenlabs/baseten-skills)).
- **Analysis window:** 2026-04-12 to 2026-10-12 inclusive (UTC dates); sources accessed 2026-10-16.
- **Researcher / factual reviewer / review date:** AI-assisted first pass / **pending** / **pending**.
- **Status:** screened (provisional); 37 dated ledger rows across all seven month segments.
- **Source coverage:** see the [search log](067-baseten.search-log.md). The web-search budget for this session ran out after seven queries, so vendor-partner confirmations (Microsoft AI, OpenAI, Goodfire, NVIDIA) and further independent or critical coverage were **not** retrieved. First-party coverage is much stronger than independent coverage.

## 1. Search and inclusion audit

| Search run (date) | Site/engine | Query or enumeration | Found | Screened | Included | Excluded/why | Coverage limitation |
|---|---|---|---:|---:|---:|---:|---|
| 2026-10-16 | baseten.co blog index (`?page=1..11`, 3 category pages) | full listing; embedded CMS records parsed | 80 posts with CMS time in window (republish-biased) | all titles/summaries; 19 full posts read | 20 rows | model-catalog/tutorial posts; pre-window posts republished in window; posts dated Oct 13–15 | CMS `_publishedAt` is a **republish** time, not the displayed date (see §9) |
| 2026-10-16 | baseten.co `sitemap.xml` → changelog | 237 changelog URLs; 72 most recent fetched individually | 53 with displayed dates in window | 72 | 17 rows (some as `independent_check_url`) | model-availability entries kept as context | Older 165 entries not fetched (pre-window by sitemap order) |
| 2026-10-16 | status.baseten.co API | `/api/v2/incidents.json` | 50 incidents (feed limit) | 50 | 3 rows + monthly counts | minor incidents summarized only | Feed starts 2026-06-03; **Apr 12–Jun 2 incidents not screened** |
| 2026-10-16 | GitHub API (`gh api`) | basetenlabs repos created since 2026-03; releases of 7 repos | 36 repos (several apparent upstream forks) | 7 (fork flag checked) | 4 rows / checks | upstream-project mirrors not screened | API metadata only; code not exercised |
| 2026-10-16 | public web search | 7 queries (listed in search log) | unknown | ~40 result titles | 2 independent rows/checks | crypto/aggregator sites, irrelevant hits | 3 planned queries **not run** (budget exhausted) |

## 2. Verified company/product identity and baseline

Baseten sells hosted inference for open-weight and custom models ("Dedicated Inference", shared "Model APIs" with an OpenAI-compatible endpoint), post-training ("Loops", early access), and, from May–July 2026, distribution services for model labs (Frontier Gateway, Baseten for Model Labs). Its open-source packaging tool **Truss** is MIT-licensed on GitHub; the hosted platform is proprietary. The Sep 10 Blaxel acquisition adds microVM sandboxes for agents. **Baseline before the window (not counted):** Rolling deployments changelog (2026-03-30), Baseten Delivery Network (2026-03-19), NemoClaw harness post (displayed 2026-03-19, CMS republish 2026-04-16), Inferless acquihire (2026-02-14), Series E (reported January 2026 in secondary sources; not fetched).

## 3. Month-by-month discoveries

| Month | Announcements/changes (ledger IDs) | Primary URLs | Independent reporting | Notes or no-result limitations |
|---|---|---|---|---|
| 2026-04-12..30 | Truss v0.16.0 breaking default to Python 3.13 (001); cache-token pricing (002); deprecation notice DeepSeek v3 0324/GLM 4.6 (003); RBAC explainer (004) | [Truss release](https://github.com/basetenlabs/truss/releases/tag/v0.16.0), [changelog](https://www.baseten.co/resources/changelog/cache-token-pricing-for-model-apis/) | none found | Status feed does not reach April |
| 2026-05 | Frontier Gateway (005); Loops early access (006); SSO/SCIM (007); deprecation notice DeepSeek v3.1/MiniMax M2.5 (008) | [Gateway](https://www.baseten.co/blog/introducing-baseten-frontier-gateway/), [Loops](https://www.baseten.co/blog/introducing-the-baseten-loops-sdk/) | none found | baseten-cli v0.1.0 on GitHub 2026-05-22 (context) |
| 2026-06 | MAI-Thinking-1 "coming" (009); rolling-deployment claims (010); **Series F** (011, 013); GLM-5.2 speed claim (012); deprecation executed with changed date (014); MCP/skill changelog (015) | [Series F](https://www.baseten.co/blog/announcing-our-series-f/) | [Reuters via techpartner.news](https://www.techpartner.news/news/ai-startup-baseten-hits-13-billion-valuation-as-australias-blackbird-makes-record-bet-626878); [Dealroom](https://dealroom.co/news/135561-baseten-raises-1-5b-series-f-at-13b-valuation-as-ai-inference-demand-sur/) | Lead-investor description conflicts |
| 2026-07 | GLM 5.1 etc. deprecation notice (016); Model API partial outage (017); Baseten for Model Labs (018); Baseten Switch (019) | [Model Labs](https://www.baseten.co/blog/announcing-baseten-for-model-labs/), [Switch](https://www.baseten.co/blog/how-to-run-kimi-k3-in-any-harness-routing-with-baseten-switch/) | none found | 4 major + 11 minor status incidents in feed |
| 2026-08 | Runtime OIDC (020); autoscaling schedules GA (021) | [Runtime OIDC](https://www.baseten.co/resources/changelog/runtime-oidc/) | none found | Thinnest month for platform changes; model-availability posts excluded |
| 2026-09 | MCP benchmark (022); **Blaxel acquisition** (023); 6-model deprecation (024); CLI 1.0.0 GA (025); terms update (026); Hosted Tools (027); Kimi K3 outage (028); API-key prefix (029); NVIDIA OpenShell (030); **OpenAI partnership** (031) | [Blaxel](https://www.baseten.co/blog/blaxel-is-joining-baseten-to-build-the-future-of-agentic-cloud/), [OpenAI](https://www.baseten.co/blog/baseten-openai-partnership/) | [Digital Today](https://www.digitaltoday.co.kr/en/view/109278/baseten-joins-openai-marketplace-open-models-available-directly-in-codex) (restates Baseten); [Tekedia](https://www.tekedia.com/baseten-acquires-tekedia-capital-portfolio-company-blaxel/) (Blaxel investor) | No OpenAI/NVIDIA-hosted confirmation fetched |
| 2026-10-01..12 | Agent-built inference engine experiment (032); CLI 1.1.0 (033); DeepSeek v4.1 outage posted retroactively (034); Project Beacon (035); rolling deployments default (036); egress restrictions (037) | [experiment](https://www.baseten.co/blog/agentic-inference-optimization-faster-than-sota/), [egress](https://www.baseten.co/resources/changelog/egress-restrictions/) | none found | Oct 13–15 posts excluded |

## 4. Dated event evidence and capabilities

Full detail is in the [CSV](067-baseten.events.csv). Highlights:

| Event ID | Published / underlying date | Claim or observed feature | Availability and limitations | Source (type) | Independent check | Grade |
|---|---|---|---|---|---|---|
| CI2026-067-001 | 2026-04-14 | Truss v0.16.0: Python 3.13 default, 3.9 deprecated; OpenAI-compatible endpoints | 42 stable + 37 pre-release Truss tags in window (GitHub API) | GitHub release | — | E2 |
| CI2026-067-005 | 2026-05-06 | Frontier Gateway: white-label multi-tenant API for model labs | "starting today"; vendor testimony on customers | blog | — | E1 |
| CI2026-067-008 / -014 | 2026-05-28 / 2026-06-24 (00:00 UTC Jun 25) | DeepSeek v3.1 + MiniMax M2.5 deprecation | **Notice said June 17; executed June 24**; recommended replacement changed | changelog | each other | E2 |
| CI2026-067-011 / -013 | 2026-06-22 / 2026-06-24 | $1.5B Series F at $13B valuation | **Leads differ**: Baseten names Altimeter/Conviction/Spark (Sands, Wellington co-lead); Reuters says Sands and Wellington led | blog; Reuters syndication | Dealroom | E1 |
| CI2026-067-015 / -022 | 2026-06-30 / 2026-09-02 | Backend MCP server + skill for coding agents; vendor benchmark 320 runs/16 tasks, 7.5% average reduction, pass rate 89%→97% | **Launch date conflict**; summary "about 50%" vs body "up to 57%" | changelog; blog | GitHub repo exists (MIT) | E1–E2 |
| CI2026-067-017, -028, -034 | 2026-07-13, 2026-09-20, 2026-10-07 | Major-impact Model API incidents (provider InfiniBand outage; ~20% Kimi K3 errors; DeepSeek v4.1 outage posted ~24 h after it ended) | Vendor self-report; incomplete feed | status page | — | E2 |
| CI2026-067-023 | 2026-09-10 | Blaxel acquisition; Blaxel product continues | Terms undisclosed; speed claims vendor-only | blog | Tekedia (investor, not neutral) | E1 |
| CI2026-067-024 | 2026-09-13 | Six shared model IDs deprecated with ~12 days' notice | Several had lived ~2–3 months | changelog | — | E2 |
| CI2026-067-025 / -033 | 2026-09-15 / 2026-10-02 | Baseten CLI 1.0.0 GA (MIT); 1.1.0 | 1.1.0 changelog Oct 2 vs GitHub release Oct 1 | changelog | GitHub API | E2 |
| CI2026-067-031 | 2026-09-29 | Open models in OpenAI B2B Marketplace and Codex | No OpenAI page fetched; ZDR claim unaudited | blog | Digital Today (restatement) | E1 |
| CI2026-067-032 | 2026-10-02 | Claude Code with Fable 5 + MetaInfer skills built an engine beating vLLM 0.25.1 by up to 90% decode, 2.33x TTFT | One self-reported run on one GPU/model | blog | — | E1 |
| CI2026-067-037 | 2026-10-12 | Per-deployment egress allow lists in Truss config | Org enablement requires contacting Baseten | changelog | — | E2 |

**Feature inventory (vendor assertion unless noted):** *APIs/SDKs* — OpenAI-compatible Model APIs, Management API (observability, billing/costs, API-key management), Truss (MIT), Baseten CLI (MIT, GA 2026-09-15, GitHub-verified), Baseten Switch (MIT, still pre-release on GitHub), Terraform provider (MIT, v0.1.0 2026-09-15, GitHub-verified), baseten-bdn SDK (MIT). *Agent integration* — backend + docs MCP servers and skill; Hosted Tools web search; OpenAI Codex/Responses integration; Blaxel sandboxes. *Security/governance* — SSO/SCIM (Enterprise plan), runtime OIDC, AWS AssumeRole, viewer role, regional deployments, `b10_` key prefix, egress allow lists, compliance-policy visibility. *Reliability* — rolling deployments (default for new environments from Oct 12), autoscaling schedules, container-restart and engine metrics. *Licensing* — open-source client tooling is MIT/Apache per GitHub metadata; the hosted service is governed by the Terms (updated 2026-09-15; diff not reviewed) and separate supplemental terms for model labs (not reviewed). *Observed vs verified:* GitHub release dates and licences are observed via API; no product feature was exercised.

## 5. What the company says it intends to do

| Public direction (≤25 words quoted) | Link/date | Horizon | Status | Missing/contradictory context |
|---|---|---|---|---|
| "This financing allows us to invest aggressively in the compute, software, and talent required to support our customers" | [Series F, 2026-06-22](https://www.baseten.co/blog/announcing-our-series-f/) | unstated | general intent | No capacity or product targets |
| "Over time, Baseten will add new products based on Blaxel's primitives, starting with Sandboxes." | [Blaxel, 2026-09-10](https://www.baseten.co/blog/blaxel-is-joining-baseten-to-build-the-future-of-agentic-cloud/) | "over time" | planned, uncommitted date | Sep 28 post says Blaxel sandboxes already support OpenShell |
| Hosted Tools as "a new ecosystem for capabilities like web search, code execution in sandboxes, browser use and automation" — web search first | [Hosted Tools, 2026-09-16](https://www.baseten.co/blog/introducing-baseten-hosted-tools/) | unstated | web search launched; others tentative | No dates for other categories |
| MAI-Thinking-1 "is coming to Baseten" | [2026-06-02](https://www.baseten.co/blog/mai-thinking-1/) | unstated | announced only | Availability not confirmed by 2026-10-12 in screened sources |
| Project Beacon capabilities to market "with a small number of early partners" | [2026-10-09](https://www.baseten.co/blog/safe-open-models-baseten-goodfire/) | unstated | early access | No accuracy data |
| New API keys gain `b10_` prefix from 2026-10-01 15:00 UTC | [2026-09-25](https://www.baseten.co/resources/changelog/upcoming-change-to-baseten-api-key-format/) | dated | scheduled at publication | Rollout not verified |

## 6. Independent interpretation: conditional 2027–2031 scenarios (researcher's hypotheses, not company strategy)

| Hypothesis | Supporting observations | Rival explanations | Disconfirming signals | Confidence/unknowns |
|---|---|---|---|---|
| H1. Inference platforms become **multi-model distribution channels** inside coding agents (open models routed alongside closed ones) | Model Labs (018), OpenAI Codex marketplace (031), Switch router (019) | Partnerships may be promotional pilots; hyperscaler marketplaces may absorb the role | By 2028 opt-in agent logs show negligible open-model routing share; Codex integration withdrawn | Low; no usage data |
| H2. **Short shared-endpoint lifecycles** make pinned open-model IDs a reproducibility and maintenance cost for agent workflows | Notices with ~2 weeks (003) and ~12 days (024); GLM 5.1 lived ~2 months; changed deprecation date (008/014) | Dedicated deployments give stability for paying users; churn reflects rapid model improvement, not instability | Notice periods lengthen to ≥90 days, or shared-endpoint lifetimes exceed 12 months by 2028 | Medium for the observation, low for impact |
| H3. Inference vendors **vertically integrate agent execution** (sandboxes, hosted tools, safety monitors) | Blaxel (023), Hosted Tools (027), OpenShell (030), Beacon (035) | Separate sandbox vendors stay best-of-breed; integration remains marketing | Blaxel remains a separate product with no integrated SKU by end-2027, or sandboxes discontinued | Low–medium |
| H4. **Agent-built, workload-specific inference engines** become routine, raising verification demands | Oct 2 experiment (032); vendor MCP benchmark (022) | Single cherry-picked run; generic engines (vLLM, SGLang) catch up | Independent replications fail, or speedups vanish under accuracy-preserving constraints | Low; n = 1 |

## 7. Implications for the GitHub 1000 study (M1–M7)

| Construct | Possible observable effect | Study design to test it | Negative/null explanation | Measurement boundary |
|---|---|---|---|---|
| M1 workflow change | Coding agents operate infrastructure via MCP/CLI (015, 022, 025) and route among models (019, 031) | Opt-in agent tool-use records; count tasks using platform MCP vs. raw API | Availability ≠ adoption; vendor says "most users already write code with agents" without data | No user telemetry accessible |
| M2 accepted quality, review and maintenance | Model-ID churn forces config changes; agent-built code needs correctness checks (032) | Track forced dependency/model-ID changes per repo-month and review minutes | Churn may be absorbed by dedicated deployments | Only vendor-side notices observed |
| M3 discovery | New MIT repos (Switch, CLI, skills) appear; stars are not use | Trending/stars panel vs. independently verified installs | Stars track launch marketing | No install/download data collected |
| M4 first-use success and verified reuse | CLI GA and machine-readable output (`--output json`) may ease first use | Independent newcomer task: deploy a sample Truss with CLI vs. dashboard | GA labels do not ensure success | Not exercised |
| M5 reuse vs. generate | The Oct 2 experiment let agents reuse vLLM/TensorRT-LLM kernels rather than write all code | Matched tasks with and without reuse access, hidden acceptance tests | Gains may come from specialization, not reuse | Single vendor anecdote |
| M6 lifecycle cost and energy | Cache-token pricing (002), pre-warm schedules (021) shift cost/energy trade-offs | Metered runtime + human minutes on frozen workload | Pre-warming can raise idle energy | **No energy data**; never convert tokens to CO2e |
| M7 maintainer interventions | Agent-facing interface (MCP/skill) as an adoption intervention | See §8 | Vendor benchmark is self-authored | Not independent |

Funding, valuation, customer logos and stars in this report are **not** evidence of adoption or task quality.

## 8. One practical, falsifiable change for the maintainer's own repositories

**Repository/component:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study) offline CLI (`python -m trending_study …`). No Baseten account, paid API call, live GitHub capture or network access is involved; `capture` stays disabled.

**Candidate practice (not yet validated):** Baseten claims (CI2026-067-022) that an agent-facing interface raised its agents' pass rate. The local analogue is a short **agent-facing CLI reference**: one page listing each subcommand's inputs, exit codes and JSON outputs, linked from `AGENTS.md`. It reuses the existing argparse `--help` text instead of new tooling.

**Treatment/control and frozen task:** Freeze 10 small offline tasks before the trial, such as "add a validation error for X with a test" or "fix the failing fixture parse". Include 2 tasks with no valid solution, which count in the denominator. A human who is not the agent writes the hidden acceptance tests. **Control:** the current README + `--help`. **Treatment:** the same plus the CLI reference. Use the same coding agent, model version, subscription plan and per-task budget in both arms; this follows the owner's rule against paid API scripts. Alternate the arm order across tasks.

**Functional unit and measures:** the primary unit is an **independently accepted task**: hidden tests pass, `python -m unittest discover -s tests -v` passes, and the maintainer's review is approved. Count it against all assigned tasks, including refused, failed and timed-out ones. Secondary measures are the maintainer's review and rework minutes (stopwatch), agent wall time, and the number of iterations. Agent use is logged privately in `.claude/plans/` and never in commit metadata. All commits stay authored by the maintainer.

**Guardrails:** offline synthetic fixtures only; no secrets in the environment; no edits outside the task scope; any attempt to call GitHub or bypass the capture hard stop ends the trial. No energy or CO2e numbers unless they are actually metered.

**Stop/reversal rule:** stop after 10 task pairs or 6 human hours, whichever comes first. Keep the reference only if the accepted-task count improves by at least 2 of 10 **and** median review minutes do not rise. Otherwise drop it and record the null result. Stop immediately on any guardrail breach.

## 9. Findings, uncertainties and review outcome

- **Observed/shipped (documentary):** a dense changelog cadence (53 in-window entries); GitHub-verified Truss, CLI and Switch releases with MIT licences; enterprise identity and network controls (SSO/SCIM, OIDC, egress); the CLI's move to 1.0.
- **Claims/announcements only:** MAI-Thinking-1 availability, Project Beacon, Blaxel-based sandbox products, the broader Hosted Tools categories, and every performance figure (280+ TPS, 7.5%/57%, 50–90%, 25 ms, 50–60% more frequent deploys).
- **Conjectures and unknowns:** actual usage of the OpenAI marketplace route, the Series F tranche structure (the $11B/$13B split appears only in search snippets of secondary sites that were not fetched, so it is E0), filing-level ownership, and status incidents before 2026-06-03.
- **Contradictory or null evidence:** the Series F lead investors differ between Baseten and Reuters; one deprecation was announced for June 17 but executed June 24; the MCP launch date conflicts (changelog Jun 30 vs. blog Sep 2); the MCP benchmark's summary (~50%) and body (57%) disagree; CLI 1.1.0 dates differ by a day; one outage was posted only after it ended; 12 major-impact incidents appear in the status feed from Jun 3 to Oct 12. **CMS caveat:** the blog's embedded `_publishedAt` values are republish times. For example, Loops displays May 8 but its CMS time is Jul 13, and Frontier Gateway displays May 6 but its CMS time is Aug 29. The ledger therefore uses **displayed** dates.
- **Untrusted page content:** the [connect-coding-agents changelog](https://www.baseten.co/resources/changelog/connect-coding-agents-to-baseten/) embeds an install prompt addressed to the reader's coding agent. It was treated as data and not executed.
- **Reviewer links and audit date:** human factual/link, rights and methods review **pending**. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.
