# 2027 reuse-first task pilot: frame, allocation and outcome audit

**Prepared:** 2026-10-12. **Status:** proposed instrument for issue [#25](https://github.com/MSKazemi/github-trending-1000-study/issues/25), **not a frozen/preregistered protocol**. No participants have been recruited; the committed frame and outcomes are wholly synthetic.

## Why this instrument exists

The original Trending cohort answers observational questions about *attention*. It cannot identify the causal effect of code reuse. The distinct, consented task experiment must draw tasks **independently of whether reusable code exists**, lock independently written task/acceptance evidence before allocation, then retain **every randomized task**, including abandoned, failed, refused and no-opportunity cases, in the intention-to-treat (ITT) analysis. This CLI operationalizes that ledger for the proposed [2×2 design](REUSE_FIRST_EXPERIMENT.md): human/agent allowed × ordinary/reuse-first workflow. It is not a search engine, experimental trial, carbon calculator or power analysis.

## Offline example (no network, no installs beyond Python stdlib)

From the repository root:

```bash
python -m trending_study.trial assign \
  --frame examples/trial_frame.synthetic.json \
  --output /tmp/trial-allocation.synthetic.json
python -m trending_study.trial audit \
  --frame examples/trial_frame.synthetic.json \
  --assignments /tmp/trial-allocation.synthetic.json \
  --outcomes examples/trial_outcomes.synthetic.json
python -m unittest discover -s tests -v
```

`assign` refuses to overwrite an existing output. This helps preserve allocations but does not make them tamper-proof. The synthetic example includes **nine fictional screened tasks**: **eight assigned**, **one preassignment exclusion**. Its SHA-256 strings, reviews, simulated timings and acceptances are demonstration fields **without executable acceptance suites or independent human validation**. The outcome example deliberately illustrates failures, refusal, pending work and missing time. Do not interpret the simulated per-arm performance as a real finding.

## Frame schema v1.0

A frame is a JSON object with the exact following keys; unknown keys are rejected to prevent post-treatment labels from creeping into sampling:

| Field | Meaning / constraint |
|---|---|
| `schema_version` | Exactly `1.0`. |
| `dataset_kind` | `synthetic` or consented `pilot`; **never** claim confirmatory study registration. |
| `protocol_id` | Pseudonymous protocol/version token tied to a reviewed protocol. |
| `frame_source_ref` | Human-readable reference to the full prospective task source frame / selection log. The CLI cannot validate it. |
| `frame_locked_at_utc` | ISO8601 **UTC** lock timestamp; no task baseline may be later. |
| `randomization_seed` | Public, fixed integer in `[0, 2^63)`; decide and register **before** outcomes. |
| `design` | `factorial_2x2` only. |
| `ethics_review_ref` | Null for `synthetic`; nonempty permission/ethics reference for `pilot` (the CLI cannot verify approval). |
| `tasks` | Nonempty list of all screened *consented and specified* task IDs including prespecified exclusions. |

Each task has exactly: `task_id`, `family_id`, `cluster_id`, `baseline_utc`, `spec_sha256`, `acceptance_sha256`, `independent_acceptance_ref`, `language`, `project_type`, `difficulty`, `experience_band`, `source_kind`, `consent_ref`, `eligibility_status`, `exclusion_reason`. IDs must be pseudonymous; do not include participant names, accounts, private prompts or secrets. SHA fields must be lowercase 64-character digests of the **actually retained, access-controlled** frozen task spec and independent acceptance suite. `baseline_utc` must be UTC and not later than lock time. `source_kind` is `synthetic` with null consent for examples; for `pilot`, it is `opt_in` with a nonempty consent reference. A blank/placeholder string does not demonstrate genuine authorization or independent evaluation.

`eligibility_status` is `eligible` (reason null) or `excluded_pre_assignment` with exactly one of `duplicate`, `out_of_scope`, `safety_prohibited`. A finding of *no viable reusable package* is never an allowable exclusion. Prespecify how out-of-scope and duplicate decisions are made, with a blinded audit before allocations are revealed. **Do not store identifiable no-consent recruitment records in this frame**; report aggregate nonconsent counts in a separately reviewed screening/ethics ledger. A refusal *after assignment* is an outcome (`refused`), never a retroactive exclusion.

## Allocation and audit semantics

- Eligible records are grouped by `cluster_id` (the allocation unit). Every task in a cluster inherits the same arm; a `family_id` may not span clusters, reducing task-family leakage. Each cluster must belong to one language/project-type/difficulty/experience block. These safeguards do not solve all same-developer or shared-code contamination, which requires a prospective enrollment design.
- Within each block, clusters and complete four-arm cycles are deterministically ordered by SHA-256 of the stored seed and block/cluster identifiers; per-block cluster counts across arms differ by at most one. **Task** counts can differ when clusters contain different numbers of tasks. For small blocks, arms can be empty. Do not claim powered balance or independence from that fact.
- Output contains the canonical frame digest, four-arm assignment table, per-arm counts and every prespecified exclusion. Running on identical frame bytes/values yields the same assignment; changed frame values fail verification during outcome audit. Hashes are traceability checks, **not cryptographic proof of prospective registration**.
- All assigned tasks require exactly one outcome record. Outcomes use exact fields `task_id`, `status`, `human_active_minutes`, `closed_at_utc`, `independent_review_ref`, `security_gate`, `rights_gate`, `protocol_deviation`. `status` is `accepted`, `failed`, `abandoned`, `refused` or `pending`. A pending task has a null close time; other statuses require closure after lock. `human_active_minutes` is a measured nonnegative number or **null** (unknown, never silently zero). Accepted outcomes need a nonempty independent-review reference plus `pass` for security and rights, but this utility cannot inspect actual reviews.
- `audit` recomputes the assignment from the supplied frame and requires exact equality with the preserved allocation. It fails if any assigned outcome is missing or if an excluded/unrecognized task is included. If a task has not finished, retain it as `pending`; record missing active-time as null. Do not invent zero time for refusal or abandonment.
- The report includes status counts, accepted-rate lower/upper bounds (pending could eventually pass), all-assigned denominators, known total active minutes and accepted tasks per **fully observed** human hour. The latter is null when any record in the comparison has missing time, no positive time, or pending status. Both per-arm and pooled `usual`/`reuse_first` summaries are **descriptive**, not an inferential ITT effect estimate.

**Power-stage boundary:** [The synthetic cluster-factorial sensitivity helper](CLUSTER_TRIAL_POWER_SENSITIVITY_2026_10.md) shows how equal cluster size, ICC and assumed binary accepted-task rates change normal-theory sensitivity. It does **not** power the primary accepted-tasks-per-human-hour rate, replace pilot-derived variance or validate an experimental N. No confirmatory recruitment approval is implied.

## Required external protocol gates before **real** enrollment

1. Agree on **one primary estimand** and exact comparison. A recommended task-level ITT estimand is the reuse-first versus ordinary workflow difference in independently accepted task throughput per total measured human-active hour across *all* randomized tasks, with the randomized agent-permission factor prespecified. Establish minimum worthwhile effect, safety/rights noninferiority gates, handling of undefined zero-hour rates, clustering, 95% CIs and multiplicity **before opening the confirmatory dataset**. Retain both completion rates and raw effort counts so a ratio cannot hide severe failures.
2. Independently author, version and freeze acceptance suites *before assignment*. Use held-out tasks/tests and check training-data leakage, solved public issues, cross-condition solution sharing, persistent developer learning and agent prompt contamination. Keep a dated component availability cutoff; goldset labels must be blind to treatment/outcome and must not be a sampling criterion.
3. Obtain real participant consent and privacy approval; define lawful collection, retention, access, deletion and opt-out workflows. Keep raw human effort/token traces access-controlled; release aggregates or approved pseudonymous derivatives only. This tool deliberately collects no personal identifiers or live telemetry.
4. Precommit the frame/seed/hash and independent acceptance-test checksums to an immutable, externally timestamped research record **before execution**. Obtain independent statistical/protocol review and a preregistration identifier. No Git commit or string in `ethics_review_ref` alone demonstrates this approval.
5. Run an opt-in feasibility pilot with positive, negative and **unknown** reuse opportunities. Measure block/cluster balance, missing/failed/refused rates, reproducible tool/model versions, time and reviewer burden, contamination, assessment agreement, relevant security/license findings and retained no-opportunity tasks. Estimate sample size with a pilot-informed simulation, **not** an arbitrary `N=30–50` confirmatory claim.
6. Collect device/CI energy with a calibrated boundary, document provider inference as measured/modelled/unavailable, and quantify upstream maintainer/runtime costs where feasible. Do **not** equate token savings with CO2 reductions; report distinct endpoints and uncertainty.

## Key limitations and stop rules

- Assignment hashes and fields validate **format and internal consistency**, not honest prospective capture, live ethics approval, correctness of test suites or independent reviewers. The utility cannot prove a global absence of reusable software, full task-frame completeness or causal effects.
- Refuse confirmatory reuse-efficiency or environmental claims when study gates above are missing. If pilot shows severe imbalance, noncompliance, hidden test exposure, high missingness or unethical collection, correct and version the design **before** new confirmatory recruitment; never silently rewrite observed assignments.
- Preserve positive, neutral, **negative** and unresolved results. Synthetic example outcomes favor one arm by construction and have **zero** external validity.

See [issue #25](https://github.com/MSKazemi/github-trending-1000-study/issues/25), [scientific governance](SCIENTIFIC_GOVERNANCE_2027.md), [independent gold set](REUSE_GOLD_STANDARD_2027.md), [ethics](ETHICS.md), [metrics](REUSE_SUSTAINABILITY_METRICS.md) and [inception gates](INCEPTION_CHECKLIST_2026_2027.md).

## Integration checks added after the 2026-10-12 branch review

**Separate assignment truth from outcome file truth.** Real pilot outcome files now **require** a `frame_sha256` equal to the canonical frozen frame SHA-256 in the assignment artifact. Historical synthetic demonstration input remains accepted without this new field for backwards-compatible examples; when a synthetic file includes the field, it must match. A task with the same ID but a silently changed acceptance suite cannot silently inherit the previous pilot outcomes. A checksum links user-provided records; it **does not authenticate** actual participants, tests, or real prospective registration.

**Write-once allocation.** The CLI now uses the existing shared `safe_io` exclusive staged publisher, rejects source/output path collisions and prior files, and will not overwrite a task frame even under an ordinary existing-target race. A pilot frame lock timestamp in the future is rejected. All changes are demonstrated via offline synthetic tests and do not constitute verified human data.

**Concealment warning:** deterministic assignment with a visible seed/algorithm is *reproducible* but not a randomization-concealment protocol. An investigator who knows the seed could attempt to select tasks or reassign cluster IDs to steer treatment. Before any actual trial, freeze the task frame with independent time-stamped review, use an allocation custodian or otherwise control allocation visibility, document deviations and preserve all screening failures. Never use these scripts as proof of concealed unbiased randomization.
