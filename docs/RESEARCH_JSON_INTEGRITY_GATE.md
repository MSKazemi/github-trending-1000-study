# Research JSON integrity gate for PRs (issue #247)

**Implemented as an offline engineering control, 2026-10-13.** This is **not** a systematic literature review, an authenticated data capture, an ethics approval, a schema registry or empirical research evidence.

The GitHub Actions Python 3.10/3.12/3.14 matrix runs three steps before treating a pull request as technically verified:

```bash
python -m compileall -q trending_study tests
python -m trending_study.data_integrity --root .
python -m unittest discover -s tests -v
```

The standard-library validator inspects committed `.json`, `.jsonl` and `.csv` research files under `examples/`, `references/`, `research/`, `research-notes/` and `templates/`. It **does not read, rewrite, delete, fetch or enroll** real raw captures. It deterministically fails on duplicate object keys (including deeply nested keys), malformed JSON or UTF-8, nonstandard JSON `NaN`/`Infinity`, overflowing floating-point literals, empty JSONL, CSV duplicate/blank headers, ragged or malformed quoted CSV rows, embedded CSV NUL bytes, symlinked evidence files/directories and files exceeding 16 MiB. JSONL errors include the actual record line number.

## Why this protects the study

Python's default `json.loads('{"status":"unknown","status":"verified"}')` normally retains only the last key. A duplicate may therefore **silently change the apparent evidence state**, source URL, DOI, repository ID or experimental denominator. A conventional syntax check alone does not reject this. We now fail closed **before merging**, retaining original files so a human can investigate.

The validator's output counts parsed documents and JSONL records, not confirmed articles, code-reuse successes, human reviewers or study participants. A source file that is structurally valid may still contain fabricated, outdated, misleading, incomplete or non-consensual assertions. Independent source/date/DOI/rights checks, study-specific schemas, scientific adjudication and human PR review remain mandatory.

## Operator workflow

When the CI step fails, open the referenced path and (for JSONL) line. Compare against the original source and the intended canonical schema. Repair only on a new branch, preserve original evidence when required by the research provenance policy, add a regression test, and rerun the full matrix. Never resolve a duplicate by blindly keeping the last value or replacing unknown with zero.

This gate is deliberately conservative but limited: it checks only files in the listed directories and only JSON/JSONL/CSV structural integrity, not CSV semantic schemas, Markdown links, research-statistical logic or source authentication. If a legitimately large artifact exceeds 16 MiB, document and review a format/sharding amendment instead of silently bypassing the gate.

**Practical reusable lesson for your repositories:** enforce unambiguous machine-readable evidence and traceable failures in CI before optimizing stars or claiming reproducibility; no checksum or passing unit test can replace independent verification of the underlying observation.

## 2026-10-13 canonical CSV consolidation from overlapping PR #253

The existing `trending_study.data_integrity` command now **reuses the same scanner** for CSV instead of installing another competing CLI. It checks exact UTF-8, a nonblank case-insensitively unique header, consistent field widths across quoted/multiline records, malformed quoting, NULs, symlinks, bounded file size and existing read-only provenance rules. A header-only CSV is a valid structural empty table but does **not** certify the absence of real observations. The existing return key `json_documents_or_jsonl_records` is preserved for compatibility and excludes CSV rows; `csv_data_records` and `total_logical_records` provide explicit counts. Unknown/missing values are not converted to zero.

The original overlapping [#253](https://github.com/MSKazemi/github-trending-1000-study/pull/253) also produced an independent dated [PR collision and source-preservation inventory](PR_AUDIT_2026-10-13.md) retained as historical evidence; the competing normative policy and scanner are not duplicated. The audit remains an AI-assisted point-in-time inventory, not verified company or study results. This implementation does not validate financial/scientific numeric cell semantics, Excel formula injection, CSV encodings other than UTF-8, or actual source authenticity; downstream CSV schema checks and safe spreadsheet presentation must be handled independently.
