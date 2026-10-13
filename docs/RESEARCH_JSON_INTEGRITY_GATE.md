# Research JSON integrity gate for PRs (issue #247)

**Implemented as an offline engineering control, 2026-10-13.** This is **not** a systematic literature review, an authenticated data capture, an ethics approval, a schema registry or empirical research evidence.

The GitHub Actions Python 3.10/3.12 matrix runs three steps before treating a pull request as technically verified:

```bash
python -m compileall -q trending_study tests
python -m trending_study.data_integrity --root .
python -m unittest discover -s tests -v
```

The canonical standard-library validator inspects committed `.json`, `.jsonl` and `.csv` research files under `examples/`, `references/`, `research/`, `research-notes/` and `templates/`. It **does not read, rewrite, delete, fetch or enroll** real raw captures. It deterministically fails on duplicate object keys (including deeply nested keys), malformed JSON or UTF-8, nonstandard JSON `NaN`/`Infinity`, overflowing floating-point literals, empty JSONL, symlinked JSON files/directories and files exceeding 16 MiB. JSONL errors include the actual record line number.

## Why this protects the study

Python's default `json.loads('{"status":"unknown","status":"verified"}')` normally retains only the last key. A duplicate may therefore **silently change the apparent evidence state**, source URL, DOI, repository ID or experimental denominator. A conventional syntax check alone does not reject this. We now fail closed **before merging**, retaining original files so a human can investigate.

The validator's output counts parsed documents and JSONL records, not confirmed articles, code-reuse successes, human reviewers or study participants. A source file that is structurally valid may still contain fabricated, outdated, misleading, incomplete or non-consensual assertions. Independent source/date/DOI/rights checks, study-specific schemas, scientific adjudication and human PR review remain mandatory.

## Operator workflow

When the CI step fails, open the referenced path and (for JSONL) line. Compare against the original source and the intended canonical schema. Repair only on a new branch, preserve original evidence when required by the research provenance policy, add a regression test, and rerun the full matrix. Never resolve a duplicate by blindly keeping the last value or replacing unknown with zero.

This gate is deliberately conservative but limited: it checks only selected research files in the listed directories for JSON/JSONL/CSV syntax and malformed numeric inputs, not Markdown links, research-statistical logic, provenance, private data rights, or source authentication. If a legitimately large artifact exceeds 16 MiB, document and review a format/sharding amendment instead of silently bypassing the gate.

## 2026-10-13 additive extension — CSV and numeric preservation (issue #240)

Instead of introducing a second competing validator, the canonical `trending_study.data_integrity` module now also screens `.csv` artifacts in the same research directories. It rejects empty/duplicated column names (case-insensitive), malformed UTF-8/CSV quotes, uneven row widths, embedded NUL bytes, nested symlinks, and oversized inputs. Quoted commas and multiline CSV cells remain valid; the checker is offline, read-only and never interprets spreadsheet formulas.

For JSON/JSONL, the new guard additionally rejects finite-looking decimal literals that would **underflow to zero** in ordinary floating-point conversion, and integer tokens longer than a conservative 1,024-digit safety boundary. These are **parsing-safety rules** rather than claims that all large numbers are scientifically invalid. Applications requiring larger numeric values must explicitly review and version the format instead of silently weakening the gate.

The original response field `json_documents_or_jsonl_records` retains its previous **JSON-only denominator**. New fields `csv_records` and `total_logical_records` report CSV row counts separately, so an existing report cannot be reinterpreted as having acquired additional JSON observations. Successful validation still says nothing about truthful observations, empirical reproducibility, source licensing, consent or statistical correctness.

Run:

```bash
python -m trending_study.data_integrity --root .
python -m unittest discover -s tests -v
```

This extension reuses existing tested code from [issue #247](https://github.com/MSKazemi/github-trending-1000-study/issues/247) instead of copying another integrity CLI proposed in [issue #240](https://github.com/MSKazemi/github-trending-1000-study/issues/240). The source reports from competing draft PRs remain separate and require **human no-loss reconciliation**.

**Practical reusable lesson for your repositories:** enforce unambiguous machine-readable evidence and traceable failures in CI before optimizing stars or claiming reproducibility; no checksum or passing unit test can replace independent verification of the underlying observation.
