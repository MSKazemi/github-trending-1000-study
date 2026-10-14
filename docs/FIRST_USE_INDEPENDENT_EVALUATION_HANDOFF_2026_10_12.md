# Independent first-use evaluation handoff — U01 (review packet; no results)

**Prepared:** 2026-10-12. **Scope:** one bounded pilot engineering task ([issue #83](https://github.com/MSKazemi/github-trending-1000-study/issues/83), [first-use dry-run specification](FIRST_USE_REUSE_PILOT_2026_10_12.md)). **State:** `NOT_APPROVED_NOT_ENROLLED`. This is a practical packet *for future independent human review*. **No reviewer, participant, independent hidden test, ethics permission, experimental result or actual energy saving is claimed.** The associated internal CI fixture remains synthetic.

## Decision to make

**Can a developer unfamiliar with the repository successfully obtain a ranked, explicitly *parse-only* JSONL report from a locally provided HTML file using public documentation, without coaching or new parser code?**

- **Assessment type:** narrow *first-use usability/reproducibility feasibility assessment* of the existing CLI, **not** a randomized reuse-vs-generation comparison and **not** live Trending page-recall validation.
- **Project:** [MSKazemi/github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study). Choose and record one immutable review-time commit, a fixed Python version and an isolated, network-disabled environment before the human attempt. The engineering design referenced baseline `4d524c460e6992f08fbc57118cdbd9962feb2098`; **do not silently replace that design baseline** with a later task outcome.
- **Comparable output:** source-listed order/rank, a `source_sha256` of input bytes, valid JSONL, honest timestamps and no false confirmatory eligibility. Never interpret the fixture's names as real observed GitHub activity.
- **Value of a negative result:** if first use fails, record the exact stopping point and improve onboarding/API documentation before investing in another parser. This is a practical local lesson, not a general causal effect.

## Five gates before **any** real user observation

| Gate | Independent evidence required | Current state |
|---|---|---|
| G1: source/task freeze | Task from a legitimate user need; repository commit, environment, accepted functional scope, first-use instructions and risks frozen *before* attempted use | **Pending**; only internal U01 dry-run task exists |
| G2: genuinely independent tests | A human unaffiliated with the implementing agent authors fresh positive and negative inputs and an inaccessible acceptance script; commits a secure SHA-256 of the private acceptance suite before task use | **Pending**; internal visible tests are not independent |
| G3: rights, privacy and human authorization | Source/input rights and data protection reviewed; if collecting people’s experiences for research/publication, prior ethics/consent clearance where applicable; safe opt-out, retention and access policy | **Pending**; do not enroll anyone through this file |
| G4: actual first-use attempt | Consenting eligible tester receives the scoped task and public instructions without private expected outputs, coaching, credentials or access to hidden tests | **Pending**; no participant or session |
| G5: independent outcome and cost audit | Reviewer checks full attempt incl failure/abandonment; records task success, version, UTC trace, human active time (only if legitimately collected), ambiguity and missingness. Second qualified reviewer or adjudication where needed | **Pending**; internal CI cannot substitute |

**STOP** if any required gate remains missing. A file with `approved: true`, matching reviewer labels or self-declared timestamps is **not proof** of independence/consent. Preserve the authentic source documents and approval in access-controlled custody, not as unverified public attestations.

## Task statement given to a future consenting tester (do not reveal hidden outputs)

> You have a **local saved HTML file** and a clean copy of this public Python repository. Using its documented interfaces and without downloading external packages, produce a machine-readable list of the repositories displayed in the saved file in their source order, with provenance fields adequate to detect changes to the file. Confirm what the output can and cannot establish about original GitHub page capture. Do not contact GitHub, modify the fixture, use a live token, or rewrite the parser. Report any unclear documentation or point at which you cannot proceed.

The independent task/test author supplies an *authorized fresh local fixture* through a private review channel and writes positive/negative expected checks **before** the participant sees the task. The public `tests/fixtures/trending.html` and `tests/test_first_use_reuse_pilot.py` remain only an engineering smoke test; copying them into a "hidden" suite does not create genuine independence. Do not require the participant to install arbitrary candidate packages.

### Required acceptance checks (independent reviewer to freeze exact expected values privately)

1. The participant identifies an existing supported CLI workflow; `parse-trending` and `summarize` are candidate commands, **not mandatory prompt text**. If documentation hides them, record discoverability failure instead of coaching.
2. Positive fixture: all **supported** `article.Box-row` entries appear once, source order/rank preserved, no off-row footer link counted; compare against the reviewer’s own full-page manual annotation.
3. SHA of actual local file bytes matches each output `source_sha256`; file unchanged; `parsed_at_utc` must reflect parsing rather than historical page capture.
4. All parsed rows explicitly retain `capture_time_status=unverified_parse_only`, `eligible_for_confirmatory_cohort=false`. Supplied `--date` must **not** be interpreted as a verified capture timestamp.
5. A malformed supported row must produce nonzero failure without partial published output; repeating the same destination must refuse overwrite and preserve existing bytes.
6. Summarize occurrence/name counts *without* saying displayed names are immutable repository IDs; report correct counts and uncertainty.
7. Record observable setup friction, failed commands, attempted shortcuts, use of an agent if allowed, and reviewer-observed deviations. Do **not** use agent-generated acceptance outputs as hidden gold.

If actual GitHub-origin row completeness is the goal, switch to the **separate** [independent 30-real-row page-QA method](INDEPENDENT_PAGE_AUDIT_2026_10_12.md). The U01 synthetic fixture is not a substitute.

## Roles and custody — independent people only, if actually recruited

| Role | Responsibility | Must be withheld from |
|---|---|---|
| Task/sample steward | Record selection without filtering by known reusable solutions, baseline UTC, inclusion/exclusion and permits | Intervention outcomes and solved candidates at sample time |
| Independent acceptance author | Write/freeze hidden tests, exact source fixture and negative checks; store acceptance SHA securely; establish criterion-level scoring | Evaluated agent's prompts/context and solution patches |
| First-use tester | Attempt original task using only allowed public documentation/tools; can refuse/stop safely | Hidden answer/test suite and post-hoc hints |
| Outcome assessor | Reproduce output in isolation, inspect logs and negative cases; check rights/security; record uncertainty | Assigned workflow where feasible, previous reviewer conclusions |
| Privacy/methods steward | Verify actual consent, retention, approval, denominator, preregistration if estimating causal effects | Public release of participant identities or raw confidential prompts |

**No names or approvals are recorded here.** Do not send packets, invite participants or share restricted access without explicit authorization and verified recipient permissions.

## What to record, without making up outcomes

Use existing versioned project artifacts instead of a new data platform:

- **Task origin and eligibility:** [`templates/feasibility_task_review_card.md`](../templates/feasibility_task_review_card.md) for each independently sourced task, with original timestamp, source rights and `reuse_opportunity=unknown` at intake. U01 is *selected because prior code is known*; exclude it from estimation of general reuse-first benefit.
- **Any human comparison:** [`templates/experiment_registration.md`](../templates/experiment_registration.md), [`templates/protocol_signoff.md`](../templates/protocol_signoff.md) and [`docs/TRIAL_PILOT_INSTRUMENT.md`](TRIAL_PILOT_INSTRUMENT.md). Freeze independent task/acceptance hashes before allocation; use existing `trending_study.trial` for **permitted and appropriately authorized** assignment/outcome auditing, not U01 alone.
- **Actual candidate verification:** [blinded task-to-component review workflow](BLINDED_REUSE_REVIEW_WORKFLOW.md) / existing `trending_study.blind_review`; two actually independent humans; exact version, available-at-baseline, license, security, functional acceptance and maintainer burden; unknown must remain unknown.
- **Write-once trace/log:** securely retain actual environment version and commit, timestamped task/start/stop/attempts, accepted criteria, failures/refusals, active human minutes where permission exists, reviewer disagreement, inaccessible information and loss/withdrawal. Store private identifiable material outside public repository. **Missing values remain null/unknown, not zero.**
- **Environmental accounting:** only report locally/CI **metered** energy with a declared boundary; opaque provider inference and 30/90/180-day downstream burdens remain missing until observed. Do not convert tokens into avoided CO2.

### One-session evaluator worksheet (blank, not a result)

| Field | Value to be entered by real reviewer |
|---|---|
| Task ID and frozen frame link / SHA | **NOT RECORDED** |
| Task sampling and first-availability baseline UTC | **NOT RECORDED** |
| Reviewer-authored criteria/test suite private SHA and lock UTC | **NOT RECORDED** |
| Genuine review/consent/privacy clearance | **NOT RECORDED** |
| Exact repository commit, Python/toolchain/runtime OS | **NOT RECORDED** |
| Tester eligibility and consent reference (pseudonymous) | **NOT RECORDED** |
| Task start/stop, abandoned/failure status, command log | **NOT RECORDED** |
| Criterion-level independently accepted / rejected / unknown | **NOT RECORDED** |
| Human minutes, token/provider coverage, other missingness | **NOT MEASURED** |
| Reviewer disagreement/adjudication and explicit limits | **NOT RECORDED** |
| Reused component license/security/maintenance suitability | **UNKNOWN** |
| Actual user adoption, follow-up, metered energy/CO2e | **NOT OBSERVED** |

**Reporting rule:** until all required gates are genuinely satisfied, label any external report **"protocol/readiness only, no human first-use results"**. After one consented first-use attempt, report *one narrow usability observation*, not a generalizable effect size. A controlled reuse-vs-ordinary workflow comparison requires an independently sampled multi-task frame, actual consenting developers, predeclared ITT outcome, ethics approval where applicable, and statistical power analysis; see [#21](https://github.com/MSKazemi/github-trending-1000-study/issues/21) and [#25](https://github.com/MSKazemi/github-trending-1000-study/issues/25).

## Maintainer action after a genuine observation

If independent first use fails: improve command discoverability, documentation, clean-install reproducibility, output/error explanation or API stability **only where the evidence points**. If it succeeds: test a different task and another user rather than claiming universal adoption. In both cases track review effort, changes to upstream dependencies, accessibility, possible new vulnerabilities, and 30/90-day burden before presenting a "green coding" benefit.

**No new parsing engine, new score, new reviewer validator, recruited person, hidden test or claimed saving is created by this handoff.** The central engineering choice remains to reuse the existing, well-bounded CLI until a real independently verified problem justifies a new implementation.
