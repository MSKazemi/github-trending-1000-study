# When does reuse actually save human effort and environmental resources?

**Status:** preregistration candidate and model; no measured kWh, token savings or carbon benefit claimed.

## Design the right alternatives
For one frozen functional task, compare feasible real options:
- **N0: do not build** (existing workflow or scope reduction), when it meets the user's need.
- **R: reuse/adapt** existing component with license/security/integration obligations.
- **U: improve upstream** or compose existing modules.
- **B: new bounded implementation**.
The primary contrast for a randomized reuse-first study is **assigned workflow**, with actual chosen strategy as a mediating behavior/outcome, not an after-the-fact treatment label. Do not exclude failures, abandoned work or discovery-only work.

## Whole-life cost equation and break-even
For strategy s, functional workload count n, observation horizon H and predeclared boundary:

    E_s(n,H) = E_discovery,s + E_development,s + E_verification,s
               + E_maintenance,s(H) + n * E_runtime,s + E_other,s(H)

Similarly report human work minutes (including upstream and downstream externalities where observable), direct cost, water impact and lifecycle carbon. For carbon, **do not** multiply overall kWh by a single intensity if activity spans grids/times; use time/location terms and embodied hardware allocation.

Define **signed net energy benefit of R relative to B** as

    Delta_E(n,H) = E_B(n,H) - E_R(n,H)

Positive means reuse consumes less measured/modeled boundary energy at the same functionality. Negative means build is better in that boundary. Report measurement/estimate intervals and missing provider-side terms.

If reuse has greater per-use runtime energy (E_runtime,R > E_runtime,B), and B has greater pre-run energy, then:

    n_break_even = (E_pre-run,B - E_pre-run,R)
                   / (E_runtime,R - E_runtime,B)

where pre-run includes discovery, development, verification, and the horizon's maintenance estimates. Only interpret if numerator and denominator are positive and assumptions hold. If the numerator is negative, reuse never saves at n=0; if denominator <=0 and reuse has lower pre-run energy, reuse dominates within the model. Perform scenario analysis over n, maintenance horizon, workload mix, security upgrades and hardware assumptions.

### Synthetic illustration ONLY (not observed)
Suppose B costs 12 kWh pre-run, R 4 kWh, but R uses 0.04 kWh per accepted task versus B 0.01 kWh. Then the *hypothetical* break-even is 8/0.03 ≈ 267 task executions; after more executions, the fresh implementation would consume less energy in this simplified boundary. Carbon and costs can have different thresholds, and cloud inference energy may be unknown. **Never call this an actual software saving.**

A [synthetic, fail-closed scenario CLI](LIFECYCLE_BREAK_EVEN_SCENARIO_CLI.md) and [test fixture](../examples/lifecycle_break_even.synthetic.json) exercise this arithmetic without any measured energy. Its exact integer workload crossover avoids rounding an equality threshold into a misleading action recommendation. **This is not protocol signoff or lifecycle calibration.**

## Costs beyond electricity
- **Energy (kWh):** metered or scope-defined modelled; calibrate local telemetry, CI, retrieval-index build, searches and inference. Unknown cloud internals ≠ 0.
- **Carbon (gCO2e):** [ISO SCI / SCI for AI](https://sci.greensoftware.foundation/), matched useful functional unit, grid intensity by region/time and embodied hardware allocation; distinguish allocation from marginal-avoided emissions (the latter needs a valid counterfactual).
- **Water (liters, location/time):** direct and indirect where measurable/modelled; a low-carbon grid can still have water impacts. Avoid a single universal water/tokens ratio.
- **Hardware/material and waste:** embodied emissions, devices replaced early, GPU/server age/utilization; don't pretend one amortization rule fits all providers.
- **Human opportunity cost:** total planning, prompting, review, retries, testing, search, integration and 30/90/180-day upkeep—including additional upstream maintainer work when realistically measurable.
- **Risk:** vulnerabilities, credential leaks, legal non-compliance, dependency abandonment and reliability regressions; use gating rather than balancing unacceptable risk against saved tokens.
- **Discovery overhead:** generating embeddings/indices or running repeated deep retrieval can be more expensive than the bounded tool task. Include amortized index creation and stop rules.

## Rebound and externalities
A cheaper tool may attract far more user executions, raising *total* system energy while lowering **intensity per accepted task**. Always report both. Reusing an upstream library may shift support load to its maintainers and may increase dependency-chain vulnerability exposure. Count or qualify where possible; do not assert a global reduction from one developer's local bill.

## Uncertainty and sensitivity
- Freeze full workload and environment (hardware, OS, provider, model/tool version, request types, tokens, time, source commit).
- Repeated matched trials with random task ordering and cold/warm cache sensitivity; calibrate sensor offsets and systematic uncertainty.
- Energy boundary matrix with source (metered/calibrated/modelled/unknown), inclusion decision and uncertainty distribution per term.
- Report signed Delta_E with uncertainty, task failure probability and H/n sweeps. Where server inference or manufacturing terms are unknown, label result **partial boundary**, not lifecycle total.
- Do not optimize one global score: engineering hours, functionality, security, water, carbon and reliability are incomparable without normative stakeholder-defined tradeoffs.

## Relevant external evidence
- [Green Software Foundation: Beyond Watts](https://greensoftware.foundation/articles/beyond-watts-what-should-ai-efficiency-really-measure/)
- [GSF: green software includes carbon, water, embodied hardware and waste](https://greensoftware.foundation/articles/revisiting-green-software-from-silicon-to-screen/)
- [Software Carbon Intensity specification](https://sci.greensoftware.foundation/)
- [2024 systematic review of industrial reuse cost/benefit measurement](https://doi.org/10.1016/j.infsof.2024.107451)


## 2026-10-16 bounded sensitivity envelopes — proposal for issue #23

The offline command `python -m trending_study.lifecycle_sensitivity --input examples/lifecycle_sensitivity.synthetic.json` reuses the existing `trending_study.lifecycle_break_even.evaluate` and computes the **minimum/maximum signed Delta E across explicitly supplied scenarios at the same workloads**. It does **not** estimate confidence intervals, fit parameter distributions, meter hardware or infer CO2e. The three fixtures are exclusively artificial.

**Comparator identity:** each supplied case must have the same functional unit, frozen task-spec and acceptance SHA-256, observation horizon H, boundary identifier, declared omissions, dataset kind, and precise sorted workload counts. Mixed incomparable tasks or boundaries fail closed rather than producing a misleading range. Only declared energy terms from the canonical original scenario are used.

**Missingness:** If any included energy term has `basis=unknown` in **any** case, all envelope results are null, the missing scenarios/terms are listed, and no favorable min/max is computed. Missing cloud inference/embodied/upstream/deployment inputs remain explicit boundary exclusions, **never** zero-valued measurements. The scenario envelope is not statistical uncertainty; a genuine uncertainty interval would need calibrated measurement/uncertainty inputs and a prespecified statistical method.

**Meaning of sign:** `delta_build_minus_reuse > 0` indicates reuse is lower only within that artificial comparison's *declared* energy boundary at the same independently accepted functional workload. A positive lower envelope means all included hypothetical scenarios favor reuse; ranges spanning zero are mixed/indeterminate. A claim about carbon, water or whole lifecycle needs time/region-specific energy/carbon factors, embodied allocations, rebound, whole service life and independently matched usage — not tokens-to-kWh guesses.

**Reproducibility:** `tests/test_lifecycle_sensitivity.py` tests three-workload sign conditions, rounding, mismatch/refusal and missingness against canonical decimal arithmetic. It does not claim source truth or a real pilot.

**Unmet issue #23 closure gates:** agree on a real accepted-task functional unit, authorization and energy capture boundaries, physically calibrate local/CI/serving meters with uncertainty, obtain actual independent paired workload observations and cloud-provider limitations, review upstream maintenance and sensitivity/rebound, and arrange qualified human methods review. No calibrated hardware channels were available in this implementation environment, so the measurement gate is **not** passed; #23 remains open.

**Practical repository owner lesson:** for Claude Code vs manual/reuse comparisons, capture human-active time and real task acceptance first. If no calibrated energy instrumentation or cloud inference data exist, report the bounds of what you **do not know** rather than promoting lower token counts as environmental savings.
