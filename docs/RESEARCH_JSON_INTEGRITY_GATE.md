# Research JSON integrity gate for PRs (issue #247)

**Implemented as an offline engineering control, 2026-10-13.** This is **not** a systematic literature review, an authenticated data capture, an ethics approval, a schema registry or empirical research evidence.

The GitHub Actions Python 3.10/3.12/3.13/3.14 **test matrix** compiles source, checks every Git-tracked Python and JSON artifact, runs offline tests, and smoke-tests CLI entrypoints. The separate **research-artifacts** job runs both pre-existing JSON/JSONL/CSV validators. Both jobs run on pull requests and pushes to `main`:

```bash
# Each Python matrix job
python -m compileall -q trending_study scripts tests
python scripts/check_research_artifacts.py --root . --tracked-code-json
python -m unittest discover -s tests -v
python -m trending_study --help
python -m trending_study.reuse_gate --help
python -m trending_study.goldset --help

# Separate research-artifacts job (Python 3.12)
python -m trending_study.data_integrity --root .
python scripts/check_research_artifacts.py --root .
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

## Nested symlink completeness hardening (2026-10-13)

A later audit of the canonical JSON/JSONL/CSV tool found that recursive discovery could encounter a **nested symlinked directory** without any eligible file suffix and silently omit its contents. The validator now explicitly rejects every symlink found in an evidence source subtree **before file-extension filtering**, including directory aliases. This prevents a superficially successful run from claiming full eligible input coverage while skipping an unreviewed subtree. Offline synthetic regression coverage is in `tests/test_data_integrity.py`. Symlink rejection does not authenticate the rest of the data, and a checked local SHA never proves GitHub or publisher origin.

## Preserved test evidence from legacy nested-symlink branch (2026-10-13)

The older `fix/canonical-nested-symlink-audit-20261013` branch adds useful negative witnesses even though the current validator and its existing tests already reject nested symlinked directories. The integration retains the stronger synthetic duplicate-key JSON witness **outside** a symlinked subtree and tests a symlink to an existing **extensionless file**; both must fail closed without following the link. The older branch commit `7301a0207032dee0175ff27d12e965fd6e8b3b48` is retained as a merge parent, not overwritten. The canonical implementation and its newer CSV/JSON numeric checks remain unchanged. This is offline integrity coverage, not evidence-source authentication or permission to collect data.


## 2026-10-14 — Git-tracked Python and JSON coverage (issue #244)

The existing, dependency-free `scripts/check_research_artifacts.py` now has an **additive** option, `--tracked-code-json`. This avoids shipping the competing standalone checker previously proposed by [closed PR #251](https://github.com/MSKazemi/github-trending-1000-study/pull/251). Its useful negative-test cases informed this integration.

```bash
python scripts/check_research_artifacts.py --root . --tracked-code-json
python -m unittest discover -s tests -p 'test_tracked_code_json_gate.py' -v
python -m unittest discover -s tests -v
```

The checker obtains a NUL-delimited, staged-mode-aware inventory from **`git ls-files --stage --cached --full-name -z`**, requires the supplied root to be the Git top-level, then checks every indexed `.py` or `.json` regardless of location (including hidden and unimported paths). It rejects symlink Git modes, missing checkout files, symlinked ancestor directories, oversized files, invalid Python syntax, malformed/non-UTF-8 JSON, duplicate object keys and nonstandard/overflowing/underflowing JSON numerics. Python code is compiled for comprehensive syntax validation **without imports or execution** (including contextual compiler errors such as module-level `return`). JSON is checked for syntax and ambiguity, not arbitrary research-schema fields; valid scalar JSON remains valid. Untracked build output is not represented as committed source, and Git submodule internals are not traversed.

The new check is run before unit tests on **each** CI Python interpreter (3.10, 3.12, 3.13, 3.14). The existing research-directory JSON/JSONL/CSV validations remain intact. Per-file and total-size limits (16 MiB, 128 MiB), a 5,000-file limit and an 8 MiB index-listing cap prevent silently skipping unusually large tracked input. On POSIX systems with `dir_fd`, `O_DIRECTORY` and `O_NOFOLLOW`, the checkout reader opens each ancestor relative to its parent descriptor to reject directory-to-symlink swaps after prechecks. Other platforms retain best-effort pathname checks; neither path is a comprehensive hostile-filesystem sandbox. A Git index is required for the opt-in mode; if it is missing or unreadable, the command fails rather than claiming coverage. This remains a bounded read-only checkout inspection, not a race-hardened filesystem sandbox or verifier of the index blob bytes against external trusted origins.

**Evidence boundary:** Git-tracked coverage and green CI are engineering claims about the particular checkout and interpreter. They do not authenticate source URLs, historical observations, ethics/legal permission, code safety, reviewer independence, approved preregistration or any environmental impact. Repository branch-rule enforcement and independent human merge review remain separate open gates tracked in [#248](https://github.com/MSKazemi/github-trending-1000-study/issues/248).

Because every tracked `.py` and `.json` file is checked, deliberately malformed fixtures must be generated at test time (for example in a temporary directory) rather than committed.

**Practical lesson:** put a negative regression in a surprising location (for example `ops/broken.json` or `.hidden/broken.py`) and prove your CI rejects it. A scanner that only knows familiar directories cannot promise full tracked-file coverage.


## 2026-10-14 follow-up: staged Git blob divergence

The tracked-code/JSON gate also validates each eligible regular **Git index blob** using `git cat-file`, independently of the checked-out working-tree bytes. This catches an important local pre-commit failure mode: a contributor stages invalid Python/JSON and subsequently repairs only the working copy. Both representations must be parseable; differing but valid contents are allowed. The output `tracked_code_json.index_checked_bytes` counts inspected staged bytes, separately from `checked_bytes`. Blobs and working files each have independent 16 MiB/file and 128 MiB/aggregate bounds; blob type and declared size are checked before reading bytes. No clean/smudge filters or staged source code are executed.

Four offline Git-index tests cover hidden staged duplicate JSON keys, staged module-level Python errors, valid divergent content and oversized staged blobs. CI checks the checkout and index actually supplied by GitHub Actions; this does **not** prove the local staging area, Git host provenance, file signatures, package safety, or trustworthiness of scientific observations. An authorized reviewer must still approve the PR and separately enable repository branch rules (#248).


## 2026-10-15 validation-error privacy hardening

The validator now reports **duplicate JSON object key** without copying the
caller-provided key into a CI failure. Keys in untrusted research files can
contain accidentally pasted tokens, names or other sensitive material; their
values are not necessary to locate the offending tracked file. The tracked
Git-index scanner checks **both** the checked-out file and the staged Git blob.
Synthetic negative regression checks assert redaction for both paths, and
a CLI regression checks that a token-shaped duplicate key is absent from
`--tracked-code-json` failure output. This
protects one diagnostic class, not arbitrary private information in other
file names, Python syntax tracebacks or source materials. Treat CI logs as
public outputs and independently review proposed data before uploading it.
