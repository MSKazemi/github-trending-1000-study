# Roadmap

## M0 — Foundation (this PR)
- [x] Provisional study protocol and hypotheses
- [x] Observation schema and ethics guidance
- [x] Fixture-tested single-page Trending parser and CLI
- [x] Optional point-in-time metadata enrichment
- [x] CI, contributors' instructions and issues
- [ ] Manual audit of parser against real page variants (not yet executed)

## M1 — Validated collection pilot
- [ ] Document permission and access policy for repeat Trending captures
- [ ] Manually check at least 30 parsed rows; track parse failures and language/window stratification
- [ ] Save collection manifest with source checksums
- [ ] Implement stable-ID deduplication and safe resume/backoff
- [ ] Freeze protocol v1 before inspecting outcomes

## M2 — 1,000-unique-repository cohort
- [ ] Multi-week window-stratified collection to 1,000 **unique** eligible repositories
- [ ] Document inclusion flow and attrition
- [ ] Build separately sourced non-observed-trending cohort with fixed seed
- [ ] Collect baseline feature audits (blinded to outcomes where feasible)

## M3 — Longitudinal measurement
- [ ] 30/90/180-day followups, missingness tracking and sensitivity checks
- [ ] Reproducible statistics and uncertainty intervals
- [ ] Clearly labeled exploratory vs confirmatory analyses

## M4 — Publication and community
- [ ] Replication package and manuscript
- [ ] Transparent limitations, null results and actionable evidence-graded lessons
- [ ] Reuse guides and optional interactive dashboard

Do not mark sample goals complete without public methodology and verified counts.

## M5 — Evidence-to-usefulness research (2027 extension, not started)
- [x] Define distinct user value, quality, sustainable growth and cost constructs
- [x] Publish AI workflow substudy design and study-specific threats
- [x] Integrate an explicitly **partial** Sourcegraph #015 documentary pilot with dated first-party candidate leads, seven-segment search-coverage limitations, and offline integrity tests ([issue #81](https://github.com/MSKazemi/github-trending-1000-study/issues/81); [pilot](../research/company-intelligence/2026-04-12_2026-10-12/015-sourcegraph.md))
- [ ] Complete Sourcegraph #015 independent dated-source/human methods audit, true screening denominators, rights/availability checks and prospective reuse-first task validation **before** calling the company issue complete
- [x] Publish evidence-to-lesson grades, templates and claim ledger
- [x] Harden the offline lesson registry v1.1 with strict JSON, RQ/source/result metadata, explicit outcome-scale null reference, bounded regular-file CLI input, supersession integrity and synthetic-only tests ([issue #11 engineering instrument](LESSON_REGISTRY_AUDIT_2026_10.md))
- [ ] Independently verify the source/data hashes, real reviewer, correct null reference/uncertainty interpretation and methodological context before treating any self-reported E4/E5 card as validated evidence
- [x] Add deterministic, offline project idea validation gate with synthetic tests
- [ ] Pre-register independent user-task and task-randomization studies
- [ ] Complete human subject/consent and privacy review as appropriate
- [ ] Capture real task, adoption, agent-cost and 30/90-day maintenance outcomes
- [ ] Publish null/negative results and graded decision-ready practice cards
- [ ] Review scenarios and source version drift quarterly through 2027


## M6 — 2027 green reuse and Trending construct validity (draft; not yet executed)
- [x] Write full study discussion checkpoint with substantive user messages and decisions
- [x] Evaluate Trading/Trending (observed exposure vs unproven utility) construct validity and sampling risks
- [x] Create independent low-star/older reusable component cohort proposal
- [x] Define reuse opportunity, candidate precision/recall, independently accepted task/effort/energy measures
- [x] Publish 2×2 human/AI × conventional/reuse-first experiment candidate protocol
- [x] Publish ISO SCI and SCI for AI measurement boundaries plus source registry
- [x] Build offline reuse-first decision gate + synthetic unit tests
- [ ] Pilot independent open-source reuse sampling and safe software-candidate verification
- [ ] Human audit for functional equivalence, license, CVE and dependencies
- [ ] Obtain ethics/consent and complete registered task experiments
- [ ] Measure kWh (instrumented where feasible) and honestly bound unobservable inference emissions
- [ ] Publish net value, verified software reuse, negative findings and late-2027 evidence-graded practices


## M7 — Fix remaining scientific validity gaps before confirmatory 2027 study
- [x] Audit 12 high-impact missing or under-specified dimensions and identify P0 blockers
- [x] Draft independent task/candidate gold-label protocol, multi-retriever pooling and unknown handling
- [x] Draft versioned supply-chain provenance, licensing/security and malicious package gates
- [x] Draft lifecycle break-even, water/hardware/rebound, upstream maintainer and human comprehension measures
- [x] Draft research governance with independent tasks, consent, contamination safeguards and all-task ITT estimand
- [x] Implement offline, synthetic goldset validation with fail-closed unknown judgments, CI tests and README
- [ ] Pilot diverse task recruitment independently of search systems and future outcomes
- [ ] Assess inter-rater agreement on real cases, third-party evidence and false positives/negatives
- [ ] Obtain complete project/security/legal provenance and verify viability on isolated fixtures
- [ ] Preregister all-task primary outcome, experiment power, stop rules and feasible dates
- [ ] Measure complete lifecycle, provider-energy unknowns, water and upstream maintainer spillovers
- [ ] Report null findings, uncertainty and context-limited 2027 lessons; no training data leakage


## M9 — Publication figures and tables (planned; not empirical)
- [x] Offline F01/T02 observed-only audit with synthetic tests, no inferred cohort or follow-up ([usage](SAMPLING_VISUALIZATION_CLI.md))
- [x] Register 18 figures and 14 tables with manuscript/supplement/future tiers, estimands, denominators, evidence gates and source contracts
- [x] Record dated user visualization request and discussion summary
- [ ] Freeze main-paper visual/estimand mapping during preregistration and independent review
- [ ] Validate each chart's provenance, missingness, sample size, model, CI and quality checks on *observed* data
- [ ] Produce accessible SVG/PDF/PNG plus machine-readable chart manifests with observed-vs-modeled status
- [ ] Publish negative/null analyses, boundary uncertainties and full reproducible exports

See [visual plan](FIGURE_TABLE_PLAN_2027_2031.md), [register](../references/figure_table_register_2027.json), [issue #33](https://github.com/MSKazemi/github-trending-1000-study/issues/33).

## M8 — Adaptive 2027–2031 strategy and stakeholder governance (proposed)
- [x] Define hypothetical professor/statistician/climate/CEO/CTO/OSS/ethics advisory questions and dissent/veto criteria
- [x] Specify research waves for 2027, 2028, 2029, 2030, 2031 with stop/pivot conditions, and *no assumption of funding or partners*
- [x] Define outcome-focused leadership scorecard and quarterly versioned review template
- [x] Register future scenarios with observable triggers and possible disconfirmation
- [x] Define short-term launch/preregistration checks before the first confirmatory cohort
- [ ] Recruit actual independent scientific/statistical review if resources allow; do not imply formal board exists
- [ ] Resolve 2027 sample timeline from actual pilot yield, ethics/access permissions and statistical power
- [ ] Publish first versioned quarterly review with *actual* missingness, protocol amendments and source updates
- [ ] Validate one real task cohort, external evidence and verifiable total cost before building a product
- [ ] Repeat experiment and revisit product decision at 2028/2029 stage gates; no assumed year-2031 outcomes


## M9 — Issue #27: operational pilot provenance and conservative enrollment preflight
- [x] Implement client-recorded SHA-256/UTC manifest from a single explicitly invoked public HTML request
- [x] Add strict raw SHA/size/URL/date/HTML verification and separate captured-versus-parsed timestamps
- [x] Ensure parse-only legacy output and verified-integrity pilot rows are **not** silently confirmatory-cohort eligible
- [x] Add a documentary readiness evaluator for pilot and confirmatory phases, defaulting to **not_ready**
- [x] Add a synthetic offline test suite and a blank audit/signoff form
- [x] Consolidate preliminary RQs, observational and randomized estimands into explicitly unfrozen v0.3 draft
- [ ] Human access/Terms/robots review for recurring collection; no scheduled capture yet
- [ ] Validate collector against real allowed GitHub Trending HTML and >=30 independently audited rows
- [ ] Implement six language source surfaces, true immutable-ID dedup and full missing-capture journal
- [ ] Freeze independent tasks, safety rubric, power/sample simulation, privacy/consent and statistical review
- [ ] Submit/record authentic independent signoff and appropriate prospective registration **before enrollment**
- [ ] Start prospective capture only under permitted scope; record real N and actual missingness
See docs/PILOT_CAPTURE_AND_PREFLIGHT.md and docs/PROTOCOL_FREEZE_STATUS_2026_10_12.md. The proposed November 2026 cohort start **must change** if blockers remain.

### 2026-10-12 #4 progress (instrumentation, not cohort data)

- Write-once capture/manifest and parsed outputs are implemented in PR #46 (merged); the multi-file pair is not a database transaction.
- A separate prospective 30/90/180-day follow-up module, immutable event ledger and mocked API tests are proposed in a follow-up PR. It requires explicit human-approved cohort references and an opt-in network flag.
- Still missing: verified real parser recall (#2), external collection/access authorization, stable-ID reconciliation across actual observed captures, qualified control sampling/power (#3), signed preregistration and real follow-up data. Keep issue #4 open until actual safe pilot/resume and integration readiness are audited.


## M11 — Issue #2 independent page QA (2026-10-12)
- [x] Refactor raw manifest validation so a parser-rejected page can still be audited against intact source bytes
- [x] Implement independent two-reviewer full-page rank/identity comparisons across specified windows
- [x] Report exact ranked TP/FP/FN, parser abstentions, unresolved reviewer discrepancies, source checksums and coverage
- [x] Require 30 agreed rows across daily/weekly/monthly for **documentary** coverage check, never automated cohort approval
- [x] Add write-once CLI report and synthetic 36-row cross-window / off-selector / malicious path fixture tests
- [x] Publish human audit runbook, bundle template and truthful current-access limitation
- [ ] Approve platform access scope and capture actual raw daily/weekly/monthly sources without bypass
- [ ] Recruit 2 truly independent human reviewers and adjudicate >=30 real visible rows across windows
- [ ] Measure real row/rank precision/recall, including off-selector omissions and source layout drift
- [ ] Obtain human scientific review/signoff and leave pilot/pre-registration pending until evidence exists

No actual live 30-row QA can be credited from this PR. Issue [#2](https://github.com/MSKazemi/github-trending-1000-study/issues/2) remains open for field validation. Details: [independent audit runbook](INDEPENDENT_PAGE_AUDIT_2026_10_12.md).

## M12 — enterprise CI and no-loss PR review (2026-10-13 integration)

- [x] Consolidate SHA-pinned official GitHub Actions into a **single canonical** CI workflow with Python 3.10, 3.12 and 3.14 and read-only checkout; retain JSON integrity, unittest and CLI smoke checks (integration PR #255).
- [x] Reconcile the existing PR author template and canonical scientific merge gate instead of force-merging a competing template/policy (PR #255).
- [x] Record responsible exact-head, non-destructive merge procedures in AGENTS.md and CONTRIBUTING.md (documentation follow-up to #245).
- [ ] Configure enforceable GitHub branch protections, required status checks and genuinely independent reviews in repository settings; documentation is not an access-control mechanism.
- [ ] Complete actual source-access permission, real-sample QA, protocol preregistration, and independent task/energy validation before presenting synthetic tools as empirical findings.
- [ ] Resolve all remaining conflicting research and company-intelligence draft PRs claim by claim, preserving unique citations and tests before retirement.

Related: [canonical PR gate](PR_MERGE_QUALITY_GATE_2026_10_13.md), [integration checkpoint](PR_REVIEW_CHECKPOINT_2026_10_13.md), [source-access limitations](SOURCE_ACCESS_DECISION_2026-10-13.md). Superseded PR #245 remains in GitHub history for audit rather than being overwritten.

## Issue #6 — Trending validity engineering instruments (2026-10-14)

- [x] Reuse existing within-surface Jaccard, common-item Kendall tau and bounded/extrapolated RBO with documented page denominators (see [temporal-overlap pilot](TRENDING_OVERLAP_PILOT_2026_10_12.md)).
- [x] Implement offline per-language/per-window observed-in-frame fraction with an **explicit predeclared candidate-frame denominator**, declared filter/window/URL binding, an outside-frame count, and no invented cross-language population measure.
- [x] Implement a pre-capture-feature-only, strictly chronological train/heldout rank-order proxy for **already displayed** repositories; require distinct repository IDs across splits and fixed training-only predictor selection, distinct feature-source digests and a bounded pairwise-work budget.
- [x] Add fully synthetic versions of both contracts, privacy/URL/timestamp/denominator/leakage/tie tests, a CLI and [complete runbook](TRENDING_COVERAGE_AND_RANK_PROXY_2026_10_14.md).
- [x] Harden bounded JSON reads against symlink-substitution races, non-regular FIFO input and file growth; redact unsupported field names from diagnostics, with focused adversarial tests (see [engineering review](reviews/2026-10-14-pr-290-merge-readiness.md)).
- [ ] Independently review source rights/robots/permission, verify original real page captures and audit actual ranks across daily/weekly/monthly and language filters (dependent on #2).
- [ ] Build an independently justified at-risk frame for population-level sampling interpretation; verify historical feature timestamps, true prospective preregistration and heldout temporal replicability.
- [ ] Produce observational estimates, missingness and uncertainty only when lawful real observations and human methodology review exist. Synthetic scores do **not** close the empirical research question.

**Disposition:** issue #6 software implementation has undergone an [engineering review](reviews/2026-10-14-pr-290-merge-readiness.md). Technical CI is distinct from the still-pending **independent qualified methods sign-off** required for PR #290's research protocol boundary. The instrument is not a validated real-world Trending analysis, reverse-engineered ranking algorithm or confirmed fairness result. Keep empirical issue #6 open.
