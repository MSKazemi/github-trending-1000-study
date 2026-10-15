# DeepSeek — provisional six-month AI/software company intelligence screen (009)

> **Provisional source-lead screen (upgraded 2026-10-16):** this report, its [event ledger](009-deepseek.events.csv), [search log](009-deepseek.search-log.md) and [source-QC note](009-deepseek.source-qc-2026-10-16.md) are **provisional, AI-assisted documentary source leads**. They are **unreviewed by a qualified human**; factual/link, source-access/rights and methods review are **pending**. Merging is not scientific or security sign-off; issue [#75](https://github.com/MSKazemi/github-trending-1000-study/issues/75) was closed on maintainer instruction (2026-10-16) with these review gates still open — reopen it if review finds a defect.

- **Watchlist ID:** 009; [issue #75](https://github.com/MSKazemi/github-trending-1000-study/issues/75).
- **Window:** 2026-04-12 to 2026-10-12 inclusive (calendar publication dates). **Source-screened:** 2026-10-16.
- **Status:** **provisional dated documentary screen — 24 traceable source leads covering all seven calendar segments**; not exhaustive retrieval, not independently verified task outcomes, not human-approved scientific completion.
- **Official channels checked:** [news index](https://deepseek.com/en/news/), [API news](https://api-docs.deepseek.com/news/) (sidebar), [API change log](https://api-docs.deepseek.com/updates), [pricing](https://api-docs.deepseek.com/quick_start/pricing), [GitHub deepseek-ai](https://github.com/deepseek-ai), [Hugging Face deepseek-ai](https://huggingface.co/deepseek-ai), [DeepSeek Harness](https://deepseek.com/harness).
- **Method:** [company-source protocol](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md) (E0–E4 company-watch tiers); [M1–M7 mission](../../../docs/AI_ERA_CODING_REUSE_RESEARCH_MISSION.md). Claim grading is not the separate [2027 lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md).

## 1. Discovery, coverage and exclusions

The [search log](009-deepseek.search-log.md) records the official index reads, six web searches (shared budget), read-only GitHub and Hugging Face API calls, and queries **not executed**. The previous screen's statement that May, June, July and early October had no documented event is **superseded**: each now has dated official or artifact records. Coverage remains purposive. Machine-translated explainers, prediction markets, pricing trackers and star-count aggregators were excluded; independent reporting for June, July and October is **unknown** (queries not run), not absent.

## 2. Identity and rights baseline

- **Entity:** the API documentation footer reads "Copyright © 2026 DeepSeek, Inc."; the GitHub organisation is `deepseek-ai` and arXiv papers are authored as "DeepSeek-AI". Parent company, ownership and jurisdictional structure were **not verified** to filing level in this screen.
- **Host behaviour:** on 2026-10-16 every tested `https://www.deepseek.com/...` path answered HTTP 302 to `chat.deepseek.com`, while the same paths on `https://deepseek.com/...` answered 200 (QC note). Links in this report use whichever form was reachable; the ledger keeps original URLs.
- **Open-weight licences (Hugging Face metadata, not LICENSE text):** DeepSeek-V4-Pro, V4-Flash, V4-Flash-0731, V4-Pro-0813, V4-Pro-DSpark, V4-Flash-Vision-Exp and V4.1-Flash are tagged `license:mit` and not gated. The V4 `-Base` checkpoints and the twelve small Jun 28 draft models carry **no** licence tag in the API listing.
- **Code licences (GitHub API `license.spdx_id`, 2026-10-16):** MIT for [deepseek-harness](https://github.com/deepseek-ai/deepseek-harness), DeepSpec, DeepSelect, DeepJIT, DeepGEMM, DeepGEMM-Ascend, TileKernels, FlashMLA, DeepEP, 3FS and deepseek-recipe; MPL-2.0 for dsh-libreoffice-kit; **no licence detected** for DeepEP-Ascend and awesome-deepseek-agent; NOASSERTION for clangd-ascend. An "open-source" label does not substitute for a detected licence.
- **API service terms, data-retention and regional restrictions** were not reviewed; they matter more than weight licences for hosted-API use.

## 3. Seven-segment dated chronology

| Segment | In-window source evidence (ledger IDs) | Availability / attribution limits |
|---|---|---|
| Apr 12–30 | [V4 Preview, Apr 24](https://deepseek.com/en/news/v4-preview/) (-01); [HF V4-Pro/Flash weights, MIT tag](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) (-05); [legacy alias retirement notice](https://api-docs.deepseek.com/news/news260424/) (-15); [V4 technical report](https://arxiv.org/abs/2606.19348) (-04) | "Preview" but live API; arXiv dateline Apr 26 conflicts with ID prefix 2606 and DeepSeek's "June 24" index date |
| May | [NIST CAISI evaluation, May 1](https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro) (-06); [FAR.AI stress test, May 11](https://www.far.ai/blog/security-stress-test-deepseek-v4-pros-safeguards) (-07); DeepGEMM tag (-08); clangd-ascend repo (-09) | Two independent evaluations; FAR.AI page looks unfinished (E0) |
| June | [DeepSpec](https://github.com/deepseek-ai/DeepSpec) (-10); [V4-Pro-DSpark](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-DSpark) (-11) | Same checkpoint plus speculative-decoding module; dates are repository creation |
| July | [Change log Jul 31: V4-Flash public beta + Responses API](https://api-docs.deepseek.com/updates) (-14); scheduled Jul 24 retirement of `deepseek-chat`/`deepseek-reasoner` (event date on -15) | Retirement execution not verified |
| August | [V4-Pro GA, Aug 13](https://api-docs.deepseek.com/news/news260813/) (-02, -12 same event); [DeepSeek Harness preview](https://github.com/deepseek-ai/deepseek-harness) (-13); [V4-Flash-Vision-Exp, Aug 21](https://api-docs.deepseek.com/news/news260821/) (-16) | Pricing announced Aug 13, effective Aug 16 16:00 UTC; harness is developer preview |
| September | DeepSelect/DeepJIT (-22); [V4.1-Flash, Sep 10](https://www.deepseek.com/en/news/deepseek-v4-1-flash/) (-03; reachable at [bare host](https://deepseek.com/en/news/deepseek-v4-1-flash/)); [V4.1-Flash weights](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash) (-18); **conflicting** change-log statement on V4-Pro (-19); [V4.1-Flash report](https://arxiv.org/abs/2609.19969) (-17); [DeepGEMM-Ascend](https://github.com/deepseek-ai/DeepGEMM-Ascend) (-20); [DeepEP-Ascend](https://github.com/deepseek-ai/DeepEP-Ascend) (-21) | V4-Pro reroute plan contradicted by change log and current pricing page |
| Oct 1–12 | [dsh-v0.2.1-alpha.1, Oct 3](https://github.com/deepseek-ai/deepseek-harness/releases/tag/dsh-v0.2.1-alpha.1) (-23); [alpha.2, Oct 9](https://github.com/deepseek-ai/deepseek-harness/releases/tag/dsh-v0.2.1-alpha.2) (-24) | Pre-releases; Oct 14/15 pre-releases excluded (post-window); no official news item found Oct 1–12 |

## 4. Feature map and integration surface

| Cluster | Supported by cited documents | Non-equivalence / counter-evidence |
|---|---|---|
| Models: V4-Pro, V4-Flash → V4-Flash-0731 → V4.1-Flash; Vision-Exp | 1M context, thinking/non-thinking modes, effort levels low/high/max, open weights (MIT tag) | Benchmark claims vendor-reported; [CAISI](https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro) found self-reported scores higher than its own |
| API compatibility | OpenAI ChatCompletions and Anthropic formats (Apr 24); native OpenAI Responses API for Codex (Jul 31/Aug 13); Files API for images (Aug 21) | Format compatibility ≠ behavioural equivalence; not tested here |
| Aliases and routing | Legacy `deepseek-chat`/`deepseek-reasoner` retirement after Jul 24; `deepseek-v4-flash` → V4.1-Flash; `deepseek-v4-pro` reroute plan | Change log says V4-Pro continues; pricing page lists V4-Pro-0813 — **a model name is not a stable treatment label** |
| Pricing | Peak/off-peak (off-peak 50%) from Aug 16; further price change Sep 10 | List prices only; no metered per-task cost |
| Agent tooling | [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness): plugin architecture (Cordis), web UI via `npx @deepseek-ai/dsh web`, experimental Claude Code Mods layer, Git-worktree plugin, AGENTS.md loading | Developer preview with explicit breaking-change warning; translation plugin may send content to third-party services |
| Inference infrastructure | DeepSpec + DSpark speculative decoding, DeepSelect, DeepJIT, DeepGEMM, TileKernels; Ascend ports | Hardware-specific; DeepSpec default target cache ~38 TB; DeepEP-Ascend has no detected licence |

## 5. Stated direction versus shipped

| Dated first-party statement | Stated intention | Classification |
|---|---|---|
| [Apr 24 V4 Preview](https://deepseek.com/en/news/v4-preview/) | Retire legacy aliases after Jul 24 | Announced; execution unverified |
| [Jul 31 change log](https://api-docs.deepseek.com/updates) | Official V4-Pro release to follow | Delivered Aug 13 (vendor-reported GA) |
| [Sep 10 V4.1-Flash](https://deepseek.com/en/news/deepseek-v4-1-flash/) | Phase out V4-Pro; route to V4.1-Flash until a V4.1-Pro launches; work with OSS community on inference support | V4.1-Pro **not observed** by Oct 12; reroute **contradicted** by change log (CI-009-19) |
| [deepseek.com/harness](https://deepseek.com/harness) | Global testing, parallel open-sourcing | Preview; no stable release by Oct 16 |
| Ascend repositories (Sep 29–30) | Non-NVIDIA hardware support | Code published; scope claims in secondary press unverified |

## 6. Conditional 2027–2031 outlook (analyst hypotheses, not company commitments)

| Hypothesis | Rival explanation | Disconfirming observation |
|---|---|---|
| MIT-tagged open weights plus OpenAI/Anthropic-compatible endpoints lower switching cost for routine repository tasks | Alias churn, regional/data terms and output differences dominate | A pinned-model replay fails frozen acceptance tests more often than the incumbent, or migrations need ongoing adapter work |
| Plugin-style harnesses converge on shared conventions (AGENTS.md, Mods-like APIs) | Each vendor's harness stays incompatible | The same AGENTS.md task gives materially different behaviour across harnesses |
| Hardware-diverse kernel ports widen self-hosting options | Ports stay unlicensed, unmaintained or hardware-locked | No downstream project imports the Ascend ports within 12 months |

## 7. M1–M7 mapping

| Question | Observation needed (not inferred here) |
|---|---|
| M1 agent workflow | Opt-in, version-pinned use of Harness/Responses-API workflows; availability ≠ adoption |
| M2 accepted quality | Frozen external acceptance tests; CAISI shows self-reported vs independent gaps |
| M3 discoverability | Star counts reported for the harness conflict and are not evidence |
| M4 verified reuse | Audited downstream imports of DeepGEMM/DeepSpec/harness plugins |
| M5 reuse vs rebuild | Compare existing harnesses/libraries; check licence gaps (DeepEP-Ascend, clangd-ascend) |
| M6 lifecycle cost | Per-task billed tokens at peak/off-peak, migration minutes after alias changes; tokens ≠ kWh |
| M7 maintainer intervention | Pinned-model compatibility test below |

## 8. One falsifiable reuse-first maintainer experiment

**Repository:** [GitHub Trending 1000 Study](https://github.com/MSKazemi/github-trending-1000-study); offline synthetic fixtures only (live Trending capture remains disabled).

**Practice:** before adopting any provider model for a documentation/summary helper, reuse the existing deterministic CLI and add a **model-identity pin check** rather than new model-calling code.

- **A (comparator):** existing offline Python CLI, no model calls.
- **B (treatment):** same task through an OpenAI-compatible client against an explicitly pinned open-weight checkpoint (e.g. a Hugging Face revision hash), recording the resolved model identity, endpoint, response schema and billed tokens.
- **Frozen acceptance:** a second person writes 10 hidden fixture cases (exact expected JSON fields, rejection of invented fields) before any run; all assigned cases, refusals and timeouts stay in the denominator.
- **Verified external-use signal:** none expected; record "unknown" unless an outside user reproduces the task.
- **Cost cap:** 2 human hours and a fixed token budget; record reviewer minutes.
- **Stop rule:** drop B if it adds no accepted case over A, if the resolved model differs from the pin (cf. CI-009-03 vs CI-009-19), or if licence/data terms are unclear. Report nulls. **Not run.**

## 9. Evidence quality and limitations

- **Inventory:** 24 rows (3 preserved, 21 new): E2 = 15, E1 = 8, E0 = 1. Mostly first-party or artifact metadata; two independent evaluations (CAISI E2 because partly non-public benchmarks; FAR.AI E0).
- **Dates:** GitHub/Hugging Face dates are creation timestamps, not announcements; arXiv V4 date conflict unresolved.
- **Contradiction:** V4-Pro routing after Sep 14 is contradicted between official pages; unresolved without change-history or live test.
- **Not demonstrated:** benchmark validity, adoption, safety of the harness, per-task cost savings, energy/CO2e.
- **Pending:** human link/date spot-check, licence-text and API-terms review, independent methods review. Cross-link verified items to [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56) only after that review; no `NEWS-` IDs minted.

## Earlier screen (preserved)

The previous version (commits `b59ffe1` "source-graded DeepSeek six-month screen" and `5e97838` "source-check product status, license and reuse boundaries", issue #75; full text in git history) was an **initial source-screened draft** with three first-party rows: [DeepSeek V4 Preview](https://deepseek.com/en/news/v4-preview/) (Apr 24, preview with live API), [DeepSeek V4-Pro API](https://api-docs.deepseek.com/news/news260813/) (Aug 13, GA; pricing effective Aug 16 16:00 UTC) and [DeepSeek V4.1 Flash](https://www.deepseek.com/en/news/deepseek-v4-1-flash/) (Sep 10, V4.1-Flash live; V4-Pro alias reroute scheduled Sep 14 04:00 UTC). It named [api-docs.deepseek.com/news](https://api-docs.deepseek.com/news/) as the publication entry, marked May, June, July and Oct 1–12 as "no event documented" (unresolved coverage), listed suggested queries that were explicitly **not** a log of executed searches, and flagged that "DeepSeek's Sep 10 statement about V4-Pro retirement and current update guidance may conflict". Its 2026-10-13 recheck advised: "Do not use a shared alias as a stable model-treatment label." This upgrade confirms that conflict with dated evidence (CI-009-19), corrects the empty-month statements, and keeps all three original rows and event IDs.
