# Independent full-page Trending QA — offline workflow (2026-10-12)

**Scope:** bounded partial work on [issue #2](https://github.com/MSKazemi/github-trending-1000-study/issues/2). **Status: code and synthetic tests only.** No live GitHub Trending capture, independently annotated real rows, signed source-use approval, frozen 2027 protocol, or actual parser-recall estimate is claimed. Substantial AI assistance was used to implement the tool, **not** to simulate human review evidence.

## Research and access decision

The existing parser rejects malformed and duplicate supported `article.Box-row` entries, but it cannot detect all **off-selector** repositories on redesigned pages. A capture SHA proves local bytes, not visible-row completeness. To establish reliable observational evidence, compare the parsed result with **two genuine humans independently reading the entire saved rendered page**, without seeing the parser output.

**Important access hold:** the retrieved [GitHub robots.txt](https://github.com/robots.txt) shows `User-agent: *` and `Disallow: /*since=*`. The current capture URL pattern `https://github.com/trending?since=daily` matches that restriction. The [GitHub Acceptable Use Policies](https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies) limit automated bulk collection and permit use of public, non-personal information for research under stated conditions, including open-access research publication. This does **not** by itself authorize automated scraping or override robots restrictions.

**Do not run the repository's `capture` command against restricted Trending URLs, or schedule recurring requests, without an independently documented permitted-access decision.** Recheck up-to-date rules before collection. Consider written GitHub permission or a separately reviewed lawful data source, explicitly acknowledging its coverage limits. GitHub REST repository metadata cannot retrospectively reconstruct Trending ranks. If permission remains blocked, report that Study A's primary Trending data source is unavailable and amend the protocol prospectively; do not invent historic rankings or equate GitHub stars with Trending.

The QA tool itself is **offline** and accepts only locally supplied, lawfully retained HTML+manifest+independent annotation records. Do not commit raw third-party HTML or contributor identities without data-rights/privacy review.

## Reuse-first implementation decision

The tool reuses `trending_study.pilot.validate_capture`, the existing parser/selector inspector and `safe_io.publish_json`, plus Python's standard-library JSON/hash/counter utilities. It does not create a second crawler, dependency, ML classifier, new repository-ranking algorithm or environmental claim.

## Run the synthetic example

The committed example uses **only** the fictional two-entry `tests/fixtures/trending.html` and artificial A/B reviewer files whose SHA references match the fixture manifest. Perfect performance here is **synthetic test success, not human-audited GitHub recall**.

~~~bash
python -m trending_study.page_qa audit \
  --raw tests/fixtures/trending.html \
  --manifest examples/page_qa_manifest.synthetic.json \
  --review-a examples/page_qa_review_A.synthetic.json \
  --review-b examples/page_qa_review_B.synthetic.json \
  --output /tmp/page-qa-synthetic-report.json

python -m trending_study.page_qa aggregate \
  --inputs /tmp/page-qa-synthetic-report.json \
  --output /tmp/page-qa-synthetic-summary.json

python -m unittest discover -s tests -v
~~~

All outputs are write-once; use a **new pathname** on retry, not overwrite. A fake fixture must return `qa_status=synthetic_only`, `documentary_minimum=synthetic_not_applicable` and `cohort_enrollment_status=not_enrolled`. The tool makes no HTTP requests, GitHub modifications, third-party package installs or local untrusted code execution.

## Independent real-page audit procedure — NOT YET PERFORMED

1. **Source authorization:** human data steward documents source-use rules, exact permitted URLs, frequency, retention, distribution rights and the decision. No bypass, proxy rotation or bulk collection.
2. **Original evidence:** for each authorized capture, retain immutable raw HTML bytes, source URL/window, actual UTC capture time, HTTP metadata and matching SHA manifest in an access-controlled location. Also record exact parser source commit and capture location. Filenames/ISO times are **not** server attestation.
3. **Two independent annotators:** reviewers A and B separately render the saved original page and transcribe **every displayed repository and its visual rank**, not just supported CSS selectors or a favorable subset. Include off-selector rows, page-length discrepancies and ambiguity. They must not inspect the parser output before their own annotations are frozen. Keep A and B separate with actual human signoff and pseudonyms rather than personal emails.
4. **Binding and schemas:** each reviewer uses `page-qa-review-1.0` with `dataset_kind=pilot`, `coverage=all_displayed_rows`, `inspection_mode=independent_rendered_saved_capture`, exact raw+manifest SHA-256 digests, distinct reviewer references, UTC reviewed timestamps and all consecutive rank rows. Any unreadable identity has `repository=null` **and a nonempty note**; do not silently omit the row.
5. **Blind comparison:** run `page_qa audit` for one capture. A/B disagreement about identity, ambiguous entry or visible page length blocks numerical claims. A third independent reviewer C may adjudicate disagreement with a later timestamp and explicit reason, but cannot alter an already jointly resolved rank. Original A/B files must remain untouched.
6. **QA calculation:** score both identity-only and rank-sensitive matching. With full agreed/adjudicated references, `TP` is a correct (rank, owner/repo) pair, `FP` an unmatched parser-emitted pair and `FN` a manually visible pair missed or wrongly ranked. Compute `precision=TP/(TP+FP)` and `recall=TP/(TP+FN)` for observed page denominators; ranks exchanged count both FP and FN. Unknown reference => **null metric**. Structural parser rejection => **failed capture/QA**, not an empty Trending day.
7. **Multi-page evidence:** use `page_qa aggregate` on distinct, write-once QA reports. The minimum documentary target is **at least 30 fully resolved actual displayed rows across daily, weekly and monthly capture windows**, with known number of pages, skipped rows, failures and source dates. This is a **pilot QA floor**, not a probability sample or sufficient inferential power. A single 30-row page from one window does not satisfy all three surfaces. Language-filtered panels need separate parser and permission validation.
8. **Independent scientific decision:** a qualified human methods reviewer must examine permits, saved raw/rendered pages, annotation independence, conflicts/adjudication, metrics, regression tests and statistical uncertainty. Keep a dated immutable signoff and explicit approval/refusal. **The tool never changes cohort enrollment from `not_enrolled`.** Freeze allowed sampling and external preregistration before confirmatory inference.

## Reviewer file contract

See the complete committed `examples/page_qa_review_A.synthetic.json` and `examples/page_qa_review_B.synthetic.json` for exact field names.

| Field | Meaning |
|---|---|
| `schema_version` / `dataset_kind` | `page-qa-review-1.0`; `synthetic` or self-declared `pilot` |
| `reviewer_slot` / `reviewer_ref` / `reviewed_at_utc` | A, B or adjudicator C; pseudonymous reference, UTC not before capture |
| `source_sha256` / `manifest_sha256` | SHA-256 hashes of **raw and manifest file bytes**, binding all judgments to one capture |
| `coverage` / `inspection_mode` | `all_displayed_rows`; source mode distinct for synthetic vs real saved rendered page |
| `rows` | Exact full-page list `{"rank":1,"repository":"owner/name","note":null}`; unknown identity must have reason |
| `decision_note` | Null for A/B; nonempty explanatory rationale for C |

The first schema supports up to 100 displayed rows per page. If a real page exceeds this bound, **change and review the schema**; never trim the page to make it pass.

## Interpretation of reports

- A `page-qa-report-1.0` gives source hashes, reviewer identity references, disagreement count/positions, parsed row count, full-page exact match, and finite-page rank-sensitive/identity-only TP/FP/FN and rates **only for resolved pages**.
- A `page-qa-summary-1.0` pools resolved-page counts and documents daily/weekly/monthly coverage. If a self-declared pilot has >=30 rows across all three windows, it can show `documentary_minimum=met_on_self_reported_inputs`. This is **not** authenticated human review or a signed QA result.
- All reports carry `cohort_enrollment_status=not_enrolled` and require separate external signoff. Do not use the rates as confidence intervals or extrapolate to all GitHub Trending. Rows within a page are clustered, so naive independent-binomial error bars are inappropriate; define confidence/sensitivity methods after real pilot sampling.
- A captured HTML page can be structurally consistent and *still miss off-selector rows*. The synthetic drift test demonstrates that logical scenario, **not current live GitHub behavior**.

## Outstanding gates

| Gate | Status as of 2026-10-12 |
|---|---|
| Offline two-reviewer comparison, optional third-reviewer adjudication, strict checks and synthetic QA tests | Implemented on feature branch |
| Actual GitHub Trending capture under independently reviewed access conditions | **Not performed** |
| >=30 actual manually audited rows across all three page windows | **Pending** |
| External reviewer independence, source rights, data retention, research signoff | **Pending** |
| Real-page recall, language-filter QA, longitudinal cohort, 2027 external preregistration | **Not established** |

See [ethics](ETHICS.md), [pilot source manifest](PILOT_CAPTURE_AND_PREFLIGHT.md), [structural parser QA](PARSER_STRUCTURE_QA_2026_10_12.md), [selection protocol](SELECTION_PROTOCOL_2027.md) and [data dictionary](DATA_DICTIONARY.md).

**Practical lesson for the maintainer's other repositories:** green CI and internally consistent data never substitute for independent whole-user-task verification. Preserve immutable evidence, score missing cases, and reject unsupported success/green claims.
