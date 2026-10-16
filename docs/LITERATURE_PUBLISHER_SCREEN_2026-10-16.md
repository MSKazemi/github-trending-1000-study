# Bounded publisher-first literature screen — issue #7 (2026-10-16)

> **Status: candidate evidence, NOT a completed systematic literature review or human-blinded screen.** This is an AI-assisted screen of specifically selected public pages, not an ACM/IEEE/Scopus/OpenAlex/Google Scholar census. No database export, hit count, complete exclusions, blinded dual screening, full-text appraisal or independent methodological sign-off was collected. The `searched_at_utc` value `2026-10-16T00:00:00Z` in the companion JSON denotes **date-only normalization**, not a verified clock time. Do not use it for prospective priority claims. This log is a transparent bounded artifact, not PRISMA counts.

**Machine-readable record:** [11 screened source entries, five stated discovery searches](../references/literature_publisher_screen_2026-10-16.json), validated with existing `python -m trending_study.literature_ledger --input references/literature_publisher_screen_2026-10-16.json`. The validator can verify **schema and candidate identity**, not the truth or copyright permissions of included documents. Do not treat `decision: include` as human-reviewed study acceptance.

## Reproducible searched surfaces

| Run ID | Surface and exact query | Qualification |
|---|---|---|
| IEEE_WEB | IEEE Xplore public landing pages via web: `site:ieeexplore.ieee.org/document github repository popularity star growth mining software repositories` | Focused 2021/2023 selected abstracts; not IEEE-wide search |
| ACM_WEB | ACM DL public DOI page: `site:dl.acm.org/doi/10.1145/3715907 Beyond Dependencies Role of Copy Based Reuse in Open Source Software Development` | One preknown DOI, not ACM-wide search |
| ARXIV_WEB | arXiv public abstract/version page: `site:arxiv.org coding agent adoption GitHub 2026 129134 128018` | Version comparison and related later preprint, no export |
| METR_WEB | METR original authors' report pages: `site:metr.org measuring impact AI experienced open-source developer productivity randomized July 2025 February 2026 update` | Research institute report, **not peer-reviewed** as recorded here |
| SUPP_WEB | `site:doi.org/10.1145/2597073.2597074 Promises Perils Mining GitHub` | Historical validity reference |

**Screen:** 11 chosen publisher/author records: **8 provisional include**, **2 pending preprint versions**, **1 excluded** paper outside the task-first causal/reuse scope. These are *deliberately retrieved leads*, not complete search hits or independently unique research studies. IEEE/ACM records and DOI metadata were spot checked against public publisher/author metadata on 2026-10-16; not every full text was read. Scopus/OpenAlex bulk screening, Google Scholar exact exports, complete source discovery, rights/robots review and second reviewer decisions remain outstanding.

## Document-specific science and limitations

| Record | Design and key usable construct | Interpretation for our repo |
|---|---|---|
| [#01, IEEE MSR 2023](https://doi.org/10.1109/MSR59073.2023.00024) | 576 AI repositories from PapersWithCode and 24,953 issue records in publisher abstract | Documentation and first-run issues are useful *candidate constructs*, not independently accepted user outcomes; selection bias |
| [#02, IEEE MSR 2021](https://doi.org/10.1109/MSR52588.2021.00054) | Observational adoption of GitHub Actions; publisher reports activity changes | PR/commit activity is not proof of user-task quality or agent productivity |
| [#03, IEEE/ACIS BCD 2023](https://doi.org/10.1109/BCD57833.2023.10466327) | Ten repository growth-pattern case study, **excluded** from substantive evidence track | Normative star-growth reasoning and tiny frame do not measure independently verified reuse |
| [#04, ACM TOSEM 2025](https://doi.org/10.1145/3715907) | World of Code copy-based reuse and 374 developer survey responses | Small/medium OSS may originate substantial reused code; exact blob copy is not functional fit, legal reuse, or environmental savings |
| [#05, ACM MSR 2014](https://doi.org/10.1145/2597073.2597074) | GitHub mining representation and API/PR state pitfalls | Distinguish source-platform metadata from actual merged work; never assume all repositories are active or software |
| [#06/#07, arXiv 2026 v1/v2](https://arxiv.org/abs/2601.18341v2) | *Same* study revised from v1 to v2, with changed sample and estimated trace prevalence | Keep paper-version IDs and reported denominator together. Not two independent replicates |
| [#08, arXiv:2606.07448](https://arxiv.org/abs/2606.07448) | Authors' prospective/new-project frame reports higher agent-use trace signals | Preprint; selection and trace sensitivity prohibit all-GitHub incidence inference |
| [#09, METR 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) | 16 experienced OSS developers, 246 randomized tasks; authors report 19% longer completion with 2025 AI | Applies to selected mature OSS tasks and specific tool vintage, not general AI systems |
| [#10, METR Feb 2026](https://metr.org/blog/2026-02-24-uplift-update/) | Authors report refusal-to-participate and task selection, and overlapping-agent time measurement problems | Later apparent uplift is not a clean estimate; preregister missing/refused-task denominator |
| [#11, SPACE](https://doi.org/10.1145/3454122.3454124) | Conceptual developer-productivity dimensions | Framework, **not** observed benefit. Evaluate user quality, human workload and satisfaction separately |

**Version/de-duplication decision:** #06 and #07 share DOI `10.48550/arXiv.2601.18341` and are different revisions of one work; the existing [journal–preprint pilot](LITERATURE_VERSION_RECONCILIATION_2026-10-15.md) also links the later ACM peer-reviewed work. Do **not** pool sample sizes or count preprint and journal versions as independent replication. Later #08 has overlapping authors but new-project sample; independent data provenance and potential overlap require follow-up.

**What has *not* been shown:** No empirical project cohort, source-access approval to collect Trending pages, real search recall, 2027 trend estimate, task success improvement, green computing saving, costs, or accepted causal effect is established by these eleven candidate records.

## Closure gates still required for #7

1. Freeze PICOC questions and eligible time/language/type/quality criteria; choose exact translated queries per database **before retrieving outcomes**.
2. Conduct permission-reviewed full searches in ACM, IEEE, OpenAlex and any licensed Scopus/Google Scholar surfaces. Save true hits, rejected counts, exported metadata hashes, inaccessible screens and deduplicated records, including documented source rights.
3. Two genuinely separate human reviewers screen abstracts/full texts; adjudicate overlap, risk-of-bias, method quality, retractions and contradictory/null findings.
4. Extract precise task/participant/repository denominators, historical study version, uncertainty, primary outcome, validation code, confounders, author conflicts and funding; count one study once.
5. Only then update the canonical references and issue with a reproducible flow diagram, versioned CSV/JSON study table, reviewer approvals and limitations.

## Practical maintainer lessons to test (not demonstrated improvements)

- For each repository, independently test one external newcomer's *first runnable example*, not just README length or stars (motivated by #01).
- Require at least one non-agent reviewer to verify a submitted fix and report time-to-accept/rework; count every failed and abandoned task (#02/#09/#10).
- Index older/quiet OSS with explicit identity+license+version and frozen task tests before recommending reuse (#04); never equate copy events with successful integration.
- Record true GitHub API UTC states, immutable repository IDs, full errors/permission gaps and missing values; avoid historical inference from current API counts (#05).

## Public-host source URL guard (engineering follow-up, 2026-10-16)

The shared literature-ledger validator now rejects an *included* study's `source_url` when its literal host is loopback, link-local, non-global IPv4/IPv6 or a local/cloud-metadata name. A public HTTPS publisher URL remains structurally eligible, **not authenticated**. This avoids making internally-addressed metadata look like normal publisher evidence in a screening record; it also reduces the chance a human reviewer or future tool is directed to a local service.

One synthetic regression covers several private address classes and the unchanged legitimate DOI example. No network calls or DNS lookups occur; public-looking hostnames can later resolve to private addresses, so a future network-enabled source checker would need its own post-resolution SSRF protections. Search coverage, licensed access, independent bibliographic/factual screening, actual human coding and all systematic-review denominators remain unfinished.
