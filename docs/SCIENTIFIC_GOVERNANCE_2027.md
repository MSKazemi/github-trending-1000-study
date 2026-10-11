# Study governance: avoid invalid conclusions and benchmark gaming

**Status: protocol proposal only. No study registration, ethics approval or real trials have been completed.**

## Three evidence sources, three distinct inferences
1. GitHub Trending, independently selected public controls, and independent OSS reuse cohorts: describe visibility and conditional associations, *not* actual project utility or randomized treatment.
2. Independent task-to-component gold set: measures candidate discovery, judged coverage and technical/legal feasibility. Pooled-retrieval judgments are incomplete; absolute recall is generally unidentifiable.
3. Opt-in developer/task experiment: measures independently accepted functionality per total effort when assignment, tests, consent and risk controls are validated.

Do not merge their observations into a single "success" metric.

## Primary estimand correction
Across **all preregistered sampled tasks**, compare reuse-first versus ordinary assigned workflow on independently accepted correct tasks per total human-active hours, including failures, refusals and no-viable-component cases. A viable-reuse-opportunity subgroup is secondary, defined by independent auditors *prior* to observing assigned outcomes; selecting only reusable tasks as the primary denominator favors one treatment arm and invalidates generalization.

## Standards of evidence and inference
- Pilot feasibility, rater disagreement, effect-size/missingness distributions, and power *before* specifying confirmatory N and minimum worthwhile effect.
- Freeze task specification, baseline, acceptance suite, environmental boundaries, analysis, model/version, and selected tasks before results.
- Block assignment by task/developer/project where possible. Assess carryover, learning, interference through shared upstream maintainers, and temporal effects.
- Use intent-to-treat as primary analysis; per-protocol sensitivity separate. Treat no-completion and security violations as explicit outcomes.
- Avoid outcome leakage: hidden tests, blind independent adjudication, temporal held-out tasks, solution-availability cutoffs, and no cherry-picked accepted PRs.
- Report all missing, unknown, abandoned and not-applicable values independently of zero.
- Use 95% uncertainty intervals where meaningful, clustered by task/developer/project; account for multiplicity and report practical impact, not p-value alone.
- For observational source-trace adoption, date of first public trace might follow actual adoption; no trace is NOT a human-only category.
- Count both total lifecycle impact and intensity per independently accepted task; unclear cloud energy means partial-boundary only.

## Governance and privacy
- No confidential prompts, participant identity logs, private code or real secrets in a public data release.
- Confirm lawful data reuse and publication rights for third-party source/candidate artifacts; public source does not permit arbitrary copying.
- Never run untrusted candidates inside a credentialed CI runner or uncontrolled workstation. Isolate, restrict resources, and require human review.
- Maintain versioned amendments to all study plans, not retroactive edits to preregistration after seeing outcomes.
- Preregister revised pilot/enrollment dates before collecting confirmatory data; if October 2026 prerequisites are unmet, amend dates openly.
- Register null, negative and contradictory outcomes and issue scientific corrigenda when code/data is discovered to be wrong.

## Research outputs by end of 2027 (targets, not promises)
An audited and reusable gold set, a description of what GitHub Trending predicts and cannot measure, an externally validated reuse-vs-build task experiment, separate carbon/water bounds, upstream maintainer burden estimates where consent allows, and evidence-graded lessons that future developers can use.

See [gap register](CRITICAL_RESEARCH_GAPS_2027.md), [gold labels](REUSE_GOLD_STANDARD_2027.md), [supply-chain policy](SUPPLY_CHAIN_PROVENANCE_2027.md), and [break-even analysis](FULL_LIFECYCLE_BREAK_EVEN_2027.md).
