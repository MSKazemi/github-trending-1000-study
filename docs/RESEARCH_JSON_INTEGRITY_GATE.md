# Research JSON integrity gate for PRs (issue #247)

**Implemented as an offline engineering control, 2026-10-13.** This is **not** a systematic literature review, an authenticated data capture, an ethics approval, a schema registry or empirical research evidence.

The GitHub Actions Python 3.10/3.12 matrix runs three steps before treating a pull request as technically verified:

```bash
python -m compileall -q trending_study tests
python -m trending_study.data_integrity --root .
python -m unittest discover -s tests -v
```

The new standard-library validator inspects committed `.json` and `.jsonl` research files under `examples/`, `references/`, `research/`, `research-notes/` and `templates/`. It **does not read, rewrite, delete, fetch or enroll** real raw captures. It deterministically fails on duplicate object keys (including deeply nested keys), malformed JSON or UTF-8, nonstandard JSON `NaN`/`Infinity`, overflowing floating-point literals, empty JSONL, symlinked JSON files/directories and files exceeding 16 MiB. JSONL errors include the actual record line number.

## Why this protects the study

Python's default `json.loads('{"status":"unknown","status":"verified"}')` normally retains only the last key. A duplicate may therefore **silently change the apparent evidence state**, source URL, DOI, repository ID or experimental denominator. A conventional syntax check alone does not reject this. We now fail closed **before merging**, retaining original files so a human can investigate.

The validator's output counts parsed documents and JSONL records, not confirmed articles, code-reuse successes, human reviewers or study participants. A source file that is structurally valid may still contain fabricated, outdated, misleading, incomplete or non-consensual assertions. Independent source/date/DOI/rights checks, study-specific schemas, scientific adjudication and human PR review remain mandatory.

## Operator workflow

When the CI step fails, open the referenced path and (for JSONL) line. Compare against the original source and the intended canonical schema. Repair only on a new branch, preserve original evidence when required by the research provenance policy, add a regression test, and rerun the full matrix. Never resolve a duplicate by blindly keeping the last value or replacing unknown with zero.

This gate is deliberately conservative but limited: it checks only files in the listed directories and only JSON/JSONL lexical integrity, not CSV contents, Markdown links, research-statistical logic or source authentication. If a legitimately large artifact exceeds 16 MiB, document and review a format/sharding amendment instead of silently bypassing the gate.

**Practical reusable lesson for your repositories:** enforce unambiguous machine-readable evidence and traceable failures in CI before optimizing stars or claiming reproducibility; no checksum or passing unit test can replace independent verification of the underlying observation.

## Extended canonical data-integrity checks (2026-10-13 PR integration)
This module is the **single** canonical offline research-artifact checker after review of overlapping [PR #251](https://github.com/MSKazemi/github-trending-1000-study/pull/251) and [PR #253](https://github.com/MSKazemi/github-trending-1000-study/pull/253). The useful original ideas—strict CSV column-count/header validation, rejecting numeric float underflow, bounded huge integers, symlink safety and total file/byte budgets—are integrated **without adding a competing script/CLI or replacing any existing CI protections**.

- The existing `python -m trending_study.data_integrity --root .` CI step now checks `.csv` under the five research source directories as well as `.json`/`.jsonl`. CSV uses Python's RFC-4180-style reader with strict quoted-field errors; header columns must be nonblank and unique after trimming/casefolding, and all rows must have the header's exact width. A header-only CSV has no auditable data records and fails closed.
- JSON fractional literals that would overflow to infinity **or silently underflow to zero** are rejected; integer literals exceeding 1,024 digits are rejected, avoiding version-dependent Python conversion behavior.
- A file is limited to 16 MiB, all scanned data to 128 MiB, and the inspected artifact set to 5,000 files; explicit over-limit input requires a signed dataset-sharding/limit amendment, not silent filtering.
- Preserve original `json_documents_or_jsonl_records` count for compatibility; new report fields `csv_data_rows`, `total_research_records`, and `checked_bytes` distinguish file classes. Existing main CSV registry files are used as regression/CI inputs, but **do not certify their publication-date or organizational claims**.
- This is a syntactic and elementary structural input gate—not a full RFC 4180 formal certification, package-vulnerability scanner, complete source-coverage audit, DOI resolver, independent empirical verification, or permission to release private data. Tests remain synthetic except for ordinary pre-existing, source-unverified public repository fixture files scanned by CI.

**Preservation:** #251's useful tracked-Git versus filesystem selection semantics and #253's stricter size/CSV tests remain reviewable in their GitHub branches; the common validated subset is integrated here. Avoid merging three redundant validators or overwriting the current Python 3.10/3.12/3.14 SHA-pinned Actions workflow.
