# Independent page-level QA for GitHub Trending captures

**Status:** 2026-10-12 tooling, **not actual human-audit evidence**. Tracking [issue #2](https://github.com/MSKazemi/github-trending-1000-study/issues/2); existing [structural checks](PARSER_STRUCTURE_QA_2026_10_12.md) do NOT establish live-page recall. **No live page or 30 independently audited real rows have been collected here.**

## Purpose

A parser can accept every supported article.Box-row and still silently omit visible rows with changed markup. A source SHA256 checks local bytes, not complete extraction. This offline module compares actual parser output to TWO individually recorded, complete, blinded human annotation declarations attached to the same source URL and capture hash. It does **not** collect GitHub pages, invent human reviewers, authenticate origins or certify study cohort enrollment.

### 1. Preserve a permitted capture

Use the existing [pilot source-access SOP](PILOT_CAPTURE_AND_PREFLIGHT.md). Confirm rights/platform terms before recurring collection. Store one **write-once** raw HTML and manifest per observed page, with real UTC collection time, HTTP status/date, source URL, bytes and SHA. The current capture tool supports only unfiltered global daily, weekly and monthly pages; it does not implement language-filtered pages or a nine-surface panel.

### 2. Create independently authored complete-row annotations

Use two different consenting reviewer codes (pseudonyms) and inspect **ALL visible repository rows across each whole page**, not only parser-selected rows. Each reviewer must record exact rank and owner/repository before viewing parser output. Preserve source-specific independent originals, even with disagreement. The tool verifies declared format and mutual agreement but cannot authenticate that real humans did the work; actual independent signoff remains essential.

A structurally valid **placeholder only** (not true labels):

~~~json
{
  "schema_version": "1.0",
  "source_sha256": "ACTUAL_MANIFEST_SHA256",
  "source_url": "https://github.com/trending?since=daily",
  "annotation_scope": "all_visible_repository_rows",
  "reviewers": [
    {
      "reviewer_code": "reviewer_A",
      "declares_independent_blinded_annotation": true,
      "complete_visible_row_scan": true,
      "reviewed_at_utc": "ACTUAL_UTC_REVIEW_TIME",
      "rows": [{"rank": 1, "repository": "OBSERVED_OWNER/OBSERVED_REPO"}]
    },
    {
      "reviewer_code": "reviewer_B",
      "declares_independent_blinded_annotation": true,
      "complete_visible_row_scan": true,
      "reviewed_at_utc": "ACTUAL_UTC_REVIEW_TIME",
      "rows": [{"rank": 1, "repository": "INDEPENDENTLY_OBSERVED_OWNER/REPO"}]
    }
  ]
}
~~~

Replace every placeholder with independently inspected information. Multiple rows must have contiguous displayed ranks starting at 1. Reviewer declarations are self-attestations, **not automatic gold truth**. If reviewers disagree, this tool does not fabricate a consensus or a precision denominator; a separate adjudication and methods approval are required.

### 3. Build a local index

Save a JSON file next to the captures and annotations, listing relative in-directory paths; no absolute paths, path traversal or symlink escapes:

~~~json
{
  "schema_version": "1.0",
  "pages": [
    {
      "raw_file": "2026-10-12-daily.html",
      "manifest_file": "2026-10-12-daily.manifest.json",
      "annotation_file": "2026-10-12-daily.annotations.json"
    }
  ]
}
~~~

Include distinct actual captures from all three global windows for the initial 30-row coverage floor. Do not publish original source HTML or reviewer-linked identity without data rights/privacy review.

### 4. Execute the fully offline, write-once comparison

~~~bash
python -m trending_study.page_audit \
  --index data/raw/pilot-page-qa.index.json \
  --output data/processed/pilot-page-qa.report.json \
  --markdown data/processed/pilot-page-qa.report.md
~~~

Use --synthetic ONLY for explicitly invented fixtures. Otherwise the report label is UNVERIFIED_HUMAN_DECLARATIONS; neither state allows automatic research enrollment.

The CLI validates capture SHA/bytes, HTTPS source URL, captured time, declared HTTP status and HTML type before scoring. It fails on contradictory provenance, repeated capture, illegal paths, or invalid reviewer records. Audit outputs are immutable and include source, manifest and annotation SHA hashes.

**Measured only within agreed manually annotated pages:**
- TP: parser output matched both identity and visible rank.
- FP: parser-emitted (rank, repository) absent from agreed labels.
- FN: agreed (rank, repository) absent from usable parser output. Parser failure produces no usable output, with agreed rows operationally missed; precision is undefined when no rows were emitted.
- Same repository but wrong rank yields ranked FP+FN as well as a separate rank-disagreement count.
- Unresolved reviewer disagreements remain recorded and unscored; unknown is NOT zero or success.
- Precision=TP/(TP+FP); recall=TP/(TP+FN) with raw denominators, for audited agreed pages only. No general GitHub recall or unjustified row-independent confidence intervals.

The >=30 audited rows across all three global windows is a **minimum descriptive coverage floor**. It is not source permission, independent reviewer authentication, all-language coverage, statistically powered validation, or cohort readiness. Human review remains required even if all declared rows match.

### 5. Scientific next steps

Human reviewers must inspect original captures, document actual visible page counts and assess disagreements and layout changes. The proposed source-access and parser-audit preflight gates remain pending until permitted real pilot evidence and external signoff exist. If an off-selector row is omitted, fix the parser only via versioned, independently verified new tests. Stable GitHub IDs and 30/90/180-day follow-ups remain separate work under [selection](SELECTION_PROTOCOL_2027.md) and [longitudinal protocol](LONGITUDINAL_FOLLOWUPS_2026_10_12.md).

Run offline verification with the standard test suite:

~~~bash
python -m unittest discover -s tests -v
~~~

Tests use invented pages and labels for partial positive parses, structural failure, tampering, rank errors, reviewer conflict, duplicate captures, path containment and immutability. Passing CI is **not** an empirical finding.
