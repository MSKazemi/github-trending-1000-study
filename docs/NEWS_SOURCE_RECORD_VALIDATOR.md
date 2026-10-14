# Offline news-source record validator (engineering subset of draft PR #59)

**Status: tested engineering instrument, not a curated or authenticated news corpus.** This change extracts the reusable `trending_study.news_corpus` source-ledger checker from [draft PR #59](https://github.com/MSKazemi/github-trending-1000-study/pull/59), without merging any of its 20 provisional third-party source summaries. PR #59 and its original branch retain the exact report texts, URLs, citations, review discussions and source IDs for independent screening.

## Purpose and reuse-first design

A repo maintainer can prepare a **candidate** JSON source record offline, check that it has all required provenance fields, and avoid accidentally treating a missing reviewer, conflicting URL, malformed date or article full-text copy as a validated scientific observation. The implementation **reuses** `trending_study.data_integrity._decode_document`, the existing strict duplicate-key/NaN/int-size reader and byte/file limits; no external package, scraper, download, authentication token, GitHub Actions write permission or second competing research decoder was added.

Run this fully synthetic example:

```bash
python -m trending_study.news_corpus --directory tests/fixtures/news_corpus
python -m unittest tests.test_news_corpus -v
python -m unittest discover -s tests -v
```

The bundled `NEWS-2026-0001.json` lives **only** under `tests/fixtures/news_corpus/`; `example.org` and the fictitious publisher represent no real article. Expected CLI output includes `"records": 1` and `"evidence_status": "provisional_structural_validation_only"`. It is not counted toward the proposed 1,000-news-item corpus, any GitHub Trending cohort, or a real experiment.

## Schema v1.0 and failure policy

Standalone reads inspect the opened file descriptor, refuse nonregular inputs,
and cap bytes actually read. This prevents a leaf symlink or FIFO substituted
after a preliminary path check from being read on platforms with no-follow
and nonblocking file flags. Aggregate limits count actual bytes, including file
growth after stat. This does not make ancestor-directory traversal a hostile
filesystem sandbox. Strict JSON rejection uses a controlled diagnostic rather
than echoing untrusted duplicate key names or recursion tracebacks.

The reader requires a stable `NEWS-YYYY-NNNN` ID matching the JSON filename; fixed version `1.0`; bounded title, publisher, topic and attributed-claim text; original publication/access `YYYY-MM-DD` dates not later than execution date; clean HTTPS canonical source URL and nonduplicated canonical URL identity. It only strips common marketing query trackers while retaining meaningful query selectors such as `ref` and `id`. Blank/malformed fields, duplicate IDs/URLs, missing expected data, malformed ports, user-info/fragment URLs, URL whitespace/control characters, malformed percent escapes and backslashes fail. Source folders must be ordinary directories; symlinks, nested folders, unexpected JSON names, unexpected files, oversized artifacts, and ambiguous/overlarge raw JSON fail rather than being silently omitted.

The validator permits only two **non-verifying** states:

- Real-source *leads*, still not independently corroborated: `included_provisional_single_reviewer` and `web_primary_page_inspected_not_independently_fact_checked`. These fields are self-reported by the submitting record, not checked against the Internet or a reviewer registry.
- Synthetic fixture: `synthetic_test_only` and `not_inspected_synthetic_fixture`, with no actual visited page.

Both require `review_status=pending`, `independent_reviewer=null`, `independent_corrob_status=not_assessed`, `fulltext_stored=false`. Any claim of verified human approval in v1 is rejected: a genuine independently reviewed source requires a separately justified versioned protocol and human confirmation, not simply a changed string.

**Limitations:** URL parsing is *syntactic*, not DNS checking, permanent canonicalization or publisher authentication. A valid date can be fabricated. Distinct URLs may report the same event; matching URLs may have been edited. The validator does **not** access or quote articles, authenticate licenses/consent, verify historical availability, assess corroboration, reproduce statistics, certify benchmarks, or establish adoption/productivity/energy impacts. The tool never upgrades a news lead to independent scientific evidence.

## How to finish draft PR #59

Retain all 20 original record files on the existing draft branch. Before any evidence records go to `main`, a qualified source/method reviewer must independently inspect the **exact primary documents, publication/event dates, URL revisions, rights and relevant independent counter-evidence**, record unresolved disputes and negative findings, freeze a documented inclusion/exclusion protocol, and rerun this instrument plus full exact-head CI. Do **not** report "20 authenticated sources" merely because 20 syntactically valid JSON files pass. Separate an engineering merge from scientific source acceptance.

**Practical lesson for other repositories:** merge small, testable **data-contract code** independently from unreviewed research content; keep original branches/PRs as immutable provenance until verified transfer; maximize safely reusable functionality and clear acceptance criteria instead of PR volume, stars or unsupported green-computing claims.
