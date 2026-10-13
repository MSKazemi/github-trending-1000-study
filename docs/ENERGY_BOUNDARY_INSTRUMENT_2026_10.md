# Matched-task energy boundary and missingness guard: issue #18

**2026-10-12. Status: preliminary modeling instrument; no calibrated meters, no provider telemetry, no benchmark and no observed CO2e savings.** Partial response to [#18](https://github.com/MSKazemi/github-trending-1000-study/issues/18); complements [full lifecycle model](FULL_LIFECYCLE_BREAK_EVEN_2027.md).

## How to use

```bash
python -m trending_study.energy_boundary --input MY_BOUNDARY.json
python -m unittest discover -s tests -p 'test_energy_boundary.py' -v
```

Supply one frozen functional unit (`task_id`, `horizon_days`, `boundary_description`, and **independently assessed** `reuse_task_accepted` and `build_task_accepted`) plus `arms.reuse` and `arms.build`. Each must account for `local_development`, `ci`, `model_inference`, `runtime`, `maintenance`, `embodied` and `upstream_support`. Declare every component as **measured**, **modeled** or **unavailable**. Known values need a `source_ref` and finite nonnegative `kwh`. Unknown values require `kwh: null`; arbitrary tokens cannot be used as electricity.

The tool reports signed `reuse − build` energy only when both task outputs are accepted and **all declared component slots have non-missing estimates**. If any term is unavailable, the net is null; no 'zero missing energy' assumption. Optional `grid_intensity_gco2e_per_kwh` produces **only** `grid_only_scenario_gco2e_delta`, a single-intensity *illustration* for local development, CI, runtime and maintenance electricity. It **excludes** cloud model inference, embodied resource production and upstream support; `net_gco2e_reuse_minus_build` remains null because component-specific carbon provenance is missing. The output always declares the boundary self-reported. It is *not* an ISO/IEC SCI certification or proof of reductions.

## Calibrating a real experiment (not yet conducted)

1. Freeze equivalent accepted functionality, workload volume, hardware/region, observation and maintenance horizon, permitted reuse alternatives, randomization and security constraints.
2. Calibrate local joules via reference load and idle subtraction, instrument CI/build energy, document power and temperature uncertainty and meter calibration date.
3. Identify hosting/model inference per API request or disclose opaque estimates, cached requests, batch rework and failed search attempts separately; no universal token-to-kWh constant.
4. Include runtime/dependency update effects and upstream maintainer support. Allocate embodied hardware and external infrastructure with defensible assumptions; otherwise label coverage partial.
5. Report ranges for grid intensity by region/time, uncertainties, rebound/adoption changes and break-even workload sensitivity; use negative/null results. **Do not advertise net carbon benefit from a single best-case arithmetic result.**

## Practical maintainer experiment

Use one independently reviewed code task with an existing library candidate and a new-code baseline; record *all* time, installation failures and ongoing maintenance. A smaller prompt or fewer generated lines is not the functional unit. If input energy, security or performance cannot be measured, publish those gaps instead of claiming a green win.

This work is an instrument for later independent energy study, not evidence that AI assistance is energetically cheaper.

**Validation contract:** the optional grid-intensity field must be numeric, finite and nonnegative **even when a task was not accepted**. A task failure must not become a bypass for malformed evidence. The model still reports no comparative net kWh or carbon benefit for unaccepted tasks; the regression suite covers this failure path.


## 2026-10-13 validation and SCI boundary caveat

Change: `energy_boundary.compare()` validates **all seven declared components for both comparison arms even when one arm's user task was not accepted**. Previously, early return on a rejected task could bypass malformed energy evidence. The report explicitly distinguishes `incomplete_boundary`, `mixed_modeled_scenario_only`, and `all_components_self_reported_measured_not_authenticated`. A complete *declared* boundary with modeled terms is not fully metered energy.

**Functional unit:** independently accepted same task and service level, pinned hardware/model/configuration, usage count and 90-day follow-up horizon (or a justified alternative). Predeclare which measured versus modeled terms are inside the boundary, use idle-power subtraction and calibration uncertainty for local/CI measurements, and separately disclose provider inference unavailable rather than equate tokens with kWh. `upstream_support` is only energy if attributable hardware energy was actually estimated or measured; **human minutes belong to issue #24** and are not automatically kWh. Check source SHA, sampling, caching/region/time intensity, embodied impacts and rebound before total lifecycle claims.

**Scientific anchor:** [ISO/IEC 21031:2024 Software Carbon Intensity](https://www.iso.org/standard/86612.html) establishes an SCI methodology, not a certified carbon result from this partial scenario. `grid_only_scenario_gco2e_delta` excludes inference/embodied and other terms; `net_gco2e_reuse_minus_build` remains null. State every omitted term and measurement calibration; no universal per-token emissions multiplier.

**Practical repository experiment:** on one reusable CLI integration, compare equivalent accepted outputs, account for CI plus downstream maintenance and upstream review, and report unknown cloud energy explicitly; do not claim a green saving from shorter code.
