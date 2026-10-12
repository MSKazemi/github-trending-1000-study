# Start-of-study checkpoint — 2026-10-12

**Requested action:** turn earlier guidance to begin the 2027 sustainability/reuse study into concrete, reproducible work in [MSKazemi/github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study). This note summarizes the research decision and actual implementation state. It is **not** observed user/developer data or peer-reviewed research.

## What was found before changes

- The repository already contained extensive protocol, selection, ethics, agent adoption, gold-standard, lifecycle, five-year and critical-gap documents, plus synthetic offline `reuse_gate`, `goldset`, `value_gate` validation tools.
- The README explicitly said no 1,000-repository empirical cohort, opt-in task experiment or verified carbon savings existed. The open issue [#25](https://github.com/MSKazemi/github-trending-1000-study/issues/25) called for all-task, leakage-resistant randomized inference. At inspection there were no open PRs, and #25 had no comments.
- Remaining urgent work was to **operationalize a complete prospective task frame and reproducible allocation**; collecting 1,000 Trending repositories first would not resolve whether suitable existing code should be reused.

## Concrete decision

The 2027 core falsifiable question remains: **Across all prospectively selected user tasks, does a documented reuse-first workflow improve independently accepted functionality per complete human effort, without worse rights, security or net lifecycle costs?** GitHub Trending is a separate attention/exposure cohort, not the primary measure of software usefulness or waste.

**Priorities:** (1) freeze task/source/acceptance evidence; (2) review no-solution/unknown opportunity and provenance; (3) randomize before observing outcomes; (4) report failures, no-opportunity, refusals and missing costs; (5) independently validate functional/legal/security outcomes; (6) measure energy only with an honest declared boundary; (7) audit real sources, permission and bias before expanding N.

The proposed frame uses a fixed 2×2 human/agent × ordinary/reuse-first allocation consistent with the existing repo protocol. An agent-only three-way exploratory design (ordinary, local-reuse-first, ecosystem-reuse-first) remains an interesting **separate** pilot comparison, not silently folded into this preregistered candidate. Approval is required before deciding which trial is primary.

## This implementation (bounded slice of #25)

- `trending_study/trial.py`: strict frame/consent-schema checks, deterministic block/cluster allocation and audit of all assigned tasks, missing time and incomplete outcomes. No network calls or untrusted software execution.
- `examples/trial_frame.synthetic.json` and `examples/trial_outcomes.synthetic.json`: fictional instrument fixtures only, including a prespecified exclusion and an explicitly unsuccessful/missing/pending/refused mix.
- `tests/test_trial.py`: deterministic assignment, leakage, eligibility, time/consent/rights gates, tamper detection, missing data, and CLI round-trip checks.
- `docs/TRIAL_PILOT_INSTRUMENT.md`: exact schema, commands, evidence requirements and limitations.

**Local execution evidence:** the 13 new synthetic unit tests passed in a Python 3.13 environment before PR submission. Full repository CI on the PR is needed to cover the existing suite and supported Python 3.10/3.12 matrix. Synthetic per-arm accepted counts and human minutes are **fabricated fixture values**, not performance or energy results.

## NOT completed; do not mark #25 closed

Human review and preregistration; real task sourcing and independent hidden acceptance suites; access/consent approvals; independent reuse-opportunity gold labels; power simulation; actual pilot recruitment/execution; blind correctness and rights/security review; measured kWh/CI/inference boundary; whole-lifecycle follow-ups; real statistical effects. The suggested 30–50 task pilot is a planning example only and **not** a fixed statistical N.

## Next gate

Have an independent methods/statistics and privacy reviewer verify [#25](https://github.com/MSKazemi/github-trending-1000-study/issues/25), the separate observational versus randomized population, the ITT estimand, sampling lock and consent regime. Then time-stamp an approved task frame, pilot a small number of real eligible tasks under explicit permission, capture a complete dropout/unknowns ledger and quantify feasibility. Do not auto-merge methodology amendments without human review.
