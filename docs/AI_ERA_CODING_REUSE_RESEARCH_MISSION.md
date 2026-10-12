# Research mission: modern coding, reused software, community value and sustainability

**Decision recorded:** 2026-10-12. **Status:** research-program clarification and draft protocol amendment, NOT a preregistered new primary endpoint or an empirical finding. Applies to the 2027 advice target. Related issue: #41.

## The problem

Modern generative assistants and coding agents can lower the friction of creating code. The scientifically testable question is whether these new workflows change *what gets built*, whether working implementations are independently discovered and reused rather than needlessly re-created, who benefits and bears the costs, and whether software remains trustworthy and maintainable. Code volume, repository count, stars, pull requests and token throughput are insufficient outcome measures.

**Central question:** How have AI-assisted, vibe and delegated-agent coding workflows changed open-source production, quality, discoverability, responsible contribution and independently validated reuse, and which interventions improve net useful outcomes per lifetime human and ecological cost?

**Mission:** derive falsifiable, evidence-graded recommendations for maintainers to produce *more reusable value*, not simply more artifacts or attention. Avoid presenting hypotheses about '2027 best practices' as established findings.

## Separate five constructs, never collapse to one success index

1. **Workflow exposure** — confirmed manual/AI-assisted/prompt-led or agent-delegated methods, model version, time, task and confidence. Config files or stylistic heuristics are NOT authorship proof. Workflow categories can overlap; record concrete human review and delegation rather than assigning personality labels.
2. **Artifact engineering** — independent task correctness, packaging/API stability, reproducibility, tests, security, readable documentation, accessibility and maintainer responsiveness, conditional on project type.
3. **Discovery and attention** — capture-specific Trending appearances/rank, baseline and future stars, external referrals where permitted, and visibility-channel provenance; stars are not equivalent to use.
4. **Independent adoption and reuse** — external working installations, documented downstream dependency/import, reproduced scientific use, independently tested integration, repeat user task, and qualified PRs, each with opportunity/observable denominators.
5. **Lifecycle costs and externalities** — developer active hours, review/rework/upgrade/support minutes, tokens (not an energy unit), metered or carefully modeled kWh, operational overhead, upstream maintainer burden, lifecycle CO2e with uncertainty and scope.

Useful open-source diversity matters. Five interoperable domain tools may produce more public value than one giant repository. Conversely many near-duplicate packages can burden discovery. **Never use repo count alone as a target for reduction.** Reuse can transfer costs or introduce dependencies and vulnerabilities.

## Scientific research questions and disconfirmation

| ID | Question | Required evidence / method | Key disconfirmation or bias |
|---|---|---|---|
| M1 | How did coding workflows change from historical 2024 reference through agent expansion in 2025–27? | Verified release chronology; opt-in tool-use records; repo-month observable markers with accuracy audit | Availability != adoption; earlier Copilot and automated tools predate 2025; detector error |
| M2 | Do different workflows change independently accepted code quality, maintenance/review cost and throughput? | Consented, task-stratified and pre-registered prospective comparison; 2×2 agent/human × reuse-first/usual workflow where feasible | Model/developer/task confounding, cross-task leakage, model updates, missing failures |
| M3 | Which baseline repository practices predict *future* discovery, sustained attention and contributor participation? | Trending panel + independent controls, 30/90/180-day observation, baseline adjustment and chronological holdouts | Reverse causality, platform selection, publicity and broad confounding |
| M4 | Which practices independently improve first-use success, verified external reuse, repeat usage and useful contribution? | Independent user tasks, audit of real downstream integrations and contributors, type-specific usability testing | Stars/downloads/forks do not identify distinct genuine users; observation selection |
| M5 | When does search/verify/adapt/upstream contribution beat generating a new solution? | Task-first gold candidate pool; matched acceptance specs; deliberate missing/no-solution tasks; prospective reuse-first comparison | Retrieval recall incomplete; hidden license/security/integration costs |
| M6 | Under what workloads does reuse reduce total cost and environmental burden without reducing outcomes? | Same functional task and horizon; human + provider-model uncertainty + CI/build/runtime/maintenance; SCI-style boundaries, sensitivity and rebound | Fewer tokens/LOC != lower energy or emissions; costs shifted to upstream |
| M7 | Which evidence-backed interventions help maintainers increase organic visibility *and* useful adoption? | Registered, ethical, staggered or randomized opt-in README/onboarding/docs/release/contribution interventions, independently verified end user outcomes | Promotion confounding, regression to mean, no access to third-party traffic data |

**Negative/null findings must be published.** Evaluate subgroup heterogeneity by language, repository archetype, age, owner size, geographic/time access and task difficulty. Distinguish association from cause. Define feasible denominators and non-observed/missing values explicitly.

## Time frame and eligibility

- **2024:** historical reference for already-existing AI-assisted coding; NOT an AI-free control. A historical commit, release or events archive is not an archived GitHub Trending snapshot.
- **2025–2026:** documented agent availability and maturation. Product launches are timing anchors, not proofs that developers used them.
- **2026-10-15–31:** planned prospective capture *pilot* subject to permissions and protocol review; adjust transparently if missed.
- **2026-11-01–2027-04-30:** proposed main recruitment for ~1,000 unique observed Trending repos plus a separately sampled control cohort, **subject to pilot, ethics, power and preregistration**; follow up 30/90/180 days.
- **Task-study 2027 onward:** independently recruited and consented workflow/use/reuse measures, separately powered, including real failures and no-reuse tasks.

Do **not** drop old projects from the **reused-software candidate universe**: a ten-year-old dependency can be the most relevant thing a 2027 agent should discover. Old projects need not dominate the *modern workflow change* cohort. A separate quiet/high-reuse control is essential to avoid Trending visibility bias. Repo creation date and an AGENTS.md are not valid AI-use inclusion tests.

The sample target of 1,000 is not statistical power or representativeness; determine precision and detectability after a real pilot. Before enrollment, reconcile PROTOCOL.md, STUDY_DESIGN.md and SELECTION_PROTOCOL_2027.md into one registered, versioned main protocol. Do not quietly replace the existing star-growth estimand: report it as a visibility-focused endpoint; independent user value demands separately enrolled and powered evidence.

## Operational causal map

Workflow/tool maturity → search/implementation/review behavior → functional software and maintenance burden → packaging/discovery and contributor experience → externally verified adoption/reuse → net human + operational + environmental effects.

Important feedbacks: attention can attract contributors and alter quality; promotion affects attention before quality; popularity shapes training/retrieval exposure; successful reuse may raise or lower upstream maintainer load. Prefer longitudinal temporal ordering, pre-exposure measurement and pre-registered randomized interventions to identify causal effects. The diagram is a hypothesis, **not** demonstrated causality.

## Required deliverables of the study

1. Reproducible dataset provenance, sampling/attrition and source-verified chronology.
2. Descriptive trends in coding practices with attribution sensitivity.
3. Audited reference implementations, task-level independent reuse evidence and *failed* searches.
4. Publication-grade statistical models plus null/sensitivity analyses and uncertainty.
5. An evidence-rated, task- and archetype-specific practical playbook (see PRACTICAL_REPOSITORY_GROWTH_AND_REUSE_2027.md), with exactly what to do, cost, proof and counterexample.
6. A conservative portfolio audit of maintainer's own repositories, conducted separately from development of research hypotheses to avoid circularity.

**Related design documents:** [selection](SELECTION_PROTOCOL_2027.md), [agent measurement](AGENT_ADOPTION_MEASUREMENT.md), [reuse metrics](REUSE_SUSTAINABILITY_METRICS.md), [independent gold standard](REUSE_GOLD_STANDARD_2027.md), [study experiment](REUSE_FIRST_EXPERIMENT.md), [evidence-to-lesson protocol](EVIDENCE_TO_LESSON_PROTOCOL.md), [critical validity risks](CRITICAL_RESEARCH_GAPS_2027.md), [study design](STUDY_DESIGN.md).
