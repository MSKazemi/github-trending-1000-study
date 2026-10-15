# LangChain — provisional six-month technology intelligence screen (041)

> **Provisional source-lead screen (2026-10-16):** this report, its [event ledger](041-langchain.events.csv) and [search log](041-langchain.search-log.md) are **provisional, AI-assisted documentary source leads** for [issue #108](https://github.com/MSKazemi/github-trending-1000-study/issues/108). They are **unreviewed by a qualified human**; factual/link review, source-access/rights review and methods review remain **pending**. This is not scientific or security sign-off; issue #108 was closed on maintainer instruction (2026-10-16) with these review gates still open; reopen it if review finds a defect.

- **Watchlist:** 041; [issue #108](https://github.com/MSKazemi/github-trending-1000-study/issues/108). **Study lens:** agent state, traceability and components.
- **Window:** 2026-04-12 through 2026-10-12 inclusive; **source-screened on 2026-10-16**. Exact UTC search-run times, full search result counts, immutable page snapshots and an independent reviewer are unavailable.
- **Status:** **provisional dated documentary screen (29 traceable source leads covering all seven calendar segments); not reviewed by a qualified human; factual/link, source-access/rights and methods review pending**. These are not independently verified task outcomes, exhaustive retrieval or human-approved scientific completion. See the [event ledger](041-langchain.events.csv), the [month-segment queries and inclusion/exclusion log](041-langchain.search-log.md) and the [study method](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md).
- **Official sources checked:** [LangChain](https://www.langchain.com/), [blog](https://www.langchain.com/blog/), [LangSmith changelog](https://docs.langchain.com/langsmith/changelog), [about page](https://www.langchain.com/about), public repositories [langchain-ai/langchain](https://github.com/langchain-ai/langchain), [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph), [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents), [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki) and their GitHub security advisories. **Claim grading** uses the company-watch E0–E4 tiers, not the separate [2027 lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md).

## 1. Discovery, coverage and exclusions

The [search log](041-langchain.search-log.md) records every query and call actually run, page by page, for all seven segments. Most evidence is **first-party**: blog posts, the weekly LangSmith changelog, GitHub releases and GitHub security advisories. Independent evidence inside the window is thin. It consists of vulnerability-database mirrors ([Wiz](https://www.wiz.io/vulnerability-database/cve/cve-2026-48775), [OSV](https://osv.dev/vulnerability/CVE-2026-44843)) and one secondary news relay of vendor claims ([AI2Work, May 14](https://ai2.work/blog/langchain-ships-langsmith-engine-and-managed-deep-agents-at-interrupt)). The searches surfaced **no in-window TechCrunch, Register, InfoWorld or VentureBeat article**, which means only that this screen did not find one.

The search was **not exhaustive**. Result totals are unknown, not zero. Pages were read through a summarizing fetch tool, so a human must re-open every URL. In the portion read, the LangSmith changelog showed no entries between Feb 16–20 and Jun 1–5, 2026. Whether this is a real gap or a tool artifact is **unknown**.

## 2. Corporate/product identity and rights baseline

**Entity.** The [about page](https://www.langchain.com/about) names the company "LangChain" with founders Harrison Chase and Ankush Gola. It lists a San Francisco headquarters with offices in New York, Boston and Amsterdam, and shows investor logos for IVP, Benchmark and Sequoia. The page does **not** state the legal entity name. This screen did **not** verify the exact legal name, corporate parent or beneficial ownership to filing level. No in-window acquisition, rename or parent change surfaced. **Baseline (pre-window):** [TechCrunch, 2025-10-21](https://techcrunch.com/2025/10/21/open-source-agentic-startup-langchain-hits-1-25b-valuation) reported a $125M round led by IVP at a $1.25B valuation. Funding is not adoption evidence.

**Product boundaries as of 2026-10-12:**

| Component | Nature | Rights (verified how) |
|---|---|---|
| LangChain (`langchain`, `langchain-core`, integrations) | OSS agent/LLM framework; `create_agent`, middleware, `langchain.mcp` (beta, 1.4.0) | MIT (GitHub API `license.spdx_id`) |
| LangGraph (`langgraph`, `langgraph-checkpoint*`, `langgraph-sdk`) | OSS stateful graph runtime: checkpointers, stores, durable execution, interrupts | MIT (GitHub API) |
| Deep Agents (`deepagents`) | OSS agent harness (Python/JS): subagents, filesystem, skills, middleware | MIT (GitHub API; the [Apr 9 post](https://www.langchain.com/blog/deep-agents-deploy-an-open-alternative-to-claude-managed-agents) also says MIT) |
| OpenWiki | OSS agent memory/wiki, v0.1.0 (Jul 2026) | MIT (GitHub API) |
| LangSmith SDK | Client for tracing/evaluation | MIT (GitHub API) |
| LangSmith platform (tracing, Engine, Sandboxes, LLM Gateway, Managed Deep Agents, Fleet, BYOC, `langgraph-api` server) | **Proprietary hosted/commercial** service; self-hosted and BYOC for Enterprise | Commercial terms; **not** reviewed here |

MIT-licensed client libraries do **not** imply that the hosted LangSmith services, Engine, Gateway or Managed Deep Agents are open source, free, or covered by MIT. "Fleet" is the no-code agent product. A third-party summary returned by search said Agent Builder was renamed to Fleet in March 2026; this is **E0, unverified**.

## 3. Seven-segment dated chronology

| Period | In-window source evidence (source publication dates) | Availability and attribution limits |
|---|---|---|
| Apr 12–30 | [Apr 16 evaluator templates + reusable evaluators](https://www.langchain.com/blog/reusable-langsmith-evaluator-templates); [Apr 16 async subagents (Agent Protocol)](https://www.langchain.com/blog/running-subagents-in-the-background); [Apr 16 GHSA-fv5p text-splitter SSRF fix](https://github.com/langchain-ai/langchain/security/advisories/GHSA-fv5p-p927-qmxr) | Vendor says the features are available; there is no independent test. **Excluded as pre-window:** Apr 9 `deepagents deploy` beta, Apr 7 Arcade.dev tools in Fleet, Apr 8 GHSA-926x. |
| May | [May 5 GHSA-pjwx load() allowlist (high)](https://github.com/langchain-ai/langchain/security/advisories/GHSA-pjwx-r37v-7724); [May 12 LangGraph 1.2.0](https://github.com/langchain-ai/langgraph/releases/tag/1.2.0); May 13 [Engine public beta](https://www.langchain.com/blog/introducing-langsmith-engine), [Sandboxes GA](https://www.langchain.com/blog/langsmith-sandboxes-generally-available), [Managed Deep Agents (private beta)](https://www.langchain.com/blog/introducing-managed-deep-agents); May 14 [Interrupt overview](https://www.langchain.com/blog/interrupt-2026-overview), [LangChain Labs](https://www.langchain.com/blog/introducing-langchain-labs); [May 22 GHSA-fjqc checkpoint deserialization](https://github.com/langchain-ai/langgraph/security/advisories/GHSA-fjqc-hq36-qh5p) | Interrupt 2026 was held May 13–14 (event date) per the [Apr 9 preview post](https://www.langchain.com/blog/previewing-interrupt-2026-agents-at-enterprise-scale). Launches mix GA, public beta and private beta. The LLM Gateway was **private beta** at this point. |
| June | [Jun 2 RubricMiddleware beta](https://www.langchain.com/blog/introducing-rubrics-for-deepagents); [Jun 12 GHSA-gr75 path traversal/sandbox escape](https://github.com/langchain-ai/langchain/security/advisories/GHSA-gr75-jv2w-4656) | Only 2 rows were ledgered. The [Jun 25 newsletter](https://www.langchain.com/blog/june-2026-langchain-newsletter) items (Fleet Computer Use, programmatic subagents) carry no availability labels and were not ledgered. |
| July | [Jul 10 OpenWiki Brains 0.1.0](https://www.langchain.com/blog/introducing-openwiki-brains-general-purpose-wiki-memory-for-agents); [Jul 25 "own your intelligence"](https://www.langchain.com/blog/own-your-intelligence); Jul 27–31 [changelog: v1 endpoints sunset 2027-01-31](https://docs.langchain.com/langsmith/changelog); [Jul 29 Deep Agents v0.7](https://www.langchain.com/blog/deep-agents-v0-7); [Jul 30 LLM Gateway public beta](https://www.langchain.com/blog/langsmith-llm-gateway-runtime-controls-for-production-agents); [Jul 30 GHSA-47pj store namespace leak](https://github.com/langchain-ai/langgraph/security/advisories/GHSA-47pj-3jcm-6whg) | v0.7 has **breaking changes**. The sunset is a future removal (`announced_only`). |
| August | [Aug 7 Managed Deep Agents public beta](https://www.langchain.com/blog/managed-deep-agents-is-now-in-public-beta); [Aug 12 BYOC GA on AWS](https://www.langchain.com/blog/langsmith-byoc-is-now-generally-available-on-aws); [Aug 28 GHSA-fvww SDK auth actions= ignored (high)](https://github.com/langchain-ai/langgraph/security/advisories/GHSA-fvww-7h3r-vfhp) | Managed Deep Agents is US-only and CLI-first. BYOC is Enterprise-only on AWS. |
| September | [Sep 3 langchain 1.4.0 `langchain.mcp` (beta)](https://www.langchain.com/blog/mcp-in-langchain-stateless-protocol-elicitation-and-more); Sep 7–14 [changelog: 180-day extended-retention cap from Sep 14](https://docs.langchain.com/langsmith/changelog); Sep 24 [Engine v2 red teaming (private beta)](https://www.langchain.com/blog/langsmith-engine-v2-redteam), [Trajectories](https://www.langchain.com/blog/langsmith-trajectories-tracing); [Sep 28 GHSA-4hm6 cross-user Store access (high)](https://github.com/langchain-ai/langgraph/security/advisories/GHSA-4hm6-w6qq-w73v) | The Sep 24 Fine-Tuning public beta and Managed Deep Agents v0.8 were screened but not ledgered. |
| Oct 1–12 | [Oct 7 Managed Deep Agents v0.9](https://www.langchain.com/blog/managed-deep-agents-schedules-per-run-configuration-slack); [Oct 7 GHSA-3fx2 SDK streaming redirect](https://github.com/langchain-ai/langgraph/security/advisories/GHSA-3fx2-cqw9-xr3c) | **Excluded as post-window:** Oct 13 AI Search, Oct 14–15 posts, the Oct 15 newsletter, and an unverified "Interrupt NYC" Oct 13 lead. |

The [CSV](041-langchain.events.csv) holds **29 dated source records** (Apr 3, May 8, Jun 2, Jul 6, Aug 3, Sep 5, Oct 2). It is a purposive selection fitted to the study lens, not a census of releases. The LangGraph repository alone published 79 release objects in the window. Shared `duplicate_event_group` values (`041-MDA`, `041-ENGINE`) mark staged steps of one product line, which must not be counted as independent launches.

## 4. Feature map: agent state, traceability and components

| Evidence cluster | What the cited document supports | Important non-equivalence or counterexample |
|---|---|---|
| **State and durability:** [LangGraph 1.2.0](https://github.com/langchain-ai/langgraph/releases/tag/1.2.0) (durable error-handler resume, delta-channel checkpoints in beta); [Managed Deep Agents](https://www.langchain.com/blog/managed-deep-agents-is-now-in-public-beta) (thread state that survives restarts, pause/retry/resume) | Vendor release notes describe durable execution primitives in OSS, plus a hosted runtime that manages them | Release-note bullets are not tested crash-recovery behaviour. Delta-channel APIs are beta. The hosted runtime is proprietary and US-only. |
| **State-store security:** [GHSA-fjqc](https://github.com/langchain-ai/langgraph/security/advisories/GHSA-fjqc-hq36-qh5p) (checkpoint JSON deserialization), [GHSA-47pj](https://github.com/langchain-ai/langgraph/security/advisories/GHSA-47pj-3jcm-6whg) (namespace prefix leak across tenants), [GHSA-4hm6](https://github.com/langchain-ai/langgraph/security/advisories/GHSA-4hm6-w6qq-w73v) and [GHSA-fvww](https://github.com/langchain-ai/langgraph/security/advisories/GHSA-fvww-7h3r-vfhp) (authorization bypasses) | The persistence and authorization layer that holds agent state had **four in-window advisories**. Each lists a patched version. | Each advisory states narrow preconditions (write access to the store, specific auth configuration). Advisories show potential impact, **not** prevalence or exploitation. The vendor states no in-the-wild evidence for GHSA-47pj and GHSA-gr75. |
| **Memory components:** [Context Hub `/memories/`](https://www.langchain.com/blog/managed-deep-agents-is-now-in-public-beta); [OpenWiki 0.1.0](https://www.langchain.com/blog/introducing-openwiki-brains-general-purpose-wiki-memory-for-agents) (MIT) | One hosted memory layer and one open memory layer are reported | OpenWiki connects to personal sources (mail, notes), which raises privacy, retention and consent questions that have not been reviewed |
| **Traceability:** [Trajectories](https://www.langchain.com/blog/langsmith-trajectories-tracing) (projection over thread traces incl. subagents); [Engine](https://www.langchain.com/blog/introducing-langsmith-engine) / [Engine v2](https://www.langchain.com/blog/langsmith-engine-v2-redteam) (trace clustering, red teaming, fix validation); [180-day retention cap](https://docs.langchain.com/langsmith/changelog); [BYOC](https://www.langchain.com/blog/langsmith-byoc-is-now-generally-available-on-aws) (traces in the customer VPC) | Trace data is the substrate for debugging, evaluation, fixes and (per Labs/Fine-Tuning) training | Engine "pre-validated fixes" are vendor self-validation, **not independent acceptance**. The retention cap limits how long trace-based audits remain possible on SaaS. |
| **Components and interoperability:** [`langchain.mcp` on FastMCP](https://www.langchain.com/blog/mcp-in-langchain-stateless-protocol-elicitation-and-more); [async subagents on Agent Protocol](https://www.langchain.com/blog/running-subagents-in-the-background); [Deep Agents v0.7](https://www.langchain.com/blog/deep-agents-v0-7) | Movement toward protocol-level reuse (MCP, Agent Protocol, AGENTS.md, Agent Skills) | `langchain.mcp` is beta and requires migration from `langchain-mcp-adapters`. v0.7 removed defaults and APIs, so reuse carries an upgrade cost. |
| **Sandboxing and tool confinement:** [Sandboxes GA](https://www.langchain.com/blog/langsmith-sandboxes-generally-available) (microVM, credential-injecting proxy); [GHSA-gr75](https://github.com/langchain-ai/langchain/security/advisories/GHSA-gr75-jv2w-4656) (path traversal in file-search middleware via untrusted LLM input) | The vendor asserts isolation for hosted sandboxes, and a separate advisory documents a real confinement defect in OSS middleware | No independent isolation audit was located. GHSA-gr75 is a concrete reminder that tool path confinement fails when an LLM acts on untrusted input. |
| **Runtime controls:** [LLM Gateway public beta](https://www.langchain.com/blog/langsmith-llm-gateway-runtime-controls-for-production-agents) | Spend caps, rate limits, fallbacks; PII/secret redaction on Enterprise only | Redaction efficacy is untested. Broader guardrails are explicitly future work. |

## 5. Publicly stated direction versus shipped functionality

| Dated first-party source (≤25-word paraphrase/quote) | Promised horizon | Current research classification |
|---|---|---|
| [May 13 Engine](https://www.langchain.com/blog/introducing-langsmith-engine): "working toward a future where more of it runs continuously without manual triggers" | Unspecified | **Stated intention**. In the window, Engine stays public beta, and Engine v2 features are private beta. |
| [May 14 LangChain Labs](https://www.langchain.com/blog/introducing-langchain-labs): continual learning from traces, feedback and evals with named partners; will publish research, evals and integrations | Unspecified | **Announced only**. Partner roles not verified with the partners. |
| [Jul 25 "own your intelligence"](https://www.langchain.com/blog/own-your-intelligence): "Buy the generic infrastructure, but own the intelligence that compounds" | Strategic | **Positioning statement**, not product evidence |
| [Jul 30 LLM Gateway](https://www.langchain.com/blog/langsmith-llm-gateway-runtime-controls-for-production-agents): broader guardrails listed as future direction | Unspecified | **Planned**. Current controls are spend/rate/fallback/redaction (beta). |
| [Aug 7 Managed Deep Agents](https://www.langchain.com/blog/managed-deep-agents-is-now-in-public-beta): other regions and deployment methods planned; API being finalized | Unspecified | **Planned**. As of Oct 7 the product is still public beta. |
| [Sep 3 MCP](https://www.langchain.com/blog/mcp-in-langchain-stateless-protocol-elicitation-and-more): TypeScript MCP support "to follow" | Unspecified | **Announced only** for TypeScript |
| [Sep 24 Engine v2](https://www.langchain.com/blog/langsmith-engine-v2-redteam): self-hosted Engine v2 "coming shortly"; BYOK in the next self-hosted release | Next self-hosted release | **Planned**, not verified as shipped by Oct 12 |
| [Changelog Jul 27–31](https://docs.langchain.com/langsmith/changelog): legacy v1 run/sharing endpoints sunset 2027-01-31 | 2027-01-31 | **Scheduled removal**. Observable only after the window. |

A public intention is not a scheduled delivery, and it does not establish the company's 2027–2031 strategy.

## 6. Conditional 2027–2031 outlook (analyst hypotheses, not company statements)

| Testable scenario | Rival cause | Disconfirming observation |
|---|---|---|
| Agent frameworks converge on **hosted durable state + trace-derived improvement loops** (Engine, Labs, Fine-Tuning), which makes the trace store the main lock-in surface | Open protocols (MCP, Agent Protocol, OpenTelemetry-style tracing) commoditize traces and keep them portable | Independent users export traces and replay them on a different stack with equivalent accepted-task results and low migration effort |
| The **state/persistence layer** becomes the dominant security surface for agent frameworks (4 LangGraph state/auth advisories in 6 months) | Security reports may reflect more disclosure/bug-bounty attention, not more defects | Advisory counts per KLOC or per release fall, or match peer frameworks under comparable disclosure programmes |
| Protocol-level component reuse (MCP in core, Agent Skills, AGENTS.md) lowers integration cost for maintainers | Breaking changes (Deep Agents v0.7, `langchain-mcp-adapters` → `langchain.mcp`) shift the cost to upgrades | Measured upgrade/migration minutes exceed the integration minutes saved across a 6-month horizon |

These are **hypotheses**, not forecasts issued by LangChain or evidence of adoption.

## 7. M1–M7 study relevance

| Construct | Possible observable effect | Prospective measurement, not inferred conclusion | Negative/null explanation |
|---|---|---|---|
| **M1** coding-workflow change | Agent harnesses with durable state, subagents and scheduled runs move work from interactive to delegated mode | Dated release chronology (this ledger) + opt-in workflow records; availability ≠ adoption | Feature availability may not change what maintainers actually do |
| **M2** accepted task quality / review | Engine fixes and Rubric self-evaluation could reduce or add review load | Independently authored hidden acceptance tests; count all attempts incl. refused/failed; reviewer minutes | Self-graded rubrics or vendor-validated fixes may inflate apparent quality |
| **M3** discovery | Not directly addressed by this evidence | Do not use LangChain stars or funding as a discovery signal | — |
| **M4** verified third-party reuse | MIT components (LangGraph, deepagents, OpenWiki) are reuse candidates | Trace one consented downstream integration that passes a fixed task; downloads ≠ users | Package downloads are dominated by CI/transitive installs |
| **M5** reuse-first vs build | LangGraph checkpointers/stores vs a small custom persistence layer | Matched acceptance spec, dependency/advisory exposure, upgrade cost (see §8) | Reuse may be inferior when it brings 4 state-layer advisories and breaking changes |
| **M6** lifecycle human and energy cost | Deep Agents v0.7 reports a reduction in base input tokens of about 65%; retention caps and BYOC shift storage costs | Measure human minutes, CI time and metered energy only where instrumented; **no token-to-energy or CO2e conversion** | Fewer tokens does not mean lower energy; costs shift to upstream/hosting |
| **M7** maintainer interventions | Explicit, dated advisories with patched ranges are a reusable maintenance practice | Compare advisory-to-patch latency and clarity across watched OSS projects | Disclosure volume reflects programme maturity, not code quality |

## 8. One falsifiable reuse-first maintainer experiment

**Repository/component:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study), applied to a **synthetic, offline** multi-step pipeline only (for example, re-processing committed synthetic follow-up fixtures). The live Trending `capture` stays **disabled** under the source-access decision, and nothing here changes that.

**Question:** Is a reused state/checkpoint component (LangGraph `StateGraph` + `SqliteSaver`) better than the repository's existing pattern (plain Python steps writing write-once JSON artifacts) for **resumable** multi-step processing?

**Freeze before the trial:** one task specification, i.e. a 5-step deterministic pipeline over committed synthetic fixtures. Freeze 10 fault-injection cases in the denominator: the process is killed after each step, twice, at different points. The hidden acceptance tests are authored by someone other than the implementer. They check (1) that the final outputs are byte-identical to an uninterrupted run, (2) that no write-once artifact is overwritten or truncated, (3) that no step's side effect is duplicated, and (4) that the code works offline with no network access.

**Comparator A:** the existing repository pattern plus the minimal resume logic needed. **Treatment B:** LangGraph with a SQLite checkpointer, pinned at or above the patched versions from the in-window advisories (`langgraph-checkpoint` ≥ 4.1.1, `langgraph-checkpoint-sqlite` ≥ 3.1.1, `langgraph` ≥ 1.2.14). The checkpoint DB is treated as trusted-write-only, given [GHSA-fjqc](https://github.com/langchain-ai/langgraph/security/advisories/GHSA-fjqc-hq36-qh5p).

**Primary endpoint:** fault-injection cases that pass all hidden assertions / **all 10 assigned cases** (failures and timeouts count as failures).

**Secondary endpoints:** implementer and reviewer minutes; added lines of code; number of new direct and transitive dependencies; known advisories against the pinned set at trial time and over 30 days; time to upgrade across one minor release. CI wall-time and energy are recorded only if actually metered.

**Cost bound:** at most 4 human hours per arm plus one independent review.

**Stop/reversal rule:** keep comparator A if any of the following holds:
- B does not pass strictly more fault cases than A.
- B violates write-once semantics.
- B adds more than 15 transitive dependencies.
- B has an unpatched advisory at trial time.
- B's review and upgrade minutes exceed A's by more than 50% with no correctness gain.

**No trial has been executed and no effects are estimated.** The correct outcome may be **no improvement**, and that result must be preserved.

## 9. Findings, uncertainties and review outcome (2026-10-16)

- **Observed/shipped (E2 documentary):** LangGraph 1.2.0 (May 12), Deep Agents v0.7 (Jul 29), langchain 1.4.0 (Sep 3) and OpenWiki 0.1.0 are on GitHub. Eight GitHub security advisories with patched versions were published in the window. Sandboxes GA (May 13), BYOC GA on AWS (Aug 12) and Trajectories (Sep 24) rest on vendor statements (E1).
- **Preview/beta only:** Engine (public beta; v2 red teaming in private beta), Managed Deep Agents (private → public beta, US-only), LLM Gateway (private → public beta), RubricMiddleware, the `langchain.mcp` namespace.
- **Announced only:** LangChain Labs research agenda, self-hosted Engine v2/BYOK, TypeScript MCP, broader gateway guardrails, the 2027-01-31 v1 endpoint sunset.
- **Important contradictory or null evidence:** the agent-state layer (checkpoint serialization, store namespaces, SDK/server authorization) had several in-window advisories, which tempers "durable state" marketing. OSV lists 2026-05-26 for CVE-2026-44843 versus the 2026-05-05 GitHub advisory date. The Managed Deep Agents May 13 post was edited after publication. No independent, task-based evaluation of any LangSmith feature was found.
- **Unknowns:** legal entity and ownership at filing level; usage/adoption of any feature; exact rollout dates beyond the displayed publication dates; whether the changelog has a real Feb–Jun gap; non-US availability; hosted-service terms and data rights; full search-result denominators.
- **Pending:** human factual/link spot-check (especially advisory version ranges and quoted figures), source-access/rights review, methods review and any real opt-in task comparison. **Issue #108 was closed on maintainer instruction (2026-10-16); this screen alone is not scientific completion — reopen it if factual, rights or methods review finds a defect.**
