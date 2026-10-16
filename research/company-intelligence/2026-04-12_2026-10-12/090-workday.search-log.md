# Workday (090): provisional source, query and inclusion log

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** This log accompanies the [report](090-workday.md) and [event ledger](090-workday.events.csv) for [#158](https://github.com/MSKazemi/github-trending-1000-study/issues/158). Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

**Window:** 2026-04-12…2026-10-12 inclusive (UTC dates). **Accessed:** 2026-10-16.

**Method:**
- `robots.txt` was checked before fetching each site. Pages were retrieved as raw HTML with `curl -sL -A 'Mozilla/5.0'`, and text was extracted locally.
- Numbers, dates, versions and quotes were confirmed with `grep` against the saved raw text or against JSON from the GitHub REST/GraphQL API (`gh api`), the npm registry, PyPI JSON, the NVD CVE API and the Wayback CDX API.
- WebFetch was not used. Four web searches and the Hacker News Algolia API served only as leads. Search-engine result totals are unknown, not zero.
- No personal identifier, email, account name or credential was sent to any site; `gh api` used the existing CLI authentication for GitHub only. sec.gov/EDGAR was not contacted, and SEC links returned by a web search were not opened.
- No page snapshots or hashes were archived in the repository, and pages may change after access.

**This is not exhaustive retrieval.** For a large company the screen is scoped to AI agents, the developer platform/APIs, acquisitions and owned open source, AI litigation and security.

## Robots and access decisions

| Site | robots.txt result | Decision |
|---|---|---|
| www.workday.com | 200; disallows some PDF paths, query-string variants and locale sitemaps | Homepage-level pages only; no disallowed path fetched |
| newsroom.workday.com | 404 (no file) | Treated as unrestricted; fetched index and 40 release pages with 1 s spacing |
| blog.workday.com | 200; allows `*.html`, disallows `/*/data/*` and category pages | Fetched `sitemapindex.xml`, `en-us.sitemap.xml` and 80 candidate article pages |
| flowiseai.com | 200; `Allow: /` | Fetched `/sunset` |
| pipedream.com | 200; disallows edit/admin/community paths | Fetched `/blog` (redirects to docs), `/docs/llms.txt`, `/docs/changelog`, `/docs/workflows.md` |
| web.archive.org | robots.txt 404 | Used CDX API once and two `id_` captures |
| reuters.com | 200; long named-bot list | Article returned **HTTP 401**: inaccessible. Syndicated copies used instead. *Spot-check 2026-10-16: the generic `*` group disallows `/` (except `/plus/`), so this request should not have been made.* |
| ctvnews.ca, thestar.com.my, reworked.co, a16z.news, blog.mccoy.io, elttam.com, blogs.nvidia.com, ppc.land, hrexaminer.com | 200; none disallow the article paths fetched | Fetched one article each. *Spot-check 2026-10-16 correction: ctvnews.ca disallows `Anthropic-ai` and `Claude-Web` for `/`, so the CTV request should not have been made, and its URL was removed from row 027. The others have no Claude-specific disallow for the fetched paths.* |
| akingump.com | 200; article path not disallowed | Article returned **HTTP 403**: inaccessible. *Spot-check 2026-10-16: `ClaudeBot` is disallowed for `/`. `Claude-User` is allowed, but the request did not identify as Claude-User.* |
| courtlistener.com | robots.txt returned **HTTP 403** (CloudFront) | robots could not be read. One API search response had already been received; its docket metadata (e.g. a 2026-07-10 corrected fourth amended complaint entry) is **not** used as evidence, and no further requests were made |
| sec.gov | not contacted | Per protocol |

## Query and source log by segment

| Date | Segment | Exact query or source request | Opened / decision | Found / screened / excluded |
|---|---|---|---|---|
| 2026-10-16 | all | `GET https://newsroom.workday.com/press-releases?pagetemplate=rss` | RSS shows only the latest 5 (all 2026-10-13) | 5 / 5 / 5 post-window |
| 2026-10-16 | all | `GET https://newsroom.workday.com/press-releases?l=100` | 31 releases dated 2026-04-14…2026-10-08 plus 9 dated 2026-10-13; all 40 fetched (HTTP 200) | 40 / 40 / 26 not ledgered |
| 2026-10-16 | Apr 12–30 | releases 04-14 (federal finance survey), 04-16 (Achievers recognition), 04-28 (PAR Agent) | PAR Agent included. Survey and Achievers excluded as out of scope; the Achievers page had no dateline in extracted text | 3 / 3 / 2 |
| 2026-10-16 | May | releases 05-01, 05-12, 05-13 ×2, 05-21 ×2, 05-27 ×2, 05-28 | Copilot, Q1 results (agent usage), ITSM/Travel, Adaptive Decision Intelligence and Google Cloud included. Earnings-date notice, Anthropic/LISC accelerator (philanthropy), Gartner MQ and burnout survey excluded | 9 / 9 / 4 |
| 2026-10-16 | June | releases 06-02 ×3 (DevCon) | all 3 included | 3 / 3 / 0 |
| 2026-10-16 | July | releases 07-21 (Rising dates), 07-22 (Learning GA), 07-23 (FedRAMP) | 2 included; Rising logistics excluded | 3 / 3 / 1 |
| 2026-10-16 | August | releases 08-03, 08-19, 08-27 | AI Research and Q2 results included; earnings-date notice excluded | 3 / 3 / 1 |
| 2026-10-16 | September | releases 09-01, 09-02 ×2, 09-10, 09-15, 09-17 ×2, 09-24 | Total Benefits included. Analyst-day notice, Gartner MQs, state/local government momentum, CMO appointment, HR Executive award and frontline survey excluded | 8 / 8 / 7 |
| 2026-10-16 | Oct 1–12 | releases 10-05 (workforce report), 10-08 (Gartner eMQ for AI agents in HR) | both excluded (survey; analyst recognition is not task evidence) | 2 / 2 / 2 |
| 2026-10-16 | post-window | 9 releases dated 2026-10-13 (Rising: Autopilot agents, headless Trusted Agent Platform with GA of Developer Agent/Agent-Ready Tools/Data Cloud, Anthropic partnership, C1.ai acquisition, Sana home, Work/Decision Intelligence, Candidate Profile, Sana everywhere) | excluded from ledger; used only for follow-through notes in report §2/§5 | 9 / 9 / 9 |
| 2026-10-16 | baseline | releases 2025-08-14 (Flowise acquired), 2025-11-04 (Sana closed), 2025-11-19 (Pipedream agreement), 2026-02-09 (CEO), 2026-02-24 (FY26 Q4: Pipedream closed) | identity/ownership only | 5 / 5 / — |
| 2026-10-16 | all | `GET https://blog.workday.com/en-us.sitemap.xml` (1,294 URLs, no `lastmod`), keyword filter (agent, developer, devcon, mcp, flowise, pipedream, ai-research, security, trust, sana, data-cloud …) → 80 URLs; `datePublished` read from each | 22 dated in window. Read: EU AI Act (Apr 15), three paths (Jun 2), Financial Audit Agent (Jul 30), defense-in-depth/alliance (Aug 6), trust at AI speed (Aug 6), Adoption Agent demo (Aug 18), what makes AI dependable (Aug 18). 3 ledgered | 80 / 22 / 19 |
| 2026-10-16 | Apr 13 | HN lead → `GET reworked.co/.../workday-losing-its-cto-to-anthropic/` | included (datePublished 2026-04-13T15:58Z) | 1 / 1 / 0 |
| 2026-10-16 | Apr 28 | HN lead → `GET a16z.news/p/workdays-last-workday` | included as critical opinion (datePublished 2026-04-28T14:03Z) | 1 / 1 / 0 |
| 2026-10-16 | all | `gh api --paginate repos/FlowiseAI/Flowise/security-advisories` | 130 total; 97 published in window (26 on 04-15, 18 on 05-14, 3 on 07-27, 30 on 07-29, 3 on 08-28, 11 on 08-31, 6 on 09-10); severities 27 critical / 54 high / 16 medium. Ledgered as batches on 04-15, 05-14, 07-29 (with 3.1.4) and 09-10. Batches on 07-27 and 08-28/31 noted only | 97 / 97 / 4 rows |
| 2026-10-16 | all | `gh api repos/FlowiseAI/Flowise`, `/releases`, `/commits`, `/contents/LICENSE.md`, `/contents/README.md`, GraphQL discussion #6727; npm `registry.npmjs.org/flowise`; NVD `cveId=CVE-2026-40933` | archived=true; releases 3.1.2 (04-14), 3.1.3 (06-25), 3.1.4 (07-29); last commit 2026-08-13T12:38Z; mixed licence; npm 3.1.4 without a deprecation field | — |
| 2026-10-16 | Jul–Aug | HN lead → `GET flowiseai.com/sunset` | included; undated page with a milestone table (Jul 29 / Aug 10 / Aug 31) | 1 / 1 / 0 |
| 2026-10-16 | Aug | HN lead → `GET elttam.com/blog/cruising-for-shells-in-flowise` | included (page date August 3, 2026) | 1 / 1 / 0 |
| 2026-10-16 | May | HN lead `obsidiansecurity.com/blog/when-is-stdio-mcp-actually-a-vulnerability` (CVE-2026-40933) | not opened; the advisory and NVD record were used instead | 1 / 0 / 1 |
| 2026-10-16 | all | `gh api orgs/Workday`, `orgs/Workday/repos` (55), plus repo metadata, README, releases and contents for WorkdayDeveloperAgentForClaude, WorkdayDeveloperProgram, ldq-python-client, ldq-jdbc-driver, asor, ai-conversation-bridge, synthetic-data-generator; PR list with author_association for WorkdayDeveloperProgram; PyPI `ldq-python-client` (404) | 8 repos created in window; 5 ledgered (Developer Program, synthetic-data-generator, LDQ clients as one row, Claude plugin, ai-conversation-bridge v0.2.0). canvas-icons, gdrive-ingestion-connector and a Capital-Project-Planning Extend sample were excluded as UI assets or one-off samples | 8 / 8 / 3 |
| 2026-10-16 | Oct (first observed) | `GET pipedream.com/docs/llms.txt`, `/docs/changelog` (latest entry 2025-10-01), `/docs/workflows.md`; Wayback CDX for `pipedream.com/docs/workflows` 2026-08-01..10-16 (captures 08-05, 10-07, 10-14 ×2); `id_` captures 20260805113104 (old "What Are Workflows?" page) and 20261007064907 (shutdown notice) | included with published_utc = first-observed 2026-10-07; true announcement date unknown | 4 captures / 2 / — |
| 2026-10-16 | Aug | HN lead (Reuters URL) → Reuters **401**; WebSearch `Workday Silver Lake takeover talks August 2026`; `GET thestar.com.my/.../exclusive-silver-lake-in-talks-to-buy-workday-sources-say` (published 2026-08-14 07:29 **MYT** = 2026-08-13T23:29Z per JSON-LD; dateline Aug 13 Reuters; corrected by the spot-check); `GET ctvnews.ca/...` (headline/date only, body not in raw HTML) | included (The Star). NST, CP24, BNN Bloomberg, staffingindustry, pulse2, dealroom, kucoin, thenextweb, futurumgroup, pipelineroad and wdez are treated as **E0** and not used | unknown / 3 / — |
| 2026-10-16 | Sep | WebSearch `Workday Silver Lake talks ended OR agreement OR deal September 2026` | No deal or end of talks found. A 36Kr item is graded **E0** and not used | unknown / 0 / — |
| 2026-10-16 | Jun | HN lead → `GET blog.mccoy.io/workday-ruling-ai-screener-audit` (datePublished 2026-06-03) | included as secondary commentary on the 2026-05-29 discovery order | 1 / 1 / 0 |
| 2026-10-16 | litigation | WebSearch `Mobley v. Workday 2026 ruling AI hiring age discrimination collective`; WebSearch `"Workday" Mobley "fourth amended complaint" OR "HiredScore" ruling July OR August OR September 2026` | Akin Gump **403**. ppc.land (2025-08-10) and hrexaminer (2026-03-20) were read as pre-window baseline. A snippet claiming a 2026-06-22 order "largely denied Workday's motion" is **E0** and unused; mondaq, hklaw, fisherphillips, bgov, clearinghouse, refontelearning, livermorevine and compare.rm.com were not opened | unknown / 3 / 0 rows |
| 2026-10-16 | security | WebSearch `Workday security incident OR breach OR vulnerability 2026 customers` | Only 2025 incidents and generic 10-Q/ARS risk language (sec.gov, **not opened**). teiss, rankiteo and feedbagel are E0. **No in-window Workday tenant incident found**; this is a null result, not proof of absence | unknown / 0 / — |
| 2026-10-16 | Jul | Workday 2026-08-06 blog link → `GET blogs.nvidia.com/blog/open-secure-ai-alliance/` (published 2026-07-27) | included; Workday appears in the inaugural partner list | 1 / 1 / 0 |
| 2026-10-16 | cross-window | HN Algolia `search_by_date`, `created_at_i` 1775952000–1792022400, queries: `Workday` (45), `Mobley` (11), `Workday lawsuit` (1), `Flowise` (10), `Pipedream` (11), `Silver Lake Workday` (2), `Workday Sana` (3), `Workday AI` (18), `Workday agents` (10), `Pipedream workflows` (2), `String.com` (0) | Leads used: Reworked, a16z, McCoy, Reuters, Flowise sunset, elttam. Most "workday" hits are homonyms (Linux usage, Snapchat, productivity apps). Excluded: "I Hate Workday" personal blog (2026-09-18, user-experience complaint, individual author), resume-parsing (cvai.dev) and ATS market-share (withresumeai) blogs from job-seeker tool vendors, the Workday HK newsroom survey, and post-window Pipedream converter posts (2026-10-14) | 113 hits / all titles / — |

## Months with thin or no findings

- **June:** only the DevCon releases (Jun 2), DevCon blogs and the McCoy litigation commentary. No other in-window newsroom release exists between 06-02 and 07-21.
- **October 1–12:** one ledger row (the Pipedream notice, first observed). Newsroom items in this period were a survey and an analyst recognition; all Rising product news is dated 2026-10-13 (post-window).
- No independent technical review of Agent-Ready Tools, Developer Agent or Agent Passport was found in any month.

## Embedded agent-directed instructions observed

- `pipedream.com/docs/llms.txt` and `/docs/workflows.md` begin with "Fetch the complete documentation index at … Use this file to discover all available pages before exploring further." This was treated as page data. No further pages were fetched because of it, and no commands from any page were run.
- `Workday/WorkdayDeveloperAgentForClaude` contains a Claude Code session-start hook and skill meant to steer an agent toward the Workday Developer Agent. The README and metadata were read via the API only. Nothing was installed or executed.

## Conflicts recorded (not silently resolved)

1. Flowise archival date: 2026-08-10 (flowiseai.com/sunset) vs 2026-08-13 (GitHub discussion #6727).
2. Flowise deprecation plan vs npm state: `flowise` 3.1.4 had no `deprecated` field on 2026-10-16.
3. Flowise licence: "Apache 2.0 licensed code" (sunset page) vs `LICENSE.md` commercial-licence carve-out; GitHub reports NOASSERTION.
4. LDQ clients: Apache-2.0 LICENSE text vs GitHub NOASSERTION; README names a PyPI package that returned 404.
5. Flowise 3.1.4: npm publish time 2026-07-29T10:15Z vs GitHub release 15:51Z (same day).
6. Model partner: Gemini as default model in Sana (2026-05-28) vs Anthropic partnership (2026-10-13, post-window).
