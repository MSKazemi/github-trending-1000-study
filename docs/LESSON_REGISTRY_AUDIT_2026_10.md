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

## 2026-10-14 hardening — v1.1 (issue #11)

The validator accepts historical **v1.0** documents for review, reports
`v1_0_legacy_input=true`, and provides **v1.1** for new lesson records. It does
not rewrite historical records. The canonical E0 fixture was migrated to v1.1;
an additional entirely fabricated E2 / null-compatible example is at
[lesson_registry.null_result.synthetic.json](../examples/lesson_registry.null_result.synthetic.json).
Both are **synthetic illustrations, not findings**.

New v1.1 requirements, in addition to v1.0:

| Scope | Required fields or behavior | Scientific boundary |
| --- | --- | --- |
| All lessons | `research_question_id`, `result_kind` | The RQ link is self-declared; a frozen preregistration is not implied |
| E0/E1 | `result_kind=not_estimated`; `effect_size`, `interval`, `interval_level` must be absent or null | Missing is not zero; E0 `sample_n` must be null or absent |
| E1–E5 | `observed_at_utc` (explicit UTC) and `observed_data_ref`, plus HTTPS dated source, analysis commit and frozen-data SHA-256 | Hash, dates and data refs are syntax-checked, not independently authenticated |
| E2–E5 | `result_kind=estimated|null_compatible`, measured `effect_size`, containing `interval`, `interval_level` in (0, 1), `effect_unit`, `analysis_method`, and positive `sample_n` | `null_compatible` means the reported interval contains zero; **not** evidence of equivalence, no effect or good statistical design |
| E4/E5 | Distinct analyst/reviewer, `review_record_ref`, and `reviewed_at_utc` no earlier than `observed_at_utc` | A claimed review reference is not authenticated endorsement |
| Superseded | `superseded_by` must point to another ID **in the same file**, without cycles | Earlier card remains intact and can be recovered; do not discard negative findings |

For **both** schema versions, only documented top-level, lesson and source
fields are accepted; unknown keys such as `prompt`, `raw_log` and
`private_user_email` fail closed (but textual fields still require a human
privacy check). A synthetic document **cannot** declare
`validated_for_context` even if it contains forged hashes/reviewer aliases.
For self-reported records meeting E4/E5 structure, any declared
`validated_for_context` entry remains in
`declared_validated_ids_needing_external_review`, and
`independently_verified_lesson_count` always remains **zero**. Never present
the `by_status` declaration counts as verified research.

The direct CLI now reuses the shared research JSON strict decoder: no
duplicate object keys, NaN/Infinity, non-UTF-8 or oversized files; it also
refuses symlink inputs. This prevents the CLI from quietly bypassing the
repository-wide artifact-integrity gate. No network access or data collection
was added. Sample input:

```bash
python -m trending_study.lesson_registry --input examples/lesson_registry.synthetic.json
python -m trending_study.lesson_registry --input examples/lesson_registry.null_result.synthetic.json
python -m unittest tests.test_lesson_registry -v
python -m unittest discover -s tests -v
```

**Acceptance boundary:** The engineering deliverable is an offline validator,
schemas, synthetic fixtures and tests. It does **not** grant publication
approval, independently verify source authenticity, supply a signed methods
review or produce E4/E5 study findings. Keep human empirical sign-off and
real task measurement as separate future study gates.

**Practical repository lesson:** require a specific RQ, immutable data and
code references, a stated uncertainty interval with units, an independent
review record, and a reproducible negative-result trail **before** promoting
a claimed growth/reuse technique. Keep hypothetical examples searchable
without counting them as evidence.
