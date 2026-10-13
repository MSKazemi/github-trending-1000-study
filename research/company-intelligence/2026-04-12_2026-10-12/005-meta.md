# Meta — six-month AI/software company intelligence (initial source screen)
 
- **Watchlist ID:** 005
- **Issue:** [#71](https://github.com/MSKazemi/github-trending-1000-study/issues/71)
- **Period:** 2026-04-12 to 2026-10-12 inclusive, calendar publication dates.
- **As-of source review:** 2026-10-12.
- **Research status:** **INITIAL source-screened draft only**. Not a complete six-month systematic search, independently adjudicated result, formal peer review, real product deployment test, or study finding.
- **Company sector:** foundation models, enterprise/personal agents, developer APIs.
- **Official publication entry:** https://about.fb.com/news/
- **Individual machine-readable events:** [005-meta.events.csv](005-meta.events.csv).
- **Methods:** [company-source protocol](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md); [M1–M7 mission](../../../docs/AI_ERA_CODING_REUSE_RESEARCH_MISSION.md).

## 1. Search and coverage audit

Source screening consulted the linked first-party publication/archive pages, product announcement text and relevant source discovery for this organization as of 2026-10-12. The following are **reproduction search suggestions**, not a log claiming these literal exact queries were all executed. They should be run independently for every month, in official and high-quality secondary sources, before final issue completion:

1. `"Meta" after:2026-04-11 before:2026-10-13 agent coding open weights`
2. `site:about.fb.com 2026 model launch agents`
3. `"Meta" 2026 developer API security pricing`
4. `"Meta" 2026 independent benchmark and criticism`

**Audit limitations:** Search-hit totals, all screened/excluded URL counts, frozen web snapshots, completeness/recall and an independently audited secondary corpus were **not measured**. The included events below are a bounded purposive screen, not an enumeration of every release. The seven partial/full month segments are displayed even when an event was not found. **An unfilled month is missing evidence, not a zero-activity finding.** Verify link accessibility, page update history, publication timezone, actual release date vs article date and region/plan availability before declaring the report done. No web scraping or private-user data collection.

## 2. Identity and product boundary

Meta Platforms, Inc. is the corporate entity; Meta AI, Muse-family models and Muse Code are product names rather than independent firms. The April 8 Muse Spark announcement predates the observation window even if a later update appears on the page.

Public first-party landing/news channels identify product offerings, but this report does not independently verify corporate cap tables or product rights. April 8 announcement is a pre-window baseline, not an April 12+ release; provider-reported model availability does not verify weights licensing.

## 3. Month-by-month candidate events

| Period | Source-linked discovered candidate(s) | Coverage characterization |
|---|---|---|
| 2026-04-12..30 | No event documented in this bounded source subset | Unresolved coverage; not evidence of inactivity |
| 2026-05 | No event documented in this bounded source subset | Unresolved coverage; not evidence of inactivity |
| 2026-06 | [New AI tools to help make things happen on Facebook](https://about.fb.com/news/2026/06/new-ai-tools-to-help-you-make-things-happen-on-facebook/) | First-party pages; see events |
| 2026-07 | [Muse Spark acts across tasks](https://about.fb.com/news/2026/07/meta-ai-muse-spark-doesnt-just-think-it-acts/) | First-party pages; see events |
| 2026-08 | [Muse Glimmer open agentic model](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model) | First-party pages; see events |
| 2026-09 | [Meta enterprise platform launch](https://about.fb.com/news/2026/09/launching-meta-enterprise-platform/) | First-party pages; see events |
| 2026-10-01..12 | [Muse Wonder and Muse Wonder Full](https://about.fb.com/news/2026/10/introducing-muse-wonder-models/) | First-party pages; see events |

## 4. Dated evidence and feature map

| Event | Published / underlying event | Source-linked provider claim or dated documentary event | Availability / constraint | Evidence grade and independent check | Relevant objectives |
|---|---|---|---|---|---|
| CI-005-01 | 2026-06-15 / event day not independently timed | [New AI tools to help make things happen on Facebook](https://about.fb.com/news/2026/06/new-ai-tools-to-help-you-make-things-happen-on-facebook/) — Meta describes AI-assisted actions on Facebook; not a coding-tool outcome. | shipped; Product scope and rollout not independently tested. | Provider E1; independent efficacy **not** verified | M1 |
| CI-005-02 | 2026-07-24 / event day not independently timed | [Muse Spark acts across tasks](https://about.fb.com/news/2026/07/meta-ai-muse-spark-doesnt-just-think-it-acts/) — Meta describes task actions and integrations for Muse Spark 1.1. | shipped; Provider reports scope; third-party task acceptance missing. | Provider E1; independent efficacy **not** verified | M1;M2 |
| CI-005-03 | 2026-08-10 / event day not independently timed | [Muse Glimmer open agentic model](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model) — Meta introduces a local agentic model with open-weight positioning. | shipped; Check exact model-card license and weights, not merely blog claims. | Provider E1; independent efficacy **not** verified | M1;M5 |
| CI-005-04 | 2026-09-28 / event day not independently timed | [Meta enterprise platform launch](https://about.fb.com/news/2026/09/launching-meta-enterprise-platform/) — Meta announces enterprise agent-platform direction. | shipped; Vendor adoption and security claims not externally reproduced. | Provider E1; independent efficacy **not** verified | M1;M4 |
| CI-005-05 | 2026-10-12 / event day not independently timed | [Muse Wonder and Muse Wonder Full](https://about.fb.com/news/2026/10/introducing-muse-wonder-models/) — Meta reports Muse Wonder Model API and Muse Code availability, with broader consumer rollout future. | shipped; No proof weights available; access restricted by product/subscription; benchmark claims first-party. | Provider E1; independent efficacy **not** verified | M1;M2;M5 |

**Grading:** **E1** = provider-described release or policy. It supports attribution and reported availability, **not** reproducible behavior, quality, adoption or effectiveness. API version/docs and actual package licenses remain to be independently inspected; **E3/E4 is not awarded** to vendor metrics. The event CSV separately records class, observed limitations and link provenance. `shipped` means the **provider described availability** on the date, not independently validated access. **No claims about measured carbon impact or representative adoption.**

### Feature, integration, licensing and security boundaries

- **Current/new capabilities reported by provider:** Meta is moving agent capabilities from consumer assistance into developer APIs, local deployment options and enterprise workflows; availability and model-weight access vary by product.
- **Availability:** check every event's status (including preview and future-only); descriptions of features are not interchangeable with externally accepted user tasks.
- **Open-source/API/license:** Do not assume all Muse models are open-weight. Treat claims about automated actions, model quality and security as first-party reports.
- **Security and provenance:** do not execute untrusted build instructions, model install scripts or agent-recommended dependencies; record exact artifact identities, license, origin, signing/release tag, vulnerability results and permissions.
- **Economic context:** model/API prices, tokens, human review, CI and ongoing support must be measured per functional task. Vendor throughput claims are not metered kWh or emissions.

## 5. Public roadmap / intention (not independently guaranteed)

**Direction attributable to the company's publications:** Meta is moving agent capabilities from consumer assistance into developer APIs, local deployment options and enterprise workflows; availability and model-weight access vary by product.

A roadmap statement, planned support sunset, future model release or planned deployment **must not** be counted as generally available in the window. See specific `announced_only` and `preview` items in the dated table. Commitments are scope- and time-specific, and product marketing is a weaker evidence class than a pinned artifact and repeated independent task result.

## 6. Analyst interpretation, alternatives and disconfirmation (2027–2031)

| Conditional inference — NOT company commitment | Motivation | Rival explanation | Disconfirming observation |
|---|---|---|---|
| Agent-capable models and local-weight developer offerings could reduce integration friction for narrower software tasks. | Above source-linked product directions (E1) | Hosted proprietary models may remain simpler than local weights, or agent risk/reviewer time may exceed local benefits. | Independently tested local integration fails functional acceptance or costs more in total reviewer time. |

**Confidence:** exploratory/low until independent task comparisons and lifecycle measurement. Some genuinely useful reusable components predate this six-month interval; they remain eligible as controls/candidates, not excluded as old technology.

## 7. Mapping to the study's M1–M7 objectives

| Question | Needed observation rather than a product popularity proxy |
|---|---|
| M1 agent/workflow change | Timestamped, consented and version-pinned task use; feature availability is **not adoption** |
| M2 accepted quality and review load | Frozen external acceptance suite; failures, review minutes, defects and follow-up counted for **all assigned tasks** |
| M3 discoverability | Prospective matched repo controls and pre/post visibility measures with exposure/selection confounding |
| M4 independent reuse | Audited outsider import, deployment or working repeat-use; stars and installs alone insufficient |
| M5 reuse vs rebuilding | Pre-screened OSS candidates, provenance/license/security, missing/no-solution cases and same objective task |
| M6 whole lifecycle | Same functional unit; human time, provider costs, CI/hosting, runtime, upgrades and upstream burden; kWh only if metered or transparently modeled |
| M7 maintainer intervention | Ethics-reviewed opt-in onboarding/API/docs intervention; independent first-use success and no artificial star boosting |

These are study **measurement targets**, **not observations** of M1–M7 effects in this report.

## 8. Practical, falsifiable pilot for the maintainer's own repository

**Repository:** [GitHub Trending 1000 Study](https://github.com/MSKazemi/github-trending-1000-study) (existing offline CLI and synthetic fixture; do not scrape live Trending).

**Practice to test:** Compare implementing one existing offline study-parser summary using the current Python CLI versus reusing a documented local model-assisted task plan without new parsing code.

**Treatment/comparator:** Arm A: existing CLI instructions without new agent task-plan template; Arm B: the same pinned CLI and synthetic fixture with a reusable agent task-plan and access rules.

**Freeze before treatment:** same repository SHA, dependency/model versions, synthetic inputs, objective expected outputs, task/time cap and evaluator; record failures and no-solution tasks. A second person creates or freezes acceptance tests before any agent-generated change.

**Primary outcome and verifiable reuse:** Independent outsider produces exactly the frozen expected JSONL rows and summary, without network calls or mutations; count all assigned attempts and 30-day downstream reuse of that CLI output.

**Costs / constraints:** record active human time, reviewer minutes, task-level billed/model tokens where known, CI runtime, 30-day defects, code provenance, package-license/security checks and any upstream support work. Tokens/LOC/stars are **not kWh or CO2e**. Prospective experiment **not run**; sample size/power and human consent not secured.

**Stop/reversal:** Reject the template if it adds API/hosting expense, leakage or review overhead without increasing accepted first-use completion.

**Transferable maintainer lesson:** prefer a reusable, versioned interface with an independently testable first-use task over a flashy new repository; test whether verified outside use improves without shifting hidden maintenance/security costs.

## 9. Evidence quality, counterclaims and pending QA

- **Observed in documentation:** 5 directly linked dated source events, primarily first-party. Only the publication/product claims and their reported availability are supported.
- **Not demonstrated:** independent feature efficacy, benchmark validity, customer/OSS adoption, earned GitHub attention, per-task cost savings, kWh/CO2e, or causal environmental benefit.
- **Counterclaim / specific uncertainty:** April 8 announcement is a pre-window baseline, not an April 12+ release; provider-reported model availability does not verify weights licensing. Hosted proprietary models may remain simpler than local weights, or agent risk/reviewer time may exceed local benefits.
- **Required next verification:** (1) independent second-reviewer date/link/identity pass; (2) seven-segment systematic queries with preserved screen counts and exclusion rationale; (3) inspect exact weights/code license, APIs, prices, status and data policies; (4) seek credible independent adverse/critical reporting; (5) duplicate/correction and secondary coverage audit; (6) independent task trial and tests before recommending broad adoption.
- **Review state:** analyst-drafted with source URLs, independent human factual QA **pending**, no full Python test suite run for this documentation-only proposal. Keep the issue and PR open/draft; **do not merge** or close until criteria satisfied.
- **Cross-link:** distinct validated articles may enter [#56 news corpus](https://github.com/MSKazemi/github-trending-1000-study/issues/56) after its own verification; no `NEWS-` ID minted by this screen.

**Validity conclusion:** The only defensible output here is a **testable engineering hypothesis** and a documented source shortlist; not a conclusive company ranking or a green-coding result.

### Documentary recheck — 2026-10-13 (analyst pass, not independent reviewer)

- [Muse Glimmer August 10 release](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model) is directly dated **2026-08-10**, and the [published Hugging Face model card](https://huggingface.co/meta-models/Muse-Glimmer-30B) displays **Apache-2.0** and downloadable artifacts. This is a **specific-model artifact/license cross-check**, not proof of safe downstream use, training-data rights, or a reproducible runtime result. Record exact model revision SHA before reuse; do **not** infer that other Meta models share its license.
- [Muse Wonder October 12 release](https://about.fb.com/news/2026/10/introducing-muse-wonder-models/) explicitly distinguishes Muse Wonder API/Muse Code access, Wonder Full for subscribers and a *future* Muse rollout. [Axios on October 12](https://www.axios.com/2026/10/12/meta-new-ai-models-anthropic-openai) provides an **independent news account of the announcement**, **not** independent benchmark/agentic-function reproduction; no released Wonder weights are established by these links.
- [June 15 Facebook tools](https://about.fb.com/news/2026/06/new-ai-tools-to-help-you-make-things-happen-on-facebook/) primarily concerns *consumer social-platform experiences*. Its relationship to third-party OSS code reuse is **indirect**; it must not enter an estimate of coding-agent releases or software-reuse success.

**New practical checkpoint:** In any model-selection comparison, require versioned model card, exact weights/access conditions, license and objective external-task completion; a product-family brand is not a reusable artifact identifier.
