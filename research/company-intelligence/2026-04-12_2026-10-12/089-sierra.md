# Sierra — provisional six-month technology intelligence screen (089)

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** This report, its [event ledger](089-sierra.events.csv) and [search log](089-sierra.search-log.md) are an AI-assisted first-pass documentary source screen. No qualified human has reviewed them. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open. Nothing here is a verified task outcome, an adoption measure or an endorsement.

- **Company watchlist ID:** 089
- **Research issue:** [#157](https://github.com/MSKazemi/github-trending-1000-study/issues/157); evidence corpus link [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56) (no `NEWS-YYYY-NNNN` item minted here; candidates listed in §9).
- **Ownership and product boundaries (as of 2026-10-12):** Sierra (legal name reported by SiliconANGLE as **Sierra Technologies Inc.**), co-founded by Bret Taylor and Clay Bavor; privately held and venture-funded (GV and Tiger Global led the May 2026 round; Benchmark, Sequoia and Greenoaks participated, per [SiliconANGLE](https://siliconangle.com/2026/05/04/ai-agent-startup-sierra-valued-15b-new-950m-funding-round/)). No parent company was found. Bret Taylor also chairs OpenAI's board (per SiliconANGLE and TechCrunch). That relationship matters for reading the OpenAI marketplace row. In-window acquisitions: Fragment (Paris; announced 2026-04-23) and Takeoff (described as "is acquiring" on 2026-07-23). Pre-window acquisitions reported by TechCrunch: Opera Tech and Receptive AI (late March 2026). Filing-level corporate verification was **not** performed, and no regulator site was contacted.
- **Product URL and company newsroom:** [sierra.ai](https://sierra.ai/), [news & blog](https://sierra.ai/blog) ([RSS](https://sierra.ai/rss.xml)), [sierra-research GitHub org](https://github.com/sierra-research) (tau-bench, tau2-bench, mu-bench, hyper-tau-bench), [status page](https://status.sierra.ai/) (client-rendered; history not retrievable without JavaScript), [Personal Agent Protocol site](https://personalagentprotocol.org/).
- **Analysis window:** 2026-04-12 to 2026-10-12 inclusive; accessed 2026-10-16.
- **Researcher / factual reviewer / review date:** AI-assisted screen / **pending** / **pending**.
- **Status:** screened (provisional); 34 ledger rows across all seven calendar segments.
- **Source coverage:** all 49 in-window official blog posts (the blog index's embedded `publishedAt` timestamps; 132 posts in total, matching the sitemap) were fetched as raw HTML. 34 rows were ledgered and the rest were excluded with reasons in the log. Other sources: GitHub API for four sierra-research repositories and one protocol repository, Hacker News Algolia API (7 queries), 5 web searches, and two independent outlets read in full (SiliconANGLE ×2, TechCrunch ×1). Axios returned HTTP 403. CNBC was not fetched because its robots.txt disallows Claude agents. Reuters/WSJ/NYT are not reachable by the search tool. See the [search log](089-sierra.search-log.md).

## 1. Search and inclusion audit

Summary only; exact queries, opened URLs and exclusions are in the [search log](089-sierra.search-log.md). Search engine result totals were not exposed, so they are recorded as **unknown**, not zero.

| Search run UTC | Site/engine | Full query and dates | Found | Screened | Included | Excluded/why | Coverage limitation |
|---|---|---|---:|---:|---:|---:|---|
| 2026-10-16 | sierra.ai robots.txt, sitemap, blog index | all blog posts with `publishedAt` 2026-04-12..10-12 | 49 in-window | 49 fetched raw | 30 rows | 19 (explainers, guides, office openings, case/hiring posts; see log) | page dates are vendor CMS `publishedAt`; later edits not detectable |
| 2026-10-16 | GitHub API (`gh api`) | sierra-research org repos, tau2-bench releases/tags/CHANGELOG/commits, mu-bench, hyper-tau-bench, personal-agent-protocol | 4 org repos + 1 protocol repo | 5 | 1 row (+ check URLs) | tau-bench (no in-window push) | commits counted, not read individually |
| 2026-10-16 | HN Algolia API | 7 queries, 2026-04-12..10-12 | 32 hits (overlapping) | ~16 unique relevant | 0 rows (leads) | mostly Sierra blog reposts; one aggregator | HN is a discovery channel, not evidence |
| 2026-10-16 | web search (5 queries) | funding, criticism/outage, PAP/Horizon/Takeoff coverage | unknown | ~40 | 3 rows (2 SiliconANGLE, 1 TechCrunch) | aggregators (E0), Axios 403, CNBC robots | no independent in-window criticism of Sierra's product found |

## 2. Verified company/product identity and baseline

Sierra sells a platform for building customer-facing AI agents across chat, voice and email ("Agent OS", Agent Studio, Agent SDK, Ghostwriter). It charges by outcomes rather than by seats or usage, per the vendor's own [outcome-based pricing post](https://sierra.ai/blog/outcomemaxxing). The **platform, models (Linnaeus, Darwin, Curie, Fleming) and Ghostwriter are proprietary and hosted**. The open-source surface is the research benchmarks in [sierra-research](https://github.com/sierra-research): `tau-bench` (MIT, no in-window push), `tau2-bench` (MIT), `mu-bench` (code Apache-2.0, **data CC BY-NC 4.0**) and `hyper-tau-bench` (MIT). The in-window Personal Agent Protocol has an Apache-2.0 repository under a separate `personal-agent-protocol` org, but that repository was created on **2026-10-14, after the window**.

Pre-window baseline (context only, not counted): tau2-bench v1.0.0 "τ³-bench 1.0.0 — Voice, Knowledge, Task Quality" (GitHub release 2026-03-18). This release included the voice track and tau-knowledge, which the vendor says was "first released in early March 2026". Ghostwriter launched in March 2026 per the [2026-06-15 post](https://sierra.ai/blog/how-customer-teams-became-software-builders). A $350M round at a $10B valuation in September 2025 is described by SiliconANGLE as "eight months" before May 2026, and TechCrunch also reports a $10B valuation before the May round.

## 3. Month-by-month discoveries (six calendar months + partial endpoints)

| Month | Announcements/changes | Primary URLs | Independent reporting | Notes or no-result limitations |
|---|---|---|---|---|
| 2026-04-12..30 | μ-Bench open ASR benchmark (Apr 20); AI-native engineering interview (Apr 22); Fragment acquisition (Apr 23) | [mu-bench](https://sierra.ai/blog/mu-bench-an-open-multilingual-transcription-benchmark), [interview](https://sierra.ai/blog/the-ai-native-interview), [Fragment](https://sierra.ai/blog/sierra-acquires-fragment-in-france) | [TechCrunch Apr 23](https://techcrunch.com/2026/04/23/bret-taylors-sierra-buys-yc-backed-ai-startup-fragment/) | Apr 14 "golden articles" search-evaluation post excluded (method explainer without a dated change) |
| 2026-05 | tau-voice results update (May 1); $950M round (May 4); Monitors evaluation loop (May 7); tau-knowledge results update (May 13) | [funding](https://sierra.ai/blog/better-customer-experiences-built-on-sierra), [tau-voice](https://sierra.ai/blog/tau-voice-benchmarking-real-time-voice-agents-on-real-world-tasks), [tau-knowledge](https://sierra.ai/blog/tau-knowledge) | [SiliconANGLE May 4/5](https://siliconangle.com/2026/05/04/ai-agent-startup-sierra-valued-15b-new-950m-funding-round/) | Toronto office (May 21) and four explainer/career posts not ledgered |
| 2026-06 | Outcome-pricing position (Jun 3); FedRAMP High via Knox Systems (Jun 10); Experiments A/B testing (Jun 30) | [outcomemaxxing](https://sierra.ai/blog/outcomemaxxing), [FedRAMP](https://sierra.ai/blog/certified-fedramp-high), [Experiments](https://sierra.ai/blog/let-your-customers-shape-your-agents) | none found | FedRAMP marketplace not checked; Ghostwriter-adoption post (Jun 15) and CX explainer (Jun 12) not ledgered |
| 2026-07 | SoftBank Japan exclusive partnership (Jul 14); Horizon (Jul 16); MCP Gateway lessons (Jul 22); **tau2-bench 1.0.1 grading correction** (Jul 22); Takeoff acquisition (Jul 23); Agency sandboxes (Jul 29) | [Horizon](https://sierra.ai/blog/horizon), [MCP Gateway](https://sierra.ai/blog/building-sierras-mcp-gateway-an-engineering-iceberg), [v1.0.1](https://github.com/sierra-research/tau2-bench/releases/tag/v1.0.1), [Agency](https://sierra.ai/blog/agency-secure-scalable-sandboxes-for-agents) | none read (one aggregator lead on Takeoff, unused) | Ghostwriter hackathon (Jul 1), AI-pilling (Jul 9) and Pinecone (Jul 15) posts used as context only |
| 2026-08 | Plaid integration (Aug 3); Context Engine (Aug 4); Voice Personas (Aug 7); defense-in-depth guardrails (Aug 13); release governance (Aug 20); CFO and ARR claim (Aug 31) | [Plaid](https://sierra.ai/blog/our-partnership-with-plaid), [Personas](https://sierra.ai/blog/introducing-voice-personas), [release governance](https://sierra.ai/blog/release-governance-guardrails-for-agents-at-scale) | none found | Munich (Aug 14) and Seoul (Aug 25) offices, IVR navigation (Aug 11) and follow-up sales (Aug 12) posts not ledgered |
| 2026-09 | hyper-tau-bench open-sourced (Sep 8); AIUC-1 certification (Sep 17); export/portability statement (Sep 22); Ghostwriter as teammate (Sep 28); OpenAI marketplace launch partner (Sep 29) | [hyper-tau-bench](https://sierra.ai/blog/hyper-t-bench-evaluating-agents-that-build-agents), [AIUC-1](https://sierra.ai/blog/sierra-achieves-aiuc-1-certification), [laid bare](https://sierra.ai/blog/your-agent-laid-bare-and-why-it-matters) | none found | Two SEO guides (Sep 1, Sep 4) and multimodal agents post (Sep 10) not ledgered |
| 2026-10-01..12 | Personal Agent Protocol with Meta (Oct 6); Summit: Curie, Fleming, Tandem Voice, Persona Studio (Oct 6); fleming-1 (Oct 8); Poppy draft and 35 more design partners (Oct 9) | [PAP](https://sierra.ai/blog/introducing-personal-agent-protocol), [Summit](https://sierra.ai/blog/summit-recap-2026), [fleming-1](https://sierra.ai/blog/caller-id-in-the-age-of-agents), [Poppy](https://sierra.ai/blog/poppy) | [SiliconANGLE Oct 6/7](https://siliconangle.com/2026/10/06/meta-teams-up-with-bret-taylors-sierra-technologies-on-new-standards-for-ai-agent-commerce/) | Partner-ecosystem post (Oct 6) not ledgered; PAP GitHub repo created Oct 14 (post-window) |

## 4. Dated event evidence and capabilities

Full row detail is in the [CSV](089-sierra.events.csv) (34 rows, IDs `CI2026-089-001`…`034`). Highlights:

| Event ID | Published UTC / underlying event date | Claim or observed feature | Availability and limitations | Source link (type) | Independent check | E0–E4 working grade |
|---|---|---|---|---|---|---|
| CI2026-089-001 | 2026-04-20 | μ-Bench: 4,270 annotated utterances, 250 calls, 5 locales, 5 ASR providers, new UER metric | Repo public. Code Apache-2.0, **data CC BY-NC 4.0** | [blog](https://sierra.ai/blog/mu-bench-an-open-multilingual-transcription-benchmark) | [repo](https://github.com/sierra-research/mu-bench) | E2 |
| CI2026-089-006/007 | 2026-05-04 / 05-05 | $950M led by Tiger Global and GV. Valuation is "over $15 billion" (vendor) or "$15 billion" (SiliconANGLE) | $15.8B appears only in unread search snippets (E0) | [blog](https://sierra.ai/blog/better-customer-experiences-built-on-sierra) | [SiliconANGLE](https://siliconangle.com/2026/05/04/ai-agent-startup-sierra-valued-15b-new-950m-funding-round/) | E1 |
| CI2026-089-009 | 2026-05-13 | tau-knowledge: best Pass^1 25.5%→37.4%, Pass^4 9.3%→20.6% | Superseded by the 1.0.1 re-grade | [blog](https://sierra.ai/blog/tau-knowledge) | tau2-bench repo | E2 (documentary) |
| CI2026-089-015 | 2026-07-22 | Coding agents "love to cheat" while building the internal MCP gateway. A living design doc improved one-shot success | Anecdotal; no denominator | [blog](https://sierra.ai/blog/building-sierras-mcp-gateway-an-engineering-iceberg) | none | E1 |
| CI2026-089-016 | 2026-07-22 (changelog 07-15) | tau2-bench 1.0.1 corrects banking_knowledge grading: up to ~9 points pass^1 (GPT-5.5 37.37→46.39). Scores are not comparable across versions | GitHub release, MIT | [release](https://github.com/sierra-research/tau2-bench/releases/tag/v1.0.1) | [CHANGELOG](https://github.com/sierra-research/tau2-bench/blob/main/CHANGELOG.md) | E2 |
| CI2026-089-018 | 2026-07-29 | Agency: in-house agent sandboxes (Kubernetes pods on isolated nodepools) chosen over off-the-shelf providers | Internal; not open | [blog](https://sierra.ai/blog/agency-secure-scalable-sandboxes-for-agents) | none | E1 |
| CI2026-089-023 | 2026-08-20 | Release governance: Agent Checks linter, required Simulations, merge approvals with a Reviewer role, split-traffic releases | Plan and date details absent | [blog](https://sierra.ai/blog/release-governance-guardrails-for-agents-at-scale) | none | E1 |
| CI2026-089-025 | 2026-09-08 | hyper-tau-bench: solo developer agent 23.9% vs engineer-paired 82.2% on held-out tasks | MIT repo created 2026-09-04 | [blog](https://sierra.ai/blog/hyper-t-bench-evaluating-agents-that-build-agents) | [repo](https://github.com/sierra-research/hyper-tau-bench) | E2 (documentary) |
| CI2026-089-030/032/034 | 2026-10-06 / 10-07 / 10-09 | Personal Agent Protocol: OAuth sessions, `/.well-known/poppy.json` discovery, draft published, 35 further design partners | Draft. Repo (Apache-2.0) created after the window | [blog](https://sierra.ai/blog/introducing-personal-agent-protocol), [draft](https://sierra.ai/blog/poppy) | [SiliconANGLE](https://siliconangle.com/2026/10/06/meta-teams-up-with-bret-taylors-sierra-technologies-on-new-standards-for-ai-agent-commerce/) | E1 |

**Feature inventory (vendor-documented, not exercised by us):**

| Area | In-window change | Class |
|---|---|---|
| Agent building | Ghostwriter repositioned as proactive Slack/Teams teammate; Persona Studio; Experiments (A/B) | vendor-described / announced |
| Long-horizon agents | Horizon (Jul 16), Context Engine (Aug 4), Takeoff runtime acquisition (Jul 23) | announced; availability unclear |
| Models | Curie (orchestration), Fleming / fleming-1 (agent-caller detection); Tandem Voice architecture | announced (Oct 6–8) |
| Evaluation and governance | Monitors validation loop; Agent Checks; required Simulations; merge approvals; split traffic | vendor-described |
| Security and compliance | FedRAMP High (with Knox Systems); AIUC-1 (Schellman audit); layered supervisors and deterministic guards | vendor-stated certifications |
| Integrations | Plaid Link; SoftBank Japan distribution; OpenAI B2B marketplace; OpenTelemetry/EventBridge/Pub/Sub export | announced |
| Open artefacts | μ-Bench (Apache-2.0 code / CC BY-NC data), tau2-bench 1.0.1 (MIT), hyper-tau-bench (MIT), PAP draft (repo Apache-2.0, post-window) | observed via GitHub API |
| Interoperability | Personal Agent Protocol (OAuth; MCP/OpenAPI routes; `/.well-known/poppy.json`) | draft / announced |

## 5. What the company says it intends to do

| Verbatim or close paraphrase of public direction (<=25 words per source quoted) | Link/date | Promised horizon | Status (planned, tentative, uncommitted) | Missing/contradictory context |
|---|---|---|---|---|
| "plan to publish the v0.1 specification later this month, host design workshops with interested parties, and publish a reference implementation" | [2026-10-06](https://sierra.ai/blog/introducing-personal-agent-protocol) | October 2026 | planned; draft published Oct 9 | Reference implementation not seen in window |
| Possible extensions: finer permissions, push notifications, payments without sharing card details | same | none stated | tentative ("could") | — |
| "more than $1 billion to invest in becoming the global standard" for AI customer experience | [2026-05-04](https://sierra.ai/blog/better-customer-experiences-built-on-sierra) | none | uncommitted | Funding is not adoption |
| Horizon to move agents from support to revenue outcomes over "days, weeks, or months" | [2026-07-16](https://sierra.ai/blog/horizon) | none | announced; availability unspecified | No docs or GA statement found |
| Taylor "expects" OpenAI to back the protocol in future (reported) | [SiliconANGLE 2026-10-06](https://siliconangle.com/2026/10/06/meta-teams-up-with-bret-taylors-sierra-technologies-on-new-standards-for-ai-agent-commerce/) | none | uncommitted | Related party (Taylor chairs OpenAI board); OpenAI is listed among Oct 9 design partners |
| AIUC-1 technical evaluations "recur at least quarterly", with a full audit every year | [2026-09-17](https://sierra.ai/blog/sierra-achieves-aiuc-1-certification) | quarterly / annual | stated commitment | No public results |

These are **company statements**, not forecasts we endorse.

## 6. Independent interpretation: direction and alternative scenarios (researcher's conditional 2027–2031 view)

| Hypothesis for 2027–2031 | Supporting observations | Rival explanations | Disconfirming signals | Confidence/unknowns |
|---|---|---|---|---|
| H1: Vendor-maintained open benchmarks will need versioned, non-comparable score breaks as grading bugs surface | tau2-bench 1.0.1 raised scores up to ~9 points and the vendor says results must not be compared across versions; tau-knowledge leaderboard figures were superseded within ~10 weeks | Normal maturation of a young benchmark; fixes may become rare | Later releases introduce no further grading-scheme breaks through 2028 | moderate for "breaks happen", low for frequency |
| H2: Human context remains the bottleneck for agents that build agents | hyper-tau-bench 23.9% solo vs 82.2% engineer-paired; MCP Gateway post says coding agents "cheat" and need human-curated design docs | Vendor benefits from showing its human agent-development team matters; task design may favour paired condition | Independent replications show solo agents near paired performance on frozen tasks | low–moderate; vendor-run, single benchmark |
| H3: Agent-to-business interaction will move to explicit, declared agent identity (protocol plus detection) rather than covert web automation | PAP with Meta and many design partners; fleming-1 agent-caller detection; SiliconANGLE reports bank calls for standards | Rival protocols may fragment the space; design partners may not ship | No production `/.well-known/poppy.json` deployments from named partners by end-2027 | low; draft only |
| H4: Outcome-based pricing will push vendors to own more of the agent stack (in-house sandboxes, models) rather than reuse | Agency built in-house; proprietary Curie/Fleming models; SiliconANGLE notes possible replacement of models to cut inference cost | Build choices may reflect early-market immaturity, not pricing | Sierra adopts off-the-shelf sandbox/model providers once mature | low; no cost data |

These are hypotheses for testing, not company strategy or fact.

## 7. Implications for the GitHub 1000 study

| M1–M7 construct | Possible observable effect | Study design to test it | Negative/null explanation | Measurement boundary |
|---|---|---|---|---|
| M1 AI coding-agent change | Engineering orgs report coding agents doing most implementation, with humans curating context and verification | Count consented repos with agent-read design docs (e.g. AGENTS.md) and compare accepted-task rates | Docs may not change outcomes | Only consented workflows; vendor statements ("mostly written by AI") are not data |
| M2 accepted task quality | Benchmark grading defects can shift measured success by several points | Re-grade a fixed trajectory set across benchmark versions before comparing | Shifts may be confined to one domain | Pin benchmark version and commit |
| M3 discoverability | Heavy funding and press ($950M round; Summit) | Separate press counts from verified reuse | Press is not reuse | Funding/press never used as an outcome |
| M4 verified third-party reuse | Open benchmarks (tau2-bench) used by third parties (e.g. an HN-posted voice leaderboard claim) | Trace downstream repos that actually execute the benchmark at a pinned version | Mentions without execution | Executed tests only |
| M5 rights/security/provenance | Mixed licensing: MIT benchmarks; mu-bench data CC BY-NC; proprietary platform; certifications vendor-stated | Licence check of code and data separately before reuse | Non-commercial data cannot back commercial reuse regardless of stars | Licence files at a pinned commit |
| M6 review/maintenance and lifecycle cost | Agent release governance mirrors code review (approvals, linters, staged rollout) | Measure reviewer minutes per accepted change with/without required checks | Gates add friction without catching defects | No energy or CO2e inferred from tokens or ARR |
| M7 actionable interventions | Versioned evaluation with explicit score-comparability notes | See §8 | Versioning adds maintenance with no reviewer benefit | Synthetic tasks only until approval |

Company adoption claims ("over 40%", "almost half" or "almost 50%" of the Fortune 50, "billions of customer interactions", customer resolution rates) are **not** independent task outcomes or verified reuse.

## 8. One practical, falsifiable change for the maintainer's own repositories

**Repository/component:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study) offline validators (`scripts/check_research_artifacts.py`, `trending_study.data_integrity`), run on **synthetic, network-free** fixtures only. The disabled Trending `capture` command stays disabled.

**Candidate practice (not yet validated):** Borrow the tau2-bench 1.0.1 pattern. When a validator rule changes, add a **versioned changelog entry stating whether earlier pass/fail results are comparable**, and re-check a frozen fixture set under the old and new rule before merging. Reuse first: use the existing `CHANGELOG`/docs and `unittest` suite. Do not add a new framework.

**Treatment/control and frozen comparable task:** Freeze 10 synthetic validator-rule changes (for example a new allowed status, a stricter date rule or a column rename), each with a **hidden expected-outcome fixture written by a person other than the implementer**. Control: the current practice (change the rule, run unit tests). Treatment: the same change plus a re-check of the frozen fixture set and a mandatory "comparability" changelog note. The unit of acceptance is one rule change that passes hidden fixtures and is accepted by the human reviewer without rework.

**Success and guardrails:** The primary measure is the share of silent comparability breaks caught before merge (a fixture that changes verdict without a changelog note counts as a failure), counted over all 10 tasks, including abandoned ones. Guardrails: full unit suite green, no new dependency, no network access, no real GitHub data, and no change to research protocol without human approval. Measured human work: implementer minutes and reviewer minutes per change. No energy or carbon estimate. Commit authorship stays with the maintainer, and no paid API spend is allowed without approval.

**Stop/reversal rule:** Stop and keep the control if the treatment catches no additional break across the 10 tasks, or adds more than 10 reviewer minutes per change on average. Stop immediately if any treatment step requires network access or real data. **No trial executed; no effect estimated.**

## 9. Findings, uncertainties and review outcome

- **Observed/shipped (documentary):** GitHub-verifiable open artefacts: μ-Bench repo (created 2026-04-14; Apache-2.0 code, CC BY-NC 4.0 data), tau2-bench v1.0.1 release (2026-07-22T21:22Z; changelog 2026-07-15; MIT), hyper-tau-bench repo (MIT; created 2026-09-04). Plus 116 tau2-bench commits in the window (Apr 26, May 23, Jun 6, Jul 29, Aug 14, Sep 16, Oct 1–12: 2). Voice Personas are stated "available today" (vendor).
- **Claims/announcements only:** funding ($950M; over $15B), ARR ($100M in seven quarters, $200M in nine), customer shares, SoftBank LINEMO 97%/93%, Takeoff "nearly 8 figures", Horizon, Context Engine, Curie/Fleming/Tandem Voice/Persona Studio, FedRAMP High and AIUC-1 certifications, export portability, and Personal Agent Protocol design-partner lists. All are unverified vendor statements.
- **Conjectures and unknowns:** H1–H4 in §6; actual task outcomes; certification scope; incident history (status page not retrievable); Takeoff deal completion.
- **Important contradictory or null evidence:** (a) Valuation: "over $15 billion" (vendor) and "$15 billion" (SiliconANGLE) vs $15.8B in unread Axios/CNBC snippets (E0). (b) Customer share is stated as "40% of the Fortune 50" (Apr–Sep posts), "almost half" (Jul 16) and "almost 50%" (Sep 29, Oct 6). Both "nearly half" and $150M ARR come from SiliconANGLE, May 2026. (c) PAP founding partners: Oct 6 lists Genesys, Instinct, Rocket, Shopify, Stripe and Walmart, while Oct 9 adds NiCE. (d) TechCrunch called Fragment Sierra's "third public acquisition" (April). Takeoff followed in July. (e) The tau-knowledge leaderboard figure in May (37.4% best Pass^1) was superseded by the July 1.0.1 re-grade (46.39). (f) tau2-bench 1.0.1 changelog date 2026-07-15 vs release 2026-07-22. (g) No independent in-window criticism, outage report, security advisory or licence change about Sierra was found. That is a search null, not evidence of absence. The only contrary coverage found concerns the agentic-commerce context (bank concerns and Meta Muse privacy reports relayed by SiliconANGLE).
- **#56 candidates (not minted):** SiliconANGLE 2026-05-04 (funding); SiliconANGLE 2026-10-06 (PAP); TechCrunch 2026-04-23 (Fragment; see the robots note in the log). Each needs human reading before a `NEWS-YYYY-NNNN` ID is assigned.
- **Reviewer links and audit date:** none yet. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.
