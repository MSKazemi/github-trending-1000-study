# Groq — provisional six-month technology intelligence screen (064)

> **PROVISIONAL, AI-assisted first-pass screen (2026-10-16); not reviewed by a qualified human.** This report, its [event ledger](064-groq.events.csv) and [search log](064-groq.search-log.md) are documentary source leads only. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open. Nothing here is a validated task outcome, an adoption measurement or an endorsement.

- **Company watchlist ID:** 064 — [issue #132](https://github.com/MSKazemi/github-trending-1000-study/issues/132); news-corpus linkage: [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56).
- **Window:** 2026-04-12 through 2026-10-12 inclusive (UTC dates); sources accessed 2026-10-16.
- **Researcher / factual reviewer / review date:** AI-assisted first pass / **pending** / **pending**.
- **Status:** screened (provisional). 27 dated ledger rows covering all seven calendar segments; no row is an independent behavioural test (no E3/E4).
- **Official sources checked:** [groq.com](https://groq.com/) (blog/newsroom, sitemap), [GroqCloud changelog](https://console.groq.com/docs/changelog), [deprecations](https://console.groq.com/docs/deprecations) (also its [.md form](https://console.groq.com/docs/deprecations.md)), [Compound changelog](https://console.groq.com/docs/changelog/compound), [Supported Models](https://console.groq.com/docs/models), [status page](https://groqstatus.com/) and its RSS feed, GitHub [groq/groq-python](https://github.com/groq/groq-python), [groq/groq-typescript](https://github.com/groq/groq-typescript), [groq/groq-changelog](https://github.com/groq/groq-changelog), [groq/openbench](https://github.com/groq/openbench) and the `groq` org repository list (via `gh api`).
- **Grading:** company-watch E0–E4 from the [method](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md), not the separate [lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md). Ledger labels `E1_INDEPENDENT_*` mean "dated, attributable third-party report": they support *what was reported*, not validated behaviour, and are no stronger than E1/E2 in the method's sense.
- **Verification rule used:** every number, version, date, price and quote in this report and the ledger was checked against raw page text (`curl` + text extraction) or the GitHub API; items that could only be seen in search-engine summaries are excluded or flagged (see the [search log](064-groq.search-log.md)).

## 1. Search and inclusion audit

Summary only; exact queries, opened URLs, exclusions and inaccessible sources are in the [search log](064-groq.search-log.md).

| Search run (date) | Site/engine | Query focus | Found | Screened | Included | Excluded/why | Coverage limitation |
|---|---|---|---:|---:|---:|---:|---|
| 2026-10-16 | groq.com, console.groq.com, groqstatus.com (direct fetch) | newsroom/blog, changelog, deprecations, models, status | n/a | ~25 pages | 14 rows | pre-window posts (baseline), Oct 15 post (after window) | groq.com sitemap is stale (omits Aug 2026 posts); status RSS exposes only Oct 9–12 items |
| 2026-10-16 | GitHub API | releases/commits in groq org | 28 repos with pushes since 2026-04-12 (as of 2026-10-16) | 7 repos | 7 rows | Terraform/workflow automation commits | commit counts are activity, not quality |
| 2026-10-16 | Web search (provider-interpreted) | funding, leadership, antitrust, LPX, deprecation fallout, month segments | not recorded | ~30 result pages | 6 rows | aggregators, LLM-flagged Wikipedia, 2025 items | session web-search budget ran out before the final two planned queries; result counts unavailable |

## 2. Verified company/product identity and baseline

**Entity as of 2026-10-12 (partly verified).** Groq (founded 2016; LPU inference chip and the GroqCloud API) **was not acquired**, but its ownership and corporate form changed around the window:

- **Baseline (pre-window, context only):** on 2025-12-24 Groq [announced](https://groq.com/newsroom/groq-and-nvidia-enter-non-exclusive-inference-technology-licensing-agreement-to-accelerate-ai-inference-at-global-scale) a non-exclusive licence of its inference technology to Nvidia. Founder Jonathan Ross, President Sunny Madra and other staff joined Nvidia. Simon Edwards became CEO, and Groq said "GroqCloud will continue to operate without interruption". On 2026-02-16 Groq [reported](https://groq.com/blog/groqcloud-expanding-to-meet-demand) more than 3.5 million developers and a UK data centre built with Equinix. The 2026-03 Senate letter about the deal (Warren/Blumenthal) is also baseline; the senate.gov page returned HTTP 403 and was not read.
- **In-window restructuring evidence:**
  - Reuters ([CI2026-064-005](064-groq.events.csv)) cited one unnamed source. It said investors had been paid out and were being asked to fund "Groq 2.0", and that shareholders could invest in "a new company".
  - The public OSS licences changed their copyright holder from "Groq, Inc." to **"Groq LLC"** on 2026-06-26 (CI2026-064-011).
  - The August raise was announced by **"Groq LLC"** as a **"Series A"** (CI2026-064-016).

  Together these fit a re-formed operating entity. The legal relationship between Groq, Inc. and Groq LLC (successor, conversion or subsidiary) was **not verified** against filings.
- **Leadership (conflicting sources).** Groq's own releases name **Adam Winter as CEO**: the [2026-06-22 release](https://groq.com/newsroom/groq-raises-usd650m-to-scale-its-ai-inference-cloud-business) and the 2026-08-12 NCP release, which quotes "Adam Winter, CEO of Groq". The 2026-06-22 release also names Alex Davis (Disruptive) as chair, CFO Matt Eng and COO Alan Rice, plus CTO Sinclair Schuller and CPO Rakesh Malhotra from July. [TechCrunch 2026-05-29](https://techcrunch.com/2026/05/29/after-nvidias-20b-not-acqui-hire-ai-chip-startup-groq-reportedly-raising-650m/) called Winter *interim* CEO. [TNW 2026-08-17](https://thenextweb.com/news/groq-3-5bn-valuation-funding-round) says co-founder Doug Wightman "stepped up as chief executive", which **contradicts** the first-party sources. The date Winter succeeded Edwards is **unknown**.
- **Deal value conflict:** Reuters reports **$17 billion** (May 28, Sep 9). TechCrunch, TNW and others report about **$20 billion**. Neither company disclosed terms in the pages read.
- **Nvidia relationship:** Groq became an NVIDIA Cloud Partner (2026-08-12), and Nvidia had "planned participation" in the Series A (2026-08-17). Nvidia sells the licensed technology as "NVIDIA Groq 3 LPX" (announced at GTC 2026 per Groq's June release; that event itself is baseline). The Groq brand now names both a cloud operator and an Nvidia product line, so do not conflate them.
- **Offering as of 2026-10-16 (observed):** GroqCloud, an OpenAI-compatible inference API for open-weight models. The [Supported Models](https://console.groq.com/docs/models) page lists, for example:
  - gpt-oss-120b at $0.15 input / $0.60 output per 1M tokens;
  - Qwen 3.8 27B (Preview) at $0.80 / $4.00 per 1M tokens;
  - Enterprise-only Llama 3.1 8B / 3.3 70B, MiniMax M2.7 and Muse Spark Open.

  `groq.com/pricing` now redirects to the homepage. These prices are a 2026-10-16 snapshot, not window history.
- **Licences:** groq-python and groq-typescript are Apache-2.0 ("Copyright 2026 Groq"). openbench, groq-desktop-beta and groq-mcp-server are MIT. The hosted service is proprietary.

## 3. Month-by-month discoveries

| Month | Announcements/changes (ledger IDs) | Primary URLs | Independent reporting | Notes or no-result limitations |
|---|---|---|---|---|
| 2026-04-12..30 | Kimi K2 0905 shutdown (001); Enterprise-only MiniMax M2.5 / Qwen3-VL 32B and SDK notes (002); groq-python v1.2.0 (003) | [deprecations](https://console.groq.com/docs/deprecations), [changelog](https://console.groq.com/docs/changelog), [v1.2.0](https://github.com/groq/groq-python/releases/tag/v1.2.0) | none found | The Apr 18 changelog entry was committed publicly on 2026-05-06. It is the **last** changelog entry as of 2026-10-16. |
| 2026-05 | SDK env-headers and api-key log redaction (004); $650M raise and "Groq 2.0" reported (005); interim CEO/CFO reported (006) | [TS v1.2.0](https://github.com/groq/groq-typescript/releases/tag/v1.2.0) | [Reuters/Yahoo](https://finance.yahoo.com/sectors/technology/articles/groq-targets-650-million-fundraise-150216663.html), [TechCrunch](https://techcrunch.com/2026/05/29/after-nvidias-20b-not-acqui-hire-ai-chip-startup-groq-reportedly-raising-650m/) | No first-party newsroom post found for May. |
| 2026-06 | Compound `browser_automation` retired (007); four model deprecations emailed (008); Qwen3.6 27B in SDK (009); $650M + leadership (010); "Groq LLC" copyright (011) | [Compound changelog](https://console.groq.com/docs/changelog/compound), [$650M](https://groq.com/newsroom/groq-raises-usd650m-to-scale-its-ai-inference-cloud-business), [openbench commit](https://github.com/groq/openbench/commit/3f190a835f7fee34ccd96e17242a36a29e0620a6) | Reuters (May) pre-reported the round | — |
| 2026-07 | Qwen3 32B / Llama 4 Scout shutdown (012); SDK release engineering and CODEOWNERS changes (013) | [deprecations](https://console.groq.com/docs/deprecations), [TS v1.4.0](https://github.com/groq/groq-typescript/releases/tag/v1.4.0) | none found | No first-party blog/newsroom post found for July. |
| 2026-08 | NCP (014); Llama 3.1 8B / 3.3 70B self-serve shutdown (015); $350M Series A at $3.5B (016); LPX adoption plan (019); Compound deprecation announced, no replacement (021); Qwen 3.8 27B in SDKs (022) | [NCP](https://groq.com/newsroom/groq-becomes-an-nvidia-cloud-partner), [Series A](https://groq.com/newsroom/groq-closes-usd350-million-series-a-building-the-world-s-leading-ai-inference-cloud), [LPX blog](https://groq.com/blog/groq-among-the-first-to-bring-nvidia-groq-3-lpx-and-vera-rubin-nvl72-to-market), [v1.7.0](https://github.com/groq/groq-python/releases/tag/v1.7.0) | [TNW](https://thenextweb.com/news/groq-3-5bn-valuation-funding-round) (017), [Bloomberg Government](https://news.bgov.com/private-equity/groq-valued-at-3-5-billion-in-funding-round-after-nvidia-deal), [HF forum migration post](https://discuss.huggingface.co/t/looking-for-an-open-source-llm-to-replace-llama-3-3-70b-versatile/178871) (018), [StorageReview](https://www.storagereview.com/news/nvidia-groq-3-lpx-enters-full-production-3400-tokens-per-second-at-100k-context-256-lp30s-per-rack) (020) | The busiest month. |
| 2026-09 | Unreleased "white-label" OpenAI-compatibility SDK commit (023); DOJ probe reported (024); Qwen3.6 27B shutdown (025); Compound decommissioned (026) | [TS commit](https://github.com/groq/groq-typescript/commit/8180ac6ec732f3703ae8d15704dc3bab4d301806), [Compound changelog](https://console.groq.com/docs/changelog/compound) | [Reuters via The Star](https://www.thestar.com.my/tech/tech-news/2026/09/10/us-doj-probes-nvidia039s-licensing-deal-with-ai-startup-groq-nyt-reports) | No first-party newsroom post found for September. |
| 2026-10-01..12 | Status incidents: MiniMax M2.7 hardware issues, console outage (027) | [status RSS](https://groqstatus.com/feed.rss) | none found | The Muse Spark Open preview post is dated **2026-10-15** and is excluded (after the window). |

## 4. Dated event evidence and capabilities

See the [CSV](064-groq.events.csv) for all 27 rows. Key clusters:

| Event ID(s) | Published / event date | Claim or observed feature | Availability and limitations | Source (type) | Independent check | Grade |
|---|---|---|---|---|---|---|
| 008, 012, 015, 018 | 2026-06-17 → 07-17 → 08-16 | Self-serve (free/developer) retirement of `qwen3-32b`, `llama-4-scout`, `llama-3.1-8b-instant` and `llama-3.3-70b-versatile`. Enterprise committed-spend contracts were exempt. | 30–60 days' notice. Llama IDs remain Enterprise "Contact Sales" (observed 2026-10-16). | deprecations page (first-party) | One HF forum user reports a forced migration (anecdote, not prevalence) | E2 + single third-party report |
| 009, 022, 025 | 2026-06-17 → 08-25 → 09-14 | `qwen/qwen3.6-27b` added (SDK) and recommended as a Llama replacement. It was itself retired on 09-14 for `qwen/qwen3.8-27b`, which the model page labels **Preview**. | Replacement-of-replacement churn inside one quarter. The Preview tier for 3.6 is stated only by a third-party post. | GitHub releases/commits, deprecations, model page | none | E2 |
| 007, 021, 026 | 2026-06-12, 08-24, 09-21 | Compound agentic systems: built-in `browser_automation` became a silent no-op, then `groq/compound` and `compound-mini` were decommissioned with **no replacement ID**. | Vendor-reported. Shutdown not observed by API call. | Compound changelog, deprecations | none | E2 |
| 003, 004, 013, 022, 023 | 2026-04-18 … 09-03 | SDK releases: headers via env, api-key redaction in debug logs, npm OIDC trusted publishing, reasoning-effort levels for Qwen 3.8 and dependency vulnerability lock updates. Plus an unreleased "strict OpenAI compatibility for white-label deployments" commit. | Generated (Stainless) clients. Release-note dates and GitHub release timestamps differ by up to 16 days (e.g. Python v1.4.0 notes dated 05-12, released 05-28). | GitHub (public artifacts) | none | E2 |
| 010, 016, 005, 006, 017 | 2026-05-28 … 08-17 | $650M (Jun 22) and $350M Series A at $3.5B (Aug 17, "subject to customary closing conditions"). Vendor claims of 13 data centres, ">five million" then ">six million" developers, 54 MW → 200+ MW target. | Financing is not adoption. Developer counts are undefined vendor metrics. | press releases + Reuters/TechCrunch/TNW/Bloomberg Government | Bloomberg Government and TNW independently report the valuation as roughly half the prior $6.9B | E1 |
| 014, 019, 020 | 2026-08-12, 08-24 | NCP certification. Plan to deploy NVIDIA Groq 3 LPX + Vera Rubin NVL72 with Dell. Repeats NVIDIA's "3,400 output tokens/s on Gemma 4 31B at 100K context" and "4x" claims. | **Announced only**: no GroqCloud availability date. StorageReview notes NVIDIA's figure came from a *private pre-release endpoint measured Aug 21* vs live serverless competitors. | Groq blog; trade press | Comparability caveat only, not a replication | E1 |
| 024 | 2026-09-10 (event 09-09) | Reuters relays the NYT: DOJ investigating whether Nvidia structured the Groq deal to avoid antitrust review, with a formal information request. | No outcome; Groq did not comment. | Reuters (syndicated) | none | E1 |
| 027 | 2026-10-09..12 | Self-reported incidents: MiniMax M2.7 data-centre hardware/connectivity issues, plus a console issue affecting Website and API. | The feed shows only recent items. Uptime percentages are self-reported. | status RSS (first-party) | none | E2 |

**Independent speed snapshot (not an in-window event):** [Artificial Analysis' Groq provider page](https://artificialanalysis.ai/providers/groq) (accessed 2026-10-16) lists gpt-oss-120b (high) on Groq at 474 output tokens/s. The Groq Supported Models page shows ~500 tps for the same model, so the vendor figure is roughly consistent. Artificial Analysis still tracks Llama 3.1 8B / 3.3 70B on Groq although self-serve access ended 2026-08-16. Its methodology (median, first-party API) was not audited here.

**Observed maintenance signal (GitHub API; activity, not quality):** commits other than Terraform/workflow automation fell sharply in the window compared with the prior six months:

| Repository | 2025-10-12…2026-04-11 | Window |
|---|---:|---:|
| openbench | 76 | 3 (last release v0.5.3, 2025-12-09) |
| groq-desktop-beta | 26 | 1 |
| groq-api-cookbook | 5 | 0 |
| groq-mcp-server | 0 | 1 |

This coincides with the reported transfer of engineering staff to Nvidia, but **causation is not established**. These repositories should be treated as low-maintenance reuse candidates until their activity is re-checked.

## 5. What the company says it intends to do

| Public direction (≤25 words quoted) | Link/date | Promised horizon | Status | Missing/contradictory context |
|---|---|---|---|---|
| "Groq expects to scale toward 200 MW by the end of 2027." | [2026-06-22](https://groq.com/newsroom/groq-raises-usd650m-to-scale-its-ai-inference-cloud-business) | end of 2027 | planned | The Aug 17 release says "from 54 megawatts to 200+ megawatts in 2027". The MW figures are capacity, not delivered inference or energy measurement. |
| "As we look to bring NVIDIA accelerated computing online in the future, customers will get more capacity … without changing a line of code." | [2026-08-12](https://groq.com/newsroom/groq-becomes-an-nvidia-cloud-partner) | undated | tentative | No dates, regions or model list. "No code change" is untested. |
| Groq "will be among the first adopters of NVIDIA Groq 3 LPX … which it will deploy to its purpose-built AI inference cloud." | [2026-08-24](https://groq.com/blog/groq-among-the-first-to-bring-nvidia-groq-3-lpx-and-vera-rubin-nvl72-to-market) | undated | planned | Performance claims are NVIDIA's pre-release measurements (see 020). |
| "We will be focused on supporting the most important model makers…" (Alex Davis) | [2026-08-17](https://groq.com/newsroom/groq-closes-usd350-million-series-a-building-the-world-s-leading-ai-inference-cloud) | uncommitted | uncommitted | The same release also mentions "training and inference" clusters of NVIDIA compute, a broader scope than the earlier inference-only positioning. |
| Deprecation policy: Preview models "may be discontinued at short notice"; the page advises users to "Consider designing your systems to be model-agnostic". | [deprecations](https://console.groq.com/docs/deprecations.md) (undated policy text) | standing | standing policy | In-window practice: a recommended replacement (Qwen 3.6) was itself retired within the quarter. |

## 6. Independent interpretation: direction and alternative scenarios (2027–2031, conditional)

These are **researcher hypotheses**, not Groq strategy or forecasts.

| Hypothesis | Supporting observations | Rival explanations | Disconfirming signals | Confidence/unknowns |
|---|---|---|---|---|
| H1: GroqCloud moves from an LPU-differentiated API to a largely NVIDIA-hardware neocloud, so "Groq speed" stops being a distinct, reproducible property. | 014, 016, 019; departure of the chip team; "training and inference" wording | LPUs remain the core fleet and NVIDIA is additive capacity | 2027–28 Groq model pages still disclose LPU-specific latency advantages, measured independently at a matched model and context | low–medium; the fleet mix is undisclosed |
| H2: Self-serve model catalogue churn stays high (30–90-day lifetimes) while Enterprise contracts get stability. | 001, 008, 012, 015, 025, 026; enterprise exemptions | Short-term capacity re-allocation during the hardware transition | Median Preview→Production graduation becomes common, with ≥6-month notice periods | medium for 2026; unknown beyond |
| H3: Regulatory scrutiny of "licence + hire" deals constrains future similar transactions but not GroqCloud operations. | 024; Senate letter (baseline) | The probe closes without action | DOJ action or settlement that alters Groq's licence or operations | low; no outcome known |
| H4: Built-in agentic "compound" features are left to customers or third-party integrations rather than the inference vendor. | 007, 021, 026 (no replacement) | Temporary removal before a relaunch | A new Groq-hosted agent/tool system with a stable ID | low–medium |

## 7. Implications for the GitHub 1000 study (M1–M7)

| Construct | Possible observable effect | Study design to test it | Negative/null explanation | Measurement boundary |
|---|---|---|---|---|
| **M1** AI coding-agent change | Agent workflows pinned to a hosted model ID break or silently change when an ID or tool is retired (007, 026). | Log agent runs against pinned model IDs over ≥90 days; count failures caused by provider retirement. | Most agents use aliases or routers and never notice. | opt-in, synthetic tasks only |
| **M2** accepted task quality | A forced swap (e.g. Llama 3.3 70B → gpt-oss-120b) changes acceptance rates. | Frozen task set with hidden independent tests, run on both models (self-host the retired one). | No measurable difference at our task scale. | Same prompts, temperature and tools; Groq's feature matrix differs per model. |
| **M3** discoverability | Vendor developer counts (3.5M → 5M → 6M) are not discoverability evidence. | Not tested here. | — | Counts undefined; never used as an outcome. |
| **M4** verified third-party reuse | Official Groq OSS (openbench, desktop, MCP server) shows low activity; reuse claims need fresh checks. | Trace one consented downstream integration of the groq-python SDK. | Activity drop is irrelevant if the code is stable. | Stars and commits are not reuse. |
| **M5** reuse-first / package rights | The OpenAI-compatible API means the generic `openai` client or a router can replace the vendor SDK. Apache-2.0/MIT licences are clear; the copyright holder changed to Groq LLC. | Compare vendor SDK vs generic client in the experiment below. | The vendor SDK may add real value (typed enums, reasoning params). | Hosted service terms not reviewed. |
| **M6** lifecycle human/energy cost | Migration minutes per deprecation; model-catalogue churn as maintenance load. | Measure human minutes per forced migration. | Churn cost is small relative to other maintenance. | **No energy or carbon estimate**: MW capacity figures are not per-task energy, and no metered data was available. |
| **M7** actionable interventions | Provider-agnostic configuration plus a deprecation-monitoring CI check. | The experiment below. | Over-engineering for a hobby repo. | — |

## 8. One practical, falsifiable change for the maintainer's own repositories

**Repository/component:** a generic pilot on one of the maintainer's repositories that calls a hosted LLM API, or a throwaway sandbox repo if none does. **Not** this study's capture pipeline: `trending_study capture` stays disabled under the source-access decision, and nothing here changes that.

**Candidate practice (not validated):** route hosted-model calls through a thin, provider-agnostic, OpenAI-compatible adapter. The model ID lives in config. A scheduled-by-hand (not automated-scraping) CI check compares the configured IDs against the provider's published deprecation list or `/models` endpoint.

**Treatment and comparator:**
- **Comparator A:** direct vendor SDK calls (groq-python, pinned version) with a hard-coded model ID.
- **Treatment B:** the generic `openai` Python client (pinned) pointed at the OpenAI-compatible base URL, with the model ID in config plus the deprecation check.
- Pin both client versions and the same model ID.

**Frozen comparable task (functional unit):** one **accepted task** is one model-swap migration. Simulate the Aug 16 scenario: replace a retired model ID with the provider's recommended replacement. The task counts as accepted only when a frozen, **independently authored** acceptance suite passes. That suite has 10 synthetic prompts with structured-output and tool-call assertions, written by someone other than the person or agent doing the migration, and the person doing the migration does not see it. All assigned migrations count in the denominator, including abandoned or failed ones.

**Measured human work:** wall-clock reviewer and maintainer minutes per migration (timer log), number of files changed, and number of review rounds.

**Quality/security guardrails:**
- No API keys in code, logs or CI output. A secret scan must be clean, and debug-log redaction must be verified.
- Synthetic prompts only, with no personal data.
- Respect provider rate limits and terms.
- No new paid API spend beyond a fixed, pre-agreed small budget.
- Acceptance tests are never generated by the same agent that performs the migration.
- No AI-contributor attribution appears in commits, per the owner's rule. AI assistance, if used, is recorded only in the private experiment log.

**Success criterion:** B achieves ≥ the acceptance rate of A with ≥30% fewer median human minutes per migration over at least 3 simulated migrations.

**Stop/reversal rule:** stop and keep A if any of the following happens:
- B's acceptance rate is lower;
- a vendor-specific feature that the tasks need (e.g. reasoning-effort enum, citation options) is unreachable through the generic client;
- the deprecation check produces more than 1 false alarm per month;
- any secret appears in logs.

Report a null or negative result as is. **No trial has been executed; no effect is claimed.** No carbon or energy savings are estimated.

## 9. Findings, uncertainties and review outcome

- **Observed/shipped (documentary, E2):**
  - Six self-serve model retirements: Kimi K2 0905; Qwen3 32B and Llama 4 Scout; Llama 3.1 8B and 3.3 70B; Qwen3.6 27B.
  - Compound systems and the `browser_automation` tool retired with no replacement.
  - New Qwen 3.6 then 3.8 model IDs, with Qwen 3.8 in Preview.
  - 13 SDK releases (6 Python, 7 TypeScript) with modest features, including log-redaction and trusted-publishing changes.
  - The OSS copyright holder renamed to Groq LLC.
  - Self-reported October hardware incidents.
- **Claims/announcements only (E1):** $650M and $350M financing (the Series A subject to closing); 13 data centres; 5–6 million developers; 54 → 200+ MW targets; NCP status; LPX deployment and NVIDIA's 3,400 tok/s figure.
- **Conjectures and unknowns:**
  - the legal entity chain (Groq, Inc. → Groq LLC);
  - CEO succession dates;
  - the fleet mix (LPU vs NVIDIA);
  - why the changelog has no entries after April 18;
  - the outcome of the DOJ probe;
  - real usage of any feature.
- **Contradictory or null evidence:**
  - Deal value $17B (Reuters) vs ~$20B (others).
  - CEO named Adam Winter (Groq, TechCrunch) vs Doug Wightman (TNW).
  - A valuation halved from $6.9B to $3.5B (Bloomberg Government, TNW).
  - The LPX benchmark was a pre-release private endpoint (StorageReview).
  - Sharply reduced activity in official OSS repositories.
  - No in-window first-party newsroom posts were found for April–May, July or September.
- **Reviewer links and audit date:** none yet. A human factual/link spot-check, a source-access/rights review and a methods review are required before any lesson is drawn. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.
