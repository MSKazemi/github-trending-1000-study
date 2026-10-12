# Faculty-style critical review: from 1,000 Trending repositories to validated reuse-first engineering

**Date:** 2026-10-12. **Status:** independent AI-assisted *advisory proposal*, **not** an actual panel of professors, scientific peer review, external endorsement, preregistration, field observation or finding from this study. Intended to inform, not override, the maintainers' protocol and ethics decisions.

**Repository reviewed:** [GitHub Trending 1000 Study](https://github.com/MSKazemi/github-trending-1000-study), its main-branch protocol, audit, agent-adoption methods, current study roadmap, literature registry and open issues, observed on this date.

## Executive recommendation

Do **not** optimize this research for 1,000 stars, 1,000 scraped entries, 1,000 AI headlines or 1,000 Markdown pages. Optimize for a small number of **independently verified, replicable, decision-changing conclusions** about building, finding and maintaining useful software in the agentic era.

Proposed central question:

> For a prospectively defined software task, under which technical, human and lifecycle conditions does **search -> independent verification -> safe reuse or upstream improvement** outperform building new code with or without coding agents?

A strong negative result is a valid result. Reuse is not always the correct choice; different specifications, threats, intellectual-property constraints, accessibility needs, educational goals and runtime profiles can justify fresh implementations.

## Current evidence-readiness decision (not a new audit)

The repository has meaningful research tooling and written safeguards, but **no verified 1,000-repository longitudinal cohort, independent real-world task gold set, consenting developer randomized trial or measured net lifecycle carbon reduction**. The recorded [freeze-status audit](PROTOCOL_FREEZE_STATUS_2026_10_12.md) still reports permission, real-page QA, task/acceptance-test design, power, privacy, independent methods approval and external preregistration as pending. The [older repo audit](REPOSITORY_AUDIT_2026-10-12.md) describes an earlier commit/PR snapshot; do not assume its historical PR and file counts remain current.

**Faculty-style verdict:** instrumented-methods prototype, **not ready for confirmatory scientific claims**. Read [the proposed v0.3 preregistration](PREREGISTRATION_DRAFT_2027.md) as an unfrozen draft. The immediate bottleneck is securing independent *real* evidence rather than authoring another broad strategy.

## Strong scientific design: three distinct outputs, not one mixed score

| Workstream / proposed paper | Unit and target population | Primary defensible output | Identification / limitation |
|---|---|---|---|
| **A. The agent-era open-source ecosystem (observational)** | Public observed Trending appearances and independently sampled comparison repositories; stable repo IDs with pre-observation characteristics | Report associations between practices, credible agent events, visibility and independently audited adoption/reuse proxies, with 30/90/180-day follow-up | Trending is an opaque attention surface; source/agent detection, selection, time-varying confounding, no unqualified causal effects |
| **B. Reuse-first versus conventional coding (prospective experiment)** | Independently chosen, frozen real software tasks *before* candidates/search outcomes are known | All-assigned-task success, total nonoverlapping active human time, independent correctness/security, total cost, reuse opportunity and maintainability | Randomized and independently adjudicated only after consent and methods review; failures and absent viable components stay in denominator |
| **C. Environmental break-even (conditional paired study)** | Functionally equivalent completed workloads, versions and declared lifecycle boundaries | Measured or appropriately qualified modeled whole-boundary energy/carbon **with uncertainty and sensitivity to runtime, CI, support, hardware, rebound** | No universal grams of CO2 per token; incomplete provider inference-energy data means only partial-boundary conclusions |

**Recommendation with budget constraints:** Begin with Study A's small permitted parser-quality pilot and Study B's **feasibility** task intake. Keep the 2x2 human/agent x usual/reuse-first design as an option; if recruitment and power cannot support four arms, preregister a simpler **two-arm comparison within a fixed agent setup** before exposure to outcomes. Do not retroactively redefine the primary estimand. Study C should proceed only if equivalent functionality and sufficient energy-boundary evidence exist.

## Methods a full professor would require before interpreting results

| Scientific failure mode | Minimum credible safeguard | Existing tracker |
|---|---|---|
| Success is selected because an existing library was easy to find | Sample **tasks before code search**; include no-match tasks, failed tasks, unknowns and abandonment; independently freeze task specs and acceptance tests | [#21](https://github.com/MSKazemi/github-trending-1000-study/issues/21), [#25](https://github.com/MSKazemi/github-trending-1000-study/issues/25) |
| High stars/trending is mistaken for usefulness | Separate discovery exposure, validated downstream use, independent acceptance and maintainer outcomes; do not merge into one unvalidated scalar | [#16](https://github.com/MSKazemi/github-trending-1000-study/issues/16), [#8](https://github.com/MSKazemi/github-trending-1000-study/issues/8) |
| Agent authorship is guessed from an AGENTS.md or style | Use verified, dated public agent events or consented tool logs; absence of trace remains **unknown**, not human-only | [Agent evidence definitions](AGENT_ADOPTION_MEASUREMENT.md) |
| Matched controls are treated as proof of causality | Predeclare pre-exposure covariates, source coverage, overlap, timing; check pre-trends, placebo windows, negative controls, sensitivity and missingness; label observational estimates as associations | [#3](https://github.com/MSKazemi/github-trending-1000-study/issues/3), [#13](https://github.com/MSKazemi/github-trending-1000-study/issues/13) |
| Fast PR merging substitutes for high quality | Hidden functional/security tests and human adjudication independent of implementation; track escaped defects, rework, integration and support | [#21](https://github.com/MSKazemi/github-trending-1000-study/issues/21), [#22](https://github.com/MSKazemi/github-trending-1000-study/issues/22) |
| AI seems to save time by moving work elsewhere | Instrument review, integration, learning, prompt/search effort, parallel-agent supervision, rework, upstream maintainer burden and 30/90-day repair | [#10](https://github.com/MSKazemi/github-trending-1000-study/issues/10), [#24](https://github.com/MSKazemi/github-trending-1000-study/issues/24) |
| The preferred method wins because many metrics were explored | Choose primary and quality/no-harm guardrails with a statistician and pilot-informed power **before confirmatory analysis**; report nulls, uncertainty and exploratory tests separately | [#27](https://github.com/MSKazemi/github-trending-1000-study/issues/27), [#13](https://github.com/MSKazemi/github-trending-1000-study/issues/13) |
| Token count or fewer LOC is reported as green savings | Declare functional unit and energy boundary; measure what is observable and report unknown inference/embodied/water terms, maintenance and runtime horizon separately | [#18](https://github.com/MSKazemi/github-trending-1000-study/issues/18), [#23](https://github.com/MSKazemi/github-trending-1000-study/issues/23) |

**Special warning about N=1,000:** 1,000 is a useful nominal sample ambition but **not a power argument**. The effective sample depends on deduplication, missing follow-ups, clustering by owner, language and time, eligibility, and the smallest meaningful effect. Estimate yield and variance from an approved pilot; publish actual N and representativeness limits rather than collecting a convenient mix merely to reach a round number.

**Special warning about independent reuse search:** candidate pools built from GitHub keywords, ecosystems/registries, code search and expert judgment provide *pooled relevance*, **not guaranteed recall of every viable solution**. Unknown must not become no-solution. Record baseline component release/version, license, security, compatibility and executable task evidence.

## Important relevant published evidence (not findings of this repository)

These sources were checked as **source documents/abstracts**, not fully reproduced or meta-analyzed. The numerical claims are source-population-specific. In a systematic review, screen versions and assess risk of bias first.

| Evidence and source | What the authors actually support | Critical limit / methodological lesson |
|---|---|---|
| [Huang et al., *More Code, Less Reuse*, MSR 2026](https://doi.org/10.1145/3793302.3793622) | Studied AI-agent PRs showed redundancy and missed reuse opportunities under their code-quality measures | Observational/mining challenge data; cannot generalize prevalence to every agent or repo; warrants independent clone/reuse assessment |
| [Gao et al., *On Autopilot?*, MSR 2026](https://doi.org/10.1145/3793302.3793573) | In their analyzed AI co-authored PR sample, about 80% were merged without **explicit** review feedback; agent collaboration and ownership differed | Lack of explicit recorded feedback does **not** prove no human reading or inferior quality; track review trace completeness and decision contexts |
| [Hamza, Siemon & Awan, ESEM 2026](https://doi.org/10.4230/LIPIcs.ESEM.2026.67) | Longitudinal comparisons found some changes in documentation/testing; apparently lighter reviews also occurred in control groups | Observational difference-in-differences; do not attribute broad review trends uniquely to agents without valid parallel-trend assumptions |
| [Ogenrwot & Businge, *PatchTrack*, Empirical Software Engineering 2026](https://doi.org/10.1007/s10664-026-10869-5) | In a **self-admitted ChatGPT-usage** sample, authors observed patch adaptation, selective integration and conceptual reuse, not just verbatim copying | Selected self-disclosures and older ChatGPT interactions; not all coding agents, not an estimate of universal 2026 adoption |
| [METR, 24 Feb 2026 productivity update](https://metr.org/blog/2026-02-24-uplift-update/) | Later developer AI-task productivity research struggled with task/developer selection, payment and concurrent-agent time attribution | Earlier slowdown and later exploratory uplift estimates are **not** a reliable universal 2026 productivity effect; motivate feasibility/time measurement |
| [DORA, 10 Mar 2026 AI-SDLC analysis](https://dora.dev/insights/balancing-ai-tensions/) | Qualitative enterprise software-engineering study reports gains in code generation accompanied by auditing/verification effort | Contextual enterprise survey/qualitative evidence, not a randomized independent reuse effect |
| [Stack Overflow 2026 coding-agent survey](https://survey.stackoverflow.co/2026/ai/data/ai-code-agent) | Among 12,255 respondents to its multi-select tool question, 65.5% named Claude Code and 29.5% Codex | Non-probability respondent subset, overlapping answers: neither global market share nor GitHub repository adoption |
| [Green Software Foundation SCI for AI specification](https://github.com/Green-Software-Foundation/sci-ai/blob/main/SPEC.md) | Defines functional-unit and energy/carbon/embodied-boundary methodology for AI workloads | A standard is a measurement framework, **not** evidence this project has measured or reduced emissions |

**Interpretation across sources:** one study reports reduced explicit PR feedback; another finds time-trend changes in reviews also occur among comparison developers. They investigate different operationalizations/populations. Do **not** smooth this into a universal claim that agents always make review worse, or that every fast merge is safe. That disagreement is a research opportunity for correctly specified baselines.

## Practical 2027 repository-maintainer playbook: test these rather than assert them as causal growth hacks

| Action for your own repositories | Evidence artifact to publish | What to measure |
|---|---|---|
| Write a plain-language one-sentence problem, audience and honest non-goals | README first screen; examples tied to real user tasks | Task comprehension and successful independent onboarding |
| Provide a reproducible <=5-minute quickstart and a minimal real demo | Pinned release, CI-tested clean install, expected example output | Independent fresh-install success/time by platform |
| Make **reuse-first** the default contributor/agent workflow, not automatic copying | AGENTS.md/CONTRIBUTING.md: search alternatives, compare licenses and risks, test & attribute dependencies, explain why new code is necessary | Verified reuse/rework and true upstream links; not mere LOC removed |
| Supply automated functional/security tests and explain test scope | Offline/CI reproducible tests, pinned toolchain and declared unsupported configurations | External acceptance and regression/repair incidence |
| Make contribution and AI-agent boundaries explicit | Limited-permission agent guide, PR template, review/maintainer expectations, no unsolicited mass PRs | Review time, abandoned PRs, maintainers' reported burden |
| Release stable, interoperable interfaces | SemVer policy, changelog, examples, dependency bounds, migration guides, SPDX/attestation when justified | Repeatable downstream integrations and upgrades |
| Make research/engineering claims auditable | Claim/evidence ledger with source/version/date, methodology, unknowns and nulls | Independently verified downstream reuse rather than only stars |
| Measure costs only to the degree justified | Optional human-time, compute and infrastructure boundary sheet; redact private logs | Accepted-task effort and bounded footprint, never invented CO2/token |

**Development rule:** *search first -> evaluate credible alternatives -> verify license/security/fit -> reuse, improve upstream or build new deliberately -> validate externally -> document actual outcome*. The research must measure when this rule helps **and when it fails**.

## 2026-10 to early-2027 gated action plan

| Proposed order | Concrete deliverable | Gate before claiming success |
|---|---|---|
| **0, now** | Reconcile one authoritative Study A/Study B protocol and analysis schema; preserve historical drafts; freeze only after human scientific/privacy review | [#13](https://github.com/MSKazemi/github-trending-1000-study/issues/13), [#27](https://github.com/MSKazemi/github-trending-1000-study/issues/27): signed/versioned amendments and appropriate external preregistration |
| **1, earliest authorized pilot** | Verify source access rules, audit **actual full** captured Trending page across supported windows, stable IDs, misses/ranks and checksums | [#2](https://github.com/MSKazemi/github-trending-1000-study/issues/2): independent reviewer labels; synthetic tests are insufficient |
| **2, next bounded pilot** | Produce 12-20 diverse **feasibility-only** task cards sampled before search, with separate candidates, no-match/unknown strata, hidden task acceptance and two independent rater judgments | [#21](https://github.com/MSKazemi/github-trending-1000-study/issues/21), [#22](https://github.com/MSKazemi/github-trending-1000-study/issues/22): human permission, acceptance freeze, safe candidate testing |
| **3, after feasibility evidence** | Choose viable randomized conditions and primary estimand, power and missingness design; capture all assigned outcomes and concurrency-correct time | [#25](https://github.com/MSKazemi/github-trending-1000-study/issues/25), [#17](https://github.com/MSKazemi/github-trending-1000-study/issues/17): independent statistical approval, consent and protocol freeze |
| **4, conditional later** | Launch prospective complete-source observational enrollment; separately implement calibrated lifecycle paired measurement | [#3](https://github.com/MSKazemi/github-trending-1000-study/issues/3), [#18](https://github.com/MSKazemi/github-trending-1000-study/issues/18), [#23](https://github.com/MSKazemi/github-trending-1000-study/issues/23): observed N, verified preflight and defensible boundaries |

The 2026-11-01 proposed enrollment start in the draft is **not a guaranteed start date**. If necessary prerequisites fail, amend prospectively. Do not backdate records or retroactively claim a 2026 cohort. A smaller clean feasibility result can be more publishable than a nominal 1,000-row sample with ambiguous timestamps.

## Potential scientific publications, only if data become valid

- **Paper A** (empirical software engineering / mining software repositories): *Attention, Agent Traces and Independently Verified Reuse in Open Source, 2026-2027*. No causal claim from Trending membership or public bot traces.
- **Paper B** (ESEM/ICSE/FSE-style empirical evaluation): *Does Reuse-First Agentic Development Improve Independently Accepted Outcomes?* Prespecified randomized contrast, all assigned tasks, human cost and no-harm outcomes.
- **Paper C** (green software / systems / lifecycle): *When is Software Reuse Environmentally Better Than Regeneration?* Functionally equivalent lifecycle scenarios with explicit energy and embodied unknowns.

These are **proposed titles/targets**, not submissions, endorsements or evidence that a result exists.

## Explicit no-go rules

No unauthorized scraping, no extrapolation from Trending rank to real users, no retrospective fake agent adoption dates, no causal labels for observational correlations, no running unknown dependencies with credentials, no claims of fewer emissions from tokens alone, and no paper-grade performance claim from synthetic fixtures or a convenience pilot. No pressure on volunteer maintainers to absorb AI-generated PRs for research without informed permission where required.

**Related repository resources:** [existing hypothetical advisory strategy](ADVISORY_BOARD_STRATEGY_2027_2031.md), [scientific freeze status](PROTOCOL_FREEZE_STATUS_2026_10_12.md), [preregistration draft](PREREGISTRATION_DRAFT_2027.md), [research critical gaps](CRITICAL_RESEARCH_GAPS_2027.md), [source review](READING_LIST_2027.md), [next-step execution plan](NEXT_STEPS_EXECUTION_2026-10-12.md). This memo intentionally **does not supplant** them; it records a dated methodological decision recommendation.
