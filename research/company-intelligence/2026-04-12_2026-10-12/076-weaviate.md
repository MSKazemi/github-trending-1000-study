# Weaviate — provisional six-month technology intelligence screen (076)

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** This report, its [event ledger](076-weaviate.events.csv) and [search log](076-weaviate.search-log.md) are an AI-assisted first-pass documentary source screen. No qualified human has reviewed them. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open. Nothing here is a verified task outcome, an adoption measure, a legal opinion or an endorsement.

- **Company watchlist ID:** 076
- **Research issue:** [#144](https://github.com/MSKazemi/github-trending-1000-study/issues/144); evidence corpus link [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56) (no `NEWS-YYYY-NNNN` item minted here; candidates listed in §9).
- **Ownership and product boundaries (as of 2026-10-12):** Weaviate (the licence text in the repository names "Weaviate BV"), a privately held, venture-funded company that develops the Weaviate vector database. The vendor's about page still lists a 2023 Series B ($50M, 21 Apr 2023) as its latest press release. No in-window funding round, acquisition, rename or change of parent was found. Filing-level corporate verification was **not** performed.
- **Product URL and public channels:** [weaviate.io](https://weaviate.io/), [blog](https://weaviate.io/blog) ([RSS](https://weaviate.io/blog/rss.xml)), [docs](https://docs.weaviate.io/), [weaviate/weaviate](https://github.com/weaviate/weaviate) releases, [GitHub Advisory Database](https://github.com/advisories?query=weaviate), client repositories ([Python](https://github.com/weaviate/weaviate-python-client), [TypeScript](https://github.com/weaviate/typescript-client), [Go](https://github.com/weaviate/weaviate-go-client), [Java](https://github.com/weaviate/java-client), [C#](https://github.com/weaviate/csharp-client)), [PyPI `weaviate-client`](https://pypi.org/project/weaviate-client/), [npm `weaviate-client`](https://www.npmjs.com/package/weaviate-client). A `status.weaviate.io` host did not respond to our request (see search log).
- **Analysis window:** 2026-04-12 to 2026-10-12 inclusive; accessed 2026-10-16.
- **Researcher / factual reviewer / review date:** AI-assisted screen / **pending** / **pending**.
- **Status:** screened (provisional); 37 ledger rows across all seven calendar segments.
- **Source coverage:** 23 in-window blog posts (from the paginated blog index; the RSS feed holds only the latest 20 items) fetched as raw HTML; `weaviate/weaviate` GitHub releases (86 release objects from 2026-04-01 on, of which 74 stable releases and 8 release candidates fall in the window; 14 release bodies fetched, 8 of them read in full or via headings and keyword search); GitHub Advisory Database and NVD API; licence files and their commit history via `gh api`; client release objects, PyPI and npm registries; second-entity sources: DigitalOcean release notes, VulnCheck advisory, a third-party review page; Hacker News Algolia API. No reputable independent news story covering Weaviate in-window was found. See the [search log](076-weaviate.search-log.md).

## 1. Search and inclusion audit

Summary only. Exact queries, opened URLs and exclusions are in the [search log](076-weaviate.search-log.md). Search-engine result totals were not exposed and are recorded as **unknown**, not zero.

| Search run UTC | Site/engine | Full query and dates | Found | Screened | Included | Excluded/why | Coverage limitation |
|---|---|---|---:|---:|---:|---:|---|
| 2026-10-16 | weaviate.io blog index pages 1–3 + RSS | all posts 2026-04-12..10-12 | 23 in-window posts | 23 opened | 12 rows | 11 (demo series, how-to, explainers; see log) | blog shows a day date only (`datePublished` T00:00Z) |
| 2026-10-16 | `gh api` weaviate/weaviate releases | 2026-04-01..10-13 | 86 release objects since 2026-04-01; 74 stable + 8 RCs in window | 8 bodies read (4 in full, 4 via headings), all titles read | 12 rows | other patch releases (log) | titles only for most patches |
| 2026-10-16 | GitHub Advisory DB, NVD API, VulnCheck | `weaviate` | 3 in-window CVEs | 3 | 3 rows | pre-window CVEs | two of three advisories are unreviewed GHSAs |
| 2026-10-16 | `gh api` licence files and commits | `LICENSE`, `wl/` at tags | 4 licence commits in window | 4 | 3 rows | typo/wording commits | no legal review |
| 2026-10-16 | client releases, PyPI, npm | Python, TS, Go, Java, C#, weaviate-agents | ~30 versions | ~30 | 4 rows | Java/C# minor releases (log) | changelog depth varies |
| 2026-10-16 | HN Algolia API (stories + comments) | `weaviate`, window timestamps | 9 stories, 33 comments | all titles | 0 rows | vendor submissions and incidental mentions | HN is not a news source |
| 2026-10-16 | web search (2 queries) | licence; funding/news | unknown | ~18 | 3 rows (via fetched DigitalOcean page and a third-party review) | aggregators graded E0 | session search budget nearly exhausted |

## 2. Verified company/product identity and baseline

Weaviate is a vector database written in Go. It stores objects and vectors and supports hybrid (BM25 plus vector) search, filtering, multi-tenancy, RAG modules and model-provider integrations. The company also runs **Weaviate Cloud** (Shared, Dedicated, Marketplace) and hosted services that are not open source: the **Query Agent**, **Weaviate Embeddings** and, new in the window, **Engram** (managed agent memory).

**Licensing baseline and change.** Before 2026-08-26 the repository's `LICENSE` was a single BSD-3-Clause licence. On 2026-08-26 a commit split it: code outside `wl/` stays BSD-3-Clause (`LICENSE-BSD`), and code inside `wl/` falls under a separate Weaviate License. By 2026-09-30 that `wl/` text read "all rights reserved" and offered the code only under a separate enterprise licence, enabled by a licence key. The GitHub API reports the repository licence as `NOASSERTION` (2026-10-16). Client SDKs are BSD-3-Clause (PyPI and npm metadata, GitHub API). New in-window repositories carry mixed licences: `weaviate-cloud` is MIT, while `engram-plugins` shows no detected licence.

**Pre-window context (not counted):** v1.36 (Mar 3) introduced HFresh as a technical preview; agent-skills repo (created 2026-02-05); a `CLAUDE.md` agent-instruction file has existed in `weaviate/weaviate` since 2026-02-23. **Post-window, excluded:** PathSeer blog (2026-10-14), a nearObject cross-collection vector-disclosure security post (2026-10-15, fix already in v1.39.3), v1.40.1 (2026-10-13) and wcloud v0.1.2 (2026-10-13).

## 3. Month-by-month discoveries (six calendar months + partial endpoints)

| Month | Announcements/changes | Primary URLs | Independent reporting | Notes or no-result limitations |
|---|---|---|---|---|
| 2026-04-12..30 | Shared Cloud GA on AWS (Apr 15); v1.37.0 with built-in MCP server preview (Apr 16); Engram deep dive (Apr 21); Go client v6 alpha (Apr 22); Python client 4.21.0 (Apr 23); DigitalOcean Vector Databases with Weaviate private preview (Apr 28) | [blog](https://weaviate.io/blog/aws-shared-cloud-launch), [v1.37.0](https://github.com/weaviate/weaviate/releases/tag/v1.37.0), [blog](https://weaviate.io/blog/engram-deep-dive) | [DigitalOcean release notes](https://docs.digitalocean.com/release-notes/weaviate/) (second entity) | 1.37 release blog (Apr 23) folded into the v1.37.0 row |
| 2026-05 | text2vec-digitalocean module (May 21); MCP coding-assistant tutorial (May 21); standalone MCP server deprecated (May 25/26); Cloud console Editor/Viewer roles (May 28) | [v1.35.21](https://github.com/weaviate/weaviate/releases/tag/v1.35.21), [blog](https://weaviate.io/blog/coding-assistant-weaviate-mcp), [repo](https://github.com/weaviate/mcp-server-weaviate), [blog](https://weaviate.io/blog/rbac-overview) | DigitalOcean May 28 entry (control panel, private preview) | retrieval-quality (May 6) and tokenization (May 14) explainers excluded |
| 2026-06 | Engram GA (Jun 3); v1.38.0 (Jun 5); CVE-2026-11500 advisory (Jun 8); Verba archived (Jun 8); free tiers across Cloud (Jun 17); debug endpoints off by default (Jun 17); SSRF header fix (Jun 24); 1.38 blog claims MCP GA (Jun 25) | [blog](https://weaviate.io/blog/engram-generally-available), [v1.38.0](https://github.com/weaviate/weaviate/releases/tag/v1.38.0), [GHSA](https://github.com/advisories/GHSA-jqpm-wf57-qx5c), [Verba](https://github.com/weaviate/Verba), [blog](https://weaviate.io/blog/weaviate-free-tier) | GHSA/NVD (CNA VulDB) | data-import how-to (Jun 18) excluded |
| 2026-07 | DigitalOcean Managed Weaviate public preview (Jul 1); CVE-2026-59093 RBAC privilege escalation published (Jul 2); TS client 3.14.0 (Jul 17); read-repair data-integrity patch (Jul 27) | [DigitalOcean](https://docs.digitalocean.com/release-notes/weaviate/), [VulnCheck](https://www.vulncheck.com/advisories/weaviate-privilege-escalation-via-unchecked-permissions-in-rbac-role-assignment), [v1.38.7](https://github.com/weaviate/weaviate/releases/tag/v1.38.7) | VulnCheck, NVD | query-profiling explainer (Jul 21) and Foundry demo series (Jul 30) excluded |
| 2026-08 | v1.39.0: Namespaces, Search REST API, Hybrid MMR, RQ4 (Aug 4); Query Agent Search Mode `effort` (Aug 11); **open-core licence split committed** (Aug 26) | [v1.39.0](https://github.com/weaviate/weaviate/releases/tag/v1.39.0), [blog](https://weaviate.io/blog/search-mode-effort), [commit](https://github.com/weaviate/weaviate/commit/8677d32e173ca5154ce5346b61f3f366e498aeaf) | none in-window for the licence change itself | 1.39 release blog (Aug 27) folded into the v1.39.0 row; Foundry part 2 excluded |
| 2026-09 | v1.39.3 security fixes (Sep 7); HFresh default on free tier (Sep 9); wcloud agent-first CLI v0.1.1 (Sep 14); licence-key gate (Sep 15); RQ4 blog (Sep 17); third-party review notes split licence (Sep 19); enterprise licence text (Sep 30) | [v1.39.3](https://github.com/weaviate/weaviate/releases/tag/v1.39.3), [wcloud](https://github.com/weaviate/weaviate-cloud/releases/tag/v0.1.1), [commit](https://github.com/weaviate/weaviate/commit/6642209395b9c25cae80983ee9b8804b9b328452), [commit](https://github.com/weaviate/weaviate/commit/e0cc80ce004e319c41175d8362528c0c17baaee7) | [PromptQuorum review](https://www.promptquorum.com/power-local-llm/weaviate-review) (reputation unassessed) | charts/PDF how-to (Sep 1), Foundry part 3 (Sep 8), Engram guide (Sep 22) excluded |
| 2026-10-01..12 | Google-modules credential-disclosure advisory (Oct 1); Go client v6 RC (Oct 2); Verba CVE (Oct 4); v1.40.0 with first **licence-gated features** (Oct 7); Engram plugin for Claude Code (Oct 8) | [blog](https://weaviate.io/blog/weaviate-security-release-googlemodules-2026), [v1.40.0](https://github.com/weaviate/weaviate/releases/tag/v1.40.0), [blog](https://weaviate.io/blog/engram-for-claude-code), [GHSA](https://github.com/advisories/GHSA-8456-r8c8-j656) | GHSA (CNA VulDB) for Verba | v1.39.12/v1.38.21 patches (Oct 12) not ledgered |

## 4. Dated event evidence and capabilities

Full row detail is in the [CSV](076-weaviate.events.csv): 37 rows, IDs `CI2026-076-001`…`037`. Highlights:

| Event ID | Published UTC / underlying event date | Claim or observed feature | Availability and limitations | Source link (type) | Independent check | E0–E4 working grade |
|---|---|---|---|---|---|---|
| CI2026-076-002 | 2026-04-16 | Built-in MCP server at `/v1/mcp`: four tools, disabled by default, RBAC permissions `read_mcp`/`create_mcp`/`update_mcp` | Preview; GA label conflict (see 018) | [release](https://github.com/weaviate/weaviate/releases/tag/v1.37.0) | none independent | E2 |
| CI2026-076-006 / 019 | 2026-04-28 / 07-01 | DigitalOcean offers managed Weaviate (private → public preview) | Second-entity record; not usage | [DigitalOcean](https://docs.digitalocean.com/release-notes/weaviate/) | — | E2 (second entity) |
| CI2026-076-014 / 035 | 2026-06-08 / 10-04 | Verba RAG app archived; later CVE (≤2.1.3) with no fix expected | Archived OSS remains forkable but unpatched | [repo](https://github.com/weaviate/Verba), [GHSA](https://github.com/advisories/GHSA-8456-r8c8-j656) | NVD API | E2 |
| CI2026-076-020 | 2026-07-02 (fix merged 2026-05-28) | RBAC role-assignment privilege escalation, CVSS 3.1 8.8 | Fixed in 1.38.0; not labelled as security in release notes | [VulnCheck](https://www.vulncheck.com/advisories/weaviate-privilege-escalation-via-unchecked-permissions-in-rbac-role-assignment) | NVD API; PR 11493 | E2 |
| CI2026-076-025 / 029 / 031 / 032 | 2026-08-26 → 09-30 | Open-core split: BSD-3-Clause outside `wl/`, proprietary licence-key-gated code inside `wl/` | First tag carrying `wl/LICENSE-WEAVIATE`: v1.39.4 (2026-09-11) | [commit](https://github.com/weaviate/weaviate/commit/8677d32e173ca5154ce5346b61f3f366e498aeaf) | third-party review (unassessed) | E2 (repository artefact) |
| CI2026-076-026 / 033 | 2026-09-07 / 10-01 | Google modules could leak the operator's Google credential via `apiEndpoint`, including from a read-only GraphQL parameter; High (7.1) | Fixed in v1.39.3; disclosed 24 days later; CVE pending | [blog](https://weaviate.io/blog/weaviate-security-release-googlemodules-2026) | release v1.39.3 | E2 (vendor advisory) |
| CI2026-076-028 | 2026-09-14 | `wcloud` CLI with a stable JSON envelope for coding agents | Beta v0.1, MIT | [release](https://github.com/weaviate/weaviate-cloud/releases/tag/v0.1.1) | — | E2 |
| CI2026-076-036 | 2026-10-07 | v1.40.0: Namespaces GA **and** "Make namespaces a feature requiring license"; deduplicated backups gated on licence key | "Breaking Changes: none" in the same notes | [release](https://github.com/weaviate/weaviate/releases/tag/v1.40.0) | `wl/` listing at tag | E2 |
| CI2026-076-037 | 2026-10-08 | Engram plugin for Claude Code uploads each prompt and reply to Engram | Plugin repo shows no detected licence | [blog](https://weaviate.io/blog/engram-for-claude-code) | repo metadata | E1 |

**Feature inventory (vendor-documented, not exercised by us):**

| Area | In-window change | Class |
|---|---|---|
| Agent interfaces | Built-in MCP server (1.37 preview → 1.38 "GA" per blog, "Preview" per release notes); standalone MCP server deprecated; `wcloud` agent-first CLI; Engram plugin for Claude Code | shipped / preview / conflicting label |
| Agent services (hosted, proprietary) | Engram preview → GA; Query Agent Search Mode `effort` (weaviate-agents 1.8.0); free tiers for database, Query Agent, Engram | shipped (vendor) |
| Retrieval quality | Extensible tokenizers (accent folding, stopword presets); Hybrid MMR; Boost API; BM25/BlockMax rework; nested object filtering; Search REST API (experimental); gRPC-web | mixed GA/preview |
| Index/compression | HFresh disk index GA (1.38), default on free tier (vendor); RQ4 4-bit quantization; HFresh MUVERA (1.40) | shipped / preview |
| Operations | Incremental and deduplicated backups (latter licence-gated); Namespaces (preview → GA, licence-gated in 1.40); async replication by default; collection export | shipped |
| Security | 3 CVEs in window (API-key auth bypass low; RBAC privilege escalation high; Verba info disclosure medium) plus a vendor-disclosed High Google-module credential leak; SSRF header validation; debug endpoints off by default; Cloud console RBAC roles | observed advisories |
| Licensing | Open-core split with licence-key gating (Aug 26 → Oct 7); enterprise-edition link in licence text returned 404 on 2026-10-16 | observed |
| Ecosystem | DigitalOcean managed Weaviate; text2vec- and generative-digitalocean modules; generative-deepseek, generative-meta, multi2vec-twelvelabs modules; Go client v6 rewrite (alpha → RC) | shipped / preview |
| Discontinuations | Verba archived; standalone MCP server deprecated | observed |

## 5. What the company says it intends to do

| Verbatim or close paraphrase of public direction (<=25 words per source quoted) | Link/date | Promised horizon | Status (planned, tentative, uncommitted) | Missing/contradictory context |
|---|---|---|---|---|
| "More coming soon, including Engram – memory and context management for agents – and Model Evaluation." | [2026-04-15](https://weaviate.io/blog/aws-shared-cloud-launch) | "soon" | Engram delivered (GA Jun 3); Model Evaluation not observed in window | — |
| "We are working to expand Weaviate Shared Cloud to more regions and providers" | same | none | uncommitted | no list of regions |
| Continual-learning and multi-agent Engram templates "available in the following weeks" | [2026-06-03](https://weaviate.io/blog/engram-generally-available) | weeks | not verified as delivered | — |
| Extensible tokenizers: "better support for CJK languages coming in phase 2" | [v1.37.0 notes](https://github.com/weaviate/weaviate/releases/tag/v1.37.0) | none | planned | — |
| "if we are going to build and scale a platform, the way in should be free across its entirety" | [2026-06-17](https://weaviate.io/blog/weaviate-free-tier) | ongoing | stated policy | Coexists with licence-key gating of some self-hosted features from Oct 7 |
| Google-modules post: "we will update this post with the CVE ID once it has been issued" | [2026-10-01](https://weaviate.io/blog/weaviate-security-release-googlemodules-2026) | none | pending | — |
| Preview features: "The API and behavior may change in future releases." (MCP server) | [1.37 blog, 2026-04-23](https://weaviate.io/blog/weaviate-1-37-release) | none | tentative | — |

These are **company statements**, not forecasts we endorse. No public dated roadmap was found.

## 6. Independent interpretation: direction and alternative scenarios (researcher's conditional 2027–2031 view)

| Hypothesis for 2027–2031 | Supporting observations | Rival explanations | Disconfirming signals | Confidence/unknowns |
|---|---|---|---|---|
| H1: Open-source vector databases will keep a permissive core but move multi-tenant and operational features behind licence keys (open core) | Aug–Oct 2026 `wl/` split; Namespaces and deduplicated backups gated in 1.40.0 | Gating may stay limited to a few enterprise features; it may also be reversed | `wl/` stays at ≤3 features through 2028, or gated features return to BSD | moderate that the split exists; low for its trajectory |
| H2: Databases will expose agent-native interfaces (MCP, JSON-envelope CLIs, memory services) as first-class APIs | Built-in MCP server; standalone server deprecated; `wcloud`; Engram plugin | Marketing alignment with an agent trend; usage may stay low | MCP endpoint deprecated or usage not reported; agents keep using plain SDKs | low–moderate; no usage data |
| H3: "Memory for coding agents" services will raise data-governance questions faster than they show task gains | Engram plugin uploads prompts and replies; team-shared topics | Users may accept the trade if tasks improve | Controlled tasks show accepted-task gains without data-handling incidents | low; untested |
| H4: Security fixes in fast-moving OSS databases will often ship before, or without, a labelled advisory | RBAC fix shipped May 28 and CVE assigned Jul 2 by a third party; Google-module fix Sep 7 and disclosure Oct 1; SSRF fix with no advisory | Responsible-disclosure embargo is deliberate and good practice | Release notes routinely label security fixes at release time | moderate for "lag exists"; lag reasons unknown |

These are hypotheses for testing, not company strategy or fact.

## 7. Implications for the GitHub 1000 study

| M1–M7 construct | Possible observable effect | Study design to test it | Negative/null explanation | Measurement boundary |
|---|---|---|---|---|
| M1 AI coding-agent change | Retrieval vendors ship MCP endpoints, agent-oriented CLIs and memory plugins; the upstream repository itself keeps an agent instruction file (`CLAUDE.md`, 8 commits by 2026-09-14) and some in-window commits carry a disclosed AI co-author trailer | Count agent-facing interfaces per release over time | Interfaces exist but are unused | Repository-level disclosure only; no inference about individual developers or undisclosed authorship |
| M2 accepted task quality | Hybrid MMR, Boost, Search Mode effort claim retrieval gains (nDCG@10 57.5 vs 13.0, vendor) | Fixed retrieval tasks with hidden relevance judgements | Gains do not transfer to code/doc retrieval | Vendor benchmarks are not task outcomes |
| M3 discoverability | Free tier, DigitalOcean listing, vendor-submitted HN posts | Separate vendor-originated from third-party mentions | Mentions are not reuse | Stars/press never used as outcomes |
| M4 verified third-party reuse | DigitalOcean managed offering; a third-party GUI (Apache-2.0, created 2026-07-31) seen on HN | Trace consented downstream repos that pin and run Weaviate | Presence without execution | Pinned commits, executed tests only |
| M5 rights/security/provenance | Licence split mid-window; licence-gated features in a "no breaking changes" release; 3 CVEs plus a vendor-disclosed High; archived Verba with an unpatched CVE; repos with no licence | Licence check per pinned version (not per repo name); advisory check before reuse | Gating may not affect the BSD features a reuser needs | Licence files at a pinned tag; not legal advice |
| M6 review/maintenance and lifecycle cost | 74 stable server releases (plus 8 release candidates) across six minor lines (1.35–1.40) in the window; Go client major rewrite; deprecations | Measure upgrade minutes for a pinned example across 1.37→1.40 | Upgrades are cheap in practice | No kWh/CO2e inferred from heap or quantization figures |
| M7 actionable interventions | Pin versions, record licence per tag, prefer BSD-only paths, keep MCP disabled unless needed | See §8 | Guardrails add friction without value | Synthetic tasks only |

Vendor claims such as "many millions of active Weaviate databases" are **not** independent adoption evidence.

## 8. One practical, falsifiable change for the maintainer's own repositories

**Repository/component:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study) documentation and research corpus, used as a **synthetic, network-free** retrieval task. The disabled Trending `capture` command stays disabled.

**Candidate practice (not yet validated):** Before answering "where is X documented / which file enforces Y" questions while working on this repository, retrieve from a local hybrid (BM25 + vector) index of `docs/`, `research/` and `trending_study/` instead of plain `grep`/file browsing. Reuse first: compare (A) `ripgrep` plus reading files, the existing baseline, with (B) a self-hosted Weaviate container pinned to a BSD-only path. For B, record the exact image tag and use no licence key, no `wl/` features, MCP disabled and no external model-provider modules. Use a local embedding model, or BM25-only if none is approved. Do not build a new search tool.

**Treatment/control and frozen comparable task:** A person other than the operator freezes 20 lookup questions with **hidden reference answers** (file path plus line range), for example "which test enforces chronological ledger rows?". The same operator answers all 20 in each arm, in randomized order, with a 3-minute cap per question. Accepted-task unit: one answer whose cited path and lines match the hidden reference, judged by the question author.

**Success and guardrails:** Primary measure: accepted answers out of the 20 assigned (timeouts and wrong answers stay in the denominator). Guardrails:
- no network egress from the container beyond the local host;
- no credentials or personal data indexed;
- no new dependency added to the repository;
- full unit suite green;
- the licence of the exact image tag recorded before use.

Measured human work: setup minutes, per-question minutes and index-refresh minutes after a docs change. Cost and energy: none are estimated, and nothing is metered beyond wall-clock time.

**Stop/reversal rule:** Stop and keep arm A if B does not raise accepted answers by at least 3 of 20, if setup and refresh exceed 60 minutes in total, or if any required feature needs a licence key or a hosted service. **No trial executed; no effect estimated.**

## 9. Findings, uncertainties and review outcome

- **Observed/shipped (documentary):**
  - four minor server releases (1.37.0–1.40.0) plus many patches, with tag dates confirmed via `gh api`;
  - built-in MCP server;
  - HFresh GA;
  - Namespaces;
  - a licence split confirmed in repository files at tags, with licence-gated features from v1.40.0;
  - three in-window CVEs and one vendor-disclosed High credential leak;
  - Verba archived;
  - the standalone MCP server deprecated;
  - `wcloud` CLI v0.1.1;
  - Python client releases 4.21.0–4.23.1 (PyPI times confirmed), TypeScript client 3.13.0–3.15.0 (npm times confirmed) and the Go v6 alpha→RC series;
  - DigitalOcean managed Weaviate private → public preview (second entity).
- **Claims/announcements only:** Engram GA and its durability claims; the free-tier allowances; "many millions of active databases" and downloads "approaching double-digit millions"; nDCG@10 57.5 vs 13.0; the 45% heap reduction for RQ4; HFresh as the free-tier default; the AWS regions; the Cloud console RBAC roles.
- **Conjectures and unknowns:** H1–H4 in §6. Also unknown:
  - whether self-hosted Namespaces users lose function when upgrading to 1.40.0;
  - the enterprise licence terms (the link returned 404);
  - incident history (no reachable status page);
  - real usage.
- **Important contradictory or null evidence:**
  - (a) MCP server: "GA" in the 1.38 blog vs "Secure MCP Server (Preview)" in the v1.38.0 release notes. Separately, the standalone README says the built-in server is available "from v1.37.1", while the v1.37.0 notes include it.
  - (b) v1.40.0 lists "Breaking Changes: none" while making Namespaces require a licence.
  - (c) Python client 4.21.0: PyPI upload 2026-04-23 vs GitHub release 2026-04-28.
  - (d) The RBAC privilege-escalation fix shipped without a security label; its CVE came from a third party five weeks later, and its GHSA is unreviewed.
  - (e) A web-search summary said Weaviate 1.32 was the stable version as of March 2026. Release tags contradict this (v1.36 was released in March), so the claim was not used.
  - (f) Ramp vendor-share figures differ between a search snippet (June 2026: 15%, down 3 points) and the live page (October 2026: 10%, down 5 points). Both are spend-tracker estimates, graded E0 and not ledgered.
  - (g) No independent news coverage of the licence change was found in the window. The only third-party description found is one review page of unassessed reputation.
- **#56 candidates (not minted):** DigitalOcean release notes (2026-04-28, 2026-07-01); VulnCheck CVE-2026-59093 (2026-07-02); GHSA-jqpm-wf57-qx5c (2026-06-08); GHSA-8456-r8c8-j656 (2026-10-04). Each needs human reading before a `NEWS-YYYY-NNNN` ID is assigned.
- **Reviewer links and audit date:** none yet. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

## Independent source spot-check (2026-10-16)

23 of 37 ledger rows and the ownership baseline were re-checked on 2026-10-16. Methods: robots.txt was checked for each site first; `curl` with a generic user agent plus a text grep of each page; `gh api` for releases, commits, file contents at tags, PRs and the GitHub advisory database; PyPI and npm JSON; and the NVD CVE API 2.0 for three CVEs. Outcome: **23 confirmed, 0 corrected, 0 unverifiable, 0 wrong**. No CSV change was needed, and event IDs are unchanged.

| Rows | Outcome | Note |
|---|---|---|
| Ownership | confirmed | The about page's latest press item is "Weaviate Raises $50 Million Series B" dated 21 Apr, 2023. The licence text names "Weaviate BV". |
| 001, 011, 015 | confirmed | `datePublished` 2026-04-15, 2026-06-03 and 2026-06-17. US East (N. Virginia) and Europe (Frankfurt); "More coming soon, including Engram … and Model Evaluation". The free-tier post is by Bob van Luijt, CEO: "many millions of active Weaviate databases", "approaching double-digit millions", no credit card or time expiration. |
| 002, 012, 018 | confirmed | v1.37.0 (2026-04-16): "Secure MCP Server (Preview)", Drop vector index "(Experimental)", BlobHash, accent folding, Breaking Changes *none*. The 1.37 blog: disabled by default, `MCP_SERVER_ENABLED`, four tools, `read_mcp`/`create_mcp`/`update_mcp`. v1.38.0 (2026-06-05): "HFresh (GA)", still "Secure MCP Server (Preview)", PR 11493 (merged 2026-05-28). The 1.38 blog (`datePublished` 2026-06-25) says HFresh and the MCP Server reach "general availability", so the label conflict is real. |
| 005, 021, 024 | confirmed | PyPI weaviate-client 4.21.0 at 2026-04-23T10:37Z vs GitHub release 2026-04-28 (as §9(c) says), BSD 3-clause. npm 3.14.0 at 2026-07-17T11:03Z, BSD-3-Clause; Boost and diversity PRs present. weaviate-agents 1.8.0 at 2026-08-11T13:46Z; "nDCG@10 to 57.5 compared to 13.0" on BRIGHT Biology. |
| 006, 019 | confirmed | DigitalOcean notes: 28 April GA of Vector Databases with Weaviate "in private preview", "not billed"; 28 May control panel in private preview; 1 July public preview "enabled for all users", `/v2/vector-databases`, `doctl`. |
| 009, 014 | confirmed | mcp-server-weaviate: deprecation commit 2026-05-25, merge 2026-05-26, not archived; the README says "from v1.37.1". Verba: archived, BSD-3-Clause, last commit "goodbye" 2026-06-08. |
| 013, 020, 035 | confirmed | GHSA-jqpm (CVE-2026-11500): reviewed, low, up to 1.37.7, patched in 1.38.0-rc.0; NVD shows CNA VulDB 5.0 (v3.1) and 1.3 (v4.0). CVE-2026-59093: VulnCheck page dated 7/2/2026, `assign_and_revoke_users`, < 1.38.0, v4 8.7; NVD adds v3.1 8.8 from VulnCheck; GHSA-667j is unreviewed. GHSA-8456 (CVE-2026-105145): unreviewed, Verba up to 2.1.3, 5.3 (v3.1), "did not respond in any way". |
| 025, 029, 032 | confirmed | Commit 8677d32e (2026-08-26) adds LICENSE-BSD and wl/LICENSE-WEAVIATE plus the `WEAVIATE_LICENSE` toggle. `wl/LICENSE-WEAVIATE` is absent at v1.39.2, v1.39.3 and v1.38.15 and present at v1.39.4 (2026-09-11). 66422093 (2026-09-15): `wv8.<license_id>.<32-byte ed25519 seed>`, "validates the key's form only and makes no network requests". e0cc80ce (2026-09-30): "Copyright Weaviate BV 2026-present, all rights reserved". Same file at v1.39.12 and v1.40.0. |
| 026, 033 | confirmed | v1.39.3 title "… Modules and GraphQL security Fixes …", with the nearObject beacon fix. Security post (2026-10-01): "High (7.1)", "< v1.39.3", the GraphQL path needs "only ordinary read access", CVE pending, Cloud and Marketplace patched, "no indication" of exploitation. |
| 030, 036, 037 | confirmed | RQ post (2026-09-17): "45% heap reduction", "significantly faster", TurboQuant comparison. v1.40.0 (2026-10-07): "Namespaces (GA)", "Make namespaces a feature requiring license", "Gate deduplicated backups on a Weaviate license key", Breaking Changes *none*; `wl/` holds backupdedupe, namespaces and selfrecovery. Engram plugin post (2026-10-08): saves "your message and Claude's reply", "free for up to 1,000 runs per month". The release count of 82 in-window objects (74 stable plus 8 pre-releases) also matches. |

**Process note:** weaviate.io's robots.txt disallows `/blog/rss.xml` for all user agents, but the search log records that the original screen fetched it. This spot-check did not fetch it. The ledgered facts do not depend on the feed, because every blog row was confirmed from its post page. This is an AI-assisted spot-check, not qualified human review.
