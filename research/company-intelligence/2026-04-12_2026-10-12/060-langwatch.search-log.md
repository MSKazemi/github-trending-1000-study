# LangWatch (060) — provisional source-query and inclusion log

> **PROVISIONAL / AI-assisted, not human-reviewed (2026-10-16).** This log, the [report](060-langwatch.md) and the [event ledger](060-langwatch.events.csv) are an AI-assisted first-pass documentary screen for [issue #128](https://github.com/MSKazemi/github-trending-1000-study/issues/128). Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

**Window:** 2026-04-12 to 2026-10-12 inclusive (UTC). **Searched/accessed:** 2026-10-16. **Method:** [company-intelligence protocol](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md). **Tools:** a general web-search tool (results returned as titles/URLs plus a model summary; total hit counts not exposed), `curl` of public pages with raw-text extraction, the GitHub REST API via `gh api` (releases, commits, security advisories, repository licence metadata), and the PyPI JSON and npm registry APIs. Search hit totals and exact run times in UTC were **not captured**; they are unknown, not zero. No page snapshots or byte hashes were archived.

## 1. Primary-source sweeps (not keyword searches)

| Source | How it was enumerated | In-window items found | Notes |
|---|---|---:|---|
| [langwatch.ai/sitemap.xml](https://langwatch.ai/sitemap.xml) → `/blog/*` | All blog URLs listed; first 40 fetched with `curl`; `datePublished` and visible date read from raw HTML | 22 posts dated 2026-04-14 … 2026-09-22 | No blog post dated 2026-09-23 … 2026-10-12. Posts after 40th position are pre-2026-01 |
| [langwatch.ai/changelog](https://langwatch.ai/changelog) and sitemap `/changelog/*` | All 38 entries fetched; dates from raw HTML | 17 entries dated 2026-04-13 … 2026-09-27 | Gaps: no entries between 2026-04-14 and 2026-05-30, or between 2026-07-13 and 2026-08-01; none after 2026-09-27 |
| GitHub releases, [langwatch/langwatch](https://github.com/langwatch/langwatch/releases) | `gh api --paginate repos/langwatch/langwatch/releases` | 188 release objects in window (409 total) | Many are duplicate tag spellings (`langwatch@vX`, `vX`, `langwatch-X`) and SDK pre-releases; 32 beta tags on 2026-04-27/29. Only milestone releases are ledgered |
| GitHub releases, [langwatch/scenario](https://github.com/langwatch/scenario/releases) | same | 37 in window (97 total) | 1.0.0 on 2026-07-24; latest in window 2026-10-07 |
| GitHub releases, better-agents / agent-plugin / skills / kanban-code | same | 0 / 0 / 0 / 7 | agent-plugin and skills releases are tagged in the monorepo instead; kanban-code (v0.1.26…v0.1.32) excluded as not in scope of the observability product |
| LICENSE history | `gh api repos/.../commits?path=LICENSE.md` and `path=LICENSE` | 2 in-window licence commits | langwatch BSL 1.1 → Apache 2.0 (2026-05-17); scenario AGPLv3 → Apache 2.0 (2026-04-23) |
| GitHub security advisories | `gh api repos/langwatch/langwatch/security-advisories`; same for scenario; global `advisories?affects=` for `langwatch` and `@langwatch/scenario` | 1 (GHSA-h25p-f8f6-2ccf, 2026-08-19) | Scenario: none listed; global DB: none for those package names |
| Package registries | PyPI JSON (`langwatch`, `langwatch-scenario`), npm registry (`@langwatch/mcp-server`, `langwatch`) | used as independent upload-time checks | PyPI `langwatch` 1.0.0 uploaded 2026-07-24T18:45Z; npm mcp-server 2.0.0 2026-08-07T17:22Z; PyPI scenario 1.6.0 2026-10-07T12:56Z. npmjs.com web page returned HTTP 403 to `curl`; the registry API was used instead |
| Legal/entity | [terms](https://langwatch.ai/legal/terms-conditions), [about](https://langwatch.ai/about-us) | entity snapshot | See conflicts below |

## 2. Web queries actually run (2026-10-16)

| Segment / purpose | Exact query | Opened / decision |
|---|---|---|
| ownership, funding | `LangWatch 2026 funding OR raises OR acquisition` | Only Feb 2025 €1M pre-seed (pre-window). Opened [Emerce wire](https://www.emerce.nl/wire/nederlandse-startup-langwatch-gespecialiseerd-aikwaliteitscontrole-haalt-1-miljoen) (marked "Geplaatst door LangWatch", i.e. company-posted, 2025-02-25). Aggregators (tech.eu funding DB, vcbacked, premieralts, fundz, CB Insights) **not opened**; they disagree on stage label (pre-seed vs seed) per search summary only → E0, excluded |
| licence (Apr–May) | `"LangWatch" open source Apache 2.0 relicense 2026` | Confirmed via GitHub commits; opened [open-core licensing doc](https://langwatch.ai/docs/ai-governance/open-core-licensing). dev.co / enterprisedna / openalternative directory pages not opened (E0) |
| security | `"LangWatch" mcp-server vulnerability Mitiga` | No independent write-up found; generic MCP-security articles excluded |
| security | `Mitiga research MCP server session id authorization LangWatch 2026` | No Mitiga publication found. A search-summary snippet attributed an "April 28, 2026" date to the MCP-OAuth changelog entry; the raw page reads **April 6, 2026** (pre-window) → snippet treated as E0 and discarded |
| general news | `"LangWatch" news 2026 agent testing Amsterdam startup` | Only vendor pages, directories, a HumanX Amsterdam exhibitor listing (not opened) |
| Jul (Langy) | `"LangWatch" Langy AI engineer launch July 2026` | Vendor posts ledgered; aiindigo.com "review" pages not opened (promotional, E0) |
| independent comparison | `"LangWatch" Scenario agent simulation framework review OR comparison 2026 -site:langwatch.ai` | Opened [Luca Berton meetup write-up, 2026-05-07](https://lucaberton.com/blog/langwatch-scenario-ai-agent-testing-2026/) → ledgered as third-party secondary. Respan (competitor) and aicoolies pages not opened (E0) |
| community | `"LangWatch" Hacker News 2026` | No HN thread surfaced; directories only |
| Jul–Aug (gateway/coding agents) | `"LangWatch" AI gateway governance Claude Code usage tracking news` | Vendor docs and Product Hunt pages; Product Hunt not opened (no launch date shown in summary) |
| incidents (all months) | `LangWatch outage OR incident OR "data leak" OR breach 2026` | No LangWatch incident found; results concerned LangChain/LangSmith/Langdock (name collisions) → excluded |
| Sep (Instant Evals) | `"LangWatch" "Instant Evals" OR "Jev" TypeSafe judge model` | Opened [Arize, 2026-09-18](https://arize.com/blog/typesafe-jev-llm-judge/) as contrary context for Jev accuracy (competitor relay of TypeSafe's own evals). LangChain/Langfuse/futureagi Jev pages not opened |
| Oct 1–12 | `LangWatch October 2026` | No October news; directory pages only |
| Jun / Aug | `"LangWatch" June 2026 OR August 2026 announcement partnership` | No partnership found; unrelated "language" results |

## 3. Month-segment outcome

| Segment | Ledger rows | Main sources | Empty or thin areas |
|---|---:|---|---|
| Apr 12–30 | 6 | blog (Apr 14, 20, 30), releases 3.1.0 / 3.2.0, Scenario licence commit | changelog entries Apr 13 are UI polish (excluded) |
| May | 4 | third-party meetup report, licence commit, release 3.4.0, May blog | no changelog entry until May 31 |
| Jun | 4 | voice blog, changelog Jun 7 / Jun 21, release 3.5.0 | Jun 14 / Jun 28 changelogs excluded (UI, dataset storage) |
| Jul | 6 | PR Hound, Langy launch, Langy red team, 1.0 releases, 3.6.0, Claude Code tracking | Jul 3/5/8/23 posts are opinion/how-to (excluded) |
| Aug | 7 | context-cost post, MCP 2.0, LangEvals 3.0, agent-plugin 1.0, GHSA, 3.16.0, Agent Testing v2 | Aug 12 gateway comparison and Aug 14 inventory essay are marketing (excluded) |
| Sep | 3 | Go SDK 1.0, Instant Evals, 3.18.0 | no blog after Sep 22 |
| Oct 1–12 | 2 | release 3.20.0, Scenario 1.7.0 | **no blog, changelog or independent news found** |

## 4. Exclusions and deduplication

- **Pre-window baseline (not counted):** LangWatch 3.0.0 release and changelog (2026-04-08), MCP server with OAuth (2026-04-06), Scenario MIT → AGPLv3 (2026-03-06), LiteLLM-vulnerability note (2026-03-25), pricing change (2026-02-20), €1M pre-seed (2025-02-25).
- **Deduplicated:** the Instant Evals changelog (2026-09-20) and blog (2026-09-22) are **one event** in one row; the blog's different speed/cost figures are recorded as a conflict. The 3.4.0 release and the 3.4.1 governance changelog are one row. The BSL → Apache commit (05-17), release 3.4.0 (05-31) and the May blog (05-31) share duplicate group `060-licence` and are not independent confirmations. The GHSA (08-19) and the mcp-server 2.0.0 release (08-07) share group `060-mcp-ghsa`.
- **Excluded as marketing/opinion with no dated product change:** competitor "alternatives"/"top N tools" posts; EU AI Act guide (07-05); cost-per-successful-task essay (07-03, cited as context only); Codex vs Claude Code (07-08, cited as context for CI2026-060-015); Background agents (07-05); Things you can ask Langy (07-23); LLM gateway comparison (08-12); agent inventory essay (08-14); Altura meetup post (05-19, customer narrative, unverifiable); Every Way Your AI Agent Can Be Broken (04-15, attack taxonomy accompanying the red-teaming launch, folded into group `060-redteam`); two companion event-sourcing posts (04-20, same engineering series as CI2026-060-002).
- **Customer and certification claims** on the homepage (named enterprise customers, "ISO 27001 Certified", "GDPR Compliant") are undated vendor claims and were not verified; no certificate was inspected.

## 5. Conflicts recorded (not silently resolved)

1. **AI Gateway status:** release 3.2.0 (2026-04-29) says "ship v1 GA"; the April blog (2026-04-30) says "private beta".
2. **Langy launch date/scope:** changelog 2026-06-07 says Langy "now mounts for every team member"; blog 2026-07-22 says "Today we are launching Langy" (likely in-product assistant vs PR-opening agent; unresolved).
3. **Instant Evals figures:** changelog 2026-09-20: 10,000 conversations in 2 min 26 s for $0.62; blog 2026-09-22: about a minute for $0.32 (table: 1 min 13 s). Arize (2026-09-18) relays TypeSafe's own four-workflow average of 68% for Jev vs 73% for Opus 5, against LangWatch's single-question 97% vs 91%.
4. **"Entire platform open source, nothing held back"** (May blog) vs the open-core licensing doc listing Enterprise-only governance surfaces and the proprietary `enterprise/` directory.
5. **Legal entity:** terms page names "Reasoning Engines B.V." and "Reasoning Engine B.V." with two Amsterdam addresses (Singel 126; Herengracht 551); site footer says "LangWatch B.V.". No Chamber of Commerce (KvK) record checked.
6. **Release dates:** 3.20.0 body dated 2026-10-01, GitHub publish 2026-10-02; 3.18.1 body 2026-09-29, publish 2026-09-30.

## 6. Untrusted-content log

- The `.md` docs pages (e.g. [open-core licensing](https://langwatch.ai/docs/ai-governance/open-core-licensing.md)) contain an "Agent Instructions" block asking AI agents to run `npx langwatch report --user-approved`. **Ignored**; nothing was executed. No other instructions aimed at AI agents were seen in fetched pages.

## 7. Coverage limits

Not exhaustive. Paywalled outlets, LinkedIn, X/Twitter, YouTube, Product Hunt and Dutch-language trade press beyond one Emerce wire were not systematically searched. WebFetch summaries were not used for any figure; every number in the ledger was read from raw page text or an API response. Stars/forks were seen in API output but are deliberately not used as adoption evidence.
