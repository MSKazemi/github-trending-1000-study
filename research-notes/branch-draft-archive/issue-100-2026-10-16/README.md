# Issue #100: preserved, noncanonical GitHub changelog draft

**Historical source-recovery archive (2026-10-18, Europe/Rome). Do not ingest this folder into the canonical study.**

This preserves all three original files from `research/issue-100-github-changelog-ledger-20261016` at commit `4ffbb5c953cf8d4dd477e9b7a13983845e76867d` **byte-for-byte**. The source branch was divergent from `main`; a full-tree merge would restore older versions of unrelated code and overwrite the later curated GitHub company-intelligence files. This selective no-loss merge carries the original commit history as a second Git parent while applying only archival copies of its three Git blobs.

## ID collision and independent-source status

At the explicitly pinned `main@566b6d6ad20701e02959241b4d7aab24c7af6d2f` checkpoint, the canonical file `research/company-intelligence/2026-04-12_2026-10-12/033-github.events.csv` had 63 records. The original draft contains **19 provisional first-party GitHub Changelog leads** with publication dates between 2026-04-23 and 2026-10-08 and a self-declared 2026-10-16 access date. All 19 `source_url` strings were absent from the 63-row canonical file at that checkpoint, **but all 19 draft `event_id` values (`CI2026-033-001` through `CI2026-033-019`) collide with different canonical records**. Different URL strings do not prove different underlying events; no source has been independently authenticated in this preservation step. These counts are time-bounded, not a new company sample or accepted 19-event finding.

| Original relative path, at source commit | Preserved relative path in this folder | Original Git blob SHA |
| --- | --- | --- |
| `033-github.events.csv` | `033-github.events.csv.txt` | `0e12d6d668423379f4aaf72d4c5da6938ca4c98c` |
| `033-github.md` | `033-github.md` | `55bfd1fbc52157445beca89787197df25b31ceea` |
| `033-github.search-log.md` | `033-github.search-log.md` | `4d237225ec142388dc4ae90c4529e70b6578e007` |

All three original files were under `research/company-intelligence/2026-04-12_2026-10-12/` on the source branch. The `.csv.txt` extension is intentional: these historical IDs **must not** enter automated canonical CSV corpus ingestion or study denominators. The byte-level original CSV remains recoverable by renaming an *offline copy*, not by editing this archived source.

## Future scientific reconciliation: not performed here

A qualified source reviewer must verify original URLs, publisher, title, UTC publication versus effective dates, corrections, archival access rights and contradictory evidence. Match events across the existing canonical 63 rows, retain rejected/missing/negative leads, and allocate genuinely new canonical stable IDs only for accepted unique events. Do not backfill review dates, claim independent source verification, assume vendor claims are functional performance, or infer 19 new independently validated user benefits. Never overwrite the write-once source archive. This is not a permission to capture blocked GitHub Trending pages, enable branch retirement, or delete the source branch.

**Practical lesson:** before merging agent-generated datasets, compare both primary-event identity and stable record IDs. Provenance-preserving archival of a conflicting draft is safer than a green CSV validator followed by a data-losing overwrite. See [issue #279](https://github.com/MSKazemi/github-trending-1000-study/issues/279).
