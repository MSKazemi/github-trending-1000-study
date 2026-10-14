# PR #291 review and integration record — 2026-10-14

**Scope:** [#244](https://github.com/MSKazemi/github-trending-1000-study/issues/244), an engineering-only Git-tracked Python/JSON syntax and ambiguity gate. **Target:** `main`. **PR:** [#291](https://github.com/MSKazemi/github-trending-1000-study/pull/291).

## Actual review

- Inspected all seven original changed paths: `.github/workflows/ci.yml`, `CONTRIBUTING.md`, `README.md`, `docs/RESEARCH_JSON_INTEGRITY_GATE.md`, `docs/ROADMAP.md`, `scripts/check_research_artifacts.py`, and `tests/test_tracked_code_json_gate.py`.
- Reviewed fail-closed Git-index NUL-delimited inventory, top-level requirement, stage/mode checking, path/symlink avoidance, UTF-8 and strict JSON checks, compile-without-execute Python validation, cardinality and byte limits. This is read-only validation of checkout bytes, **not** a race-proof sandbox, security audit or source authentication.
- Inspected positive and negative tests for nested/hidden files, contextual Python syntax, bad UTF-8, duplicate keys, nonfinite numeric values, symlinks, missing files, size limits, newline filenames, untracked exclusions and empty index. No substantive implementation defect identified.
- Verified [pre-documentation-fix CI run 38602382600](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38602382600) succeeded with `test (3.10)`, `test (3.12)`, `test (3.13)`, `test (3.14)`, and `research-artifacts` on commit `8c63b628bbd160057065489dd2ad325b81b87496`. **That run does not validate subsequent documentation-only commits; require a new exact-head run before merge.**
- Checked review submissions/threads at the time of review: none reported; GitHub reported mergeable. The separate PR #290 overlaps README/roadmap, not the new scanner. Re-check current base, mergeability, reviews and CI immediately before merge.
- Corrected a stale operator-guide introduction: it incorrectly described three steps in the matrix and omitted the standalone research-artifacts job; now documents current matrix and both research validators. This is a documentation-only correction, not evidence of a new validated result.

## Explicit non-claims and required gates

No empirical GitHub Trending collection, source-rights/robots approval, scientific preregistration, independent source or human methods review, real-world reuse/adoption result or environmental effect is implied. A repository owner should establish server-enforced required checks and independent review where needed ([#248](https://github.com/MSKazemi/github-trending-1000-study/issues/248)). This record is an engineering-agent review and **not an independent qualified human signoff**.

**Merge condition:** completed all-five-job GitHub Actions `pull_request` workflow with success on **final** SHA; no new review objections, merge conflicts or unexpected base changes; merge with expected head SHA and verify post-merge main separately. If any condition fails, keep open and correct it.

## Practical maintainer lessons

1. Check *tracked* inputs as well as conventional code directories, including hidden or unimported paths.
2. Combine negative fixtures and per-file/aggregate bounds with an explicit fail-closed parser; never execute inputs to merely check syntax.
3. Run exact-head CI for documentation fixes too; a prior passing commit does not certify subsequent changes.
4. Treat structural engineering checks and scientifically authenticated evidence as separate gates.
