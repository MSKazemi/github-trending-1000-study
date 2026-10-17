# Issue #24 — opt-in maintainer burden and newcomer comprehension feasibility pilot

**State (2026-10-17): DESIGN / NOT AUTHORIZED FOR RECRUITMENT.** This is a prospective, reviewable protocol proposal, **not** an ethics approval, participant consent, preregistration, observed pilot, randomized experiment, or actual verified result. No human participants were contacted or enrolled by this work. Owner and independent methods/privacy/ethics reviewers must authorize it before any live use.

## Research question and study unit

Can an opt-in study *feasibly* record the downstream and upstream human effort of a software reuse attempt, the proportion of independently actionable contributions, and whether a fresh developer can understand/repair a bounded task at baseline and follow-up?

This first stage is a **descriptive, nonrandomized feasibility pilot**. The unit is a frozen, independently accepted **task/contribution case**, nested in consenting projects/maintainers; analyses must show both case and project counts. Recruitment is a nonprobability opt-in convenience sample, **not representative** of all OSS maintainers. No causal or population-generalizable “agents increase burden” effect can be inferred. If a future treatment experiment is proposed, freeze design, task sampling, power and an independent preregistration *before* assignment.

## Prospective gates (all must be recorded before any real collection)

1. Assign a responsible study owner, independent methods reviewer, privacy/ethics reviewer and, where applicable, an institutional ethics committee and GDPR controller/DPO. Obtain **recorded approvals**, not self-reported JSON flags. Seek legal advice on data-processing basis and retention. Research-participation agreement is distinct from the GDPR legal basis for processing.
2. Approve a complete participant information notice, purpose-specific voluntary participation and data processing notices, withdrawal process, access/retention/deletion windows, storage location, breach procedures and contact route **outside this public repository**. No individual names, handles, emails, IP addresses, work logs, raw text or signed consent in GitHub. Keep the reidentification key outside public Git with restricted access.
3. Recruit only willing adult OSS maintainers/newcomers through an opt-in channel **after** approval. No unsolicited agent-created issues/PRs, experiments on nonparticipants or covert monitoring. Refusal and withdrawal must not have consequences.
4. Freeze inclusion/exclusion criteria, task rubric, outcome states, negative acceptance tests and stop rules before inspecting results. Predeclare which project/maintainer/task strata can be matched and the treatment/selection biases that remain.
5. Obtain permission from maintainers/rights holders to inspect relevant repositories and artifacts. Use local isolated copies and dummy credentials; no production mutations or live third-party participant telemetry.
6. Freeze an initial *feasibility* recruitment target (planning discussion: up to 8–12 consenting projects/maintainers, subject to independent review). The target is **not** a power-based sample size. Review feasibility precision, variance and retention first; power a future hypothesis study separately.
7. Independent safety/privacy review must approve disclosure thresholds for potentially identifiable small cells before a report can be published.

## Frozen task, acceptance and reviewer rubric

Each candidate gets a nonidentifying task code, project pseudonym, frozen source commit, task-spec SHA-256, acceptance-suite SHA-256, UTC eligibility snapshot and exclusions **before** work begins. Retain cases that fail or become unavailable in the attrition ledger; do not cherry-pick successes.

The actionable-contribution reviewer should not be the agent/code author. A prespecified **pass** requires a reproducible specific problem, concrete useful proposed change, appropriate scope, no disqualifying safety/license blocker, and independently checked acceptance tests/evidence. **Fail** indicates an independent, documented negative adjudication (e.g. unneeded duplicate, broken behavior, unsafe proposal). **Unknown** includes insufficient evidence and disagreement. Reviewers independently code before seeing one another's decision; unresolved disagreement stays unknown until documented adjudication. Rater calibration uses separate fictional practice tasks, not the analysis set.

A consenting newcomer receives a standardized repository overview (same time, material and environment for comparability), then a bounded *safe sandbox* comprehension/repair exercise independent of any agent author's hidden tests. Pilot the rubric for clarity. Suggested pass conditions for reviewer approval: identify key assumptions/risks, locate the relevant test/code, explain observed behavior and pass a frozen acceptance check within a prespecified time box; **fail** is a genuine attempted but unsuccessful assessed task; **unknown** means no assessable task/consent, unclear result or unavailable independent assessor. Record actual time-to-fix privately with uncertainty, not in source code.

## Minimum measurement plan

- Time boundary: separately record upstream review/support and downstream search/implementation/review-repair/follow-up active **minutes** for the same case and observation horizon. Count failed/rejected attempts and follow-up support, not just shipped changes. Distinguish human-active time from wall/agent waiting; overlapping intervals must not be double counted. Calibrate a volunteer's time diary/timer against independent, consented timing for a small subsample; record disagreements, interruptions, and missingness.
- The existing `trending_study.maintainer_burden` offline v0.1 instrument accepts **only** a bounded, pseudonymized six-category summary. `null` means unknown, **never 0**. `consent_state` is self-declared metadata; it does not authenticate approval.
- Outcome codes proposed for the descriptive feasibility report: actionability and newcomer comprehension = `pass/fail/unknown`; 30- and 90-day follow-up = `completed/missing/not_started/unknown`; incident = `yes/no/unknown`. An explicit failure is **not** missing, and `not_started` is **not** attrition. These statuses describe respondent/reviewer-entered codes and are not independently authenticated by software.
- Follow-up windows (proposal for reviewer decision): 30 ± 7 days and 90 ± 14 days after task closure. Mark events not yet due as `not_started`; missing despite being due as `missing`; unavailable source as `unknown`. Censor withdrawals; retain only minimal denominator state as legally approved. Do not backfill successes.
- Keep opt-in/refusal/withdrawal and all initially screened/assigned *denominators* outside public Git; publish only privacy-reviewed aggregates. Link project/task outcomes through controlled pseudonymous identifiers and encrypted access, not public usernames. Instrument's current counters are **internal unapproved descriptive output** and may be unsafe to publish for very small samples.
- Separately collect protocol deviations, zero-incident reports, negative cases, no-success cases, and missing category reasons. The pilot must report unresolved disagreements and protocol violations, not “fix” them by dropping rows.

## Analysis and no-claim guard

Before reading actual data, document invited/eligible/declined/consented/withdrawn projects and participant counts, total screened/accepted/rejected/unknown tasks, task and follow-up attrition, full six-category coverage and the number requiring adjudication. Report **both numerator and denominator** for any descriptive proportion, explicitly label it unverified if external signoff is missing, and avoid reporting potentially identifying small strata.

Predeclare feasibility outcomes: recruitment/consent rate (invited denominator if authorized), complete time-diary fraction (all eligible cases), independent review agreement and disagreements, and retention at 30/90 days (eligible/due denominators). Report distributions (median/range and small-sample uncertainty where defensible) rather than treating sums or a single individual's time as population estimates. Treat unknown/missing separately from negative. A null total is the only appropriate “result” when required parts are unavailable.

**No statistical efficacy/causal comparison, no maintainer ranking, no energy/carbon savings claim.** Future comparative claims require matched tasks and baseline, randomization or defensible confounding analysis, independent acceptance, calibration, power assessment and preregistered estimands.

## Software and synthetic-only rehearsal

- `python -m trending_study.maintainer_burden --input examples/maintainer_externality.synthetic.json`
- `python -m trending_study.maintainer_burden --input examples/maintainer_feasibility_batch.synthetic.json`
- `python -m unittest tests.test_maintainer_burden -v`

The batch example is deliberately fictional and illustrates pass **and fail**, never-observed cases, missing follow-ups and separate known upstream/downstream **partial** minute totals. Reports label outcomes `self_reported_not_authenticated`, set `independent_review_authenticated=false` and `approved_for_public_release=false`, and omit a per-accepted-task point estimate. No publication authorization is implied by a successful command.

## Final closure acceptance (all external to this engineering PR)

- [ ] Authenticated independent methods and ethics/privacy approvals; repository-safe retention and rights record
- [ ] Consented opt-in study with a dated actual recruitment/eligibility denominator and withdrawal log
- [ ] Real independently frozen task and acceptance evidence; separate independent actionability/comprehension grading, disagreement/adjudication log
- [ ] Authenticated human effort measurements with calibration/uncertainty and explicit unsuccessful-task costs
- [ ] Completed or appropriately censored 30/90-day follow-up with missingness and null/negative outcomes retained
- [ ] Independently reviewed, nonidentifying pilot aggregate report with limitations and sample-size/power caveats; release authorization recorded *outside the input ledger*
- [ ] Qualified independent signoff on any interpretation, and final change-review and post-merge CI

**If recruitment is impossible, report “pilot not executed; effects not estimable” with reasons and request independent scientific approval of a revised scope; never fabricate participants or close #24 as empirically complete.**

## External reporting/rights reference points

- [STROBE observational reporting checklists](https://www.strobe-statement.org/checklists/) — useful reporting guardrails for nonrandomized descriptions; not scientific approval.
- [CONSORT pilot extension](https://www.equator-network.org/reporting-guidelines/consort-2010-statement-extension-to-randomised-pilot-and-feasibility-trials/) — relevant only if a later randomized pilot is truly conducted; **not** a checklist that certifies this observational proposal.
- [European Commission: legal bases, consent and withdrawal](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/legal-grounds-processing-data_en) — seek expert case-specific GDPR guidance before processing personal information.
- [EDPB Guidelines 1/2026 scientific research consultation](https://www.edpb.europa.eu/public-consultations/guidelines-12026-on-processing-of-personal-data-for-scientific-research_it) — a consultation resource, not evidence of final issued guidance or ethics approval.

**Practical lesson for other repositories:** privacy-sensitive studies need both fail-closed code and genuinely external human authorization. A green test cannot turn self-reported “approved” into consent or convert synthetics into an observed environmental/social impact.


## Follow-up: all-missing human effort must remain null (2026-10-17)

A review of the overlapping draft PR #436 and this feasibility instrument found that initialized numerical accumulators previously reported `0.0` for a wholly missing six-category time diary. The feasibility addition also reported `0.0` for a direction (upstream or downstream) even when that entire side had **no observed entries**. The code now counts observed component entries overall and per direction, emits `null` for every wholly unobserved subtotal, and reports `0.0` **only where a zero was actually recorded**. Synthetic tests check all-missing, observed zero on each side, and a multi-case partially missing batch. This prevents false assertions that unseen upstream maintainer effort was zero. These fields remain diagnostic, **not** independently authenticated human labor or permission to publish data. All earlier negative/unknown outcome handling is retained.

**Maintainer lesson:** missing-as-zero can be reintroduced by later grouping logic even after it is fixed in a global total. Test the empty set at *every aggregation level* before interpreting costs.
