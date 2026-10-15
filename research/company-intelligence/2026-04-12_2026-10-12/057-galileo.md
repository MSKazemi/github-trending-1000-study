# Galileo — provisional six-month technology intelligence screen (057)

> **Provisional source-lead screen (2026-10-16):** this report, its [event ledger](057-galileo.events.csv) and [search log](057-galileo.search-log.md) are **provisional, AI-assisted documentary source leads** for [issue #125](https://github.com/MSKazemi/github-trending-1000-study/issues/125). They are **unreviewed by a qualified human**; factual/link review, source-access/rights review and methods review remain **pending**. This is not scientific or security sign-off; issue #125 was closed on maintainer instruction (2026-10-16) with these review gates still open; reopen it if review finds a defect.

- **Watchlist:** 057; [issue #125](https://github.com/MSKazemi/github-trending-1000-study/issues/125). Study lens: *task-grounded evaluation and production control*.
- **Window:** 2026-04-12 through 2026-10-12 inclusive; **source-screened on 2026-10-16**. Exact UTC search-run times, full search result counts, immutable page snapshots and an independent reviewer are unavailable. The session's web-search budget ran out after ten searches; two planned searches were **not executed** (see [search log](057-galileo.search-log.md)).
- **Status:** **provisional dated documentary screen (30 traceable source leads covering all seven calendar segments); not reviewed by a qualified human; factual/link, source-access/rights and methods review pending**. Not independently verified task outcomes, exhaustive retrieval or human-approved scientific completion. [Event ledger](057-galileo.events.csv), [month-segment queries and inclusion/exclusion log](057-galileo.search-log.md), [study method](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md).
- **Official sources checked:** [Galileo](https://galileo.ai/), [Galileo blog index](https://galileo.ai/blog), [Galileo docs release notes](https://docs.galileo.ai/release-notes), [Splunk Agent Observability release notes](https://agent-observability-docs.splunk.com/release-notes), [Splunk acquisition page](https://www.splunk.com/en_us/about-splunk/acquisitions/galileo.html), [Cisco acquisition post](https://blogs.cisco.com/news/cisco-announces-the-intent-to-acquire-galileo), and public GitHub release metadata for [galileo-python](https://github.com/rungalileo/galileo-python), [galileo-js](https://github.com/rungalileo/galileo-js), [agent-control](https://github.com/agentcontrol/agent-control) and [eval-engineer](https://github.com/Galileo-Agent-Labs/eval-engineer). **Claim grading** is company-watch E0–E4, not the separate [2027 lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md).

## 1. Discovery, coverage and exclusions

The [source screen](057-galileo.search-log.md) covers all seven partial/full month segments and records every search actually run, every page opened, and the include/exclude decision. It is **not** an exhaustive internet search: search-result totals were not exposed by the tool and are recorded as unknown, not zero. Independent (non-vendor) reporting was found for **April** (Futurum analyst note), **June** (TFiR interview) and **September** (NAND Research analyst note) only; for **May, July, August and October 1–12** the ledger rests on first-party documents and GitHub release metadata, and the existence of independent coverage in those months is **unknown** because two planned searches could not be run.

Name collisions were explicitly excluded: the EU Galileo satellite system, Debian/Ubuntu `galileo` packages, Galileo Suite (galileosuite.com), the GALILEO library consortium, and an energy-sector "Galileo Technologies" that one aggregator conflated with the Cisco transaction.

## 2. Corporate/product identity and rights baseline

**Entity:** Galileo Technologies, Inc. ([Cisco, Apr 9 2026](https://blogs.cisco.com/news/cisco-announces-the-intent-to-acquire-galileo)), an AI evaluation, observability and guardrail vendor (galileo.ai). **Ownership change in window:** Cisco announced its intent to acquire on **Apr 9 2026 (pre-window baseline)**; a **May 22 2026 update** on the same Cisco post states the acquisition was completed. Financial terms were not disclosed and no regulatory filing was checked. **Brand change in window:** Galileo's own [release notes](https://docs.galileo.ai/release-notes) state that "as of August 7, 2026, Galileo is now Splunk Agent Observability"; galileo docs apply to customers onboarded before that date, and later customers are sent to Splunk's docs site. The [galileo.ai homepage](https://galileo.ai/), read on 2026-10-16, still presents "Galileo" with no Cisco/Splunk mention — an unresolved brand-continuity inconsistency, not evidence that the rebrand was reversed.

**Rights:** the managed platform (evaluations, Luna evaluator models, Signals, Protect/runtime guardrails, Luna Studio) is proprietary SaaS/VPC/on-premises software; no source availability is claimed for it. Public SDKs are **Apache-2.0** ([galileo-python](https://github.com/rungalileo/galileo-python), [galileo-js](https://github.com/rungalileo/galileo-js), per GitHub license metadata and release notes). **Agent Control** ([agentcontrol/agent-control](https://github.com/agentcontrol/agent-control)) is Apache-2.0 per repository metadata; its open-source launch was **Mar 11 2026 (pre-window baseline)**. **Eval Engineer** reports MIT in GitHub repository metadata while its launch blog only says "open source" without naming a license — license text must be checked at a pinned commit before reuse. Whether Agent Control and the SDKs keep their governance and licensing after the Cisco/Splunk transition is **not documented** in any source found.

## 3. Seven-segment dated chronology

| Period | In-window source evidence (source publication dates) | Availability and attribution limits |
|---|---|---|
| Apr 12–30 | [Apr 13 Futurum analyst note](https://futurumgroup.com/insights/cisco-to-acquire-galileo-ai-agent-observability-cant-run-at-human-speed/) on the Apr 9 deal; [Apr 23 galileo-a2a v1.0.0](https://github.com/rungalileo/galileo-python/releases/tag/galileo-a2a-v1.0.0); Apr 24 [release notes](https://docs.galileo.ai/release-notes): multimodal evaluation, Signals integrations, error catalog | Apr 9 intent announcement and Apr 10 trade coverage **excluded** (pre-window); Futurum is opinion, not a test |
| May | May 8 notes: A2A tracing, OTel (beta), Model Pricing (beta preview); [May 14 galileo-adk v2.0.0](https://github.com/rungalileo/galileo-python/releases/tag/galileo-adk-v2.0.0); [May 19 Eval Engineer alpha](https://galileo.ai/blog/introducing-eval-engineer-bringing-eval-expertise-to-claude-and-codex); [May 20 Luna Studio blog](https://galileo.ai/blog/evals-you-can-trust-without-the-bill-luna-studio) + May 22 release note; [May 22 Cisco completion update](https://blogs.cisco.com/news/cisco-announces-the-intent-to-acquire-galileo); [May 28 Splunk integration blog](https://www.splunk.com/en_us/blog/leadership/splunk-observability-galileo.html) | Eval Engineer is **alpha**; Luna Studio **enterprise-only**; blog pages show a later Oct 14 metadata timestamp (date conflict recorded) |
| June | [Jun 2 Splunk Cisco Live blog](https://www.splunk.com/en_us/blog/observability/splunk-observability-at-cisco-live.html) names Splunk Agent Observability; Jun 5 Agent Control for enterprise customers; [Jun 5 agent-control v8.0.0](https://github.com/agentcontrol/agent-control/releases/tag/v8.0.0) removes the Luna2 evaluator; [Jun 17 TFiR interview](https://tfir.io/cisco-splunk-federated-analytics-ai-agent-governance/); Jun 23 multi-turn experiments | Splunk posts carry "when-and-if-available" disclaimers; no Galileo blog posts after May 26 |
| July | Jul 7 AI Assistant **beta**, webhook alerts; [Jul 15 galileo-python v2.5.0](https://github.com/rungalileo/galileo-python/releases/tag/v2.5.0) annotation-queue SDK; Jul 21 AI-assisted code metrics, Model Pricing GA; [Jul 30 galileo-python v2.6.0](https://github.com/rungalileo/galileo-python/releases/tag/v2.6.0) gateway headers | First-party only; independent July coverage **unknown** |
| August | Aug 4 Annotation Queues **GA**; **Aug 7 "Galileo is now Splunk Agent Observability"**; [Aug 7 Splunk on-premises note](https://agent-observability-docs.splunk.com/release-notes); [Aug 14 agent-control v8.5.0](https://github.com/agentcontrol/agent-control/releases/tag/v8.5.0) default controls (part 1) | Splunk release notes show no entries Aug 8–Sep 7; independent August coverage **unknown** |
| September | Sep 8 AI Assistant **GA**; Sep 15 Tokenomics; [Sep 16 Splunk .conf26 blog](https://www.splunk.com/en_us/blog/observability/splunk-observability-at-conf26-optimize-ai-at-scale.html); [Sep 16 galileo-js v2.3.0](https://github.com/rungalileo/galileo-js/releases/tag/v2.3.0); [Sep 21 NAND Research](https://nand-research.com/splunk-conf26-building-the-trust-layer-for-agentic-ai/) | Vendor says "available September 2026"; analyst says GA; Essentials/Premier editions only **announced** for November |
| Oct 1–12 | [Oct 9 agent-control v8.12.0](https://github.com/agentcontrol/agent-control/releases/tag/v8.12.0) per-control duration; Oct 9 Luna-3 for enterprise users ([Splunk notes](https://agent-observability-docs.splunk.com/release-notes)) | Oct 13 evaluator-access note and Oct 14 galileo-python v2.7.0 **excluded** (post-window) |

See the [CSV](057-galileo.events.csv) for **30 separate dated source records**. This is a purposive selection of material events, not every SDK or Agent Control release (31 Agent Control tags alone fall in-window). Release-note dates are the displayed entry dates, not independent UTC archive timestamps. `event_date_utc` is filled only for GitHub release timestamps, the Cisco completion update, the rebrand date and the pre-window event a commentary discusses.

## 4. Feature, rights and security cross-check

| Evidence cluster | What is supported by the cited document | Important non-equivalence or counterexample |
|---|---|---|
| Evaluation loop: [Luna Studio](https://galileo.ai/blog/evals-you-can-trust-without-the-bill-luna-studio) (May), dataset metric validation (May 8, Jun 23), AI-assisted code metrics (Jul 21), [Luna-3](https://agent-observability-docs.splunk.com/release-notes) (Oct 9) | Vendor describes fine-tuned small-model judges from 300–500 labelled samples and newer evaluator models | "98% cheaper", "150 ms" and "faster and more accurate than Luna-2" are **vendor claims without published task denominators**; a judge model is not an independent acceptance test |
| Human review: annotation queues (enterprise beta May → GA Aug 4) and [SDK support](https://github.com/rungalileo/galileo-python/releases/tag/v2.5.0) | Expert-review workflow and annotator-agreement charts exist | Tooling for agreement is not evidence of measured inter-rater reliability on any real task |
| Production control: [Agent Control OSS](https://github.com/agentcontrol/agent-control) releases + Jun 5 enterprise availability | Central policy server, out-of-box controls (part 1, Aug 14), per-control latency capture (Oct 9) | Blocking efficacy for prompt injection/PII not independently measured; **v8.0.0 removed the Luna2 evaluator** from the OSS project — a compatibility break whose rationale is not stated |
| Coding-agent integration: [Eval Engineer](https://github.com/Galileo-Agent-Labs/eval-engineer) (alpha) | Installs skills into `.claude/skills` / `.agents/skills` so Claude Code/Codex can inspect traces, make one bounded change and re-verify | Requires a Galileo backend; self-verification by the agent against vendor metrics is exactly what this study's protocol warns against using as acceptance |
| Cost telemetry: Model Pricing/Integration Costs (beta → GA), [Tokenomics](https://www.splunk.com/en_us/blog/observability/splunk-observability-at-conf26-optimize-ai-at-scale.html) (Sep 15/16), JS per-modality tokens | Spend/adoption tracking by provider, model and user | **Tokens or spend are not energy or CO2e**; per-user drill-down raises consent/privacy questions |
| Security disclosures | GitHub security-advisory endpoints for agent-control and galileo-python returned empty lists on 2026-10-16 | **Not** evidence of absence of vulnerabilities; no vendor security-bulletin page found |

**Counterevidence and rights:** the Futurum analyst explicitly questions whether guardrail *enforcement* survives as a distinct capability or is reduced to monitoring inside Splunk; NAND Research cautions that teams "must first instrument agents and coding tools consistently". Apache-2.0 SDKs and Agent Control do not license the hosted Luna models, the Luna Studio synthetic-data pipeline (stated as not open-sourced) or Splunk services.

## 5. Publicly stated direction versus shipped functionality

| Dated first-party source | Company-stated near-term intention | Current research classification |
|---|---|---|
| [Cisco, May 22 update](https://blogs.cisco.com/news/cisco-announces-the-intent-to-acquire-galileo) | Galileo to "strengthen Cisco's Splunk Observability portfolio" | Transaction **reported completed** by acquirer; integration outcome not measurable from this |
| [Splunk, May 28](https://www.splunk.com/en_us/blog/leadership/splunk-observability-galileo.html) | Integrate Galileo evaluations, guardrails and Luna-2 into AI Agent Monitoring | **Announced only** at publication; later partially reflected in Aug 7 rebrand and Sep 16 availability claim |
| [Splunk .conf26, Sep 16](https://www.splunk.com/en_us/blog/observability/splunk-observability-at-conf26-optimize-ai-at-scale.html) | Essentials and Premier editions "coming in November"; business-value linking "soon"; forecasting with a Cisco time-series model | **Announced only**; carries a "when-and-if-available" disclaimer |
| [Luna Studio blog, May 20](https://galileo.ai/blog/evals-you-can-trust-without-the-bill-luna-studio) | Evaluate every trace rather than samples because small-model economics make it affordable | **Vendor positioning**, not a measured coverage or cost outcome |

A public intention is not a scheduled delivery. These sources cannot establish Cisco/Splunk's 2027–2031 strategy.

## 6. Conditional 2027–2031 outlook (analyst hypotheses, not company statements)

| Testable scenario | Rival cause | Disconfirming observation |
|---|---|---|
| Evaluation-plus-guardrail tooling becomes bundled into general observability suites rather than sold standalone | Standalone OSS evaluators (e.g. framework-native test harnesses) stay sufficient for most teams | Agent Control and SDKs stay actively maintained and independently adopted outside Splunk |
| Small-model judges replace frontier-model judges for continuous evaluation | Judge drift and domain shift erase the cost advantage | Independent replication shows lower agreement with blinded human labels than a frontier judge or a deterministic test |
| Coding agents increasingly run "eval-driven" fix loops (Eval Engineer pattern) | Ordinary CI tests already provide the same signal at lower cost | Hidden, independently authored acceptance tests show no improvement over plain CI-driven loops |

## 7. M1–M7 study relevance

| Construct | Prospective measurement, not inferred conclusion |
|---|---|
| **M1** coding practice | Opt-in records of coding-agent sessions with vs without an eval-skill bundle (Eval Engineer pattern); availability ≠ adoption |
| **M2** accepted task quality | Independently authored hidden acceptance tests; compare vendor-judge scores against them, counting **all** attempts including failures |
| **M3** discovery | Not addressed by these sources; a corporate acquisition and rebrand are confounders for any discoverability panel |
| **M4** verified third-party reuse | Trace consented downstream integrations of Apache-2.0 Agent Control/SDKs; GitHub release counts are not users |
| **M5** reuse-first | Compare existing CI tests + an OSS evaluator against Agent Control/Galileo SDK for one fixed task; include license and lock-in costs |
| **M6** lifecycle human and energy cost | Measure setup/review/rework minutes and metered CI/runtime energy if instrumented; **no token-to-CO2e conversion**, and Tokenomics spend data is not energy |
| **M7** actionable interventions | Whether an evaluation/guardrail layer changes maintainer outcomes at all must be tested on independently graded tasks |

## 8. One falsifiable maintainer experiment (reuse-first; not executed)

**Target:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study) offline test suite and an isolated sandbox; the study's live Trending `capture` remains **disabled under source-access policy** and nothing here changes that.

**Question:** does adding an LLM-judge evaluation/guardrail layer to a coding-agent fix loop improve independently accepted outcomes over the existing `unittest` suite alone?

**Frozen task set (preregister first):** 12 synthetic, offline bug-fix tasks against committed fixtures (e.g. CSV ledger validation, date-window checks), each with **hidden acceptance tests authored by someone other than the agent operator** and kept out of agent context; include at least 2 no-solution/ill-posed tasks in the denominator.

**Comparator A (reuse-first, existing):** coding agent + repository's existing `python -m unittest discover -s tests -v` as the only feedback. **B:** same agent, model version and budget + Apache-2.0 Galileo SDK / Agent Control (pinned versions, license checked at a pinned commit) scoring each attempt with a configured evaluator; only synthetic data leaves the machine, and only if the service terms are reviewed and accepted.

**Primary endpoint:** hidden-test-accepted tasks / **all assigned tasks** (failed, refused and timed-out included). **Secondary:** reviewer minutes, rework iterations, judge–hidden-test disagreement rate, setup and maintenance minutes, wall-clock time, and metered energy **only if actually instrumented**.

**Stop rule:** stop B if any non-synthetic data would be transmitted, if license/terms are unclear, if setup exceeds 4 human hours, or if after the 12 tasks B does not improve accepted tasks by at least 2 over A. Prefer A when results tie. **No trial executed, no effects estimated.**

## 9. Evidence quality, limitations and missingness (2026-10-16)

- **Observed/shipped (vendor-documented, E2):** release-note entries and GitHub releases dated Apr 24 – Oct 9; the strongest records are versioned GitHub releases with Apache-2.0 notices.
- **Claims only (E1):** cost/latency/accuracy figures for Luna Studio, Luna-2/Luna-3 and guardrails; Splunk integration intentions; November editions.
- **Independent evidence:** only two analyst notes and one media interview; none tested the product. **No E3/E4 evidence.**
- **Contradictions:** displayed vs metadata dates on three Galileo blog pages (May vs Oct 14); OWASP control-plane post dated Apr 21 in the index but May 15 on the page; homepage still unbranded "Galileo" after the Aug 7 rebrand note; Splunk's Sep 16 blog avoids a GA label while NAND Research calls it GA.
- **Unknowns:** independent reporting for May, July, August and Oct 1–12; closing date/terms of the acquisition; post-acquisition governance of Agent Control and the SDKs; customer migration terms; any security advisories outside GitHub's database; search-result denominators.
- **Pending:** human factual/link spot-check, source-access/rights review, methods review, and the two unexecuted searches. **Issue #125 was closed on maintainer instruction (2026-10-16); this screen alone is not scientific completion — reopen it if factual, rights or methods review finds a defect.** on the basis of this screen.
