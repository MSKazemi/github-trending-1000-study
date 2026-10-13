# Adoption, real reuse and maintenance evidence — issue #12

**As of 2026-10-12: draft codebook and deliberately fictional example.** No downloads, installations, users, dependents or 30/90/180-day outcomes have been collected. This partially advances [#12](https://github.com/MSKazemi/github-trending-1000-study/issues/12); it does **not** validate 2027 adoption claims or change the frozen study design.

## Operational measures with non-interchangeable denominators

| Signal | Unit and verifiable source | Useful for | What it cannot prove |
|---|---|---|---|
| GitHub star/fork/Trending rank | repo at observed timestamp, official GitHub metadata / saved page SHA | public attention and discovery exposure | installation, user count, functionality, open-source license |
| Package downloads | registry event/count with source/version/time and bot/cache caveats | distribution *attempts* | unique users, successful import or downstream task |
| Downstream declared dependency | exact manifest lock + project/version/commit, license and availability | an *explicit integration intention* | runtime execution, consent, sustained use or useful outcome |
| Downstream successful integration | independently reproduced import/call/task, exact version and environment | verified bounded reuse of a code component | prevalence across all potential users |
| New-user first-run task | consented participant, frozen task and independent rubric | actual initial usefulness | unobserved use by others, future retention |
| Repeated independent-use task | same consenting user, 30/90/180-day windows with attrition | follow-up value for observed eligible population | global retention from sparse convenience sample |
| Maintenance | accepted user task plus support/repair/upgrade minutes and relevant CI/runtime failures | cost per maintained accepted task | complete ecosystem burden without upstream costs |

The [synthetic structured record](../examples/adoption_signals.synthetic.json) shows **unknown and missing**, never fake zeros. Use immutable GitHub numeric repo ID where available; owner/name is mutable. A downstream manifest with an old dependency version is not proof the dependency still works.

## Minimal prospective state dictionary

Each `signal`: `observed_verified|observed_negative|unknown|not_applicable|withdrawn`. Record `observation_eligible`, `evidence_source_url`, `observed_at_utc`, `version`, `independent_reviewer` and `access_basis` (public metadata, opt-in task, declared manifest). A supplied reviewer ID is not authentication. Independent reproducible tests provide stronger evidence than scraped GitHub stars.

A denominator must be anchored to a **preselected candidate frame** and opportunity:
- `N_eligible`: units eligible for that *specific signal*, not all 1,000 repositories for all signals.
- `N_observed`: eligible units with an ethically accessible, valid source and completed inspection.
- `N_verified`: independently passing the signal's defined criterion.
- `N_unknown`: no permitted source, restricted telemetry, attrition, unavailable package, or conflicting evidence.
- `N_na`: construct genuinely cannot apply; report alongside eligibility rather than code as negative.

For a fixed finite eligible audit panel, a *logical* unweighted bound on verified-success proportion under missingness is `N_verified / N_eligible` through `(N_verified + N_unknown) / N_eligible` when the frame and labels are valid; this is **not** a population confidence interval and does not adjust for unequal detection probability, selective observability or external audits. Report selection and clustering effects; consider inverse-probability adjustment only with supportable assumptions and a registered design.

## Verification plan (not performed)

1. Freeze an archetype-stratified repo/task panel before looking at the outcome and record frame SHA, discovery channel, age, language and baseline popularity.
2. Obtain terms-compliant, opt-in or permissible public dependency information; avoid invasive telemetry and identifiable rankings.
3. Blind independent reviewers to Trending rank when auditing actual imports/functional tasks; inspect exact package version/date/license, duplicate downstream forks and archival scope.
4. Collect scheduled outcome follow-ups without inventing historical snapshots. Include disappeared, private, deleted and renamed endpoints as *distinct censored/missing states*, not zero adoption.
5. Relate visibility exposure to verified reuse only in adjusted longitudinal models with sensitivity to frame coverage, missingness, PR popularity, promotion and reverse causality. Report null/negative findings and independent task replications.

## Practical lesson for your repositories

Offer one reproducible minimal integration example and a tiny downstream smoke test rather than optimizing stars. Ask consenting external users to reproduce the same code integration under pinned versions. Measure successful first use, repairs and opt-in repeat use; do not infer real adoption from downloads or README traffic.

**Remaining acceptance:** actual data access audit, denominators, independent user cohort and repeated observations, privacy/ethics review, statistical uncertainty and prospective comparison protocol. See [usefulness](USEFULNESS_FRAMEWORK.md), [metrics](METRIC_REGISTER_2027.md), [data dictionary](DATA_DICTIONARY.md) and [mission](AI_ERA_CODING_REUSE_RESEARCH_MISSION.md).

## 2026-10-13 bounded finite-frame adoption evaluator

Run `python -m trending_study.adoption_bounds --input examples/adoption_signals.synthetic.json` for a fictional one-repository demonstration; tests: `python -m unittest tests.test_adoption_bounds -v`. The evaluator accepts one card or a `{"cards":[...]}` list from the **same frozen frame**, disallows duplicate repository IDs, requires signal-specific applicability, and rejects observed positives/negatives without a clean evidence URL, UTC timestamp and declared reviewer.

For each signal, it preserves separately `eligible`, `not_applicable`, `verified`, `negative`, `unknown` and `withdrawn`. The finite-panel logical bounds are `verified/eligible` to `(verified+unknown+withdrawn)/eligible` for a binary signal, assuming only that absent outcomes can be positive or negative. They are **not** a sampling confidence interval, missing-at-random assumption, causal comparison, software population estimate or user count. A zero eligible denominator returns null. Snapshot age, incomplete registry coverage, dependency declarations versus executed imports, right-censoring and 30/90/180-day attrition all require real-world sensitivity analyses.

**Methods references:** [Cochrane Handbook, Chapter 10, §10.12.3](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-10) cautions that worst-/best-case missing-outcome bounds can be uninformative without plausible sensitivity assumptions; [Runeson & Höst (2009)](https://doi.org/10.1007/s10664-008-9102-8) supports traceable case-level evidence. Our exact implementation is an explicitly labeled design choice, **not** a Cochrane-certified estimator.

**Practical maintainer lesson:** attach a version-pinned consumer smoke test and observe opt-in repeat success, repair/support time and attrition rather than use package downloads as a proxy for users.
