# Green/reuse metrics, traps, denominators and evidence levels

**Status:** pre-analysis metric candidates, not findings. Reproducible comparison requires the SAME useful task, acceptance standard, risk threshold, environments and observation horizon.

## Definitions: reuse vs duplicate effort
- **Reuse opportunity:** a pre-existing licensable/compatible/secure-enough component meets the fixed functional specification in independent verification. Not mere search-result similarity or star count.
- **Reuse discovered:** eligible component was surfaced *before new implementation* and logged with provenance. Search alone does not imply safe integration.
- **Viable reuse:** independent functional task pass, compatible license, reasonable dependency/supply-chain evaluation and acceptable integration budget.
- **Successful reuse:** verified completed user task using an existing dependency, compatible extension, upstream contribution or referenced implementation (without unlicensed copying).
- **Unnecessary reimplementation candidate:** new original work built for a task where viable prior solution existed and independent counterfactual later shows worse net effort/impact. Must be demonstrated—not assigned from clone similarity.
- **Net emissions avoided:** meaningful only when baseline and intervention use the same functional unit/boundary, behavior and service life; subtract actual/estimated totals with uncertainty.

## Metrics
| ID | Metric and formula | Unit / denominator | Validity threat and correction |
|---|---|---|---|
| R01 | Verified reuse opportunity coverage = tasks with >=1 qualified pre-existing solution / **all prospectively sampled tasks** | share of tasks | not all Github indexed; blinded multi-search + independent reviewers |
| R02 | Valid-candidate discovery recall = viable eligible solutions retrieved / manually adjudicated gold candidate set | share; per task | incomplete ground truth; relative recall upper/lower limits |
| R03 | Discovery precision@K = audited functionally relevant and license-permitted candidates / top K results | per K candidates | similarity != suitability; report judge reliability, K |
| R04 | Pre-code search completion = tasks with verifiable alternatives report before implementation / eligible tasks | share | performative logging; capture timestamp & independent audit |
| R05 | Verified reuse task success = accepted tasks completed through reuse / all assigned reuse attempts | share | not directly comparable if tasks differ; fixed specs, randomization, intent-to-treat |
| R06 | Reuse vs build accepted-task throughput = independently accepted task units / total human-active hours | accepted tasks/human-hour | report quality guardrails, all failed/abandoned tasks included |
| R07 | Work avoided = human minutes of matched build arm − reuse arm | minutes per same accepted task | reuse setup and long-term updates counted |
| R08 | Unnecessary implementation fraction = new components **independently determined replaceable** / reviewed new components | share | reviewers require true functional equivalence, not line clones |
| R09 | Structural clone rate = validated Type-1/2/3 clone fragments / analyzed eligible fragments | share | only duplication indicator, not waste; generated/vendor files excluded/separate |
| R10 | Functional overlap = task-same solutions confirmed using acceptance tests / evaluated pairs | per pair | embedding similarity is candidate retrieval, not gold proof |
| R11 | Independent reuse = externally validated distinct integrations / eligible observed candidates | count/rate | API download/fork stars are weak proxies; verify task or dependency chain |
| R12 | Post-release update burden = dependency upgrades, compatibility repairs, security fixes hours over fixed 90/180-day window | hours per accepted solution | observation windows must match; no updates != secure |
| G01 | Development energy = measured or modeled kWh for local devices + CI + agent inference + build/test + transfer | kWh per accepted functional task, uncertainty | vendor inference may be opaque; never derive one exact kWh/token without model/hardware data |
| G02 | SCI-style task carbon intensity = (E*kWh grid intensity + allocated hardware embodied M) / R | gCO2e per independently accepted task | **R = same useful unit**, same boundary/time/region, measured vs estimate labeled |
| G03 | Lifetime energy = development + 30/90/180d maintenance + incremental runtime/deployment for stated workload | kWh per life horizon and workload | reuse might increase usage; include rebound and migration costs |
| G04 | Net energy difference = energy(build) − energy(reuse) for equivalent functional task and horizon | signed kWh with interval | no universal saving; local measurement ≠ cloud inference |
| G05 | Tokens per accepted task = input/output/cached-equivalent tokens across all attempts / accepted tasks | tokens; undefined if 0 accepted | model, caching, tool count, API scheme affect energy; tokens ≠ CO2 |
| G06 | Data-center carbon uncertainty = modeled gCO2e interval with alternative intensity/embodied assumptions | gCO2e range | provider values usually unobservable; do not label estimate as measurement |
| R13 | Licensing provenance compliance = integrations with documented valid license compatibility / independently audited integrations | share | public repo != license-free; project changes possible |
| R14 | Security/maintenance gate = severe unresolved vulnerability or incompatible license or unmaintained critical dependency | category + evidence | binary gate not reducible to arbitrary popularity score |

## Energy/carbon methodology
ISO/IEC 21031:2024 Software Carbon Intensity (SCI): **SCI = (E × I + M) / R** where E kWh, I location/time intensity in gCO2e/kWh, M allocated embodied emissions in gCO2e and R the functional unit. GSF SCI for AI (ratified extension) distinguishes provider and consumer perspectives. Define functional unit as **one independently accepted same user task**, not one prompt or line of code.

**Boundaries:** local developer device (CPU/GPU/display where measurable), local build/test, cloud model inference, agent orchestrator, GitHub CI, downloaded packages and integration, maintenance, and incremental operation over declared user workload. Embodied resource allocation and energy may be unavailable; mark missing and report partial-boundary metrics instead of claiming a total.

**Measurement priority:** (1) calibrated physical meter / reliable device telemetry (RAPL, NVML where suitable), (2) provider-published task telemetry with scope, (3) versioned Green Software Foundation Impact Framework or CodeCarbon modeled estimate with uncertainty, (4) unknown. CodeCarbon's unsupported hardware uses assumptions; energy measured locally is not the whole server-side service footprint.

**Counterfactual:** if an existing solution already serves the need, a 'do not build; reuse' arm may be the strongest baseline. If a fresh build is safer/more efficient in runtime, measuring one-off development energy can give the wrong answer. Report totals AND intensities, sunk/shared infrastructure assumptions, and whether improved accessibility induces additional workload (**rebound effect**).

**Don't invent false equivalences:** no universal CO2-per-token multiplier; '10k tokens saved' does not establish kWh saved. Carbon reduction depends on model/provider/hardware, grid mix, token-length shape, caching, task success, full lifecycle and rebound.

## Quality gates before claiming green benefit
Same task accepted by independent reviewer; no critical open security/functional failures; legal provenance; elapsed time/cost complete enough to compare; uncertainty and sensitivity for unavailable inference energy; repeated hardware/CI workload runs where feasible. A statistically significant reduction in tokens alone is **not** a demonstrated carbon or user-value benefit.

## Analysis
Paired / task-blocked 2x2 experimental outcomes; participant/project clustered CIs; intention-to-treat; no exclusion of failed tasks; pilot-derived power, stage-appropriate outcome hierarchy, preregistered interaction tests. Report separate human time, tokens, kWh and carbon estimates, with robustness to unknown server-side energy.


## Additional scientifically necessary measurements (October 2026 protocol amendment)
- **Judgment coverage@K and P@K bounds:** report the count and fraction of unjudged top-K candidates, lower/upper precision bounds, and do not label pooled-relative recall as absolute/global recall.
- **Non-availability confidence:** cannot infer no safe reusable solution exists from zero retrieved candidates; preserve unresolved/missing.
- **Time-indexed provenance:** a candidate released after the task baseline is ineligible for a historical reuse opportunity.
- **Upstream maintainer workload:** where consented and observable, review/support/upgrade effort moved from downstream developers; if unavailable state unknown.
- **Developer comprehension/knowledge transfer:** independent maintainer succeeds at future fix with specified acceptance suite, human time, defect burden.
- **Supply-chain hallucination rate:** proportion of suggested packages with missing/incorrect official registry identity and audited version, plus typosquat or incompatible license/safety review.
- **Lifecycle break-even:** signed reuse-vs-build impact over declared number of accepted task executions and maintenance horizon; include upfront candidate discovery/indexing, model inference, CI, deployment/runtime and environmental source coverage.
- **Water, embodied hardware and rebound:** separate axes, not derived from fixed tokens×carbon constants. Carbon-aware does not imply water-efficient.
- **All-task analysis denominator:** the reuse-eligible stratum is secondary; primary assigned-workflow analysis includes no-opportunity and failed tasks.

References: [critical gaps](CRITICAL_RESEARCH_GAPS_2027.md), [gold labeling](REUSE_GOLD_STANDARD_2027.md), [trust](SUPPLY_CHAIN_PROVENANCE_2027.md), [life cycle](FULL_LIFECYCLE_BREAK_EVEN_2027.md), [human externalities](MAINTAINER_EXTERNALITIES_2027.md).
