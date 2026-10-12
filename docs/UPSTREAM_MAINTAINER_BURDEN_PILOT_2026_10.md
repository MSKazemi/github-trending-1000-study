# Upstream maintainer and newcomer cost study — bounded issue #24 contribution

**2026-10-12. Status:** prospective privacy-preserving instrumentation proposal and synthetic record. **No maintainers contacted; no opt-in, consent, time tracking or actual cost findings.** This partly advances [#24](https://github.com/MSKazemi/github-trending-1000-study/issues/24) and does not authorize interventions on unrelated repositories.

## Research questions and independent outcomes

The study's sustainability goal is to reduce **combined** human/compute and community work for the same independently accepted feature or fix, not merely downstream generated-code time. An agent can submit a fast patch that upstream maintainers spend hours screening. Record unsuccessful patches, duplicate reports, back-and-forth, supply-chain incidents and downstream upgrade work.

| Outcome | Unit / prospective denominator | Valid measurement | Important confound |
|---|---|---|---|
| Reviewer active minutes | opt-in maintainer × incoming actionable case (include rejected/withdrawn submissions) | minute diary, reviewer confirmation and timestamped metadata without private content | case complexity, triage delegation, automation |
| Upstream support minutes | opt-in maintainer × reused component × 30/90-day horizon | nonoverlapping human time spent answering, debugging, reverting or deprecating | large downstream installation base, seasonality |
| Actionability | all *consented/eligible* submitted cases, including invalid and duplicates | rubric assessing minimal reproducer, correct fix, test, scope, license | selectively shared PRs, reviewer expectation |
| Newcomer comprehension | user × independently frozen task | independently timed locate/explain/fix test, quality adjudication | expertise, familiarity, prior agent exposure |
| Downstream saved effort | independently accepted task × assignment arm | own active minutes, repairs, follow-up, CI and tool cost | tool/model drift, task difficulty, uncounted attempts |
| Net social effort | matched accepted task at full chosen observation boundary | downstream + attributable upstream minutes (with double-count audit) | unobservable upstream burden and future rebound |

## Recruitment and safety requirements

1. Request **explicit voluntary opt-in** from maintainers before collecting personal work diaries or intervening. Institutional ethics/privacy review and acceptable retention/withdrawal provisions are preconditions, not checkboxes achievable by an agent.
2. No unsolicited automated PRs, AI-generated issue floods, contributor profiling or ranking 'bad maintainers.' Do not use private messages, raw prompts, emails, security disclosures or support tickets without access permission.
3. Frame eligible work independently of agent or reuse success; timestamp and freeze sample, task definitions, baseline skill/complexity, arm and provider/model version.
4. Where an ethical intervention is possible, compare normal vs reuse-first paths on **the same functional tasks** with independent quality/risk screening. Otherwise use observational designs with explicit confounding and report only associations.
5. Keep `unknown` distinct from `not_applicable`, `not_consented`, `withdrawn` and `observed_zero`. Zero minutes needs a completed time diary, not absence of a comment.
6. Report all assigned work, including abandoned attempts and failed PRs, stratified by project type, maintenance load, first-time contributors and severity. Follow up 30 and 90 days from actual completion (not imagined publication dates).
7. Aggregate publication and cell suppression should be approved during privacy review; do not commit person-identifiable time entries or sensitive project names into the public repo.

## Instrument representation

Use [the synthetic JSON card](../examples/maintainer_externality.synthetic.json) to understand field separation. Source metadata should link to a *consented* and approved project snapshot only when available. The example contains neither a real participant nor measured costs.

`human_time_minutes` separates `upstream_review`, `upstream_support`, `downstream_search`, `downstream_implementation`, `downstream_review_repair`, `downstream_followup`; do not add overlapping wall-clock agent time to human active time. Unknown components remain null. An agent's PR count, star growth and comments are not a proxy for human labor or actual downstream savings.

## Pilot feasibility and rejection rules

- **Gate A:** formal local consent/ethics and privacy scheme; without it, data gathering is **no-go**.
- **Gate B:** independently accepted user task and frozen experimental frame; absent acceptance, mark cost-per-success unknown, not a win.
- **Gate C:** compare upstream/downstream person-hours over a stated horizon including rejected tasks; unknown cost parts prohibit claiming *net* societal effort reduction.
- **Gate D:** reviewer checks for manipulations, spam, license/security breaches and burnout; pause if any arises.
- **Gate E:** report effect estimates with uncertainty only after enough real observations and a justified analysis; a one-off anecdote is exploratory.

**Practical maintainer lesson for 2027:** before enabling many agents to open PRs, cap scope, require reproducible failing tests and a self-reviewed candidate patch. Count the recipient maintainers' time as a real cost. Prefer small upstream fixes with tested user value over bulk low-quality contribution volume.

**Related existing instruments:** [task cost ledger](TASK_COST_LEDGER_2026-10-12.md), [upstream externalities](MAINTAINER_EXTERNALITIES_2027.md), [reuse and green metrics](REUSE_SUSTAINABILITY_METRICS.md). Reuse those tools rather than creating an overlapping time logger.
