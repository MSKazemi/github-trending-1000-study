# GitHub Trending 1000 Study

**2027 mission:** Discover, verify and reuse existing open-source code before reinventing it, so developers can deliver **genuinely useful software** with less unnecessary human effort, AI-token expenditure, technical debt and environmental impact. GitHub Trending measures *observed attention*, not proven utility or sustainability.

**A reproducible, longitudinal observational study of open-source repository visibility, community practices, and growth.**

[![CI](https://github.com/MSKazemi/github-trending-1000-study/actions/workflows/ci.yml/badge.svg)](https://github.com/MSKazemi/github-trending-1000-study/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/Code-MIT-blue.svg)](LICENSE)

> **Research status: protocol and tooling (not findings).** No sample of 1,000 repositories has been collected or analyzed yet. This project does **not** claim causal effects or endorse manipulation of GitHub Trending.

## Questions
- **RQ1:** Which observable repository practices are associated with subsequent star growth *within* a trending sample?
- **RQ2:** Do documentation, governance, automation and contribution affordances predict subsequent engagement after controlling for age, language and baseline popularity?
- **RQ3:** How do trending repositories differ from an independently sampled non-trending comparison cohort?
- **RQ4:** Which observed associations persist across languages, observation windows and follow-up periods?

## Start here
- [Research protocol](docs/PROTOCOL.md) — operational definitions, sampling, confounding and analysis.
- [**Scientific protocol reconciliation and outstanding decisions**](docs/PROTOCOL_RECONCILIATION_DECISIONS_2026_10_12.md) — conflict register for Study A/Study B and evidence gates. **Reviewer proposals only; no approved or frozen preregistration.**
- [Data dictionary](docs/DATA_DICTIONARY.md) — schema, missingness and provenance.
- [Ethics and limitations](docs/ETHICS.md) — privacy, API etiquette and validity.
- [Contributing](CONTRIBUTING.md) — human and AI-agent contributions.
- [Roadmap](docs/ROADMAP.md) — staged milestones and acceptance criteria.
- [Offline CI artifact gate](docs/RESEARCH_JSON_INTEGRITY_GATE.md) — strict JSON/CSV validation plus full Git-tracked Python/JSON syntax coverage; engineering checks, not scientific source verification.
- [**Ten-issue parallel scientific methods audit (2026-10-13)**](docs/TEN_ISSUE_METHODS_INTEGRATION_2026_10_13.md) — ten reproducible research workstreams, per-PR Python 3.10/3.12 CI evidence, shared task/denominator design, remaining human/permission/metering gates and practical lessons; **not empirical findings or approved enrollment**.
- [**Repository checkpoint (2026-10-13)**](docs/REPOSITORY_CHECKPOINT_2026-10-13.md) — 152 tracked files, source-access stop gate, scientific blockers and next priority; risk-based audit, not empirical findings.
- [**Full repository audit (2026-10-12)**](docs/REPOSITORY_AUDIT_2026-10-12.md) — code integrity, data/methods readiness, CI, scientific blockers, open PRs and practical remediation priorities; **inspection, not research findings**.
- [**Execution plan after the audit**](docs/NEXT_STEPS_EXECUTION_2026-10-12.md) — evidence-gated development tasks, human approvals, PR dependencies, go/no-go milestones and a bounded feasibility pilot.
- [Faculty-style methodological review](docs/FACULTY_STYLE_RESEARCH_RECOMMENDATIONS_2026-10-12.md) — evidence-grounded advice, **not actual professorial endorsement**; [first expanded task intake](docs/CROSS_ECOSYSTEM_TASK_INTAKE_2026-10-12.md).
- [Observed sampling visualization CLI](docs/SAMPLING_VISUALIZATION_CLI.md) — offline F01 SVG and T02 Markdown/JSON audit; **not empirical findings**.
- [Publication figures and tables](docs/FIGURE_TABLE_PLAN_2027_2031.md) — proposed **18 figures and 14 tables** across 2027 observational research and conditional 2028–2031 trials; **no empirical results yet**. [Machine-readable register](references/figure_table_register_2027.json).
- [**One-repository, reuse-first first-use pilot (offline synthetic)**](docs/FIRST_USE_REUSE_PILOT_2026_10_12.md) — reproducible existing-CLI task, testable fail-closed output, source/uncertainty and build-vs-reuse decision card; **not a recruited user study or measured cost/energy benefit**. [Evidence card](examples/first_use_reuse_pilot.example.json).
- **[News, scientific journal and conference evidence watch (2026–2027)](docs/SOURCE_MONITORING_AND_JOURNALS_2027.md)** — research windows, journals and verified 2027 submission dates; [49-source curated watch register](references/source_watch_2026.json). The weekly briefing configuration is currently **disabled**.

## Install & run

Requires Python 3.10+; no external Python dependencies.

```bash
python -m unittest discover -s tests -v
python -m trending_study --help
python -m trending_study parse-trending --input tests/fixtures/trending.html --date 2026-10-11 --window daily --output /tmp/trending.jsonl
python -m trending_study summarize --input /tmp/trending.jsonl
```

**Source-access stop gate (2026-10-13):** GitHub's [published robots.txt](https://github.com/robots.txt) includes `Disallow: /*since=*` under `User-agent: *`, matching the `/trending?since=daily|weekly|monthly` paths this prototype would request. Because appropriate access for the proposed research cadence is **not documented or independently approved**, the `capture` command is now **hard-blocked before any HTTP request**. There is **no CLI flag, token or environment override**. A PR that re-enables live fetching must contain a dated platform/source-access assessment, exact authorized URLs and cadence, independent human review, and any needed signed protocol amendment. A robots rule is an access warning, not by itself a complete legal opinion; neither code nor self-written approval text grants permission.

The [source-access decision and lawful alternatives](docs/SOURCE_ACCESS_DECISION_2026-10-13.md), [pilot runbook](docs/PILOT_CAPTURE_AND_PREFLIGHT.md) and [write-once capture contract](docs/CAPTURE_IMMUTABILITY_2026_10_12.md) document the controls. **Offline** `parse-trending`, `pilot-parse` for already-authorized, locally preserved evidence, synthetic page QA, and approved GitHub REST API metadata workflows remain available. Offline parser success is not independently authenticated live Trending data. Do not use manual snapshots as a workaround without the same source-access and provenance review.

**Current command behavior:** `python -m trending_study capture --date <current-UTC-date> --window daily --output ...` returns a nonzero error before accessing GitHub or creating files. The earlier UTC/manifest capture example is retained as a *future conditional procedure* in the pilot SOP, **not** an instruction to run it now. Observations cannot be backdated or reconstructed from today's Trending page.

Enrich observed repositories with current public metadata (optional `GITHUB_TOKEN`; do not commit tokens):

```bash
GITHUB_TOKEN=... python -m trending_study enrich --input <actual-pilot-jsonl> --output <new-output-path>.jsonl
```

See the protocol before interpreting any collected counts. A Trending appearance is not a random sample of all GitHub projects, and GitHub's Trending ranking methodology is opaque.

## Reproducibility and citation
Each observation includes provenance, UTC collection time, selection window and source URL. Preserve frozen raw captures with checksums before analysis. Record a protocol version, fixed analysis scripts and a snapshot tag for published results. **Do not infer causal growth strategies from cross-sectional correlations.**

## License
MIT applies to original code and text here. Third-party repository metadata remains subject to applicable rights, platform terms and privacy obligations. Reuse of harvested data should be assessed separately.

## Contribute
Open an issue for reproducibility defects, language coverage, validity threats, sampling improvements, visualization or replication. See [CONTRIBUTING.md](CONTRIBUTING.md).


## 2027 research track: Useful software in the AI-agent era

**Our goal extends beyond trending:** learn what makes a public project *useful, independently verifiable, economical to maintain, and worth building* as AI-assisted coding expands. This is a proposed sub-study, not a completed set of results.

- [Discussion synthesis / decision history](docs/CONVERSATION_SYNTHESIS.md)
- [Usefulness constructs and metrics](docs/USEFULNESS_FRAMEWORK.md)
- [AI-assisted and vibe-coding sub-study](docs/AI_CODING_STUDY_2027.md)
- [Evidence-to-lesson protocol (E0–E5)](docs/EVIDENCE_TO_LESSON_PROTOCOL.md) and [versioned offline lesson registry v1.1](docs/LESSON_REGISTRY_AUDIT_2026_10.md) — strict synthetic examples, source/result metadata, unknown-versus-null handling, no certified findings
- [Developer build/reuse/pivot playbook](docs/DEVELOPER_DECISION_PLAYBOOK.md)
- [Total token, human and maintenance economics](docs/TOKEN_TIME_ECONOMICS.md)
- [2027 conditional scenarios and monitoring](docs/FUTURES_2027.md)
- [Reference register](docs/REFERENCES_AI_2027.md) and [claim ledger](docs/CLAIM_LEDGER.md)
- [Project idea validation template](templates/idea_validation_card.md), [evidence-graded lesson template](templates/lesson_card.md) and [experiment registration](templates/experiment_registration.md)

### Assess a proposed idea offline

```bash
python -m trending_study.value_gate --input examples/idea_card.example.json
```

This deterministic **heuristic** shows the next evidence gate and budget warnings. It does **not** claim to predict the popularity or usefulness of a project, classify trained-on-1,000 data, or validate a product. The example is synthetic. See [its specification](docs/USEFULNESS_EVALUATION_TOOL.md).

### Research commitments
No generated 'findings' without observed data; no fabricated users, installations or savings; no claim that AI attribution is perfectly detectable; no manipulation of stars/traffic; and no paid growth services. A verified small niche tool may be more useful than a large popular repo.


## New central research track: Green, reusable software by 2027

We now explicitly study **reuse before generation**, not only repository popularity. The scientific question is whether finding, evaluating, integrating and maintaining existing code can improve independently verified user outcomes and reduce total human/energy cost relative to a matched new-build alternative. No energy/CO2 savings have yet been demonstrated.

- **[Green reuse research mission](docs/GREEN_REUSE_MISSION_2027.md)** — updated overarching goal and additional independent reuse cohort
- **[Trending validity and weakness audit](docs/TRENDING_VALIDITY_AUDIT.md)** — what rank/stars do and do not validate
- **[Selection period and eligibility](docs/SELECTION_PROTOCOL_2027.md)** — 2026 Oct pilot; Nov 2026–Apr 2027 candidate enrollment; 180-day follow-ups
- **[Coding agent chronology](docs/AGENT_RELEASE_ADOPTION_TIMELINE.md)** — why 2024+ baseline and verified agent-use events
- **[Reuse/green measurement dictionary](docs/REUSE_SUSTAINABILITY_METRICS.md)** — functional proof, time, token, kWh and SCI-style CO2 bounds
- **[Reuse-first randomized study](docs/REUSE_FIRST_EXPERIMENT.md)** — human vs agent × normal vs reuse-first workflows
- **[Agent development reuse guide](docs/REUSE_FIRST_PLAYBOOK.md)** — practical search, license, security, validation, stop rules
- **[Reusable evidence gate](docs/REUSE_GATE_TOOL.md)** — offline deterministic heuristic; unknown is not pass
- **[Scientific source list](docs/READING_LIST_2027.md)**; [35 AI/GitHub/tech news sources](references/study_sources_2026.json); [16 green/reuse/energy sources](references/green_reuse_sources_2026.json)
- [Offline provisional news-record validator](docs/NEWS_SOURCE_RECORD_VALIDATOR.md) — reusable, synthetic-tested source-structure gate extracted from draft #59; **no real records or scientific findings merged**
- **[Conversation checkpoint](research-notes/conversation-checkpoint-2026-10-11.md)** — all study-related user prompts in this chat, dated assistant findings and decision history

To use the **offline reuse-first evidence check**:

```bash
python -m trending_study.reuse_gate --input examples/reuse_check.example.json
python -m unittest discover -s tests -v
```

The example is synthetic and should request verification, not install code or claim carbon savings. New code may be desirable when no safe, compatible or suitable prior implementation exists. A 1,000-repository Trending sample cannot by itself represent the global universe of useful reusable software.


## Newly identified scientific risks — read before interpreting results

The October 2026 critical-gap review found that three ideas need independent validation: **a search that fails to find code cannot prove no viable code exists**, an apparently suitable package is not necessarily safe/legal/functionally equivalent, and fewer tokens do not establish net environmental benefit.

- **[Critical gaps and prioritized research actions](docs/CRITICAL_RESEARCH_GAPS_2027.md)** — 12 risks with P0/P1/P2 safeguards
- **[Independent gold-standard task-to-code judging](docs/REUSE_GOLD_STANDARD_2027.md)** — stratified tasks, mixed retriever pools, two raters, blind adjudication and incomplete relevance
- **[Supply-chain identity/security/rights](docs/SUPPLY_CHAIN_PROVENANCE_2027.md)** — actual package versions, OpenSSF, SLSA, SPDX, OSV and no blind execution
- **[Lifecycle break-even and rebound](docs/FULL_LIFECYCLE_BREAK_EVEN_2027.md)** — development versus runtime, carbon/water/hardware, maintained full-boundary comparison
- **[Upstream maintainers and human learning](docs/MAINTAINER_EXTERNALITIES_2027.md)** — support burden, comprehension, fair reuse
- **[Research governance](docs/SCIENTIFIC_GOVERNANCE_2027.md)** — study eligibility, data leakage, preregistration and selection effects
- **[New research and standards sources](references/critical_gaps_sources_2026.json)** — 15 contextual and methodological references

Offline, self-reported *synthetic* gold-set validator:

```bash
python -m trending_study.goldset --input examples/goldset.synthetic.json --k 2
python -m unittest discover -s tests -v
```

This does **not** label real packages, measure true recall, or validate actual reuse. An unknown candidate must not silently become an irrelevant one. See [CLI notes](docs/GOLDSET_VALIDATION_CLI.md).


## Strategic vision: 2027–2031 (five-year research program)

The **scientific question remains falsifiable:** when does **discovering, verifying and reusing** existing code create more independently accepted value per whole-lifecycle human, maintainer, security and ecological cost than ordinary development? Trending is an observed discovery/attention *surface*, not evidence of usefulness.

The original 2026–2027 study is **Year 1 of a proposed five-year program**, not an indefinitely expanding single paper. New waves should remain subject to science, budget, ethics, source permissions and replicated negative results.

- [Hypothetical senior scientific/CEO/CTO advisory perspectives](docs/ADVISORY_BOARD_STRATEGY_2027_2031.md) — no actual external endorsement implied
- [Annual scientific and engineering milestones 2027–2031](docs/FIVE_YEAR_ROADMAP_2027_2031.md) — explicit annual gates and stop conditions
- [Conditional 2027–2031 scenarios and disconfirming signals](docs/FUTURE_SCENARIOS_2027_2031.md)
- [Professor/CEO/CTO/maintainer leadership scorecard](docs/LEADERSHIP_SCORECARD_2027_2031.md) — verified outcomes, not arbitrary success score
- [Independent multi-stakeholder governance and research ethics](docs/RESEARCH_PROGRAM_GOVERNANCE_2027_2031.md)
- [Immediate 2026–early 2027 launch gates](docs/INCEPTION_CHECKLIST_2026_2027.md) — do not collect a confirmatory cohort before baseline freeze
- [Quarterly advisory review template](templates/quarterly_advisory_review.md) and [curated source register](references/five_year_strategy_sources_2026.json)

**As of 2026-10-11:** only methods, examples and tooling exist; a funded board, 1,000-repository sample, task-level trial, kWh savings and 2027–2031 forecast outcomes do **not** exist.


## October 2026 pilot instrumentation — status: not enrolled

The first code implementation for issue [#27](https://github.com/MSKazemi/github-trending-1000-study/issues/27) adds SHA-256-linked capture manifests and a strict pilot parser. **A test passing is not pilot data collection, a validated real-page ranking or preregistration.** The latest status is [pending scientific gates](docs/PROTOCOL_FREEZE_STATUS_2026_10_12.md), with the [pilot SOP](docs/PILOT_CAPTURE_AND_PREFLIGHT.md) and [draft v0.3 protocol](docs/PREREGISTRATION_DRAFT_2027.md).

A single user-initiated, currently observed **unfiltered** Trending page can be captured after permitted-access review:

```bash
UTC_DAY="$(date -u +%F)"
python -m trending_study capture --date "$UTC_DAY" --window daily \
  --output "data/raw/$UTC_DAY-daily.html" \
  --manifest-output "data/raw/$UTC_DAY-daily.manifest.json"

python -m trending_study pilot-parse \
  --input "data/raw/$UTC_DAY-daily.html" \
  --manifest "data/raw/$UTC_DAY-daily.manifest.json" \
  --output "data/processed/$UTC_DAY-daily.pilot.jsonl" \
  --audit-output "data/processed/$UTC_DAY-daily.audit.json"
```

Validate unresolved study prerequisites offline:

```bash
python -m trending_study pilot-preflight \
  --input examples/pilot-preflight.example.json --stage confirmatory
```

**The example must report `not_ready`.** Actual approvals, pilot sample QA, stable repository IDs, permission-safe language panels, sample/power analysis, independent task-frame and consent review remain **pending**. Output is *not* cohort eligible until those steps are documented. Existing `parse-trending` remains supported for legacy fixtures but explicitly marks its capture timestamp unverified.

## Central mission clarification — modern coding to verified reuse and practical 2027 lessons (2026-10-12)

The main target is **how AI-assisted, vibe/prompt-led and agent-delegated development change open-source practice**, which repository practices lead to **genuine, independently verifiable reuse, useful adoption and responsible contributions**, and when reuse rather than needless reinvention delivers better outcomes for people and the environment. GitHub Trending is one **visibility observation surface**, not the ultimate success criterion. Older projects remain valid historical/reference or reuse candidates; new agent-era workflows remain the focal comparison.

- [Integrated research mission, constructs and falsifiable questions](docs/AI_ERA_CODING_REUSE_RESEARCH_MISSION.md)
- [Practical repository quality, reuse, contribution and visibility handbook](docs/PRACTICAL_REPOSITORY_GROWTH_AND_REUSE_2027.md)
- [Per-repository action and evidence card](templates/repository_action_evidence_card.md)
- [Dated mission-clarification decision log](research-notes/mission-clarification-2026-10-12.md)

**Status:** proposed methods and engineering checklist, not analyzed scientific results or a guarantee of stars, users or lower carbon. Changes to primary outcomes/sampling still require a consolidated preregistration and human approval.


### Preservation safeguard — issue #4 (2026-10-12)

The `capture`, `parse-trending`, `pilot-parse` and `enrich` commands now reject existing destination files and input/output aliases before overwriting any source. Outputs are fully staged before exclusive publication. The raw+manifest pair is **not** one atomic transaction: if only one exists after an interrupted run, preserve it, record an incident, and never call it validated or enrolled. See [technical contract and operator SOP](docs/CAPTURE_IMMUTABILITY_2026_10_12.md).

## Immutable 30/90/180-day follow-up instrumentation (2026-10-12)

To prepare **future** cohort measurement, the [longitudinal follow-up CLI](docs/LONGITUDINAL_FOLLOWUPS_2026_10_12.md) creates a deterministic write-once schedule from self-declared human-approved baseline rows, and maintains per-attempt immutable event records with exact UTC and GitHub stable numeric ID checks. It refuses pilot-only/unverified baseline rows, never silently backfills missing follow-ups with current stars, and distinguishes rate limits, unavailable repos and missed windows from zero adoption. `status` works **offline**; `collect` requires explicit `--confirm-network` and a bounded request budget.

```bash
python -m trending_study.longitudinal plan --input examples/followup_baseline.synthetic.jsonl \
  --output /tmp/followup-plan.synthetic.jsonl --grace-days 3 7 14
python -m trending_study.longitudinal status \
  --plan /tmp/followup-plan.synthetic.jsonl --events-dir /tmp/followup-events.synthetic
```

**The fixture is synthetic and deliberately lacks real approval. Do not run live collection against it.** No 1,000-repository cohort or real follow-up result exists; source access, external method approval, human-reviewed parser QA and confirmatory preregistration remain pending.

## Structural Trending parser QA — pending real-page audit (2026-10-12)

The [strict Box-row parser and audit protocol](docs/PARSER_STRUCTURE_QA_2026_10_12.md) now rejects **partially positive parses** (one correct row plus malformed other rows), duplicate identities, missing/multiple header links and truncated supported articles rather than silently re-numbering results. The pilot JSON audit exposes supported-selector row counts but still explicitly requires **independent human verification** of at least 30 actual rows and of rows outside that selector. **No real page QA has been performed**. Language pages and confirmatory collection remain blocked pending permissions and scientific review.

### 2027 blinded task-to-existing-code review instrument (synthetic pilot)

The [blinded review workflow](docs/BLINDED_REUSE_REVIEW_WORKFLOW.md) prepares rank-redacted candidate packets and audits separate reviewer-A/B submissions with optional C adjudication. It preserves unreviewed candidates as **unknown**, attaches a frozen pool SHA-256, checks version/availability and declared functional/license/security/maintenance gates, and can export into the existing `goldset.py` validator. It **cannot** verify real reviewer independence, functional tests, evidence truth or complete recall. All examples are synthetic; the earlier [public issue intake PR #38](https://github.com/MSKazemi/github-trending-1000-study/pull/38) is not a reviewed or accepted task benchmark.

```bash
python -m trending_study.blind_review prepare --pool examples/review_pool.synthetic.json --output /tmp/blind-review-packet.json
python -m trending_study.blind_review audit --pool examples/review_pool.synthetic.json --review-a examples/review_rater_a.synthetic.json --review-b examples/review_rater_b.synthetic.json --adjudication examples/review_adjudication.synthetic.json --output /tmp/blind-review-audit.json
```

See the [2026-10-12 milestone record](docs/REVIEW_MILESTONE_2026-10-12.md) for the evidence status and open scientific gates. No real AI/reuse productivity or sustainability findings are claimed.

## October 2026: prospective task-candidate intake pilot

An [offline task-intake validator and documented exploratory public-issue frame](docs/PUBLIC_TASK_INTAKE_PILOT_2026-10-12.md) now demonstrate **pre-reuse** deterministic candidate sampling with provenance, preserved pull-request exclusions, and explicit unknown/unreviewed states. The selected open GitHub issues are task leads, **not** verified reusable-software opportunities or randomized study assignments. Human screening, frozen acceptance tests, consent, independent adjudication, and a preregistration decision remain pending. Run `python -m trending_study.task_intake --input examples/task_intake.public_2026-10-12.json --output /tmp/task-intake-audit.json` and inspect the complete ledger.

**New real public metadata intake (2026-10-12, exploratory, not enrolled):** Six deliberately chosen Python/JS-TS/Rust/Go repositories yielded **90** first-page REST issue/PR entries: 44 non-PR issue leads and 46 excluded PRs. The frozen-seed selector identified **16 unreviewed public issue leads**. See the [source and validity report](docs/CROSS_ECOSYSTEM_TASK_INTAKE_2026-10-12.md), [directly clickable 16-issue screening queue](research-notes/task-screen-queue-2026-10-12.md), [independent human screening template](templates/feasibility_task_review_card.md), and [pending human evidence issue #65](https://github.com/MSKazemi/github-trending-1000-study/issues/65). No real experiments, independent acceptance tests, verified reusable solutions or environmental results have been produced.

```bash
python -m trending_study.task_intake --input examples/task_intake.cross_ecosystem_2026-10-12.json --output /tmp/task-intake-cross-ecosystem-2026-10-12.json
```

## 2026-10-12: 16 public issue metadata rechecks and pre-search review instrument

The existing **16 hash-selected, unreviewed** public issue leads were rechecked through individual permitted GitHub REST issue endpoints at a batch completion time of **2026-10-12 20:25:45 UTC**. All 16 stable numeric IDs/links matched and were open at recheck, with no `updated_at` timestamp differences from their original reduced intake metadata. This **does not** establish independently accepted tasks, absence of public solution hints, genuine reviewer independence, agent outcomes, 1,000 Trending observations or environmental savings.

The [limited observed metadata and scientific caveats](docs/TASK_SCREENING_SOURCE_RECHECK_2026-10-12.md) accompany the [reduced recheck JSON](research-notes/issue-recheck-2026-10-12.json), [offline task-screening CLI](trending_study/task_screen.py) and [synthetic reviewer consistency tests](tests/test_task_screen.py). The **human-source screening and independent acceptance criteria remain open** at [issue #65](https://github.com/MSKazemi/github-trending-1000-study/issues/65).

```bash
python -m trending_study.task_screen prepare \
  --frame examples/task_intake.cross_ecosystem_2026-10-12.json \
  --recheck research-notes/issue-recheck-2026-10-12.json \
  --output /tmp/issue65-screen-packet.json
```

Avoid interpreting even two matching *synthetic or self-reported* reviewer labels as verified human approval. **Original public issues may already contain specific fixes**; real maintenance and independent blind task-solving require different experimental designs.

## 2026-10-12: reproducible, synthetic 2027 task-trial pilot instrument

For the **separate, opt-in randomized reuse-first experiment** (not the observational Trending cohort), the initial [offline task-frame allocation and outcome audit](docs/TRIAL_PILOT_INSTRUMENT.md) is available. It validates frozen task/acceptance hashes, prespecified screening exclusions, deterministic task-cluster randomization across the proposed 2×2 human/agent × usual/reuse-first arms, and all-assigned-task outcome accounting including failures, refusals, pending work and missing human time.

```bash
python -m trending_study.trial assign --frame examples/trial_frame.synthetic.json --output /tmp/trial-allocation.synthetic.json
python -m trending_study.trial audit --frame examples/trial_frame.synthetic.json --assignments /tmp/trial-allocation.synthetic.json --outcomes examples/trial_outcomes.synthetic.json
```

**Important:** both fixtures are **synthetic only**; no task trial, recruited participants, study preregistration, independent human review, verified reuse outcome or energy saving has occurred. [Start-of-study checkpoint (2026-10-12)](docs/TASK_TRIAL_START_2026-10-12.md) records the decisions, engineering scope and next approval gates. This is a bounded tooling contribution tracked in [issue #25](https://github.com/MSKazemi/github-trending-1000-study/issues/25), now **closed**; its closure does **not** establish independent protocol/ethics review, power simulation, real-task screening or a real randomized pilot. The remaining real-world task acceptance gate is tracked separately in [issue #65](https://github.com/MSKazemi/github-trending-1000-study/issues/65).


## Independent Github Trending page QA (2026-10-12, Issue #2)

The new **offline** `audit-pages` command compares each preserved raw HTML+UTC/SHA manifest against two separately annotated, full-page ranked row lists. It records reviewer disagreements, exact rank+identity true/false positives and omissions, and whole-page parser rejections. For a genuine A/B disagreement, the same command now also accepts an **optional third reviewer-C adjudication record**; original A/B disagreement and the separate C decision remain visible, never self-certifying reviewer independence. It can detect off-selector pages that a positive-subset parser would otherwise miss. The report can reach a **documentary consistency pass** but **never claims actual human independence, permission, cohort eligibility or real recall**.

Use optional `--markdown-output <new-summary.md>` for a write-once **derived** review table; the JSON report remains canonical, and neither output proves human independence. [Detailed independent 30-real-row QA protocol](docs/INDEPENDENT_PAGE_AUDIT_2026_10_12.md) · [Template input](templates/page_audit_bundle.template.json) · [CLI source](trending_study/page_audit.py) · [Synthetic unit tests](tests/test_page_audit.py).

```bash
python -m trending_study audit-pages --bundle data/raw/qa-bundle.json \
  --output data/processed/qa-report.json --min-rows 30 --require-consistent
```

Populate the bundle **only after permitted captures and independent human labeling**. The committed test suite simulates 36 rows across daily/weekly/monthly, but these are synthetic: **no current raw Trending captures or >=30 real row human audit were obtained**. Direct source access was unavailable in this runtime, and independent access/legal review remains outstanding. [Issue #2](https://github.com/MSKazemi/github-trending-1000-study/issues/2) must remain open.

## 2026 AI software and coding-agent company watchlist (exploratory)

- [100 named companies across 10 ecosystem layers](docs/AI_SOFTWARE_COMPANIES_100_WATCHLIST_2026-10-12.md) — dated, non-ranked company/brand landscape, ownership corrections, research questions and practical reuse-first lessons.
- [Machine-readable 100-company register](references/ai_software_companies_100_2026-10-12.csv) — official-source URLs and editorial study lenses; **not** a verified success ranking, complete company population or sampled GitHub repository cohort.


## Six-month 100-company AI and software intelligence (2026-10-12)

**100 GitHub issues created** for the [100-company industry watchlist](docs/AI_SOFTWARE_COMPANIES_100_WATCHLIST_2026-10-12.md). Each ticket requests a **2026-04-12 through 2026-10-12** official website/release-note/roadmap and independent-news screening, a feature/change chronology, attributed future plans, conditional 2027–2031 scenarios, and a falsifiable reuse-first lesson for our own open-source repositories. **Issues created ≠ company research completed.**

- [Browse the 100 company-specific GitHub issues grouped by sector](docs/COMPANY_ISSUE_INDEX_2026_10.md)
- [Machine-readable 100-issue URL index](references/ai_software_company_issue_index_2026-10-12.csv)
- [Scientific evidence/coverage protocol](docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md) and [report template](templates/company_six_month_intelligence.md)
- [Issue task template](templates/company_intelligence_issue.md)
- [Initial dated source-checked company news leads](research-notes/company-intelligence-initial-leads-2026-10-12.md) — examples only; all full company reviews pending

The index and watchlist are **editorial, non-ranked snapshots**, not empirical firm-performance/market-share datasets; future plans and vendor assertions are not verified outcomes.

## Strategic industry foresight: AI-native software, agents and OS (2026-10-12)

- [**2027–2031 technology outlook: programming, applications, operating systems, LLMs and agents**](docs/STRATEGIC_TECH_OUTLOOK_2027_2031_2026_10_12.md) — source-checked 2026 forecast vintage, *uncertain falsifiable* scenarios, practical 2027 implementation and measurement gates; [**18-source, nine-forecast, seven-metric register**](references/industry_technology_outlook_2026_10_12.json); [issue #58](https://github.com/MSKazemi/github-trending-1000-study/issues/58). **Not personal views of any real executive, a completed empirical study, or a protocol amendment.**



## October 2026: bounded human/agent cost ledger (offline, synthetic only)

The [task-cost ledger audit](docs/TASK_COST_LEDGER_2026-10-12.md) extends the existing **all-assigned-task** randomized-trial instrument with privacy-minimized human work intervals, model/tool/retry/CI event counts, provider token quantities, provenance-tagged USD event amounts, missingness-aware summaries, and predeclared budget alerts. **It does not collect live agent telemetry, authenticate consent, observe real participants, calculate carbon, or prove productivity effects.**

```bash
python -m trending_study.trial assign \
  --frame examples/trial_frame.synthetic.json \
  --output /tmp/assigned-costs.synthetic.json
python -m trending_study.task_costs \
  --frame examples/trial_frame.synthetic.json \
  --assignments /tmp/assigned-costs.synthetic.json \
  --outcomes examples/trial_outcomes.synthetic.json \
  --input examples/task_costs.synthetic.json \
  --output /tmp/task-costs-report.synthetic.json
```

All eight **synthetic** randomized tasks remain in the denominator, including failures/refusals/pending records. Unknown human/token/event-cost coverage remains `null`, and output is write-once. This engineering instrument addresses part of [issue #10](https://github.com/MSKazemi/github-trending-1000-study/issues/10) and CTO systems-economics priority CT2; it is **not** a completed scientific trial.


## Merge assurance and code/research quality

Follow the [canonical enterprise PR merge gate](docs/PR_MERGE_QUALITY_GATE_2026_10_13.md) and the [dated integration audit](docs/PR_REVIEW_CHECKPOINT_2026_10_13.md). PRs require real code review, **latest-head PR CI**, conflict checks and preservation of useful parallel work. Synthetic method checks cannot certify GitHub-source authenticity, independent human review, package safety or lifecycle energy findings. The test matrix covers Python 3.10/3.12/3.14 with official immutable SHA-pinned actions; only verified tasks and observations can support scientific conclusions.

## October 2026: enterprise PR merge and research-artifact integrity

**[Enterprise PR policy](docs/PR_QUALITY_AND_MERGE_POLICY.md)** | **[Dated 45-PR audit and collision register](docs/PR_AUDIT_2026-10-13.md)** | [Issue #240](https://github.com/MSKazemi/github-trending-1000-study/issues/240)

The 2026-10-13 audit found many **draft PRs**, green head-only test checks, and multiple pairs modifying the **same company-intelligence evidence note**. Draft status, scientific human review, updated merge-tree CI and no-loss comparison are independent merge gates; a green badge alone is **not** sufficient.

The CI suite now tests Python 3.10/3.12/3.13/3.14 compilation and regressions plus a separate read-only research artifact integrity check. Locally:

```bash
python -m compileall -q trending_study scripts tests
python -m unittest discover -s tests -v
python scripts/check_research_artifacts.py --root .
```

The integrity check rejects corrupt JSON/JSONL/CSV, duplicate keys and nonfinite constants; it **does not** validate factual sources, rights, human approval, empirical results or permitted access. See the PR policy for reviewer and branch-protection requirements. These are proposed contributor/repository engineering controls, **not** completion of scientific study prerequisites.
