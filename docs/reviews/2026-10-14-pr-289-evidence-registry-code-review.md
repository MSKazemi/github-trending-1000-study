# PR #289 — offline evidence registry engineering review (2026-10-14)

**Repository:** [MSKazemi/github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study) · **PR:** [#289](https://github.com/MSKazemi/github-trending-1000-study/pull/289) · **Issue:** [#11](https://github.com/MSKazemi/github-trending-1000-study/issues/11).

## Decision boundary

Integrate the **offline engineering instrument**, tests, versioned synthetic fixtures, user documentation and roadmap updates, provided exact-head CI is green. **Do not interpret schema validation as real evidence, independent human review, statistical significance, regulatory approval or a recommendation to reuse code.** Keep issue #11 open for external methods/security review and real evidence gates.

## Findings corrected in the merge review

1. **Uncontrolled error on huge numeric claims.** Python's `math.isfinite` raises `OverflowError` when converting sufficiently large integers, so a structurally legal JSON input could escape the controlled CLI error path. Reject unrepresentable numeric values as `LessonError` instead; exercise both direct and CLI entry points using adversarial fixture inputs.
2. **Unspecified reference for a null result.** An interval containing zero is appropriate for an additive difference, but a ratio has a null value of one. v1.1 now requires a finite, explicit `null_value` for E2–E5, and checks whether `result_kind` agrees with interval inclusion of the declared reference. This is a **semantic consistency gate**, not a statistical-validity or effect-certification gate. Legacy v1.0 remains readable.
3. **Ambiguous source/provenance trail.** Reject repeated exact source URLs within a lesson and v1.1 `superseded_by` declarations on lessons that are not marked `superseded`. Preserve all original IDs and noncyclic replacement history.
4. **Path substitution between checking and reading.** Use a bounded read from a verified regular open file descriptor, with a no-follow final symlink flag when available, rather than separate path stat/read operations. The CLI remains offline and read-only.

**CI correction loop:** the first integrated-head [run 38575729309](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38575729309) detected one directory-descriptor error while the other 549 unit tests passed; the non-regular-file check now precedes `fdopen`, and the test also exercises the direct CLI's controlled exit code. Require a new green final-head run before merge. This failure is retained as a real regression-test result, not concealed.

## Scoped change audit

- Changes are limited to `trending_study/lesson_registry.py`, `tests/test_lesson_registry.py`, the existing `data_integrity` shared decoder exported by the PR, the two **synthetic** example inputs, plus linked README, protocol, data dictionary, lesson template, roadmap and issue audit documentation.
- No study cohorts, observations, licensed third-party content, scientific decisions or other software modules are changed by this review.
- Run `python -m unittest discover -s tests -v`, both example CLIs, and the repository's current `research-artifacts` integrity validator. Require the exact final PR-head workflow for Python 3.10, 3.12, 3.13, 3.14 and research artifacts to pass before merging.
- Preserve intervening commits from `main` in a non-destructive merge and protect the final merge with the expected PR-head SHA. The PR discussion is the authoritative record of final CI job IDs and merge commit.

## Scientific and operational follow-up — NOT complete

- A quoted URL, 40-hex commit and SHA-256 string are **not source authentication**, consent evidence or proof that the data snapshot exists.
- Claimed `independent_reviewer` and `review_record_ref` strings are not authenticated reviewer signatures.
- The analysis owner must demonstrate that `null_value`, `effect_unit`, `interval_level` and estimator align with an actual preregistered estimand. An interval spanning a null value is **not** a test of equivalence or proof of no effect.
- Independently assess source rights, reproducibility, missingness, contamination and real task acceptance before any E4/E5 evidence is published.
- As of this review, GitHub `main` has no active branch protection; CI checks are voluntarily enforced for this PR, not an administrator-enforced universal gate. Review rulesets separately.

## Practical lessons to transfer to other repositories

Bound file reads at the **opened descriptor**, reject malformed measurements with controlled exceptions, encode the null reference of each effect scale instead of hard-coding zero, and maintain explicit supersession trails. Treat passing schema tests as a **necessary engineering check**, never as sufficient scientific validation; require independent user-task outcomes and real maintenance-cost follow-up before recommending a growth or sustainability technique.

**Review provenance:** AI-assisted code and methodological review, not a signed independent human/academic audit. No empirical results generated.
