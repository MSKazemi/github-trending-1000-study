# Factory (021) — seven-segment source-query and inclusion log (2026-10-16)

> **Provisional source-lead screen (upgraded 2026-10-16):** this log, the [report](021-factory.md), [event ledger](021-factory.events.csv) and [source-QC note](021-factory.source-qc-2026-10-16.md) are **provisional, AI-assisted documentary source leads**. They are **unreviewed by a qualified human**; factual/link, source-access/rights and methods review pending. Merging is not scientific or security sign-off; issue #88 was closed on maintainer instruction (2026-10-16) with these review gates still open — reopen it if review finds a defect.

**Window:** 2026-04-12 … 2026-10-12 inclusive. **Screened:** 2026-10-16 by an AI assistant, read-only public pages, no login, no paywall, no scraping of github.com/trending, no personal identifier in any request. **Not exhaustive.** Search-engine result totals and query-run UTC times were not preserved: counts are **unknown**, not zero. The previous pass's search expression (`site:factory.com/news 2026 "software factories" "routing" "cost" product; 2026 August September 2026 droid`) is recorded in the [report's preserved section](021-factory.md#earlier-screen-preserved) and in [021-factory.events.json](021-factory.events.json); there was no older separate search-log file.

**Name-collision control:** "Factory" is a generic word. Only sources about **Factory (factory.com / factory.ai, maker of Droid coding agents; GitHub org `Factory-AI`)** were kept. Generic "software factory", "AI factory" (e.g. GPU data-centre "AI factories") and unrelated companies named Factory were excluded on sight.

## A. Fetches and API calls actually run

| # | Tool | Exact request | Result / use |
|---|---|---|---|
| F1 | WebFetch | https://factory.com/news (news index) | 19 posts listed, 2026-08-14 … 2026-10-15; "View more" for older posts (not paged further). Basis for Aug–Oct candidates. |
| F2 | WebFetch | https://docs.factory.ai/changelog | 308 → https://docs.factory.com/changelog → **404** |
| F3 | WebFetch | https://docs.factory.com/changelog/cli-updates (offsets 0 and 100000) | Dated CLI/Desktop release entries 2026-04-20 … 2026-10-12 (≈ v0.105 … v0.239.1). Characters 200000+ (pre-April) not read. |
| F4 | gh api | `orgs/Factory-AI/repos?per_page=100&sort=updated` | 22 public repos with licence / pushed dates |
| F5 | gh api | `repos/Factory-AI/{factory,droid-action,droid-sdk-python,droid-sdk-typescript,droid-code-review,legacy-bench,factory-plugins,tui-test,vfs,eslint-plugin}` + `/releases` | droid-action v5–v10 and vfs v1.0.0–v1.1.1 in window; others no in-window releases |
| F6 | gh api | `/advisories?cve_id=CVE-2026-42876` | GHSA-fq7h-9x26-6j22, published 2026-05-08, medium, external-secrets |
| F7 | curl (no auth, no custom headers) | https://huggingface.co/api/models?author=factoryai&full=true | 2 models created 2026-06-28; no `license:` tag |
| F8 | WebFetch | each existing ledger URL (6) | see [source-QC](021-factory.source-qc-2026-10-16.md) |
| F9 | WebFetch | factory.com/news/{series-c, droid-shield-2-0, automated-security-review, open-secure-ai-alliance (via factory.ai 307), personas-and-connectors, what-it-takes-for-coding-agents-to-complete-large-software-tasks, claude-marketplace, 5-billion-valuation, factory-private, legacy-bench-specialized-intelligence-index, openai-b2b-marketplace, automations, factory-analytics-transparency, mentlio, droids-now-have-a-fleet-of-sandboxes, factory-japan} | titles/dates/availability read with narrow prompts |
| F10 | WebFetch | https://www.gunder.com/en/news-insights/client-news/factory-announces-dollar150-million-series-c-at-dollar15-billion-valuation | Apr 16 2026, $150M Series C, $1.5B, Khosla lead |
| F11 | WebFetch | https://www.cityam.com/?p=2447558 | Aug 4 2026, unconfirmed >$3.5bn report |
| F12 | WebFetch | https://thenextweb.com/news/factory-200m-5bn-valuation-ai-coding-agents | Sep 17 2026; restates company release |

## B. WebSearch queries (4 of ≈6 budget)

| # | Exact query | Notable results (search-result level unless opened in A) | Decision |
|---|---|---|---|
| S1 | `Factory AI Droids coding startup raises $200 million $5 billion valuation September 2026` | TNW (opened F12), Morningstar/Dow Jones, dealroom, runtimewire, local radio syndications | One independent restatement kept as `independent_check_url`; syndications deduplicated, not rows |
| S2 | `Factory.ai Droid coding agent vulnerability OR security issue OR outage 2026` | Search summary found **no** reported Factory/Droid vulnerability or outage; pointed to Droid Shield 2.0 and Automated Security Review; Docker/Aviatrix/threatcluster generic agent-risk pages | Negative result logged; absence of a hit ≠ absence of incidents. Generic pages excluded (not Factory-specific) |
| S3 | `Factory AI Droid Series C $150 million $1.5 billion valuation April 2026` | Gunderson (opened F10), City AM (opened F11), kucoin/tech-insider/texxr/sacra/plushcap | dealroom item conflating "$200M Series C" noted as an aggregator error, not used |
| S4 | `Factory Droid Shield 2.0 OR "Automated Security Review" OR CVE-2026-42876 July 2026` (allowed domains factory.com, factory.ai, github.com) | factory.com/news/automated-security-review, /droid-shield-2-0, factory.ai/news/open-secure-ai-alliance; third-party repos with `factory-droid[bot]` PRs | Three vendor posts opened (F9); third-party bot PRs excluded (individual users' repos, not company events) |

**Not executed (budget / scope):** `"Factory" Droid May 2026 independent review`; `Factory Droids Terminal-Bench 2026 leaderboard`; `site:news.ycombinator.com Factory droid 2026`; `Factory status page incident 2026`; second page of factory.com/news ("View more", April–July posts); `"Matan Grinberg" interview 2026 roadmap`. SEC/state registries were **not** queried (identity-bearing request requirements).

## C. Per-segment screen

| Segment | Candidates seen | Included rows (event_id) | Excluded / notes | Counts found/screened/excluded |
|---|---|---|---|---|
| Apr 12–30 | Series C (Apr 16), droid-action v5 (Apr 16), changelog v0.105–v0.114, Automated QA (Apr 23) | CI2026-021-004, -005, -006, -001 | v0.105.0 AutoWiki GitHub-wiki sync, v0.109.x, v0.112.0 (security review on by default), v0.113/v0.114 not given separate rows (logged here); Factory-AI/legacy-bench repo created 2026-04-02 (pre-window) | unknown |
| May | GHSA (May 8), changelog v0.118–v0.126 | CI2026-021-007, -008 | v0.120.0 BYOM Droid Computer controls, v0.123.0 Mission Control token usage, v0.124.0 deep/shallow security review modes: logged, no rows; vfs repo created 2026-05-09 (no release until Aug) | unknown |
| June | Router (Jun 1), ASR (Jun 11), blocklist (Jun 12), Factory 2.0 (Jun 15), AutoWiki (Jun 17), v0.140/v0.144/v0.152/v0.156.2 | CI2026-021-002, -009, -010, 021-E01, CI2026-021-003 | v0.140.0 automated incident investigation, v0.144.0 risky-command classification, v0.152.0 org MCP/marketplace governance, v0.156.2 org-wide hooks governance: logged, no rows; HF Droid Shield weights created Jun 28 (see Jul 1 row) | unknown |
| July | Droid Shield 2.0 (Jul 1), v0.167/v0.169/v0.172/v0.176/v0.179, Alliance (Jul 28) | CI2026-021-011, -012, -013 | v0.179.0 (Jul 23) folded into -012 claim; Factory-AI/factory repo created 2026-07-29 (no licence, no releases) — repo creation not an event row | unknown |
| August | City AM (Aug 4), vfs v1.0.0–1.1.1 (Aug 8–10), droid-action v6 (Aug 7)/v7 (Aug 18), Guild (Aug 14), partner network (Aug 19), model routing (Aug 24), Connectors (Aug 25), research (Aug 27), Japan (Aug 31) | CI2026-021-014, -015, -016, 021-E02, CI2026-021-017, -018 | Factory Guild (Aug 14), partner network (Aug 19), Japan office (Aug 31, opened) and droid-action v6 logged but not rows (community/GTM, low study relevance) | unknown |
| September | Claude Marketplace (Sep 9), raise (Sep 15), Factory Private (Sep 18), Router savings (Sep 23), Legacy-Bench (Sep 24), OpenAI marketplace (Sep 29), Automations (Sep 30), changelog v0.213–v0.230, droid-action v8/v9 | CI2026-021-019, -020, -021, 021-E03, CI2026-021-022, -023 | OpenAI marketplace (opened) merged into -019 as `independent_check_url` (same procurement-channel family, not independent corroboration); v0.216.0 managed computers on Pro, v0.227.0 Droid Shield Git scanning logged, no rows | unknown |
| Oct 1–12 | Analytics (Oct 2), droid-action v10 (Oct 6), Head of Federal hire (Oct 8), Mentlio (Oct 9), Environments (Oct 12), changelog v0.231–v0.239.1 | CI2026-021-024, -025, -026, -027 | Oct 8 executive hire excluded (personnel, no product evidence). **Out of window, excluded:** OpenCompute (Oct 14), Blackstone case study (Oct 15) | unknown |

## D. Inclusion rules applied

- Publication date inside window; `published_utc` is the displayed source date. `event_date_utc` is filled only for GitHub releases (API `published_at` date).
- Multiple rows citing https://docs.factory.com/changelog/cli-updates are **distinct dated entries on one changelog page**, not independent corroboration.
- Vendor posts = E1; GitHub releases and changelog entries = E2 official dated records; GitHub Advisory/third-party press = second-party evidence but still not functional replication. No row is E3+.
- Funding/acquisition rows are `reported_undetermined`/`announced_only`; they are context, never adoption or quality evidence.
