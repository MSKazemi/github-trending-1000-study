# Evidence-to-lesson registry: offline structural audit (issue #11)

**Scope updated 2026-10-13:** a bounded, standard-library-only structural validator. Neither its passing tests nor its synthetic examples authenticate data, researchers, causality, adopted packages or energy savings. The protocol at [EVIDENCE_TO_LESSON_PROTOCOL.md](EVIDENCE_TO_LESSON_PROTOCOL.md) remains authoritative for E0–E5 semantics.

## Canonical v1.0 input and example

```bash
python -m trending_study.lesson_registry --input examples/lesson_registry.synthetic.json
python -m unittest discover -s tests -v
```

JSON top level must contain `schema_version: "1.0"`, `dataset_kind: "synthetic"|"self_reported"`, and `lessons[]`. The migrated [synthetic E0 sample](../examples/lesson_registry.synthetic.json) preserves the earlier proposal from [PR #184](https://github.com/MSKazemi/github-trending-1000-study/pull/184) in this single canonical schema rather than maintaining two incompatible `lesson_registry.py` modules. The source contribution remains linked for audit.

Each lesson requires a unique `id`, `title`, `status`, `evidence_grade` (E0–E5), `question`, `population`, `intervention_or_feature`, `comparison`, `primary_outcome`, `measurement_window`, `applicability`, `negative_findings`, `practical_cost`, `suggested_experiment`, `risks`, `stop_rule`, `validity_threats`, and `sources`. Superseded cards require `superseded_by` different from their own ID. All fields are **self-reported**; URL strings, hashes and reviewer pseudonyms are not verified against third parties.

**E0:** a hypothesis may have zero `sources`; it cannot claim a nonzero evidence grade. Null sample/effect fields mean *not measured*, not zero effect.

**E1–E5:** require at least one HTTPS source with explicit UTC `published_at_utc`, a 40-hex `analysis_commit` and a 64-hex `data_sha256` pointing to frozen source/data content. E1 represents reproducible descriptive observation, **not** an independent endorsement of a vendor launch. The SHA is checked structurally; the tool does not download source bytes or prove the hash was calculated correctly. A plain citation is not evidence of externally measured adoption.

**E2–E5:** additionally require positive integer `sample_n`, finite numerical `effect_size`, and a finite, ordered two-bound `interval` that encloses the estimate. This encodes the current protocol's adjusted/triangulated/controlled evaluation prerequisites but cannot assess confounding, sampling, power or interval coverage. Preserve missing and failed observations in the primary dataset.

**E4–E5:** require an `analyst`, a distinct (case-insensitively) `independent_reviewer`, and explicit UTC `reviewed_at_utc`. The status `validated_for_context` additionally requires `observed_data_ref` and E4 or E5 grade; these are **declarations needing external human review**, not an automatic promotion or approval. The output keeps `independent_verification=false` and `empirical_result_generated=false` even if a submitted card declares validated status.

The validator rejects malformed URLs with embedded credentials or fragments, future UTC source/review times beyond five minutes of allowable clock skew, invalid reviewer aliases, duplicate lesson IDs, nonfinite numeric effects, mismatched interval ranges, missing immutable source/analysis references, and unsupported evidence statuses or kinds. The program makes **no network calls** and executes no downloaded code.

## Why this consolidation matters

The previous drafts [#184](https://github.com/MSKazemi/github-trending-1000-study/pull/184) and [#208](https://github.com/MSKazemi/github-trending-1000-study/pull/208) used incompatible `grade` versus `evidence_grade`, `effect` versus `effect_size`, and source date fields while both added the same module/test path. We retain the existing protocol's canonical `evidence_grade`, `effect_size`, and UTC source timestamp names, incorporate #184's stricter provenance/sampling guards and synthetic example, and preserve a single reproducible implementation. This avoids duplicate maintenance, contradictory experimental denominators and wasteful parallel AI-generated infrastructure.

## Remaining evidence gates

Independent field-level source/date checks; direct data-hash verification; cohort consent and missingness; appropriate adjustment or randomization; measured downstream reuse; external analyst/reviewer identity checks; accessible licensing; and preregistered, bounded whole-lifecycle energy assessments are still pending. Do not close issue #11 as empirically accepted from this PR.

**Practical 2027 maintainer lesson to test:** attach a traceable, independently tested task-outcome card to a reuse-first fix. Reuse an existing checked CLI and research registry instead of spawning separate, incompatible schemas. Evaluate user task acceptance, safety, version/license fit, review time and 30/90-day maintenance before recommending or claiming sustainability benefits. Null and adverse results remain publishable.
