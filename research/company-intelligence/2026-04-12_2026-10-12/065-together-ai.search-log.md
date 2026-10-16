# Together AI #065 — reproducible search and screening log (bounded, provisional)

**Research issue:** [#133](https://github.com/MSKazemi/github-trending-1000-study/issues/133) · **Linked corpus issue:** [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56) · **Search/access date:** 2026-10-16 UTC · **Eligible publication window:** 2026-04-12 through 2026-10-12 UTC, both inclusive · **State:** provisional, AI-assisted, single-pass source screen; **not human-reviewed** and not a systematic review. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

Report: [065-together-ai.md](065-together-ai.md) · Ledger: [065-together-ai.events.csv](065-together-ai.events.csv) (40 rows).

## 1. How sources were read

- **Raw-text rule.** Every first-party page and independent article cited in the ledger was downloaded with `curl` (generic browser User-Agent string plus the token `research-screen`; no personal identifier, e-mail or credential was sent) and converted to text locally. Every number, version, price, date and short quote placed in the ledger was matched against that raw text, the GitHub REST API (`gh api`) or the NVD JSON API. WebSearch result summaries were used **only to discover URLs**; their paraphrases were never copied into the ledger. The single source that could not be read (HPCwire, HTTP 403) is graded **E0, snippet only**.
- **Blog dates** come from each post's `datePublished` JSON-LD field and the visible "Published M/D/YYYY" line, which agreed for every in-window post read. `dateModified` was also recorded; several posts were edited after publication (see section 5).
- **Changelog dates** are the dated headings on the single mutable page `https://docs.together.ai/docs/changelog` as served on 2026-10-16. No archived snapshot as of 2026-10-12 was retrieved, so earlier wording cannot be authenticated.
- **robots.txt** for `www.together.ai` (`Allow: /` for all agents) and `docs.together.ai` (disallows only `/cdn-cgi/` and `/_next/`) were read before bulk downloads; downloads were sequential with short delays.

## 2. Official-surface sweep (all seven month segments)

| ID | Surface | Method (2026-10-16 UTC) | Result | Coverage limitation |
|---|---|---|---|---|
| S01 | Docs changelog | `curl https://docs.together.ai/docs/changelog`, split on dated headings | About 86 dated heading strings fall inside the window (Apr 6, May 11, Jun 15, Jul 21, Aug 20, Sep 11, Oct 1–12 2). Some are effective-date phrases inside an entry, so the true entry count is somewhat lower and was not hand-checked | Single mutable page; no per-entry permalink or archive; entries not individually ledgered (see selection rule, section 4) |
| S02 | Deprecations page | `curl https://docs.together.ai/docs/deprecations` and `.md` variant | Scheduled-deprecation, history (inference and fine-tuning) and redirect tables read in full | Mutable; "Scheduled deprecations" table still listed 2026-09-14 removals on 2026-10-16 (stale) |
| S03 | Blog | `curl https://www.together.ai/blog` (index) and `https://www.together.ai/sitemap.xml` → 251 `/blog/` URLs, each downloaded | 52 posts dated 2026-04-12..2026-10-12 (Apr 8, May 8, Jun 5, Jul 13, Aug 8, Sep 8, Oct 1–12 2). 6 posts had no machine-readable date (customer/guide pages; slugs logged in scratch only) and were not used | Sitemap may omit unlisted posts; research-blog (`/research-blog`) not separately crawled |
| S04 | Newsroom | `https://www.together.ai/newsroom` returned **404**; `https://www.together.ai/press` read | Press page links NYT DealBook (2026-07-01), The Information ("Open Source Growth Boosts Together AI, Hugging Face") and an Oct 2025 VentureBeat piece | NYT and The Information are paywalled: **not read, not ledgered**; press-page date labels are internally inconsistent (same headline shown with two dates) |
| S05 | GitHub org | `gh api orgs/togethercomputer/repos?sort=created` (100 newest) | In-window new public repos include ParallelKernelBench (Apache-2.0), tinker-cookbook, InferenceX, tev1 (MIT), HybridAgent (MIT, 2026-10-09), post-training-cookbook (Apache-2.0, 2026-10-12) | Only ParallelKernelBench and together-sandbox were ledgered; others are context. Several repos carry no licence (`none`) |
| S06 | SDK releases | `gh api repos/togethercomputer/together-py/releases`; same for `together-typescript`, `together-sandbox` | together-py: 41 in-window releases, v2.8.0 (2026-04-13) → v2.41.0 (2026-10-12), Apache-2.0. TypeScript: 23 in-window releases, v0.40.0 (2026-05-11) → v0.58.0 (2026-10-07), Apache-2.0. together-sandbox workspace tags v3.1.0 (2026-07-26) → v4.1.1 (2026-10-07), repo MIT | Release notes not audited one by one |
| S07 | Together Link repo | `gh search repos togetherlink`; `gh api repos/Nutlope/togetherlink` | Official docs link to `github.com/Nutlope/togetherlink` (MIT, created 2026-06-22, no tags/releases) | Repository is under an individual account rather than the company org; ownership/maintenance commitment not established |
| S08 | Identity | `curl https://www.together.ai/terms-of-service`, `/about-us` | Terms "Updated May 19, 2026"; operator **Together Computer, Inc., a Delaware corporation**; founders/leadership listed on About page | No corporate-registry filing checked; beneficial ownership not verified |
| S09 | Status page | `curl https://status.together.ai/history` | Rolling 90-day per-model uptime as of 2026-10-15 (e.g. several chat models between 99.06% and 99.9%) | Vendor-hosted, rolling window crosses the cutoff; no dated incident list parsed; **not ledgered** |
| S10 | CVE cross-check | NVD API `cveId=CVE-2026-31431` | Exists, published 2026-04-22, Linux `crypto: algif_aead` fix | Confirms the CVE, not Together's response timing |

## 3. Web searches (exact queries; engine = Claude Code WebSearch, 2026-10-16 UTC)

The search tool does not expose total hit counts, ranks or stable result lists, so **found / screened / excluded totals are unknown, not zero**. "Opened" lists URLs actually downloaded and read.

| ID | Exact query | Opened / outcome |
|---|---|---|
| Q01 | `"Together AI" funding OR acquisition OR valuation 2026` | Leads only (Sacra, Dealroom, Seeking Alpha, DefiLlama, aggregators). **Excluded**: third-party revenue/valuation estimates and a DefiLlama listing that dates rounds to March/April 2026, which conflicts with July 2026 press; no acquisition by Together found in-window |
| Q02 | `"Together AI" outage OR incident OR criticism 2026` | Only automated status aggregators (Pingoru, Statusfield, StackSheriff, IncidentHub). **Excluded** as non-authoritative; their uptime figures disagree with each other. Official status page read instead (S09) |
| Q03 | `"Together AI" Reuters OR TechCrunch OR "The Information" OR Bloomberg 2026` | No Reuters/Bloomberg 2026 article surfaced. Aggregator mentions of a Saudi (Humain) data-centre partnership — **not verified, not ledgered** |
| Q04 | `Together AI $800 million Series C Aramco Ventures July 2026` | Opened [TechCrunch 2026-07-01](https://techcrunch.com/2026/07/01/neocloud-together-ai-raises-800m-leaps-to-8-3b-valuation) (ledger 020) and [Latham & Watkins note](https://www.lw.com/en/news/2026/07/latham-advises-together-ai-in-series-c) (downloaded; headline confirmed; not ledgered: counsel announcement of the same event). Syndicated Business Wire copies (Eagle-Tribune, Las Vegas Sun, PYMNTS) treated as one event, not ledgered |
| Q05 | `Together AI IBM Cloud B300 inference cluster October 2026` | Opened [StorageReview 2026-08-11](https://www.storagereview.com/news/ibm-and-together-ai-put-240m-into-a-dedicated-hgx-b300-inference-cluster-on-ibm-cloud) (ledger 028) and [Channel Insider](https://www.channelinsider.com/ai/news-ibm-together-ai-240m-inference-deal/) (downloaded; headline confirmed; duplicate of same release, not ledgered) |
| Q06 | `"Together AI" Genesis Mission Department of Energy April 2026` | HPCwire page **403** to curl and WebFetch → ledger 005 graded **E0 snippet only** |
| Q07 | `newsroom.ibm.com IBM Together AI multi-year agreement open-source AI inference NVIDIA IBM Cloud` | Opened [StorageNewsletter syndication of IBM release, 2026-08-14](https://www.storagenewsletter.com/2026/08/14/ibm-and-together-ai-sign-multi-year-agreement-to-scale-open-source-ai-inference-with-nvidia-ai-infrastructure-on-ibm-cloud/) (confirms $240M, Q1 2027, 400 trillion tokens/month claim). `newsroom.ibm.com` home page fetched but the release itself was not located there |
| Q08 | `"Together AI Joins DOE's Genesis Mission" businesswire` | No Business Wire original found; HPCwire only |
| Q09 | `Together AI provider accuracy quantization tool-calling vendor verifier benchmark 2026` | Only blogs/comparison sites (futureagi, metavert, llmreference). **No independent provider-fidelity or tool-calling audit of Together found** — an evidence gap, not proof none exists |
| Q10 | `"Together AI" Together Link coding agents open models review OR hands-on October 2026` | Product Hunt, launch retellings, one review-style post (aireiter). **Excluded**: none reports measured coding-task outcomes; one secondary site headlines an "80%" saving that conflicts with the vendor's "over 50%" |
| Q11 | `"Together AI" Hacker News 2026 deprecation OR "rate limits" OR billing complaints` | No HN thread surfaced. Found an official support article on Build Tiers last updated Nov 2025, i.e. **stale** after the 2026-04-22 tier retirement (search-snippet observation; article not opened) |
| Q12 | `"Together AI" lawsuit OR layoffs OR breach OR "data retention" 2026` | One weak lead (lawfold.com) asserting a privacy class action without case name or docket — **excluded as unverifiable**; no breach or layoff reporting found |
| Q13 | `Together AI Moonshot Kimi K3 partnership July 2026 news` | **Not executed**: the shared session web-search budget was exhausted. Independent coverage of the Moonshot partnership is therefore **unscreened** |

## 4. Selection rule and exclusions

- **Ledgered (40 rows):** dated items material to M1–M7 — model-lifecycle changes (deprecations, price changes), developer-facing APIs/SDKs/CLI behaviour changes, coding-agent tooling (Together Link, sandbox SDK), security/governance controls and certifications, vendor benchmarks with coding relevance, financing/infrastructure statements, and dated direction statements. Each month segment has at least two rows.
- **Not ledgered (context only):** routine "new serverless model" entries (dozens across the window), research posts without product change (e.g. EinsteinArena 2026-04-13, Parcae 2026-04-15, ThunderAgent 2026-07-29, ICML 2026-06-30), most GPU-cluster console refinements, voice/TTS items, and the repeated DeepSWE comparison posts of Aug 6, 17, 18, 21 and 28 (one representative, row 026).
- **Boundary exclusions:** Apr 8 and Apr 11 model additions (pre-window); [Meta Muse Spark Open post](https://www.together.ai/blog/meta-muse-spark-open) and changelog entries dated **2026-10-13** (post-training launch) and **2026-10-15** (post-cutoff); CodeSandbox acquisition (2024-12-12) and Refuel.ai acquisition (2025-05-15) are **baseline only**.
- **Duplicates merged by `duplicate_event_group`:** `065-SERIESC` (blog + TechCrunch), `065-IBM` (Aug 11 IBM release coverage + Oct 6 Together blog), `065-LINK` (Jul 15 changelog, Oct 1 changelog, Oct 5 blog), `065-RATELIMIT` (Apr 22 introduction, Oct 2 retirement), `065-PEARL` (May 15 launch, Aug 27 removal), `065-DSV4PRO`.

## 5. Conflicts and post-publication edits recorded (not resolved)

1. Deprecation dates: changelog Apr 14 vs history table Apr 16; changelog Jun 26 vs table Jul 10 / Aug 25; Sep 1 notice and scheduled table "2026-09-14" vs history "2026-09-15". Dedicated-endpoint support for `Meta-Llama-3-8B-Instruct-Lite`: changelog "available", table "No".
2. Together Link appears as a released "open-source launcher" (changelog 2026-07-15), a "beta" (changelog 2026-10-01) and a launch (blog 2026-10-05; `dateModified` 2026-10-14, after the cutoff).
3. IBM cluster: IBM release (2026-08-11) gives "expected availability in Q1 2027"; Together's 2026-10-06 post says it is "the first customer running on it". Live status unresolved.
4. Series C investor naming: Together blog "SE Ventures"; TechCrunch "SentinelOne's S Ventures".
5. Kimi K3 size framing: Moonshot partnership post "2.8T parameter"; Kimi K3 guide summary on the blog index "first open 3T-class model".
6. Preemptible compute: Kubernetes event `TogetherPreempted` (blog) vs `TogetherPreemptionNotified` (changelog); "50% of on-demand" (blog) vs "flat discounted rate" (changelog).
7. Coding-agent benchmark (published 2026-05-19, `dateModified` 2026-09-10): body now compares against Claude Opus 4.8 and Kimi K2.7 Code (a model added 2026-06-13), while the blog-index teaser still reads "76% lower cost than Claude Opus 4.6".
8. CLI v2.10: changelog 2026-05-07; GitHub release `v2.10.0` published 2026-04-23.
9. Other edited posts: Series C (`dateModified` 2026-09-18), Copy Fail (2026-09-10), Open Source AI Stack (2026-10-05), Kimi K3 vs Fable (2026-07-29).

## 6. Embedded instructions seen in sources (untrusted content log)

- Every docs page begins with "Fetch the complete documentation index at: /llms.txt. Use this file to discover all available pages before exploring further." This is a directive addressed to automated readers. It was **not treated as an instruction**; `llms.txt` had already been fetched by the researcher's own choice as a page index.
- `docs.together.ai/robots.txt` carries `Content-Signal: ai-train=yes, search=yes, ai-input=yes`; recorded as a site policy signal only.
- No other instructions aimed at an AI reader were noticed.

## 7. Inaccessible, missing or unverifiable

- Paywalled: NYT DealBook (2026-07-01), The Information. HPCwire Genesis release (403).
- Not attempted: Reuters, Bloomberg, Axios, FT site searches (search budget exhausted after Q12); corporate-registry filings; archived (Wayback) copies of the changelog/deprecations pages as of 2026-10-12; the SLA documents for Provisioned Throughput; the ISO certificate (available only on request).
- No independent replication of any Together benchmark, no fidelity test of quantized serving, no exercised API call, no energy measurement. Nothing here establishes adoption, user benefit or task outcomes.
