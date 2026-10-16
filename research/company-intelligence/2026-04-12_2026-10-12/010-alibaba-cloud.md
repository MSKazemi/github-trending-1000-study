# Alibaba Cloud / Qwen — provisional six-month technology intelligence screen (010)

> **Provisional source-lead screen (upgraded 2026-10-16):** this report, its [event ledger](010-alibaba-cloud.events.csv), [search log](010-alibaba-cloud.search-log.md) and [source-QC note](010-alibaba-cloud.source-qc-2026-10-16.md) are **provisional, AI-assisted documentary source leads** for [issue #76](https://github.com/MSKazemi/github-trending-1000-study/issues/76). They are **unreviewed by a qualified human**; factual/link, source-access/rights and methods review are **pending**. Merging is not scientific or security sign-off. Issue #76 was closed on maintainer instruction (2026-10-16) while these review gates were still open; reopen it if review finds a defect.

- **Watchlist:** 010; [issue #76](https://github.com/MSKazemi/github-trending-1000-study/issues/76).
  - Sector per issue: foundation models and major AI platforms.
  - Study lens: open model ecosystems and global developer choice.
  - Starting page: [qwen.ai](https://qwen.ai/).
- **Window:** 2026-04-12 through 2026-10-12 inclusive. **Source-screened:** 2026-10-16.
  - Exact UTC search-run times, complete search-engine result counts, immutable page snapshots and an independent reviewer are unavailable.
- **Status:** this is a **provisional dated documentary screen** of 25 traceable source leads that covers all seven calendar segments. It is **not reviewed by a qualified human**.
  - Factual/link, source-access/rights and methods review are pending.
  - It does not provide independently verified task outcomes, exhaustive retrieval or human-approved scientific completion.
  - See the [event ledger](010-alibaba-cloud.events.csv), the [segment queries and inclusion/exclusion log](010-alibaba-cloud.search-log.md) and the [study method](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md).
- **Official sources checked:**
  - [QwenCloud model-release changelog](https://docs.qwencloud.com/changelog/models)
  - the [Alibaba Cloud Community blog tag index](https://community.alibabacloud.com/tags/type_blog-tagid_39251) and individual blog pages
  - one [press release](https://www.alibabacloud.com/en/press-room/alibaba-announces-comprehensive-full-stack-ai?_p_lc=1)
  - [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) GitHub releases, tags and compares
  - the npm registry record for `@qwen-code/qwen-code`
  - Hugging Face model cards and `LICENSE` files
  - the GitHub Advisory Database
- **Claim grading:** company-watch E0–E4, not the separate [2027 lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md).

## 1. Discovery, coverage and exclusions

The upgrade replaced the earlier five-row shortlist with structured official indexes.

**Official indexes:**

| Index | In-window content | Rows selected | Rule |
|---|---|---|---|
| QwenCloud changelog | 54 dated entries | 9 | Selected because they are coding/agent-relevant Qwen models or dated snapshots. |
| npm registry for Qwen Code | 75 stable versions (9/9/11/14/17/13/2 across the seven segments) | 7 | Each selected version has readable release notes or a compare. |
| Alibaba Cloud Community tag index | 16 in-window posts | — | Discovery only. |

**Other sources:**
- One trade-press report (eWeek) gives independent secondary coverage of the Qwen3.8 licence split.
- One GitHub Advisory Database record covers Qwen-Agent.

The 25 rows are a **purposive selection**. Absence from the ledger is not evidence that nothing else shipped.

**Not found, and recorded as unknown rather than zero:**
- **Lingma (Tongyi Lingma):** no in-window English-language source. Chinese-language sources were not searched.
- **Qoder:** the [changelog page](https://qoder.com/changelog) rendered no dated entries. Its footer names "BRIGHT ZENITH PRIVATE LIMITED" as operator and does not mention Alibaba.
- **Qwen Code security advisory:** none found.
- **Alibaba Cloud outage post-mortem:** not searched.
- **Reuters:** not reachable. Reuters coverage of a reported Qwen revenue-share plan appeared only via an aggregator and was **excluded as unverified**.

**Out of window and excluded:**
- Pre-window: Qwen3.6-Plus (Apr 2) and Qwen3-Coder (Jul 2025).
- Post-window: none were recorded.

## 2. Corporate/product identity and rights baseline

**Corporate entities:**
- Alibaba Cloud is the cloud business of **Alibaba Group**.
- Qwen is Alibaba's model family and brand. Pages are authored as "Qwen Team" or "Alibaba Cloud Community".
- QwenCloud (`qwencloud.com`, docs at `docs.qwencloud.com`) is the global AI-native platform launched in Singapore on **May 26, 2026** (CI-010-03). Model Studio (Bailian) is the older model-serving platform.
- Filing-level ownership was **not checked**. SEC EDGAR was skipped because it requires a contact identifier in requests.
- Qoder's corporate link to Alibaba is **unresolved** at the source level. Qoder is named as an Alibaba-adjacent "AI Work Assistant" example in the Qwen licences below.

**Licences, as read 2026-10-16 from GitHub `license.spdx_id`, Hugging Face card metadata and `LICENSE` files:**
- [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) (Qwen Code CLI, about 28.5k stars, a popularity signal only) is **Apache-2.0**.
- [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) is **Apache-2.0**.
- [Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B), [Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B) and [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) are tagged **apache-2.0**.
- [Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next/blob/main/LICENSE) uses the custom **Qwen Community License 1.0**.
- [Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/blob/main/LICENSE) uses the custom **Qwen3.8-Max License**.

**What the two custom licences require:** a licensee that runs a "Model as a Service" or an "AI Work Assistant" business (defined as an AI coding/office assistant, with Qoder and QwenWork named as examples) must obtain a **separate licence** for commercial use.
- Under the Community License this applies regardless of revenue.
- Under the Max License it applies once revenue exceeds USD 50M in 12 months.
- Both licences carry a model-name display duty above 100M MAU or USD 20M monthly revenue.

Vendor pages call these releases "open-source". The licences are **not OSI-approved** and specifically constrain coding-assistant products. This is the single most consequential rights finding for this study. **It is not legal advice; a human reviewer must read the full texts.**

**Model families:** Qwen3.6-Max-Preview, Qwen3.7-Max and Qwen3.8-Max are described as **closed-weight / proprietary** API models. Hosted APIs carry separate service terms, region and plan limits, which were not checked.

## 3. Seven-segment dated chronology

| Period | In-window source evidence (displayed / changelog / release dates) | Availability and attribution limits |
|---|---|---|
| Apr 12–30 | [Apr 17 Qwen3.6-35B-A3B open weights](https://www.alibabacloud.com/blog/qwen3-6-35b-a3b-thinking-open-weights-uncompromised-agentic-coding_603043) (-01)<br>Apr 20 qwen3.6-max-preview (-06)<br>[Apr 22 Qwen Code v0.15.0](https://github.com/QwenLM/qwen-code/releases/tag/v0.15.0) (-07)<br>Apr 23 qwen3.6-27b (-08) | -01's page still mixes "coming soon" and API wording. The changelog lists the hosted model on Apr 16. |
| May | [May 20 full-stack press release](https://www.alibabacloud.com/en/press-room/alibaba-announces-comprehensive-full-stack-ai?_p_lc=1) (-09)<br>[May 21 Qwen3.7-Max](https://qwen.ai/blog?id=qwen3.7&locale=en) (-02; [mirror](https://www.alibabacloud.com/blog/qwen3-7-the-agent-frontier_603154))<br>[May 21 Qwen Code v0.16.0](https://github.com/QwenLM/qwen-code/releases/tag/v0.16.0) (-10)<br>[May 27 Singapore Skills portal](https://www.alibabacloud.com/blog/alibaba-cloud-brings-full-stack-ai-ecosystem-to-global-customers-for-the-agentic-era_603186) (-11)<br>[May 28 Qwen Cloud launch](https://www.alibabacloud.com/blog/603191) (-03; event May 26) | Qwen3.7-Max was "available soon" on May 20. The changelog lists it on May 21, yet the May 21 article still says API "coming soon". -11's page date (May 27) conflicts with its index date (Jun 22). |
| June | Jun 1 qwen3.7-plus (-12)<br>Jun 10 qwen3.7-max-2026-06-08 snapshot adds vision (-13)<br>[Qwen Code v0.18.0, npm Jun 12](https://github.com/QwenLM/qwen-code/compare/v0.17.0...v0.18.0) (-14) | No first-party blog post about coding was found in June. Only an interview (Jun 26) was listed and it was not opened. |
| July | [Qwen Code v0.20.0, npm Jul 19](https://github.com/QwenLM/qwen-code/compare/v0.19.0...v0.20.0) (-15)<br>Jul 25 qwen3.7-flash (-16)<br>[Jul 31 Qwen Code v0.21.2](https://github.com/QwenLM/qwen-code/releases/tag/v0.21.2) (-17) | The hardware-ecosystem post was excluded because of a date conflict and because it is off-lens. |
| August | Aug 3 qwen3.8-max (-18)<br>Aug 13 qwen3.8-2.4t-a95b open weights under a custom licence (-19)<br>[Aug 17 eWeek licence report](https://www.eweek.com/news/alibaba-qwen3-8-27b-license-apac-china/) (-20)<br>[Aug 27 Qwen3.8-Flash-Next](https://www.alibabacloud.com/blog/qwen-3-8-flash-next-a-new-architecture-towards-ultimate-cost-efficiency_603501) (-04)<br>[Aug 28 Qwen-Agent SSRF advisory](https://github.com/advisories/GHSA-h9q8-qvr9-h4c6) (-21) | Release dates for Qwen3.8-27B conflict: Aug 5 (HF repo created), Aug 14 (eWeek) and Aug 19 (changelog). The advisory is unreviewed and lists no patched version. |
| September | Sep 2 qwen3.8-max-0902 "stronger coding" snapshot (-22)<br>[Qwen Code v0.23.0, npm Sep 3](https://github.com/QwenLM/qwen-code/compare/v0.22.0...v0.23.0) (-23)<br>[Sep 25 Apsara roadmap](https://www.alibabacloud.com/blog/alibaba-clouds-2026-apsara-conference-full-stack-ai-roadmap-along-with-global-market-expansion-plan_603598) (-05; same event family as the [Sep 22 roadmap article](https://www.alibabacloud.com/blog/alibaba-unveils-roadmap-on-full-stack-ai-strategy-from-chips-cloud-infrastructure-models-to-agents_603589)) | Qwen 4 is "in training". Regions and chips are planned. |
| Oct 1–12 | [Oct 8 Joe Tsai open-source position](https://www.alibabacloud.com/blog/joe-tsai-open-source-is-europes-ai-opportunity_603620) (-25)<br>[Oct 11 Qwen Code v0.25.1](https://github.com/QwenLM/qwen-code/releases/tag/v0.25.1) (-24) | The Kubernetes runtime is labelled experimental. qwen-image-2.1 (Oct 2/9) was excluded as off-lens. |

**Per-segment ledger counts:** 4 / 5 / 3 / 3 / 5 / 3 / 2. Rows -06, -08, -12, -13, -16, -18, -19 and -22 have no link in the table above because they all cite the [QwenCloud changelog](https://docs.qwencloud.com/changelog/models).

**Date fields in the ledger:**
- `published_utc` is the displayed page date, the changelog date, the GitHub `published_at` value, or the npm publish time.
- `event_date_utc` is left blank. Where a source states a distinct event date (CI-010-03: May 26), the date is given in the text instead.

## 4. Feature, rights and security cross-check

| Evidence cluster | What the cited documents support | Non-equivalence or counterexample |
|---|---|---|
| **Licence regime by model** (-01, -08, -04, -19, -20) | 2026 Qwen open weights use at least three regimes: Apache-2.0 (3.6-35B-A3B, 3.6-27B, 3.8-27B), Qwen Community License 1.0 (3.8-Flash-Next) and the Qwen3.8-Max License (2.4T-A95B). | "Open-source" in vendor copy does not mean OSI open source. The custom licences restrict coding-assistant and MaaS businesses. A repository that swaps model checkpoints can change its legal position without any code change. |
| **Hosted API vs article wording** (-01, -02, -09, -11) | The changelog lists hosted models on dates that precede or contradict "coming soon" wording in launch articles. | No API call was exercised. Region (Singapore vs China) and plan matter. The listing date is not the same as general availability. |
| **Snapshot pinning** (-12, -13, -16, -22) | Models are published as dated snapshots (e.g. `qwen3.7-max-2026-06-08`, `qwen3.8-max-0902`) under stable family names. | The behaviour of a family alias changes over time. Experiments must pin the snapshot ID. Deprecation policy was not read. |
| **Qwen Code CLI cadence** (-07, -10, -14, -15, -17, -23, -24) | Apache-2.0 terminal agent with 75 stable npm versions in 6 months. Features include hooks/ACP, MCP, subagents, multi-provider presets (MiniMax, xAI), automated PR review/triage, bounded autofix, `/verify`, a daemon/web shell and a managed Kubernetes runtime. | High churn means upkeep cost for anyone pinning it. v0.23.0 **relaxed** two policies (public-only extension network policy; trusted-loopback API access), and the security impact was not assessed. Release notes are PR lists, not tested behaviour. Many versions have no GitHub release page. |
| **Agent framework security** (-21) | GHSA-h9q8-qvr9-h4c6 / CVE-2026-82268 reports an SSRF in the Qwen-Agent document parser through 0.0.34. | The advisory is unreviewed and lists no patched version. Qwen-Agent has no repository advisory. Prevalence and exploitation are unknown. It is a separate project from Qwen Code. |
| **Platform/tool exposure** (-03, -11) | Qwen Cloud entry points are Skills, a CLI and a website. A Skills portal exposes 60+ cloud products as MCP-compatible tools. | Tool exposure enlarges the agent permission surface. No independent security or rights review was found. |
| **Vendor benchmarks** (-02, -04, -22) | SWE-Verified 80.4 and Terminal-Bench 69.7 (Qwen3.7-Max). For Flash-Next: about 1/9 the training compute, plus prefill/decode speedups. | All are vendor-reported. Task sets and contamination checks were not reviewed. **No energy or CO2e conclusions can be drawn.** |

## 5. Publicly stated direction versus shipped functionality

| Dated first-party source | Company-stated intention (paraphrase; short quotes) | Current research classification |
|---|---|---|
| [May 20 press release](https://www.alibabacloud.com/en/press-room/alibaba-announces-comprehensive-full-stack-ai?_p_lc=1) | Qwen3.7-Max "will be available soon" worldwide. | **Realised per vendor index**: the changelog lists it May 21, and Singapore access is stated May 27. |
| [Aug 27 Flash-Next](https://www.alibabacloud.com/blog/qwen-3-8-flash-next-a-new-architecture-towards-ultimate-cost-efficiency_603501) | The architecture is an "early preview" of Qwen4. | **Announced direction**. Qwen4 has not shipped. |
| [Sep 25 Apsara](https://www.alibabacloud.com/blog/alibaba-clouds-2026-apsara-conference-full-stack-ai-roadmap-along-with-global-market-expansion-plan_603598) | Qwen 4 "in training". Qwen 4.5/5 at 5–10T parameters. First regions in Türkiye, Finland and the Netherlands within 12 months. >20 GW by 2032. Zhenwu V900 in Q1 2027. | **Announced only.** Some agent products (AgentCore, Agent Security Center, Agent Context) are announced with their shipped status unclear. |
| [Sep 22 roadmap](https://www.alibabacloud.com/blog/alibaba-unveils-roadmap-on-full-stack-ai-strategy-from-chips-cloud-infrastructure-models-to-agents_603589) | Qwen3.8-Max improved via "automated self-improvement runs". Qwen-Image 3.1 "later this year". | Vendor claim / planned. |
| [Oct 8 Joe Tsai](https://www.alibabacloud.com/blog/joe-tsai-open-source-is-europes-ai-opportunity_603620) | AI companies should open-source their work. Open weights support sovereignty. | **Position statement**, in tension with the restrictive custom licences on two August open-weight releases. |

A public intention is not a scheduled delivery.

## 6. Conditional 2027–2031 outlook (analyst hypotheses, not company strategy)

| Testable scenario | Rival explanation | Disconfirming observation |
|---|---|---|
| Licence bifurcation (Apache small models, restricted large/efficient models) continues, so reuse decisions must be made per checkpoint. | The custom licences are a one-off. Future releases revert to Apache-2.0. | Qwen 4 open weights ship under Apache-2.0 with no MaaS/AI-assistant clause. |
| Fast-churning open agent CLIs (Qwen Code) become reusable components rather than products to rebuild. | Release velocity creates breaking-change and security upkeep that outweighs reuse. | A pinned version fails a frozen task suite after a minor upgrade, or needs more maintainer minutes than a minimal in-house script. |
| Dated model snapshots make hosted-model experiments reproducible. | Snapshots are deprecated too quickly for 30/90-day replication. | A snapshot used in a preregistered task is withdrawn before follow-up. |

## 7. M1–M7 study relevance

| Construct | Prospective measurement, not inferred conclusion |
|---|---|
| **M1** coding practice | Record agent CLI version, model snapshot ID and provider for every opt-in task. A release is not adoption. |
| **M2** accepted task quality | Independently authored acceptance tests count all attempts. Vendor SWE-bench scores are not study outcomes. |
| **M3** discovery | Stars (about 28.5k for qwen-code) and press are excluded as usefulness evidence. |
| **M4** verified third-party reuse | Trace one consented downstream use of a Qwen checkpoint or Qwen Code, with the licence checked. |
| **M5** reuse-first | Compare an existing Apache-2.0 checkpoint/CLI with a custom-licence checkpoint. Licence eligibility is a hard gate. |
| **M6** lifecycle cost | Maintainer upgrade minutes under a 75-releases-per-six-months cadence, plus inference spend where billed. **No token-to-CO2e conversion.** |
| **M7** actionable interventions | A licence-and-snapshot pinning checklist for model-swapping repos, tested on a frozen task. |

## 8. One falsifiable reuse-first maintainer experiment

**Target:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study), using only committed offline synthetic fixtures (e.g. `tests/fixtures/trending.html`). Live Trending `capture` stays **disabled** under the source-access decision.

**Practice under test:** before any model is used to assist a maintenance task, a pinned **"model provenance card"** is added and checked in CI. The card lists the checkpoint or snapshot ID, the licence SPDX or custom-licence name with its commercial-use clauses, the provider region and the agent CLI version. This reuses existing tooling: Hugging Face card metadata and npm/GitHub release metadata via a short script. It builds no new framework.

**Preregister before running:**
- **Frozen task set:** 10 synthetic maintenance tasks. Examples: add a field to the parser output schema with tests, or fix a deliberately broken fixture assertion. Each task has hidden acceptance tests authored by someone other than the agent operator.
- **Arm A:** Qwen Code at a pinned version, with an Apache-2.0 open-weight checkpoint (Qwen3.6-27B or Qwen3.8-27B) served locally.
- **Arm B:** the same CLI with a hosted snapshot (e.g. `qwen3.8-max-0902`).
- **Arm C:** no agent (human only).

**Primary endpoint:** independently accepted tasks out of all assigned tasks, counting refusals, failures and timeouts in the denominator.

**Secondary endpoints:**
- reviewer minutes and rework
- reproducibility, measured by re-running the same snapshot after 30 days
- a licence-gate failure count: tasks where the provenance card flags an ineligible licence
- billed inference cost where available

**Stop rule:** drop model assistance if any of these occur:
- an ineligible or unclear licence is found
- a snapshot is withdrawn before replication
- the accepted rate is no better than arm C
- the reviewer and upkeep burden exceeds arm C

**Expected null:** model assistance may give **no improvement**. If so, preserve that result. **No trial has been executed and no effects have been estimated.**

## 9. Evidence quality, limitations and release checklist (2026-10-16)

**Inventory:**
- 25 CSV rows: 5 preserved and 20 new.
- Tiers: 17 at E2 (dated changelog, release, registry, licence file or advisory record) and 8 at E1 (first-party prose). None is E3 or E4.
- Rows built on the same changelog URL are not independent of each other.

**Source QC (see [QC note](010-alibaba-cloud.source-qc-2026-10-16.md)):**
- All 5 original rows were confirmed on date and claim.
- The CI-010-02 canonical URL is unrenderable, but its content was confirmed via a first-party mirror.
- Four `limitation` fields were refined. No status was corrected.

**Dated conflicts preserved:**
- **Qwen3.7-Max:** the May 21 article says "coming soon" while the changelog lists it on May 21.
- **Article -11:** the page shows May 27 and the index shows Jun 22.
- **Qwen3.8-27B:** dated Aug 5 (HF repo creation), Aug 14 (eWeek) and Aug 19 (changelog).
- **Hardware article:** the page shows Jul 10 and the index shows Jul 31; the article was excluded.

**Unknowns:**
- Lingma and Qoder in-window activity and Qoder ownership
- Chinese-language sources
- Model Studio release notes
- outage and incident history
- filing-level ownership
- exercised API availability by region
- full licence legal reading
- downstream adoption

**Pending:**
- human factual/link spot-check
- licence/rights review
- methods review
- a real, preregistered, independently accepted task trial

**News corpus:** no `NEWS-YYYY-NNNN` IDs were created for the [#56 news corpus](https://github.com/MSKazemi/github-trending-1000-study/issues/56). Any cross-link must wait for human verification of the individual articles.

**Concrete maintainer action:** never refer to a model only by family name. Pin the checkpoint or snapshot ID, record its licence (including custom-licence clauses for AI coding assistants) and the agent CLI version. Gate the use in CI with the same frozen acceptance tests used for a no-agent baseline.

## Earlier screen (preserved)

The previous version of this file came from the following commits on `main`:

| Commit | Date | PR | Description |
|---|---|---|---|
| 7cfcabf | 2026-10-12 | — | Initial screen |
| d0ce524 | 2026-10-13 | — | Dated provider-claim audit |
| 35dbf0d | 2026-10-14 | — | First-party recheck |
| f443d7d | 2026-10-14 | PR #207 | Integration |

The full texts are in git history.

**What the earlier screen contained:**
- It was an "INITIAL screened research DRAFT" with **five E1 first-party rows** (CI-010-01…05).
- It left June, July and Oct 1–12 as "Not documented in this limited screen; not a finding of no releases".
- It stated that search counts and queries were not preserved. Its suggested queries were "next-pass suggestions, not claims that each exact expression was executed".

**Its key qualified claims, all re-confirmed on 2026-10-16:**
- The Apr 17 Qwen3.6 article contains contradictory "available" versus "coming soon" API wording.
- Qwen3.7-Max: the [May 20 press release](https://www.alibabacloud.com/en/press-room/alibaba-announces-comprehensive-full-stack-ai?_p_lc=1) said "coming soon". The [QwenCloud changelog](https://docs.qwencloud.com/changelog/models) and the [community index](https://community.alibabacloud.com/tags/type_blog-tagid_39251) date it May 21, so the CSV date was corrected from May 20 to May 21 in PR #207.
- The [May 28 Qwen Cloud post](https://www.alibabacloud.com/blog/603191) describes a May 26 event.
- The Sep 25 Apsara roadmap labels Qwen 4 "in training" and the regions "planned".

**What the earlier screen left unresolved, now partly resolved:**
- It flagged the [qwen.ai Qwen3.7 article](https://qwen.ai/blog?id=qwen3.7&locale=en), the [Aug 27 Flash-Next article](https://www.alibabacloud.com/blog/qwen-3-8-flash-next-a-new-architecture-towards-ultimate-cost-efficiency_603501) and the [Sep 25 Apsara article](https://www.alibabacloud.com/blog/alibaba-clouds-2026-apsara-conference-full-stack-ai-roadmap-along-with-global-market-expansion-plan_603598) as unrenderable or reader errors. The latter two now render. The qwen.ai page still does not, and its content was verified via a mirror.
- Its open question about Qwen3.6 licence and model-card terms is now partly answered: the card is tagged Apache-2.0, and Flash-Next uses a custom licence.

**Its maintainer experiment:** pinned small-model assistance for explaining parser fixture output, with blind reviewer acceptance. It is superseded by §8, which keeps the same reuse-first logic and adds licence/snapshot gating.

The earlier text described the change as a draft PR and gave a review-gate instruction. That instruction is replaced by the banner above, following the maintainer's 2026-10-16 decision.
