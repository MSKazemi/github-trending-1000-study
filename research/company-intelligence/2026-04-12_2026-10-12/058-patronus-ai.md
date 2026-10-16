# Patronus AI — provisional six-month technology intelligence screen (058)

> **Provisional source-lead screen (2026-10-16):** this report, its [event ledger](058-patronus-ai.events.csv) and [search log](058-patronus-ai.search-log.md) are **provisional, AI-assisted documentary source leads**. They have **not been reviewed by a qualified human**. Factual/link review, source-access/rights review and methods review are all **pending**. This screen is not scientific or security sign-off and does not close [issue #126](https://github.com/MSKazemi/github-trending-1000-study/issues/126).

- **Watchlist:** 058; [issue #126](https://github.com/MSKazemi/github-trending-1000-study/issues/126). Study lens: verification and reliability testing (LLM evaluation and testing, per the watchlist's indicative offering, which this screen found to be **out of date**; see section 2).
- **Window:** 2026-04-12 through 2026-10-12 inclusive. **Sources screened on 2026-10-16.** Exact UTC search-run times, full search-result counts, immutable page snapshots and an independent reviewer are not available.
- **Status:** **provisional dated documentary screen (13 traceable source records across six of the seven calendar segments; nothing verifiable found for Apr 12–30).** Not reviewed by a qualified human. Factual/link, source-access/rights and methods review are pending. These records are not independently verified task outcomes, not exhaustive retrieval and not a human-approved scientific result. See the [event ledger](058-patronus-ai.events.csv), the [segment queries and inclusion/exclusion log](058-patronus-ai.search-log.md) and the [study method](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md).
- **Official sources checked:** [Patronus AI homepage](https://www.patronus.ai/), [blog index](https://www.patronus.ai/blog), [press page](https://www.patronus.ai/press), [research page](https://www.patronus.ai/research), [products](https://www.patronus.ai/products), [company](https://www.patronus.ai/company), [DWM preview page](https://patronus.ai/dwm), the [PyPI `patronus` SDK](https://pypi.org/project/patronus/), the public `patronus-ai` GitHub organization (read through the GitHub REST API) and the `PatronusAI` Hugging Face organization (read through the Hugging Face API). **Not accessible:** `docs.patronus.ai` redirects to `/docs`, which returned HTTP 401 on 2026-10-16. No login was attempted. **Claim grading** uses the company-watch E0–E4 tiers, not the separate [2027 lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md).

## 1. Discovery, coverage and exclusions

The [search log](058-patronus-ai.search-log.md) records 12 executed web queries, one query that was **not executed** because the session's web-search budget ran out, and every page or API record opened. It also records the include/exclude decisions. Search-result totals are **unknown**, not zero.

Coverage by segment:

| Segment | Ledger rows | Notes |
|---|---:|---|
| Apr 12–30 | 0 | Unknown, not "no activity". No dated item was found. The only April 2026 arXiv item on the research page (2604.03677, submitted 2026-04-04) is out of window, and its arXiv page does not mention Patronus. |
| May | 2 | |
| June | 3 | |
| July | 2 | |
| August | 2 | |
| September | 3 | |
| Oct 1–12 | 1 | |

The ledger is a **purposive documentary screen**. It is not a census of company activity, not a measure of how fast the company ships, and not independent replication.

## 2. Corporate/product identity and rights baseline

**Entity:** the site footer names **Patronus AI, Inc.** The company page lists Anand Kannappan (co-founder and CEO) and Rebecca Qian (co-founder and CTO). [TechCrunch (2026-06-25)](https://techcrunch.com/2026/06/25/patronus-ai-lands-50m-to-build-digital-worlds-that-stress-test-ai-agents/) reports that the company was founded in 2023 by former Meta AI researchers and is based in San Francisco. No parent company, acquisition or rename was found. Ownership was **not checked at filing level**. A search result surfaced an unrelated "Patronus" AI-companion startup. That page was not opened, and the result was excluded as a name collision.

**Offering drift (important for the study lens):** issue #126 describes the offering as "LLM evaluation and testing". As of 2026-10-16, the [homepage](https://www.patronus.ai/) describes "a research lab developing training data and simulated environments for frontier AI". The [products page](https://www.patronus.ai/products) lists only *Tasks*, *Environments* and *Research*, and does **not** mention the earlier evaluation products (Percival, Lynx, Glider, evaluators, tracing). The evaluation SDK is still being published: [`patronus` 0.1.26 was uploaded to PyPI on 2026-09-17](https://pypi.org/project/patronus/). However, the SDK's declared source repository (`github.com/patronus-ai/patronus-py`) returned 404 and the docs returned 401 on 2026-10-16. **When the repositioning happened is unknown.** An archive snapshot from 2026-04-13 exists but could not be opened with the available tool. The repositioning may predate the window (Generative Simulators was announced 2025-12-17, outside the window). Treat the current site as a snapshot taken on 2026-10-16, not as a dated in-window event.

**Rights:** licenses vary by artifact and must be checked one artifact at a time:

- `mdlm_world_modeling` code: Apache-2.0.
- `world_model_corpus`: tagged MIT.
- FigmaTrace dataset and model: tagged CC-BY-4.0.
- `trace-dataset` (out of window): CC-BY-SA-4.0.
- SpeedrunBench dataset: license "other". It is gated, research and evaluation use only, and the commercial game footage remains with its rights-holders.
- `speedrun_bench` repository: **no license**.
- `supertux-speedrun` and `tuxemon-speedrun`: GPL-3.0.
- `kimi-k3-nvfp4` weights: upstream Kimi-K3 terms.
- The hosted DWM preview: no terms or pricing found.

## 3. Seven-segment dated chronology

| Period | In-window source evidence (displayed source dates) | Availability and attribution limits |
|---|---|---|
| Apr 12–30 | **None verifiable** | Unknown, not zero. The 2026-04-04 arXiv item is excluded as out of window. |
| May | [May 7 MDLM world-model preprint v1](https://arxiv.org/abs/2607.16204v1) with [Apache-2.0 code](https://github.com/patronus-ai/mdlm_world_modeling); [May 19 HalluWorld](https://arxiv.org/abs/2605.19341) | The 2607 arXiv identifier conflicts with the May 7 v1 submission date, so the first public date is unresolved. HalluWorld's Patronus affiliation is **unverified**: only the Patronus research page lists it. |
| June | [Jun 12 v3 of the unified-hallucination position paper](https://arxiv.org/abs/2512.21577) (ICML poster on Jul 8); [Jun 25 Series B blog and Digital World Model preview](https://www.patronus.ai/blog/announcing-our-50m-series-b), with [TechCrunch](https://techcrunch.com/2026/06/25/patronus-ai-lands-50m-to-build-digital-worlds-that-stress-test-ai-agents/) the same day | The DWM is a **preview**, and its benchmark lead is **self-reported**. The funding round and the "15x revenue" figure are company or investor claims. Channel Insider (Jun 29) and Pulse 2.0 (Jun 26) cover the **same event** and were deduplicated. |
| July | [Jul 8 GLM-5.2 NVFP4 post-training note](https://www.patronus.ai/blog/getting-glm-5-2-nvfp4-post-training-off-the-ground); [Jul 29 `kimi-k3-nvfp4` weights](https://huggingface.co/PatronusAI/kimi-k3-nvfp4) | This is an engineering note, not a product. The forks it names, and the tooling repository linked from the model card, were not public or not found on 2026-10-16. |
| August | [Aug 20 FigmaTrace](https://www.patronus.ai/blog/figmatrace-a-comprehensive-training-dataset-for-figma-design-workflows); [Aug 26 `supertux-speedrun`](https://github.com/patronus-ai/supertux-speedrun) (with `tuxemon-speedrun` on Aug 30) | Repository dates are GitHub `created_at` values, not announcements. |
| September | [Sep 3 SpeedrunBench](https://www.patronus.ai/blog/introducing-speedrunbench-a-challenging-benchmark-for-frontier-agents); [Sep 17 SDK 0.1.26](https://pypi.org/project/patronus/); [Sep 30 `speedrun_bench` repository](https://github.com/patronus-ai/speedrun_bench) | The dataset is gated and not commercial. The harness has no license. No SDK release notes were located. |
| Oct 1–12 | [Oct 7 preprint v2, "Accepted to NeurIPS 2026"](https://arxiv.org/abs/2607.16204v2) | The acceptance is an author comment. NeurIPS listings were not checked. The `speedrun_bench` push on Oct 14 is **excluded** as out of window. |

**Dating rules used in the [CSV](058-patronus-ai.events.csv):**

- Blog post pages show no date, so blog dates come from the blog index (Jul 8, Aug 20, Sep 3, Jun 25).
- Repository and model dates are registry creation timestamps, which are not confirmed public-visibility dates.
- `event_date_utc` is blank unless a source names a distinct event date. Two rows have one: the ICML poster on 2026-07-08 and the PyPI upload on 2026-09-17.

## 4. Feature, rights and verification cross-check

| Evidence cluster | What the cited document supports | Non-equivalence or counterexample |
|---|---|---|
| [DWM preview](https://patronus.ai/dwm) and [MDLM paper](https://arxiv.org/abs/2607.16204v1) | Vendor-described diffusion world models that generate tool-use environments from schemas, rules and steering directives. The paper reports a GRPO framework with **deterministic state checks**. | Generated environments are **simulations**. Whether they predict real agent behaviour is untested here. No independent coverage that was screened tested it either: the Channel Insider and TechCrunch pieces relay company and investor claims. Benchmark leadership is self-reported. |
| [HalluWorld](https://arxiv.org/abs/2605.19341) and the [position paper](https://arxiv.org/abs/2512.21577) | Hallucination defined against a fully specified reference world, with automatic labels in gridworld, chess and terminal settings. The authors report that state tracking remains hard. | Patronus's authorship is **unverified**: neither arXiv nor ICML names it. Treat these as adjacent research, not as company output. |
| [SpeedrunBench](https://www.patronus.ai/blog/introducing-speedrunbench-a-challenging-benchmark-for-frontier-agents) and its [harness](https://github.com/patronus-ai/speedrun_bench) | Frame-count scoring with deterministic headless forks of GPL games. | Gated dataset. Seven of the ten titles are commercial. The harness has no license. The results are vendor-reported. |
| [FigmaTrace](https://www.patronus.ai/blog/figmatrace-a-comprehensive-training-dataset-for-figma-design-workflows) | 3,469 expert design trajectories plus an SFT model, both public under CC-BY-4.0 tags. | Consent and terms for the recorded human workflows were not reviewed. The model gains come from the vendor or a third-party listing. |
| [NVFP4 note](https://www.patronus.ai/blog/getting-glm-5-2-nvfp4-post-training-off-the-ground) | Detailed engineering negatives: an entropy-bonus reward collapse and an optimizer warm-start bug. | One run per arm. The forks it names were not visible publicly. |
| [SDK 0.1.26](https://pypi.org/project/patronus/) | The package is still released, with OpenTelemetry dependencies. | The source repository returned 404 and the docs returned 401. Maintenance and changelog cannot be inspected, which is a **reuse risk signal**. |

## 5. Publicly stated direction versus shipped functionality

| Dated first-party source | Company-stated intention (<=25 words quoted) | Classification |
|---|---|---|
| [Series B blog, 2026-06-25](https://www.patronus.ai/blog/announcing-our-50m-series-b) | "expand our research organization, accelerate GTM, and invest in the compute and infrastructure required to train and serve Digital World Models at scale" | **Announced intention.** No dated milestones. |
| [TechCrunch, 2026-06-25](https://techcrunch.com/2026/06/25/patronus-ai-lands-50m-to-build-digital-worlds-that-stress-test-ai-agents/) | The article says current markets are software engineering and finance, with broader use planned. | **Reported plan.** The customer claim ("virtually every frontier AI lab") comes from an investor and is unverified. |
| [DWM preview page](https://patronus.ai/dwm) | Interactive environments generated on demand through one API, with the customer's own model, reward and training backend. | **Preview.** No GA, pricing or terms were found. |

Patronus's statements of intent describe what it plans to do. They do not guarantee delivery, and they are not evidence of its 2027–2031 strategy.

## 6. Conditional 2027–2031 outlook (analyst hypotheses, not company statements)

| Testable scenario | Rival cause | Disconfirming observation |
|---|---|---|
| Vendors move from post-hoc LLM-output evaluation toward generated RL environments with programmatic verifiers | Repositioning driven by funding and buyer mix (frontier labs), not technical superiority | Evaluation and tracing products reappear as the primary offering, or the DWM preview is withdrawn |
| Deterministic state checks and reference-world labels become a reusable verification pattern for agent tasks | Existing unit tests, property tests and hidden acceptance tests already provide equivalent signal | Matched tasks show no extra defect detection from world-model checks over plain hidden tests |
| Simulated environments reduce the cost of agent reliability testing | Simulation-to-reality gap produces misleading passes | Agents that pass simulated tasks fail matched real-application tasks at similar or higher rates |

## 7. M1–M7 study relevance

| Construct | Prospective measurement (not an inferred conclusion) |
|---|---|
| **M1** coding-workflow change | Dated evidence that a verification vendor moved toward RL-environment and data supply. This shows availability, not adoption. |
| **M2** accepted task quality | Hidden, independently authored acceptance tests versus vendor-style simulated checks on the **same** tasks. All attempts count. |
| **M3** discovery | Funding and press coverage are attention signals, not usefulness. Do not treat them as an outcome. |
| **M4** verified third-party reuse | Trace one consented downstream use of an Apache, MIT or CC-BY artifact. Hugging Face and GitHub counts are not reuse. |
| **M5** reuse-first | Licensing varies by artifact (GPL, no license, gated "other", CC-BY-SA), and the SDK source is unreachable. A license and provenance gate is required before any reuse. |
| **M6** lifecycle human/energy cost | NVFP4 and simulation claims are **not** energy evidence. Measure only instrumented CI or runtime energy. **No token-to-CO2e conversion.** |
| **M7** actionable interventions | Test whether adding a cheap deterministic test-tampering check improves maintainers' detection of reward-hacked agent patches (section 8). |

## 8. One falsifiable reuse-first maintainer experiment

**Target:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study), using offline synthetic fixtures only. The live Trending `capture` stays **disabled** under the source-access decision.

**Question:** Patronus's research agenda (TRACE reward-hack detection, out of window, plus the in-window deterministic state checks) suggests that agent patches can "pass" by gaming tests. Does a **reused, simple deterministic diff rule** catch seeded test-tampering patches as well as a more expensive LLM-judge review?

**Frozen task set:**

- 20 synthetic patches to existing `trending_study` modules: 10 legitimate fixes and 10 seeded "reward hacks", such as deleting or weakening an assertion, skipping a test, or special-casing a fixture value.
- Labels are authored and sealed by a human who is independent of both arms.
- Every patch stays in the denominator.

**Comparators:**

- **A (reuse-first):** the existing `python -m unittest` suite plus a short rule that flags any diff touching `tests/`, removing `assert*` lines or adding `skip` decorators.
- **B:** A plus an LLM-judge review of each diff, run through a subscription subagent. No paid API is added to project scripts. TRACE-style contrastive prompting is allowed, but the CC-BY-SA `trace-dataset` is **not** vendored without a license review.

**Endpoints:**

- **Primary:** detection of seeded hacks (true positives out of 10) and false alarms (out of 10).
- **Secondary:** reviewer minutes per patch, plus disagreement with the sealed labels.

**Stop rule:** adopt B only if it detects at least 3 more of the 10 hacks than A **and** raises at most 1 extra false alarm, with less than 5 added reviewer-minutes per patch. Otherwise keep A. A null or negative result is preserved. **No trial has been executed, and no effect is estimated or claimed.**

## 9. Evidence quality, uncertainties and review checklist

- **Observed or shipped (documentary E2):** the MDLM code and corpus, the FigmaTrace dataset and model, the SpeedrunBench gated dataset and harness, the GPL game forks, the `kimi-k3-nvfp4` weights, and SDK 0.1.26. These are artifacts that exist, not verified quality.
- **Preview or claims only:** the Patronus-DWM preview and its benchmark lead; the funding, revenue-growth and customer claims; NeurIPS acceptance (author comment).
- **Unverified attribution:** the HalluWorld paper and the position paper (Patronus is not named on arXiv or ICML).
- **Contradictions and limits:**
  - The arXiv 2607 identifier conflicts with the May 7 v1 date.
  - Aggregators disagree on total funding and valuation ($70M per TechCrunch; other figures were seen only in search snippets and are excluded).
  - Press-release dates vary between Jun 25 and Jun 26.
  - Blog post pages carry no dates.
  - The docs were inaccessible (401), and the SDK repository returned 404.
- **Missing:**
  - April 12–30 events (unknown, not zero).
  - Independent technical evaluation of any Patronus artifact.
  - Customer-verified adoption.
  - Filing-level ownership.
  - Archive snapshots showing when the site repositioned.
  - Complete search-hit counts.
  - The final arXiv-wide query, which was not run because the web-search budget ran out.
- **Pending:** a human factual/link spot-check, source-access and rights review (especially the gated and unlicensed artifacts), methods review, and any real opt-in experiment. **Issue #126 was closed on maintainer instruction (2026-10-16); this screen alone is not scientific completion — reopen it if factual, rights or methods review finds a defect.**
