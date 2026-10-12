# Literature inclusion and duplication ledger — issue #7

**Status:** reproducibility instrument, 2026-10-12. **No systematic database search was run, no peer-reviewed corpus assembled, and no PRISMA flow inferred from this tool.** Partial response to [issue #7](https://github.com/MSKazemi/github-trending-1000-study/issues/7).

## Run it offline

```bash
python -m trending_study.literature_ledger --input SCREEN.json
python -m unittest tests.test_literature_ledger -v
```

The JSON requires `search_runs` with distinct `run_id`, `database`, **verbatim query**, UTC search date; `records` each with `record_id`, the run ID, `title`, publication year, optional DOI, `source_type` and screening `decision` (include, exclude, pending). Exclusions require reasons. Included studies require a plain-language extraction of `design`, `population`, `outcome` and `limitations`. A reviewer must verify DOI resolution and source identity; syntax validation does not prove a DOI exists.

DOIs normalize `doi:` and `https://doi.org/` aliases. Duplicate DOI keys and missing-DOI title+year collisions are flagged for **human adjudication**, not automatically discarded. Multiple publications, conference-to-journal extensions, versioned arXiv records and studies of the same dataset must remain traceable. Source types include peer-reviewed, preprint, standard, news and vendor so opinion/press cannot be silently counted as peer-reviewed evidence.

## Required full review (not yet done)

1. Fix search strings before screening and register database coverage (ACM DL, IEEE Xplore, OpenAlex, Scopus if authorized, other sources explicitly documented).
2. Store per-search run query, filters, dates, hits, export file hashes and permission/redistribution boundaries. Archive permitted metadata only; do not copy paywalled text.
3. Double-screen titles/abstracts then accessible full texts, prespecify inter-reviewer conflict handling and reasons for full-text exclusions.
4. Extract denominator, task, evaluation design, effect/uncertainty, code/data reproducibility, external validity and adverse/null findings.
5. Build version-pinned references and a flow table **only from observed audited counts**, distinguishing inaccessible papers from excluded papers. Do not report 'zero papers found' for unavailable database search.
6. Audit retracted/corrected work and historical version timestamps; tie each retained empirical claim to a specific edition and confidence.

**Practical application:** before deciding a fashionable AI agent makes a repository greener or more reused, distinguish company performance claims, uncontrolled online benchmarks, and independently evaluated longitudinal user tasks. See [evidence grading](EVIDENCE_TO_LESSON_PROTOCOL.md) and [source watch](SOURCE_MONITORING_AND_JOURNALS_2027.md).

**Limit:** the offline validator proves only logical consistency of supplied screening records, not complete retrieval, inclusion validity or peer review.
