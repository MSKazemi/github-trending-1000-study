# Literature inclusion and duplication ledger — issue #7

**Status:** reproducibility instrument, 2026-10-12. **No systematic database search was run, no peer-reviewed corpus assembled, and no PRISMA flow inferred from this tool.** Partial response to [issue #7](https://github.com/MSKazemi/github-trending-1000-study/issues/7).

## Run it offline

```bash
python -m trending_study.literature_ledger --input SCREEN.json
python -m unittest discover -s tests -p 'test_literature_ledger.py' -v
```

The JSON requires `search_runs` with distinct `run_id`, `database`, **verbatim query**, UTC search date; `records` each with `record_id`, the run ID, `title`, publication year, optional DOI, `source_type` and screening `decision` (include, exclude, pending). Exclusions require reasons. Included studies require a plain-language extraction of `design`, `population`, `outcome` and `limitations`. A reviewer must verify DOI resolution and source identity; syntax validation does not prove a DOI exists.

DOIs normalize `doi:` (with optional spacing) and `https://doi.org/` / `https://dx.doi.org/` aliases. Duplicate DOI keys and missing-DOI title+year collisions are flagged for **human adjudication**, not automatically discarded. Multiple publications, conference-to-journal extensions, versioned arXiv records and studies of the same dataset must remain traceable. Source types include peer-reviewed, preprint, standard, news and vendor so opinion/press cannot be silently counted as peer-reviewed evidence.

## Required full review (not yet done)

1. Fix search strings before screening and register database coverage (ACM DL, IEEE Xplore, OpenAlex, Scopus if authorized, other sources explicitly documented).
2. Store per-search run query, filters, dates, hits, export file hashes and permission/redistribution boundaries. Archive permitted metadata only; do not copy paywalled text.
3. Double-screen titles/abstracts then accessible full texts, prespecify inter-reviewer conflict handling and reasons for full-text exclusions.
4. Extract denominator, task, evaluation design, effect/uncertainty, code/data reproducibility, external validity and adverse/null findings.
5. Build version-pinned references and a flow table **only from observed audited counts**, distinguishing inaccessible papers from excluded papers. Do not report 'zero papers found' for unavailable database search.
6. Audit retracted/corrected work and historical version timestamps; tie each retained empirical claim to a specific edition and confidence.

**Practical application:** before deciding a fashionable AI agent makes a repository greener or more reused, distinguish company performance claims, uncontrolled online benchmarks, and independently evaluated longitudinal user tasks. See [evidence grading](EVIDENCE_TO_LESSON_PROTOCOL.md) and [source watch](SOURCE_MONITORING_AND_JOURNALS_2027.md).

**Limit:** the offline validator proves only logical consistency of supplied screening records, not complete retrieval, inclusion validity or peer review.

**Input error contract (2026-10-13):** Each record's `run_id` must be a nonblank string matching a declared search run. Malformed JSON types (including arrays and objects) raise a controlled `LiteratureError`, never an uncaught hashability exception; regression tests cover these cases. This validator does not authenticate the claimed source or reviewer.

**Reusable reading bibliography:** For legal publisher/author-manuscript PDF links and journal-vs-preprint separation, see [the open-access journal evidence register](OPEN_ACCESS_JOURNAL_EVIDENCE_2026_10_12.md). Do not treat this link as a completed systematic search.


## 2026-10-13 scientific hardening: PRISMA-constrained screening

Change: the offline ledger now rejects future-dated search runs and reports **title/year collisions even when candidate DOIs differ**, while retaining independent DOI-identity duplicate groups. No records are deleted, no two reports are assumed to represent two independent studies, and no PRISMA flow is asserted to have been authenticated.

**Protocol to freeze before search:** explicit PICOC-style research questions; eligibility (source type, population, outcome, date ranges, language/format, exclusions); exact per-database query and filters; earliest/latest snapshot UTC and access rights; version of automatic deduplication; reviewer identity/blinding protocol; independent full-text decision and extraction fields. Search ACM, IEEE, Scopus/OpenAlex and supplemental citation chaining only where permissions allow, recording records found per actual run. Do not label vendor announcements `peer_reviewed` without original venue verification.

**Unit caveat:** one scientific study may yield several reports/preprints; use DOI, normalized titles, author/year and full-text comparison to *flag* probable overlaps for independent human adjudication. Two different DOIs with matching titles may be distinct corrections, not automatic duplicates. Keep exclusions and conflict reasons; store study design, sample/task frame, effect estimates, uncertainty, ethics, limits, implementation cost, reuse outcomes, and carbon measurement boundaries separately.

**Sources:** [PRISMA 2020 (BMJ, 2021)](https://www.bmj.com/content/372/bmj.n71) and the [PRISMA 2020 reporting checklist](https://www.prisma-statement.org/prisma-2020). PRISMA is a reporting guideline, not evidence that this project performed a systematic review. The current example and tests remain synthetic; real screening has not happened.

**Practical repository lesson to test:** cite the original method and independent evidence for each reusable coding practice; keep negative results and methodological contradictions, not only promotional articles.

## 2026-10-13 merge follow-up: mandatory source traceability for inclusion

An audit found that a record could previously be marked `include` while its `source_url` was absent. For a research evidence register, this makes even first-pass verification irreproducible. The offline instrument now requires every **included** record to supply a canonical HTTPS `source_url`, without embedded credentials, query strings, fragments, whitespace or an absent host. A valid DOI can use its `https://doi.org/10...` resolver page as this link; this is a **claimed reference**, not proof that the DOI resolves or that publisher/venue and findings are correct. Unverified search leads may remain `pending` without a URL and are never implicitly counted as included. Synthetic tests cover malformed/missing links and continued conservative treatment of pending leads.

**Scientific safeguard:** a syntactically valid HTTPS URL is not proof of content authenticity, peer-review status, human double-screening, right to access, or unbiased retrieval. Real systematic reviews must preserve the exact retrieved title/abstract, query, source export identifier and permission-appropriate source record, then obtain independent link/date/venue review before publication. Existing PR #189 was merged separately; this follow-up records the specific integration correction without rewriting historical claims.
