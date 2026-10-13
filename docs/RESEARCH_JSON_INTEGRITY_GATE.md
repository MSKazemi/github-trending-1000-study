# Research JSON integrity gate for PRs (issue #247)

**Implemented as an offline engineering control, 2026-10-13.** This is **not** a systematic literature review, an authenticated data capture, an ethics approval, a schema registry or empirical research evidence.

The GitHub Actions Python 3.10/3.12/3.14 matrix runs three steps before treating a pull request as technically verified:

```bash
python -m compileall -q trending_study tests
python -m trending_study.data_integrity --root .
python -m unittest discover -s tests -v
```

The standard-library validator inspects committed `.json`, `.jsonl` and `.csv` research files under `examples/`, `references/`, `research/`, `research-notes/` and `templates/`. It **does not read, rewrite, delete, fetch or enroll** real raw captures. It deterministically fails on duplicate object keys (including deeply nested keys), malformed JSON/CSV or UTF-8, nonstandard JSON `NaN`/`Infinity`, overflowing or underflowing nonzero floating-point literals, extremely long integer tokens, empty JSONL, malformed/duplicate CSV headers, inconsistent CSV row widths, embedded NUL bytes in CSV, symlinked data files/directories and files exceeding 16 MiB. JSONL errors include the actual record line number.

## Why this protects the study

Python's default `json.loads('{"status":"unknown","status":"verified"}')` normally retains only the last key. A duplicate may therefore **silently change the apparent evidence state**, source URL, DOI, repository ID or experimental denominator. A conventional syntax check alone does not reject this. We now fail closed **before merging**, retaining original files so a human can investigate.

The validator's output counts parsed documents and JSONL records, not confirmed articles, code-reuse successes, human reviewers or study participants. A source file that is structurally valid may still contain fabricated, outdated, misleading, incomplete or non-consensual assertions. Independent source/date/DOI/rights checks, study-specific schemas, scientific adjudication and human PR review remain mandatory.

## Operator workflow

When the CI step fails, open the referenced path and (for JSONL) line. Compare against the original source and the intended canonical schema. Repair only on a new branch, preserve original evidence when required by the research provenance policy, add a regression test, and rerun the full matrix. Never resolve a duplicate by blindly keeping the last value or replacing unknown with zero.

This gate is deliberately conservative but limited: it checks only files in the listed directories and only JSON/JSONL/CSV lexical and tabular integrity, not Markdown links, research-statistical logic or source authentication. If a legitimately large artifact exceeds 16 MiB, document and review a format/sharding amendment instead of silently bypassing the gate.

**Practical reusable lesson for your repositories:** enforce unambiguous machine-readable evidence and traceable failures in CI before optimizing stars or claiming reproducibility; no checksum or passing unit test can replace independent verification of the underlying observation.

## CSV and numerical preservation extension (2026-10-13)

**Enterprise integration decision:** carry forward the unique useful **CSV grammar, headers and row-width checks** proposed in [PR #253](https://github.com/MSKazemi/github-trending-1000-study/pull/253) into the already-merged canonical `trending_study.data_integrity` validator from [PR #250](https://github.com/MSKazemi/github-trending-1000-study/pull/250). Keep one public CLI and the existing read-only three-Python-version CI matrix, immutable official actions, current smoke tests and source snapshot rules. Do not merge another competing CI workflow to gain these checks.

The extension performs read-only, strict CSV parsing with correct quoted commas and multiline cells; rejects case-insensitive duplicate/blank header names, malformed quoting, irregular column counts, embedded NUL bytes and malformed UTF-8. It counts CSV files/data rows separately so the original `json_documents_or_jsonl_records` measure remains backward compatible. JSON float parsing now distinguishes true zero from nonzero underflow to zero, and rejects >1024-digit integer tokens to avoid version-dependent interpretation and resource exhaustion. Six new tests exercise correct and failure cases. The checked-out source content is **never modified or discarded**.

**Scope limits:** The checker does not verify semantic column types, third-party source identities, GDPR/ethics permissions, whether numeric quantities have real measurement methods, or whether the source is historically accurate. Duplicate column rejection is a deliberate dataset contract; source providers with repeated names must be preserved and mapped in an independently documented amendment rather than silently renamed by an agent. CSV formula strings are read as literal data and never executed. A header-only CSV yields zero observed data rows, not an inferred negative research result.

[PR #251](https://github.com/MSKazemi/github-trending-1000-study/pull/251) proposes an additional *Git-tracked Python AST* check (including scripts outside `trending_study/`), which remains a separate possible improvement, not a reason to duplicate the integrated JSON/CSV evidence contract. Preserve useful test cases and original PR discussion. Report all claim statuses and unknown/missing denominators faithfully.

**Reusable lesson for your own repositories:** test not just that data parses, but that a parser cannot silently *change its meaning*: two duplicate fields should never discard an earlier status, a tiny positive measurement must not become zero, and a CSV header must not be interpreted ambiguously.

## 2026-10-13 final integration: bounded cardinality and explicit empty CSV

Concurrent changes had already brought the CSV grammar and numeric underflow tests from #253 into this **canonical** validator, so no copy of those implementations was merged again. This follow-up adds only the missing requirements: at most **5,000** research JSON/JSONL/CSV artifacts and **128 MiB** total inspection bytes (besides the existing 16 MiB per file), explicit rejection of a CSV containing headers but no data rows, and backward-compatible counts `total_research_records` / `checked_bytes`. Tests include mixed JSON/CSV data and budget failures. The separate strict tracked-artifact gate from #253 was **not** deleted or overwritten; its own test/CI scope remains visible pending a future deliberate consolidation.
These are input-integrity bounds, **not** externally validated research or a guarantee against intentionally malicious repositories.

## 2026-10-13 post-merge consistency review

The original overlapping PR #253 was merged concurrently and already preserved the dated [PR collision audit](PR_AUDIT_2026-10-13.md) plus the separate script validator. Therefore PR #264 no longer adds a duplicate CSV parser or deletes either existing CLI. Its final reviewed change adds regression tests for CSV quoting and aliases, aligns both scanners to fail closed on header-only **empty input data** (not claim zero observations), and limits redundant CI branch-push runs to PR checks plus post-merge main checks. The two validators remain separate until a specifically versioned backward-compatibility review; a green syntax gate never validates the true source, participant consent or sustainable savings.

## Nested research-source link safeguard (2026-10-13)
The canonical scanner fails closed if a nested symlink, even one without a JSON/CSV suffix, appears under a source directory. `Path.rglob` can otherwise return an internally consistent count while omitting a symlinked subdirectory containing unchecked records. Negative regression cases cover nested directory and file aliases; no link is followed or external data read. This retains unique findings from the overlapping [PR #261](https://github.com/MSKazemi/github-trending-1000-study/pull/261) while preserving the current canonical module, primary/supplementary CI, user records and scientific caution.
