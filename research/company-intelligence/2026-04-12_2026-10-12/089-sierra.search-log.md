# Sierra (089) — provisional source-query and inclusion log

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** Companion to the [report](089-sierra.md) and [event ledger](089-sierra.events.csv) for [#157](https://github.com/MSKazemi/github-trending-1000-study/issues/157). Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

**Window:** 2026-04-12…2026-10-12 inclusive (UTC dates). **Accessed:** 2026-10-16.

**Method:**
- Official pages were retrieved as raw HTML with `curl` using a generic `Mozilla/5.0` User-Agent. No personal identifier, email or credential was sent to any site.
- robots.txt was checked before fetching from each site. Text was extracted from the HTML, and every number, date and quote used in the ledger was confirmed by exact-phrase matching against the extracted raw text. 156 phrases were checked and 0 were missing.
- `gh api` supplied repository, release, tag, commit and licence metadata. The Hacker News Algolia API and a small number of web searches were used for discovery.
- **This is not exhaustive retrieval.** Search-engine result totals were not exposed and are recorded as unknown, not zero. No page snapshots or hashes were archived in the repository, and pages may change after access.

## Access rules (robots.txt) observed

| Site | robots.txt result | Action |
|---|---|---|
| sierra.ai | `User-agent: *` / `Disallow:` (all allowed); sitemap index listed | fetched blog index, 49 in-window posts, Summit registration page, RSS |
| personalagentprotocol.org | `Allow: /` | homepage fetched once |
| siliconangle.com | `User-agent: *` / `Disallow:` (all allowed) | 2 articles fetched |
| techcrunch.com | generic `*` allows article paths; **disallows `anthropic-ai`, `Claude-Web`, `ClaudeBot`** (and other AI agents) | one article (Fragment, Apr 23) was fetched with the generic UA before this AI-agent block was noticed. No further TechCrunch pages were fetched. The row is flagged so the maintainer can decide whether to keep it |
| cnbc.com | no generic disallow for articles; **disallows `anthropic-ai`, `ClaudeBot`, `Claude-Web`** | **not fetched** (conservative); CNBC figures appear only as E0 search-snippet leads |
| axios.com | robots.txt request returned HTTP 403 | not fetched; **inaccessible** |
| status.sierra.ai | incident.io page, client-rendered (`noindex`); `/feed.rss` 404; `/history` client-rendered | incident history **not retrievable** without JavaScript; no incident rows |
| reuters.com, wsj.com, nytimes.com, theverge.com, zdnet.com | search tool reported these domains are not accessible to its user agent | not used |

## Query and source log by segment

| Date | Segment | Exact query or source request | Opened / decision | Found / screened / excluded |
|---|---|---|---|---|
| 2026-10-16 | all | `GET https://sierra.ai/robots.txt`, `/sitemap.xml`, `/sitemap-en-us.xml` | 394 en-US URLs, 132 under `/blog/`. Sitemap `lastmod` values are bulk timestamps, not publication dates, so they were not used for dating | — |
| 2026-10-16 | all | `GET https://sierra.ai/blog` (embedded CMS JSON) | 132 posts with `publishedAt` parsed; **49 in window** | 49 / 49 fetched raw / 19 not ledgered |
| 2026-10-16 | all | `GET https://sierra.ai/rss.xml` | 132 items, consistent with the blog index count; used only as a cross-check | — |
| 2026-10-16 | all | `gh api orgs/sierra-research/repos` | tau-bench (MIT; last push 2026-03-18, no in-window activity), tau2-bench (MIT), mu-bench (created 2026-04-14T17:09Z; LICENSE: Apache-2.0 code + CC BY-NC 4.0 data; API shows NOASSERTION), hyper-tau-bench (MIT; created 2026-09-04T01:09Z; 4 commits to 2026-09-07) | 4 repos |
| 2026-10-16 | all | `gh api repos/sierra-research/tau2-bench/releases`, `/tags`, `contents/CHANGELOG.md`, `commits?since=2026-04-12&until=2026-10-13` (paginated) | v1.0.1 release 2026-07-22T21:22:42Z (CHANGELOG heading `[1.0.1] - 2026-07-15`). v1.0.0 2026-03-18 and tag `voice-user-sim-v1.0` (2026-03-19) are pre-window. CHANGELOG `[Unreleased]` section empty. Commits by month: Apr 26, May 23, Jun 6, Jul 29, Aug 14, Sep 16, Oct (1–12) 2 | 1 row |
| 2026-10-16 | Oct | `gh api repos/personal-agent-protocol/personal-agent-protocol` | created **2026-10-14T12:55Z** (post-window), Apache-2.0; no tags; no commits before 2026-10-13. Used only as a limitation note | 0 rows |
| 2026-10-16 | all | HN Algolia `search_by_date`, `tags=story`, `created_at_i` 1775952000–1792022400, queries: `Sierra AI` (12), `sierra.ai` (10), `Bret Taylor` (3), `tau-bench` (2), `Sierra agent` (4), `Sierra raises` (1), `Sierra customer service` (0) | Hits were mostly reposts of Sierra blog posts (funding post: 110 points, 154 comments; comments not read). Also a TechCrunch Fragment link, a runtimewire Takeoff link (aggregator, not used) and a third-party tau-voice leaderboard claim (not used) | 32 hits / ~16 unique relevant / leads only |
| 2026-10-16 | Apr 12–30 | blog posts `mu-bench-…`, `the-ai-native-interview`, `sierra-acquires-fragment-in-france`; `evaluating-and-improving-search` | 3 rows; Apr 14 search-evaluation post excluded (method explainer, no dated change) | — |
| 2026-10-16 | Apr 12–30 | TechCrunch `2026/04/23/bret-taylors-sierra-buys-yc-backed-ai-startup-fragment/` (from HN) | read raw (`datePublished` 2026-04-23T21:00Z); see robots note above | 1 row |
| 2026-10-16 | May | blog posts `tau-voice-…`, `better-customer-experiences-built-on-sierra`, `agent-monitoring`, `tau-knowledge`; also `context-engineering-the-key-to-great-agents`, `voice-ai-is-only-as-good-as-what-it-hears`, `agent-strategist-your-phd-in-applied-ai`, `sierra-lands-in-the-6`, `ai-native-product-localization` | 4 rows; the latter five were excluded as explainers, career/role posts or an office opening (Toronto, "about a dozen employees") | — |
| 2026-10-16 | May | web search `Sierra Bret Taylor AI agents $950 million Tiger Global GV valuation May 2026`; `Sierra customer service AI startup raises funding Tiger Global GV Reuters OR CNBC OR Fortune OR Bloomberg 2026`; `Sierra Bret Taylor $950 million $15.8 billion` (domain-restricted) | [SiliconANGLE May 4](https://siliconangle.com/2026/05/04/ai-agent-startup-sierra-valued-15b-new-950m-funding-round/) read raw (`datePublished` 2026-05-05T00:47Z). Axios (403) and CNBC (robots) were not read; their $15.8B figure stays an **E0 snippet**. trendingtopics, mezha, metodoviral, texxr, startupresearcher, torre.news, cryptobriefing, defillama, sacra, pluang and neuronfeed were excluded as aggregators or estimators (E0). One aggregator listed a duplicate "$950M Series E" dated 2026-07-17, which is unsupported and not used | unknown / ~25 / 24 |
| 2026-10-16 | June | blog posts `outcomemaxxing`, `certified-fedramp-high`, `let-your-customers-shape-your-agents`; also `discovering-what-s-possible-with-ai-for-cx`, `how-customer-teams-became-software-builders` | 3 rows; the CX explainer and the Ghostwriter-adoption anecdote post were excluded (the latter is used only for the Ghostwriter March-launch baseline) | — |
| 2026-10-16 | July | blog posts `announcing-our-partnership-with-softbank-corp`, `horizon`, `building-sierras-mcp-gateway-…`, `sierra-acquires-takeoff`, `agency-secure-scalable-sandboxes-for-agents`; also `takeaways-from-our-ghostwriter-hackathon`, `ai-pilling-our-company-lessons-learned`, `pinecone-harnessing-the-wisdom-of-the-workforce` | 5 blog rows + 1 GitHub release row; hackathon, AI-pilling and Pinecone posts were used as context only (internal-practice series) | — |
| 2026-10-16 | August | blog posts `our-partnership-with-plaid`, `context-engine`, `introducing-voice-personas`, `defense-in-depth-in-the-age-of-agents`, `release-governance-guardrails-for-agents-at-scale`, `julia-brau-donnelly-joins-sierra`; also `navigating-ivr-systems`, `the-follow-up-is-the-sale`, `building-in-dach`, `sierra-launches-in-korea` | 6 rows; IVR, follow-up sales and the Munich/Seoul office posts were not ledgered (capability anecdote, sales explainer, office openings) | — |
| 2026-10-16 | September | blog posts `hyper-t-bench-…`, `sierra-achieves-aiuc-1-certification`, `your-agent-laid-bare-and-why-it-matters`, `ghostwriter-ai-tool-to-teammate`, `sierra-joins-the-openai-marketplace`; also `what-is-voice-ai`, `ai-for-call-centers`, `multimodal-agents` | 5 rows; the two SEO guides were excluded, and the multimodal post was excluded (no availability or technical detail) | — |
| 2026-10-16 | Sep–Oct | web search `Sierra AI agents Bret Taylor criticism OR lawsuit OR outage OR layoffs OR skeptic 2026` | no 2026 criticism, lawsuit, outage or layoff report found. Results were salesforceben rivalry commentary (not read) and 2024 Fortune recusal interviews (pre-window baseline, not read) | unknown / 9 / 9 |
| 2026-10-16 | Oct 1–12 | blog posts `introducing-personal-agent-protocol`, `summit-recap-2026`, `caller-id-in-the-age-of-agents`, `poppy`; also `the-sierra-partner-ecosystem`; `GET https://sierra.ai/events/sierra-summit-2026-register` | 4 blog rows. The registration page confirms "October 6, 2026, at Fort Mason in San Francisco". The partner-ecosystem post was excluded (no named partners or dated capability) | — |
| 2026-10-16 | Oct 1–12 | web search `Sierra AI Horizon OR Takeoff OR "Personal Agent Protocol" OR Ghostwriter 2026` (domain-restricted to siliconangle, theregister, venturebeat, infoq, thenewstack) | [SiliconANGLE Oct 6](https://siliconangle.com/2026/10/06/meta-teams-up-with-bret-taylors-sierra-technologies-on-new-standards-for-ai-agent-commerce/) read raw (`datePublished` 2026-10-07T00:54Z). No independent coverage of Horizon, Takeoff or Ghostwriter was found. VentureBeat benchmark article is undated in results and likely pre-window, so it was not read | unknown / 10 / 9 |
| 2026-10-16 | Oct 1–12 | `GET https://personalagentprotocol.org/` | current site read; it links to the post-window GitHub repo. Used as the check URL on the Poppy row only | — |
| 2026-10-16 | Sep–Oct | `GET https://status.sierra.ai/`, `/feed.rss`, `/history` | client-rendered or 404; **no incident history obtainable** | — |

## Inclusion, deduplication and conflicts

- **Included:** 34 rows by month: Apr 4, May 5, Jun 3, Jul 6, Aug 6, Sep 5, Oct 5. Each row cites a URL that was fetched as raw text or queried by API. No row relies on a search snippet alone.
- **Duplicate groups:**
  - `089-003`: Fragment acquisition (Sierra blog + TechCrunch).
  - `089-006`: funding round (Sierra blog + SiliconANGLE).
  - `089-030`: Personal Agent Protocol (announcement Oct 6, SiliconANGLE Oct 6/7, draft Oct 9). Three documents, one initiative.
- **Date conflicts recorded, not resolved:**
  - tau2-bench 1.0.1: CHANGELOG 2026-07-15 vs GitHub release 2026-07-22T21:22Z.
  - SiliconANGLE funding article: `datePublished` 2026-05-05T00:47Z, which is May 4 in US time.
  - SiliconANGLE PAP article: 2026-10-07T00:54Z, which is Oct 6 in US time.
  - PAP GitHub repo created 2026-10-14, after the Oct 9 "draft" post.
- **Figure conflicts:**
  - Valuation: "over $15 billion" (vendor) and "$15 billion" (SiliconANGLE) vs $15.8B (E0 snippets).
  - Fortune 50 share: "40%" (several posts) vs "almost half" (Jul 16) vs "almost 50%" (Sep 29, Oct 6) vs "nearly half" (SiliconANGLE, May).
  - ARR: $150M (SiliconANGLE, May, relaying Sierra) vs "$100M in seven quarters / $200M in nine quarters" (Sierra, Aug 31). Timing makes these potentially compatible, but they are not reconciled.
  - tau-knowledge best Pass^1: 37.4% (May 13 post) vs 46.39 after the v1.0.1 re-grade.
  - PAP founding partners: NiCE appears on Oct 9 but not on Oct 6.
- **Figures confirmed against raw text** (exact-phrase match on extracted page text; 156 phrases, 0 missing):
  - μ-Bench: 4,270 / 250 / 8 kHz / 5×5 / 79 locales / ~8× latency.
  - Fragment and TechCrunch: third acquisition, Opera Tech, Receptive AI, ~$2M, $10B.
  - tau-voice: 30%→67%, ~79%, ~45%, 91 sampled simulations.
  - Funding: $950M, Tiger Global and GV, over $15B, >$1B; SiliconANGLE $15B, $150M ARR, >15 models.
  - tau-knowledge: 698 / 21 / ~195K / 25.5 / 9.3 / 37.4 / 20.6 / 18.6 / 9.5 / 11 variants / 19.4→9.1.
  - FedRAMP: Knox Systems, 58 languages. SoftBank: 97% / 93%.
  - Takeoff: $0 → nearly 8 figures, 3-person team, 14 months.
  - Agency: Kubernetes / DynamoDB / 24GiB.
  - CFO post: $100M / seven quarters, $200M / nine quarters.
  - hyper-tau-bench: 23.9% / 82.2% / ~1,700 files.
  - AIUC-1: Schellman, quarterly.
  - PAP: partner lists, OAuth, v0.1 plan, `/.well-known/poppy.json`, 35 partners.
  - Summit: Fort Mason, Oct 6; >50% resolution claim; 80% of Fortune 50 healthcare.
  - tau2-bench CHANGELOG: 37.37 → 46.39.

  All of these remain **vendor or press statements**, not verified measurements. A summary of the tau2-bench release body was read via `gh api`; its re-grade table was not independently recomputed.
- **Untrusted-content note:** fetched pages were treated as data. No Sierra page contained instructions aimed at the researcher. The `sierra-research/mu-bench` repository contains an `AGENTS.md` file, which is a contributor guide for coding agents working in that repository. It was read only as metadata. Nothing in it was followed or executed, and no repository code was run. Search-tool summaries were treated as leads only. Their numeric claims were not used unless confirmed in raw text.

## Missing, inaccessible or not attempted

- Not read or not reachable:
  - Axios (403); CNBC (robots disallows Claude agents); Reuters, WSJ and NYT (unreachable by the search tool).
  - Further TechCrunch pages, after the robots AI-agent block was noticed.
  - Partner-side pages: SoftBank, Plaid, Meta, OpenAI marketplace, Knox Systems/FedRAMP marketplace, AIUC/Schellman.
  - Sierra status-page incident history; Sierra docs and release notes (no public changelog found); Sierra terms and data-retention terms.
  - Archived (Wayback) copies of mutable pages as of 2026-10-12; filing-level corporate records.
- No product was executed, no account was created, no repository code was run, no paywall was circumvented, and no energy was measured. No regulator site was contacted.
- **Reproduction:** re-run the requests above with UTC timestamps and save raw HTML hashes. An independent human should then spot-check at least:
  - the funding rows (CI2026-089-006, 007);
  - the tau2-bench release (016) against GitHub;
  - hyper-tau-bench (025);
  - the PAP rows (030, 032, 034).

  This spot-check should happen before any evidence is promoted beyond provisional status. The human reviewer should also decide whether row 004 (TechCrunch) is kept given that site's robots.txt AI-agent disallow.
