# Matched-task energy boundary and missingness guard: issue #18

**2026-10-12. Status: preliminary modeling instrument; no calibrated meters, no provider telemetry, no benchmark and no observed CO2e savings.** Partial response to [#18](https://github.com/MSKazemi/github-trending-1000-study/issues/18); complements [full lifecycle model](FULL_LIFECYCLE_BREAK_EVEN_2027.md).

## How to use

```bash
python -m trending_study.energy_boundary --input MY_BOUNDARY.json
python -m unittest tests.test_energy_boundary -v
```

Supply one frozen functional unit (`task_id`, `horizon_days`, `boundary_description`, and **independently assessed** `reuse_task_accepted` and `build_task_accepted`) plus `arms.reuse` and `arms.build`. Each must account for `local_development`, `ci`, `model_inference`, `runtime`, `maintenance`, `embodied` and `upstream_support`. Declare every component as **measured**, **modeled** or **unavailable**. Known values need a `source_ref` and finite nonnegative `kwh`. Unknown values require `kwh: null`; arbitrary tokens cannot be used as electricity.

The tool reports signed `reuse − build` energy only when both task outputs are accepted and **all declared component slots have non-missing estimates**. If any term is unavailable, the net is null; no 'zero missing energy' assumption. Optional `grid_intensity_gco2e_per_kwh` produces a **single-intensity illustrative gCO2e calculation** only on complete supplied figures. The output always declares the boundary self-reported. It is *not* an ISO/IEC SCI certification or proof of reductions.

## Calibrating a real experiment (not yet conducted)

1. Freeze equivalent accepted functionality, workload volume, hardware/region, observation and maintenance horizon, permitted reuse alternatives, randomization and security constraints.
2. Calibrate local joules via reference load and idle subtraction, instrument CI/build energy, document power and temperature uncertainty and meter calibration date.
3. Identify hosting/model inference per API request or disclose opaque estimates, cached requests, batch rework and failed search attempts separately; no universal token-to-kWh constant.
4. Include runtime/dependency update effects and upstream maintainer support. Allocate embodied hardware and external infrastructure with defensible assumptions; otherwise label coverage partial.
5. Report ranges for grid intensity by region/time, uncertainties, rebound/adoption changes and break-even workload sensitivity; use negative/null results. **Do not advertise net carbon benefit from a single best-case arithmetic result.**

## Practical maintainer experiment

Use one independently reviewed code task with an existing library candidate and a new-code baseline; record *all* time, installation failures and ongoing maintenance. A smaller prompt or fewer generated lines is not the functional unit. If input energy, security or performance cannot be measured, publish those gaps instead of claiming a green win.

This work is an instrument for later independent energy study, not evidence that AI assistance is energetically cheaper.
