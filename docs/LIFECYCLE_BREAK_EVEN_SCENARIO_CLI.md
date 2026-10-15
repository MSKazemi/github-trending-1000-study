# Offline lifecycle break-even scenario (#23)

**Status: synthetic demonstration, 2026-10-13.** No measured energy, carbon, water, human effort, upstream load, field task success or lifecycle savings are asserted. This is a bounded implementation of the *equations* in [FULL_LIFECYCLE_BREAK_EVEN_2027.md](FULL_LIFECYCLE_BREAK_EVEN_2027.md), not calibration or human-approved research.

## Repeatable offline example

    python -m trending_study.lifecycle_break_even --input examples/lifecycle_break_even.synthetic.json
    python -m unittest discover -s tests -v

For a **single frozen accepted functional unit**, the two strategies share task-spec/acceptance SHA-256 values, the same nominal observation horizon, workload counts, explicit boundary, and a named list of omitted impacts. Input term records require a decimal kWh string, evidence basis and evidence reference. 'Unknown' requires null kWh and produces **no difference estimate**; never impute zero. The CLI does not authenticate either hash or evidence link and cannot establish task equivalence. For a real study, acceptance must be independently verified before feeding inputs.

Given build pre-use 12 kWh, reuse 4 kWh, build runtime 0.01 kWh/use and reuse runtime 0.04 kWh/use, the equality point is approximately 266.67 uses; for integer workloads, reuse is lower through 266 and higher from 267. These numbers are **invented solely to test arithmetic**, not calibrated observations. A real claim needs matched functional throughput, included unsuccessful work, uncertainty propagation, compatible grid/time carbon factors, and measurement of inference and hardware impacts. Omitted provider inference, embodied hardware, water and upstream load make the example a **partial declared boundary**, not a full lifecycle inventory.

For continuous break-even thresholds the output reports an **approximation to six decimal places**; it also reports **exact integer workload boundaries** (last workload where one approach is strictly lower, first workload where the other is strictly lower, and integer equality when applicable). Never infer which integer workload wins by rounding the approximate threshold. Operational input limits are 0–1,000,000,000 executions per workload point, 0–3,650 horizon days, and at most 100 workload points; they are software validation limits, not scientific estimates of actual deployment.

Outputs contain signed energy delta (build − reuse), crossing direction, calculation completeness and explicit omissions; carbon is **not** inferred from kWh or token counts. A negative delta is a valid outcome; successful reuse does not guarantee net environmental savings. Reporting multiple workloads is sensitivity illustration only, not confidence intervals or causal inference.

## Outstanding acceptance gates

- Independently freeze workload/acceptance and test both choices for equal accepted functionality, security and license suitability.
- Obtain consent and clearance before logging private developer effort; include search, review, failure, maintenance and upstream time where authorized.
- Calibrate meters and identify missing inference/server/embodied terms; keep uncertainty intervals and time-varying carbon intensity, not one generic conversion factor.
- Preregister horizon, candidate versions, workload mix, comparison estimand and rebound assumptions. Independently audit observations; never call this CLI a study.

## 2026-10-13 decision and uncertainty guards

The offline Decimal scenario now additionally rejects a **zero-day horizon** and malformed/unhashable evidence-basis values. Concurrent contributor work already added exact **integer workload crossing** cases to avoid a rounded threshold being mistaken for the first strictly lower-energy integer use. These are only *within-declared-boundary scenario calculations*. A synthetic crossing does not show real savings, and a `null` included term must stop point estimates rather than be treated as zero.

**Predeclare the comparison** of task-equivalent accepted outputs and stable functional unit; build-versus-reuse versus no-build, search/validation attempts, downstream runtime at `n_uses`, update/recovery, upstream support allocations and long-run rebound. For a simple additive boundary the signed difference is `ΔE(n) = (E_build_fixed - E_reuse_fixed) + n × (E_build_run - E_reuse_run)`. The numerical crossing follows from this declared *linear assumption*; caching, workload mix, memory/embodied allocations, nonlinearity and rebound require sensitivity/scenario analysis rather than concealed constants. Report cloud inference as unknown when metering unavailable. Human upstream labor is a distinct social cost, not direct electricity.

**Source:** [ISO/IEC 21031:2024 SCI methodology](https://www.iso.org/standard/86612.html). The input/output cannot certify full SCI; grid intensity, marginal effects, embodied allocation, usage displacement and uncertainty need separate justified measurement evidence. Keep physical kWh and gCO2e separate, and report all abandoned/failed tasks in both arms.

**Practical lesson:** only call a reusable component environmentally advantageous when externally accepted functionality and the time/usage/environmental boundary are comparable; otherwise publish the transparent break-even condition and open evidence gaps.


## 2026-10-15 — lifecycle scenario input-integrity fix (#308)

The scenario CLI now uses the shared strict research JSON decoder and bounded
regular-file reader from issue #306, replacing the unsafe separate
\`Path.stat().st_size\` then \`Path.read_text()\` sequence. Its input limit
remains **1,000,000 actual bytes**. FIFO/nonregular files, leaf symlinks,
malformed UTF-8, duplicate JSON keys, NaN/Infinity and invalid numeric
overflow/underflow fail closed without exposing private keys/file names.
Existing exact signed crossing and \`unknown\` propagation are retained.

This change does not convert a scenario into calibrated physical energy,
provider inference, total lifecycle carbon impact or validated savings.
The user-task acceptance, embodied allocations and rebound remain external
measurement questions requiring separately approved evidence.

**Practical maintainer lesson:** correct algebra does not make a research
calculator safe. Validate representation, filesystem input, units and
unknowns at the entrypoint before interpreting any output.
