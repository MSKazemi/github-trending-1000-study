# Independent two-reviewer Trending page audit — issue #2

**Date:** 2026-10-12. **Status:** implemented offline audit scorer and synthetic tests; **no permitted live page has been captured and no actual 30-row human audit has been completed** in this turn. GitHub collector/parser remain **not validated for cohort enrollment**.

## Scientific purpose

An HTML parser may emit a perfectly plausible **positive subset** when GitHub changes the class or markup for some actual repository rows. Checking only `article.Box-row` consistency can miss those off-selector entries; a checksum guarantees integrity of the *saved* capture, not recall against everything visibly displayed. The only credible test is to have reviewers independently inspect **all visible rows**, including first, middle and last, before looking at the parser result.

The issue's acceptance target is a **minimum of 30 actual displayed entries across daily, weekly and monthly**, with exact original timestamp/window, at least two independent assessors, recorded disagreements/adjudication, rank matching, and an explicit permission review. Thirty rows is an initial engineering QA floor, not a population-representative confidence estimate or a sample-power calculation.

## Runbook (real evidence requires permission and actual human reviewers)

1. **Before visiting pages:** review GitHub's current Terms, robots and permitted usage for the proposed frequency and locations; do not bypass access restrictions or schedule uncontrolled scraping. This offline audit tool itself **does not connect to any website**.
2. **Make deliberate captures:** only if authorized, run the existing `capture --date <today UTC> --window daily|weekly|monthly --output ... --manifest-output ...` command once per permitted window. The current strict source-manifest parser handles **unfiltered global pages only**, not the proposed six language filtered surfaces. Preserve the raw HTML and contemporaneous SHA-256/UTC manifests under `data/raw/` (ignored by Git); do not rewrite files on a retry.
3. **Distribute a sealed snapshot to two independently acting reviewers**; each reviewer records *all* visually displayed owner/repository names in exact on-page rank order, including ambiguous or failed-to-read rows as **unresolved in reviewer notes**, not a fabricated zero. Record pseudonymous reviewer ID, actual reviewed UTC, SHA of source, source URL/window and `blind_to_parser_output: true` only if they genuinely did **not** view parser output. The reviewers must annotate separately before a third person assembles the bundle.
4. **Assemble a local bundle:** copy [`templates/page_audit_bundle.template.json`](../templates/page_audit_bundle.template.json) to e.g. `data/raw/qa-bundle.json` (not to the public Git repository); replace every placeholder, include one page element for each captured window, and ensure its referenced raw/manifest files are descendants of the bundle directory. Each page requires the two complete reviewer row lists and original captured-at metadata, with no assumptions about actual dates or sources. Use `evidence_kind: "field_self_reported"` only for real human judgments; synthetic fixture data must be tagged `synthetic_fixture`.
5. **Score all supported pages in one immutable report**, with the actual required cohort QA floor:

```bash
python -m trending_study audit-pages \
  --bundle data/raw/qa-bundle.json \
  --output data/processed/qa-report.json \
  --min-rows 30 --require-consistent
```

Optionally add `--markdown-output data/processed/qa-summary.md` alongside `--output data/processed/qa-report.json` for a **derived, reviewer-readable** table of resolved/adjudicated/unresolved denominators and per-page dispositions. The JSON remains the canonical versioned audit; the Markdown intentionally omits reviewer identifiers and capture URLs. Both files use the existing write-once publisher and are prechecked for collisions. **They are not an atomic multi-file transaction**: if a second file cannot be published, preserve any first file for incident review rather than silently repairing it.

If labels disagree or parsed rows omit/mis-rank a manually verified item, `--require-consistent` returns a nonzero exit code **but still writes the report once**. Do not erase or rewrite the report; record a new attempt/incident. No network requests occur during audit. The report is write-once and cannot clobber another study artifact.

6. **Independent third-person check and disposition:** authenticate the source capture and reviewers' independence, resolve any disagreements explicitly in a separate amendment/annotation record rather than overwriting original labels, review missed/off-selector rows, confirm 30 actual rows spanning three windows, then decide which parser version should be used. Any document claiming signoff requires a named consenting reviewer and real evidence URI outside tool-generated JSON.
7. **Gate cohort use:** even an automatic `automated_documentary_check: "pass"` yields `eligible_for_confirmatory_cohort: false`. Eligibility requires signed methods approval, permissible source access, stable numeric repository IDs, specified filters, power/preregistration and actual human validation; see [preflight](PROTOCOL_FREEZE_STATUS_2026_10_12.md).

## Input format

The bundle has `schema_version: "1.0"`, `evidence_kind: "synthetic_fixture"|"field_self_reported"` and `pages[]`. Each page references `raw_path` and `manifest_path` **relative to the bundle directory**, plus exactly two reviewer entries. Files outside this directory, absolute paths and symlink escapes are refused.

Each reviewer has `schema_version: "1.0"`, `reviewer_id` (pseudonym), `reviewed_at_utc`, `blind_to_parser_output: true`, `source_sha256`, `source_url`, `captured_at_utc`, `window`, and a complete 1-based ordered `rows[]` list of `{"rank":1,"repository":"owner/repo"}`. Reviewed time cannot precede captured time or be more than five minutes ahead of the validator's UTC clock (to tolerate minor clock skew); this chronology check is not third-party timestamp authentication. Source fields must match the actual saved manifest; ranks must be contiguous and identities unique. Two copies from one annotator may **pass documentary checks but are not independent human evidence**—human source and review verification remains required.

### Optional reviewer-C adjudication (issue #169, synthetic instrument)

The **existing** `audit-pages` CLI accepts an optional `adjudicator` object for a page in the same local bundle. It is an addition to the existing A/B records, not a replacement for them and not a second page-QA command. **Only supply it when reviewers A and B genuinely disagree**. The third reviewer must inspect the preserved original source; the code checks the declared identity, timing, source fields and rank restrictions but cannot establish genuine human independence.

The `adjudicator` object contains all ordinary reviewer fields and the *additional required* `disagreement_ranks` (the exact ascending ordinal ranks listed in the A/B discrepancy report) and a short `adjudication_reason` (1–500 characters, no personal details). Use a pseudonymous `reviewer_id` distinct from both A and B (case-insensitive), with an explicitly UTC `reviewed_at_utc` **later than both** original review records. It must repeat the original source SHA, URL, capture timestamp and window, and attest `blind_to_parser_output: true` truthfully.

For example, if the first reviewer says rank 1 is `synthetic-team/one`, reviewer B says `synthetic-team/two`, and all other ranks agree, C may label that rank after a real reinspection. C **cannot change already agreed positions, invent extra undisputed rows, or omit agreed rows**. C may independently choose either reviewer's label or a different observed identity *at the disputed position only*. Both original A/B annotations, the disagreement ranks and C's reviewer reference are retained in the report. If C is absent, incorrect, or invalid, the page stays unscored or fails closed, never silently acquiring a gold standard.

The report preserves `reviewer_agreement` as the unmodified A/B comparison and adds `reference_resolution` (`a_b_agreement`, `c_adjudicated`, or `unresolved`), `adjudicator_id`, `adjudicated_disagreement_ranks`, `labels_resolved`, `pages_with_adjudicated_annotations`, `pages_with_resolved_annotations`, and `windows_with_resolved_labels`. Aggregated denominators include only pages with full **resolved** labels (by A/B agreement or valid C); unresolved pages remain excluded and explicitly counted. The 30-row/three-window threshold uses resolved labels and never authenticates reviewers or permits confirmatory enrollment.

For a synthetic C case in your **private** bundle (only one page shown, with normal capture metadata omitted):

```json
{
  "pages": [{
    "raw_path": "daily.html",
    "manifest_path": "daily.manifest.json",
    "reviewers": ["<existing complete reviewer A record>", "<existing complete reviewer B record>"],
    "adjudicator": {
      "schema_version": "1.0",
      "reviewer_id": "reviewer-C-pseudonym",
      "reviewed_at_utc": "2026-10-12T15:00:00+00:00",
      "blind_to_parser_output": true,
      "source_sha256": "<same checked manifest source_sha256>",
      "source_url": "<same checked manifest source_url>",
      "captured_at_utc": "<same checked manifest captured_at_utc>",
      "window": "daily",
      "rows": [{"rank": 1, "repository": "synthetic-team/one"}],
      "disagreement_ranks": [1],
      "adjudication_reason": "Synthetic illustration; actual C must independently inspect all rows."
    }
  }]
}
```

The snippet is **illustrative, not a valid complete QA bundle or a real reviewed source**: C must enumerate *every* displayed row and all provenance fields must match the actual saved manifest. Reviewer identities/timestamps/notes are self-declarations, not third-party proof. Do not publish real reviewer names or private evidence in the repository. Actual approval is independent of these synthetic regression tests.

The scorer uses the same validated manifest checks as `pilot-parse`, but **can report a parser rejection as an abstention** rather than discarding all human evidence. A rejected captured page counts as zero emitted entries (and missed manual rows) for the QA effective-recall denominator; this is operational noncoverage, not evidence of a non-trending day.

## Report interpretation, denominators and limitations

| Field | Definition | Warning |
|---|---|---|
| `audited_gold_rows` | Sum of *resolved* complete-page labels (A/B agreement or valid C); excludes unresolved pages | Never an actual observation count when input is synthetic |
| `correct_identity_at_rank` (TP) | Exact repository identity **at exact ordinal rank** matches parser output | Rank error adds one FP and one FN |
| `false_positives_including_rank_errors` | Emitted entries not identical to gold at that ordinal position | Not a statement of GitHub algorithm quality |
| `false_negatives_including_rank_errors` | All resolved visible entries without an exact emitted rank match, including entirely rejected pages | A parser-abstention is incomplete collection, not an empty source page |
| `precision_on_emitted_rows` | TP / emitted entries (null if no emitted entries) | Descriptive for these observed pages, not a global estimate |
| `effective_rank_recall_including_parser_abstentions` | TP / resolved labeled visible entries, counting rejected pages as emitting zero | Excludes unresolved A/B disagreement without validated C; report these counts separately |
| `annotation_disagreement_ranks` | Positions where reviewer A/B lists differ | Unresolved pages **must not** be scored as ground truth |
| `coverage_minimum_met` | >=30 resolved labeled rows and daily+weekly+monthly all represented | Documentary threshold **alone cannot verify genuine independent reviewers** |
| `automated_documentary_check` | Pass only when each page has two agreeing annotations **or** valid C adjudication, supported windows, 30+ resolved rows, and exact parser/label matches | **Not** access/ethics clearance, GitHub source attestation or cohort eligibility |
| `scientific_status` | `synthetic_only_not_empirical_evidence` or `self_reported_requires_independent_human_and_source_review` | No tool output can autonomously certify human independence |
| `eligible_for_confirmatory_cohort` | Always false here | Other study gates and external signoff remain missing |

No population sampling interval or CI can be inferred from three nonrandomly selected pages. Weekly and monthly windows are overlapping, not independent observations of developer adoption or stars. **The parser does not evaluate a programming-language-filtered page until those URL/filter semantics have been implemented and audited separately.**

## This turn's honest execution status

- [x] Implemented a strict local capture-vs-blinded-label scorer that can catch an off-selector positive subset.
- [x] Two-source chronological provenance, missingness/rank/report gates and write-once audit output tested on **synthetic** pages.
- [x] Added a **36-row synthetic test across all three global windows**—this is **not** the requested 30 real audited rows.
- [ ] Review current GitHub robots/Terms via a reliable live source and obtain approval for actual repeat capture frequency.
- [ ] Capture actual day/week/month pages at documented UTC times and preserve raw bytes/manifests.
- [ ] Recruit two independent human annotators to label >=30 **real** source entries; any genuine third-person adjudication and signed independent review are still pending.
- [ ] Measure real TP/FP/FN/missed classes; quarantine/patch any supported layout drift.
- [ ] Validate six language-filtered pages separately if included in the preregistered sampling frame.

**Access limitation:** A direct HTTP check from the current code-execution environment on 2026-10-12 returned temporary DNS name-resolution failures for both `github.com/robots.txt` and a GitHub Trending URL. A web tool showed a cached page from roughly two months prior, not a current signed HTML capture. We did **not** bypass the restriction, retrieve current raw HTML, or infer current page counts from that cache. This is not a platform-permission ruling.

## Source links and related issues
[Current GitHub Trending](https://github.com/trending) · [GitHub robots](https://github.com/robots.txt) · [GitHub Terms](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service) · [Issue #2](https://github.com/MSKazemi/github-trending-1000-study/issues/2) · [Related structural limits](PARSER_STRUCTURE_QA_2026_10_12.md) · [Capture SOP](PILOT_CAPTURE_AND_PREFLIGHT.md).
