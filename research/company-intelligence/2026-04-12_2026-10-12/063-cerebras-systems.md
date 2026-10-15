# Company 6-month technology intelligence: Cerebras Systems (063)

> **PROVISIONAL, AI-assisted first-pass screen (2026-10-16). Not reviewed by a qualified human.** This report, its [event ledger](063-cerebras-systems.events.csv) and its [search log](063-cerebras-systems.search-log.md) are documentary source leads. They are not verified findings. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open. Nothing here is a product, investment, security or energy recommendation.

- **Company watchlist ID:** 063
- **Research issue:** [#131](https://github.com/MSKazemi/github-trending-1000-study/issues/131). Evidence corpus: [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56). No `NEWS-YYYY-NNNN` items were minted; candidate items are flagged in §9.
- **Ownership and product boundaries (as of 2026-10-12):** see §2.
- **Product URL and company newsroom:** [cerebras.ai](https://www.cerebras.ai/), [press releases](https://www.cerebras.ai/company/press-release), [blog](https://www.cerebras.ai/blog), [inference docs change log](https://inference-docs.cerebras.ai/support/change-log), [deprecations](https://inference-docs.cerebras.ai/support/deprecation), [status](https://status.cerebras.ai/), [GitHub org](https://github.com/Cerebras). The [investor-relations site](https://investors.cerebras.ai/) returned **HTTP 403** to automated access.
- **Analysis window:** 2026-04-12 to 2026-10-12 inclusive. Sources were accessed on 2026-10-16 UTC.
- **Researcher / factual reviewer / review date:** AI-assisted researcher (single pass). The factual/link reviewer and the methods reviewer are **pending**.
- **Status:** screened (provisional). It has not been independently checked.
- **Source coverage:** 18 logged queries (17 executed; Q18 on litigation/export-control/CFIUS was **not run** because the search budget ran out). The site sitemap was fully enumerated, along with docs Markdown, the GitHub API, PyPI/npm and the status RSS. See the [search log](063-cerebras-systems.search-log.md) for inaccessible sources (IR site, SEC via curl, GlobeNewswire, openai.com) and for the conflicts that are recorded rather than resolved.

## 1. Search and inclusion audit

| Search run UTC | Site/engine | Full query and dates | Found | Screened | Included | Excluded/why | Coverage limitation |
|---|---|---|---:|---:|---:|---:|---|
| 2026-10-16 | Web search (Q01–Q17) | 17 queries with exact strings in the search log, covering all seven segments | unknown | unknown | 7 rows (016, 017, 021, 028, 030, 033, 037) rest on pages opened from these leads | unknown (snippet-only results, aggregators, conflicting valuations) | The tool exposes no hit counts or ranks. Q18 (critical/legal) was not executed. |
| 2026-10-16 | cerebras.ai sitemap | All 103 `press-release` URLs plus `/news/` URLs fetched, with dates extracted | 105 | 105 | 13 in-window URLs = 12 releases (Lovable has 2 URLs) → 11 rows | Out-of-window releases; Aug 14 livestream logistics notice | No `lastmod`. Four IR-only releases were inaccessible directly. |
| 2026-10-16 | Blog index | Display dates read for posts from 2026-01 to 2026-10 | 30 in-window | 13 opened | 8 rows | Opinion/education posts listed in the log; one HTTP 500 | Selection is purposive |
| 2026-10-16 | Inference docs change log and deprecations | Full raw Markdown | ~25 in-window entries | all | 15 rows | Minor entries listed in the log | Mutable pages; no archived 2026-10-12 copy |
| 2026-10-16 | GitHub API / PyPI / npm / status RSS | org repos, commits, package release times, incident feed | 11 repos; 6 status entries | all | 4 rows | Low-signal commits; 5 status entries summarised only | No GitHub Releases objects exist for the SDKs |

## 2. Verified company/product identity and baseline

- **Entity.** The entity is **Cerebras Systems Inc.**, headquartered at 1237 E. Arques Ave, Sunnyvale, CA, according to the site footer. Its Class A common stock **began trading on Nasdaq Global Select as `CBRS` on 2026-05-14**. The IPO closed on 2026-05-15 ([closing release](https://www.cerebras.ai/press-release/cerebras-systems-announces-closing-of-initial-public-offering)). The SEC CIK 0002021728 appears in the 8-K exhibit URLs. **Status change in the window:** the company went from private to publicly listed. **No parent company, acquisition or rename was identified.** Beneficial ownership, state of incorporation and the dual-class/warrant structure were **not verified** at filing level, because the SEC primary documents could not be retrieved with raw tooling. A secondary analysis ([implicator.ai, 2026-05-15](https://www.implicator.ai/cerebras-got-its-ipo-pop-now-the-95-billion-promise-starts/)) reports that OpenAI holds warrants and lent $1.0B of working capital. That is secondary reporting and unconfirmed against the prospectus.
- **Regulation FD channels.** The CS-4 release names investors.cerebras.ai and the @cerebras X account as Regulation FD disclosure channels.
- **Offering (verified against current pages):**
  - Hardware: wafer-scale processors (WSE-3; **WSE-3 Turbo announced 2026-08-18**) and systems (CS-3; **CS-4** on the new "Nexus" rack platform).
  - **Cerebras Inference Cloud:** a shared/public-endpoint API with an OpenAI-compatible SDK surface, plus contract **Dedicated Endpoints**.
  - Official SDKs: `cerebras-cloud-sdk` for Python and Node, both Apache-2.0.
  - Other GitHub projects: `modelzoo` (Apache-2.0), a VS Code chat extension (MIT) and a new Dataiku plugin (Apache-2.0).
  - The serving software and hardware designs are **proprietary**. Open-weight models served on the platform keep their own upstream licences.
- **Pre-window baseline (context only, not counted):** Series H on 2026-02-03; AWS collaboration on 2026-03-13; GPT-5.3-Codex-Spark on Cerebras (blog 2026-02-12); model deprecations from January to March 2026; status incidents in Jan–Mar 2026.

## 3. Month-by-month discoveries (six calendar months + partial endpoints)

| Month | Announcements/changes (ledger rows) | Primary URLs | Independent reporting | Notes or no-result limitations |
|---|---|---|---|---|
| 2026-04-12..30 | $850M revolver (001); S-1 filed (002); `prompt_cache_key` (003); **422→400 breaking change** (004); GLM 5/5.1/Kimi K2.6 dedicated (005) | [credit](https://www.cerebras.ai/press-release/cerebras-systems-closes-usd850-million-revolving-credit-facility), [S-1 PR](https://www.cerebras.ai/press-release/cerebras-systems-announces-filing-of-registration-statement-for-proposed-initial-ipo), [change log](https://inference-docs.cerebras.ai/support/change-log) | DCD (Jun 25) gives the filing date as Apr 18, which conflicts | 5 rows |
| 2026-05 | Projects GA (006); Cognition case study (007); IPO launch, pricing, closing (008, 010, 011); Multi-LoRA private preview (009); Kimi K2.6 enterprise trials (012); 2 model deprecations (013) | [pricing](https://www.cerebras.ai/press-release/cerebras-systems-announces-pricing-of-initial-public-offering), [Multi-LoRA](https://www.cerebras.ai/blog/introducing-multi-lora-on-cerebras-inference), [Kimi](https://www.cerebras.ai/blog/cerebras-kimi-k2-Enterprise) | [implicator.ai](https://www.implicator.ai/cerebras-got-its-ipo-pop-now-the-95-billion-promise-starts/) on concentration; AA page does not show the Kimi result | 8 rows |
| 2026-06 | StepFun dedicated models (014); vendor Kimi vs Gemini comparison (015); Q1 results (016); **share fall and margin guidance cut** (017); Gemma 4 31B and image-input preview (018) | [Q1 8-K](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026044941/cbrsannouncesfinancialresu.htm) (via StorageNewsletter copy) | [DCD](https://www.datacenterdynamics.com/en/news/cerebras-shares-fall-by-20-percent-after-company-publishes-first-earnings-report-since-its-ipo/) | 5 rows |
| 2026-07 | Flex 7x CS-3 capacity plan (019); Upstage (020); 200 MW Europe plan (021); SDK 1.91.0 (022); dual-bucket rate limits and $5 credits (023); **API v2 default** (024); AMD Helios disaggregation (025); Predicted Outputs restricted (026) | [Flex](https://www.cerebras.ai/press-release/flex-and-cerebras-expand-partnership-to-scale-american-manufacturing-of-cerebras-ai), [AMD](https://www.cerebras.ai/press-release/amd-and-cerebras-announce-industry-leading-ultra-low-latency-and-high-throughput-ai-inference), [PyPI](https://pypi.org/project/cerebras-cloud-sdk/1.91.0/) | none ledgered | 8 rows. The IR release on 200 MW was inaccessible, so a reproduction is cited. |
| 2026-08 | Lovable (027); Q2 results (028); **GPT-5.6 Sol Ultrafast preview in OpenAI API** (029, 030, 035); GLM 4.7 deprecated (031); **CS-4** (032); Callosum (033); CS-5/CS-6 roadmap (034); Flowise integration retired (036) | [CS-4](https://www.cerebras.ai/press-release/cerebras-unveils-cs-4-up-to-30-times-faster-than-gpu-based-solutions-3347356), [Sol blog](https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai), [Hot Chips](https://www.cerebras.ai/blog/ultrafast-frontier-inference-cerebras-deep-dive-at-hot-chips-2026) | [OpenAI community post](https://community.openai.com/t/ultrafast-mode-preview-gpt-5-6-sol-at-up-to-14x-the-speed-in-the-api/1390344) (counterparty); [The Next Web](https://thenextweb.com/news/openais-new-ultrafast-mode-runs-gpt-5-6-sol-14-times-faster-on-cerebras-chips) | 10 rows. Post-Q2 share-decline reports were snippet-only (E0, not ledgered). |
| 2026-09 | Finland 165 MW (037); Qwen 3.8 27B public (038); **Gemma 4 31B pulled from shared tier** (039); VS Code extension maintenance (040); 2026-09-25 service disruption (041); Gimlet (042); General Compute (043) | [Gimlet](https://www.cerebras.ai/press-release/gimlet-labs-adds-cerebras-to-deliver-ultrafast-ai-inference-through-gimlet-cloud-deployment), [General Compute](https://www.cerebras.ai/press-release/general-compute-selects-cerebras-to-bring-ultra-fast-inference-to-agentic-coding), [status](https://status.cerebras.ai/incidents/8sc27zfgpkhk) | [DCD Finland](https://www.datacenterdynamics.com/en/news/cerebras-starts-construction-on-165mw-data-center-in-mikkeli-finland/) | 7 rows |
| 2026-10-01..12 | Dataiku plugin repo (044); service-tier docs correction (045) | [repo](https://github.com/Cerebras/cerebras-dataiku-plugin), [change log](https://inference-docs.cerebras.ai/support/change-log) | none found (Q12) | 2 rows. No October press release surfaced in the window. |

**Total: 45 ledger rows.** Several rows describe the same event: the IPO (002, 008, 010, 011), Q1 results (016, 017) and GPT-5.6 Sol (029, 030, 035) share `duplicate_event_group` values. Counting each group once gives **39 distinct events**. This is a purposive selection, not a census of releases.

## 4. Dated event evidence and capabilities (highlights; full detail in CSV)

| Event ID | Published UTC / underlying event date | Claim or observed feature | Availability and limitations | Source link (type) | Independent check | E0–E4 working grade |
|---|---|---|---|---|---|---|
| CI2026-063-004 | 2026-04-24 | Validation errors changed from HTTP 422 to 400; SDK exception class renamed | Breaking change for downstream handlers | [change log](https://inference-docs.cerebras.ai/support/change-log) (docs) | — | E2 |
| CI2026-063-009 | 2026-05-06 | Multi-LoRA: HF-PEFT adapters with per-request switching on a shared base model | **Private preview**, dedicated endpoints only, through an account rep | [blog](https://www.cerebras.ai/blog/introducing-multi-lora-on-cerebras-inference) | — | E1 |
| CI2026-063-011 | 2026-05-15 / 2026-05-14 | IPO closed: 34.5M shares at $185, about $6.38B gross; CBRS began trading May 14 | Release text says "May 13, 2025" for the effective date (apparent error) | [PR](https://www.cerebras.ai/press-release/cerebras-systems-announces-closing-of-initial-public-offering) | implicator.ai (analysis) | E1 |
| CI2026-063-012 | 2026-05-19 | Kimi K2.6 (1T-parameter MoE) in enterprise trials; vendor quotes 981 output tok/s attributed to Artificial Analysis | Enterprise trials only. **AA public page (2026-10-16) does not list Cerebras for K2.6** | [blog](https://www.cerebras.ai/blog/cerebras-kimi-k2-Enterprise) | [AA](https://artificialanalysis.ai/models/kimi-k2-6/providers) (contrary/unresolved) | E1 |
| CI2026-063-017 | 2026-06-25 | Shares fell ~20%; FY gross-margin guidance cut to 38–41%; CEO says capacity is "at a premium" and the company will rent its own systems back from a customer | Independent journalism about one earnings event | [DCD](https://www.datacenterdynamics.com/en/news/cerebras-shares-fall-by-20-percent-after-company-publishes-first-earnings-report-since-its-ipo/) | — | E1 (independent) |
| CI2026-063-024 | 2026-07-22 | API v2 becomes default with stricter structured-output and tool-call validation | Default change; breakage not measured | [change log](https://inference-docs.cerebras.ai/support/change-log) | — | E2 |
| CI2026-063-028 | 2026-08-12 | Q2: GAAP revenue $180.1M (+74%), core $209.9M (+103%), GAAP cloud and other services $126.0M (+281%), RPO $25.4B | Non-GAAP "core" metrics; Aug 12 date not raw-confirmed | [8-K](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm) | [StorageNewsletter copy](https://www.storagenewsletter.com/2026/08/14/cerebras-systems-fiscal-2q26-financial-results/) (raw-confirmed) | E1 |
| CI2026-063-029 | 2026-08-13 | OpenAI "Ultrafast" API tier for GPT-5.6 Sol powered by Cerebras: up to 750 output tok/s and up to 14x Standard | **Limited preview**, no published pricing. The HLE timing comparison was run by the vendor | [blog](https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai) | [OpenAI community](https://community.openai.com/t/ultrafast-mode-preview-gpt-5-6-sol-at-up-to-14x-the-speed-in-the-api/1390344); [TNW](https://thenextweb.com/news/openais-new-ultrafast-mode-runs-gpt-5-6-sol-14-times-faster-on-cerebras-chips) | E1 (counterparty-corroborated availability; speed unverified) |
| CI2026-063-032 | 2026-08-18 | CS-4 (three WSE-3T): up to 2x CS-3 speed, up to 10x throughput/W vs CS-3, more than 4,400 TPS/user on GPT-OSS-120B, RoCE v2 and switchless Direct Wafer Links | "First CS-4 shipments begin this quarter" was a plan, and shipment is unverified. Throughput is footnoted as configuration-dependent | [PR](https://www.cerebras.ai/press-release/cerebras-unveils-cs-4-up-to-30-times-faster-than-gpu-based-solutions-3347356) | none | E1 |
| CI2026-063-039 | 2026-09-03 | Gemma 4 31B removed from shared/public endpoints about 2 months after its preview launch; dedicated only | Model churn; conflicting terminology in two docs pages | [change log](https://inference-docs.cerebras.ai/support/change-log) | [deprecations](https://inference-docs.cerebras.ai/support/deprecation) | E2 |
| CI2026-063-041 | 2026-09-25 | Partial service disruption from 10:54 to 13:41 UTC, with root cause still under investigation at resolution | First-party status; no post-mortem found | [status](https://status.cerebras.ai/incidents/8sc27zfgpkhk) | — | E2 |

**Capability inventory, separating what was asserted from what was observed:**

- **APIs (documented, E2):** `prompt_cache_key` (Apr); 422→400 error semantics (Apr); Projects GA (May); image inputs in public preview (Jun); dual-bucket uncached/total TPM rate limits (Jul); API v2 default (Jul); Predicted Outputs restricted to dedicated endpoints (Jul); service-tier `auto`→`flex` fallback documented (Oct).
- **Models (E2 for availability, E1 for speed):**
  - Added: GLM 5/5.1 and Kimi K2.6 (dedicated); StepFun 3.5/3.7 Flash (dedicated); Gemma 4 31B (preview, later pulled from the shared tier); Qwen 3.8 27B (public).
  - **Retired in window:** llama3.1-8b, qwen-3-235b-a22b-instruct-2507, zai-glm-4.7, and Gemma 4 31B from the shared tier.
- **SDK/OSS (E2):**
  - SDK 1.91.0 on PyPI and npm (Apache-2.0). The GitHub repo has no git tags; a pre-window `release: 1.79.0` commit (2026-04-09) has no PyPI files, and the SDK CHANGELOG links to a **private** upstream repository, so the public repo is a mirror.
  - VS Code extension maintenance (MIT). New Dataiku plugin repository (Apache-2.0).
  - No security advisory for the SDKs was found. That is a search limit, not an audit.
- **Hardware and roadmap (E1, vendor claims):** CS-4/WSE-3T; CS-5 targeted for 2027; CS-6 with 3D-stacked DRAM. **No independent benchmark** of CS-4 was found.
- **Distribution and partners (E1, mostly announced only):** OpenAI API Ultrafast (preview); Lovable (dedicated capacity for "selected" workloads); AMD Helios (H2 2026 plan); Callosum APIs; Gimlet Cloud (later in 2026); General Compute (Q1 2027); Upstage (exploratory).
- **Licensing and rights:** the hosted service and hardware are proprietary. The SDKs are Apache-2.0. Each open-weight model's licence must be checked separately. Prompt and data handling terms were **not reviewed**.

## 5. What the company says it intends to do

| Verbatim or close paraphrase of public direction (<=25 words per source quoted) | Link/date | Promised horizon | Status (planned, tentative, uncommitted) | Missing/contradictory context |
|---|---|---|---|---|
| "plan to more than triple revenue in 2027" | [Q2 release copy](https://www.storagenewsletter.com/2026/08/14/cerebras-systems-fiscal-2q26-financial-results/), 2026-08-12 | 2027 | planned (forward-looking statement) | Snippets report the stock fell after the results (E0). Q2 GAAP revenue ($180.1M) was below Q1 GAAP ($193.4M). |
| Data-center capacity "live and under contract for delivery by the end of 2027 to more than 600 MW" | same, 2026-08-12 | end-2027 | planned | Capacity scarcity was acknowledged in June (DCD). |
| "CS-5, targeted for 2027, is designed to generate up to 10,000 output tokens per second per user" on leading open models | [Hot Chips blog](https://www.cerebras.ai/blog/ultrafast-frontier-inference-cerebras-deep-dive-at-hot-chips-2026), 2026-08-25 | 2027 | tentative target | No silicon availability evidence |
| A path "to double token-generation speed year over year for the next several years"; CS-6 to stack DRAM at wafer scale | same | multi-year | uncommitted aspiration | — |
| "First CS-4 shipments begin this quarter" | [CS-4 PR](https://www.cerebras.ai/press-release/cerebras-unveils-cs-4-up-to-30-times-faster-than-gpu-based-solutions-3347356), 2026-08-18 | Q3 2026 | planned | Shipment not verified by 2026-10-12 |
| Joint AMD solution "expected to become available initially through Cerebras Cloud in the second half of 2026" | [AMD PR](https://www.cerebras.ai/press-release/amd-and-cerebras-announce-industry-leading-ultra-low-latency-and-high-throughput-ai-inference), 2026-07-23 | H2 2026 | planned | No availability observed in window |
| First European capacity by end-2026; "200 MW by the end of 2027", partly for OpenAI workloads | [reproduction](https://www.storagenewsletter.com/2026/07/13/raise-summit-2026-cerebras-systems-accelerates-european-expansion-with-200mw-of-ai-compute-capacity-by-end-of-2027/), event 2026-07-09 | 2026–2027 | planned | Sites partly named later (Mikkeli, Sep 1) |
| "available through General Compute starting Q1 2027" | [PR](https://www.cerebras.ai/press-release/general-compute-selects-cerebras-to-bring-ultra-fast-inference-to-agentic-coding), 2026-09-29 | Q1 2027 | planned | Contract value undisclosed |
| Ultrafast access "expanding as capacity grows" | [OpenAI community](https://community.openai.com/t/ultrafast-mode-preview-gpt-5-6-sol-at-up-to-14x-the-speed-in-the-api/1390344), 2026-08-13 | none | uncommitted | No pricing and no GA date |

These are statements of intent, not delivered facts. The company's own forward-looking-statement disclaimers apply.

## 6. Independent interpretation: direction and alternative scenarios (researcher's conditional 2027–2031 view)

| Hypothesis for 2027–2031 | Supporting observations | Rival explanations | Disconfirming signals | Confidence/unknowns |
|---|---|---|---|---|
| H1: "Latency tiers" become a priced, separable option for coding agents (fast vs standard serving of the *same* model) | OpenAI Ultrafast preview on Cerebras (029); General Compute positions agentic coding as the first use case (043); Lovable deal (027) | Speed demand may be concentrated in a few large buyers; caching or speculative decoding on GPUs may close the gap | Ultrafast stays in limited preview through 2027 with no published price, or providers fold speed into standard tiers | Low. Pricing and adoption are unobserved. |
| H2: Disaggregated prefill/decode across heterogeneous chips becomes a common serving pattern | AMD (025), Gimlet (042), Callosum (033), CS-4 RoCE/Direct Wafer Links (032) | These are mostly partnership announcements and may not produce deployed services | None of the AMD/Gimlet/Callosum offerings is generally available by end-2027 | Low to medium. All are announced only. |
| H3: Hosted fast-inference catalogs stay **volatile**, which raises maintenance cost for dependants | 4 retirements in 6 months; Gemma 4 pulled from the shared tier about 2 months after preview (039); two breaking API changes (004, 024) | Volatility may reflect the fast pace of open-weight releases rather than a lasting provider practice | A published model-lifetime commitment, or no retirements over a 12-month period | Medium for the observed churn; unknown for the future |
| H4: Revenue concentration (UAE, then OpenAI) remains a structural risk to service continuity for small users | Secondary reporting on S-1/A concentration ([implicator.ai](https://www.implicator.ai/cerebras-got-its-ipo-pop-now-the-95-billion-promise-starts/)); OpenAI 750 MW deal | Diversification through AWS, Lovable and neoclouds may dilute this risk | 10-Q customer-concentration disclosure falls well below majority share | Low. The primary filing has not been read. |

These are the researcher's conjectures, not company strategy or forecasts. Energy claims such as "10x throughput per watt" and "5x tokens per second per watt" are **vendor ratios without metered system boundaries**. They cannot support any carbon or energy conclusion.

## 7. Implications for the GitHub 1000 study

| M1–M7 construct | Possible observable effect | Study design to test it | Negative/null explanation | Measurement boundary |
|---|---|---|---|---|
| **M1** AI coding-agent change | Agents run more sequential steps per task when latency is low | Pinned-model A/B on identical frozen tasks, measuring steps and wall-clock per accepted task | Faster tokens do not change step count or acceptance | Only opt-in, synthetic tasks |
| **M2** accepted task quality | A speed tier claims the same weights and precision (035) | Independent hidden acceptance tests, same model, fast vs standard provider | Quality is identical (expected if the parity claim holds) or degrades through provider differences | Speed is not quality. Vendor HLE timings are excluded. |
| **M3** discoverability | Native providers in coding tools (Kilo Code, opencode, VS Code extension) | Count onboarding steps to first successful call | Discoverability comes from upstream tools, not from Cerebras | Docs-based only |
| **M4** verified third-party reuse | SDK and plugins on PyPI, npm and GitHub | Trace a consented downstream integration; ignore stars and downloads | Registry downloads ≠ reuse | No downstream evidence collected |
| **M5** review/maintenance | Model retirements and breaking API changes (004, 013, 024, 031, 036, 039) | Log migration minutes per provider change over 6 months | Churn is comparable across all hosted providers | Requires a comparator provider log |
| **M6** lifecycle human/energy cost | Vendor perf/W claims; Finland closed-loop cooling by design | Only metered energy at the user's boundary (not available for a hosted API) | Hosted energy is unobservable to users, so the result is "unknown" | **No token-to-CO2e conversion** |
| **M7** rights/security | Proprietary hosted service; Apache-2.0 SDK; model-specific licences | Terms and data-retention review before sending any code | Terms make sending repo code unacceptable | Terms not reviewed here |

Company adoption claims (OpenAI, Lovable, Cognition) are **not** independent task outcomes, and press coverage of the IPO is not evidence of developer adoption.

## 8. One practical, falsifiable change for the maintainer's own repositories

**Repository/component:** a **synthetic, offline copy** of [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study) maintenance tasks (for example, a docs or ledger-validator fix). No live GitHub capture is involved, the source-access hard stop is respected, and no real study data is used.

**Candidate practice (not yet validated):** a provider-pinning plus fallback policy for any coding agent. Pin the exact model ID and API version header, and keep a tested fallback to a second provider serving the same open-weight model. The trigger is the documented model churn and breaking API changes listed above.

**Treatment/control and frozen comparable task:**
- **Functional unit:** one *independently accepted* task, meaning it passes hidden acceptance tests authored by someone other than the agent operator and kept out of agent context.
- **Task set:** freeze 12 bounded synthetic tasks before the trial. Every assigned task counts in the denominator, including refused, timed-out and abandoned ones.
- **Arms:** **A (control)** uses the same agent harness with `gpt-oss-120b` on a non-Cerebras provider. **B** uses `gpt-oss-120b` on a Cerebras public endpoint, pinned with `X-Cerebras-Version-Patch` per the docs.
- **Held constant:** identical prompts, temperature, tool set and token budget. Record the provider response's `service_tier`.

**Success and guardrails:**
- **Primary measure:** accepted tasks divided by all assigned tasks.
- **Secondary measures:** wall-clock to an accepted patch; maintainer review and rework minutes, measured with a timer; provider cost from invoices; count of provider-change incidents during the trial.
- **Guardrails:**
  - Only synthetic fixtures are sent to any provider: no secrets, no `.env`, no unpublished data.
  - Read the provider's data-retention terms first.
  - Every commit is authored solely by the maintainer. **No AI co-author trailer or attribution**, and no `--no-verify`.
  - Existing unit tests must stay green.
  - Energy is reported as **not measured** unless metered at the maintainer's boundary. Vendor perf/W ratios are not used.

**Stop/reversal rule:** stop if any of the following happens:
- any secret or non-synthetic content would leave the machine;
- arm B's acceptance rate falls more than 2 tasks below arm A;
- review minutes per accepted task rise in arm B;
- the pinned model is deprecated mid-trial (record this as a finding, not a failure to hide);
- the cost cap set in advance is reached.

If speed does not reduce maintainer minutes per accepted task, keep the simpler single-provider setup and record the null result. **No trial was executed and no effect was estimated.**

## 9. Findings, uncertainties and review outcome

- **Observed/shipped (E2, documentary):**
  - Seven API/console changes (rows 003, 004, 006, 023, 024, 026, 045), including two breaking-type changes.
  - Four model retirements and five model additions or availability expansions.
  - SDK 1.91.0 on PyPI and npm.
  - New Apache-2.0 Dataiku plugin repo.
  - One multi-hour service disruption on Sep 25, roughly 10:54–13:41 UTC until services were restored.
  - IPO completed and listed (E1 company releases, consistent across secondary press).
- **Claims/announcements only:** CS-4 shipments; CS-5/CS-6 targets; AMD, Gimlet, Callosum, General Compute and Lovable product availability; 200 MW Europe and >600 MW capacity; 7x CS-3 manufacturing; "more than triple revenue in 2027"; all speed and perf/W figures.
- **Conjectures and unknowns:**
  - Developer adoption. Accepted-task quality on Cerebras-served models.
  - Prompt/data retention terms. Energy at any boundary.
  - Customer concentration (primary filing not read).
  - Litigation, export-control and CFIUS developments (query not executed).
  - Whether the Cerebras Code subscription plans changed in the window.
- **Important contradictory or null evidence:**
  - The AA public page does not show the vendor-attributed Kimi K2.6 benchmark.
  - DCD reports a ~20% share fall and margin-guidance cut after Q1, plus data-center scarcity and rented-back capacity.
  - Q2 GAAP revenue was below Q1 GAAP.
  - Date conflicts in the S-1 filing date and the closing release's "2025" effective date, plus the CS-4 Aug 18/19 listing.
  - Gemma 4 31B was removed from the shared tier about two months after launch.
- **Raw-text confirmation:** every number in the ledger was matched against raw page text (curl/urllib HTML, docs Markdown, GitHub/PyPI/npm JSON, status RSS). The exceptions are the two SEC dates (Jun 23, Aug 12), which were read only via WebFetch summaries, and the Jul 9 RAISE event date, which comes from secondary reports.
- **Candidate #56 items (unminted, pending human verification):** DCD 2026-06-25 (independent contrary reporting); The Next Web 2026-08-14 (independent, non-duplicative of the vendor post); DCD 2026-09-02 (independent construction report).
- **Reviewer links and audit date:** none yet; first pass dated 2026-10-16. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

## Independent source spot-check (2026-10-16)

This is an AI-assisted spot-check by a second agent, not a qualified human review. Each cited URL was re-fetched on 2026-10-16 with a generic user agent, and the date and figures were matched against raw page text (HTML converted to text and searched), or against the GitHub API, the PyPI JSON API and the npm registry JSON. sec.gov/EDGAR was not contacted. All 45 rows were checked: **40 confirmed, 4 corrected, 1 unverifiable, 0 wrong.**

| Rows checked | Outcome | Note |
|---|---|---|
| 001 | confirmed | Apr 15 2026 display date; five-year syndicated revolver "for up to $850 million". |
| 002 | confirmed | Dateline "April 17, 2026"; Class A; Nasdaq Global Select; "CBRS"; share count and price range "not yet been determined". The DCD Apr 18 date it is contrasted with could not be rechecked (DCD returned HTTP 403). |
| 008 | confirmed | 28,000,000 shares plus a 30-day option for 4,200,000; "$115.00 to $125.00"; BUSINESS WIRE dateline carries no date and the page shows May 04 2026. |
| 010 | confirmed | 30,000,000 shares at $185.00; option for 4,500,000; trading expected May 14, 2026 and closing on May 15, 2026. |
| 011 | confirmed | 34,500,000 shares including the full option; about $6.38 billion gross; trading began May 14, 2026; the release text does say "declared effective ... on May 13, 2025". |
| 016, 028 | confirmed (figures) | StorageNewsletter raw text matches every figure: Q1 $193.4M / $191.3M (+92%) / $79.8M (+167%) / net loss $14.0M / 750 MW / >$20B; Q2 $180.1M (+74%) / $209.9M (+103%) / $126.0M (+281%) / RPO $25.4B / $880-890M / "more than triple revenue in 2027" / >600 MW. The SEC datelines (Jun 23, Aug 12) remain unverified because EDGAR was not contacted. |
| 017 | unverifiable | DCD returned HTTP 403 to curl and to WebFetch. The ~20% fall, 38-41% guidance, "at a premium", rent-back and Apr 18 / May 15 dates are not rechecked. |
| 003-006, 014, 018, 023, 024, 026, 036, 038 | confirmed | Change-log entries match the dates and wording (prompt_cache_key; 422→400 with UnprocessableEntityError→BadRequestError; GLM 5/5.1/Kimi K2.6 dedicated; Projects GA; StepFun 3.5/3.7 Flash; Gemma 4 31B image preview; $5 / 30-day credits and dual-bucket limits fully in effect Aug 17; API v2 default on Jul 22; Predicted Outputs by request; Flowise legacy with support ending Aug 31; Qwen 3.8 27B with reasoning defaulting to high). |
| 013, 031, 039 | confirmed | The deprecations page lists 2026-05-27 (llama3.1-8b, qwen-3-235b-a22b-instruct-2507 → GPT OSS 120B), 2026-08-17 (zai-glm-4.7) and 2026-09-03. The "public endpoints" (change log) vs "Shared Inference" (deprecations page) terminology conflict is real. |
| 045 | corrected | The change log says only that docs were updated "to match the current service-tier behavior". The ledger's "earlier docs implied different semantics" is an inference and has been reworded. |
| 007 | corrected | The page footnote does disclose the method: the ~5x is Cognition-provided output speed for its GPU "Free" tier (~200 TPS) vs its Cerebras "Fast" tier (~950 TPS). It is a throughput ratio between tiers, not task time. The limitation "method not published" was wrong. |
| 009, 020 | confirmed | Multi-LoRA: private preview, dedicated endpoints, "no additional cost", HF PEFT format, May 06 2026. Upstage: Jul 10 2026, "explore", Solar 31B "up to 2,000 tokens per second". |
| 012, 015 | confirmed | 981 tok/s, 6.7x and enterprise trials (May 19); 981 vs 181 tok/s with a 10,000-token input (Jun 05). The Artificial Analysis providers HTML mentions Cerebras only in a slug/logo list, which is consistent with the ledger. |
| 019 | confirmed | Dateline July 9, 2026; Milpitas; "approximately 7x through 2026" for CS-3. |
| 021, 037 | confirmed (figures) | StorageNewsletter text matches 200 MW by end-2027, France and the Nordics, first capacity by end-2026, and part of it for OpenAI; 165 MW phased from 50 MW, seven-year service orders, closed-loop cooling and waste-heat recovery "designed", and EUR 1.0-1.7B from the Ramboll study. The event dates (Jul 9, Sep 1) are not in the reproductions and remain unconfirmed. |
| 022 | corrected | PyPI 1.91.0 was uploaded 2026-07-16T17:07Z and npm 1.91.0 on 2026-07-16T20:54Z; the `release: 1.91.0` commit is dated 2026-07-08; Apache-2.0. **The repo has zero git tags**, so the "GitHub tag 1.79.0" was wrong: it is a `release: 1.79.0` commit dated 2026-04-09 with no PyPI files. The CHANGELOG does link `cerebras-cloud-sdk-python-private`, which returns 404 publicly. Fixed in the CSV and §4. |
| 025 | corrected | Footnote [i] was reviewed. The "up to 5x" T/s/W comes from *modelling* by AMD Performance Labs and Cerebras (July 2026) on Kimi 2.6 1T, comparing Helios+WSE against a **WSE-only** configuration. It is not a measurement and not a comparison against GPUs. H2 2026 availability confirmed. |
| 027, 033, 042, 043 | confirmed | Lovable: "selected latency-sensitive workloads on dedicated Cerebras capacity", 50M projects, and the duplicate URL serves the same release (Aug 05 2026). Callosum: the finviz reproduction (Aug 20, 2026, GLOBE NEWSWIRE) has "available through Callosum APIs". Gimlet: Sept. 28, 2026, "up to 3,000 tokens per second", "later this year", CS-4 launch partner. General Compute: Sept. 29, 2026, first use case agentic coding, "starting Q1 2027". |
| 029, 030, 035 | confirmed | The Cerebras blog (Aug 13) has 750 tok/s, the select-customer limited preview and HLE 2,500 questions in 11h11m vs 78h27m (Jul 10 vs Jul 13-15 runs). The "14x" appears in the OpenAI community post (Aug 13), not in the Cerebras blog. TNW (Aug 14) reports a preview opened 13 August and that OpenAI "has not published pricing". The Aug 27 explainer states it is "not ... distilled, or quantized" and runs on WSE-3. |
| 032, 034 | confirmed | CS-4: dateline Aug. 18, 2026 while the page shows Aug 19; three WSE-3T; up to twice CS-3 speed; up to 10x throughput/W; >4,400 TPS/user on GPT-OSS-120B; 750 PFLOPs; RoCE v2; Direct Wafer Links; "First CS-4 shipments begin this quarter". Hot Chips (Aug 25): CS-5 "targeted for 2027" at 10,000 / 5,000 tok/s/user; CS-6 with 3D-stacked DRAM; "double token-generation speed year over year". |
| 040, 044 | confirmed | The GitHub API shows Sep 14 merges of release-v0.1.21, the internal-model-option filter and the Qwen 3.8 speed docs (MIT). The Dataiku repo was created 2026-10-05T19:17Z (Apache-2.0); the internal sync commit is dated Oct 9 and the merge Oct 12. |
| 041 | confirmed (detail added) | Status page: 10:54 UTC onset (first post 12:16 UTC), monitoring at 13:41, resolved at 17:14. The ledger now also names GPT-OSS-120B and Qwen-3.8-27b as the affected components shown on the page. |

**In-window leads seen during the check but not ledgered or verified:**
- Change-log entries for 2026-07-14 (Gemma 4 31B in coding integrations), 2026-07-23 (image limit raised to 10), 2026-07-26 (15,000 px per-side image limit returning 413) and 2026-09-22 (temporary Qwen 3.8 27B total-TPM increase).
- A related-topic title on the OpenAI community page, "Ultrafast is rolling out today for GPT-6.1 Sol in the API, Codex, and ChatGPT Work", dated October 9, 2026. Only the title was seen.

The §9 raw-text-confirmation statement did not hold for the SDK "tag 1.79.0" claim (022). The limitations of 007 and 025 said that footnote or method text was unavailable or unreviewed, but that text is on the cited pages.
