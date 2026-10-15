# Groq (064) — provisional search, inclusion and verification log

> **PROVISIONAL, AI-assisted first-pass screen (2026-10-16); not reviewed by a qualified human.** This log is a companion to the [report](064-groq.md) and [event ledger](064-groq.events.csv). Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

**Window:** 2026-04-12 … 2026-10-12 inclusive. **Searches and fetches:** 2026-10-16 (exact UTC run times were not recorded). **Issue:** [#132](https://github.com/MSKazemi/github-trending-1000-study/issues/132); corpus link [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56).

**Tools:**
- Web search returns provider-generated summaries plus links. Result totals were unavailable, not zero.
- Direct `curl` fetches used a generic browser User-Agent and carried no personal identifiers in any header, URL or payload. They were followed by local HTML-to-text extraction.
- `gh api` read GitHub releases, commits and licences.
- Every figure, version, price, date and quote in the ledger was confirmed against raw fetched text or GitHub API output. Search-summary-only statements were **not** used as evidence.

**Coverage limits:**
- The session-wide web-search budget was exhausted near the end of the screen. Two planned queries were not run: an April-specific news query and a GTC-2026 LPX baseline query. April coverage therefore rests on first-party docs and GitHub only.
- No paywalled content was bypassed. No archive or proxy services were used.

## 1. Query log

| Segment | Exact query (web search, standard mode) | Opened / decision | Counts |
|---|---|---|---|
| identity | `Groq Nvidia licensing agreement Jonathan Ross GroqCloud 2026` | Opened the [Groq 2025-12-24 release](https://groq.com/newsroom/groq-and-nvidia-enter-non-exclusive-inference-technology-licensing-agreement-to-accelerate-ai-inference-at-global-scale). Used as **baseline** (pre-window). Constellation Research and Sacra excluded as commentary/aggregators. | unknown |
| May–Jun | `Groq raises $650 million June 2026 Disruptive Infinitum Adam Winter CEO` | Opened [Reuters/Yahoo 05-28](https://finance.yahoo.com/sectors/technology/articles/groq-targets-650-million-fundraise-150216663.html) (included, 005). The forklog (HTTP 504) and noqta (HTTP 410) pages were inaccessible. aiweekly was opened but excluded as a derivative summary. | unknown |
| Aug | `Groq Series A $350 million $3.5 billion valuation August 2026 Nvidia` | Opened [TNW](https://thenextweb.com/news/groq-3-5bn-valuation-funding-round) (included, 017) and [Bloomberg Government](https://news.bgov.com/private-equity/groq-valued-at-3-5-billion-in-funding-round-after-nvidia-deal) (used as the independent check URL). DCD returned HTTP 403. implicator, aiweekly, dealroom and asiae were excluded as derivative or unread. | unknown |
| leadership | `Groq CEO Simon Edwards steps down Adam Winter 2026`; `"Adam Winter" Groq interim CEO` | Only aggregator profiles appeared (clay.com, teahose, revenuememo), so these were excluded. The leadership conflict was resolved only as far as first-party plus TechCrunch allow. | unknown |
| May | `TechCrunch "not-acqui-hire" Groq reportedly raising $650M`; `techcrunch.com 2026/06 Groq confirms $650M raise re-staffs` | Opened [TechCrunch 05-29](https://techcrunch.com/2026/05/29/after-nvidias-20b-not-acqui-hire-ai-chip-startup-groq-reportedly-raising-650m/) (included, 006). The June TechCrunch follow-up was **not found or opened**. Search summaries attributing "Doug Wightman remains CEO" to it are unverified and not used. | unknown |
| Apr | `Groq news April 2026 GroqCloud` | No dated April 2026 independent items. Results were 2024–2025 items or aggregators (excluded). | unknown |
| critical | `Groq layoffs OR "job cuts" OR restructuring 2026 after Nvidia deal employees` | No formal layoff report found. Axios 2025-12-28 is baseline and was not opened. The summary claim that ~90% of employees joined Nvidia is **not used** because it is snippet-only (E0). | unknown |
| regulatory | `Nvidia Groq deal antitrust FTC scrutiny 2026 licensing acquihire senators`; `DOJ investigating Nvidia Groq deal New York Times civil investigative demand` | Senate letter 2026-03-23 is baseline; senate.gov returned HTTP 403. PC Gamer: curl failed and WebFetch returned no body (inaccessible). Techzine returned HTTP 403. Opened [Reuters via The Star](https://www.thestar.com.my/tech/tech-news/2026/09/10/us-doj-probes-nvidia039s-licensing-deal-with-ai-startup-groq-nyt-reports) (included, 024). | unknown |
| Aug (hardware) | `NVIDIA Groq 3 LPX Vera Rubin performance Artificial Analysis 3,400 tokens per second Gemma August 2026` | Opened [StorageReview](https://www.storagereview.com/news/nvidia-groq-3-lpx-enters-full-production-3400-tokens-per-second-at-100k-context-256-lp30s-per-rack) (included, 020). The NVIDIA investor press release and Techzine returned HTTP 403 (inaccessible). The "3,431 tok/s median" figure appears only in search summaries and is **not used**. | unknown |
| benchmarks | `Artificial Analysis Groq provider benchmark 2026 output speed gpt-oss-120b Groq vs Cerebras` | Opened [Artificial Analysis Groq provider page](https://artificialanalysis.ai/providers/groq) as a 2026-10-16 snapshot (not a ledger row). Vendor (Cerebras) and blog comparisons excluded. | unknown |
| Jul | `Groq GroqCloud July 2026` | No July first-party post. storagenewsletter 2026-07-09 is a reprint of the June release (dedup, excluded). | unknown |
| Sep | `Groq September 2026 inference cloud announcement` | No September first-party post. A CO/AI item that the summary dated 2026-08-07 is actually dated **2025** on its page (excluded; date error in the search summary logged). | unknown |
| Aug (deprecations) | `GroqCloud deprecates Llama 3.3 70B versatile free tier developers migrate gpt-oss 2026` | Opened the [HF forum thread](https://discuss.huggingface.co/t/looking-for-an-open-source-llm-to-replace-llama-3-3-70b-versatile/178871) (included, 018) and ecorpit (2026-08-21, derivative of the deprecations page, excluded). Other blogs and skill indexes excluded. | unknown |
| data centres | `Groq data center 2026 Saudi Arabia OR Helsinki OR "Bell Canada" OR Sydney capacity update May June 2026` | Only 2025 items (Sydney, Helsinki); excluded as pre-window. | unknown |
| Oct | `"Groq" October 2026` | No in-window October items. Wikipedia was opened but excluded: it carries a July 2026 suspected-LLM-text warning. | unknown |
| Apr / GTC | *(planned: April news; GTC 2026 LPX baseline)* | **Not run**: web-search budget exhausted. | — |

## 2. First-party and GitHub sources read directly

| Source | What was read | Decision |
|---|---|---|
| [groq.com](https://groq.com/), [blog](https://groq.com/blog) (`/newsroom` redirects to `/blog`), [sitemap](https://groq.com/sitemap.xml) | About 40 post links. Each candidate was opened and its displayed date read. | In-window: 06-22, 08-12, 08-17, 08-24 (rows 010, 014, 016, 019). Baseline: 2025 posts and the 2026-02-16 UK data-centre post. Excluded: the **2026-10-15** Muse Spark Open post (after the window). The sitemap omits the Aug 2026 posts (stale). `groq.com/pricing` redirects to the homepage. |
| [GroqCloud changelog](https://console.groq.com/docs/changelog) / [.md](https://console.groq.com/docs/changelog.md) | Latest entry is 2026-04-18. | Row 002. The **absence of later entries** is a finding, not "no changes": the deprecations page and SDKs show later model changes. |
| [groq/groq-changelog](https://github.com/groq/groq-changelog) commits | The Q1 2026 entries were committed on 2026-05-06 (abaa839). | Recorded as a publication-date caveat on row 002. |
| [Deprecations](https://console.groq.com/docs/deprecations.md) | Sections dated 04-15, 06-17 email, 07-17, 08-16, 08-24 announcement, 09-14, 09-21. | Rows 001, 008, 012, 015, 021, 025. |
| [Compound changelog](https://console.groq.com/docs/changelog/compound.md) | Entries 2026-06-12 and 2026-09-21. | Rows 007, 026. |
| [Supported Models](https://console.groq.com/docs/models), [Qwen 3.8 27B page](https://console.groq.com/docs/model/qwen/qwen3.8-27b) | 2026-10-16 snapshot: prices, tiers, tps. | Used for context and row 022 limitations. The Qwen 3.6 page no longer showed a tier label. |
| [Status RSS](https://groqstatus.com/feed.rss), [status page](https://groqstatus.com/) | Items Oct 9–12 only; `/history` returned 404. | Row 027. Earlier in-window incidents are **not retrievable** from this feed. |
| `gh api` groq/groq-python, groq/groq-typescript releases | Python v1.2.0–v1.7.0; TS v1.2.0–v1.6.0. Diffs read for e24f597 (qwen3.6-27b), 8f8ef54, 5d65203 (qwen3.8-27b) and 36eede4 (yarn.lock only). | Rows 003, 004, 009, 013, 022. Minor maintenance releases (Py v1.4.0, TS v1.2.1, v1.4.1, v1.5.0) were not given separate rows. |
| `gh api` groq/groq-typescript commits after v1.6.0 | 8180ac6 (2026-09-03) "strict OpenAI compatibility for white-label deployments". The diff was too large to review fully. | Row 023 (unreleased). |
| `gh api` groq/openbench, groq-desktop-beta, groq-mcp-server, groq-api-cookbook | LICENSE diff "Groq, Inc." → "Groq LLC" (2026-06-26). Non-automation commit counts in the window vs the prior six months. | Row 011. Counts are reported in report §4 as an activity signal only. |

## 3. Inclusion and validity decisions

- **Included:** 27 rows (Apr 3, May 3, Jun 5, Jul 2, Aug 9, Sep 4, Oct 1). Rows sharing a `duplicate_event_group` describe **one** underlying event, for example:
  - the 06-17 deprecation announcement and its two shutdown dates;
  - the HF forum fallout from that announcement;
  - the Series A press release and TNW's report on it.

  They are not independent confirmations.
- **No empty months.** Months with no first-party newsroom post (April–May, July, September) are still covered by documentation, GitHub or independent reporting.
- **Conflicts recorded, not resolved:**
  - Nvidia deal value: $17B (Reuters) vs ~$20B (TechCrunch, TNW).
  - CEO: Adam Winter (Groq releases, TechCrunch) vs Doug Wightman (TNW).
  - Developer counts: ">five million" (06-22) vs ">six million" (08-12 and 08-17).
  - Capacity targets: "toward 200 MW by the end of 2027" vs "from 54 MW to 200+ MW in 2027".
  - Release-note dates vs GitHub release timestamps.
  - The changelog's displayed date vs its commit date.
- **Snippet-only (E0) claims deliberately not used:**
  - "~90% of employees joined Nvidia";
  - "Adam Winter took the helm in March";
  - a 3,431 tok/s median;
  - a Groq 2025 revenue figure;
  - "Nebius, CoreWeave, SpaceXAI first customers" (only Nebius was confirmed in the StorageReview text);
  - a Clay profile listing Edwards as CEO from April 2026.
- **Untrusted content:** no page contained instructions directed at an AI agent. Wikipedia's article carries a maintainer warning about suspected LLM-generated text, so it was excluded.
- **Not done:**
  - immutable snapshots or hashes of pages;
  - result counts;
  - filings-level entity verification (no SEC/state registry lookup was attempted);
  - reading the original Axios and NYT articles;
  - the NVIDIA LPX press release (HTTP 403);
  - human review.

A future reviewer should re-run these queries with UTC timestamps, capture the Groq LLC registration record if it is publicly accessible, and spot-check at least the deprecation dates and SDK versions.
