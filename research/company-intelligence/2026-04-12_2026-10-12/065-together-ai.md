# Together AI — provisional six-month technology intelligence screen (065)

> **PROVISIONAL / AI-ASSISTED — NOT HUMAN-REVIEWED (2026-10-16).** This report, its [event ledger](065-together-ai.events.csv) (40 rows) and its [search log](065-together-ai.search-log.md) are a first-pass documentary source screen prepared with AI assistance. No qualified human has checked the facts, links, rights or methods. Nothing here is a verified chronology, a product test, an adoption measure or a research finding. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

- **Company watchlist ID:** 065
- **Research issue:** [#133](https://github.com/MSKazemi/github-trending-1000-study/issues/133); news-corpus link: [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56) (no `NEWS-` IDs minted, because no item has had human review)
- **Ownership and product boundaries (as of 2026-10-12):** the website and services are operated by **Together Computer, Inc., a Delaware corporation**, per the [Terms of Service](https://www.together.ai/terms-of-service) (page dated "Updated May 19, 2026"). Privately held. No in-window acquisition, rename or parent-company change was found. Registry filings were **not** checked.
- **Product URL and official channels:** [together.ai](https://www.together.ai/), [blog](https://www.together.ai/blog), [press page](https://www.together.ai/press) (`/newsroom` returns 404), [docs changelog](https://docs.together.ai/docs/changelog), [deprecations](https://docs.together.ai/docs/deprecations), [status](https://status.together.ai/), GitHub [togethercomputer](https://github.com/togethercomputer).
- **Analysis window:** 2026-04-12 to 2026-10-12 inclusive; sources accessed 2026-10-16 UTC.
- **Researcher / factual reviewer / review date:** AI-assisted screen for the maintainer / **pending** / **pending**.
- **Status:** screened (provisional). Not independently checked or published as a finding.
- **Source coverage:** full sweep of the docs changelog, deprecations page, all 251 sitemap blog URLs (52 dated in-window), GitHub org/release metadata, and 12 web searches. A 13th search, for independent Moonshot partnership coverage, could not run because the search budget ran out. Paywalled NYT and The Information pieces were not read. Details are in the [search log](065-together-ai.search-log.md).

**Evidence grades** are the company-watch working tiers in the [method](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md): E0 lead, E1 first-party claim, E2 documentary/artifact, E3–E4 independent behaviour. No row reaches E3. The tiers are **not** the separate [evidence-to-lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md).

## 1. Search and inclusion audit

| Search run UTC | Site/engine | Full query and dates | Found | Screened | Included | Excluded/why | Coverage limitation |
|---|---|---|---:|---:|---:|---:|---|
| 2026-10-16 | docs.together.ai (curl) | `/docs/changelog`, all in-window headings | ~86 dated headings | all | 26 rows | routine model additions | mutable page, no archive as of Oct 12 |
| 2026-10-16 | together.ai sitemap (curl) | 251 `/blog/` URLs, `datePublished` filter | 52 in-window | 52 | 13 rows | research/marketing without product change; repeated DeepSWE posts | 6 undated pages ignored |
| 2026-10-16 | GitHub REST (`gh api`) | org repos; together-py, together-typescript, together-sandbox releases; Nutlope/togetherlink | 41 + 23 releases in-window | all | 1 row + checks | per-release notes not audited | metadata ≠ quality |
| 2026-10-16 | WebSearch | 12 exact queries (Q01–Q12 in log) | unknown | see log | 3 independent rows | aggregators, unverifiable leads | no hit counts; Q13 not run |

## 2. Verified company/product identity and baseline

Together AI sells **hosted inference for open-weight models**: serverless, batch, provisioned throughput, dedicated model inference and dedicated containers. It also sells fine-tuning/post-training, evaluations, GPU clusters (Kubernetes and Slurm), managed storage and a code sandbox. The [About page](https://www.together.ai/about-us) names the founders and leadership. Leadership includes Vipul Ved Prakash (CEO), Ce Zhang (CTO) and Tri Dao (Chief Scientist), plus founders Chris Ré and Percy Liang.

**Baseline before the window, for context only.** These items are not in-window evidence:
- the [CodeSandbox acquisition](https://www.together.ai/blog/codesandbox-acquisition-together-code-interpreter) (2024-12-12), which is the lineage of the 2026 sandbox SDK;
- the [Refuel.ai acquisition](https://www.together.ai/blog/together-ai-acquires-refuel-ai) (2025-05-15);
- the [$305M Series B](https://www.together.ai/blog/together-ai-announcing-305m-series-b) (2025-02-20);
- [Python SDK v2.0](https://www.together.ai/blog/together-python-sdk-2-0) (2025-12-12).

**Licences observed on 2026-10-16** (GitHub SPDX field): together-py **Apache-2.0**, together-typescript **Apache-2.0**, together-sandbox **MIT**, ParallelKernelBench **Apache-2.0**, togetherlink **MIT**. The togetherlink repo is under an individual account, not the company org. The hosted platform itself is proprietary. Open-weight model licences are set by each model's publisher, not by Together, and were not audited here.

## 3. Month-by-month discoveries

| Month | Announcements/changes (ledger IDs) | Primary URLs | Independent reporting | Notes or no-result limitations |
|---|---|---|---|---|
| 2026-04-12..30 | SDK v2.8.0 starts a 41-release run (001); deprecations (002); **Build Tiers retired, dynamic rate limits, prepaid billing** (003); DeepSeek-V4-Pro FP4 at 512K context (004); DOE Genesis Mission (005, E0); **Copy Fail kernel CVE response** (006); Adaption fine-tuning integration (007) | [changelog](https://docs.together.ai/docs/changelog), [Copy Fail post](https://www.together.ai/blog/shutting-down-copy-fail-in-production) | [NVD CVE-2026-31431](https://nvd.nist.gov/vuln/detail/CVE-2026-31431) confirms the CVE only | Genesis release unreadable (403) |
| 2026-05 | `tg` CLI v2.10 and a response-schema relaxation (008); deprecations plus a gemma-4 **price increase** (009); Pearl crypto "Proof of Useful Work" endpoint (010); vendor coding-agent inference benchmark (011); Terms updated (012); per-user OIDC for GPU clusters (013); **price increases** on Llama/Qwen SKUs (014) | changelog; [benchmark](https://www.together.ai/blog/coding-agent-benchmarks) | none found | benchmark page edited 2026-09-10 |
| 2026-06 | ISO 27001:2022 claim (015); multi-LoRA endpoints, preview (016); ParallelKernelBench (017); **conflicting deprecation dates** (018) | [ISO post](https://www.together.ai/blog/iso-27001-2022-certification), [PKB](https://www.together.ai/blog/parallelkernelbench) | none found | certificate not inspected |
| 2026-07 | **$800M Series C** (019, 020); Provisioned Throughput with 99% SLA (021); **TogetherLink "open-source launcher"** (022); Dedicated Model Inference (023); org privacy/training opt-in controls (024); YC GPU cluster (025); Kimi K3 vs Claude Fable 5 vendor benchmark (026); **Moonshot future-models commitment** (027) | [Series C](https://www.together.ai/blog/announcing-our-series-c), [Moonshot](https://www.together.ai/blog/together-ai-announces-strategic-partnership-with-moonshot-ai-to-natively-serve-kimi-models) | [TechCrunch 2026-07-01](https://techcrunch.com/2026/07/01/neocloud-together-ai-raises-800m-leaps-to-8-3b-valuation) | NYT DealBook paywalled; Moonshot coverage unscreened |
| 2026-08 | **IBM $240M B300 cluster, expected Q1 2027** (028); project-level resource isolation for all orgs (029); serverless withdrawals incl. Pearl and Kimi-K2.7-Code (030) | changelog | [StorageReview 2026-08-11](https://www.storagereview.com/news/ibm-and-together-ai-put-240m-into-a-dedicated-hgx-b300-inference-cluster-on-ibm-cloud), [IBM release syndicated](https://www.storagenewsletter.com/2026/08/14/ibm-and-together-ai-sign-multi-year-agreement-to-scale-open-source-ai-inference-with-nvidia-ai-infrastructure-on-ibm-cloud/) | trade press restates IBM release |
| 2026-09 | "Open Source AI Stack" positioning (031); preemptible GPUs at 50% (032); canary/blue-green rollouts and HIPAA placement, CLI v2.34.0 (033); deprecations with **date conflict** (034); **LoRA default-rank change that silently affects old SDKs** (035) | [OSS stack](https://www.together.ai/blog/the-open-source-ai-stack), [preemptible](https://www.together.ai/blog/introducing-preemptible-compute-the-same-compute-half-the-price) | none found | — |
| 2026-10-01..12 | **Together Link beta** for six coding agents via a hosted gateway (036); together-sandbox SDK on an allowlist (037); **dynamic rate limits retired** (038); Together Link launch claim of ">50%" savings (039); IBM cluster "first customer" claim (040) | [Together Link docs](https://docs.together.ai/docs/togetherlink), [launch post](https://www.together.ai/blog/together-link-frontier-quality-open-models-in-the-harness-you-already-use) | none found (search budget exhausted) | Oct 13 post-training and Oct 15 model items are **post-cutoff, excluded** |

## 4. Dated event evidence and capabilities

The [CSV](065-together-ai.events.csv) holds all 40 rows. Grades: E2 = 25, E1 = 14, E0 = 1. Statuses: shipped 20, reported_undetermined 12, preview 4, announced_only 2, reversed/cancelled 2. The rows below matter most for the study.

| Event ID | Published UTC / underlying event date | Claim or observed feature | Availability and limitations | Source link (type) | Independent check | E0–E4 working grade |
|---|---|---|---|---|---|---|
| CI2026-065-003 / -038 | 2026-04-22 / 2026-10-02 | Dynamic rate limits plus prepaid billing introduced, then dynamic limits **retired** after about five months | Policy churn; a Nov 2025 support article on Build Tiers was stale after April (snippet observation) | changelog (first-party doc) | none | E2 |
| CI2026-065-006 | 2026-04-30 | Fleet-wide disabling of `algif_aead` against Copy Fail; company says "containers are not a security boundary" | Self-reported response; page edited 2026-09-10 | blog | NVD confirms the CVE (published 2026-04-22) | E1 |
| CI2026-065-011 | 2026-05-19 | +31% TPS vs TensorRT-LLM; p50 TTFT 0.71 s vs 1.1 s (Kimi K2.5, B200) | Vendor-run, synthetic load; **body edited later** and no longer matches index teaser | vendor benchmark | none | E1 |
| CI2026-065-009 / -014 | 2026-05-14 / 2026-05-29 | Price **increases**, e.g. Llama-3.3-70B-Turbo $0.88 → $1.04 per 1M tokens | Contrary datapoint to "cheaper open models" framing | changelog | none | E2 |
| CI2026-065-017 | 2026-06-23 | 87-problem multi-GPU kernel benchmark; frontier LLMs solve under a third | Company-authored; artifact public (Apache-2.0) | research blog + repo | repo exists (GitHub API) | E2 |
| CI2026-065-018 / -034 / -002 | 2026-06-26, 2026-09-15, 2026-04-14 | Deprecation records **disagree** between the changelog and the history/scheduled tables | Exact removal dates unresolved | changelog vs deprecations page | internal cross-check only | E2 |
| CI2026-065-019 / -020 | 2026-07-01 | $800M Series C; company claims >$1.15B annual bookings and >500 MW of compute commitments | Funding ≠ adoption; bookings unaudited | blog + independent news | TechCrunch (same event) | E1 / E2 |
| CI2026-065-022 / -036 / -039 | 2026-07-15 / 2026-10-01 / 2026-10-05 | Together Link: launcher for Claude Code, Codex, OpenCode, Pi Code and desktop apps on Together models. With an Anthropic key, hard requests route to Claude Opus | **Three different "launch" dates**; requests go through a **hosted gateway**; MIT repo under an individual account; savings claim is price-based | changelog, docs, blog | repo metadata only | E2 / E1 |
| CI2026-065-026 | 2026-07-24 | Kimi K3 vs Claude Fable 5 on DeepSWE: pass@1 68.5% vs 69.9%; $4.65 vs $13.41 per rollout | Vendor sells the open model; not re-run | vendor benchmark | none | E1 |
| CI2026-065-027 | 2026-07-29 | Commitment to serve "every open weights model Moonshot ships going forward" | Future intention | blog | none (unscreened) | E1 |
| CI2026-065-028 / -040 | 2026-08-11 / 2026-10-06 | IBM: $240M multi-year B300 cluster, **expected Q1 2027**. Together: "first customer running on it" | Live status at Oct 6 unresolved | trade press of IBM release; vendor blog | StorageNewsletter syndication | E2 / E1 |
| CI2026-065-035 | 2026-09-29 | LoRA max rank raised to 128; SDKs before 2.36.0 (incl. 1.x) **silently use the new max** when `lora_r` is unset; batch files kept 7 days | Reproducibility hazard for pinned old clients | changelog | none | E2 |
| CI2026-065-037 | 2026-10-01 | together-sandbox SDK replaces the CodeSandbox SDK: Docker snapshots, ephemeral by default, Together API key | Allowlist only; isolation untested | changelog + repo | MIT licence via GitHub API | E2 |

**Cross-cutting observations (documentary, not behavioural):**
- **Model churn is the dominant change.** The deprecation-history table lists 29 serverless removals dated in-window. Kimi-K2.7-Code lasted about 2.5 months on serverless. The Pearl endpoint lasted about 3.5 months, and Inkling-Small about 6 weeks. The [policy](https://docs.together.ai/docs/deprecations) gives 2–3 weeks' notice for serverless and under 24 hours for preview models. It silently redirects "upgrades" only when the price rises by ≤10%.
- **Vendor benchmarks are frequent and mutable.** Several posts carry a `dateModified` later than publication. In one, the headline comparison changed after publication.
- **Agent-facing surface grew.** Together Link, the sandbox SDK, a public `skills` repo (MIT, created 2026-03-31, baseline) and dedicated-inference rollouts all target coding-agent workloads.

## 5. What the company says it intends to do

| Verbatim or close paraphrase of public direction (<=25 words per source quoted) | Link/date | Promised horizon | Status (planned, tentative, uncommitted) | Missing/contradictory context |
|---|---|---|---|---|
| Moonshot partnership extends "to every open weights model Moonshot ships going forward" | [2026-07-29](https://www.together.ai/blog/together-ai-announces-strategic-partnership-with-moonshot-ai-to-natively-serve-kimi-models) | open-ended | planned (commercial commitment) | depends on Moonshot releasing open weights; no independent confirmation screened |
| Commitments "for over 500 MW of compute capacity … to support our expected compute growth in the coming years" | [2026-07-01](https://www.together.ai/blog/announcing-our-series-c) | "coming years" | tentative; capital from new investors | no sites, dates or energy sourcing disclosed |
| IBM cluster "expected availability in Q1 2027" | [IBM release via StorageNewsletter, 2026-08-14](https://www.storagenewsletter.com/2026/08/14/ibm-and-together-ai-sign-multi-year-agreement-to-scale-open-source-ai-inference-with-nvidia-ai-infrastructure-on-ibm-cloud/) | Q1 2027 | planned | Together's Oct 6 post implies it is already running |
| Coding-agent benchmark: "This is version one. We'll update it as we build." | [2026-05-19](https://www.together.ai/blog/coding-agent-benchmarks) | none | uncommitted | the page was already rewritten in place rather than versioned |
| Open-model stack layers (model, inference, routers, harness, tools) are independent, so models can be swapped "in minutes" | [2026-09-09](https://www.together.ai/blog/the-open-source-ai-stack) | none | positioning, not a roadmap | marketing framing |

Do NOT read these as independent future facts.

## 6. Independent interpretation: direction and alternative scenarios (2027–2031, conditional)

| Hypothesis for 2027–2031 | Supporting observations | Rival explanations | Disconfirming signals | Confidence/unknowns |
|---|---|---|---|---|
| H1. Hosted open-weight inference vendors increasingly compete *inside existing coding-agent harnesses* (provider swap under Claude Code/Codex) rather than with their own IDE | Together Link (022/036/039), sandbox SDK (037), Moonshot day-zero deal (027) | Harness vendors may restrict third-party backends; the bridge may stay a niche cost tool | Harness ToS or API changes break the bridge; Together Link is dropped or stays beta past 2027 | low; no usage data |
| H2. Rapid model turnover makes **model-ID pinning and migration tests** a maintenance cost for downstream repos | 29 in-window serverless removals; inconsistent deprecation records (018/034); silent SDK default change (035) | Churn may slow as open-model releases consolidate; redirects may absorb most of the cost | Deprecation counts fall sharply in 2027; downstream repos report no migration work | medium for the documentary pattern; impact on downstream repos unmeasured |
| H3. "Cheaper than closed models" claims will rest on per-token prices rather than accepted-task outcomes | Benchmarks 011/026 and Together Link's ">50%" claim; contrary price rises (009/014) | Independent harness-level evaluations may appear | Neutral, reproducible task-level studies show equal accepted-task rates at the claimed cost ratios | medium; no independent study screened |
| H4. Capacity growth via third parties (IBM, investor-funded MW) raises lifecycle-energy questions that vendors will not quantify | 019, 028, 040; Pearl crypto offset (010), withdrawn after ~3.5 months | Vendors may publish energy or location data under regulation | Per-token energy or emissions disclosures with stated boundaries appear | unknown; **no energy data exists here** |

These are the researcher's hypotheses, not company strategy.

## 7. Implications for the GitHub 1000 study

| M1–M7 construct | Possible observable effect | Study design to test it | Negative/null explanation | Measurement boundary |
|---|---|---|---|---|
| **M1** AI coding-agent change | Agents run on swapped open-model backends inside unchanged harnesses | Opt-in comparison of the same harness with different backends on frozen tasks (section 8) | Harness, not model, drives outcomes | Opt-in maintainer sessions only; no third-party traces |
| **M2** accepted task quality | Claimed parity at lower price (026, 039) | Hidden human-authored acceptance tests; all assigned tasks in the denominator | Open model fails more often on long-horizon tasks | Vendor benchmarks excluded as evidence of quality |
| **M3** discoverability | Funding and press (019/020) raise visibility | Do not use press or stars as adoption proxies | Visibility without use | Press counts are not adoption |
| **M4** verified third-party reuse | Public artifacts (ParallelKernelBench, together-sandbox, togetherlink) | Trace consented downstream integrations, pinned to a commit | Stars and forks without working integrations | togetherlink has no tagged release to pin |
| **M5** package rights/security | Apache-2.0/MIT SDKs; proprietary hosted platform; hosted gateway data flow; ISO 27001 claim | Licence and data-flow review before any use; per-model licence check | Licence of the hosted service ≠ licence of the client | ISO certificate and DPA not inspected |
| **M6** lifecycle human/energy cost | Migration work from deprecations; SDK default changes; preemptible capacity; new data-centre capacity | Log migration minutes per deprecation notice; metered energy only if instrumented | Redirects make churn costless for most users | **No kWh/CO2e estimated or derivable from tokens** |
| **M7** actionable interventions | Pin model IDs and SDK versions; test that `lora_r` and similar defaults are set explicitly | Section 8 | Pinning adds maintenance without benefit | Single-maintainer pilot |

## 8. One practical, falsifiable change for the maintainer's own repositories

**Repository/component:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study), offline Python modules and tests only. The Trending `capture` command stays disabled, and nothing in this experiment touches it or any network collector.

**Candidate practice (not yet validated):** run the maintainer's existing coding-agent harness (Claude Code) against a **pinned open-weight backend through Together Link** for routine, well-specified maintenance tasks. Keep the current default backend for everything else. The open question is whether this preserves accepted-task quality at lower monetary cost without adding review work.

**Treatment/control and frozen comparable task:**
- **Task set:** freeze 12 small tasks before any run. Recreate them from already-closed issues at a pinned base commit: docs or schema fixes, a validator edge case, a unit-test gap. A human (not an agent) writes hidden acceptance tests for each task and keeps them out of the agent's workspace.
- **Arms:** each task runs once per arm, in randomized order.
  - Comparator A: Claude Code with its current default model.
  - Treatment B: the same Claude Code version via Together Link, pinned with `--main` to one named model.
  - The auto-router stays off and no Anthropic key is configured, so arm B is a single open model.
- **Pinned for both arms:** Claude Code, Together Link commit and model ID.
- **Accepted-task functional unit:** one task whose patch passes the hidden tests, `python3 -m unittest discover -s tests -v`, `scripts/check_research_artifacts.py`, and an independent human review with no requested changes.

**Measured human work:**
- prompt and steering minutes;
- reviewer minutes;
- rework rounds;
- support or debug minutes for Together Link setup and updates.

**Success and guardrails:**
- **Primary endpoint:** accepted tasks ÷ all 12 assigned tasks per arm. Refused, abandoned and timed-out tasks stay in the denominator.
- **Secondary endpoints:**
  - human minutes per accepted task;
  - provider-billed cost per accepted task, from the Together session receipt or `/billing/usage` and the Anthropic invoice;
  - test or validator regressions.
- **Data-flow guardrail:** requests transit Together's hosted gateway. Run tasks in a throwaway clone with no `.env`, tokens, `.claude/` memory or unpublished data, and read Together's data-retention settings (CI2026-065-024) before the first run.
- **Rights guardrail:** check the pinned model's licence.
- **Cost guardrail:** set a pre-agreed spend cap and record it.
- **Execution approval:** a paid third-party API is involved, so the maintainer must approve the trial first. Agent sessions are run by hand; no project script or pipeline calls a paid model API.
- **Arm labels:** keep them in a private local trial log. Commit metadata stays unchanged, with the maintainer as sole author.
- **Energy:** no energy or carbon figures unless electricity is actually metered; none is expected here.

**Stop/reversal rule:** stop and keep arm A if any of the following happens:
- any secret or unpublished file is exposed;
- the pinned model is deprecated or redirected mid-trial (record this as a lifecycle-cost observation);
- arm B's accepted-task count is lower than arm A's by 2 or more;
- arm B's median reviewer minutes per accepted task exceed arm A's;
- the spend cap is reached.

A null or negative result is a valid outcome and must be recorded as such. **No trial has been run and no effect is estimated.**

## 9. Findings, uncertainties and review outcome

- **Observed/shipped (documentary only):**
  - heavy serverless model turnover with inconsistent deprecation records;
  - two policy reversals: dynamic rate limits introduced in April, retired in October;
  - SDK/CLI release cadence of 41 Python releases in-window;
  - new agent-facing tools: Together Link beta and the sandbox SDK (allowlisted);
  - governance features: per-user cluster OIDC, project isolation, HIPAA placement, org privacy controls;
  - price increases on several SKUs alongside cuts on others.
- **Claims/announcements only:** cost multiples (6x–20x, >50%, up to 90%), benchmark wins, ISO 27001 scope, 400 trillion tokens/month, >$1.15B bookings, 500 MW commitments, Moonshot future-model commitment, IBM cluster timing.
- **Conjectures and unknowns:** section 6 hypotheses; real usage of Together Link; fidelity of FP4/INT8 served models against reference weights; data retention through the hosted gateway; any energy figures.
- **Important contradictory or null evidence:**
  - deprecation dates disagree across the changelog and the deprecations page (018, 034, 002);
  - Together Link has three launch dates;
  - IBM availability is given as Q1 2027 by IBM, while Together says it is already running on the cluster;
  - a vendor benchmark was rewritten after publication;
  - price increases contradict the cost narrative;
  - investor naming differs between sources;
  - "2.8T" vs "3T-class" framing for Kimi K3;
  - no independent provider-fidelity audit, incident post-mortem or user-outcome study was found. This is a search gap, not proof of absence.
- **Reviewer links and audit date:** none yet. Human factual/link spot-check, rights review and methods review are pending. The issue may be closed with this provisional status recorded, and those gates remain open.
