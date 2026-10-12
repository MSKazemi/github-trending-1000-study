# Figure and table plan for the GitHub Trending 1000 / green reuse research program

**Created:** 2026-10-12. **Status:** proposed visual-analysis protocol; requires scientific review and preregistration where confirmatory. **Owner:** research program. **Tracking:** [issue #33](https://github.com/MSKazemi/github-trending-1000-study/issues/33).

## Evidence status and scope

As of this document, no validated empirical sample of 1,000 unique repositories, independently judged reuse gold set, consented 2x2 human/agent trial or measured lifecycle kWh/CO2 result exists. This is a specification of *what should be displayed when appropriate data exist*, **not** a report of outcomes. Charts computed from synthetic examples must be labeled synthetic and kept out of empirical result panels.

The primary 2027 paper is about (a) *observed visibility* of prospective GitHub Trending repositories against independent comparison and quiet reusable software, and (b) *independently verified reuse/usefulness* where task-level evidence is actually obtained. A separately powered 2x2 workflow experiment can be a pilot in 2027 and a later confirmatory paper only after ethics, recruitment, preregistration, power and measurement checks. Whole-life footprint and 2028–2031 projections belong in separately bounded follow-on research if not measurable in 2027.

**Hard methodological boundaries**
- Trending rank, stars and downloads are **attention or proxy signals**, not proof of user value or independent reuse.
- A missing coding-agent trace is **unknown use**, not a confirmed human-only repository.
- Reuse opportunity requires a time-eligible, independently functionally accepted, licensed and screened component; failed retrieval does not establish nonexistence.
- Randomized workflow effects use **all prospectively enrolled and assigned tasks**, including no-opportunity, failed, refused and abandoned attempts (intention-to-treat). Do not condition primary effects on final success.
- Energy/carbon analyses use the same independently accepted functional unit, workload, period and stated system boundary. Unknown provider inference/embodied burdens remain unknown, not zero or an arbitrary token multiplier.
- 1,000 Trending repositories is a *target*, not an observed count or a representative sample of public software. Full 180-day follow-up is needed before final claims.

## Tier and timing key

- **CORE:** candidate for a *main manuscript* only when corresponding valid data exist.
- **SUPP:** supplementary/replication/diagnostic.
- **FUTURE:** later-wave confirmatory or decision support, not a claim that 2027 will produce it.
- **DESIGN:** flowchart, process diagram or source chronology that can be drawn now from the declared protocol and independently verified historical references; explicitly mark hypothetical dates or illustrative paths.

## 18-figure register

| ID / tier | Figure and recommended display | Measured quantity, unit/denominator and comparison | First feasible wave / evidence gate |
|---|---|---|---|
| **F01 CORE** | **Sampling and attrition flow** (STROBE-style flow diagram) | Captured page-surfaces and parse failures → observed occurrences → stable unique repository IDs → prespecified eligibility → cohort membership → metadata and +30/90/180d follow-ups; show reasons and raw Ns | 2026 pilot DESIGN; actual 2027 captures, ID reconciliation and data QA |
| **F02 CORE** | **Attention versus verified user benefit** (log-scale stars vs independently verified task-level reuse/outcomes; points/binned trends and stratified adjusted estimates) | Correct task-completion or verified independent integrations versus baseline stars / Trending observation; report sample frame, language, type, age, baseline maturity, adjusted effect and CI; no causal inference from correlation | 2027 contingent on *independent* useful-task/integration audits and matched frame |
| **F03 FUTURE** | **Human × agent × reuse-first randomized effects** (four arm dot/forest plot with intervals, plus factorial interaction) | A human normal, B human reuse-first, C agent normal, D agent reuse-first; accepted work per *all* human-active hours and independent success/failure and security; intention-to-treat includes all randomized tasks | Pilot potentially 2027; powered effect estimation 2028 only if preregistration/power/consent pass |
| **F04 FUTURE** | **Lifecycle energy/carbon break-even** (paired cumulative kWh/CO2 versus executions/time, uncertainty ribbons, signed difference) | Reuse vs matched new-build including search/index, development, test/CI, provider inference, upgrade, runtime, upstream costs and rebound; consistent accepted-task functional unit, calibrated/modeled/unknown boundary legend | DESIGN now (synthetic, labeled); observed 2028–2030 contingent on full or explicitly partial boundaries |
| **F05 FUTURE** | **Utility–cost–risk Pareto frontier** (scatter with non-dominated solutions, error bars and explicit invalid-risk points) | Accepted, safe tasks relative to complete human+upstream time, cash, defect and lifecycle energy; never turn security/licensing veto into a weighted popularity score | 2028+ if matched experiments/quality/security adjudication exist |
| **F06 CORE/DESIGN** | **Agent release / adoption evidence timeline** (dated events and separate survey/provider denominators) | Verified public releases (Codex, Claude Code, Copilot and others), public report/event dates and evidence type; external adoption surveys and provider figures separated by population, question, period and units | Can prepare 2026 after source/date verification; no extrapolation of provider counts to sampled repos |
| **F07 SUPP** | **First *detected* coding-agent trace over calendar time** (event-time curves by evidence tier with unknown channel) | Repository-month D/H/M/L/U trace counts or time to first detection; denominator observed at-risk eligible repos, complete months and provenance coverage, report censoring; NOT first true adoption | 2027 after time-stamped audit; report selection and detection lag |
| **F08 CORE/SUPP** | **Trending observation completeness and temporal recurrence** (date × sampled page-surface coverage heatmap + eligible-appearance recurrence distribution) | Nine *proposed* page surfaces/day subject to permission; successful/failed/blocked/uncaptured pages, page lengths and repeated occurrences vs unique IDs; do not treat weekly/monthly as independent daily observations | 2026 pilot and 2027 capture |
| **F09 CORE** | **Cohort balance** (love plot / standardized differences before and after stratification, plus clear unresolved frame imbalance) | Trending vs non-observed-Trending and separately sampled quiet-useful comparator, baseline age, language, stars, project type, owner type, month; standardized mean differences and CIs where warranted | 2027 after independently sampled comparator cohorts |
| **F10 CORE** | **Prospective visibility and survival trajectory** (small-multiple growth curves/violin distributions for +30/+90/+180d) | Signed net stars and log(1+stars) change, activity and response/retention where estimable; project baselines aligned by enrollment date; right-censored/deleted/privatized marked | Interim at each completed horizon; full cohort comparison late 2027 conditional on deadlines |
| **F11 CORE** | **Search quality with incomplete judgments** (P@5/P@K lower/upper interval with judged-coverage bar) | Functionally viable, time-eligible, license/security-passing gold candidates / judged retrieved K; unjudged top-K and unknown not counted as negatives; recall only *relative to pooled gold set* | 2027 gold-label pilot after independent dual review |
| **F12 CORE/SUPP** | **Quiet software exclusion and reusable-opportunity coverage** (age/star bins or ridge plots stratified by ecosystem/task) | Fraction of *prospectively sampled tasks* with >=1 independently validated pre-existing candidate; grouped by candidate visibility, age and repository-source. Include package registries/non-GitHub software where eligible | 2027 task gold set + independent low-star/old candidate frame |
| **F13 FUTURE** | **Discovery-method benchmark** (precision–coverage–human-search-effort tradeoff) | BM25, semantic, hybrid and provenance-aware searches: P@K, judged coverage, task-level accepted integration, time/index costs; freeze retriever versions and held-out tasks | 2029 prototype decision; earlier exploratory pilot may be published distinctly |
| **F14 CORE/SUPP** | **What developers actually choose** (all-task disposition Sankey with reconciliation counts) | Assigned tasks to no-build/reuse-as-is/compose/upstream-fix/new-build and independent accepted/fail/unknown outcome; branches are mediators, not randomized arms; retain all tasks and no-opportunity cases | 2027 task pilot, with consent and blinded acceptance |
| **F15 FUTURE** | **Whole-workflow human labor and maintainer burden** (paired distributions or stacked component plots across timelines) | Human planning, search, integration, agent prompting, review, repair, downstream maintenance and *consented upstream* support minutes per randomized task; +30/+90/+180d and concurrency | 2028/2030 with opt-in full-workflow logs and upstream permission |
| **F16 FUTURE** | **Environmental uncertainty/sensitivity** (tornado/scenario plot, measured/estimated/unknown source coverage) | Signed kWh, gCO2e and water where supported; sensitivity to cloud-inference range, grid intensity, hardware allocation, runtime workloads, maintenance, shared index amortization, rebound | 2028–2030 calibrated or scoped modeled experiment; no fixed CO2/token conversion |
| **F17 CORE/SUPP** | **Verification gate outcomes and error modes** (candidate-stage funnel with mutually exclusive first failure plus multi-label failure matrix) | Pooled retrieved candidates: judged functionality, publication time, SPDX license, package identity/OSV supply chain, reproducible install and maintenance; raw audit denominator and reviewer disagreement | 2027 judged candidate pilot with safe isolated execution |
| **F18 FUTURE** | **Robustness / external replication forest** (effect sizes and compatible CIs by study wave/site/tool) | Primary experimental ITT effects by tool/version, task class, developer familiarity, ecosystem, difficulty and 2028–2031 time-heldout cohorts; preserve negative/null effects and deviations | 2028–2031, only after comparable independent replications |

### Recommended primary-paper figure ordering
For a *2027 visibility-and-utility manuscript* the candidate core is F01, F08, F09, F10, F02, and F11/F12 (if the verified task corpus is ready); F06 may be a contextual schematic. F03–F05 are **not** to be passed off as measured main findings if the human trial / lifecycle data remain uncollected. For the later experimental paper the candidate center is F03, F05, F15, F04, F16, F18.

## 14-table register

| ID / tier | Table | Minimum columns / quantity | First feasible wave / rule |
|---|---|---|---|
| **T01 CORE** | **Research question–hypothesis–estimand mapping** | RQ, population/frame, unit, exposure/assignment, outcome, horizon, denominator, prespecified covariates, observational/experimental interpretation, verification level | DESIGN now; freeze before main outcomes |
| **T02 CORE** | **Cohort description and collection completeness** | Eligible rows and unique IDs; cohort; calendar window; language/project-type strata; baseline N; followed/missing/attrition with raw numerator/denominator | 2026/2027 |
| **T03 CORE** | **Independent cohort baseline balance** | Trending vs non-observed vs quiet-reuse sampled frame; median/IQR baseline stars/age; language/type; missing N; SMD before/after matching, propensity overlap | 2027; no post-treatment matching |
| **T04 FUTURE/CORE pilot** | **Factorial task trial effectiveness** | Four assigned workflow arms; all randomized tasks, accepted successes, failure severity, total human-active hours, accepted tasks/hour, effect and 95% CI, deviations and censoring | 2027 descriptive feasibility; 2028 powered confirmatory if legitimate |
| **T05 CORE** | **Adjusted observational estimates** | Outcome (e.g. signed star growth or independent verified utility), effect per specified contrast, 95% CI, units, N repos/tasks, cluster, covariates, window, multiplicity and model diagnostics | 2027 if valid observations |
| **T06 SUPP** | **Agent evidence and adoption-source comparability** | Agent/tool, release date, source event/date, adoption population, question/metric, denominator, attribution tier, confidence and non-comparability notes | DESIGN now after source verification; direct evidence not inferred from AGENTS.md |
| **T07 SUPP** | **Analysis data contract and coverage** | Metric key; unit; source; granularity; baseline/horizon; denominator; completeness; provenance SHA; quality/evidence tier; unavailable/not-applicable distinction | DESIGN now, populate during 2027 collection |
| **T08 CORE/SUPP** | **Independent candidate gold judgments** | Prospectively sampled task; retrieved and manually pooled candidates; first availability/version; judged/unknown; task acceptance; license/provenance/security; two-rater agreement/adjudication; conditional opportunity coverage | 2027 gold pilot; no presumed global recall |
| **T09 FUTURE/SUPP** | **Retriever evaluation** | Method/version; number of tasks, retrieved top-K, known judgments, unjudged coverage, P@K bound, pool-relative recall, time, tokens and independent integration success | 2027 exploratory / 2029 confirmatory |
| **T10 CORE/SUPP** | **Reuse decision and task outcomes** | All-task assigned frame; actual no-build/reuse/compose/upstream/new-build; pre-treatment known opportunity status; accepted/failed/unknown; human and review time, safety gate | 2027 feasibility; do not exclude unsuitable/no-opportunity tasks |
| **T11 FUTURE** | **Lifecycle accounting and boundary ledger** | Task/workload, arm, observed local/CI/provider/index/runtime/repair/upstream human inputs, kWh, SCI-style gCO2e, water if valid, uncertainty, source type, excluded/unknown scope and net signed contrast | 2028–2030, scope-qualified |
| **T12 SUPP** | **Sensitivity, robustness and negative results** | Preregistered vs exploratory model; language/type/window, censoring, missingness, undocumented AI-use sensitivity, alternative controls, effect/CI, negative or null result, limitations | 2027+ |
| **T13 SUPP** | **Bias, ethics, security and protocol deviation audit** | Risk (selection, collider, survivorship, AI trace error, leak, rights, rater, token/energy opacity); detection; severity; prevention; residual uncertainty; consent/permissions; registered amendment | DESIGN now and continuously |
| **T14 FUTURE/PROGRAM** | **2027–2031 staged roadmap and evidence gates** | Year, scientific RQ, measurable deliverable, needed permissions/sampling/power, source version, evidence needed, stop/pivot condition, observed/unknown status | DESIGN now; quarterly actual-vs-plan review |

### Recommended 2027 manuscript table ordering
T01 (methods), T02 (sample/completeness), T03 (cohort comparability), T05 (observational estimates) and T08 (candidate gold audit if enough adjudicated cases). T04 is a separate descriptive/pilot table unless a properly powered trial actually occurs. Tables T06/T07/T09/T10/T12/T13 primarily support an appendix or online methods package.

## Data-to-display contract / how figures are generated

| Source table (planned, not all implemented) | Join and provenance rule | Planned displays |
|---|---|---|
| capture_manifest + raw/trending_occurrences | immutable raw page SHA256, UTC observation and window; **occurrences not IDs** | F01, F08; T02, T07 |
| repository_id_crosswalk + baseline_snapshots + cohort_membership | immutable GitHub ID, first-sighted baseline, exact random seed/inclusion probability and independent cohort source | F01, F02, F09; T02–T03 |
| dated_repository_followups + attrition | baseline-relative +7/+30/+90/+180d window, scheduled vs actual snapshots, net changes incl negative, documented reason missing | F01, F10; T02, T05, T12 |
| agent_source_events + repo_agent_trace_audit | externally dated citations and population denominators; tier D/H/M/L/U, reviewer provenance, silence=unknown | F06–F07; T06, T12 |
| independently_sampled_tasks + frozen_task_acceptance + adjudicated_candidate_pool | task ID and baseline UTC; task pre-enrollment independent of candidate discovery; candidate exact version/first release and reviewer judgements including unknown | F02, F11–F12, F17; T08–T10 |
| randomized_assignments + attempts + acceptance_reviews + time_logs | assignment pre-outcome and consent, all task IDs, independent hidden acceptance, overlapping human/agent time reconciled | F03, F14–F15; T04, T10 |
| downstream_integrations + maintenance_events + consenting_upstream_logs | verifiable *external* use and dated upgrades/support, no star/download conversion to user counts | F02, F05, F15; T05, T10–T11 |
| resource_measurements + energy_boundary_matrix + uncertainty_assumptions | metered/modelled/unknown, device/CI/provider/index/operation, matched workloads, grid/time, hardware, scenario and calibration SHA | F04, F16; T11–T12 |
| model_fit_runs + analysis_manifest | protocol+script+data commit hashes, seed, model diagnostics, cluster unit, reported null outcomes | F02–F05, F09–F10, F18; T05, T12–T13 |

**Each figure output** should have an adjacent machine-readable manifest recording: ID, status [DESIGN/SYNTHETIC/OBSERVED/MODELED/UNKNOWN], data-release hash, creation timestamp UTC, executable analysis script and git commit, filters and raw denominator, method/estimator, uncertainty method, model version where needed, exact source provenance, software dependencies, exclusions/missingness, reproducibility seed and peer-review decision. If these fields cannot be populated, do not style the plot as an empirical result.

**Recommended rendering defaults:** accessible colorblind-safe colors plus line styles; points/uncertainty over 3D bars and pies; labeled axes with units, raw Ns, time basis and 95% CIs when estimable; log axes explicitly stated; don't connect unmatched or differently sampled time series. Export editable SVG/PDF for publication and PNG for web at documented dimensions; charts plus alt text and independent caption. Avoid false precision and truncated bar axes. Unknown ≠ zero.

## Primary estimands and cross-checks for charts

1. **Observed visibility associations:** primary protocol's +30d signed difference in log(1+stars) within prospectively observed Trending cohort, adjusted for pre-specified baseline covariates and contrasted with independent controls *only with valid sampling support*. Repository-clustered or otherwise appropriate uncertainty; no "Trending caused growth" inference. Clearly distinguish relative star growth from verified usefulness.
2. **Verified reuse coverage:** independently verified, pre-existing, rights/safety compatible component present for task divided by **all prospectively sampled tasks**, with unresolved judged opportunities shown as uncertainty bounds where justified.
3. **Retrieval quality:** numerator is independently judged viable exact versions within the top K; denominator and unjudged fraction printed explicitly. P@K lower/upper bounds when unjudged, pooled-relative recall clearly described; do not assert universal recall.
4. **Randomized intervention:** report contrasts between all assigned 2x2 arms (including unsuccessful/no-opportunity tasks). Candidate primary accepted tasks / total human-active hours **across all attempts** and separate accepted proportion / all assigned tasks, plus harm/quality gates. For 0 accepted tasks define tasks/hour=0 only if recorded denominator positive and no missing success status; tokens per accepted task remain undefined (not zero) at zero accepted.
5. **Whole-life impact:** signed difference build minus reuse across matched workload and horizons, including discovery/index, model inference, CI, deployment/runtime and repairs, with plausible maintenance, upstream externality and rebound scenarios. Treat partially observed physical energy separately from modeled data-center energy. Never assign missing cloud energy a zero value.

## Delivery plan and dependencies

**P0: now, before empirical figures** — Freeze T01/T06/T07/T13/T14 as schema/decision aids, draw F01 and F06 as explicitly methodological/historical schematics; build validators for statuses and denominator/missingness fields. Finalize 2026 pilot access, sources, independent sampling, acceptance tests, permission/consent and prospective metric contract through #2, #3, #13, #21, #25, #27. No public 1,000-repo empirical charts yet.

**P1: 2026-10 pilot / 2027 observational wave** — Build real F01/F08, T02, F09/T03 after control sampling, then prospective F10/T05 as horizons mature. Start independently validated F11/F12/F17/T08 only if gold labeling and held-out task protocols pass. Use honest observed Ns.

**P2: 2027 feasibility and 2028 controlled study** — Once independently reviewed/preregistered and powered, render F03/F14/F15/T04/T10, including failure and upstream burden. Select retrieval-method reporting F13/T09 only with frozen held-out tasks.

**P3: 2028–2031 replication and sustainability** — Resource boundary audit and calibrated task repetitions before F04/F16/T11 and any environmental claim; independent replication and tool/version drift before F18; T14 reviewed quarterly. If provider/carbon scopes remain unknown, present a partial-scope sensitivity analysis and explicitly withhold a total-CO2 claim.

## Likely 2027 outputs and manuscript architecture

- **Paper A:** Is GitHub Trending a useful signal for reproducibly verified reusable software? Sampling and cohort framing (F01, F08, F09; T01–T03), prospective associations (F02, F10; T05), verified reuse task gold set (F11–F12, F17; T08). If independent user evidence is too sparse, publish a *methods/construct validation* result rather than assert utility.
- **Paper B (only after trial prerequisites):** Reuse-first versus conventional agent/human software development (F03, F14–F15; T04, T10, T12); possibly delay to 2028.
- **Paper C (only after actual measurement):** Whole-lifecycle resource and maintainer effects of reuse (F04–F05, F16; T11–T13), likely later wave.
- **Dashboard:** Separate coverage/provenance, observed statistics, experimental results and scenario visualizations; never mix them visually without status labels.

## References to canonical design

[Sampling](SELECTION_PROTOCOL_2027.md) · [Protocol](PROTOCOL.md) · [Data dictionary](DATA_DICTIONARY.md) · [Metric register](METRIC_REGISTER_2027.md) · [Agent evidence](AGENT_ADOPTION_MEASUREMENT.md) · [Gold set](REUSE_GOLD_STANDARD_2027.md) · [Task experiment](REUSE_FIRST_EXPERIMENT.md) · [Green metrics](REUSE_SUSTAINABILITY_METRICS.md) · [Lifecycle](FULL_LIFECYCLE_BREAK_EVEN_2027.md) · [Five-year roadmap](FIVE_YEAR_ROADMAP_2027_2031.md) · [Scientific ethics](SCIENTIFIC_GOVERNANCE_2027.md).
