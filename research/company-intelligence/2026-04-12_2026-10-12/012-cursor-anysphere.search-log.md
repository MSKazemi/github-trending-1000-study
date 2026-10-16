# Cursor / Anysphere (012) — provisional source-query and inclusion log

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** Companion to the [report](012-cursor-anysphere.md) (see its "Standardisation upgrade (2026-10-16)" section) and the [event ledger](012-cursor-anysphere.events.csv) for [#78](https://github.com/MSKazemi/github-trending-1000-study/issues/78). Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

**Window:** 2026-04-12 to 2026-10-12 inclusive (UTC dates). **Accessed:** 2026-10-16. **Method:** raw-HTML retrieval with `curl` and a generic `Mozilla/5.0` User-Agent. No personal identifier, email or credential was sent to any site. Text was extracted locally and every number, price, version, date and quote used in a ledger row was confirmed with `grep`. Read-only `gh api` calls were used for GitHub security advisories and repositories. The npm registry JSON and the PyPI release RSS were used for SDK packages. The Hacker News Algolia API was used for independent discovery, plus two public web searches. Before each host was fetched, its `robots.txt` was checked for a generic browser and for `ClaudeBot`, `Claude-User`, `anthropic-ai` and `Claude-SearchBot` (one lapse is recorded below). **This is not exhaustive retrieval.** Search-engine result totals were not exposed and are recorded as unknown, not zero. No page snapshots or hashes were committed, and pages may change after access.

## Query and source log by segment

| Date | Segment | Exact query or source request | Opened / decision | Found / screened / included |
|---|---|---|---|---|
| 2026-10-16 | all | `GET https://cursor.com/robots.txt` | `/blog`, `/changelog`, `/origin` are allowed. Disallowed paths include `/api/`, `/pricing-history`, `/*/docs`, `/agents`. The disallowed paths were not fetched | — |
| 2026-10-16 | all | `GET https://cursor.com/changelog/rss.xml` | 50 items, 2026-03-05 to 2026-10-13. 43 fall inside the window (first logged as 40; corrected by the 2026-10-16 spot-check, which counted 6 items before 2026-04-12 and 1 after 2026-10-12), plus the 2026-10-13 "Origin App Marketplace" item, which is **out of window** and excluded | 43 / 40 titles logged as screened / 24 changelog pages fetched raw |
| 2026-10-16 | all | `GET https://cursor.com/sitemap_index.xml` → `sitemap.xml` (195 URLs, 120 blog). Also `/blog`, `/blog/topic/{product,research,company,customers,press}` | The sitemap's newest blog post is 2026-08-14. The `/blog` index adds 9 later posts that are missing from the sitemap. `datePublished` was extracted from 69 blog pages | 69 dated / ~40 in-window screened / 17 cited |
| 2026-10-16 | all | `GET https://cursor.com/atom.xml` | Stale feed (`<updated>` 2024-09-24, 8 entries). Not used | 0 |
| 2026-10-16 | all | `gh api repos/cursor/cursor/security-advisories --paginate`, then each GHSA individually | 33 advisories in total, 6 published in the window, all ledgered (rows 011, 015, 016, 024, 026, 027). No advisory matching the Mindgard `git.exe` report was found | 6 / 6 / 6 |
| 2026-10-16 | all | `GET https://registry.npmjs.org/@cursor/sdk` and the `sdk-1.0.37.tgz` tarball (read as a tar stream, not extracted or executed) | Created 2026-04-26T19:37Z. 32 versions; latest 1.0.37 on 2026-10-07. `LICENSE.md` reads "All rights reserved" | used in row 003 |
| 2026-10-16 | all | `GET https://pypi.org/rss/project/cursor-sdk/releases.xml` (the PyPI JSON API was not used) | 24 items. First items are 0.0.0 (placeholder) and 0.1.0 on 2026-05-13; latest 1.0.37 on 2026-10-07 | used in rows 003, 014 |
| 2026-10-16 | all | `gh api orgs/cursor/repos?sort=created` | New in-window repos: `cookbook` (no licence), `terraform-provider-cursor` (Apache-2.0), `minisqlite` (no licence), `mixture-of-kittens` (Apache-2.0), `sdk-bridge` (MIT). Star counts were seen but are not used as evidence | 5 / 5 / 2 cited |
| 2026-10-16 | all | HN Algolia `search_by_date`, `tags=story`, window bounds 1775952000–1792022400, queries `Cursor`, `Anysphere`, `Cursor SpaceX`, `Cursor AI`, `Cursor editor`, `Cursor agent`, `Cursor vulnerability`, `Cursor pricing`, `Cursor Composer`, `Cursor Bugbot`, then `cybercriminals Cursor`, `OpenAI Cursor partnership`, `Cursor Origin`, `Cursor outage`, `Cursor sandbox escape`, `Cursor Chinese model`, `Cursor Kimi`, `Anysphere probe` | 209 title-matched hits in the first pass. Many are unrelated (mouse cursor, Show HN tools). About 60 relevant hits were screened; linked articles were fetched only where `robots.txt` allowed it | unknown / ~60 / 10 rows from independent or community sources |
| 2026-10-16 | Apr 12–30 | blog `spacex-model-training`, `multi-agent-kernels`, `canvas`, `better-models-ambitious-work`, `app-stability`, `typescript-sdk`, `continually-improving-agent-harness`. Changelog `3-1`, `04-14-26`, `04-15-26`, `04-24-26`, `sdk-release`, `04-30-26` | 4 vendor rows. UI/QoL releases (3.1 tiled layout, CLI debug mode, canvases) and engineering essays were excluded for focus | — |
| 2026-10-16 | Apr 12–30 | HN titles 2026-04-21: Reuters / Bloomberg / NYT / Guardian / SpaceX X post on a "$60B option/agreement to acquire". Business Insider on a Mistral team-up | **Not read.** Reuters and WSJ disallow all agents. NYT, Guardian, Bloomberg and The Verge disallow Claude agents. Business Insider disallows `ClaudeBot`. The option claim is E0 and appears only in the row-001 limitation | unknown / 6 / 0 |
| 2026-10-16 | Apr 12–30 | [Nextgov 2026-04-29](https://www.nextgov.com/artificial-intelligence/2026/04/house-panels-probe-airbnb-anysphere-over-use-chinese-ai-models/413207/) (the truncated first URL returned 404; the full URL was read raw) | Included (row 004). The Bloomberg version was disallowed and the Semafor original was not read | 1 / 1 / 1 |
| 2026-10-16 | May | changelog `05-01-26`, `05-04-26`, `05-06-26`, `05-07-26`, `05-11-26` (×2), `05-13-26` (×2), `composer-2-5`, `05-19-26`, `05-20-26` (×2), `auto-review`. Blog `may-2026-bugbot-changes`, `composer-2-5`, `cursor-leads-gartner-mq-2026`, `faire`, `paypal` | 6 rows. Excluded: Jira/Teams integrations, shared canvases, context-usage UI, the Gartner MQ post (analyst-ranking marketing) and customer case studies (Faire, PayPal, NAB, Amplitude) | — |
| 2026-10-16 | June | changelog `enterprise-organizations`, `sdk-updates-jun-2026`, `canvas-improvements`, `design-mode-improvements`, `bugbot-updates-june-2026`, `cloud-in-agents-window`, `06-18-26`, `customize`, `ios-mobile-app`, `team-marketplace-updates`. Blog `teams-pricing-june-2026`, `reward-hacking-coding-benchmarks`, `agent-autonomy-auto-review`, case studies | 7 vendor rows. Organizations, design mode, automation and marketplace updates were excluded for focus | — |
| 2026-10-16 | June | HN: Reuters/WSJ/BBC/TechCrunch/CNBC/Verge/Forbes/Bloomberg on the 2026-06-16 $60B deal. HN "Tell HN" on iOS privacy settings (2026-06-30). The New Stack on pricing (2026-06-06). Mindgard 0day post | Deal originals **not read**: robots disallow (Reuters, WSJ, Bloomberg, NYT, Verge, CNBC). TechCrunch, BBC and The New Stack disallow `ClaudeBot` and do not explicitly allow `Claude-User`. Forbes returned 403. The deal is covered by an E0 row (HN item page, 018), corroborated later by Engadget. The HN iOS post was read raw (023). Mindgard was read raw (019) | unknown / ~14 / 3 |
| 2026-10-16 | July | changelog `side-chat`, `slack-improvements`, `router`, `cursor-start`, `ipad`. Blog `cfo-council`, `grok-4-5`, `grok-4-5-model-card`, `agent-swarm-model-economics`, `cloud-agent-environment`, `vercel` | 4 vendor rows. Excluded: side chats, Slack, iPad, the CFO essay, the model card (folded into row 025) and the Vercel case study | — |
| 2026-10-16 | July | HN `Cursor sandbox escape`: BleepingComputer (2026-07-20), [Pillar Security](https://www.pillar.security/blog/one-docker-socket-to-rule-them-all-escaping-codex-cursor-and-gemini-clis-sandboxes) (2026-07-20), a Medium post | BleepingComputer's `robots.txt` returned 403, so it was treated as inaccessible. Medium disallows `ClaudeBot`. Pillar was read raw and used as the independent check for row 026 | unknown / 4 / 0 new rows |
| 2026-10-16 | August | changelog `google-workspace-plugins`, `08-13-26`, `origin-code-hosting`, `08-19-26`, `start-from-scratch`. Blog `mixture-of-kittens`, `how-cursor-router-works`, `grok-4-6`, `aiuc-1`, `firetiger`, `builds`, `joining-spacex`, `git-at-any-scale`, `imdex` | 8 vendor rows. Excluded: Google Workspace plugins, the 08-19 harness roundup, the router explainer, the Origin engineering essay and the IMDEX case study | — |
| 2026-10-16 | August | HN: Engadget 2026-08-15 (read raw, row 037). TechCrunch close and Origin stories (disallow `ClaudeBot`). [status incident l9h9vrd726jv](https://status.cursor.com/incidents/l9h9vrd726jv) (read raw, row 039). VentureBeat Origin story (HTTP 429 security checkpoint, inaccessible). Gizmodo Musk pep-talk story (gossip, not opened). a16z post (investor commentary, not opened) | 2 rows | unknown / ~10 / 2 |
| 2026-10-16 | August | Web search `Russian-speaking cybercriminals used Cursor AI to hack seven companies August 2026`. Reuters original disallowed. CTV and BNN Bloomberg disallow `anthropic-ai` | [Daily Maverick Reuters syndication](https://dailymaverick.co.za/article/2026-08-28-russian-speaking-cybercriminals-used-spacex-s-cursor-ai-tool-to-hack-seven-companies) read raw (row 041). eSecurity Planet read raw as the independent check. ynetnews was fetched and not used. letsdatascience and arynews are aggregators and were not opened | unknown / 9 / 1 |
| 2026-10-16 | Aug–Sep | Web search `OpenAI ends Cursor partnership SpaceX acquisition August 2026`. `openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/` | **openai.com returned HTTP 403 and was not read.** Forklog disallows `ClaudeBot`/`anthropic-ai`. Dealroom and basenor are aggregators and were not opened. The search tool's summary was treated as a lead only. [Free Press Journal](https://www.freepressjournal.in/tech/openai-ends-cursor-partnership-over-spacex-buyout-elon-musk-says-i-couldnt-care-less) was read raw (row 042). The HN item page was read as a pointer | unknown / 9 / 1 |
| 2026-10-16 | September | changelog `self-hosted-machines`, `projects`, `rollouts-and-security-reviewer`. Blog `basis`, `nokia`, `grab`, `improved-token-efficiency`. Blog index entry linking `x.ai/news/grok-4-7` (read raw; x.ai robots allows it) | 5 rows. Customer case studies (Basis, Nokia, Grab) excluded | — |
| 2026-10-16 | September | [Manifold Security GitSpawn](https://www.manifold.security/blog/ai-coding-agents-git-hijack) (2026-09-01) and [Armature](https://armature.tech/blog/which-tools-coding-agents-install) (2026-09-03), both read raw | 2 rows. A 2026-09-17 HN "major outage" post links only to the status-page root, so there is no dated incident record to cite and it was not ledgered | unknown / 4 / 2 |
| 2026-10-16 | Oct 1–12 | changelog `remote-control-local-agents` (2026-10-06) | 1 row. No other in-window blog or changelog item was found for Oct 1–12. The 2026-10-13 Origin App Marketplace and the 2026-10-13 x.ai pricing HN post fall **after** the window | 1 / 1 / 1 |

## Inclusion, deduplication and conflicts

- **Included:** 50 rows. By segment: Apr 12–30: 5. May: 7. Jun: 11. Jul: 7. Aug: 12. Sep: 7. Oct 1–12: 1. Every row cites a URL that was fetched raw or queried by API. Row 018 relies on an HN item page plus later press, so it is graded E0 and labelled that way.
- **Carried forward:** the earlier report's three events are rows 036 (012-E01), 044 (012-E02) and 046 (012-E03). The crosswalk is in the report's upgrade section.
- **Duplicate groups:** `012-ACQ` (rows 001, 018, 036, 037) covers one change of control documented four ways. `012-SANDBOX` groups the six sandbox advisories and the Auto-review run mode. `012-GITEXEC` covers two independent reports of untrusted-repository code execution through git; they describe different mechanisms (`git.exe` lookup vs `.git/config`), so the group links a class of issue, not one bug. Other groups: `012-SDK`, `012-PRICE`, `012-SECREV`, `012-CLOUDENV`, `012-IOS`, `012-ORIGIN`, `012-GROK`, `012-KIMI`, `012-OPENAI`, `012-MISUSE`.
- **Date conflicts recorded, not resolved:**
  - The npm `@cursor/sdk` first publish (2026-04-26) predates the SDK announcement (2026-04-29).
  - Mindgard's JSON-LD `datePublished` is 2026-06-17, while the page shows "Last Updated: September 24, 2026" and the post was submitted to HN on 2026-07-14.
  - GHSA-whx2-4gvm-m3r3 was fixed 2026-03-31 but published 2026-07-06.
  - The OpenAI decision is dated 2026-08-29 (HN submission of the openai.com page), and the press copy is dated 2026-08-31.
  - The Reuters dateline is 2026-08-27 and the syndicated copy is dated 2026-08-28.
  - `cursor.com/origin` was submitted to HN on 2026-06-16, but the changelog's early-beta rollout is 2026-08-17. The June state of the page is unknown.
- **Possible post-publication edits:** the Composer 2.5 blog (2026-05-18) names "SpaceXAI". Engadget says that name dates from July, so the vendor page may have been edited. No archived copy was checked.
- **Figures confirmed against raw text (grep of saved page text):**
  - Composer 2.5 prices ($0.50/$2.50, $3.00/$15.00 per M) and its "Kimi K2.5" base.
  - Bugbot $40/seat, "after June 8th, 2026", $1.00–$1.50 per run; ~90 s vs ~5 min, 0.62 vs 0.56 bugs per review, ~22% cheaper.
  - Teams $32/$40 and $96/$120 per seat, Premium 5x usage, "July 1st, 2026".
  - Cursor Start ₹649 and "July 28, 2026".
  - Reward-hacking figures: 63%; 87.1%→73.0%; 74.7%→54.0%.
  - Token efficiency: 7%, ~66%, 46.9%, 60%.
  - 835-page SQLite manual; Builds 3x / 10x; AIUC-1 "70% of the Fortune 500" and the Schellman audit.
  - Grok 4.7 $2/$6 and 46.3% CursorBench 4.0; "trillions of tokens of Cursor data".
  - Engadget "$60 billion" and the April/June/July sequence.
  - FPJ "November 12", "Astra", "roughly 5 per cent".
  - Reuters/Daily Maverick "28 chat sessions", "Belgian chemical company and at least six other firms", and "did not return messages".
  - Manifold "8 July 2026 … Closed as duplicate … Patched"; Armature 16,893 / 1,163 / 75.
  - Status incident timestamps 14:34–20:40 UTC; Nextgov committee names and the Kimi disclosure.
  - Advisory versions and severities, from per-GHSA `gh api`.

  All of these remain **vendor, researcher or press statements**, not verified measurements.
- **Not every figure on every cited page was checked.** Only the figures quoted in the ledger were checked.

## Access-rule lapse (disclosed)

- On 2026-10-16 this screen fetched `https://status.cursor.com/api/v2/incidents.json` once (HTTP 200). The robots check had been run only for `/incidents/<id>` and `/history`, and `status.cursor.com/robots.txt` has `Disallow: /api/` for all agents. The response file was **deleted without being used**. No ledger row, count or statement in this screen relies on it. The only status-page row (039) comes from an allowed incident page that was discovered through HN. The JS-rendered `/history` page exposed no incident list, so status-page coverage is **incomplete**: in-window incidents other than 2026-08-17 are not ledgered.

## Untrusted-content note

Fetched pages were treated as data. A pattern scan of the saved pages found no instructions directed at an AI agent or researcher. The scan searched for phrases such as "ignore previous instructions" and "if you are an AI". Its only hit was a false positive in an ordinary HN comment. The scan is not exhaustive. Web-search tool summaries were treated as leads only. No figure was taken from a summary without reading the raw page.

## Missing, inaccessible or not attempted

- **Inaccessible or not read:**
  - Reuters, WSJ, Bloomberg, NYT, The Verge, Guardian, CNBC: robots.txt disallows the user agent or a Claude agent.
  - TechCrunch, BBC, The New Stack, Business Insider, Medium, Forklog: `ClaudeBot` disallowed and no explicit `Claude-User` allow.
  - Forbes (403), openai.com (403), VentureBeat (429 checkpoint), BleepingComputer (robots 403).
  - Semafor's original House-probe report.
  - The Gambit Security and CloudSek reports.
  - The congressional letters.
  - SpaceX/xAI filings; this repository forbids contacting SEC EDGAR.
- **Not attempted:**
  - Cursor docs pages under `/docs`.
  - `forum.cursor.com` threads.
  - Cursor's pricing page history: `/pricing-history` is disallowed.
  - Wayback copies of mutable vendor pages as of 2026-10-12.
  - NVD records for the six CVEs.
  - Cursor terms of service and data-use policy changes.
- No product was installed or executed, no account was created, no paywall or access gate was bypassed, and nothing was measured for energy.
- **Reproduction:** re-run the requests above with UTC timestamps and save raw HTML hashes. An independent human should then spot-check:
  - the acquisition rows (001, 018, 036, 037);
  - the security rows (011, 015, 016, 019, 024, 026, 027, 041, 043);
  - the OpenAI row (042);
  - two pricing rows (008, 013).

  These spot-checks should happen before any evidence is promoted beyond provisional status.
