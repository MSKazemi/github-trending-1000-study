# Crosswalk for energy instruments — technical integration review (2026-10-13)

**Scope:** a synthetic **one-use** arithmetic consistency check for two existing offline research instruments. No independently accepted real user task, consented participant, actual energy meter, CO2e estimate, approved lifecycle boundary or green-savings result is introduced. This is a follow-up to [issue #18](https://github.com/MSKazemi/github-trending-1000-study/issues/18) and the code added by [PR #214](https://github.com/MSKazemi/github-trending-1000-study/pull/214).

## Canonical responsibilities — avoid interpreting two tools as two empirical studies

- [`trending_study.lifecycle_break_even`](../trending_study/lifecycle_break_even.py) is the **canonical n-use signed energy break-even scenario**. It models declared pre-run terms and per-use runtime on a reproducible synthetic or self-reported basis, with unknown terms failing closed. Use this for prospective break-even curves, not carbon conclusions.
- [`trending_study.energy_boundary`](../trending_study/energy_boundary.py) is a **component-level input completeness and acceptance guard** for a single matched accepted task. Its optional `grid_only_scenario_gco2e_delta` is limited to the declared local/CI/runtime/maintenance electricity assumptions. Its `net_gco2e_reuse_minus_build` remains null without component-specific carbon provenance.
- Neither source authenticates meters, cloud inference, equivalent functional acceptance, reviewer independence or attribution; both need independently verified upstream assumptions.

## Exact one-use crosswalk (synthetic scenario only)

| Component-level term | Canonical break-even term |
|---|---|
| `local_development + model_inference` | `pre_run.development` |
| `ci` | `pre_run.verification` |
| `maintenance` | `pre_run.maintenance` |
| `embodied + upstream_support` | `pre_run.other` |
| `runtime` for **one accepted use** | `runtime_per_use` |
| none in this example | `pre_run.discovery = 0` **only as a synthetic declared assumption** |

The signed outputs intentionally have **opposite conventions**: component-level `reuse − build` versus lifecycle-model `build − reuse`. The test asserts numerical agreement after a sign reversal and validates that an unknown included energy term blocks both point comparisons. It also checks the component guard refuses the comparison if either version of the fixed task was not accepted.

```bash
python -m unittest tests.test_energy_model_crosswalk -v
python -m unittest discover -s tests -v
```

## Limitations and next decision

The crosswalk above is **not** a general production adapter. It assumes one accepted use, equal horizon, consistent source units and that categories have been allocated exactly once. For multi-use comparisons, deployment/workload-dependent runtime and maintenance, real upstream effort, provider inference allocations, regional/time grid intensity, embodied effects, uncertainty and rebound must be separately defined. Avoid silently mapping maintainer *minutes* to kWh.

Long term, prefer one documented aggregate energy calculation with a separately versioned component-entry schema, rather than two independent public calculators. Preserve the useful tests and schema fields from both implementations; do not remove either until a migration plan, parity suite and downstream interface inventory are complete.

**Practical lesson:** reuse and reconcile preexisting analysis tools before generating another calculator. An exact arithmetic test reduces accidental contradictory outputs, but only a matched, independently accepted task and valid physical boundary could support an actual green-software claim.
