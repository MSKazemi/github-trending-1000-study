# Company 6-month technology intelligence: Anthropic

- **Watchlist ID:** 002; **research issue:** [#68](https://github.com/MSKazemi/github-trending-1000-study/issues/68)
- **Analysis window:** 2026-04-12 through 2026-10-12 inclusive (UTC)
- **Recorded initial source review:** 2026-10-12; automated research assistance; **independent human factual/link reviewer: pending**
- **Stage:** **partial, source-screened working report**, NOT a completed six-month audit or independently corroborated study finding
- **Primary landing page:** https://www.anthropic.com/claude-code; **method:** [company protocol](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md)
- **Evidence semantics:** E1 below denotes first-party publication evidence for *what a vendor says*. It is not the main study's E1 descriptive observational outcome, and cannot validate model quality, adoption, net savings or safety.

## 1. Reproducible search and inclusion audit

| Review UTC date | Channels and actually targeted discovery terms | Result count | Included from directly readable first-party sources | Selection/coverage limitation |
|---|---|---|---|---|
| 2026-10-12 | Open-web search plus official product/news/release pages: `site:anthropic.com/news "Claude Sonnet 5" June 2026; site:anthropic.com/news "Claude Opus 5.5" September 2026` | Not reliably available from retrieval interface | 3 dated events below | Selective source screen; no archived exhaustive query return sets, no independently audited source inclusion |
| 2026-10-12 | Relevant independent published benchmark or investigative evidence | Not comprehensively screened | None independently validated for this report | Independent reproduction and negative cases remain work to do |

**Non-inclusion rule:** Homepage, search snippets, and undated vendor summaries by themselves do not count as dated shipped features. Search-result totals and source sensitivity are **unknown**, never zero. The required systematic April/May/June/July/August/September/October screen, independent reporting check and second-pass URL/date QA are **still pending**. This document is a useful early deliverable, **not issue acceptance**.

## 2. Identity and product boundary

Anthropic's Claude models, Claude Code and the Claude Platform are different product surfaces. The model announcements below do not automatically establish a shipped improvement in Claude Code workflows. Identity snapshot is inferred from linked company-controlled sources; legal/corporate independent verification is outstanding.

## 3. Month-by-month dated material found in this first pass

| Segment | Located eligible in-window item | Primary source | Independent reporting | Coverage / missingness |
|---|---|---|---|---|
| 2026-04-12–30 | No qualifying item validated during this targeted pass (NOT an assertion of zero releases) | — | No independent task audit | Full calendar-month sweep pending; missing evidence ≠ inactivity. |
| 2026-05 | No qualifying item validated during this targeted pass (NOT an assertion of zero releases) | — | No independent task audit | Full calendar-month sweep pending; missing evidence ≠ inactivity. |
| 2026-06 | Introducing Claude Sonnet 5 | [primary](https://www.anthropic.com/news/claude-sonnet-5) | No independent task audit | These sources were directly reviewed; other releases not exhaustively searched. |
| 2026-07 | No qualifying item validated during this targeted pass (NOT an assertion of zero releases) | — | No independent task audit | Full calendar-month sweep pending; missing evidence ≠ inactivity. |
| 2026-08 | No qualifying item validated during this targeted pass (NOT an assertion of zero releases) | — | No independent task audit | Full calendar-month sweep pending; missing evidence ≠ inactivity. |
| 2026-09 | Claude Sonnet 5.5 | [primary](https://www.anthropic.com/claude-sonnet-5-5) | No independent task audit | These sources were directly reviewed; other releases not exhaustively searched. |
| 2026-10-01–12 | Claude Haiku 5.5 | [primary](https://www.anthropic.com/claude-haiku-5-5) | No independent task audit | These sources were directly reviewed; other releases not exhaustively searched. |

## 4. Dated event, claim and capability ledger

| Event | Publication / underlying event | Evidence-backed claim (no external performance certification) | Actual availability or status | Exact source and type | Independent check | Company-watch tier |
|---|---|---|---|---|---|---|
| 002-E01 | 2026-06-30 / 2026-06-30 (announcement or document date; implementation date unverified) | Introducing Claude Sonnet 5: Announced Sonnet 5 for agentic tool use and coding. Published changelog documents a June 30 revision to BrowseComp methodology presentation and an August 10 pricing update: historic page content is mutable. | vendor model offering; benchmarks and pricing self-reported | [First-party source](https://www.anthropic.com/news/claude-sonnet-5) | No independent functional replication in this pass | E1: vendor-dated claim / description |
| 002-E02 | 2026-09-28 / 2026-09-28 (announcement or document date; implementation date unverified) | Claude Sonnet 5.5: Vendor announced revised model capabilities, effort settings, coding use and prices; reported comparative benchmarks are not independently replicated here. | announced available across platforms; plan/model constraints require testing | [First-party source](https://www.anthropic.com/claude-sonnet-5-5) | No independent functional replication in this pass | E1: vendor-dated claim / description |
| 002-E03 | 2026-10-07 / 2026-10-07 (announcement or document date; implementation date unverified) | Claude Haiku 5.5: Vendor introduced a smaller model targeted at cost-sensitive/high-volume tasks and subagent workflows; advertised speed/cost benefit is company-reported. | announced available; third-party task validity unknown | [First-party source](https://www.anthropic.com/claude-haiku-5-5) | No independent functional replication in this pass | E1: vendor-dated claim / description |

**Caution:** For all ledger events, publication and the company's claimed effective event date are treated as coincident only for this initial announcement record; an operational first-deployment or customer-use date has **not** been independently recovered. Additional revision history, pricing and license/API guarantees have not been fully archived. No product was installed or benchmarked.

## 5. Public direction versus future plan

**Attributed 2026 direction, not a guaranteed roadmap:** Anthropic publicly describes differentiated model tiers and effort settings for agentic workflows in the 2026-09-28 and 2026-10-07 announcements. Distinguish stated marketing from a contractual roadmap. No separately dated binding 2027 product commitment was validated.

**Planned 2027–2031 releases verified:** none in this first pass. This means *not established by reviewed primary material*, **not** that no roadmap exists.

## 6. Researcher's conditional 2027–2031 interpretation

Conditional hypothesis: route small retrieval/triage tasks to a smaller model and difficult patch tasks to a larger one to reduce cost per independently accepted task. Rival: coordination, retries and escalation eliminate savings; falsifier: worse final acceptance or higher total reviewer+run cost. This is an **E0 research hypothesis**, not vendor strategy or a demonstrated causal effect.

## 7. Testable connection to the GitHub 1000 study

Relevant constructs: M1 agent/model selection workflows, M2 task quality, M5 appropriate code reuse, M6 whole-life costs. See [M1–M7 operational definitions](../../../docs/AI_ERA_CODING_REUSE_RESEARCH_MISSION.md). The study has **not** measured vendor-driven adoption or avoided energy use. A changed tool workflow, repository star count, or claimed token reduction cannot substitute for independent usability and reuse outcomes.

**Null / rival result worth publishing:** The new practice might yield **no** increase in task acceptance, external reuse or review efficiency while introducing extra tool calls, dependencies, licensing burdens, costs or maintenance.

## 8. One bounded, falsifiable experiment for this study repository

**Candidate:** Pre-freeze five offline issues with independent acceptance tests, including intentional no-reuse cases. Compare one-model execution with an explicit small-model triage plus larger-model implementation workflow; pin exact model versions, prompts, dates, token accounting and human review time.

**Primary outcome:** accepted task completion under a predeclared, **independently authored** rubric; report failures/abstentions in denominator. **Secondary:** 1st-run success for external maintainers (only if actually recruited), median human review/repair minutes, version/cost/permissions and dependency evidence; measure kWh only if metered with an explicit workload/boundary. **Status:** proposed, not performed.

**Stop / reversal rule:** Reject tiered routing if acceptance worsens, sensitive code reaches an unapproved provider, or total lifetime review/runtime cost increases.

## 9. Provisional lesson, remaining work and reviewer status

- **Practical lesson (hypothesis to test, not recommendation):** route small retrieval/triage tasks to a smaller model and difficult patch tasks to a larger one to reduce cost per independently accepted task.
- **Evidence risk:** Do not treat vendor benchmark or unit token-price claims as cost per successful maintained task. Record source edits and model drift; initial benchmark/chart correction is a concrete audit caveat.
- **Not established:** entire six-month event coverage, external model benchmark comparability, true user adoption, measured whole-life CO2e or energy, counter-evidence, legal ownership beyond vendor assertions.
- **Independent 2nd reviewer / link QA:** **pending**. Do not mark #68 completed or merge automatically.
- **Required next pass:** month-specific queries with preserved dates/results, independent high-quality reporting and corrections, archive exact release/version availability and product license/plan boundary, external functional test or explicitly absent, human review.
- **No corpus inflation:** these first-party announcements are *not* added to the 1,000-news corpus pending independent full article screening and deduplication.

**Related protocols:** [reuse-first playbook](../../../docs/REUSE_FIRST_PLAYBOOK.md) · [evidence-to-lesson grading](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md) · [company report template](../../../templates/company_six_month_intelligence.md).


## 2026-10-14 provisional source-preservation integration (not empirical validation)

An AI-assisted source reviewer checked official Anthropic announcements and dates for Claude Sonnet 5 (June 30), Sonnet 5.5 (September 28), and Haiku 5.5 (October 7). Vendor benchmark, token-price, and claimed speed/efficiency figures were **not independently reproduced** or converted to energy impacts. The Sonnet 5 source has a later August 10 pricing edit and June 30 methodology correction, so a snapshot of its current text is not an immutable record of the original post. This E1 first-pass company shortlist can be preserved as working research per maintainer request, but is **not** accepted as a complete systematic six-month study, independent human factual review or tested recommendation. Keep research issue #68 open for publication-archive versioning, legal/source review, complete monthly search and measured reuse-first trials; previous draft-stage scientific-review holds are not silently declared satisfied.
