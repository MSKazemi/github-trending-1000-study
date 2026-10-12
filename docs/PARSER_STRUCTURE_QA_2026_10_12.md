# Structural completeness and independent GitHub Trending page QA

**Date:** 2026-10-12. **Issue:** #2. **Current status:** structural fail-closed code with synthetic offline tests; **NO human-audited real Trending pages yet**. Do not close #2 or declare parser validation complete.

## Scientific failure mode

The previous parser deduplicated a list of detected `article.Box-row h2 a` links and failed only if it found zero entries. If one correctly marked repository still parsed but another supported row had changed or malformed markup, it could silently publish an incomplete, falsely compacted ranked list. A checksum validates bytes, not the completeness of parsed repository identities or positions.

## Structural safeguard now implemented

For every **supported** `<article class="Box-row"> ... </article>`:
1. Require exactly one `h2` header and one repository anchor under that header.
2. Require canonical relative `owner/repository` identity without dot/dotdot path segments, query URLs or offsite links.
3. Fail the **entire page parse** if any supported row is malformed, ambiguous, nested, truncated or duplicates a previous repository (case-insensitive).
4. Preserve original displayed ordering. Never quietly remove a duplicate and reassign subsequent ranks.
5. Report `selector_box_row_count` and `extracted_repository_count` in strict pilot audit, while leaving `parser_qa_status=requires_independent_manual_audit` and `cohort_enrollment_status=not_enrolled`.

**Strict scope:** this checks internal consistency against the **recognized Box-row selector only**. A page redesign could change another row's CSS class or render additional rows outside the recognized selector. Such omissions cannot be discovered from the selected rows alone. A positive structural check is **NOT** a gold-standard measure of live-page recall, ranking validity, current GitHub layout, or coverage of non-Box-row language panels. Conservative false rejection can also occur after legitimate UI changes.

## Required independent audit before permitting cohort data

1. Human reviewer validates permitted source access, original capture date/HTTP content, and the intended observation surface (global daily/weekly/monthly or each prespecified language view). No bots/bypass, no undocumented backfill.
2. Preserve at least one current raw capture and SHA/UTC manifest per supported surface, with exact page URL, parser commit, output file, and a manually recorded visible row count.
3. Have **at least 30 actual displayed rows** audited across the pilot's daily/weekly/monthly windows as the protocol minimum. Sample rows deliberately across top, middle and bottom; identify all displayed rows on audited pages so missed **off-selector** rows are findable. Report number and distribution of audited pages/rows. Thirty is an initial QA floor, not a powered population recall estimate.
4. Two independent readers capture exact owner/repo and displayed rank **before** comparing to parser output, resolve conflicts with a separate adjudicator where possible. Preserve disagreements rather than overwriting original annotations. See [audit card template](../templates/pilot_page_audit.md).
5. On the declared page/row denominator, compute TP (matched identities+rank), FP (incorrect emitted identities or ranks), FN (manual true visible entries missed), duplicate and ambiguity counts. For precision and recall report the actual denominators and appropriate uncertainty; if no valid denominator exists, mark recall **not estimable**. Document rows excluded and false refusals.
6. Repeat by page window and each later language surface as it is instrumented; **a global-page QA does not certify a language-filter parser**.
7. **Stop/revise** if any source permission fails, page row is missing, rank mismatch occurs, selector drift emerges, or inter-rater labels are unresolved. Record a dated incident and a versioned parser/protocol amendment. Freeze and review only after independently documented revalidation.

## Reproducible offline verification

```bash
python -m unittest discover -s tests -v
python -m trending_study pilot-preflight --input examples/pilot-preflight.example.json --stage confirmatory
```

The fixture `tests/fixtures/trending.html` now has two unique valid rows. Malformed positive-subset, duplicate, truncated, nested, multi-header, invalid URL, and unsupported-layout pages are synthetic regression tests. Neither these fixtures nor any passing CI run can be reported as real recall, a harvested Trending sample, or human-validated source evidence.

## Required publication artifact

Submit a reviewable **real** pilot page-QA record: capture SHA, code commit, UTC page date/window, audit reviewers, selection frame, counts and denominators, TP/FP/FN, rank disagreements and exact unsupported layouts. Version the record and attach raw audit file only where distribution is permitted. The tool must not claim `verified` until this actually happens.

Related: [pilot SOP](PILOT_CAPTURE_AND_PREFLIGHT.md), [capture immutability](CAPTURE_IMMUTABILITY_2026_10_12.md), [selection](SELECTION_PROTOCOL_2027.md), [source ethics](ETHICS.md), [readiness gates](PROTOCOL_FREEZE_STATUS_2026_10_12.md).
