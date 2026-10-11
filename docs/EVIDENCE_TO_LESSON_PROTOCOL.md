# From an observed correlation to an actionable lesson

**Research objective:** publish recommendations whose provenance, applicability, cost and confidence can be audited. Do not equate a highly correlated feature with a causal growth lever.

## The evidence-to-lesson pipeline

```
Question + target outcome + target project type
  -> predeclared operational metrics and collection validity
  -> cohort comparison or randomized/pragmatic intervention
  -> estimate + uncertainty + missingness + subgroup tests
  -> alternative explanations / confounders / reverse causality
  -> independent user-outcome or replication check
  -> cost and maintenance tradeoff
  -> evidence-graded lesson card (or honest 'unknown')
  -> implementation experiment + stopping rule
  -> scheduled 30/90-day re-evaluation
```

## Evidence grades (proposed; not a certified grading standard)
- **E0 — question/unverified conjecture:** no independent observations. Publish only as hypothesis.
- **E1 — descriptive observation:** reproducible counts/distribution; no defensible comparison. Publish a description, not a recommendation.
- **E2 — adjusted observational association:** predeclared outcomes, suitable controls, uncertainty, selection limitations. Language: 'associated with', not 'causes'.
- **E3 — triangulated association:** stable across independent cohorts/time windows and review/audit, with alternative explanations tested. Publish a provisional context-bounded practice.
- **E4 — controlled intervention:** randomized/credible quasi-experiment with prespecified success and verified functionality; report effect size, limits and harms.
- **E5 — replicated impact:** independently reproduced E4 across project types/timeframes including downstream value and maintenance. Broad recommendation only within tested population.

*An RCT with invalid outcomes, unblinded biased acceptance, missing data or selection problems is not automatically better evidence than a high-quality observational study. Grade by quality and fit.*

## Lesson card required fields
`id`, `status`, `title`, `question`, `population`, `intervention_or_feature`, `comparison`, `primary_outcome`, `measurement_window`, `sample_n`, `effect_size`, `interval`, `validity_threats`, `negative_findings`, `evidence_grade`, `practical_cost`, `risks`, `applicability`, `suggested_experiment`, `stop_rule`, `sources`, `analysis_commit`, `reviewed_date`.

Statuses: `hypothesis`, `exploratory`, `validated_for_context`, `inconclusive`, `contradicted`, `superseded`. Every public card must state the scope and any uncertain fields.

## Implementation recommendation categories
- **Do now:** low-regret, safe practice with demonstrable task or adoption value in a similar project type; specify boundary.
- **Test locally:** evidence suggestive or effect size small/heterogeneous; define a small, measured trial.
- **Do not prioritize yet:** weak user need, uncertain or negative net value, substantial review/maintenance cost; not permanent condemnation.
- **Avoid in this context:** evidence of unacceptable safety/privacy risk or repeated net harm.
- **Insufficient evidence:** cannot issue a recommendation.

## Example — README length vs successful onboarding (HYPOTHETICAL, NO DATA)
Observation: popular repos have longer READMEs. This alone does not show that making a README longer improves adoption. Better hypothesis: tested installation steps + minimum runnable example increase a new user's clean-install task-success rate. Define 10-minute task and compare current vs improved documentation on fresh users under a preregistered protocol; measure attempt count, pass/fail, actual time, help requests and CI/install failures. Then, if independently replicated and benefits exceed upkeep, recommend *task-complete onboarding*, not word count or keyword stuffing.

## Example — AI-written code volume (HYPOTHETICAL, NO DATA)
Observation: a repository's AI-associated PR and commit counts increase. Alternative explanations include bots, small tasks and more fragmented commits. Better evaluation: accepted safe feature tasks completed per total human hour, review minutes, 30/90-day defects and total recurring cost. Without this comparison, classify as **activity change, not productivity gain**.

## Analyst workflow / reproducible lessons
1. Register candidate lesson ID in [claim ledger](CLAIM_LEDGER.md) as a hypothesis before testing.
2. Save a versioned `templates/experiment_registration.md` specifying target and stopping rule.
3. Generate analysis from pinned cohort, scripts and exact UTC windows.
4. Have an independent reviewer check source links, statistical interpretation, alternatives and cost.
5. Fill `templates/lesson_card.md` **only with collected evidence**; label blanks `not measured`, not `0`.
6. Review every recommendation at 90/180 days and at material platform/model changes; keep replaced versions visible.

## Negative and null results are valuable
Explicitly publish features that have uncertain, negative or context-dependent results. Avoid selective publication of only 'growth tips'. Do not recommend purchased stars, mass-posting, low-value PRs or engagement exchange; ethical organic improvements are the only eligible interventions.
