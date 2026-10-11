# Longitudinal research design — draft v1.0 (2026-10-11)

**Status:** prospective design, **not** preregistered or tested. Supersedes the lighter outline in [PROTOCOL.md](PROTOCOL.md) where explicitly more precise. Before recruiting the confirmatory cohort, reconcile into a frozen preregistered v1.0 protocol.

## Scientific contribution
A multi-dimensional prospective analysis of repositories *observed* on GitHub Trending, with independent controls, prospective engagement outcomes, metadata provenance and explicit analysis of Trending as an **opaque selection/ranking mechanism**. The study must distinguish visibility, sustained attention, community participation, project engineering and sustainability; no unvalidated 'success' score.

## Units, estimands and cohorts
- Repository is the primary unit, joined by immutable numeric GitHub repository ID. An individual Trending appearance is an **event**, indexed by date, window, language and observed rank.
- **Trending cohort:** 1,000 eligible unique public repos first observed in an explicitly planned 12-week collection period, using daily, weekly, monthly global and chosen language pages. Full census of each selected capture, not cherry-picked ranks. A target, not a guaranteed N.
- **Control cohort:** 1,000 public repositories sampled from an independent GitHub search/metadata frame, fixed random seed; match or stratify by baseline stars (log bins), repository age, language, type and collection week. Identify and flag observed controls that later trend. Controls are *not observed trending in study captures*, not 'never trending'. Publish the frame and coverage limits. No random sample of 'all GitHub' can be assumed from REST search ranking.
- **Main estimand:** conditional association between baseline feature X and star-count change in next 30 days, for observed Trending repositories, adjusted for prespecified baseline covariates. Report marginal predicted contrasts with intervals and without causal language.
- **Secondary estimands:** community engagement, 90/180-day attention persistence, and conditional Trending vs control differences. Estimate separately, not with a single composite.
- **Timing:** 2-week pilot, up to 12-week main recruitment, baseline at first observation (same day where possible), follow-up days +7,+14,+30,+60,+90,+180 per repository. Always store scheduled AND measured timestamp, time drift and censoring reason. Asynchronous enrollment makes the study duration >180 days.
- **Snapshot rule:** a feature measured after exposure to Trending may be a consequence of trending; preserve its collection lag and do sensitivity analyses restricted to features measurable *before* first appearance. Historical reconstruction using Git commit trees is imperfect (force pushes, moved docs, API event gaps).
- **Power:** after pilot, simulate minimum detectable effect and interval width using observed skew, clustering, imbalance and attrition; 1,000+1,000 is a feasibility target, not a guarantee of statistical power.

## Specific research questions
RQ1 Visibility: prevalence, temporal variation, language exposure, and repeat appearance rates on Trending.
RQ2 Sustained attention: association of baseline features with 30/90/180-day **net** star change, growth decay and continued appearance.
RQ3 Contributors: external first-time contributor entry, first human review latency, unique returners (where permitted), activity continuity and concentration.
RQ4 Engineering: installability/documentation task success in a stratified manual audit; CI presence vs completed checks; releases and security practices as descriptive signals.
RQ5 GitHub algorithm audit: predict observed inclusion and rank *from only observable contemporaneous metadata*, evaluate temporal stability, perform feature ablations, language audits and calibration. Predictive success does NOT recover GitHub's hidden causal ranking formula.
RQ6 Qualitative: explain surprising high-growth/low-engagement and low-growth/high-engagement cases with coded interviews or public artifact reviews, triangulating rather than inventing causes.

## Feature collection codebook (baseline)
Document filename presence AND verified functionality: README examples, quickstart, prerequisites, installation, runnable minimal example, troubleshooting, architecture, contributing steps, issue templates, licensing, code of conduct, SECURITY, AGENTS instructions, tests and workflows. Use repository type taxonomy first (library/tool/application/dataset/awesome-list/template/docs/model/research artifact/other); many technical metrics do not apply to all types. Distinguish **not applicable** from false and missing.

Additional features: primary language, dominant domains/topics (human-audited multilingual taxonomy), repo age, owner type, old stars, description length, topics, issue/PR counts by **creation window**, releases, last-push staleness, external promotion indicators only if independently available and ethically collectable. Never equate agent instructions with actual AI agent usage.

## Repeated measures and primary outcomes
- S0: stars measured as close as possible to t0 UTC; S30 at actual approx t0+30 days.
- Absolute net star gain: S30-S0 (can be negative).
- Signed log growth: log(1+S30) - log(1+S0) (not a percentage and not a true per-day velocity).
- Add normalized reporting per elapsed day: (S30-S0)/actual_elapsed_days, clearly labeled **net** stars/day; note skew and publicity bursts.
- Longer term: changes at 90/180 and retention of an elevated growth rate vs baseline, only when true pre-event baseline available.
- Human first response: first substantive non-bot response by a contributor other than submitter; report median and right-censored probability of first response by day 7, not median only among answered issues.
- New external contributor: first observed qualifying PR authored by a non-maintainer (not an exact measure of person's first OSS contribution); distinct actor identity handled carefully under privacy rules.
- Testability: audited task success in a fixed environment, task-specific, with rubric, time budget, adjudication and exception codes.
- Forks, commits and release frequency are **secondary**, with bot/automation and project-type sensitivity checks.
- Traffic views, clones, referrers are NOT available for arbitrary public repos without elevated access. Never impute them as zero.

## Metrics and estimators
| Dimension | Definition | Measurement | Interpretation hazard | Mitigation |
| --- | --- | --- | --- | --- |
| Trending exposure | observed appearances per repository/window | frozen capture logs | opaque list selection; collection interval misses appearances | capture completeness ledger and sensitivity by capture cadence |
| Rank | 1-based position on captured page | per-capture HTML | unknown score; query-language-specific ranks incomparable | within-page analysis, percentile with list length, do not interpret as quality |
| Stars | current aggregate count | official REST snapshot | accumulated age/bots/bookmarks | baseline adjustment, cohort contrasts, suspicious-burst sensitivity |
| Future growth | S(t+30)-S(t) | prospective snapshots | negative deltas, elapsed-time drift | report both count and log change, actual elapsed time |
| Stars gained displayed | GitHub page's period label | separate parsed field with timestamp | site label and window boundaries may differ from independent snapshots | preserve raw string, don't equate automatically |
| Contributors | unique accepted external humans per window | PR/commit audit | aliases, bots, migrated history, internal-only activity | actor resolution, bot exclusions, multiple definitions |
| PR merge rate | merged PRs / eligible closed PRs in time-defined cohort | official PR merged_at | denominator selection, missing external merges | outcome cohorts with right censoring and validation |
| Responsiveness | time from issue/PR creation to first human reply | event timestamps | unanswered excluded => survivorship bias | survival analysis with censored open cases |
| Activity | substantive changes and contributors/month | commits/PRs | bots, squash/rebase, monorepos | actor filters and work-type strata |
| Docs quality | task checklist completion, audit success | blind dual reviewer rubric | README length conflation, language/size | inter-rater agreement, preregistered rubric |
| CI/test | tests present + most recent completed checks | workflow/check APIs | badge may be decorative; private external CI | separate unknown, present, passing, failing |
| Maintenance | time since last substantive change | timestamp with repo type | stable mature repo need not commit often | type-aware interpretation |
| Sustainability | concentration/retention of contributors | 90/180d cohort | small teams, bots, identity ambiguity | threshold strata and sensitivity |
| Adoption | independently corroborated reuse/dependency proxy | package registry where eligible | not comparable across ecosystems | optional ecosystem-specific analyses only |

## Methods and algorithms
1. **Capture QA:** keep source URL, UTC capture time, status, body SHA-256, parse count, capture errors, window, filters, parser version. Dual-human review random 30+ entries across distinct filters; estimate precision/recall against hand-annotated captured pages and bootstrap CIs.
2. **Cohort accounting:** stable ID reconciliation, reappearances, archive/private/delete status, exclusion ledger and STROBE-style flow diagram. No silent replacements for attrition.
3. **Feature reliability:** stratified manually coded subset of 100-150 repos across repo types; two blinded raters; report Cohen's kappa for categorical items and weighted agreement where relevant; resolve disagreements with documented rubric.
4. **Primary association:** preregistered covariate-adjusted robust model of signed log star change. As robustness, model future count with baseline star level offset/covariate as substantively appropriate; assess zeros, overdispersion, outliers and negative changes instead of forcing a count model for signed deltas. Use clustered uncertainty for repeated data.
5. **Confounding:** directed acyclic graph (DAG) to classify confounders/mediators; adjust for age, baseline popularity, language, project type, owner type and calendar week. Don't adjust for features created after Trending exposure as if they were pretreatment.
6. **Non-trending controls:** exact/coarsened-exact matching or propensity weighting with overlap checks and standardized mean differences (<0.1 as diagnostic target, not guarantee). Separate descriptive ATT-like estimates from causal claims; report sensitivity to hidden confounding.
7. **Time-to-response/sustainability:** Kaplan-Meier and Cox or flexible survival models with right censoring, inspect proportional hazards assumptions, competing events when material.
8. **Predictive audit:** chronological train/validation/test splits only, grouped by repo ID; baseline logistic/ordinal rank models and tree-based candidate models; hyperparameters tuned inside earlier periods. Evaluate PR-AUC for rare inclusion where denominator exists, ROC-AUC, Brier/calibration curves and NDCG@K/Kendall tau for rank within same capture. Compare against random, baseline stars and stars-gained naive proxies. SHAP/feature importance are descriptive, not causal.
9. **Multiple testing:** predeclare one main outcome and limited focal hypotheses; Benjamini-Hochberg FDR for exploratory tests; report effect sizes, 95% CIs, unadjusted and corrected inference transparently.
10. **Bias robustness:** re-estimate after removing largest 1% by stars, high-burst suspects, mirrors/forks, automation-heavy, AI category, and by language, list window, and repository type; use multiple imputation only under defensible assumptions, compare complete-case and worst-case missingness bounds.
11. **Out-of-sample validation:** freeze final 20% of chronological enrollment weeks as holdout, and separately check stability in new observation months; bootstrap by repository not observation row.
12. **Qualitative triangulation:** purposive maximum-variation case selection based on *predefined* axes; blinded dual coding, disagreement adjudication and a transparent case-to-theme audit trail.

## Interpretability and failure safeguards
- Association != causation; popularity != quality; repository != software product; Trending rank != user traffic.
- Selection on Trending may open **collider bias**: within-trending correlations between feature X and star velocity can reverse associations in the wider public-repo population. Re-estimate in controls and discuss external validity.
- Treat software repos and curated 'awesome' lists separately; forks/docs/templates need meaningful not-applicable categories.
- The GitHub search API is relevance-ranked and capped; it is NOT a uniform probability sampler. Build a fixed, segmented sampling frame and document coverage, duplication and residual bias.
- 'First seen trending' != first ever trending. 'No trending observation' != never trending.
- Bots, bought stars, and social promotion are not directly observable with high certainty. Flag anomalous patterns, don't accuse named maintainers.
- **Any dashboard ranking is descriptive**, and should not claim 'best-performing practice' without independent confirmatory evidence.

## Addendum 2026-10-11 — usefulness and 2027 AI development
We extend the **research questions** but do not modify the already described observational estimands post hoc. A distinct, prospectively designed, opt-in human/task-level substudy is necessary to evaluate AI-related net productivity, accepted correctness, external user value and total lifecycle economics. See [AI_CODING_STUDY_2027.md](AI_CODING_STUDY_2027.md), [USEFULNESS_FRAMEWORK.md](USEFULNESS_FRAMEWORK.md), [TOKEN_TIME_ECONOMICS.md](TOKEN_TIME_ECONOMICS.md), [EVIDENCE_TO_LESSON_PROTOCOL.md](EVIDENCE_TO_LESSON_PROTOCOL.md), [REFERENCES_AI_2027.md](REFERENCES_AI_2027.md) and [CLAIM_LEDGER.md](CLAIM_LEDGER.md). No 2027 findings or actual task-level data are claimed. Register and freeze amendments before outcomes become available.


## Design amendment and timeline conflict tracking (2026-10-11)
The older **12-week recruitment target** was a provisional feasibility assumption, **not an outcome-derived optimum**. The newer [SELECTION_PROTOCOL_2027.md](SELECTION_PROTOCOL_2027.md) proposes six calendar months of recruitment **2026-11-01–2027-04-30**, plus baseline+7/30/90/180 days; final followups occur around late October 2027. Both time plans remain **unfrozen drafts** pending collector capacity and pilot power, and this conflict must be resolved in the preregistered primary protocol. Other independent reuse/task-value cohorts are described in [GREEN_REUSE_MISSION_2027.md](GREEN_REUSE_MISSION_2027.md).


## Five-year perspective — supplementary waves, not retrospective changes to 2027 outcomes
This paper-focused prospective study remains a candidate **2027 Year 1** cohort. A five-year follow-on [roadmap](FIVE_YEAR_ROADMAP_2027_2031.md) and [advisory/governance model](ADVISORY_BOARD_STRATEGY_2027_2031.md) should not be construed as extra confirmatory endpoints in the original cohort. Any new five-year research hypothesis, repeated 2028–2031 challenge tasks, ecological measurement, partner field study or recommendation index requires a **separate versioned protocol/registration**. No human/energy results or formal collaborators are currently established.
