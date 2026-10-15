# DeepSeek (009) — provisional dated source-query and inclusion audit, 2026-10-16

> **Provisional source-lead screen (upgraded 2026-10-16):** this search log, the [report](009-deepseek.md), the [event ledger](009-deepseek.events.csv) and the [source-QC note](009-deepseek.source-qc-2026-10-16.md) are **provisional, AI-assisted documentary source leads**. They are **unreviewed by a qualified human**; factual/link, source-access/rights and methods review are **pending**. Merging is not scientific or security sign-off; issue [#75](https://github.com/MSKazemi/github-trending-1000-study/issues/75) was closed on maintainer instruction (2026-10-16) with these review gates still open — reopen it if review finds a defect.

**Window:** 2026-04-12…2026-10-12 inclusive. **Research/source inspection:** 2026-10-16 (single session; per-query UTC times not recorded). **Provenance:** a general web-search tool (provider-ranked results; totals not exposed; 6 queries used under a shared budget), direct reading of official DeepSeek pages ([news index](https://deepseek.com/en/news/), [API news](https://api-docs.deepseek.com/news/news260910/), [API change log](https://api-docs.deepseek.com/updates), [pricing](https://api-docs.deepseek.com/quick_start/pricing)), read-only GitHub REST API calls on the `deepseek-ai` organisation (repository list, licences, releases, security advisories) and read-only Hugging Face model API calls for `deepseek-ai` (createdAt, lastModified, gated, licence tag). **This is not exhaustive internet discovery.** Result totals and excluded-hit denominators are **unknown**, not zero. No snapshots or hashes stored. The earlier screen had no search log (its queries were labelled "reproduction suggestions", not executed queries).

## Official index screens (one read each on 2026-10-16)

| Index | In-window items seen | Notes |
|---|---|---|
| [deepseek.com/en/news](https://deepseek.com/en/news/) | 2 news (Apr 24, Sep 10); research index lists the V4 technical report as "June 24, 2026" | `www.deepseek.com/*` answered HTTP 302 to chat.deepseek.com; bare host answered 200 |
| [API docs news sidebar](https://api-docs.deepseek.com/news/news260910/) | 4 (2026/04/24, 08/13, 08/21, 09/10) | All opened |
| [API change log](https://api-docs.deepseek.com/updates) | 5 (Apr 24, Jul 31, Aug 13, Aug 21, Sep 10); none after Sep 10 | Sep 10 entry contradicts Sep 10 news page on `deepseek-v4-pro` routing |
| GitHub `orgs/deepseek-ai/repos` (100, sorted by created) | 12 repos created in window | Licences via API; star counts not used as evidence |
| Hugging Face `api/models?author=deepseek-ai` (40 newest) | 22 repos created in window (incl. 12 small draft models on Jun 28) | createdAt ≠ public-announcement date |

## Query / fetch log by segment

| Segment | Exact query or fetch | Pages opened and decision | Counts |
|---|---|---|---|
| Apr 12–30 | fetch [V4 preview news](https://deepseek.com/en/news/v4-preview/), [API news 260424](https://api-docs.deepseek.com/news/news260424/) | QC of CI-009-01; new CI-009-15 (Jul 24 alias retirement notice) | n/a |
| Apr 12–30 | HF API `models/deepseek-ai/DeepSeek-V4-Pro`, `-V4-Flash` | CI-009-05 (MIT tag; created Apr 22) | n/a |
| Apr 12–30 | fetch [arXiv 2606.19348](https://arxiv.org/abs/2606.19348) | CI-009-04; date conflict recorded | n/a |
| Apr 12–30 | GitHub API: `TileKernels` (created Apr 22, MIT), `awesome-deepseek-agent` (Apr 27, no licence) | **Not included** (kernel library mentioned only in report; list repo low relevance) | n/a |
| May | web search `DeepSeek May 2026 announcement` | Prediction-market pages, a third-party pricing tracker ("May 5 plan added", costbench.com) and generic explainers — **excluded** (non-authoritative; tracker unverified against official pricing) | unknown |
| May | web search `DeepSeek V4 security evaluation OR ban OR investigation 2026 Reuters` | Opened [FAR.AI May 11](https://www.far.ai/blog/security-stress-test-deepseek-v4-pros-safeguards) → CI-009-07 (E0, unfinished page). AP-syndicated "fails security tests" stories concern earlier models — **excluded** (pre-V4, duplicates). No Reuters item returned | unknown |
| May | web search `NIST CAISI evaluation DeepSeek V4 2026` (domain nist.gov) | Opened [CAISI evaluation, May 1](https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro) → CI-009-06. Sep 2025 CAISI report — **excluded** (pre-window) | unknown |
| May | GitHub API: DeepGEMM releases; `clangd-ascend` | CI-009-08 (tag May 13), CI-009-09 (May 28) | n/a |
| June | GitHub API `DeepSpec`; HF API `DeepSeek-V4-Pro-DSpark` + model card | CI-009-10, CI-009-11. DeepGEMM tag Jun 2 folded into CI-009-08 | n/a |
| July | fetch [API change log](https://api-docs.deepseek.com/updates); HF API `DeepSeek-V4-Flash-0731` | CI-009-14 (Jul 31 public beta). DeepGEMM tag Jul 20 folded into CI-009-08. Jul 24 retirement execution **not verified** | n/a |
| August | fetch [API news 260813](https://api-docs.deepseek.com/news/news260813/), [260821](https://api-docs.deepseek.com/news/news260821/), change log | QC CI-009-02; new CI-009-12 (same event, changelog detail), CI-009-16 | n/a |
| August | web search `DeepSeek Harness agent open source launch August 2026`; fetch [TechNode Aug 14](https://technode.com/2026/08/14/against-claude-cowork-deepseek-opens-its-open-source-harness-to-developers/); GitHub API `deepseek-harness` (README, releases, advisories); fetch [deepseek.com/harness](https://deepseek.com/harness) | CI-009-13. Other results (oodaloop, forklog, kocpc, hyper.ai, amplifying.ai, pasqualepillitteri.it, runtimewire, thenote.app) **not opened** — aggregators/relays of the same launch, conflicting star counts | unknown |
| September | fetch [API news 260910](https://api-docs.deepseek.com/news/news260910/), [bare-host news](https://deepseek.com/en/news/deepseek-v4-1-flash/), [pricing](https://api-docs.deepseek.com/quick_start/pricing), [arXiv 2609.19969](https://arxiv.org/abs/2609.19969); HF API `DeepSeek-V4.1-Flash` | QC CI-009-03; new CI-009-17, -18, -19 (contradiction) | n/a |
| September | web search `DeepSeek Huawei Ascend DeepGEMM-Ascend open source September 2026`; GitHub API `DeepGEMM-Ascend`, `DeepEP-Ascend`, `DeepSelect`, `DeepJIT`, `deepseek-recipe` | CI-009-20, -21, -22. [TechRadar article](https://techradar.com/pro/huawei-and-deepseek-release-open-source-ai-tools-in-a-bid-to-lower-nvidia-exposure-but-will-programmers-make-the-switch) fetched but body not returned (boilerplate only) — **not used**. Machine-translated/aggregator pages (kucoin, aireiter, toolnavs, letsdatascience, aicybr) **excluded**; claims about a 128-chip "supernode" and Ascend 950 scope **unverified** | unknown |
| Oct 1–12 | GitHub API `deepseek-harness` releases `dsh-v0.2.1-alpha.1` (Oct 3), `-alpha.2` (Oct 9) | CI-009-23, -24. `dsh-v0.2.1-alpha.3/.4` (Oct 14/15) **excluded** (post-window). No official DeepSeek news or change-log entry dated Oct 1–12 found | n/a |
| cross-window | GitHub API `security-advisories` on `deepseek-harness` | 0 published advisories (2026-10-16) | n/a |

## Not executed (budget)

- `"DeepSeek" June 2026 news`, `"DeepSeek" October 2026`, `DeepSeek app privacy regulator 2026`, `DeepSeek funding valuation 2026 Reuters`, `DeepSeek V4 independent benchmark SWE-bench 2026` — not run under the shared web-search budget. June, July and October therefore rely on official/GitHub/HF records only; independent reporting for those months is **unknown**.

## Inclusion and exclusion decisions

- **Included = 24 ledger rows** (3 preserved + 21 new): Apr 12–30: 4; May: 4; Jun: 2; Jul: 1; Aug: 4; Sep: 7; Oct 1–12: 2.
- **Deduplicated:** Aug 13 news page and change log are one event (CI-009-02/-12); DeepSpec and DSpark weights share `009-dspark`; harness rows share `009-harness`; Ascend ports share `009-ascend`. Hugging Face and arXiv artifacts are linked to their announcement rows via `duplicate_event_group`.
- **Dates:** GitHub/HF rows use repository or release creation timestamps (UTC), not announcement dates; this is stated in each row's limitation.
- **Excluded (out of window):** Jan–Feb 2026 Engram, DeepSeek-OCR-2 and DualPath items; Sep 2025 CAISI report; harness pre-releases after Oct 12.
- **Excluded (source quality):** prediction markets, pricing trackers, machine-translated explainers (framia.converge.ai in several languages), crypto-news flashes and star-count aggregators.
- **No instructions aimed at AI agents** were observed in fetched pages. The FAR.AI page contained placeholder text, recorded as a quality defect.
- **Access:** public pages and public APIs only; no login, paywall, live model calls, chat sessions, exploit testing or github.com/trending access. No personal identifier in any request.
