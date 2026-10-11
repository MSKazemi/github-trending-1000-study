# Green, reusable, human-centered software — central 2027 research mission

**Date:** 2026-10-11. **Status:** prospective research amendment; not preregistered, results not collected.

## Objective
**Stop unnecessary reimplementation when existing, secure, legally reusable code meets the same real user need.** Make valuable code easier to discover, validate, document, extend, cite and maintain; reduce wasted human work, tokens, electricity, compute and maintenance where empirical comparisons demonstrate a reduction. New code may still be the right answer when safe reuse is impossible or when the new solution improves verified outcomes.

**Core estimand:** among predefined tasks with at least one audited viable prior solution, compare the reuse-first workflow to conventional new-implementation workflows on (a) independently accepted user task outcomes, (b) *complete* human-active development and review hours, (c) 30/90-day maintenance cost and (d) bounded energy/carbon where measurable. Do **not** equate fewer tokens or code lines with lower greenhouse-gas emissions without physical or calibrated model data.

## Research questions (new central questions)
- **GRQ1 — Discovery:** How often does a suitable pre-existing OSS component exist for real task specifications, including low-star and non-Trending components? Are ranking and Github search good enough to find it?
- **GRQ2 — Selection quality:** Does evidence-guided reuse screening improve legal/secure/functionally correct candidate selection compared with generic prompts or unstructured search?
- **GRQ3 — Value and cost:** Does reuse-first lower complete implementation, debugging, review, onboarding and maintenance effort *while meeting the same task quality requirements*?
- **GRQ4 — AI agents:** Does Claude Code/Codex/Copilot/other agent assistance alter the reuse-discovery rate and clone/redundancy burden? Agent version must be reported; don't infer individual use from AGENTS.md.
- **GRQ5 — Environment:** What energy and carbon *differences* can be supported by measured device/CI energy and bounded provider estimates? What cannot be measured?
- **GRQ6 — Sustainability of reuse:** When do dependency, license, update, supply-chain and community-health risks make reuse worse than a small vetted implementation?
- **GRQ7 — External reuse potential:** What documentation, compatibility examples, machine-readable metadata, interfaces and licensing terms help other developers reuse the artifact? Validate by independent tasks, not README word counts.

## Do not make Github Trending the main measure of value
Trending is an **attention exposure**, not a validated quality or reuse metric. Include three complementary observational cohorts: (A) 1,000 date-stamped observed Trending repos (target); (B) roughly 1,000 independently sampled public controls not seen in our capture frame; (C) an **independent component-use/reuse cohort**, sampled from explicit language/ecosystem registry and dependency/cross-project reuse frames with adequate small/medium and older project representation. A pilot will determine a defensible size for cohort C. Keep cohort C separate from Trending inclusion to avoid selecting on popularity.

**Task-first validation:** even three repo cohorts cannot establish direct user benefit or AI/energy causation; add opt-in randomized, task-based reuse experiments described in [REUSE_FIRST_EXPERIMENT.md](REUSE_FIRST_EXPERIMENT.md).

## Theory of change, with unproven links
Better task descriptions and reproducible examples → more accurate discovery → viable component evaluation (security/license/quality) → actual integration or upstream contribution → accepted functionality with less net effort → less duplicate maintenance → possible lower energy/carbon. Every arrow is an **empirical question**, not a conclusion.

## Required boundaries
- Novel projects may have high research, educational or public-good value without immediate adoption; evaluate according to project type and its declared objective.
- Clone count is not a measure of waste by itself; legitimate interoperable clones, adapters, generated files, alternative implementations and education can be appropriate.
- Blindly importing dependencies may make security, maintenance, latency, energy or compatibility worse. **Reuse-first means investigate first, not reuse at any cost.**
- Small/medium or old repositories deserve discovery even when they have zero Trending appearances. Research on copy-based reuse found many resources originate outside famous repos [G05].
- Never redistribute code without respecting its original license or claim authorship of code written by others. Prefer linking dependencies, upstream contributions and explicit attribution where suitable.

## Success in late 2027
An openly documented **decision framework**, candidate-discovery benchmark, reproducible audit of Trending's predictive limits, agent-assisted reuse experiments and evidence-graded recommendation cards. Success is measured by *verified functional adoption and lower net lifecycle impact relative to realistic alternatives*, not paper publicity or star count. Publish null and negative results.

**Sources:** [green and reuse bibliography](../references/green_reuse_sources_2026.json), [Trending validity](TRENDING_VALIDITY_AUDIT.md), [green metrics](REUSE_SUSTAINABILITY_METRICS.md), [agent chronology](AGENT_RELEASE_ADOPTION_TIMELINE.md), [research decisions](CONVERSATION_SYNTHESIS.md).


## Critical amendments before preregistration (2026-10-11)
The primary experimental estimand must concern **all prospectively sampled assigned user tasks**, including those for which no reuse opportunity exists, so the trial does not favor reuse via task selection. Independent task-to-candidate gold judgment must evaluate source-availability dates, context-specific functional tests, rights, security, maintenance and retrieval-pool incompleteness. Environmental impact must include realistic runtime and maintenance horizons, plus water/hardware where possible; maintainers' external support load should be measured or declared unknown. See [critical gaps](CRITICAL_RESEARCH_GAPS_2027.md), [gold standard](REUSE_GOLD_STANDARD_2027.md), [lifecycle break-even](FULL_LIFECYCLE_BREAK_EVEN_2027.md) and [scientific governance](SCIENTIFIC_GOVERNANCE_2027.md). These are **draft amendments** awaiting a consolidated, frozen protocol.
