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

## 2026-10-14 offline input integrity correction

The direct CLI now shares the repository's strict
`data_integrity.decode_research_json` decoder. Duplicate object keys,
nonstandard/non-finite numbers, floating-point overflow/underflow, integers
exceeding 1,024 decimal digits and invalid UTF-8 fail before screening. Decoder
errors use a fixed diagnostic so arbitrary private keys and source filenames
are not echoed to the terminal.

Input must be a regular file of at most the existing research-JSON limit
(**16 MiB**). `audit_file` now reuses the shared
`data_integrity.load_research_json_file` bounded reader (2026-10-15) instead of
a local copy: the final input component cannot be a symlink on supported
platforms; directories and special files are rejected using `fstat`, and a
nonblocking open prevents FIFO inputs without writers from hanging. The read
itself also enforces the byte limit if the opened file grows after inspection.
Errors remain `LiteratureError` with fixed, non-path diagnostics. Included
`source_url` values also reject the ASCII DEL control character (0x7F) in
addition to space and C0 controls. No real source records changed. On platforms lacking
`O_NOFOLLOW`, the preliminary symlink check remains best effort; the cloud
Linux environment supplies the descriptor-level protection.

Included source URLs now force `urlsplit`'s deferred port validation, rejecting
nonnumeric, negative and out-of-range ports. Valid HTTPS source links (including
valid explicit ports), DOI normalization, exact search-query strings, existing
query/fragment restrictions and the report output fields retain their current
contracts. This is an input-integrity correction, not a scientific protocol
amendment or human literature review.

Reuse review: the MIT-licensed repository's strict decoder and lesson registry
reader were inspected before patching. They cover this bounded offline task
without another JSON implementation or external dependency. Python's official
[JSON documentation](https://docs.python.org/3/library/json.html) explains its
permissive duplicate/nonstandard defaults; its
[URL parsing documentation](https://docs.python.org/3/library/urllib.parse.html)
explains deferred port errors. New tests use synthetic files only and verify
CLI privacy, bounded inputs, no-follow behavior and FIFO rejection.

Additional 2026-10-15 regression: syntactically parseable but unusable
explicit HTTPS port zero and empty port delimiter are rejected; legitimate
nondefault HTTPS ports remain structurally acceptable. URL shape alone does
not certify a reachable or fact-checked source.


## 2026-10-15 source-specific URL integrity

An `include` decision now requires a nonempty HTTPS item path (rather than
accepting only a publisher homepage), and rejects literal backslashes or
malformed percent escapes in the canonical source URL. The previously enforced
host, port, credential, fragment and query constraints remain. Synthetic
negative tests protect this bounded source-link contract; an apparently clean
DOI/paper URL is **not** proof that the content was accessed, bibliographic
metadata verified, a systematic search performed or review acceptance met.
Preserve unresolved leads as pending rather than calling them included.


## 2026-10-15 small real-source version screen (NOT systematic)

The [versioned source pilot](../references/literature_version_pilot_2026-10-15.json)
and [reconciliation memo](LITERATURE_VERSION_RECONCILIATION_2026-10-15.md)
record public arXiv v1/v2, the subsequent ACM journal edition of
*Agentic Much?*, and the older ACM Queue SPACE framework. Four source
**records** represent only **two distinct research works**; the preprint
versions remain pending duplicate adjudication. Unlike the synthetic unit
fixtures, these source URLs and their dated abstract metadata were directly
inspected in a bounded public-web pass. This is not an actual ACM/IEEE/Scopus
systematic index search, a PDF/full-text audit, or a completed two-rater
screen. The pilot's `searched_at_utc` uses midnight on 2026-10-15 solely as
an **UTC date-precision normalization** required by the existing schema;
no claim is made that the queries ran at midnight or that the historical
search results have immutable exports. No PRISMA flow is certified. CI
ensures these linked source versions are never silently treated as four
independent empirical studies.


## 2026-10-18 offline included-citation host and exception-safety follow-up

A canonical item URL could previously pass the ledger's parser even if its hostname was an intranet single label (`https://intranet/paper`) or structurally invalid DNS (`example..org`, leading/trailing hyphens, underscores or overlong labels). The included-source structural gate now requires at least two ordinary ASCII DNS labels, each at most 63 characters with valid leading/trailing alphanumerics, and an overall host no longer than 253 characters. Valid interior hyphens and ASCII IDNA punycode remain accepted. The existing no-local/private literal IP and noncanonical numeric alias guards remain. All examples and tests are synthetic; a plausible domain is **not** proof of publication, provenance, licensed source rights, safe DNS resolution, or independent bibliographic screening.

Additionally, malformed URL parser failures are converted into generic `LiteratureError` only **after** leaving the source exception handler, so `__cause__`, `__context__` and a formatted full traceback do not retain synthetic private URL parser messages. A new negative test asserts this, alongside malformed-domain negatives and clean positive controls. No DOI, review decision, search count or observed publication claim is newly certified. Issue #7 remains open for actual date-stamped ACM/IEEE/OpenAlex/Scopus screening, source adjudication, independent reviewers and report completeness.

**Practical lesson:** validate *where evidence links could lead a reviewer* as conservatively as package registry URLs, but do not confuse structural URL format with scientific source authenticity. Check full traceback chains instead of only error text.
