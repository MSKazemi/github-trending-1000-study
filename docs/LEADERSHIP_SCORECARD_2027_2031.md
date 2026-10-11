# A scorecard for professors, CEOs, CTOs and open-source maintainers

**Status:** measurement contract, not an actual performance dashboard. As of 2026-10-11, no prospective repo cohort and no validated human/energy trial results exist. **Avoid a fabricated 0% progress metric** for observations not collected.

## Why a balanced dashboard matters
A high-performing research program might publish a negative result (reuse-first harms some workflows) and still succeed scientifically. A highly starred code repository may be unfit for a specific task. A niche OSS component with quiet verified integration may create substantial value with few downloads. The dashboard tracks **four orthogonal dimensions**, plus safety and evidence fidelity; it does not reduce them to one composite number.

| ID | Intended measurement | Unit/denominator | Collection and validation | Decision consequence |
|---|---|---|---|---|
| K1 | **Independently accepted user task outcomes** | successes / all eligible attempts by task and project type | fixed spec, independent blind review, actual attempts incl failed/abandoned | primary useful result, requires quality gate |
| K2 | **Accepted outcomes per complete human-active hour** | K1 accepted count / all developer-active hours, retries/support included | consented time log and concurrency reconciliation | compare workflows; missing hours mean uncertain estimate |
| K3 | **Safe task-relevant reuse opportunity coverage** | tasks with >=1 independently judged viable component / all prospectively sampled tasks | diverse candidate pool, exact versions, adjudication, missingness | quantify avoidable reinvention *within frame* |
| K4 | **Discovery precision@5 and judged coverage** | adjudicated safe viable top-5 / returned candidates, separate unjudged | task-to-component independent gold pool; bounds for unjudged | select retrieval tool; no absolute recall claim |
| K5 | **Independent downstream reuse/retention** | verified integration/repeat use / applicable consented cohort | opted-in user workflow or reproducible dependency trace | measure ongoing utility, not stars |
| K6 | **Security/rights/compatibility gate failures** | severity and frequency per **all** candidate recommendations | OSV/SLSA/SPDX/OSPS plus human verification | unacceptable findings can veto reuse despite speed |
| K7 | **Lifetime maintenance + upstream human cost** | 30/90/180d defect repair, security/upgrade, maintainer support time per accepted task | consenting task+upstream logs, separate observed and unknown | assess shifted cost and durable value |
| K8 | **Device/CI/provider energy** | measured/estimated/unknown kWh per accepted equivalent task | calibrated telemetry, provider scope statement and CI/index logs | constrain green claims and compare net boundaries |
| K9 | **SCI and absolute footprint** | gCO2e per verified user functional unit AND total project/workload, plus water where feasible | time/location grid intensity, embodied allocation, rebound; uncertainty | veto unsupported carbon claims; evaluate break-even |
| K10 | **Research evidence fidelity** | #registered hypotheses, validated cohorts, preregistered deviations, released nulls/replications | dated signed protocol, reviewer register, data rights | should dominate reputation/citation targets |
| K11 | **Maintainer and newcomer experience** | reviewer minutes, independent install/fix success, support burden per cohort | task timing/qualitative audit, no individual shame ranking | prevent shifting burden upstream |
| K12 | **Attention and dissemination** | Trending appearances and stars (secondary descriptive only) | timestamped page/official APIs | inform discovery, never define useful value |

### Role-based interpretation
- **Professor:** K1, K3, K4, K10 and inference validity before a broad academic claim.
- **CEO:** verified repeat value K5, workflow cost K2/K7 and willingness to choose this solution over existing alternatives.
- **CTO:** K1/K6/K7 reliability, security, provenance, rollback and engineer comprehension.
- **Sustainability chair:** K8/K9 with consistent functional unit/known coverage and explicit rebound.
- **OSS maintainer:** K7/K11 and reciprocal upstream contribution.
- **Your personal AI-coding portfolio:** K1/K2/K3/K6/K7 first; K8/K9 when instrumentable; do not optimize K12 alone.

## Quality gates and practical stop rules (not validated numeric thresholds)
- **Stop before integration:** nonexistent/wrong package identity, materially incompatible license, known unmitigated unacceptable security issue, task acceptance failure.
- **Stop before 'carbon saved' claim:** incomparable functional units, missing provider/cloud boundary presented as full total, fixed per-token coefficients without calibration, no sensitivity to runtime/horizon.
- **Stop before broad best-practice claim:** no independent comparison, unknown all-task denominator, model-only labels, unbounded retrieval-pool recall or unexplained temporal attrition.
- **Pivot rather than sink more development effort:** no plausible independent user value after an appropriate declared pilot, best existing tool passes acceptance at lower net cost, or agent search consumes more than saved work.
- **Do not automatically archive a research/educational project** whose scientific or learning objective (not commercial adoption) was independently met.

## Quarterly report template fields
Quarter/year; changes in tools/model versions; observation cohort Ns; actual versus planned enrollment; missingness; outcomes K1–K12 (raw numerator/denominator, CI where defensible); incidents and limitations; what failed; what was reproduced; stakeholder disagreement; budget spent/unknown; stop/pivot/continue; next falsifiable milestone; source dates and version hashes.

See [template](../templates/quarterly_advisory_review.md). Reporting may contain "not measured", never pretend 0 when uncollected.
