# Evidence registry validation v1.0 (issue #11)

**2026-10-12: offline schema gate; no empirical lesson has been validated.**

Run `python -m trending_study.lesson_registry --input examples/lesson_registry.synthetic.json`.
The validator accepts a JSON object with `schema_version="1.0"`, `dataset_kind="synthetic"` or `"self_reported"`, and `lessons[]`.
Each lesson declares stable `id`, `status`, E0–E5 `grade`, `rq`, `claim`, `population`, `outcome`, `measurement_window`, `sample_n` (nullable), `effect` (nullable), `interval` (nullable pair), `analysis_commit` (nullable git SHA), `data_sha256` (nullable), `sources` (dated canonical URLs), `reviewer_ref` (nullable), `reviewed_at_utc` (nullable), `validity_risks`, `applicability`, `practical_cost`, and `supersedes` (nullable).

Only E0 may lack sources, and grades E1+ require dated source records and analysis/data provenance. Grades E2+ additionally require an explicit sample, effect and uncertainty and E4+ require nonempty external-review metadata; no claimed reviewer identity is authenticated. `validated_for_context` additionally requires at least E4, external review, and explicit data/analysis provenance; the resulting report still says **self-reported only**. A source URL, commit and reviewer field cannot automatically certify scientific truth.

Use per-claim status and preserve superseded/null/contradicted evidence. A null effect is a reportable finding, not missing data; where there is no measured effect use JSON null with `status="hypothesis"` or `"exploratory"`. Revisions should preserve the previous card and add a new immutable version rather than editing already cited evidence. No automatic promotions to validated grades. See `docs/EVIDENCE_TO_LESSON_PROTOCOL.md`.

**Maintainer action:** Convert only independently audited project-specific findings into `templates/lesson_card.md` recommendations, including the time, maintenance, licensing and downside costs. The absence of a positive result is not a reason to fabricate one.
