# Anyscale — provisional six-month technology intelligence screen (069)

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** This report, its [event ledger](069-anyscale.events.csv) and [search log](069-anyscale.search-log.md) are an AI-assisted first-pass documentary source screen. No qualified human has reviewed them. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open. Nothing here is a verified task outcome, an adoption measure or an endorsement.

- **Company watchlist ID:** 069
- **Research issue:** [#137](https://github.com/MSKazemi/github-trending-1000-study/issues/137); evidence corpus link [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56) (no `NEWS-YYYY-NNNN` item minted here; candidates listed in §9).
- **Ownership and product boundaries (as of 2026-10-12):** Anyscale, Inc. (footer "© Anyscale, Inc 2026"), San Francisco, privately held and venture-funded. On **2026-07-30** Anyscale and Nscale (Nscale Limited, London) announced a **definitive agreement** for Nscale to acquire Anyscale, "subject to closing conditions and regulatory approvals", expected to close in H2 2026, terms undisclosed ([Nscale press release](https://www.nscale.com/press-releases/nscale-acquires-anyscale)). **No closing announcement was found by 2026-10-12**: CNBC on 2026-09-18 still described "plans to acquire", and Anyscale's About page still read "Anyscale to Join Nscale" when accessed 2026-10-16. Anyscale is therefore treated as an **independent company with a pending acquirer**. Filing-level verification was **not** performed (SEC/EDGAR deliberately not accessed).
- **Open-source boundary:** Ray ([ray-project/ray](https://github.com/ray-project/ray), Apache-2.0) and KubeRay ([ray-project/kuberay](https://github.com/ray-project/kuberay), Apache-2.0) are community projects; per the Nscale/Anyscale release, Ray was donated to the **PyTorch Foundation** in 2025 (pre-window baseline). Anyscale's platform, Runtime, operator, scheduler and the `anyscale` CLI (PyPI licence field "AS License", not an OSI licence) are **proprietary**. Ray events are attributed here because Anyscale staff author most release posts, but Ray releases are not Anyscale-only events.
- **Product URL and company newsroom:** [anyscale.com](https://www.anyscale.com/), [blog](https://www.anyscale.com/blog) ([RSS](https://www.anyscale.com/rss.xml)), [press](https://www.anyscale.com/press), [platform release notes](https://docs.anyscale.com/release-notes), [CLI/SDK notes](https://docs.anyscale.com/release-notes/cli-sdk), [Ray releases](https://github.com/ray-project/ray/releases), [Ray security advisories](https://github.com/ray-project/ray/security/advisories), [PyPI `ray`](https://pypi.org/project/ray/), [PyPI `anyscale`](https://pypi.org/project/anyscale/).
- **Analysis window:** 2026-04-12 to 2026-10-12 inclusive; accessed 2026-10-16.
- **Researcher / factual reviewer / review date:** AI-assisted screen / **pending** / **pending**.
- **Status:** screened (provisional); 42 ledger rows across all seven calendar segments.
- **Source coverage:** sitemap (lastmod) + RSS + 50 raw-fetched blog/press pages, monthly platform release notes (Markdown), CLI/SDK changelog, Ray/KubeRay GitHub releases and security advisories via `gh api`, PyPI JSON, CISA KEV JSON feed, Hacker News Algolia API, two web searches, and independent reporting (Reuters via The Star, TechCrunch, SiliconANGLE, CNBC, The Next Web). Inaccessible: status.anyscale.com (403), Bloomberg (403), The Hacker News (403). See the [search log](069-anyscale.search-log.md).
- **Evidence grades:** company-watch E0–E4 tiers from the [method](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md), not the separate [lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md).

## 1. Search and inclusion audit

Summary only; exact requests, opened URLs and exclusions are in the [search log](069-anyscale.search-log.md). Search-engine result totals were not exposed and are recorded as **unknown**, not zero.

| Search run UTC | Site/engine | Full query and dates | Found | Screened | Included | Excluded/why | Coverage limitation |
|---|---|---|---:|---:|---:|---:|---|
| 2026-10-16 | anyscale.com sitemap + RSS + raw HTML | blog/press URLs with lastmod ≥ 2026-04-01; RSS (Aug 18 onward only) | ~60 candidate blog/press URLs | 51 opened | 15 rows | lastmod-only refreshes of old posts, case studies, event recaps, opinion pieces (log) | `lastmod` ≠ publication date; `datePublished` used |
| 2026-10-16 | docs.anyscale.com release notes | April–October 2026 platform notes; CLI/SDK changelog; operator notes | ~90 dated entries | all | 17 rows | routine CLI version bumps, instance-type additions, operator versions (log) | notes are mutable; no archived copy |
| 2026-10-16 | GitHub API + PyPI | Ray releases, Ray advisories, KubeRay releases, anyscale org repos | 7 Ray releases, 2 in-window advisories, 3 KubeRay releases | all | 8 rows | Ray 2.55.1, 2.56.1 and KubeRay v1.6.2/v1.7.1 folded into context | release notes are maintainer statements |
| 2026-10-16 | HN Algolia + 2 web searches + CISA KEV | Anyscale, Nscale, Ray; acquisition price; CVE-2025-62593 KEV | 19 + 718 + 5 HN hits; 20 search results | ~25 | 6 rows | aggregators/E0 snippets; Bloomberg/THN 403 | "Nscale" query matches "scale" broadly; most hits irrelevant |

## 2. Verified company/product identity and baseline

Anyscale sells a managed platform for running Ray workloads (data processing, training, post-training/RL, LLM serving) on AWS, Google Cloud, Kubernetes and — new in-window — Azure. Its open-source dependency, Ray, is now PyTorch Foundation–governed; Anyscale's own commercial surface (platform, Anyscale Runtime, operator, scheduler, CLI) is proprietary. Several in-window example repositories in the `anyscale` GitHub org (for example `llm-serving-for-coding-agents`, `pd-amd-blogpost`) show **no detected licence** via the GitHub API on 2026-10-16, so they are not clearly reusable.

**Pre-window baseline (context only, not counted):** Ray donated to the PyTorch Foundation in 2025; CVE-2025-62593 (browser/DNS-rebinding RCE) disclosed and fixed in Ray 2.52.0 on 2025-11-26 ([GHSA-q279-jhrf-cc6v](https://github.com/ray-project/ray/security/advisories/GHSA-q279-jhrf-cc6v)); opt-in token authentication introduced in Ray 2.52.0; Anyscale on Azure first announced 2025-11-04. TechCrunch (2026-07-30) states Anyscale was valued at $1.38B in a 2022 Series C (not checked against a primary source). **Post-window, excluded:** KubeRay blog post of 2026-10-15.

## 3. Month-by-month discoveries (six calendar months + partial endpoints)

| Month | Announcements/changes | Primary URLs | Independent reporting | Notes or no-result limitations |
|---|---|---|---|---|
| 2026-04-12..30 | Ray 2.55.0 (Apr 15); Parquet deserialization RCE advisory (Apr 21); **Agent Skills GA** for Claude Code and Cursor (Apr 22); API-key max-expiry setting (Apr 24); memory-default change (Apr 29); CopyFail kernel advisory (Apr 30) | [Ray 2.55.0](https://github.com/ray-project/ray/releases/tag/ray-2.55.0), [GHSA-mw35-8rx3-xf9r](https://github.com/ray-project/ray/security/advisories/GHSA-mw35-8rx3-xf9r), [blog](https://www.anyscale.com/blog/announcing-anyscale-agent-skills-ray), [April notes](https://docs.anyscale.com/release-notes/platform/2026/april) | none found | SkyRL VLM post (Apr 24) excluded as research write-up |
| 2026-05 | Multi-version services narrowed to private beta (May 4); Agent Skills 0.2.0 post-training skill (May 14); log-ingestion limit 512 MB/s (May 15) | [May notes](https://docs.anyscale.com/release-notes/platform/2026/may), [blog](https://www.anyscale.com/blog/anyscale-llm-post-training-skill) | none found | ML-ops opinion post (May 21), multi-agent Ray Serve tutorial (May 7) excluded |
| 2026-06 | **Anyscale on Azure public preview** (Jun 2); AMD MI325X prefill-decode benchmark incl. negative cases (Jun 12); Ray 2.56.0 (Jun 29) | [press](https://www.anyscale.com/press/anyscale-on-azure-cost-efficient-and-sovereign-ai-microsoft-build), [blog](https://www.anyscale.com/blog/ray-vllm-prefill-decode-disaggregation-amd-mi325x-67-percent-savings), [Ray 2.56.0](https://github.com/ray-project/ray/releases/tag/ray-2.56.0) | HN submissions only (no discussion) | Debug-skill walkthrough (Jun 11), GKE serving post (Jun 18), Ray Day recaps excluded |
| 2026-07 | WebDataset pickle RCE advisory, fixed in 2.56.0 (Jul 1); restricted cloud roles beta (Jul 1); Skills 0.3.0 adds Codex (Jul 2); resource-isolation write-up (Jul 14); physical-AI skill (Jul 23); service token rotation (Jul 27); CLI adds GitHub Copilot target (Jul 28); **Nscale acquisition agreement** (Jul 30) | [GHSA-hhrp-gw25-jr43](https://github.com/ray-project/ray/security/advisories/GHSA-hhrp-gw25-jr43), [July notes](https://docs.anyscale.com/release-notes/platform/2026/july), [blog](https://www.anyscale.com/blog/anyscale-signs-definitive-agreement-to-join-nscale) | [Reuters via The Star](https://www.thestar.com.my/tech/tech-news/2026/07/30/ai-cloud-provider-nscale-to-buy-software-startup-anyscale), [TechCrunch](https://techcrunch.com/2026/07/30/nscale-buys-anyscale-as-it-seeks-to-own-more-of-the-ai-compute-stack/), [SiliconANGLE](https://siliconangle.com/?p=799592) | Bloomberg original (the $1.65B source) returned 403 |
| 2026-08 | OpenTelemetry deadlock notice + Ray 2.57.0 (Aug 10–11); **CISA KEV listing of CVE-2025-62593** (Aug 17) and Anyscale response (Aug 19); KubeRay v1.7.0 History Server beta (Aug 20); GPU observability beta (Aug 20); Ray 2.58.0 incl. experimental gVisor sandbox (Aug 23); Ray Summit launch posts: native sandboxing, KubeRay Connect private preview, 10k-node scaling (Aug 25) | [August notes](https://docs.anyscale.com/release-notes/platform/2026/august), [CISA KEV feed](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json), [blog](https://www.anyscale.com/blog/announcing-native-sandboxing-in-ray) | [The Next Web Aug 18](https://thenextweb.com/news/cisa-kev-ray-ai-framework) | Further Aug 25 posts (Shuffle V2, FP8 SkyRL, GPU-native operators, learning loops, token-aware routing) folded into Ray release rows or excluded |
| 2026-09 | Ray Summit recap (Sep 8); Anyscale scheduler beta and machine-pools deprecation (Sep 10); Nscale IPO filing reported (Sep 18) | [blog](https://www.anyscale.com/blog/ray-summit-2026-recap), [September notes](https://docs.anyscale.com/release-notes/platform/2026/september) | [CNBC Sep 18](https://www.cnbc.com/2026/09/18/nscale-ai-cloud-provider-ipo-nscl.html) | Thinnest month for Anyscale-originated news; Tom's Hardware Nscale/ByteDance story (Sep 23) concerns the acquirer only, not read |
| 2026-10-01..12 | Ray 2.59.0: LLM APIs GA, **token auth on by default for local clusters** (Oct 2); GPU pipelining beta (Oct 2); Skills 0.6.0 adds Kiro (Oct 5); **Azure GA** (Oct 7); self-hosted coding-agent serving guide and cost model (Oct 8) | [Ray 2.59.0](https://github.com/ray-project/ray/releases/tag/ray-2.59.0), [October notes](https://docs.anyscale.com/release-notes/platform/2026/october), [blog](https://www.anyscale.com/blog/run-coding-agents-on-your-own-gpus) | none found | Robotics customer post (Oct 9) excluded as case study; system-logs tab (Oct 7) noted, not ledgered |

## 4. Dated event evidence and capabilities

Full row detail is in the [CSV](069-anyscale.events.csv) (42 rows, IDs `CI2026-069-001`…`042`). Highlights:

| Event ID | Published UTC / underlying event date | Claim or observed feature | Availability and limitations | Source link (type) | Independent check | E0–E4 working grade |
|---|---|---|---|---|---|---|
| CI2026-069-003 | 2026-04-22 | Agent Skills GA for Claude Code and Cursor; vendor claims "5x development speed" vs general-purpose agents | Distributed via proprietary CLI; no task set or denominator for 5x | [blog](https://www.anyscale.com/blog/announcing-anyscale-agent-skills-ray) (first party) | April release notes | E2 (documentary) |
| CI2026-069-002 / 013 | 2026-04-21 / 2026-07-01 | Two high-severity deserialization RCEs in Ray Data loaders; the July advisory says the April fix did not cover the same bug class at another code site | Fixed in 2.55.0 / 2.56.0 | GitHub Security Advisories | GitHub API metadata | E2 |
| CI2026-069-019 / 040 | 2026-07-28 / 2026-10-05 | Skill installer extended to GitHub Copilot and Kiro; pre-tool-use command-screening hooks; docs warn shared `~/.agents/skills` lets other agents load skills **without** the hooks | Shipped; hook effectiveness untested | CLI changelog, platform notes | PyPI upload times | E2 |
| CI2026-069-020…022, 037 | 2026-07-30 … 2026-09-18 | Nscale agreement to acquire Anyscale; reported ~$1.65B price (Bloomberg, anonymous); closing pending | Announced only | Anyscale + Nscale press | Reuters, TechCrunch, SiliconANGLE, CNBC | E1 |
| CI2026-069-025…027 | 2026-08-17 … 08-19 | CISA KEV lists CVE-2025-62593 (dueDate 2026-08-20); Anyscale says upgrade to ≥2.52.0 and enable token auth | Fix pre-dates window | [CISA KEV JSON](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json) (government record) | TNW; GHSA | E2 (government record) |
| CI2026-069-030 / 031 | 2026-08-23 / 08-25 | Experimental gVisor Ray Sandbox; vendor: 100,000 sandboxes in 20 s on GKE | Experimental; isolation not audited | Ray 2.58.0 release; blog | release notes | E2 / E1 for scale claim |
| CI2026-069-038 | 2026-10-02 | Ray 2.59.0: token authentication on by default for local clusters; dashboard redacts `runtime_env`; LLM APIs GA | Remote/multi-node clusters unchanged | [release](https://github.com/ray-project/ray/releases/tag/ray-2.59.0) | PyPI 2026-10-02T07:01Z | E2 |
| CI2026-069-042 | 2026-10-08 | Self-hosted open-model serving for Claude Code/Codex/Cursor; cost model ~$58 vs ~$800 per developer-month | Vendor "planning projections rather than a TCO"; no quality comparison; repo has no licence | [blog](https://www.anyscale.com/blog/run-coding-agents-on-your-own-gpus) | none | E1 |

**Feature inventory (vendor-documented, not exercised by us):**

| Area | In-window change | Class |
|---|---|---|
| Coding-agent tooling | Agent Skills GA (Apr 22), 0.2.0 post-training (May), 0.3.0 Codex (Jul 2), physical-AI skill (Jul 23), Copilot target (CLI 0.26.106), Kiro target and skill-scoped Claude Code hook (0.6.0); one-time "I accept" security acknowledgment | shipped (vendor) |
| Open-source Ray | 2.55.0 → 2.59.0: DataSourceV2 default, Shuffle V2/external shuffle, Serve LLM re-architecture, KV-cache/token-aware routing, RocksDB GCS FT, TPU subslices, experimental gVisor sandbox, LLM APIs GA | shipped (maintainers) |
| Security defaults | Token auth default for local clusters (2.59.0); dashboard secret redaction; read_hudi unpickling guard; cloudpickle tensor metadata opt-in (2.55.0); webdataset decoder fix (2.56.0); API-key max expiry; service token rotation; restricted cloud roles (beta) | shipped / beta |
| Observability | KubeRay History Server beta; GPU observability beta / private preview; system-logs tab; log ingestion limit | mixed |
| Platform/cloud | Azure public preview → GA; Anyscale scheduler beta (Kueue-modelled); machine pools deprecated (EOL 2027-03-10); KubeRay Connect private preview; GPU pipelining beta (proprietary Runtime) | mixed |
| Licensing | Ray, KubeRay Apache-2.0; `anyscale` CLI "AS License"; several in-window example repos without a detected licence | observed |
| Breaking/behaviour changes | memory defaults (Apr 29); multi-version services narrowed (May 4); DataSourceV2 default (2.57.0); shuffle setting renames (2.59.0); deprecated CLI flags (0.26.107–108) | observed in notes |

## 5. What the company says it intends to do

| Verbatim or close paraphrase of public direction (<=25 words per source quoted) | Link/date | Promised horizon | Status (planned, tentative, uncommitted) | Missing/contradictory context |
|---|---|---|---|---|
| "Post-closing, the Anyscale Platform will continue to run across all major cloud providers. Portability remains core to our roadmap" | [2026-07-30](https://www.anyscale.com/blog/anyscale-signs-definitive-agreement-to-join-nscale) | post-closing | planned (conditional on closing) | Closing not confirmed in window |
| "Going forward, the Anyscale + Nscale team will invest heavily in maintaining and improving Ray" | same | none stated | uncommitted | No staffing or governance commitment quantified |
| Nscale "plans to join the PyTorch Foundation as a Platinum member" | same; Nscale release says "will join" | none stated | planned | Membership not verified on PyTorch Foundation site |
| "We are actively working toward making token authentication the default rather than an opt-in" | [2026-08-19](https://www.anyscale.com/blog/ray-cve-2025-62593-kev-what-you-need-to-know) | "more to say about that timeline" | partly delivered (local clusters only, Ray 2.59.0) | Remote/multi-node clusters unchanged |
| Machine pools reach end-of-support 2026-12-10 and end-of-life 2027-03-10 | [September notes](https://docs.anyscale.com/release-notes/platform/2026/september) | dated | planned removal | Migration cost unknown |

These are **company statements**, not forecasts we endorse.

## 6. Independent interpretation: direction and alternative scenarios (researcher's conditional 2027–2031 view)

| Hypothesis for 2027–2031 | Supporting observations | Rival explanations | Disconfirming signals | Confidence/unknowns |
|---|---|---|---|---|
| H1: Framework vendors will ship agent "skills" for many harnesses, making skill files a de facto documentation channel | Skills for five harnesses in under six months; installer handles shared `~/.agents/skills` | Marketing channel with little effect on outcomes | Controlled tasks show no accepted-task gain over docs-only; vendors stop maintaining skills | low; untested |
| H2: Secure-by-default changes in OSS infrastructure follow external pressure rather than precede it | Token-auth default shipped ~7 weeks after KEV listing; vendor said "working toward" it | Planned roadmap that coincided; KEV only accelerated communication | Default had been merged before Aug 17 (check PR #64755 merge date) | low; one case |
| H3: Vertical integration (neocloud acquires orchestration software) will pressure OSS neutrality | Nscale deal; parent IPO filing with large losses (CNBC) | Foundation governance protects Ray; Anyscale states multi-cloud commitment | Ray governance stays multi-vendor and non-Anyscale contributions keep growing after closing | low; deal not closed |
| H4: Self-hosted open models for coding agents become cost-competitive for mid-sized teams | Vendor cost model; KV-tiering and MTP gains | Projections ignore quality gap and ops labour | Accepted-task quality of open models stays clearly below closed APIs on frozen tasks | low; vendor-only data |

These are hypotheses for testing, not company strategy or fact.

## 7. Implications for the GitHub 1000 study

| M1–M7 construct | Possible observable effect | Study design to test it | Negative/null explanation | Measurement boundary |
|---|---|---|---|---|
| M1 AI coding-agent change | Framework-specific skills installed into agent harnesses | Compare agent runs with vs without vendor skills on frozen tasks | Skills add context cost without accuracy gain | Consented runs only |
| M2 accepted task quality | Vendor claims 5x speed; no denominator | Hidden-test acceptance per task, all attempts counted | Speed without acceptance | Hidden tests authored independently |
| M3 discoverability | Acquisition and KEV coverage drive attention | Separate press counts from reuse | Press is not reuse | Stars/funding never outcomes |
| M4 verified third-party reuse | Ray used by many frameworks (vendor list: veRL, NeMo-RL, SkyRL…) | Trace pinned downstream repos importing and executing Ray | Imports without execution | Pinned commits; executed tests |
| M5 rights/security/provenance | Two loader deserialization RCEs; KEV listing of an old flaw; unlicensed example repos; proprietary CLI | Licence + advisory check before reuse; version-floor policy | Unlicensed code is not reusable | Licence files and advisories at a pinned commit |
| M6 review/maintenance and lifecycle cost | Frequent default/behaviour changes; deprecations with dates | Migration minutes per minor version | Changes may be trivial in practice | No kWh/CO2e from GPU-hours or dollars |
| M7 actionable interventions | Version floors and secure defaults for dev tooling | See §8 | Guardrail friction | Synthetic tasks only |

Company adoption claims (attendance, customer names, "12M downloads per week") are **not** independent task outcomes or verified reuse.

## 8. One practical, falsifiable change for the maintainer's own repositories

**Repository/component:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study) offline research-artifact validators and unit tests, run as a **synthetic, network-free** task. The disabled Trending `capture` command stays disabled.

**Candidate practice (not yet validated):** a **dependency advisory floor check** in CI that fails when a pinned dependency is below the first patched version of a known advisory (the Ray pattern: a 2025 fix, a 2026 KEV listing that matters only to un-upgraded users). Reuse first: compare an existing tool (`pip-audit` against the PyPA/OSV advisory database) with the current state (no advisory check). Do not build a new scanner.

**Treatment/control and frozen comparable task:** Freeze 10 synthetic dependency-update tasks on a throwaway branch (for example, pin an old version of a test-only package with a known advisory, then ask for an unrelated feature change). Arm A: current CI. Arm B: CI plus `pip-audit` at a recorded exact version. Accepted-task unit: a change that passes the full unit suite and leaves no known-advisory pin, accepted by the human reviewer without rework. Hidden acceptance checks written by someone other than the person making the changes.

**Success and guardrails:** Primary: share of the 10 tasks where a vulnerable pin is caught before merge (all tasks counted, including abandoned). Guardrails: no network access during unit tests; the advisory database fetch happens only in the CI step and is logged; no new runtime dependency in the package; zero false blocks on clean pins; full unit suite green. Measured human work: setup minutes, triage minutes per alert, false-positive minutes. Cost: CI minutes as reported by the CI provider; no energy or CO2e estimate. No paid API use. Commit authorship stays with the maintainer.

**Stop/reversal rule:** Drop Arm B if it catches no planted vulnerable pin that Arm A missed, produces more than one false block per 10 tasks, adds more than 5 human minutes per task on average, or needs network access inside the offline test suite. **No trial executed; no effect estimated.**

## 9. Findings, uncertainties and review outcome

- **Observed/shipped (documentary):** seven Ray releases 2.55.0–2.59.0 (GitHub and PyPI times confirmed); two in-window Ray advisories (API metadata confirmed); KubeRay v1.7.0; Agent Skills GA and four later skill releases; Azure preview→GA; scheduler beta; token-auth default for local Ray clusters; CISA KEV entry for CVE-2025-62593 (confirmed in CISA's JSON feed).
- **Claims/announcements only:** 5x skill development speed; "most token-efficient skills … on the market"; up to 90% cost savings (Azure press); 1.3x–2.3x QPS / up to 67% (AMD); up to 1.5x (resource isolation); 100,000 sandboxes in 20 s; 40,000 actors on 10,000 nodes; >2,000 Summit attendees; >70% QoQ revenue growth; coding-agent cost model. Acquisition closing and Nscale's PyTorch Foundation membership remain announced only.
- **Conjectures and unknowns:** H1–H4 in §6; real task outcomes of skills; isolation strength of Ray Sandbox; the reported deal price; post-closing governance.
- **Important contradictory or null evidence:** (a) companies say terms undisclosed while Bloomberg (anonymous source, unread, 403) reports ~$1.65B; (b) a web-search summary attributed Nscale's $2B Series C at $14.6B to **Anyscale** — raw TechCrunch text shows that figure is Nscale's, and the claim was screened out; (c) GPU observability "beta for select organizations" (notes, Aug 20) vs "private preview" (blog, Aug 25); (d) log limit heading "per organization" vs body "per cloud"; (e) Skills 0.3.0 Codex date (Jul 2) vs CLI 0.26.104 (Jun 30) already referencing Codex hooks; Skills 0.6.0 Kiro (notes Oct 5) vs CLI 0.26.109 (PyPI Oct 1); (f) Ray 2.58.0 dated Aug 22 in Anyscale notes vs 2026-08-23T05:42Z on GitHub; (g) TNW calls Ray "maintained by Anyscale" though it is PyTorch Foundation–governed; (h) the July advisory explicitly states the April deserialization fix did not cover the bug class.
- **#56 candidates (not minted):** Reuters via The Star 2026-07-30; TechCrunch 2026-07-30; SiliconANGLE 2026-07-31; The Next Web 2026-08-18; CNBC 2026-09-18; CISA KEV entry (government record). Each needs human reading before a `NEWS-YYYY-NNNN` ID is assigned; the three acquisition reports are one event, not three.
- **Reviewer links and audit date:** none yet. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.
