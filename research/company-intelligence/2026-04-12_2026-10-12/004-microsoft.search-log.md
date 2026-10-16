# Microsoft (004) — provisional source-query and inclusion log (standardisation upgrade)

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** Companion to the [report](004-microsoft.md) and [event ledger](004-microsoft.events.csv) for [#70](https://github.com/MSKazemi/github-trending-1000-study/issues/70). Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

**Window:** 2026-04-12…2026-10-12 inclusive (UTC dates). **Accessed:** 2026-10-16. **Scope:** Microsoft AI developer tooling only — VS Code and Copilot-in-VS Code, Microsoft Agent Framework / Semantic Kernel / AutoGen, Microsoft Foundry developer surfaces, Microsoft-published MCP servers, and MSRC advisories for these products. GitHub-specific products (GitHub Copilot app/CLI/cloud agent, github.blog items) are left to watchlist 033 / #100. Microsoft 365 Copilot, Windows, Surface, Edge Copilot and corporate finance stories are out of scope.

**Method:** robots.txt checked for every host before fetching; raw HTML/XML/JSON retrieved with `curl` using a generic `Mozilla/5.0` User-Agent (no email, name, handle or credential sent to any site); crawl delays honoured (10 s for devblogs/news; 15 s between MSRC documents); text extraction plus `grep` confirmation of every number, version, date and quote used in a ledger row, except the three rows marked WebFetch-only. GitHub data via authenticated `gh api` (no identifier sent to any third-party site). No Azure command was run and no Azure resource was created; nothing was installed or executed. SEC/EDGAR was not contacted. **This is not exhaustive retrieval;** search-engine result totals were not available (WebSearch was not used because the session budget was nearly exhausted) and are recorded as unknown, not zero. No page snapshots/hashes are archived in the repository.

## Query and source log by segment

| Date | Segment | Exact request | Opened / decision | Found / used |
|---|---|---|---|---|
| 2026-10-16 | all | robots.txt for news.microsoft.com, blogs.microsoft.com, code.visualstudio.com, devblogs.microsoft.com, msrc.microsoft.com, azure.microsoft.com, learn.microsoft.com, techcommunity.microsoft.com, www.microsoft.com, blogs.windows.com, commandline.microsoft.com, microsoft.ai, services.nvd.nist.gov, api.msrc.microsoft.com, hn.algolia.com, blog.ammaraskar.com, www.theregister.com, thenewstack.io, www.bleepingcomputer.com | all permissive for the paths used except: thenewstack.io disallows `anthropic-ai`, `ClaudeBot`, `Claude-Web` (not fetched); theregister.com disallows `*` but explicitly allows `Claude-User` (one article fetched identifying truthfully as `Claude-User`); bleepingcomputer.com robots behind a Cloudflare challenge (not fetched) | — |
| 2026-10-16 | all | `GET https://blogs.microsoft.com/...` (the three posts cited by the earlier report), `/feed/`, `/wp-json/wp/v2/posts` | **HTTP 403 Cloudflare block** to curl; the three earlier-cited posts were then read with WebFetch (model summary) — quotes not raw-confirmed | 3 WebFetch summaries |
| 2026-10-16 | all | `GET https://news.microsoft.com/sitemap_index.xml`, `post-sitemap38/39.xml`, homepage | sitemaps readable but post sitemaps last modified 2022/2025 (no 2026 posts); homepage then returned **HTTP 403** | 0 |
| 2026-10-16 | all | `GET https://blogs.windows.com/windowsdeveloper/feed/` (pages 1–2) | **HTTP 403** | 0 |
| 2026-10-16 | all | `gh api repos/microsoft/vscode/releases` (paginated) | 26 stable minor releases 1.116.0 (2026-04-15) … 1.141.0 (2026-10-07) plus patch releases and `copilot/0.44.x–0.45.x` extension releases | used for dates |
| 2026-10-16 | all | `GET https://code.visualstudio.com/updates/v1_116` … `v1_141` (26 pages) | all 200; page release dates match GitHub release dates except 1.123 (page June 3 vs GitHub 2026-06-05) | 12 rows |
| 2026-10-16 | all | `GET https://code.visualstudio.com/blogs/...` (sidebar list) | in-window posts: 05/15 harness, 06/17 token efficiency, 06/18 BYOK, 06/19 50,000 runs, 06/26 TypeScript 7, 07/06 harness model providers, 07/29 MAI-Code-1-Flash, 08/26 agent host, 09/16 & 09/23 inline suggestions model | 3 rows (50k runs, MAI-Code-1-Flash, Agent Host); harness, token-efficiency, BYOK read and used as context; TS7 and inline-suggestion posts not opened |
| 2026-10-16 | all | `GET https://api.msrc.microsoft.com/cvrf/v3.0/updates`; `cvrf/2026-Apr` … `2026-Sep` (JSON) | product-name matching script for VS Code / Copilot / Foundry / MCP / Agent Framework; October document released 2026-10-13 (out of window) | 6 rows |
| 2026-10-16 | all | NVD API 2.0 `keywordSearch` = "Visual Studio Code", "Copilot", "Semantic Kernel", "Microsoft Foundry", "Agent Framework", "Playwright MCP", "Azure MCP" over two pubDate ranges | 220 raw hits (57 after description filter); keyword search matches words separately; used only to cross-check CVRF (one date conflict, CVE-2026-41109). No Semantic Kernel / Agent Framework CVE in the window | cross-check only |
| 2026-10-16 | all | `gh api repos/microsoft/{agent-framework,semantic-kernel,autogen,vscode-copilot-chat,playwright-mcp,markitdown,mcp,TypeScript}/releases`; repo metadata; README via API; `commits?path=README.md` | AF 54 in-window releases; SK 16; AutoGen 0 (maintenance-mode banner updated 2026-04-06); vscode-copilot-chat archived 2026-05-20; playwright-mcp 13 (v0.0.71–v0.0.83; context only, not ledgered); markitdown 5 (context only); microsoft/mcp 87 incl. Azure.Mcp.Server-3.0.0; TypeScript 7.0.2 (2026-08-20; not AI tooling, excluded) | 5 rows |
| 2026-10-16 | all | `gh api repos/microsoft/{semantic-kernel,agent-framework,playwright-mcp,markitdown}/security-advisories` | SK advisories dated Feb 2026 (pre-window); AF three advisories 2026-10-07; none for playwright-mcp/markitdown | 1 row |
| 2026-10-16 | Apr 12–30 | devblogs RSS `agent-framework/feed/?paged=1..4`, `foundry/feed/?paged=1..5` | 30 AF and 38 Foundry in-window items listed; opened: AF CodeAct, A2A v1; Foundry hosted agents, Toolboxes | 3 rows (Toolboxes folded into hosted-agents row; June roundup published 2026-07-07 counted in July) |
| 2026-10-16 | Apr 12–30 | `gh api repos/microsoft/vscode/pulls/310226`; issue search `"co author" is:pr` | PR merged 2026-04-16; PR #312821 open; PR #339437 open (2026-10-03) | used in CI2026-004-008 |
| 2026-10-16 | May | AF FIDES; Foundry Local 1.1; vscode-copilot-chat archive commit (SK README commit of 2026-04-30 counted in April) | all included | 3 rows (+2 VS Code, +1 MSRC) |
| 2026-10-16 | May | HN Algolia `query=VS Code` (story, in-window) | top items: VS Code co-author trailer (2026-05-02, 1513 pts, item 47989883 fetched via `/api/v1/items/`); BleepingComputer "GitHub confirms breach of 3,800 repos via malicious VSCode extension" (2026-05-20) — **not fetched** (Cloudflare challenge) and GitHub-side incident, left to 033 | 1 independent check |
| 2026-10-16 | June | Foundry Build posts (`agent-service-build2026`, `build-2026-open-trust-stack-ai-agents`); AF Build round-up; `whats-new-in-microsoft-foundry-june-2026` | included | 4 rows |
| 2026-10-16 | June | blog.ammaraskar.com `github-token-stealing` (found via HN, 2026-06-02, 660 pts) | read raw; included as independent security research | 1 row |
| 2026-10-16 | June | `microsoft.ai/news/introducingmai-code-1-flash/` (found via HN, 540 pts) | **HTTP 403**; not read; VS Code blog used instead | — |
| 2026-10-16 | June | Microsoft Learn search "Microsoft Execution Containers MXC preview agent sandbox Windows" | no MXC page returned (only Windows Sandbox / AppContainer docs) — MXC remains WebFetch-only | 0 |
| 2026-10-16 | July | AF orchestrations 1.0, Harness release; devblogs Go `microsoft-agent-framework-for-go-public-preview` | included | 3 rows |
| 2026-10-16 | July | HN `Microsoft Agent Framework`; The New Stack "Microsoft joins Google in backing Go for AI agents" (2026-07-12) | **not fetched** (robots disallows Claude agents) | — |
| 2026-10-16 | August | Foundry `five-new-claude-capabilities-now-available-in-foundry`; VS Code 1.133, 1.136 notes | included | 2 rows (+MSRC, +Agent Host blog) |
| 2026-10-16 | September | Foundry July–August roundup, Dev Pack, egress controls, routines GA; AF isolation and "what's new" posts (read; context only) | included | 4 rows (+MSRC, +VS Code 1.138/1.140, +E03) |
| 2026-10-16 | September | The Register "Microsoft agentically ports Copilot runtime to Rust for $120K" (2026-09-18, fetched as `Claude-User`) | read raw; its primary source is github.blog and the runtime is the GitHub Copilot runtime → **routed to watchlist 033**, not ledgered here | 0 |
| 2026-10-16 | Oct 1–12 | VS Code 1.141 notes; AF GHSA advisories; AF python-1.21.0; Azure MCP Server 3.0.0 release | included | 4 rows |
| 2026-10-16 | Oct 1–12 | HN `Microsoft Foundry`: "Microsoft-Decision-1" (commandline.microsoft.com, 2026-10-09) | not opened (model announcement, not developer tooling) | 0 |
| 2026-10-16 | cross-window | HN `Microsoft Copilot`, `Microsoft Build`, `Semantic Kernel`, `Microsoft MCP` | out-of-scope items noted, not used: Copilot Cowork exfiltration (PromptArmor, M365), M365 Copilot adoption (Windows Latest), Copilot+ branding, Surface hardware, MAI-Thinking-1, Flint visualization language | 0 |

## Inaccessible or not used

- blogs.microsoft.com, news.microsoft.com (homepage), blogs.windows.com: HTTP 403 (Cloudflare/WAF) to curl. The earlier report's three blogs.microsoft.com sources were read only via WebFetch summaries; their quotes/figures are **not** raw-confirmed.
- microsoft.ai MAI-Code-1-Flash launch page: HTTP 403.
- thenewstack.io: robots.txt disallows Claude agents — not fetched.
- bleepingcomputer.com: Cloudflare challenge on robots.txt and pages — not fetched.
- Reuters and other wire coverage: not searched (no web-search budget).

## Empty or thin segments

No segment was empty. August has the fewest rows (4); this reflects selection (one VS Code release per fortnight, monthly advisories) rather than inactivity — weekly VS Code releases and Agent Framework releases continued every month.

## Embedded instructions and untrusted content

- The Agent Framework FIDES post contains a demonstration prompt-injection string (`[SYSTEM OVERRIDE]`); treated as data.
- Agent Framework and Foundry tutorials contain setup commands (`az login`, `pip install --pre ...`, `go get ...`); none were run.
- No page contained instructions addressed to AI agents that were acted on.
