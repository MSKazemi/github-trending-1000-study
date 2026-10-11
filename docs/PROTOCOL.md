# Research protocol — v0.1 (preregistration candidate)

**Design:** Observational, longitudinal, mixed descriptive and inferential study. **Unit of analysis:** unique GitHub repository (immutable repository ID where available); repository-date for repeated measurements. **Primary population:** public repositories that appear on GitHub Trending during the explicitly recorded observation interval. This is **not** a representative sample of all GitHub repositories.

## Hypotheses (prospective; not tested)
- H1: Documentation completeness at baseline is positively associated with **future** star growth, adjusting for baseline stars, age, language and category.
- H2: Contribution affordances and release cadence are associated with subsequent distinct-contributor activity.
- H3: Estimated associations vary by programming language and initial popularity.

These are hypotheses, **not** established evidence. Freeze the analysis plan before inspecting outcomes.

## Sampling plan
1. Specify collection dates and all sampled windows *before* collection. Suggested pilot: daily, weekly and monthly Trending views over 8–12 weeks. Preserve actual page URL, UTC timestamp, query parameters, HTTP status, SHA-256 and parser version.
2. Parse every visible repository row; keep its listed position, window and language filter. Do not assume GitHub reveals the Trending ranking formula or a complete universe of trending candidates.
3. Deduplicate using GitHub repository ID when available; otherwise canonical owner/repo URL, followed by stable-ID reconciliation (renames may occur).
4. Continue until **at least 1,000 unique eligible repositories**; report the observation period, duplicate rate and every exclusion. **No cherry-picking** the most impressive repositories. If quota cannot be achieved, report actual N without silently substituting popular repositories.
5. Construct a separate control sample of public **not-observed-trending** repositories using a documented time-bounded search frame and a fixed pseudorandom seed. Match or stratify by language, age and baseline popularity. Absence from observed Trending ≠ never trending.
6. Track baseline and follow-ups at 30/90/180 days **from each baseline date**. Do not mistake today's metadata for historical metadata. Record inaccessible/deleted/private-converted repos as attrition.

## Inclusion and exclusion
Include public GitHub repositories visible in recorded Trending pages. Exclude duplicates from the unique-repository count (but keep repeated appearances); exclude deleted/private entries from prospective enrichment with reason; flag archived, forks and mirrors rather than deleting them post hoc. Track missing fields as missing, never zero.

## Measures
- **Primary outcome:** change in stars over 30 days, reported as absolute delta and as log1p(stars_30d) minus log1p(stars_0). Note: stars can decrease.
- **Secondary outcomes:** forks, unique contributors if defensibly measurable, issue/PR engagement, repeat Trending appearances, activity and retention at 90/180 days.
- **Baseline predictors:** README length and sections, setup/quickstart, LICENSE, CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md, AGENTS.md, automated tests, CI workflows, release presence, documentation link, topic count and recency metrics.
- **Confounders:** repository age, stars at baseline, language/ecosystem, organization versus individual owner, category, observation month and window, prior growth if observable.

A star is an attention proxy, not validated quality, utility or real-world adoption. Beware that some baseline measurements change rapidly after a repository trends.

## Analysis
1. Publish flow counts: discovered appearances → unique IDs → eligible → enriched → complete follow-ups. Include denominators and 95% uncertainty intervals for measured rates.
2. Describe skew with median, IQR and distributions; do not rely on means alone.
3. Fit predeclared count/continuous models as appropriate (e.g. negative binomial for nonnegative counts; robust regression of log differences) with covariates; cluster uncertainty by repository when using multiple observations.
4. For cohort comparisons, report propensity/stratification balance and sensitivity to unobserved confounding. Never claim causation.
5. Control multiple comparisons (Benjamini–Hochberg FDR) for exploratory feature screens; separate confirmatory tests from exploratory results.
6. Perform robustness checks by language, cohort, observation window, fork/archive policy, missing-data mechanism, bot effects and unusually large repositories.
7. Report effect sizes, confidence intervals, p values where applicable, model diagnostics, negative/null findings and limitations. No best-practice ranking without evidence.

## Bias and validity
Trending selection is opaque, may favor bursty repositories, languages and exposure; the study has survivorship, missingness, reverse-causality and platform-change risks. Statements about what made a repository trend require stronger designs than this study supplies. Use comparisons as associations, not randomized evidence.

## Operational reproducibility
Freeze raw snapshots and manifests (checksums, UTC, source URL, collector/parser versions), analysis plan, code commit, seeds and exact cohort membership when releasing results. Use a reviewed GitHub issue/PR to change the protocol, version the amendment, and identify deviations before interpreting results. Publish a machine-readable data dictionary and scripts. Keep individual contributors' personally identifying details out of derived public exports.

## Pilot acceptance criteria
A fixture-based parser with fail-closed behavior; verified real-page parser QA; audit of at least 30 rows across windows; ID-based dedupe; collection-completeness log; explicit baseline and longitudinal snapshots; no conclusions before full data audit.
