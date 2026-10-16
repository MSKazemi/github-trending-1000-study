# Harvey (088): provisional source, query and inclusion log

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** This log accompanies the [report](088-harvey.md) and [event ledger](088-harvey.events.csv) for [#156](https://github.com/MSKazemi/github-trending-1000-study/issues/156). Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

**Window:** 2026-04-12…2026-10-12 inclusive (UTC dates). **Accessed:** 2026-10-16.

**Method:**
- Official pages were retrieved as raw HTML with `curl -sL -A 'Mozilla/5.0'`. No personal identifier, email or credential was sent to any site.
- Text was extracted locally. Every number, version, date and quote used in a ledger row was confirmed with `grep` against the saved text.
- `datePublished` was read from each Harvey page's embedded metadata.
- The GitHub REST API (`gh api`) was used for repositories, releases, tags, issues and pull requests; PyPI JSON for `guardrails-ai`; the Hacker News Algolia API for leads; and three web searches for independent and critical coverage.
- Search-engine result totals were not exposed and are recorded as unknown, not zero. No page snapshots or hashes were archived in the repository, and pages may change after access.

**This is not exhaustive retrieval.**

## Query and source log by segment

| Date | Segment | Exact query or source request | Opened / decision | Found / screened / excluded |
|---|---|---|---|---|
| 2026-10-16 | all | `GET https://www.harvey.ai/robots.txt` (Allow: /), `/sitemap.xml` | 760 URLs, of which 524 are `/blog/`. In-window `lastmod` entries are dominated by SEO guides (for example "how-to-redline-a-contract-with-ai"), which were excluded as evergreen marketing | in-window blog URLs: several hundred / 77 fetched / see below |
| 2026-10-16 | all | `GET https://www.harvey.ai/newsroom`, `/blog` | Newsroom posts missing from the sitemap were found here (funding, Microsoft CELA, GE Aerospace, Squire Patton Boggs, Pro Bono, Legalscape, TC Energy, TX-RAMP, Ogier, brand campaign) | 18 newsroom items listed |
| 2026-10-16 | all | `GET https://www.harvey.ai/blog/<slug>` for 78 product/technical/research/company slugs (77 in window + `building-spectre-…` pre-window baseline) | all HTTP 200, with `datePublished` recorded for each | 77 in window / 77 / 46 not ledgered |
| 2026-10-16 | all | `gh api orgs/harveyai`, `orgs/harveyai/repos` | 7 public repos. `harvey-labs` (MIT, created 2026-03-30); `biglaw-bench` (no licence detected, last push 2026-03-17); others are archived forks or pre-window | — |
| 2026-10-16 | all | `gh api repos/harveyai/harvey-labs` + `/releases`, `/tags`, `/git/tags/<v1.0>`, `/contents/CHANGELOG.md`, `/contents/LICENSE`, `/contents/README.md`, `/commits?since…until` | Initial commit 2026-05-06T15:02Z. Tag v1.0 dated 2026-07-24T22:57Z. Releases v1.1.0 (2026-09-18T20:03Z) and v1.2.0 (2026-10-01T00:37Z). Commits by month in window: May 12, Jun 7, Jul 12, Aug 6, Sep 13, Oct 10 | — |
| 2026-10-16 | all | `gh api repos/harveyai/harvey-labs/issues?state=all` (paginated) | About 25 issue titles read; #94, #106, #114, #115, #124, #145, #149, #152 and #158 checked for state and dates; bodies of #106, #145 and #149 read. PR counts by author association were taken by 2026-10-12. Reporters are deliberately not named in the report | 3 issue rows + 1 PR row |
| 2026-10-16 | Apr 12–30 | blog: `two-types-of-legal-work-one-agentic-platform`, `collaborative-review-tables`, `opus-4-7-now-live-in-harvey`, `rebuilding-harveys-review-algorithm`, `gpt-5-5-research-preview-results`, `harvey-to-open-chicago-office-in-july`, `how-harvey-secures-embeddings-at-scale` | 3 rows. Review-table posts, GPT-5.5 preview and Chicago announcement excluded (feature polish, duplicate model-eval pattern, office). `building-spectre-…` dated 2026-04-07 is pre-window baseline | 7 / 7 / 4 |
| 2026-10-16 | May | blog: `introducing-harveys-transformation-office`, `agentic-platform-updates`, `introducing-harveys-legal-agent-benchmark`, `building-image-understanding-for-legal-documents`, `harvey-opens-in-paris`, `building-an-agentic-security-operations-center`, `introducing-command-center`, `introducing-contract-intelligence`, `legal-agent-benchmark-initial-results`, `using-email-harvey`, `post-training-open-legal-agents-with-baseten-research`, `opus-4-8-now-live-in-harvey` | 6 rows. Transformation Office (services), image understanding, Paris, SOC (internal), Contract Intelligence (design-partner preview) and Email Harvey excluded for brevity | 12 / 12 / 6 |
| 2026-10-16 | May | web search `Harvey "Legal Agent Benchmark" LAB critique OR skepticism OR limitations lawsites OR artificiallawyer` | [LawSites, May 19](https://www.lawnext.com/2026/05/some-thoughts-on-harveys-launch-of-lab-an-open-source-long-horizon-benchmark-for-legal-ai-agents.html) read raw and included. Results from digg, vaquill, moclaw, hermes-ai and datalearner were treated as **E0** and not used. vals.ai was fetched separately | unknown / ~9 / 7 |
| 2026-10-16 | June | blog: `why-we-built-our-own-cloud-agent-infrastructure`, `harvey-opens-in-singapore`, `us-case-law-source`, `shared-spaces-analytics-and-management`, `harvey-pitchbook-integration`, `governance-iso-42001`, `connector-library`, `fable-5-now-available-in-harvey`, `harvey-is-expanding-with-a-team-in-milan`, `legal-agent-benchmark-in-house-contracting`, `faster-more-reliable-vault-uploads`, `harvey-copilot-cowork-launch`, `visualize-legal-data-in-harvey`, `debunking-myths-data-sovereignty-and-us-based-service-providers`, `training-a-legal-agent-with-applied-compute`, `sonnet-5-in-harvey` | 7 rows (+ PR #76 from GitHub). Singapore, Milan, US case law, Spaces analytics, PitchBook, Vault uploads, visualisations, data-sovereignty opinion and Sonnet 5 excluded | 16 / 16 / 9 |
| 2026-10-16 | July | blog: `gpt-5-6-sol-in-harvey`, `harvey-opens-chicago-office`, `y-combinator-backed-benchmark-joins-harvey`, `legal-agent-bench-m-and-a-due-diligence`, `harvey-intapp-ethical-walls`, `harvey-expands-collaboration-with-microsoft-on-legal-ai`, `opus-5-in-harvey`, `scaling-document-processing-across-harvey` | 4 rows (+ AA, #106, v1.0 tag). Chicago, Microsoft CELA customer deal, Opus 5 and document-processing post excluded | 8 / 8 / 4 |
| 2026-10-16 | July | `GET https://artificialanalysis.ai/articles/harvey-lab-aa` (datePublished 2026-07-07), `/evaluations/harvey-lab-aa` | Article included. The evaluation page now shows v1.1 (hallucination-gated, not comparable) and was used as context only | 2 / 2 / 1 |
| 2026-10-16 | August | blog: `playbook-builder-in-harvey`, `the-new-harvey-for-outlook`, `audio-video-image-understanding`, `training-frontier-review-table-models-with-applied-compute`, `introducing-harvey-ii`, `post-training-update-harvey-tenet`, `memory-is-here-harvey-personalized` | 3 rows. Memory was folded into the Harvey II row. Playbook builder, Outlook and audio/video were excluded as feature marketing | 7 / 7 / 4 |
| 2026-10-16 | August | `GET https://status.harvey.ai/`, `/feed.atom`, `/incidents/01KZZCRZ8PQ8P3J6B1P8TM8EHZ` (incident.io) | AU outage 05:44–06:04 UTC Aug 14 included. EU planned maintenance Jul 19 noted, not ledgered. The page shows Jul–Oct 2026 only | 2 / 2 / 1 |
| 2026-10-16 | September | blog: `horizon-scanning-in-harvey`, `fable-5-1-in-harvey`, `rebuilding-playbook-review-as-a-multi-agent-system`, `harvey-everlaw-evidence-ediscovery`, `ge-aerospace-deploys-…`, `agentic-vault-search-and-organization`, `post-training-rlm-agents-for-m-and-a-diligence`, `guardrails-ai-joins-harvey`, `harvey-raises-dollar550m-…`, `contract-review-agents-in-harvey`, `review-table-agent-actions`, `augmenting-human-preference-in-complex-domains`, `introducing-harveys-pro-bono-program`, `squire-patton-boggs-…`, `what-the-harvey-agent-changes-about-legal-research`, `run-custom-harvey-agents-in-microsoft-word`, `agreements-make-history`, `agentic-search-document-management-systems` | 5 rows (+ v1.1.0, Bloomberg). Customer wins, Horizon Scanning, Fable 5.1, playbook rebuild, contract review agents, review-table actions, reward-model research, Word agents and DMS search excluded for brevity | 18 / 18 / 13 |
| 2026-10-16 | September | web search `Harvey $550 million Diffusion Lightspeed $15.5 billion September 2026` | [TechCrunch](https://techcrunch.com/2026/09/09/harvey-hits-15-5b-valuation-months-after-reaching-11b/) read raw (datePublished 2026-09-09T18:34Z). The snippet led to the Guardrails acquisition, confirmed on [guardrailsai.com](https://www.guardrailsai.com/blog/guardrails-ai-joins-harvey) and the Harvey blog. Autobound, trendingtopics, aiweekly, unite.ai, raising.fi and lemondedudroit were treated as **E0** and not used. The Latham & Watkins page was fetched but not used | unknown / ~10 / 8 |
| 2026-10-16 | September | `gh api repos/guardrails-ai/guardrails` (+ `/commits?since=2026-09-08`, `/commits?since=2026-06-01&until=2026-09-08`, `/pulls/1638`, `/commits/eb5c60ee`, README); `GET https://pypi.org/pypi/guardrails-ai/json` | Apache-2.0. 0 default-branch commits from 2026-09-08 to access vs 77 from Jun 1 to Sep 8. Latest PyPI 0.11.0 (2026-08-14T14:22Z). README announces hosted Hub inference discontinued, cutoff moved from Aug 6 to Aug 25, 2026 | context for row 034 |
| 2026-10-16 | September | HN lead → `GET https://finance.yahoo.com/technology/ai/articles/openai-anthropic-costs-push-more-160523322.html` | Bloomberg syndication (datePublished 2026-09-21T16:05Z) read raw and included. Bloomberg original `bloomberg.com/news/articles/2026-09-09/legal-ai-startup-harvey-hits-15-6-billion-value-with-550-million-round` returned **HTTP 403**: **inaccessible**, headline used only to record the $15.6B figure conflict | 2 / 1 / 1 |
| 2026-10-16 | Oct 1–12 | blog: `harvey-to-open-boston-office`, `how-we-built-harvey-connector-library`, `harvey-partners-with-legalscape-…`, `tc-energy-deploys-…`, `motion-to-dismiss-workflow-lexisnexis`, `building-harveys-mcp-policy-engine`, `trusted-legal-ai-for-the-us-public-sector-…`, `harvey-to-open-tokyo-office`, `ogier-adopts-harvey-firmwide` | 3 rows (+ v1.2.0, Vals). Boston, Legalscape, TC Energy, LexisNexis MTD and Ogier excluded. Tokyo was used in §5 only | 9 / 9 / 6 |
| 2026-10-16 | Oct 1–12 | `GET https://vals.ai/benchmarks/hlab` ("Updated 10/12/2026"); `https://www.vals.ai/benchmarks/lab` returned 404 | included as a mutable third-party leaderboard | 1 |
| 2026-10-16 | cross-window | HN Algolia `search_by_date` with `created_at_i` 1775952000–1792022400 for `Harvey AI` (12), `Harvey legal` (6), `harvey.ai` (6), `Legal Agent Benchmark` (5) | used as leads (Bloomberg/Yahoo, Artificial Analysis). Most hits were Harvey's own posts with 0–4 points. Vespper, use-citations, termsinator and Paper Lantern are unrelated. A freemalta "$11B" story was not opened | 29 hits / all titles / 0 direct rows |
| 2026-10-16 | cross-window | web search `Harvey legal AI 2026 criticism OR lawsuit OR outage OR hallucination` | Only vendor-comparison and SEO blogs were returned (techsy, metavert, fast.io, sonomos, refontelearning, useluminix, aiagentrank), graded **E0** and not used. A summary claim that Sullivan & Cromwell apologized for AI errors was **not verified** and is unrelated to Harvey in any source read. No lawsuit, regulatory action or security advisory naming Harvey was found | unknown / 9 / 9 |
| 2026-10-16 | post-window | blog `building-a-frontier-in-house-organization` (Oct 13), `legal-work-orchestration` (Oct 15), Drakopoulos (Oct 15) | **excluded** as out of window | — |

## Months with thin or no independent coverage

- **Apr 12–30:** no independent reporting was found. All three rows are first-party.
- **June:** the only independent element is a third-party contributor's merged PR (#76) and Vals AI's statement about it.
- **August:** no independent news. The independent elements are public GitHub issues and the official status record.
- **Oct 1–12:** only the Vals AI partner leaderboard.

Every month has at least three ledger rows. No month was empty.

## Inclusion, deduplication and conflicts

- **Included:** 43 rows: Apr 3, May 7, Jun 8, Jul 7, Aug 6, Sep 7, Oct 5. Every row cites a URL that was fetched as raw text or queried by API. No row relies on a search snippet alone.
- **Duplicate groups:** `088-005` covers the LAB launch (Harvey) and the LawSites commentary on the same launch. `088-013` covers the Connector Library announcement (Jun 8) and its engineering post (Oct 1). The Harvey II row also links the Memory post (Aug 26) as its check URL instead of counting it as a separate row.
- **Date conflicts recorded, not resolved:**
  - Guardrails acquisition: Sep 8 on guardrailsai.com vs Sep 9 (`datePublished` 12:23Z) on harvey.ai.
  - Boston office: `datePublished` 2026-10-01T12:01Z vs newsroom label "October 2, 2026".
  - GE Aerospace: `datePublished` 2026-09-01T11:57Z (newsroom also Sep 1; the post is absent from the sitemap). Not ledgered.
  - TX-RAMP: certification effective Sep 22 but announced Oct 8. The ledger uses Oct 8 as the publication date and Sep 22 as the event date.
- **Figure conflicts:**
  - Valuation: $15.5B (Harvey, TechCrunch) vs $15.6B (Bloomberg headline and syndicated text).
  - LAB size: "more than 1,200" and "1,250" in the same post, vs a README badge showing 2,010 tasks on access.
  - Opus 4.8 all-pass: 10.4% (Harvey internal) vs 7.5% (Artificial Analysis LAB-AA). The harnesses, task sets and judges differ, so the figures are not comparable.
- **Figures confirmed against raw text** (grep of saved text; 122 string checks, 0 misses after re-checking two that failed only because of HTML tags in the raw file):
  - Usage and agents: 700,000+ tasks/day; 50 million terms/week; 500+ agents.
  - LAB: 1,200+/1,250 tasks, 24 practice areas, 75,000+ criteria. Initial results: 7.1/5.4/4.2/2.1/0.8%, $50.90, ~22 minutes.
  - Model scores: 90.9% (Opus 4.7); 10.4%/91.1% (Opus 4.8); 13.3%/93.4% and 30-day retention (Fable 5); 92.7%/2.5% (GPT-5.6 Sol).
  - Deployment counts: 1,500+ deployments; 110,000+ connections.
  - Post-training: 0.913/0.126 (GLM-5.1); 84.1%/91.93%/54.8% (Review Table); Tenet's rank-64 LoRA, ~1,750 environments, 150 B300 GPUs, 2 months, +9/+2 pp; RLM 39.1 pp and 29.9%→63.0% on 50 held-out rooms.
  - Artificial Analysis: 14.2%, 7.5%, 13 of 28, ~$1.3/~$8.2, 120 tasks.
  - Acquisitions: Benchmark (third acquisition, >$100M net-new ARR, 125+ asset managers); Guardrails (fourth acquisition, 250,000 downloads/month).
  - Funding and adoption: $550M/$15.5B, 80% of Am Law 100, five of the Fortune 10; 3,000 customers, 200,000 lawyers, 70 countries.
  - Bloomberg: ~50%→−50%, twenty-fold token usage, Mercor.
  - Other: TX-RAMP effective Sep 22; Vals 25.42% (updated 10/12/2026).
  - From the GitHub API: tag, release and issue dates, PR #76 dates, and commit counts.
- All of the above remain **vendor or press statements**, not verified measurements.
- **Untrusted-content note:** fetched pages were treated as data. No page contained instructions directed at an AI agent or researcher. The LAB CHANGELOG says its audience includes "AI assistants analyzing results" (text wrapped across lines) with a git command for checking comparability. That is documentation for users, not an instruction to this researcher, and it was not executed. Search-tool summaries were treated as leads only.

## Missing, inaccessible or not attempted

- **Inaccessible:** the Bloomberg original (HTTP 403).
- **Not found:** Artificial Lawyer and Law.com coverage of LAB.
- **Not read:**
  - Anthropic's help-centre page on Fable 5 retention.
  - Microsoft, Intapp and Everlaw partner-side pages.
  - The ISO 42001 certificate and certification body.
  - The Texas DIR TX-RAMP listing.
  - The Alt-Counsel post cited by LawSites.
  - The LAB task-document licensing and provenance.
  - Harvey's terms and data-processing addendum (updated 2026-09-30 per the sitemap).
- **Not established:**
  - Tenet weights or a model card.
  - The first two 2026 acquisitions.
  - Status history before July 2026.
  - Archived (Wayback) copies of mutable pages.
- **Not done:** no product was executed, no account created, no benchmark run, no paywall circumvented, and no energy measurement taken. SEC/EDGAR was not contacted.
- **Reproduction:** re-run the requests above with UTC timestamps and save raw HTML hashes. Before any evidence is promoted beyond provisional status, an independent human should spot-check:
  - the funding and margin rows (CI2026-088-035, -037);
  - the acquisition row (-034) and the Guardrails commit-count observation;
  - the GitHub issue rows (-021, -028, -031);
  - two model-score rows against the raw posts.
