# Fireworks AI: provisional six-month technology intelligence screen (066)

> **PROVISIONAL, AI-assisted first-pass screen (2026-10-16), not reviewed by a human.** This report, its [event ledger](066-fireworks-ai.events.csv) and its [search log](066-fireworks-ai.search-log.md) are documentary source leads. An AI agent compiled them from public pages. No qualified human has reviewed them. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open. Nothing here is a verified task outcome, an adoption measure, an energy estimate or a scientific finding.

- **Watchlist:** 066. [Issue #134](https://github.com/MSKazemi/github-trending-1000-study/issues/134). Evidence corpus linkage: [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56) (see section 9; no `NEWS-` IDs were minted).
- **Window:** 2026-04-12 to 2026-10-12 inclusive (UTC publication dates). **Screened:** 2026-10-16.
- **Researcher / factual reviewer / review date:** AI-assisted screen / **pending** / **pending**.
- **Status:** screened (provisional). 39 ledger rows (37 distinct events) cover all seven calendar segments. May is sparse.
- **Official sources checked:** [fireworks.ai](https://fireworks.ai/), the full [blog sitemap](https://fireworks.ai/sitemap.xml) (184 posts enumerated), the [docs changelog](https://docs.fireworks.ai/updates/changelog), [security bulletins](https://fireworks.ai/security/bulletins), the [status page](https://status.fireworks.ai/), GitHub [`fw-ai`](https://github.com/fw-ai) and [`fw-ai-external`](https://github.com/fw-ai-external), and [PyPI `fireworks-ai`](https://pypi.org/project/fireworks-ai/).
- **Grades:** these are the company-watch working tiers E0–E4 from the [method](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md). They are not the separate [lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md). No row exceeds **E2**.
- **Coverage limitation:** the shared web-search budget ran out after 8 queries, so two planned April–May and Bloomberg queries were **not run** (see [search log](066-fireworks-ai.search-log.md) §C). Independent press coverage is therefore thin by construction, not shown to be absent.

## 1. Search and inclusion audit

| Search run UTC | Site/engine | Query / surface | Found | Screened | Included | Excluded/why | Coverage limitation |
|---|---|---|---:|---:|---:|---|---|
| 2026-10-16 | fireworks.ai sitemap + per-post JSON-LD | all `/blog/` URLs | 184 | 184 | 21 rows | 27 of 48 in-window posts not itemized (SEO roundups, overlapping launches, customer stories); 14 undated | Live pages; many `dateModified` 2026-09-23 |
| 2026-10-16 | docs changelog (raw HTML) | dated headings | 28 in-window headings | 28 | 13 rows | Training-model catalogue additions folded into context | No entries between Feb 5 and May 14 |
| 2026-10-16 | GitHub API / PyPI JSON | python-sdk, fireconnect, minimax-kernels | 53 + 13 releases | all | 2 rows (+4 check links) | Routine patch releases | Release count is not adoption |
| 2026-10-16 | security bulletins, status page | index + payload | 1 bulletin; 104 in-window incident IDs | all | 2 rows | Other status incidents aggregated | Status history starts 2026-07-17 |
| 2026-10-16 | WebSearch (8 queries, Q1–Q8) | see search log | unknown | ~20 opened or seen | 1 independent row + 5 check links | Aggregators, unrelated, E0 snippets | Budget exhausted; Q9–Q10 not run |

## 2. Verified company/product identity and baseline

- **Entity.** The site's JSON-LD names the legal entity **Fireworks AI, Inc.** ([fireworks.ai](https://fireworks.ai/)). The investor press release datelines it in San Mateo, California ([OTPP, 2026-07-16](https://otpp.com/en-ca/about-us/news-and-insights/2026/fireworks-raises-a-1-5-billion-series-d-to-lead-the-specialized-intelligence-revolution/)). Lin Qiao is co-founder and CEO (same source).
- **Brand.** In-window materials increasingly use "**Fireworks**, the platform for specialized intelligence" in place of "Fireworks AI". This is a positioning change, not a legal rename; no rename filing was checked. The GitHub orgs are `fw-ai` and `fw-ai-external`.
- **Ownership.** The company is independent and venture-backed. The 2026-07 Series D was led by Atreides Management, Index Ventures and TCV, with NVIDIA among the participants ([Fireworks](https://fireworks.ai/blog/series-d-announcement), [Orrick](https://orrick.com/en/News/2026/07/Fireworks-AI-Closes-Over-1-5-Billion-in-Series-D-Funding)). No parent company or acquisition **of** Fireworks was found. Cap-table and control details were not checked at filing level.
- **Acquired brand (pre-window baseline).** Fireworks acquired **Hathora**, a compute-orchestration company, as a "talent-and-infrastructure acquisition" ([SiliconANGLE, 2026-03-09](https://siliconangle.com/2026/03/09/fireworks-ai-bets-hathora-acquisition-power-next-phase-real-time-ai/)). This predates the window.
- **Offering.** Serverless and dedicated ("on-demand") inference for mostly open-weight third-party models. Also: training (SFT/DPO/RL via Managed Training, the Training API and the Fireworks Lab service), the Nexus coding-agent gateway with FireRouter and FireConnect, and, since 2026-09-23, its own model, Ember-1.
- **Openness.** The platform itself is **proprietary**. Public Apache-2.0 code includes the [Python SDK](https://github.com/fw-ai-external/python-sdk), the [FireConnect CLI](https://github.com/fw-ai/fireconnect) and the [MiniMax kernels](https://github.com/fw-ai/minimax-kernels). Hosted model weights carry their own upstream licences, which were not audited here.

## 3. Month-by-month discoveries

| Month | Announcements/changes | Primary URLs | Independent reporting | Notes or no-result limitations |
|---|---|---|---|---|
| 2026-04-12..30 | Control-token injection fix (04-24); DeepSeek V4 Pro launched after a reported cross-provider serving defect (04-27); SDK 1.1.0-alpha.64 (04-28) | [blog](https://fireworks.ai/blog/safe-tokenization-preventing-prompt-injection-on-fireworks), [blog](https://fireworks.ai/blog/deepseek-v4-pro-validating-frontier-models-for-production), [release](https://github.com/fw-ai-external/python-sdk/releases/tag/v1.1.0-alpha.64) | None found | No changelog entries; Q10 not run |
| 2026-05 | Eight legacy serverless models removed (05-14); Notte co-authored "Agent Execution Tax" study (05-20) | [changelog](https://docs.fireworks.ai/updates/changelog), [blog](https://fireworks.ai/blog/agent-execution-tax) | None found; Bloomberg "talks at ~$15B" seen only as E0 snippet | **Sparse**; SDK alphas only otherwise |
| 2026-06 | Harvey harness study (06-03); Nemotron 3 Ultra day-0 (06-04); audio/image generation deprecated (06-10); Kimi K2.7 Code, MiniMax M3, Qwen 3.7 Plus (06-12); prepaid billing notice (06-15); GLM 5.2 RL training service (06-24); Cursor Composer 2 story (06-26); FireConnect repo first release (06-21) | rows 006–012; FireConnect via [GitHub releases](https://github.com/fw-ai/fireconnect/releases) | None found | Many vendor customer stories |
| 2026-07 | MiniMax M3 Blackwell kernel, later open-sourced (07-10); SDK 1.2.0 stable (07-11); Series D (07-15/16); Nexus + FireConnect 0.9.0 (07-26); Kimi K3 day-0 (07-27) | rows 013–018 | [SiliconANGLE 07-16](https://siliconangle.com/2026/07/16/ai-infrastructure-startup-fireworks-closes-1-5b-round-17-5b-valuation/) | Status page starts recording 07-17 |
| 2026-08 | Voyage AI models (08-05); Meta Muse Glimmer (08-10); status incidents (61 records); SSO doc correction (08-25); DeepSeek V4 Pro 0813 cost study (08-26); same-day serverless deprecations (08-27); Training API + Lab GA (08-31) | rows 019–025 | [Unite.AI 08-31](https://www.unite.ai/fireworks-ai-makes-training-api-generally-available/) | Harvey-figure conflict (section 4) |
| 2026-09 | Rate-limit tiers (09-01); annotation API breaking change (09-08); training skill for coding agents (09-09); 13-day deprecation notice (09-12) taking effect (09-26); deployment-shape flags (09-16); router oracle analysis (09-21); Specialized Intelligence Index (09-22); Ember-1 (09-23); FireRouter with Opus and multi-region (09-28) | rows 026–035 | None found | Densest month |
| 2026-10-01..12 | Managed RFT paused, 70 models no longer tunable (10-01); DeepSeek V4.1 Flash serverless price rise (10-01); Small-tier rate limits doubled (10-02/10-07); **security incident** (identified 10-06, bulletin 10-10 UTC) | rows 036–039 | Only an aggregator ([Digg](https://digg.com/ai/5nyqpw74)) | No blog post dated Oct 1–12 |

## 4. Dated event evidence and capabilities

Full rows are in the [CSV](066-fireworks-ai.events.csv). The material items:

| Event ID | Published UTC / event date | Claim or observed feature | Availability and limitations | Source link (type) | Independent check | Grade |
|---|---|---|---|---|---|---|
| CI2026-066-002 | 2026-04-27 | Fireworks says early DeepSeek V4 deployments showed reasoning-trace corruption, which it reproduced "across multiple DeepSeek-enabled providers". It delayed its own launch and escalated to SGLang, vLLM and DeepSeek | Live 04-27. Affected providers not named | [blog](https://fireworks.ai/blog/deepseek-v4-pro-validating-frontier-models-for-production) (first-party) | none | E1 |
| CI2026-066-014 | 2026-07-11 | Python SDK 1.2.0 is the first stable release after 29 in-window alpha tags; 24 stable 1.2.x releases follow through 10-12. GitHub marks five alpha tags as non-prereleases | Apache-2.0. The 1.2.0 notes contain only a compare link | [release](https://github.com/fw-ai-external/python-sdk/releases/tag/v1.2.0) (OSS) | [PyPI](https://pypi.org/project/fireworks-ai/1.2.0/) timestamps match | E2 |
| CI2026-066-015/016 | 2026-07-15 (blog) / 2026-07-16 (press) | $1.505B Series D at $17.5B valuation; the company claims >$1B annualized run rate and >40T tokens/day | **Date conflict:** blog `datePublished` 07-15 vs press-release dateline 07-16 | [blog](https://fireworks.ai/blog/series-d-announcement); [SiliconANGLE](https://siliconangle.com/2026/07/16/ai-infrastructure-startup-fireworks-closes-1-5b-round-17-5b-valuation/) | Orrick confirms "$17.5 billion post-money" | E1 |
| CI2026-066-017 | 2026-07-26 | **Nexus**: routes existing coding tools (Claude Code, Codex, Cursor and others) to managed open models with budgets and routing. FireConnect CLI v0.9.0 ships the same day | Installs via `curl … \| sh`. Cost savings are vendor-claimed | [blog](https://fireworks.ai/blog/fireworks-nexus) | [v0.9.0](https://github.com/fw-ai/fireconnect/releases/tag/v0.9.0) | E2 |
| CI2026-066-021 | 2026-08-18 | Resolved "Kimi K3 service disruption". The status payload lists 104 resolved incident records Jul 17–Oct 12, mostly per-model "Service Degradation" | Titles only. History before Jul 17 not exposed | [incident](https://statuspage.incident.io/fireworks-dashboard/incidents/cc4cy2g4) | [status](https://status.fireworks.ai/) | E2 |
| CI2026-066-024 | 2026-08-27 | Same-day serverless deprecations (MiniMax M2.7, GPT OSS 20B, Kimi variants, DeepSeek V4 Pro) | **Internal conflict:** the entry recommends Qwen3 8B as a GPT OSS 20B replacement, but the May 14 entry had already removed Qwen3 8B from serverless | [changelog](https://docs.fireworks.ai/updates/changelog) | none | E2 |
| CI2026-066-025 | 2026-08-31 | Training API (your own Python loop; Fireworks runs the trainer and rollout) and Fireworks Lab are GA | **Figure conflict:** the current page gives Harvey Tenet 19.7% vs **10.8% base Kimi K3**. Unite.AI the same day reported 19.7% vs **11.5% Claude Fable 5**. The page's `dateModified` is 2026-09-23, so an edit is possible but unproven | [blog](https://fireworks.ai/blog/train-past-the-frontier-training-api-now-generally-available) | [Unite.AI](https://www.unite.ai/fireworks-ai-makes-training-api-generally-available/) | E2 |
| CI2026-066-026 | 2026-09-08 | Bare annotation keys now return **HTTP 403**; reads return only `custom/*` keys | Breaking change; no deprecation window stated | [changelog](https://docs.fireworks.ai/updates/changelog) | none | E2 |
| CI2026-066-027 | 2026-09-09 | Training "skill" for Claude Code, Cursor, Codex and others: plans a run, estimates cost, "wait[s] for approval before spend" | Approval gate not tested | [changelog](https://docs.fireworks.ai/updates/changelog) | none | E2 |
| CI2026-066-028/033 | 2026-09-12 → 2026-09-26 | 13-day notice, then removal from serverless of DeepSeek V4 Pro (0813), DeepSeek V4 Flash (0731), GLM 5.2, Muse Glimmer 30B, Kimi K2.6 and Kimi K2.7 Code | Dedicated deployments unaffected | [changelog](https://docs.fireworks.ai/updates/changelog) | none | E2 |
| CI2026-066-030 | 2026-09-21 | Hindsight oracle over 18 models on 113 DeepSWE tasks: 97.6% at $1.88/task vs best single model 74.1% at $6.52 | The post itself says the oracle is biased upward | [blog](https://fireworks.ai/blog/the-frontier-isnt-a-model-its-a-router) | none | E1 |
| CI2026-066-034 | 2026-09-28 | FireRouter with Opus routes per turn among Claude Opus 5.5, GLM 5.3 and GLM 5.3 Flash. Internal randomized sessions: cost/session −57% (±19 pp), $15.36→$6.63; graded-turn accuracy 78.7% vs 80.2% | Internal Fireworks traffic only. Sample size not stated in extracted text | [blog](https://fireworks.ai/blog/introducing-firerouter-with-opus) | [docs](https://docs.fireworks.ai/fireworks-nexus/overview) | E1 |
| CI2026-066-036 | 2026-10-01 | **Managed RFT paused.** No new jobs; the 70 models tunable only via managed RFT (count verified from the list) can no longer be fine-tuned. Trained models keep serving | One month after the GA post promoted Managed Training methods including RFT | [changelog](https://docs.fireworks.ai/updates/changelog) | none | E2 |
| CI2026-066-037 | 2026-10-01 | DeepSeek V4.1 Flash serverless standard price: uncached input $0.22→$0.30, output $0.66→$1.20 per 1M tokens | This model had been the recommended migration target on Sep 12 | [changelog](https://docs.fireworks.ai/updates/changelog) | none | E2 |
| CI2026-066-039 | 2026-10-10 (event 2026-10-06) | Unauthorized use of internal Fireworks credentials. A third party accessed **environment variables used in evaluation jobs** (including stored API keys and tokens) in "a limited number of customer accounts". Timeline (PDT): identified Oct 6 9am, notifications from Oct 7, employee keys rotated Oct 9, bulletin published Oct 9 10pm, further revocations Oct 10 | Vendor states no evidence of access to models, datasets, inference traffic or personal data. Investigation ongoing; affected-account count not disclosed | [bulletin](https://fireworks.ai/security/bulletins/october-2026-security-incident) | CEO posts via [Digg](https://digg.com/ai/5nyqpw74) (aggregator, not independent) | E2 |

**Feature inventory (vendor assertion vs observed).**

| Area | Vendor assertion (E1) | Observed in a reproducible artifact (E2) | Independently verified (E3+) |
|---|---|---|---|
| Inference catalogue | Day-0 launches (Nemotron 3 Ultra, Kimi K3, MiniMax M3, Muse Glimmer, Voyage) | Changelog listings and deprecations; status incidents | None |
| Coding-agent integration | Nexus, FireRouter quality/cost | FireConnect repo and releases; training skill entry; Nexus docs | None |
| Training | Zero-KLD train/serve alignment; Training API GA | SDK `training-sdk` release notes (e.g., [1.2.20](https://github.com/fw-ai-external/python-sdk/releases/tag/v1.2.20)); RFT pause entry | None |
| Security | Tokenization injection fix "for all models" | Oct 2026 bulletin; SSO doc correction | None |
| Benchmarks | SII, router oracle, DeepSeek/Fable cost studies, Ember-1 token savings | None (vendor-run) | None. Artificial Analysis provider pages exist but were E0 snippets only |
| Licensing | Muse Glimmer "Apache 2.0" weights (vendor statement) | SDK, FireConnect and kernels are Apache-2.0 on GitHub | Upstream model licences not audited |

**Other internal inconsistencies recorded.** Ember-1's on-page heading says "half the tokens", but its description says "40% fewer tokens" ([blog](https://fireworks.ai/blog/ember-1)). The Sep 26 changelog entry reports a Sep 25 effective date.

## 5. What the company says it intends to do

| Public direction (≤25 words quoted) | Link/date | Promised horizon | Status | Missing/contradictory context |
|---|---|---|---|---|
| Funding will "expand our compute infrastructure, grow our engineering team, and continue building the platform" | [Series D, 2026-07-15](https://fireworks.ai/blog/series-d-announcement) | unspecified | planned | No measurable targets |
| Shapeless deployment creation "will then require the explicit opt-in"; "Enforcement is coming soon" | [changelog, 2026-09-16](https://docs.fireworks.ai/updates/changelog) | "soon" | announced, undated | |
| DeepSeek V4.1 Flash training: "RL support is coming soon" | [changelog, 2026-09-28](https://docs.fireworks.ai/updates/changelog) | "soon" | announced | Three days later managed RFT was paused (RL remains possible via the Training API) |
| FireRouter "model set will change as new models and versions launch" | [blog, 2026-09-28](https://fireworks.ai/blog/introducing-firerouter-with-opus) | ongoing | tentative | Router results change whenever the set changes |
| Ember-1 "kicks off an ongoing series of specialized models by Fireworks" | [blog, 2026-09-23](https://fireworks.ai/blog/ember-1) | unspecified | planned | Fireworks as a model publisher as well as a host |
| SII: "More are coming soon" (domains) | [blog, 2026-09-22](https://fireworks.ai/blog/introducing-the-specialized-intelligence-index) | "soon" | planned | Vendor-operated benchmark |
| "[r]eviewing how secrets are made available to evaluation jobs. We will share additional remediation measures" | [bulletin, 2026-10-10](https://fireworks.ai/security/bulletins/october-2026-security-incident) | unspecified | committed to disclose | No date or scope |
| Forge conference, "November 3, 2026", Pier 27 San Francisco | [forge page](https://fireworks.ai/forge) (undated page, fetched 2026-10-16) | 2026-11-03 | announced (outside window) | Event content unknown |

These are company statements, not forecasts by this study.

## 6. Independent interpretation: direction and alternative scenarios (researcher's conditional hypotheses, 2027–2031)

| Hypothesis | Supporting observations | Rival explanations | Disconfirming signals | Confidence/unknowns |
|---|---|---|---|---|
| H1. Inference hosts will push "route open models for routine turns, closed models for hard ones" into coding agents as a default cost layer | Nexus, FireRouter, the oracle analysis and FireConnect harness support (rows 017, 030, 034) | Plain cost marketing that coincides with open-model price drops; closed-model vendors may cut prices instead | Independent harnesses show routed agents with lower **accepted** task rates at equal cost, or users abandoning routers after model churn | Low. Only vendor-internal evidence (E1) |
| H2. Rapid model churn on serverless shifts maintenance cost onto agent integrators | Nine changelog deprecation entries May 14–Sep 26, one (Muse Glimmer) 46 days after its launch post; a price rise on a recommended replacement (rows 004, 008, 024, 028, 033, 037) | Normal catalogue hygiene. Dedicated deployments are unaffected, so serious users may pin | Published deprecation policies with ≥90-day notice become standard; integrators report negligible migration effort | Medium on the facts (E2 changelog). Unknown on actual integrator cost |
| H3. Evaluation and training infrastructure becomes a primary credential-exposure surface for agent platforms | Oct 2026 incident centred on eval-job environment variables (row 039) | Isolated operational failure; root cause unpublished | Root-cause report shows an unrelated vector; no similar incidents at peers by 2027 | Low. One vendor-reported event, investigation ongoing |
| H4. Hosts become model publishers and benchmark operators, raising conflict-of-interest risk for "independent" evals | Ember-1, SII, multiple vendor-run cost/accuracy comparisons | Transparency may be sincere; SII cites external critiques (METR) | Third-party replication matches vendor numbers; SII governance opens to outside review | Low–medium |

None of these is company strategy. Each needs a dated, independent signal to move beyond conjecture.

## 7. Implications for the GitHub 1000 study

| Construct | Possible observable effect | Study design to test it | Negative/null explanation | Measurement boundary |
|---|---|---|---|---|
| **M1** coding workflow change | Agent harnesses (Claude Code, Codex, Cursor) pointed at non-default models via gateways | Opt-in, consented tool-use records with gateway/model metadata | Gateways may route few real turns; availability is not adoption | Vendor claims are not usage |
| **M2** accepted quality and review cost | Router/open-model substitution may keep "accuracy" while raising reviewer rework | Frozen tasks with hidden independent acceptance tests; count refused and failed tasks | Vendor "accuracy" (graded turns) is not maintainer acceptance; SII itself cites a 24.2 pp benchmark-vs-maintainer gap ([METR via Fireworks](https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/)) | No acceptance data observed here |
| **M3** discovery | Answer-engine marketing (prefilled "ask ChatGPT/Claude" links; docs `llms.txt`) | Compare answer-engine citation of repos with and without such surfaces | Brand spend confounds | Not measured |
| **M4** verified reuse | SDK, FireConnect and kernel repos are reusable Apache-2.0 artifacts | Trace consented downstream integrations, not stars or release counts | 53 SDK releases show churn, not use | Downstream use unknown |
| **M5** reuse vs generate; rights/security | Hosted model licences vary; `curl \| sh` install path; eval-job secrets exposure | Pre-adoption licence and secret-handling checklist per provider | Risks may be manageable with dedicated deployments | Model licences not audited |
| **M6** lifecycle human and energy cost | Deprecations, a price rise, the RFT pause and an API 403 change impose migration work | Log migration minutes per forced change across a fixed integration | Effort may be trivial for OpenAI-compatible clients | **No energy or CO2e figures exist in sources; none inferred from tokens** |
| **M7** maintainer interventions | Model-agnostic configuration and lifecycle checks as a maintainer practice | Section 8 pilot | May add overhead without benefit | Not run |

## 8. One practical, falsifiable change for the maintainer's own repositories

**Repository/component.** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study): agent-assisted maintenance of the offline `trending_study` CLI and tests. Live Trending `capture` stays **disabled**, and no Fireworks feature changes that.

**Candidate practice (not yet validated).** A *model-lifecycle and secret-free evaluation guard*. Agent model choice lives in one configuration file, and the evaluation environment carries **no credentials**. Agent-produced patches are accepted only through hidden, human-authored acceptance tests. The motivating evidence is rows 024/028/033/036/037 (model churn, price change) and row 039 (secrets in evaluation jobs).

**Treatment/control and frozen task.**
- *Control (A):* the maintainer's current default single-model agent workflow, on the existing subscription (no new paid API).
- *Treatment (B):* the same harness and prompts, routed to one pinned open-weight model through an OpenAI-compatible endpoint. This could be Fireworks serverless or a dedicated deployment, or a reused existing gateway (e.g., LiteLLM) if it passes the same tests.
- *Tasks:* freeze 12 bounded maintenance tasks drawn from the existing backlog before the trial. Include 2 tasks with no valid solution. A human who has no contact with the agent context writes hidden acceptance tests for each.
- *Unit:* one **independently accepted task**, meaning the hidden tests pass and a human reviewer would merge it. The denominator is all 12 assigned tasks, counting refused, failed, timed-out and abandoned tasks.
- *Spend:* B is run **only after the maintainer explicitly approves the spend**, with a fixed cap. Per the owner's rules, paid model APIs are never added to project scripts or CI.

**Success and guardrails.**
- *Primary:* accepted tasks / 12 for A vs B. The pilot is falsified as "no worse" if B accepts ≥2 fewer tasks than A.
- *Secondary:* reviewer minutes per accepted task (stopwatch log), rework rounds, metered provider charges from the invoice, CI minutes, and migration minutes if the pinned model is deprecated mid-trial (recorded as a lifecycle failure, never silently swapped).
- *Guardrails:*
  - zero secrets in the agent or evaluation environment, checked with an env-dump assertion before each run;
  - full offline unit suite and `value_gate`/`reuse_gate` smoke tests green;
  - no new dependency without licence and maintenance review;
  - commits authored solely by the maintainer, with no AI contributor attribution;
  - energy reported only if actually metered (no token-to-energy or CO2e conversion).

**Stop/reversal rule.** Stop B and keep A on any of these:
- any secret appears in the agent or evaluation environment;
- the spend cap is reached;
- the provider's licence or retention terms for the chosen model cannot be confirmed;
- the pinned model is deprecated during the trial;
- B is ≥2 accepted tasks worse.

With 12 tasks this is a **feasibility pilot**. It cannot show non-inferiority, and a null or negative result is preserved. **No trial has been executed.**

## 9. Findings, uncertainties and review outcome

- **Observed/shipped (E2 documentary):**
  - Python SDK stable 1.2.x (Jul 11 onward);
  - FireConnect and MiniMax kernel repositories (Apache-2.0);
  - nine changelog deprecation entries (May 14–Sep 26), including 13-day and same-day notices;
  - Managed RFT paused with 70 models no longer tunable (Oct 1);
  - a DeepSeek V4.1 Flash price rise;
  - a breaking annotation-API change;
  - SSO doc correction;
  - 104 resolved status incidents (Jul 17–Oct 12);
  - an Oct 6–10 credential incident affecting evaluation-job secrets.
- **Claims/announcements only (E1):** routing quality and cost gains (FireRouter, oracle), customer outcomes (Harvey, Cursor, Factory), the zero-KLD RL alignment, the Ember-1 token savings, the tokenization injection fix, the $1B+ run rate and 40T tokens/day, and Nexus cost savings.
- **Conjectures and unknowns:** whether routed or open-model agents keep *maintainer-accepted* quality; the root cause and scope of the October incident; actual integrator migration costs; adoption by real developers; and energy, which is unknown and not estimable from sources.
- **Contradictory or null evidence:**
  - Series D date: 07-15 on the blog vs 07-16 in the press release.
  - Harvey comparator: 10.8% base Kimi K3 on the current page vs 11.5% Claude Fable 5 per Unite.AI.
  - The Qwen3 8B migration advice conflicts with its earlier removal.
  - Ember-1 says "half" vs "40% fewer" tokens.
  - Managed RFT was paused one month after a GA post promoting it.
  - The status page shows sustained per-model degradations, against the "reliable" marketing.
  - No independent critical journalism was found, but the search budget limited this.
- **#56 linkage:** the candidate nonduplicate evidence items for [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56) are CI2026-066-016 (SiliconANGLE, independent press), CI2026-066-039 (first-party incident bulletin) and CI2026-066-036 (RFT pause). They should be minted as `NEWS-` items only after human verification.
- **Reviewer links and audit date:** none yet. Pending human factual/link spot-check (start with rows 015/016, 025, 036, 039), rights review and methods review. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.
