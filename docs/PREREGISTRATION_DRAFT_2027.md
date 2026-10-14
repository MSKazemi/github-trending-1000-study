# Draft v0.3 — 2027 prospective OSS visibility and reuse-first study

**Authored 2026-10-12. STATUS: UNFROZEN, NOT PREREGISTERED OR APPROVED.** This document is a proposed consolidated preregistration *draft* only. It does **not** replace an externally time-stamped preregistration, statistical-review signoff, ethics approval or collection access permission. Any dated changes after data observation must be reported transparently as amendments. Distinguish **Study A** and **Study B**; they do not share an interchangeable causal estimand.

## Rationale and knowledge gap

GitHub Trending exposes attention, not independent software quality. Coding agents (Claude Code, Codex, Copilot coding agent and others) change software-generation workflows and source discovery, but tool launch dates do not prove actual repo-level use. Existing or low-star projects may already satisfy the same problem, potentially saving human work, but blind dependency reuse can create security and maintenance debt. Actual carbon benefit requires equivalent task outcomes and correctly bounded energy/embodied measures.

**Principal 2027 question:** when does a structured, evidence-based *reuse-first* development workflow improve independently verified useful outcomes per complete human time relative to ordinary development, without violating functionality, provenance, privacy, security and licensing guardrails?

### Study A — public ecosystem visibility (observational)

- **Sampling frame:** all rows on documented permitted, saved, dated GitHub Trending pages, not an inferred global ranking. Six language pages are **currently unsupported by strict capture**; implement and audit them before including that panel. Keep a separate independently sourced public comparison frame, and a third *component-reuse* frame (including old/quiet/low-star packages beyond GitHub).
- **Recruitment pilot:** tentatively 2026-10-15–2026-10-31, excluded from confirmatory endpoint estimates. **Enrollment proposed 2026-11-01–2027-04-30**, conditional on preflight, true unique-repository yield and power. If not feasible, amend the prospective dates before commencing.
- **Target N:** 1,000 unique observed Trending repo IDs and ~1,000 independently sampled comparison repo IDs are **feasibility targets**, not current samples or guarantees. Stratify and deduplicate by immutable numeric repo ID; retain every source occurrence and unresolved entry.
- **Exposure:** verified membership on one captured filter/date. A missed capture means unknown exposure; lack of appearance does not mean 'never trended.'
- **Primary descriptive outcome proposed:** 30-day signed log1p star growth, with absolute star deltas, baseline and +7/30/90/180-day snapshots, exact timestamps and missingness. Attention outcome **not** a proxy for real user value.
- **Comparator:** independent non-observed-trending candidate frame with documented coverage. GitHub search ranking is not random sampling; matching uses **pre-exposure** language, repo age, type, size, owner, prior activity and calendar time. Test overlap, balance, selection/collider bias and differential history coverage.
- **Agent observational marker:** high-confidence recorded agent actions vs uncertain/undetected markers, not AGENTS.md or code style. No observed trace ≠ verified human-only.
- **Analyses:** cohort flow, rates by original stratum, median/IQR, 95% intervals, signed change models with predeclared covariates and diagnostics; chronological holdout, attrition/selection sensitivity, BH-FDR for exploratory feature screens. Observational coefficients are association, **not causal** effects of Trending or agent use.
- **Data rights:** GitHub capture permitted-source policy, minimal public data, respectful access, no private traffic/sensitive contributor profiling. No retroactive reconstruction of historical Trending positions from GH Archive events.

### Study B — coding strategy and code reuse (prospective task experiment)

- **Sampling unit:** real bounded task with fixed required outcome, sampled independently from a documented user/task frame. Include tasks with no known existing reusable component, abandoned attempts, failed tasks and negative results. Tasks must be chosen **before inspecting which search method succeeds**.
- **Allocation:** optionally randomized and blocked 2×2 comparison (ordinary manual, manual reuse-first, agent-assisted ordinary, agent-assisted reuse-first), with opt-in consented developers and independent evaluator. Main **reuse-first vs ordinary agent** contrast is D vs C under assignment, not self-selected tools. If randomization is not feasible, call the result *observational*, not causal.
- **Main estimand proposal:** ITT contrast in **ratio of total independently accepted task outcomes to total nonoverlapping human-active hours** per arm, evaluated over **all assigned attempts** including zero-acceptance and abandoned tasks, plus separate accepted task success probability and human-time distribution. Compare differences/ratios with participant/project/task-clustered uncertainty; do not discard failures or divide by selected successful tasks only. This ratio-of-sums is distinct from the average of individual task success/time ratios. Final primary and quality co-primary plan must be frozen with statistician approval after pilot.
- **Requirements:** acceptance tests and negative/security tests frozen before assignment, potentially hidden from model-visible tasks; accepted functionality independently adjudicated. A model does not author its own gold test suite. Preserve source/versions and data-contamination risk. Exact agent tool/model version and allowed retrieval environment recorded.
- **Reuse opportunity:** independent task–candidate gold judging **prior to assigned outcomes**, with two blinded assessors, multi-source candidate pool and unresolved judgment labels. Pre-existing component must have existed at baseline and pass task/compatibility/license/security/maintenance gates. A secondary reuse-eligible subgroup may be prespecified; it is **not** the primary study population.
- **Human effort:** planning, search/prompt, debugging, code review, integration, clean-install verification, shipping, support and 30/90-day repair; account for overlap and multitask agent concurrency. Capture input/output/cached tokens and actual billable provider costs where accessible; unknown provider energy is not zero.
- **Safety:** high-risk package provenance or license failures stop the action, not traded against minutes saved. Test untrusted candidate functionality only in isolated secret-free authorized environments. Record upstream maintainer burden if consented, not as an automatically free externality.
- **Main outcome family:** agreed independent tasks and full human effort; secondary correctness/security, maintainer hours, cost per accepted task, verified follow-up, resource footprint, educational/public-good outcome for specialist project types.
- **Environmental outcomes:** report only with functional-equivalent scenarios, defined system boundaries including development/CI/inference/runtime/maintenance and declared observational H and n, using ISO SCI principles. If provider AI inference energy or embodied/water values are unavailable, publish only **partial-boundary measured/modeled** estimates, not 'total CO2 saved.'
- **Analysis:** randomized assignment ITT primary; log task-level outcomes and crossed developer/task effects; cluster bootstrap or properly justified model for rate contrasts, fixed exposure windows, power and missingness sensitivity, treatment × ecosystem/task/version interactions exploratory unless powered. Failure/abandonment explicitly retained. Declare alpha, minimum meaningful difference, equivalence/no-harm guardrail and multiplicity **after** pilot and **before** outcomes; do not pick thresholds by observed confirmatory results.

## Preregistration, integrity and stop rules

**Gates not yet complete (no assumed signoff):**
1. Approved data access/collection frequency and complete source capture plan (the strict parser currently covers unfiltered daily/weekly/monthly only).
2. Actual pilot capture page audit (>=30 human-reviewed rows), misses and immutable ID coverage.
3. Task recruitment frame and independent acceptance tests, time-stamped and separated from search/retrieval system outputs.
4. Review of security/license acceptance rubric and authorized human privacy/consent.
5. Pilot-based sample size/power, meaningful effect and handling of multiple comparisons.
6. Independent scientific/statistical reviewer, named consented role and explicit dated approval.
7. Immutable public protocol commit + appropriate external preregistration record when applicable.

**Proposed stop/pivot:** suspend confirmatory enrollment on poor parser validity, source access violations, inadequate power, biased task frame, unsafe candidate evaluation or lack of consent. A scientifically honest null or feasibility finding is preferable to an unsupported causal claim.

**Current source evidence and literature:** [Agent timeline](AGENT_RELEASE_ADOPTION_TIMELINE.md), [Selection](SELECTION_PROTOCOL_2027.md), [Existing design](STUDY_DESIGN.md), [Gold standard](REUSE_GOLD_STANDARD_2027.md), [AI experiment](REUSE_FIRST_EXPERIMENT.md), [Energy metrics](REUSE_SUSTAINABILITY_METRICS.md), [Claim ledger](CLAIM_LEDGER.md), [Science governance](SCIENTIFIC_GOVERNANCE_2027.md), [2027–2031 roadmap](FIVE_YEAR_ROADMAP_2027_2031.md).

**This text is deliberately not a completed or frozen preregistration**. Amend with version, date, reviewers, rationale and exact code/data source once pilot evidence exists.

## Decision reconciliation (2026-10-12)

Before approving or registering this v0.3 draft, resolve all dated cross-document choices in [the protocol reconciliation register](PROTOCOL_RECONCILIATION_DECISIONS_2026_10_12.md). That register is **review guidance only**, not approval or registration, and explicitly preserves Study A (visibility) and Study B (independent user-task/reuse) endpoints, the inability to treat 2024 as AI-free, actual implemented capture surfaces, and the unresolved ethical/statistical gates.
