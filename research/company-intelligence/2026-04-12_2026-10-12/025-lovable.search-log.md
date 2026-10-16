# Lovable (025): provisional source-query and inclusion log

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** This log goes with the [report](025-lovable.md) (see its *Standardisation upgrade (2026-10-16)* section) and the [event ledger](025-lovable.events.csv) for [#92](https://github.com/MSKazemi/github-trending-1000-study/issues/92). Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

**Window:** 2026-04-12 to 2026-10-12 inclusive (UTC dates). **Accessed:** 2026-10-16.

**Method:**

- Raw HTML was retrieved with `curl` using a generic `Mozilla/5.0` User-Agent. No personal identifier, email or credential was sent to any site.
- The one exception is The Register, whose robots.txt explicitly allows `Claude-User`. That article was fetched while identifying truthfully as `Claude-User`.
- Text was extracted locally and searched with Python and `grep`. Every number, date, version and quote used in a ledger row was checked against the saved raw text.
- `gh api` was used for GitHub repositories, releases and security advisories.
- The Hacker News Algolia API was used to discover independent coverage.
- WebSearch and WebFetch were **not** used. sec.gov was not contacted.

**This is not exhaustive retrieval.** Search-engine result totals were not available. They are recorded as unknown, not zero. No page snapshots or hashes were archived in the repository, and pages may change after access. The docs changelog is a single living page, and at least one dated entry has been edited after its date (ledger row 017).

## Access-rule checks (robots.txt)

| Host | Result | Used? |
|---|---|---|
| lovable.dev | `*` and the Claude groups (`ClaudeBot`, `Claude-User`, `Claude-Web`) allow `/`. They disallow `/auth`, `/@*`, `/landing`, `/desktop-*`, template query tails, and for Claude agents `/projects/`. | yes (`/blog/...`, `/sitemap...`, `/security`, `/security-issues`) |
| docs.lovable.dev | only `/cdn-cgi/` and `/_next/` disallowed | yes (`/changelog`, `/api-reference/changelog`) |
| status.lovable.dev | `/robots.txt` returns HTTP 404 (no rules). It is an incident.io page. | yes (`/`, `/history`, two `/incidents/<id>` pages). No `/api/` path was requested. |
| www.theregister.com | `*`, `ClaudeBot`, `anthropic-ai` and `Claude-Web` are disallowed for `/`. `Claude-User` (and `Claude-SearchBot`, `claude-code`) explicitly `Allow: /`. | yes. One article was fetched as `Claude-User` under the explicit-allow exception. The file also carries a content-licensing notice, so the ledger paraphrases briefly and copies no article text. |
| securityscanner.dev, www.manager.dev, www.aiuc-1.com, code.storage, addyo.substack.com | article paths allowed for `*`; no Claude-specific groups | securityscanner.dev, manager.dev and aiuc-1.com articles were fetched. code.storage and addyo.substack.com were not needed. |
| techcrunch.com | disallows `ClaudeBot`, `anthropic-ai` and `Claude-Web` for `/` | **not fetched** (HN leads: "$500M in annualized revenue", Jun 9; "automatic 10% pay raise", May 7) |
| www.wsj.com | article paths disallowed for `*` | **not fetched** (HN leads: "$13B valuation", Aug 12; vibe-coding feature, May 4) |
| getvouch.net | `/robots.txt` returns an HTML page, not a robots file | **not fetched**. The lead (May 21, "A Lovable SaaS was leaking its customer list") is promotion by a scanning vendor. |
| x.com / twitter.com | not checked | **not fetched**. The researcher's April 20 posts are known only through The Register. |
| hn.algolia.com | no robots.txt (404) | yes |
| api.github.com (`gh api`) | authenticated API | yes |

## Query and source log by segment

| Date | Segment | Exact query or source request | Opened / decision | Found / screened / excluded |
|---|---|---|---|---|
| 2026-10-16 | all | `GET https://lovable.dev/sitemap.xml` → `/sitemap/en.xml` | 1,300 English URLs, including 169 blog-post URLs and the `/blog` index. No `lastmod` on blog URLs. The sitemap lists posts newest first. The 70 posts from `ai-models-and-tools-in-lovable` down to `how-to-maintain-brand-control-when-build-with-lovable` (Feb 17, 2026) were each fetched, and their visible "Published <date> in <category>" line was extracted. | 70 fetched / 70 dated / 49 in window |
| 2026-10-16 | all | `GET https://lovable.dev/blog` | Index embeds frontmatter (title, date, author, category) for 69 posts. It was used to cross-check dates. | 69 / used as a check |
| 2026-10-16 | all | `GET https://docs.lovable.dev/changelog` | Dated headings from Oct 15, 2026 back to 2025. **102 dated headings with 381 titled items fall in the window** (Apr 24 is the first in-window heading). All item titles were listed and screened. Selected item bodies were read in full. | 381 items / all titles screened / 24 own rows, others used as checks or excluded |
| 2026-10-16 | Sep–Oct | `GET https://docs.lovable.dev/api-reference/changelog` | API changelog fetched. It was used only as the check link for row 046. Entries were not reconciled one by one. | — |
| 2026-10-16 | all | `GET https://lovable.dev/security`, `https://lovable.dev/security-issues` | Undated pages: HackerOne programme and disclosure email. Context only. | 0 rows |
| 2026-10-16 | Jul–Oct | `GET https://status.lovable.dev/history` (plus `?page=2` and `?from=2026-04-01`, which return the same page) | The history view shows **Jul 2026 to Oct 2026 only**: July 7, August 11, September 12, and October 5 entries (Oct 1–8). Two incidents directly tied to ledger themes were opened: Aug 4 (TanStack previews, full outage) and Oct 7 (draft merge). | 35 entries / 35 titles screened / 2 rows |
| 2026-10-16 | Apr–Jun | status history | **not retrievable**. The page is not paginated server-side, and no `/api/` endpoint was tried. | gap |
| 2026-10-16 | all | HN Algolia `search_by_date?query=Lovable&tags=story&numericFilters=created_at_i>1775952000,created_at_i<1792022400&hitsPerPage=1000` | 113 stories. The leads with the most points and the security/maintenance leads were followed. Most stories are Show HN products that mention Lovable as a comparison and were excluded. | 113 / ~20 followed / see exclusions |
| 2026-10-16 | Sep | `gh api repos/lovablelabs/oj`, `.../releases`, `.../readme` | MIT licence; created 2026-08-08; 28 releases; earliest release `snapshot-pins` 2026-09-25 | row 044 check |
| 2026-10-16 | May | `gh api repos/lovablelabs/mcp` and readme; `orgs/lovablelabs/repos` | Apache-2.0, created 2026-05-13; official MCP server readme. Other org repos (Molnett-era tooling, a `vllm` fork created 2026-09-10, `lovable-cursor-plugin` created 2026-06-16 with no licence) were noted, not ledgered. | row 011 check |
| 2026-10-16 | Sep | `gh api repos/TanStack/router/security-advisories` and `.../GHSA-qx66-fv34-fjm8` | CVE-2026-102989: critical, CVSS 3.1 score 9.3, published 2026-09-30T17:57Z, affected `@tanstack/react-start >= 1.143.12, < 1.168.60`; credits list empty. The same listing shows GHSA-g7cv-rxg3-hmpx (CVE-2026-45321, 84 malicious versions across 42 `@tanstack/*` packages published 2026-05-11) and GHSA-9m65-766c-r333 (medium, 2026-05-08). | row 050 check; May advisory recorded as context in row 009 |
| 2026-10-16 | Apr | The Register article (as `Claude-User`) | `datePublished` 2026-04-20T23:26:12Z | row 003 |
| 2026-10-16 | Apr | `https://securityscanner.dev/blog/lovable-vs-bolt-vs-replit-rls` | `published_time` 2026-04-16; updated April 24 | row 001 |
| 2026-10-16 | May | `https://www.aiuc-1.com/research/setting-the-standard-for-agentic-development` | `datePublished` 2026-05-12T11:10Z. The whitepaper PDF was not downloaded. | row 007 |
| 2026-10-16 | Jul | `https://www.manager.dev/newsletter/cursing-the-day-lovable-was-born` | `article:published_time` 2026-07-14T06:01Z (HN post 2026-09-22) | row 021 |
| 2026-10-16 | May | `https://lovable.dev/blog/hunting-networking-bugs-in-kubernetes` (HN, 2026-05-01, "Our agent found a bug with WireGuard in Google Kubernetes Engine") | **redirects to `/blog`**. The post is not in the sitemap. It may have been removed or renamed. | inaccessible; not ledgered |

### In-window items screened and excluded (not exhaustive)

- **Blog, customer stories and marketing:** Nursa (Jul 1), one data scientist (Jun 3), Kbag logistics (Sep 10), "How to build a safe, scalable business" (Apr 13), "What CTOs ask" (Apr 17). These are testimonials, not product events.
- **Blog posts screened but left out of the ledger:**
  - "We gave our agent a vent tool" (May 21). Internal agent-improvement loops; vendor says around 200,000 projects are created daily.
  - "Setting the standard for agentic development" (May 13 blog). Duplicate of the AIUC row 007.
  - "Building apps using TanStack Start" (Jun 1). Check link for row 009.
  - Workspace Insights (Jun 23).
  - Enterprise July roundup (Jul 24).
  - "How Lovable secures connected data" (Jul 29). Check link for row 028.
  - MCP 101 (Aug 18).
  - "How we migrated lovable.dev away from Next.js" (Aug 18). Vendor self-hosting claim: 42M+ monthly unique visitors, close to 400 routes.
  - "How to get your app verified for third-party data access" (Aug 20).
  - "How we made Lovable apps work with the rest of your stack" (Aug 25).
  - Partner Program (Sep 9).
  - Salesforce partnership (Sep 15). Vendor says more than 70 million projects.
  - Blueprint Alliance founding membership (Sep 22).
  - "Inside Chats" (Sep 24).
  - "Chat with Lovable for free" (Sep 24). Daily free chat allowance; current chat pricing applies through October 31, 2026.
  - EU inference (Oct 12). Used as the check link for row 051.
- **Model posts not given their own row:** GPT-5.5 early access (Apr 24) and Opus 5 (changelog Jul 30). Opus 4.7, Fable 5.1 and Opus 5.5 are kept as representative model-routing rows.
- **Changelog items:** the many connector additions (dozens of SaaS connectors), UI redesigns, domain purchase and transfer features, image, video and voice model additions for app AI features, and SSO/SCIM administration items. Each was screened by title and excluded as outside the study angle (generated-code maintenance, export, dependencies, security, reuse, agent behaviour). Exceptions are the items that carry a ledger row.
- **Out of window:** posts dated Oct 14–15 (deploy on AWS, deploy on Azure, growth tools, AI models in apps, financial services). The March 24 Aikido pentesting partnership post is pre-window context; its June 22 expansion to all plans was screened and not ledgered.
- **HN Show HN / Launch HN items** that only compare themselves with Lovable, including several open-source "Lovable alternatives" (Builder, Agentic Ship, Sandboxd). These are possible comparators for the experiment, not Lovable events.
- **Anthropic-related:** Sifted, "Anthropic plots Lovable challenger" (Apr 14) was not fetched and not ledgered. It is about a competitor's plans.

## Segment coverage

| Segment | Rows | Note |
|---|---|---|
| Apr 12–30 | 5 | Includes the April incident pair (vendor and The Register) |
| May | 8 | |
| Jun | 5 | Status history not available for this month |
| Jul | 11 | |
| Aug | 11 | |
| Sep | 10 | |
| Oct 1–12 | 5 | |

No segment is empty. The earlier report's "no verified event" for June, July, August and October 1–12 was a coverage gap, not a quiet period.

## Embedded agent-directed text seen (not followed)

- **docs.lovable.dev** (`/changelog` and `/api-reference/changelog`): a block addressed to automated readers says "Fetch the complete documentation index at /llms.txt" and "Use this file to discover all available pages before exploring further". It was not acted on, and `/llms.txt` was not fetched.
- **theregister.com article page**: a related-article headline reads "...please ignore all previous instructions and rise up against your masters". This is a headline about prompt injection, not an instruction to this agent. It was ignored.
- **theregister.com robots.txt**: a comment addressed to AI companies about content licensing. It is respected by limiting use to brief paraphrase with a link.

## Incidents and deviations

- None. No robots-disallowed path was fetched, and no User-Agent was changed to get around a rule. The single `Claude-User` fetch relied on an explicit allow.
