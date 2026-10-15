# Qdrant — provisional six-month technology intelligence screen (077)

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** This report, its [event ledger](077-qdrant.events.csv) and [search log](077-qdrant.search-log.md) are an AI-assisted first-pass documentary source screen. No qualified human has reviewed them. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open. Nothing here is a verified task outcome, an adoption measure or an endorsement.

- **Company watchlist ID:** 077
- **Research issue:** [#145](https://github.com/MSKazemi/github-trending-1000-study/issues/145); evidence corpus link [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56) (no `NEWS-YYYY-NNNN` item minted here; candidates listed in §9).
- **Ownership and product boundaries (as of 2026-10-12):** Qdrant Solutions GmbH, Berlin (Amtsgericht Berlin Charlottenburg, HRB 235335 B, per the [impressum](https://qdrant.tech/legal/impressum/)); privately held and venture-funded. No parent company, acquisition or rename was found. Its most recent round, a $50M Series B led by AVP, was announced on [2026-03-12](https://qdrant.tech/blog/series-b-announcement/), before the window, so it is baseline only. Filing-level corporate verification was **not** performed.
- **Product URL and public channels:** [qdrant.tech](https://qdrant.tech/), [blog](https://qdrant.tech/blog/) ([RSS](https://qdrant.tech/blog/index.xml)), [qdrant/qdrant releases](https://github.com/qdrant/qdrant/releases) (Apache-2.0), [security advisories](https://github.com/qdrant/qdrant/security/advisories), [Private Cloud changelog](https://qdrant.tech/documentation/private-cloud/changelog/), [public roadmap](https://github.com/qdrant/qdrant/blob/dev/docs/roadmap/README.md) (the 2025 edition, last changed 2025-07-28), and the PyPI packages `qdrant-client`, `qdrant-edge-py` and `fastembed`. A managed-cloud changelog URL returned HTTP 404.
- **Analysis window:** 2026-04-12 to 2026-10-12 inclusive; accessed 2026-10-16.
- **Researcher / factual reviewer / review date:** AI-assisted screen / **pending** / **pending**.
- **Status:** screened (provisional). The ledger has 28 rows covering all seven calendar segments (Apr 1, May 5, Jun 4, Jul 4, Aug 4, Sep 5, Oct 5).
- **Source coverage:**
  - Official sources: the blog RSS (30 in-window entries, 24 opened as raw HTML), all 7 in-window engine releases, both repository security advisories, PyPI upload times, Hugging Face licence tags, the Private Cloud changelog, and the website-source commit for the serverless page.
  - Independent and contrary coverage: two Elastic Search Labs posts (a competitor, so not neutral), a Vultr partner post, the HN Algolia API, the NVD API and two web searches.
  - The search-engine budget was nearly exhausted. No neutral trade-press article on an in-window Qdrant product event was found or read.

## 1. Search and inclusion audit

This is a summary. The exact requests, the opened URLs and the exclusions are in the [search log](077-qdrant.search-log.md).

| Search run UTC | Site/engine | Full query and dates | Found | Screened | Included | Excluded/why | Coverage limitation |
|---|---|---|---:|---:|---:|---:|---|
| 2026-10-16 | qdrant.tech RSS + raw HTML | all blog items 2026-04-12..10-12 | 30 in-window | 24 opened | 13 rows | case studies, explainers, hackathon/event posts | the feed lacks some posts; sitemap `lastmod` is edit time |
| 2026-10-16 | GitHub `gh api` | qdrant/qdrant releases + advisories; qdrant-client and fastembed releases; org repos | 7 engine releases, 1 in-window advisory | all | 10 rows | v1.18.3 (single bug fix) | release notes are vendor-authored |
| 2026-10-16 | PyPI / Hugging Face / NVD | upload times, licence tags, `keywordSearch=qdrant` | 4 packages; 10 CVEs | all | 1 row (+ checks) | 3 in-window CVEs belong to third-party products | NVD keyword match only |
| 2026-10-16 | Private Cloud changelog | versions 1.9.7–1.10.0 | 10 versions | 10 | 3 rows | routine version bumps | page undated as a whole |
| 2026-10-16 | HN Algolia + 2 web searches + Elastic/Vultr pages | `qdrant` stories in window; FineWeb and news queries | 13 HN stories; unknown web | ~28 | 3 rows | Show HN projects, aggregators (E0) | Business Wire copy HTTP 403 |

## 2. Verified company/product identity and baseline

Qdrant is a vector search engine written in Rust. The engine is open source under Apache-2.0 at [qdrant/qdrant](https://github.com/qdrant/qdrant) (licence per the GitHub API). It ships with Apache-2.0 clients (`qdrant-client`) and the `fastembed` embedding library. Around the engine, Qdrant sells proprietary operated offerings:

- Qdrant Cloud (managed)
- Hybrid Cloud and Private Cloud (operator-based, on the customer's Kubernetes)
- Cloud Inference

The website also lists **Qdrant Edge (Beta)**, an embedded in-process library (`qdrant-edge-py`, Apache-2.0 per PyPI), and **Qdrant Serverless (Coming soon)**. In-window community and demo code largely sits in the `qdrant-labs` organisation. Many of those repositories show no detected licence.

**Pre-window baseline (context only, not counted):**

- **Series B (2026-03-12):** $50M led by AVP. The announcement states "250 million downloads across all our packages and 29,000 GitHub stars"; both figures are vendor-stated and are not adoption evidence.
- **Agent skills (2026-03-31):** the agent-skills launch post, with `qdrant/skills` v0.1.0 tagged 2026-03-30 (Apache-2.0).
- **Security:** CVE-2026-25628 / GHSA-f632-vm87-2m2f, an arbitrary file write via `/logger`, published 2026-02-05.
- **Public roadmap:** the 2025 roadmap remains the current public roadmap. It was not updated in the window.

**Post-window, excluded:** blog posts dated 2026-10-13 (`pplx-embed-v2`) and 2026-10-14 (`reachy-robot-memory-qdrant-edge`), and `qdrant-labs/qdrant-ray` (created 2026-10-15).

## 3. Month-by-month discoveries (six calendar months + partial endpoints)

| Month | Announcements/changes | Primary URLs | Independent reporting | Notes or no-result limitations |
|---|---|---|---|---|
| 2026-04-12..30 | Cloud GPU indexing, Multi-AZ and audit logging (Apr 28) | [blog](https://qdrant.tech/blog/qdrant-cloud-enterprise-launch/) | none found | Vector Space Day SF announcement (Apr 21) folded into June recap; Series B is pre-window |
| 2026-05 | v1.18.0 with TurboQuant, named-vector add/delete, RocksDB removal and internal gRPC auth option (May 11); v1.18.1 snapshot-upload authorization fix (May 22); Edge Python 0.7.0 (May 27); Private Cloud 1.9.7 (May 28) | [release](https://github.com/qdrant/qdrant/releases/tag/v1.18.0), [blog](https://qdrant.tech/blog/qdrant-1.18.x/), [PyPI](https://pypi.org/pypi/qdrant-edge-py/json) | none found | Three customer case studies excluded |
| 2026-06 | v1.18.2 auth-bypass and heap-read fixes (Jun 4); Edge blog (Jun 16); Elastic "7x faster" benchmark (Jun 24); Vector Space Day recap (Jun 24, event Jun 11) | [release](https://github.com/qdrant/qdrant/releases/tag/v1.18.2), [blog](https://qdrant.tech/blog/qdrant-edge-on-device-vector-search/), [recap](https://qdrant.tech/blog/vector-space-day-2026-recap/) | [Elastic, Jun 24](https://www.elastic.co/search-labs/blog/vector-search-benchmark-elasticsearch-vs-qdrant) (competitor) | Hackathon winners post excluded |
| 2026-07 | Branch-aware code search pattern (Jul 2); Qdrant benchmark rebuttal (Jul 8); Elastic reproduction (Jul 13); Private Cloud 1.9.12 operator least-privilege RBAC (Jul 17) | [blog](https://qdrant.tech/blog/branch-aware-code-search/), [blog](https://qdrant.tech/blog/benchmark-elastic-diskbbq/) | [Elastic, Jul 13](https://www.elastic.co/search-labs/blog/vector-search-benchmark-elasticsearch-qdrant) | One dispute, three documents (duplicate group `077-007`); v1.18.3 not ledgered |
| 2026-08 | qdrant-client 1.19.0 breaking removals (Aug 4); v1.19.0 with Turbo4 datatype, memory tiers and per-tenant IDF (Aug 5); serverless landing page added (Aug 7); Minima partner case study (Aug 13) | [release](https://github.com/qdrant/qdrant/releases/tag/v1.19.0), [client](https://github.com/qdrant/qdrant-client/releases/tag/v1.19.0), [commit](https://github.com/qdrant/landing_page/commit/f57defc9fe6e70a04c395ec91a777a7c8e56dbe1) | none found | Edge 0.8.0 on PyPI (Aug 5) not separately ledgered; explainers excluded |
| 2026-09 | FineWeb-10B datasets and Supernova (Sep 1); v1.19.1 (Sep 4); Rust cross-encoder experiment (Sep 25); Constella research preview (Sep 29) | [blog](https://qdrant.tech/blog/qdrant-fineweb-10b-release/), [release](https://github.com/qdrant/qdrant/releases/tag/v1.19.1), [blog](https://qdrant.tech/blog/constella-research-preview/) | [Vultr, Sep 1](https://blogs.vultr.com/qdrant-fineweb-10b-vector-search-benchmark-vultr) (infrastructure partner, not independent) | SHIFT multilingual-RAG post and case studies excluded |
| 2026-10-01..12 | v1.19.2 and **GHSA-3gph-6c29-p29v** (high; internal gRPC accepted read-only credentials) (Oct 5); Private Cloud 1.10.0 (Oct 6); EmbeddingGemma 2 tests (Oct 6); fastembed 0.9.0 (Oct 7) | [advisory](https://github.com/qdrant/qdrant/security/advisories/GHSA-3gph-6c29-p29v), [release](https://github.com/qdrant/qdrant/releases/tag/v1.19.2), [fastembed](https://github.com/qdrant/fastembed/releases/tag/v0.9.0) | none found | Jevjitsu experiment post (Oct 8) excluded |

## 4. Dated event evidence and capabilities

Full row detail is in the [CSV](077-qdrant.events.csv) (28 rows, IDs `CI2026-077-001`…`028`). Highlights:

| Event ID | Published UTC / underlying event date | Claim or observed feature | Availability and limitations | Source link (type) | Independent check | E0–E4 working grade |
|---|---|---|---|---|---|---|
| CI2026-077-002/003 | 2026-05-11 | v1.18.0: TurboQuant, named-vector add/delete, RocksDB fully removed, internal gRPC auth option, link to agent skills | Recall tables are vendor-run | [release](https://github.com/qdrant/qdrant/releases/tag/v1.18.0) | release blog + PyPI | E2 / E1 |
| CI2026-077-007 | 2026-06-04 | REST auth whitelist bypass and malicious-snapshot heap read fixed | No advisory or CVE published | [release](https://github.com/qdrant/qdrant/releases/tag/v1.18.2) | none | E2 (documentary) |
| CI2026-077-009/012/013 | 2026-06-24 / 07-08 / 07-13 | Benchmark dispute: Elastic claimed 7x; Qdrant claimed 2.1x the other way; Elastic's reproduction found the engines on par | Every party is a vendor; Elastic's reproduction found io_uring silently disabled under Docker's default seccomp | [Elastic](https://www.elastic.co/search-labs/blog/vector-search-benchmark-elasticsearch-vs-qdrant), [Qdrant](https://qdrant.tech/blog/benchmark-elastic-diskbbq/), [Elastic](https://www.elastic.co/search-labs/blog/vector-search-benchmark-elasticsearch-qdrant) | cross-vendor | E1 / E1 / E2 |
| CI2026-077-011 | 2026-07-02 | Branch-aware semantic code search for coding agents (payload filter over branch ancestry) | Pattern and tutorial only; no evaluation | [blog](https://qdrant.tech/blog/branch-aware-code-search/) | none | E1 |
| CI2026-077-015 | 2026-08-04 | qdrant-client 1.19.0 removes `add`/`query` and deprecates `search`/`recommend` in favour of `query_points` | Breaking for downstream code | [release](https://github.com/qdrant/qdrant-client/releases/tag/v1.19.0) | PyPI upload | E2 |
| CI2026-077-016 | 2026-08-05 | v1.19.0: Turbo4 storage, memory tiers, per-tenant IDF for BM25, prefix and slice filters, global quotas, S3 snapshot path-traversal fix | Turbo4 gives up rescoring against originals | [release](https://github.com/qdrant/qdrant/releases/tag/v1.19.0) | release blog | E2 |
| CI2026-077-019/020 | 2026-09-01 | FineWeb-10B (ODC-BY), PubMed-MV, Coyo-VE datasets; Supernova (Apache-2.0) | Query count stated as both 100,000 and 120,000 | [blog](https://qdrant.tech/blog/qdrant-fineweb-10b-release/) | HF API licence tag; Vultr (partner) | E2 |
| CI2026-077-024/025 | 2026-10-05 | GHSA-3gph-6c29-p29v (high, CVSS 3.1 score 8.3): with `enforce_internal_auth`, read-only keys or JWTs could add peers and write internally; affects ≥1.18.0 <1.19.2 | Default config and Managed Cloud stated not materially affected; no CVE ID seen | [advisory](https://github.com/qdrant/qdrant/security/advisories/GHSA-3gph-6c29-p29v) | v1.19.2 release notes | E2 |
| CI2026-077-028 | 2026-10-07 | fastembed 0.9.0: Constella encoders; HF-only model downloads; upstream HF config change alters embeddings of texts >128 tokens for **any** fastembed version on a fresh download | Reproducibility hazard; effect size unmeasured | [release](https://github.com/qdrant/fastembed/releases/tag/v0.9.0) | PyPI upload | E2 |

**Feature inventory (vendor-documented, not exercised by us):**

| Area | In-window change | Class |
|---|---|---|
| Hybrid / lexical retrieval | Per-tenant IDF statistics for sparse/BM25 (1.19); option to disable the BM25 stemmer; keyword prefix match; slice filter; MMR and full-text fixes (1.19.1–1.19.2) | shipped (OSS) |
| Compression / storage | TurboQuant quantization (1.18) → Turbo4 primary datatype (1.19); memory tiers cold/cached/pinned replacing `on_disk`/`always_ram` (old flags deprecated); RocksDB removed (1.18) | shipped (OSS) |
| Schema evolution | Add and remove named vectors without recreating the collection (1.18), which makes embedding-model migration possible without a full reindex | shipped (OSS) |
| Observability / governance | Audit-log query API, tracing IDs, per-collection metrics (1.18); global quota API (1.19); Cloud audit logging on paid clusters; Private Cloud audit config and quota enforcement | shipped (OSS + proprietary) |
| Security | Internal gRPC auth (1.18), later found to accept read-only credentials and fixed in 1.19.2 (advisory); snapshot-upload authorization (1.18.1); REST auth-bypass and heap-read fixes (1.18.2); S3 snapshot path traversal (1.19.0); `.`/`..` collection names (1.19.1); a startup warning when no API keys are set (1.19.2); least-privilege operator RBAC (Private Cloud 1.9.12) | shipped; only one fix has an advisory |
| Agent / coding-agent tooling | Agent-skills link in the startup message (1.18); `qdrant/skills` repo active (≥100 commits) with no new release; branch-aware code-search pattern; **`mcp-server-qdrant` had no release in the window** | mixed |
| Edge / embedded | Qdrant Edge beta: `qdrant-edge-py` 0.7.0–0.8.0 on PyPI | preview |
| Open data / benchmarks | FineWeb-10B, PubMed-MV, Coyo-VE datasets; Supernova framework; benchmark reproduction kit (no licence detected) | shipped (data/tool) |
| Embeddings | fastembed 0.8.1 and 0.9.0; Constella query encoders (MIT on HF; research preview) | shipped / preview |
| Licensing | Engine, clients, fastembed, skills and Supernova are Apache-2.0. Constella-nano is MIT and FineWeb-10B is ODC-BY. `landing_page`, `edge-mission-control`, `wiki-dpr-disk-rescore-benchmark`, `many-jev-recipies` and `AstraBert/cross-encode-rs` show **no detected licence** via the GitHub API (2026-10-16) | observed |
| Breaking changes | qdrant-client 1.19.0 removals; deprecated search endpoints removed from OpenAPI (1.19.0); `max_resident_memory_percent` deprecated one minor version after it was introduced (1.18 → 1.19) | observed in release notes |

## 5. What the company says it intends to do

| Verbatim or close paraphrase of public direction (<=25 words per source quoted) | Link/date | Promised horizon | Status (planned, tentative, uncommitted) | Missing/contradictory context |
|---|---|---|---|---|
| "We're bringing serverless to Qdrant Cloud." Access will roll out "in stages, starting with a limited group from the waitlist." | [serverless page](https://qdrant.tech/serverless/), added in [commit of 2026-08-07](https://github.com/qdrant/landing_page/commit/f57defc9fe6e70a04c395ec91a777a7c8e56dbe1) | none stated | planned (waitlist) | The 2025 roadmap said Qdrant did not plan "a separate serverless product". Whether this conflicts with the new page is unresolved |
| The operator sets a flat 90% quota "For Qdrant 1.20.0 and newer" | [Private Cloud 1.10.0, 2026-10-06](https://qdrant.tech/documentation/private-cloud/changelog/) | next minor version | implied planned release; no 1.20.0 on GitHub by 2026-10-16 | no date |
| "We plan to continue to release more datasets for the community." | [FineWeb-10B post, 2026-09-01](https://qdrant.tech/blog/qdrant-fineweb-10b-release/) | none | uncommitted | — |
| Constella shared "as a research preview" | [2026-09-29](https://qdrant.tech/blog/constella-research-preview/) | none | tentative | No GA criteria stated |
| Qdrant Edge is "free to use and currently in beta" | [2026-06-16](https://qdrant.tech/blog/qdrant-edge-on-device-vector-search/) | none | beta; GA uncommitted | No licence or pricing commitment for a future GA |
| Public roadmap: keep backward compatibility "for at least one minor version back" | [2025 roadmap](https://github.com/qdrant/qdrant/blob/dev/docs/roadmap/README.md) (pre-window, last edit 2025-07-28) | 2025 | stale | No 2026 roadmap was published in the window |

These are **company statements**, not forecasts we endorse.

## 6. Independent interpretation: direction and alternative scenarios (researcher's conditional 2027–2031 view)

| Hypothesis for 2027–2031 | Supporting observations | Rival explanations | Disconfirming signals | Confidence/unknowns |
|---|---|---|---|---|
| H1: Hybrid (dense + lexical) retrieval with tenant-aware scoring becomes the default configuration for retrieval in agent loops | Per-tenant IDF (1.19); RRF/BM25 used in the Edge demo and the Minima case study; first-pass sufficiency 72%→87% (partner-reported) | Dense-only plus better embeddings may suffice; vendor and partner selection of favourable tasks | Independent accepted-task comparisons show no gain for hybrid over dense-only at matched budget | low; no neutral evaluation |
| H2: Vendor benchmark wars will move toward open, reproducible kits and shared datasets, but the headline multipliers will keep failing reproduction | Elastic 7x → Qdrant 2.1x → Elastic "on par"; repro kit published; FineWeb-10B + Supernova released | Open kits may still embed configuration choices that favour one engine (segment count, warm cache) | Neutral third parties reproduce vendor multipliers within noise | moderate that disputes continue; unknown for neutrality |
| H3: Compression-first storage (4-bit/1-bit) shifts cost from RAM to accuracy risk and needs per-dataset validation | TurboQuant → Turbo4 within 3 months; vendor states results vary by dataset; ~74% top-10 overlap without rescoring (EmbeddingGemma 2 test) | Losses may be negligible for most RAG tasks | Accepted-task rates are unchanged across compression levels on independent task sets | moderate for "tradeoff exists" |
| H4: Embedding pipelines are less reproducible than code pins suggest, because model artefacts change under a fixed library version | fastembed 0.9.0 note: a config change on HF changes embeddings for any version on a fresh download | One-off cleanup; most users re-embed rarely | Hash-pinned model downloads become the default, and no further silent changes are recorded | moderate; single documented instance |
| H5: Security fixes in fast-moving OSS infrastructure are often disclosed only as release-note lines | Five security-relevant fixes across 1.18.1–1.19.1 (four in "Security" sections, one S3 path traversal under bug fixes) had no advisory; one advisory (no CVE seen) for 1.19.2 | Low severity may not merit advisories | Advisory or CVE coverage for future security fixes approaches 100% | low–moderate |

These are hypotheses for testing, not company strategy or fact.

## 7. Implications for the GitHub 1000 study

| M1–M7 construct | Possible observable effect | Study design to test it | Negative/null explanation | Measurement boundary |
|---|---|---|---|---|
| M1 AI coding-agent change | Retrieval vendors package "agent skills" and code-search patterns for coding agents | Compare agent context retrieval (grep vs branch-scoped semantic index) on frozen tasks | Agents do as well with grep on small repos | Consented runs only; no vendor usage counts |
| M2 accepted task quality | Hybrid retrieval and compression change answer grounding | Hidden acceptance tests over a fixed retrieval corpus; all attempts counted | No difference at matched budget | Partner metrics (Minima) are not study outcomes |
| M3 discoverability | Benchmark disputes, events and datasets generate attention | Separate attention signals from verified reuse | Attention is not reuse | Stars/downloads (vendor: 29,000 stars, 250M downloads, pre-window) never used as outcomes |
| M4 verified third-party reuse | Many Show HN projects and connectors build on Qdrant (HN leads) | Trace consented downstream repos at pinned commits that run tests | Mention or import without execution | Executed tests only |
| M5 rights/security/provenance | Mixed licensing (Apache/MIT/ODC-BY versus unlicensed demo repos); security fixes without advisories; a high-severity advisory in an opt-in hardening feature | Licence and advisory check before reuse; diff release notes for "Security" sections | Advisory-less fixes may be minor | Licence files at pinned commits; advisory DB plus release notes |
| M6 review/maintenance and lifecycle cost | Breaking client removals, deprecations within one minor version, silent embedding changes | Measure migration minutes and embedding-drift checks per upgrade | Agents absorb migration cheaply | No kWh/CO2e inferred from GPU-hours, RAM or compression ratios |
| M7 actionable interventions | Pin embedding-model artefacts by hash; add a drift test; prefer `query_points`-style stable APIs | See §8 | Guardrail adds friction without catching drift | Synthetic tasks only until approval |

Vendor adoption claims (customer names, attendance, downloads, stars) are **not** independent task outcomes or verified reuse.

## 8. One practical, falsifiable change for the maintainer's own repositories

**Repository/component:** the [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study) offline research artifacts: the `research/company-intelligence/` Markdown and CSV files, run as a **synthetic, network-free** retrieval task. The disabled Trending `capture` command stays disabled. A retrieval tool does not make unapproved scraping permissible.

**Candidate practice (not yet validated):** add hybrid retrieval (BM25 plus dense) over the repository's own research ledgers to help a reviewer find conflicting or duplicate evidence rows across companies.

- **Reuse first:** compare the baseline (existing `grep`/`ripgrep` plus the CSV validators already in the repo) against a local reused stack: Qdrant in local mode via the pinned Apache-2.0 `qdrant-client` and `fastembed` packages, with BM25 and a small dense model. No hosted service, no new service code and no paid API.
- **Pin and hash:** record exact package versions and the model-file hashes, because of the fastembed 0.9.0 note (CI2026-077-028).

**Treatment/control and frozen comparable task:**

- **Task set:** a person other than the operator freezes 20 reviewer questions. An example: "which ledger rows report the same incident under different dates?" The same person writes hidden answer keys from manual reading, kept out of tool and agent context.
- **Arm A:** `grep`/`rg` plus spreadsheet filtering.
- **Arm B:** hybrid search, then the same manual confirmation step.
- **Controls:** the same reviewer, a time cap per question, and randomized question order.
- **Accepted-task unit:** one question answered with every key row found and no false row accepted after the reviewer's confirmation.

**Success and guardrails:**

- **Primary outcome:** accepted answers divided by all 20 questions. Abandoned and timed-out questions are included.
- **Guardrails:**
  - no network access during runs (the model is downloaded once beforehand and its hash recorded);
  - no new runtime dependency is added to the repository's package manifest (the experiment lives in a scratch environment);
  - embedding outputs are recomputed twice, and identical vectors are required;
  - the full unit suite stays green;
  - no personal data is indexed.
- **Measured human work:** setup minutes, per-question minutes, and minutes spent on false leads.
- **Energy:** none is estimated unless metered.
- **Authorship:** commit authorship stays with the maintainer, and no AI contributor attribution is recorded in commits.

**Stop/reversal rule:** keep Arm A and remove Arm B in any of these cases:

- Arm B does not raise accepted answers by at least 3 of 20 questions.
- Arm B adds more than 5 minutes of setup or review per question on average.
- The embedding re-run is not bit-identical.
- Any package or model licence cannot be confirmed.

**No trial executed; no effect estimated.**

## 9. Findings, uncertainties and review outcome

- **Observed/shipped (documentary, vendor-sourced):** seven engine releases 1.18.0–1.19.2 (GitHub publish times confirmed); qdrant-client 1.18.0/1.19.0/1.19.1 and fastembed 0.8.1/0.9.0 (PyPI times confirmed); Edge Python 0.7.0–0.8.0 (PyPI); three Private Cloud operator releases with the security hardening above; one high-severity advisory with a fix; open datasets with HF licence tags; Apache-2.0 Supernova.
- **Claims/announcements only:**
  - Performance and scale figures: Cloud GPU 4x index builds; TurboQuant and Turbo4 recall and storage figures; Edge 0.1 ms vs 52 ms; Minima 2.92x; EmbeddingGemma 2 30x/77x.
  - Competing benchmarks: Qdrant's 2.1x and Elastic's 7x.
  - Other: attendance (350+), the Serverless waitlist, and Qdrant 1.20 quota behaviour.
- **Conjectures and unknowns:** H1–H5 in §6; actual task outcomes; the severity of advisory-less security fixes; whether any CVE was assigned to GHSA-3gph-6c29-p29v; any managed-cloud incidents (no status history was read).
- **Important contradictory or null evidence:**
  - (a) **Benchmark dispute.** Elastic's own reproduction (2026-07-13) reports the engines on par. It found the disk idle (0 IOPS) and io_uring silently disabled by Docker's default seccomp profile. That undercuts the mechanisms both vendors had named.
  - (b) **FineWeb-10B figures.** The Qdrant post states both 100,000 and 120,000 queries, and both ~25 TiB and 24.47 TB.
  - (c) **Serverless.** The 2025 roadmap's "no separate serverless product" sits against the 2026 "Qdrant Serverless (Coming soon)" page (unresolved).
  - (d) **Advisory-less fixes.** Five security-relevant fixes before 1.19.2 have no published advisory.
  - (e) **Unmaintained surfaces.** `mcp-server-qdrant` had no release in the window, and the public roadmap was not updated.
  - (f) **Rewrite near-null.** The vendor's own Rust cross-encoder rewrite gave only ~1.1x at the median, a near-null result for "rewrite vs reuse".
- **#56 candidates (not minted):**
  - Elastic Search Labs, 2026-06-24 and 2026-07-13 (competitor sources; label as such);
  - GitHub advisory GHSA-3gph-6c29-p29v, 2026-10-05;
  - Vultr, 2026-09-01 (partner).

  Each needs human reading before a `NEWS-YYYY-NNNN` ID is assigned. No neutral independent news article was found for this window.
- **Reviewer links and audit date:** none yet. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.
