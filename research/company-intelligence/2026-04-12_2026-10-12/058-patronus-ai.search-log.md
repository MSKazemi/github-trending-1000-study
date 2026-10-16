# Patronus AI (058) — provisional dated source-query and inclusion audit, 2026-10-16

> **Provisional source-lead screen (2026-10-16):** this search log, its [report](058-patronus-ai.md) and [event ledger](058-patronus-ai.events.csv) are **provisional, AI-assisted documentary source leads**. They have **not been reviewed by a qualified human**. Factual/link review, source-access/rights review and methods review are all **pending**. This log does not close [issue #126](https://github.com/MSKazemi/github-trending-1000-study/issues/126).

**Window:** 2026-04-12 to 2026-10-12 inclusive. **Research and source inspection:** 2026-10-16.

**Method:** public web search through the agent search tool (US index; provider behaviour is opaque), direct page reads and public registry APIs. The registries were the GitHub REST API for the `patronus-ai` organization, the Hugging Face API for the `PatronusAI` organization, and the PyPI JSON API for `patronus` and `patronus-api`.

**Not done:** no login, no paywall bypass, no scraping of github.com/trending. Each included event is one row in [058-patronus-ai.events.csv](058-patronus-ai.events.csv).

**Not exhaustive:**

- Result totals, UTC run times and excluded-hit denominators are **unknown**, not zero.
- No byte hashes or snapshots of third-party pages were taken.
- One planned query was **not executed** because the session web-search budget was exhausted.

## Query log

The "Found/screened/excluded" counts are unknown for every row and are noted only where a row deviates.

| Date | Segment | Exact query (or direct source) | Pages/records opened and decision | Found/screened/excluded |
|---|---|---|---|---|
| 2026-10-16 | identity / all | `"Patronus AI" 2026` | Led to the [TechCrunch Jun 25 article](https://techcrunch.com/2026/06/25/patronus-ai-lands-50m-to-build-digital-worlds-that-stress-test-ai-agents/). Aggregators (jawlah.co, af.net, vcnewsdaily, benzatine, siliconvalleyinvestclub) were **excluded** as unverified or syndicated. Their total-funding and valuation figures conflict and are not used. | unknown |
| 2026-10-16 | identity / all | Direct: [homepage](https://www.patronus.ai/), [company](https://www.patronus.ai/company), [products](https://www.patronus.ai/products), `/pricing-archived` | The current positioning is "research lab developing training data and simulated environments". Eval products are not listed. The page carries no in-window date, so it is used as a 2026-10-16 baseline only, not as an event. | n/a |
| 2026-10-16 | all segments | Direct: [blog index](https://www.patronus.ai/blog) | In-window posts by index date: Jun 25, Jul 8, Aug 20, Sep 3. All four were **included**. Dec 17 2025 and earlier posts were **excluded** as out of window. Page 2 was not opened because page 1 already reaches 2025. | 9 posts on page 1; 4 in window |
| 2026-10-16 | all segments | Direct: [press page](https://www.patronus.ai/press) | Only the TechCrunch Jun 25 item is in window. It is used as the `independent_check_url` of the funding row, not as a separate event. | 1 in window |
| 2026-10-16 | all segments | Direct: [research page](https://www.patronus.ai/research) | Arxiv IDs suggesting 2026: 2607.16204 **included**; 2605.19341 **included with affiliation caveat**; 2601.20103 (TRACE, v1 Jan 27) and 2602.00352 (DETOUR, v1 Jan 30) **excluded** as out of window with a single version; 2604.03677 (v1 Apr 4) **excluded** as out of window, and its arXiv page does not mention Patronus. | 5 candidate 2026 items; 2 included |
| 2026-10-16 | May / Oct | Direct: [arXiv 2607.16204v1](https://arxiv.org/abs/2607.16204v1) and [v2](https://arxiv.org/abs/2607.16204v2) | v1 is dated 2026-05-07 and v2 2026-10-07 ("Accepted to NeurIPS 2026"). Both **included** as separate rows in one duplicate group. Flagged: the identifier prefix conflicts with the v1 date. | n/a |
| 2026-10-16 | May | `HalluWorld benchmark hallucination reference world models Patronus` | Opened [arXiv 2605.19341](https://arxiv.org/abs/2605.19341). **Included**, with the caveat that Patronus is not named on arXiv. A Patronus social post was seen only as a snippet and was not opened or cited. | unknown |
| 2026-10-16 | June / July | `"Patronus AI" ICML 2026 position paper hallucination definition` | Opened [arXiv 2512.21577](https://arxiv.org/abs/2512.21577) (v3 Jun 12) and the [ICML poster](https://icml.cc/virtual/2026/poster/67063) (Jul 8). **Included** as one row with the v3 date. v1 (Dec 2025) is out of window. Affiliation unverified. | unknown |
| 2026-10-16 | May | `"Patronus AI" May 2026` | No dated May vendor news was found. The May rows come from arXiv and registries. | unknown |
| 2026-10-16 | Apr 12–30 | `"Patronus AI" April 2026 announcement` | No in-window April item. A snippet of the patronus.ai/announcements page said its newest item is from 2024; the page was not opened. A different "Patronus" companion startup (aifunding.me snippet) was **excluded** as a name collision. | unknown; **0 included** |
| 2026-10-16 | June | `Patronus AI "Digital World Model" playground preview Patronus-DWM` | Opened the [Series B and DWM blog](https://www.patronus.ai/blog/announcing-our-50m-series-b) and the [DWM page](https://patronus.ai/dwm). **Included** as two rows: the DWM preview and the funding round. LinkedIn, nitter and digg results were **excluded**. | unknown |
| 2026-10-16 | June | `siliconangle Patronus AI Series B digital world models June 2026` | Opened [Channel Insider Jun 29](https://www.channelinsider.com/ai/patronus-agent-simulation-testing-funding/) and [Pulse 2.0 Jun 26](https://pulse2.com/patronus-ai-raises-50-million-series-b-to-build-digital-world-models/). Both are **deduplicated** as the same funding event: Pulse 2.0 is a press-release rewrite, and Channel Insider relays company claims with only an investor quote. No independent technical assessment was found in either. The HPCwire/BigDATAwire release returned **HTTP 403** (inaccessible). No SiliconANGLE URL was found. | unknown |
| 2026-10-16 | July | `"Patronus AI" news July 2026 OR August 2026` | No independent July or August news. The July rows come from the [blog](https://www.patronus.ai/blog/getting-glm-5-2-nvfp4-post-training-off-the-ground) and the [Hugging Face record](https://huggingface.co/PatronusAI/kimi-k3-nvfp4). The third-party "tear sheet" figures are **excluded** as unverifiable. | unknown |
| 2026-10-16 | Aug / Sep | `SpeedrunBench Patronus OR FigmaTrace Patronus` | Opened the [FigmaTrace blog](https://www.patronus.ai/blog/figmatrace-a-comprehensive-training-dataset-for-figma-design-workflows), the [SpeedrunBench blog](https://www.patronus.ai/blog/introducing-speedrunbench-a-challenging-benchmark-for-frontier-agents) and the [SpeedrunBench dataset card](https://huggingface.co/datasets/PatronusAI/speedrunbench). The plushcap and featherless mirrors are **excluded** as derivative. | unknown |
| 2026-10-16 | Sep / Oct | `"Patronus AI" agents environments September OR October 2026` | No independent September or October news. The older SD Times and SiliconANGLE Generative Simulators items (Dec 2025) are **excluded** as out of window. | unknown |
| 2026-10-16 | Sep | `Patronus AI Percival evaluation SDK changelog 2026`, plus the PyPI page and JSON | [PyPI `patronus`](https://pypi.org/project/patronus/): 0.1.26 uploaded 2026-09-17T12:22Z, **included**. 0.1.25 (Jan 9) is excluded as out of window. `patronus-api` has no 2026 release. The SDK repository URL returned 404 and `docs.patronus.ai/docs` returned HTTP 401, so both were inaccessible. | 1 included |
| 2026-10-16 | cross-window | `"Patronus AI" acquisition OR acquired OR partnership 2026` | No acquisition or partnership found. Datadog and Samsung are described only as investors. | unknown |
| 2026-10-16 | cross-window | GitHub REST API: `orgs/patronus-ai/repos`, plus per-repo metadata and contents | `mdlm_world_modeling` (created May 7, Apache-2.0) is used as the check URL for the May paper row. **Included:** `supertux-speedrun` (Aug 26, GPL-3.0), `tuxemon-speedrun` (Aug 30, GPL-3.0, folded into the same row) and `speedrun_bench` (Sep 30, no license). `tuxemon-ghosts` (Aug 31, no license) was **not included** because there was no description or announcement. `kimi-k3-nvfp4`, `miles-nvfp4`, `megatron-lm-nvfp4` and `patronus-py` returned 404. | 10 public repos listed; 4 created in window; 2 rows |
| 2026-10-16 | cross-window | Hugging Face API: datasets and models by `PatronusAI` | In-window items: `world_model_corpus` (May 6), `kimi-k3-nvfp4` (Jul 29), `Qwen3.8-27B-Figmatrace-SFT` (Aug 19), `figmatrace` (Aug 19), `speedrunbench` (Sep 3). Each is used either as its own row or as the check for a blog row. The February 2026 Qwen3-4B experiment checkpoints are **excluded** as out of window. | n/a |
| 2026-10-16 | baseline | Wayback availability API for `patronus.ai` near 2026-04-12 | A snapshot from 2026-04-13 exists but **could not be opened** with the available fetch tool. The date of the repositioning therefore remains **unknown**. | n/a |
| — | cross-window | `arxiv "Patronus AI" 2026 agents benchmark` | **NOT EXECUTED.** The session web-search budget was exhausted. A future reviewer should run it. | not run |

## Inclusion, exclusion and data-validity decisions

- **Included: 13 ledger rows.**
  - Segment counts: Apr 0, May 2, Jun 3, Jul 2, Aug 2, Sep 3, Oct 1.
  - Rows sharing a `duplicate_event_group` describe one underlying work. `058-dwm-paper` covers the two arXiv versions. `058-speedrunbench` covers the blog, the game forks and the harness. `058-hallucination-research` covers the two collaborative papers. `058-nvfp4` covers the engineering note and the weights.
- **Syndication deduplicated:** TechCrunch, Channel Insider and Pulse 2.0 all report **one** funding event. Only the first-party post carries a row. TechCrunch is its independent check, and it is press reporting of company and investor claims, not verification.
- **Availability classes:**
  - The DWM is a **preview**.
  - Paper, dataset and repository releases are **shipped**, meaning publicly available artifacts.
  - Funding, NeurIPS acceptance, the NVFP4 note and attribution-uncertain papers are **reported_undetermined**.
  - No item was promoted from preview to GA.
- **Date sources:**
  - Blog post pages display no date, so dates come from the blog index.
  - Registry `created_at` and `createdAt` values are not confirmed public-visibility dates.
  - The arXiv identifier 2607 conflicts with the v1 submission date of 2026-05-07; this is flagged rather than resolved.
- **Inaccessible:** `docs.patronus.ai` (401), the HPCwire release (403), the Wayback snapshot (tool restriction), and repositories returning 404.
- **Review status:** factual and scientific **independent human review is pending**. A reviewer should re-run these queries with UTC timestamps and real result counts, open the excluded snippets, check NeurIPS 2026 listings and author affiliations, and record any contrary evidence before #126 is closed.
