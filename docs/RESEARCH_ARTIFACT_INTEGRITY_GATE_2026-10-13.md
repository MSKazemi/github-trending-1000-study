# Enterprise CI: one canonical research-artifact integrity gate (2026-10-13)

**Scope:** offline engineering safety checks only, not source authenticity, consent, scientific validation, security certification or confirmation of GitHub branch protection. Related implementation issues: [#240](https://github.com/MSKazemi/github-trending-1000-study/issues/240), [#244](https://github.com/MSKazemi/github-trending-1000-study/issues/244) and [#247](https://github.com/MSKazemi/github-trending-1000-study/issues/247).

## Why this design is unified

The concurrent proposals [#245](https://github.com/MSKazemi/github-trending-1000-study/pull/245), [#250](https://github.com/MSKazemi/github-trending-1000-study/pull/250), [#251](https://github.com/MSKazemi/github-trending-1000-study/pull/251), [#252](https://github.com/MSKazemi/github-trending-1000-study/pull/252) and [#253](https://github.com/MSKazemi/github-trending-1000-study/pull/253) each contributed relevant guards. The repository has already integrated the canonical review policy, PR template, SHA-pinned GitHub Actions, and three-version CI via [#255](https://github.com/MSKazemi/github-trending-1000-study/pull/255). This change deliberately retains **one** research-artifact validation entrypoint rather than three nearly equivalent checkers or conflicting workflow files.

Selected artifact implementation originated from #253; JSON deep-key and finite numeric requirements from #250/#251 are included. The previous inline examples/references-only JSON check is superseded because it misses JSONL, CSV and additional research data directories. The existing `compileall` gate also covers previously unimported Python syntax without a second AST-only checker. The dated source/PR discussion audit is retained in [PR_AUDIT_2026-10-13.md](PR_AUDIT_2026-10-13.md); no historical observations are deleted.

## Reproduction and safety contract

```bash
python scripts/check_research_artifacts.py --root .
python -m compileall -q trending_study scripts tests
python -m unittest discover -s tests -v
```

The standard-library checker is read-only and scans `examples/`, `references/`, `research-notes/`, plus `research/` and `templates/` when present, for `.json`, `.jsonl` and `.csv`. The three primary directories must exist. It rejects malformed UTF-8, JSON duplicate keys at any depth, NaN/Infinity, finite-float overflow/underflow, extreme integer literals, empty/invalid JSONL records, CSV duplicate/blank headers and ragged rows, NUL bytes, symlinks and unreasonable file sizes (16 MiB/file, 128 MiB total, 5000 files). CSV quoted multiline fields are handled by the Python CSV parser. Errors preserve the offending path and line/context without rewriting research records.

GitHub Actions checks **each** supported Python version (3.10, 3.12, 3.14): compilation, artifact inspection, complete offline unittest regression suite and CLI help smoke checks. Workflow checkout/setup actions are immutable-SHA-pinned with `contents: read`, `persist-credentials: false`, bounded execution and PR-only cancellation (post-merge `main` verification must not be cancelled). Check that the exact PR-head jobs pass before merge, then confirm the merged `main` push run.

The gate does **not** validate DOI existence, real-world source authorship, human reviewers, unbiased sampling, package provenance, scientific conclusions, claims about enterprise security or environmental savings. It cannot replace independent review or admin-enforced GitHub required checks.

## Follow-up quality gates

- Configure GitHub branch protection/rulesets by an authorized repository administrator to require the latest PR review, appropriate protected checks, resolved conversations and no forced pushes. A workflow file alone cannot enforce this.
- Preserve the original write-once research artifacts; repair bad inputs only after source review with traceable corrections. Do not auto-rewrite duplicate keys or replace unknown with zero.
- Review actual source permissions, security, independent task acceptance, scientific methods and statistical validity outside the lexical validator. Report all remaining blockers in PRs.
- Adopt the same pattern in other repos: one canonical validator, pinned actions, negative tests, non-destructive errors, and independent acceptance tasks, rather than maximizing check count or overlapping implementations.
