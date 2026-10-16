# Socket (093) — provisional source-query and inclusion log

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** Companion to the [report](093-socket.md) and [event ledger](093-socket.events.csv) for [#161](https://github.com/MSKazemi/github-trending-1000-study/issues/161). Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

**Window:** 2026-04-12…2026-10-12 inclusive (UTC dates). **Accessed:** 2026-10-16. **Method:** robots.txt checked before each new host (rules for `*` and for ClaudeBot / Claude-User / Claude-SearchBot / anthropic-ai); raw retrieval with `curl` and a generic `Mozilla/5.0` User-Agent (no personal identifier, email or credential sent to any site; User-Agent never switched to pass a block); text extraction and keyword-in-context checks of every number, version, date and quote used in a ledger row; `gh api` for GitHub repositories, releases, changelogs, licences and advisories; npm and PyPI JSON; Hacker News Algolia API and item pages; a small number of public web searches (snippets used only as leads, never as evidence). SEC/EDGAR was not contacted. **This is not exhaustive retrieval.** Search-engine result totals were not exposed and are recorded as unknown, not zero. No page snapshots were archived in the repository.

## Inaccessible or skipped sources

| Source | Result | Handling |
|---|---|---|
| `https://socket.dev/robots.txt`, `/`, `/blog`, `www.socket.dev/robots.txt` | HTTP 403 Cloudflare "Just a moment…" challenge | Logged as inaccessible; not bypassed (no alternate client, UA switch or mirror host such as a badge subdomain was used to read blog content). All Socket blog posts are therefore unread |
| `https://docs.socket.dev/changelog` | HTTP 404 | No product changelog page; engine changelog used instead |
| `https://www.securityweek.com/socket-raises-60-million-at-1-billion-valuation/` | HTTP 403 | not used |
| BleepingComputer (Bitwarden), The Hacker News (Bitwarden) | Cloudflare challenge | not used |
| `https://www.scworld.com/brief/compromised-github-actions-re-enabled-posing-supply-chain-risks` | HTTP 403 | not used |
| heise.de TanStack article | robots.txt disallows `anthropic-ai` for the path | **skipped by rule**; TanStack's own postmortem used instead |
| status.socket.dev `/api/`, `/embed/` | disallowed by robots.txt | not requested; public `/history` and `/history.atom` used |

## Query and source log by segment

| Date | Segment | Exact query or source request | Opened / decision | Found / screened / excluded |
|---|---|---|---|---|
| 2026-10-16 | all | `gh api orgs/SocketDev/repos --paginate` | 57 repos; 10 created in window (abitious, socket-scan-patterns, socket-page-automation, socket-facts, odai, node-smol, socket-registry-firewall-deployments, decmpfs, envrypt, ajar) — none ledgered (no dated release notes or tooling unrelated to the study angle) | 57 / 57 / — |
| 2026-10-16 | all | `gh api repos/SocketDev/{socket-cli,socket-mcp,sfw-free,socket-patch,socket-python-cli,bun-security-scanner,socket-basics,socket-registry-firewall,action,firewall-release,socket-sdk-js,socket-sdk-python,socket-vscode}/releases` | in-window counts 489, 20, 13, 5, 78, 1, 9, 100, 0, 13, 10, 10, 0; socket-cli releases v0.14.100…v1.1.0 bulk-created 2026-07-24 and socket-mcp 0.0.4–0.0.19 bulk-created 2026-06-15 (not release dates) | ~750 / minor+major read / patch and CI-only releases folded |
| 2026-10-16 | all | `gh api …/contents/CHANGELOG.md` for socket-cli and socket-mcp | socket-cli default-branch changelog stops at 2.1.0 (2025-11-02) and was not used for window dating; socket-mcp changelog used | — |
| 2026-10-16 | all | `gh api repos/SocketDev/{sfw-free,socket-basics}/license`; repo licence fields | sfw-free and socket-basics: PolyForm Shield 1.0.0 (GitHub: NOASSERTION/Other); socket-registry-firewall, firewall-release: none detected | — |
| 2026-10-16 | all | `GET https://registry.npmjs.org/{socket,@socketsecurity%2fcli,@socketsecurity%2fmcp,sfw,@coana-tech%2fcli,@bitwarden%2fcli}` | time maps and licences; `socket` 106 in-window versions; 2.0.0–2.1.0 (2025) deprecated "bad build"; `@coana-tech/cli` 176 in-window versions, no licence field | 6 packages |
| 2026-10-16 | all | `GET https://pypi.org/pypi/socketsecurity/json` | 78 in-window releases 2.2.81…2.10.11; MIT text | — |
| 2026-10-16 | all | `GET https://docs.socket.dev/robots.txt`, `/sitemap.xml`, `/llms.txt`; `docs/{reachability-analysis-changelog,remote-socket-mcp,guide-to-socket-mcp,socket-firewall-overview,socket-firewall-free}.md` | 266 sitemap URLs; engine changelog lists 254 versions (2026); doc pages carry `updatedAt` only and were used as background | 6 opened / 2 rows |
| 2026-10-16 | all | Hacker News Algolia `search_by_date` with `numericFilters=created_at_i>1775952000,created_at_i<1792022400`: `socket.dev` (restricted to url), `"Socket Security"`, `Socket researchers`, `Socket Firewall`, `socket.dev` (all fields) | 43 url-matched stories (titles used as leads); 0 hits for `"Socket Security"` and `Socket researchers`; 13 item pages fetched to confirm titles/dates | 43 / 43 / 31 not ledgered |
| 2026-10-16 | all | `GET https://status.socket.dev/history` and `/history.atom` | 25 incidents 2026-07-16…2026-10-01; 2 rows (Firewall-related Aug 12/20; DB restart Sep 30) | 25 / 25 / 23 |
| 2026-10-16 | Apr 12–30 | web search `Bitwarden CLI npm compromised April 2026 Checkmarx supply chain Socket statement` | CyberInsider read (Socket attribution, Bitwarden statement); Linuxiac read (Bitwarden window 5:57–7:30 PM ET; no Socket mention); BleepingComputer/THN challenged; borecraft excluded (unknown outlet) | unknown / 5 / 3 |
| 2026-10-16 | Apr 12–30 | `gh api /advisories?type=malware&ecosystem=npm&affects=@bitwarden/cli` | GHSA-g98r-qjhg-4fmr (2026-04-23T17:07Z; no Socket credit) | independent artifact |
| 2026-10-16 | Apr 12–30 | BankInfoSecurity article linked from the Series C story: `socket-buys-secure-annex-to-expand-supply-chain-visibility-a-31562` | read raw; dated April 30, 2026 | included |
| 2026-10-16 | Apr 12–30 | HN leads not ledgered | 108 Chrome extensions (Apr 14), Open VSX GlassWorm sleepers (Apr 25), Namastex CanisterWorm (Apr 26), SAP CAP npm (Apr 29), Checkmarx KICS (Apr 22–23; folded into CI2026-093-003 via CyberInsider) | title-only |
| 2026-10-16 | May | web search `Socket supply chain security Series C $60 million $1 billion valuation May 2026` | BankInfoSecurity read raw (May 26, 2026); SecurityWeek 403; pulse2, aiweekly, offseq, itbrief excluded as aggregators/rewrites (E0); bankinfosecurity.net/govinfosecurity are mirrors of the same ISMG story | unknown / 10 / 9 |
| 2026-10-16 | May | web search `TanStack npm packages compromised Mini Shai-Hulud May 2026 postmortem` | TanStack postmortem read raw (Socket phone call; StepSecurity first); heise skipped (robots); Snyk/Semgrep/Cloudsmith/The Register not needed | unknown / 9 / 8 |
| 2026-10-16 | May | `gh api /advisories?ecosystem=npm&affects=@tanstack/react-router` | GHSA-g7cv-rxg3-hmpx (2026-05-12T00:12Z; references Socket's blog URL, StepSecurity, NVD CVE-2026-45321, CISA KEV link) | independent artifact |
| 2026-10-16 | May | web search `Laravel Lang compromised backdoor May 2026 laravel-lang statement` | Security Affairs read raw (cites Socket and Aikido); phoenix.security, gridinsoft, cti.ngrok, backlist excluded (vendor blogs/aggregators); no official Laravel-Lang statement found | unknown / 9 / 8 |
| 2026-10-16 | May | HN leads not ledgered | node-ipc (May 15; GHSA-pvh2-rg5g-69v7 dated May 29), AntV (May 19; GHSA-hqrw-phww-294v), TrapDoor (May 24–27), "AI Has Taken over Open Source" (May 25), PyPI audit fixes (May 2), fsnotify dispute (May 12), Ruby/Go modules (May 1) | title-only |
| 2026-10-16 | June | HN lead `Malicious PyPI Wheels Target Bioinformatics and MCP Developers` (item 48462293) | ledgered as E0 | — |
| 2026-10-16 | June | socket-mcp npm/CHANGELOG | 0.0.18 (Jun 5), 0.0.19 (Jun 15), 0.0.20 (Jun 18) | 1 row |
| 2026-10-16 | June | HN leads not ledgered | Rolldown/React Compiler news (Jun 28, ecosystem news), "Socket Firewall" features page (Jun 17, undated marketing) | — |
| 2026-10-16 | July | engine changelog 15.6.x–15.9.x; sfw-free 1.13.1–1.15.0; socket-basics 2.1.0–2.2.1 | 4 rows incl. Mastra E0 | — |
| 2026-10-16 | July | `gh api /advisories?type=malware&ecosystem=npm&affects=@mastra/core` | GHSA-pp62-grrw-hvfp dated 2026-06-17 (relation to July lead unknown) | check only |
| 2026-10-16 | July | HN leads not ledgered | npm 12 install scripts off by default (Jul 9; npm/GitHub event, not Socket's), PolinRider campaign page (Jul 6) | — |
| 2026-10-16 | August | web search `Socket "Mythos" AI agent social engineer open source maintainer merge malware August 2026` | Malwarebytes read raw (dated 2026-08-06; does not mention Socket); Socket post, daily.dev, Slashdot not read/used | unknown / 9 / 8 |
| 2026-10-16 | August | web search `Rust crates compromised build-time supply chain attack August 2026 crates.io Socket` | Rust blog index and `2026/08/20/supply-chain-attack-on-arrayref` read raw (credits Nextron Systems); rankiteo, gajshield, offseq excluded (aggregators); socket.dev/badge.socket.dev URLs not fetched | unknown / 9 / 8 |
| 2026-10-16 | August | `gh api /advisories?type=malware&ecosystem=npm&affects=keyv` | GHSA-3p9h-f68w-m6fx (2026-08-04T11:19Z; keyv = 6.0.0) | 1 row |
| 2026-10-16 | August | socket-basics 3.0.0, socket-patch 4.0.0 releases; status feed | 3 rows | — |
| 2026-10-16 | August | HN leads not ledgered | Chrome VPN extensions (Aug 12), npm RAT targeting Alibaba (Aug 10), Firefox crypto-wallet extensions (Aug 20), Tokio package page (Aug 4, package-page link not an event) | — |
| 2026-10-16 | September | web search `"Mini Shai-Hulud" compromised GitHub Actions re-enabled September 2026` | BleepingComputer/THN challenge, SC World 403; rescana, ogwilliam, aicybr excluded (unknown/aggregator); `gh api repos/actions-cool/{issues-helper,maintain-one-comment}` → "Repository access blocked", reason tos, created 2026-09-24T23:51:05Z / 23:51:54Z | unknown / 9 / 9; API check used |
| 2026-10-16 | September | socket-mcp 0.1.0–0.2.1; socket-cli 1.2.0–1.4.0; status Sep 30 | 4 rows | — |
| 2026-10-16 | September | HN leads not ledgered | MemTensor npm/PyPI (Sep 24), Firefox Google-account extension (Sep 24) | — |
| 2026-10-16 | Oct 1–12 | socket-cli 1.5.0–1.8.0; engine 15.11.x–15.12.7; socket-patch 5.0.0; sfw-free 1.15.4 | 3 rows; Oct 13–16 items (engine 15.12.8, CLI 1.8.1–1.8.3) post-window and excluded | — |
| 2026-10-16 | cross-window | web search `Socket.dev false positive malware flag criticism maintainer 2026` | snippet mentions a January 2026 mis-flagging incident on Socket's status page (pre-window; not read; E0) and a 2025 Register article (pre-window); no 2026 maintainer complaint found; rywalker, plushcap, rfp.wiki, pingoru excluded | unknown / 10 / 10 |
| 2026-10-16 | cross-window | web search `Socket launches 2026 AI agent skills scanning MCP server security product announcement socket.dev` | no Socket result; other vendors' tools only | unknown / 9 / 9 |

## Months with thin findings

- **June 2026:** only an E0 lead and the MCP server changelog; no independent coverage found. This likely reflects the unreadable Socket blog, not an absence of activity.
- **October 1–12:** vendor release artifacts only; no independent coverage found.

## Embedded agent instructions observed

- docs.socket.dev Markdown pages carry front-matter `agentTools: projectIndex: https://docs.socket.dev/llms.txt` — a metadata pointer, not an instruction; `llms.txt` was read as data (a documentation index) and contained no directives to agents. No other page contained instructions aimed at AI agents. Nothing from any page was executed.

## Personal-data note

GitHub release notes and HN pages contain individual contributor/submitter handles; none were copied into the ledger. Company executives are named only as quoted in press coverage.
