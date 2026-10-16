# Issue #100: no-loss preservation of a divergent GitHub source ledger (2026-10-16)

**Scope:** noncanonical documentary preservation only. Substantial AI assistance was used. This is **not** an independent source audit, an endorsement of source claims, a methods approval, or a claim that 19 more distinct product events occurred.

## Provenance and frozen comparison

- Historical branch: `research/issue-100-github-changelog-ledger-20261016` at `4ffbb5c953cf8d4dd477e9b7a13983845e76867d`.
- Original path: `research/company-intelligence/2026-04-12_2026-10-12/033-github.events.csv`, Git blob `0e12d6d668423379f4aaf72d4c5da6938ca4c98c`. The adjacent archived CSV is intended as an **exact byte-for-byte copy** of that already-public, author-prepared historical ledger; verify the archived Git blob SHA equals the original.
- Compared with `main@639054a0b98fe29c8bd0d6d72fb16b19fc26bff9`, canonical `033-github.events.csv` blob `a93f703f16fc30ed5e1b2759848b4532ef1ef686` (merged in [PR #414](https://github.com/MSKazemi/github-trending-1000-study/pull/414)). Recheck live main before any later use.
- Strict quoted-CSV structural comparison: **21 matching field names**, **19 historical rows** vs **63 main rows**; all records have 21 fields. The old branch has 19 distinct HTTPS GitHub Changelog `source_url` values; none is an **exact** URL match for the main ledger's 63 URL values. This does *not* establish independence of underlying product events or completeness of source search.
- **All 19 historical `event_id` values collide with identifiers in main**. Blind copying/appending to canonical `033-github.events.csv` would violate identifier uniqueness and could destroy provenance. These are *two different ledgers with reused local IDs*, not 82 authenticated independent events.
- The 19 old ledger publication-date fields are within the 2026-04-12 to 2026-10-12 proposed window. The contents are candidate vendor claims, not reproductions of authenticated raw source pages. No independent qualified reviewer, source-rights clearance, or true historical exhaustiveness is established.

## Integration and safety decision

1. **Keep canonical data unchanged.** This archived file under `docs/reviews/` is intentionally outside the research-data loader's documented `SOURCE_DIRS` and must not be treated as a second canonical company observation or added to sample denominators.
2. Keep the historical branch and the original main evidence intact. Do not force update/delete refs, overwrite prior source rows, or mark issue #100 scientifically complete because this copy exists.
3. Before a future canonical integration, a qualified source/method reviewer must independently inspect each source, check displayed vs effective dates and rights, resolve duplicate *underlying* events across vendor announcements, and assign unique durable IDs with an explicit old-to-new mapping. Preserve unknown, rejected, or overlapping rows in the audit trail.
4. Retain the same publication window and attribution classification. Do not infer adoption, task benefit, causal impact, security, or energy savings from GitHub release announcements alone.
5. Technical checks should confirm the archive blob SHA, exact record/field counts, main untouched, current pull-request CI and post-merge main CI. These checks do **not** constitute scientific validation.

## Practical lessons for maintainers

- **Compare stable content identifiers and row keys as well as Git ancestry.** A squash-merged branch may be behind in history while containing genuinely different records.
- **Never conflate new URLs with new events.** Group source documents by the underlying release/decision and effective date before calculating denominators.
- **Archive noncanonical candidate evidence separately.** Immutable provenance and explicit missing review are more useful than merging away conflicts or inflating result counts.
- **Use a review gate for promotions.** A successful CSV validator confirms structure, not truth, consent, source rights or methodological independence.

**Disposition:** this change only preserves an existing public preliminary ledger and its provenance; scientific inclusion in the current dataset is explicitly deferred. Related: [issue #100](https://github.com/MSKazemi/github-trending-1000-study/issues/100), [current merge gate](../PR_MERGE_QUALITY_GATE_2026_10_13.md).
