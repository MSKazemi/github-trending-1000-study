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

## 2026-10-13 bounded cost aggregation and privacy rules

New `python -m trending_study.maintainer_burden --input examples/maintainer_externality.synthetic.json` validates six separately reported **human active-minute** categories, consent state, reported UTC and accepted-task status. It now also rejects **mixed synthetic/real case aggregates**, requires frozen 40/64-hex frame commits for non-synthetic cases, and forbids retained observation timestamps in withdrawn or unconsented case records. Every report explicitly says `approved_for_public_release=false` until external ethics/consent/privacy authorization; structural validation never substitutes for that approval. It rejects minutes for unconsented/withdrawn cases, impossible times, negative/nonfinite values, duplicate cases and partially populated time records being presented as a complete total. `known_partial_minutes_not_a_total` is explicitly diagnostic; `overall_human_minutes` is null unless every case has all six categories observed. `per_accepted_task_minutes` stays null pending a real independently authenticated equal-output study, even when a synthetic card claims pass.

**Ethical study design:** independent opt-in recruitment with institutional privacy/ethics review as required; prospectively freeze eligible case/task frame, active-time definition and consent/withdrawal handling; preserve failed, abandoned, duplicate and rejected PRs in the assigned denominator. Collect task complexity, previous familiarity, support burden and 30/90-day follow-up without raw personal emails, unpublished patches, private logs or contributor rankings. Use self-identified active time without inferring human labor from commits, comment volume or an agent's token count. Observational comparisons require confounder disclosure; randomization is only feasible under voluntary, acceptable protocols.

**Methods reference:** [Runeson & Höst (2009), empirical software engineering case-study guidelines](https://doi.org/10.1007/s10664-008-9102-8) calls for explicit protocols, case selection and chain of evidence. The synthetic audit tool is not proof of consent, participant independence or a causal productivity result.

**Practical maintainer lesson:** cap parallel bot PRs, prefer one independently testable change, and include upstream reviewer/upgrade minutes in the true cost of reuse before claiming green or labor savings.


## 2026-10-13 integration safeguard: synthetic sums are not observed human burden

The aggregator now reserves `overall_human_minutes` for a **complete, wholly non-synthetic** submitted set and returns `null` whenever any synthetic scenario is mixed in. For fully synthetic complete cases it may show an illustrative `synthetic_scenario_minutes`, but this cannot be cited as a measured maintainer burden, productivity impact, external deployment or environmental saving. Any mixed or partial set keeps missingness explicit. The repository test suite includes a synthetic complete-case regression. Neither code path authenticates the reported consent, participant identity or independent acceptance of a task.
