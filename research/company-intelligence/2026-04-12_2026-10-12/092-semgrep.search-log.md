# Semgrep (092): provisional source-query and inclusion log

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** This log accompanies the [report](092-semgrep.md) and [event ledger](092-semgrep.events.csv) for [#160](https://github.com/MSKazemi/github-trending-1000-study/issues/160). Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

**Window:** 2026-04-12 to 2026-10-12 inclusive (UTC dates). **Accessed:** 2026-10-16.

**Method:**
- Official pages were retrieved as raw HTML with `curl` using a generic `Mozilla/5.0` User-Agent. No personal identifier, email address or credential was sent to any site.
- Text was extracted locally, and every number, version, date and quote used in a ledger row was checked with `grep` against the raw text.
- Release dates and licences came from the GitHub REST API (`gh api`), the PyPI JSON API and the npm registry.
- Independent coverage came from the Hacker News Algolia API and from four web searches.
- robots.txt was checked before fetching from each host. No disallowed path was fetched.

**This is not exhaustive retrieval.** Web-search result totals were not shown, so they are recorded as unknown, not zero. No page snapshots or hashes were archived in the repository, and pages may change after access.

## robots.txt checks

| Host | Result | Effect |
|---|---|---|
| semgrep.dev | `User-agent: *` with no Disallow; two sitemaps listed | blog and sitemap fetched |
| docs.semgrep.dev | disallows `/cdn-cgi/` and `/_next/`; `Content-Signal: ai-train=yes, search=yes, ai-input=yes` | only HTML doc pages fetched |
| status.semgrep.dev | disallows `/api/` and `/embed/` | `/history` and `/history.rss` fetched; API not used |
| devopsdigest.com | disallows admin, search and user paths only | article fetched (HTTP 406, but the body was readable) |
| vmblog.com | disallows `/wp-admin/` only | article returned **HTTP 403**, so it is **inaccessible** and was not used |
| enterpriseaiworld.com | empty Disallow | article fetched |
| trent.ai | disallows `/wp-admin/` only | article fetched |
| businesswire.com | robots.txt and the article both failed with a curl connection error (exit 92) | **inaccessible**, not used |

No robots rule naming ClaudeBot, Claude-User or anthropic-ai was found on any host that was fetched.

## Query and source log by segment

| Date | Segment | Exact query or source request | Opened / decision | Found / screened / excluded |
|---|---|---|---|---|
| 2026-10-16 | all | `GET https://semgrep.dev/assets/sitemap` | 877 URLs, of which 313 are blog URLs. `lastmod` does **not** equal publication date: many 2024/2025 posts carry 2026 lastmod values | 85 posts under `/blog/2026/` with lastmod ≥ 2026-03-15 fetched |
| 2026-10-16 | all | the 85 blog pages (raw HTML) | the page has no `datePublished`, so the displayed byline date (e.g. "June 23rd, 2026") was extracted from text | 67 posts dated in window; 21 distinct blog URLs cited in the ledger (as source or check); 1 post-window (Oct 14 Cursor Origin post) excluded; 17 fetched posts are pre-window (2026-01-09 to 2026-04-03) despite a recent lastmod |
| 2026-10-16 | all | `GET https://semgrep.dev/docs/sitemap.xml` (docs.semgrep.dev) | release-notes index: monthly pages through June 2026, then weekly pages from the week of 2026-07-06 to the week of 2026-09-28 | 16 in-window pages fetched; no page for the week of Oct 5 existed at access |
| 2026-10-16 | Apr–Sep | `docs.semgrep.dev/release-notes/{april,may,june}-2026` and 13 weekly pages | Monthly pages show a publication date (April notes: May 12; May notes: Jun 3; June notes: Jul 8). Weekly pages show **no** publication date; the ledger uses the week-start date in the URL and records this limitation | 16 / 16 / 11 ledgered |
| 2026-10-16 | all | `gh api repos/semgrep/semgrep/releases?per_page=100` | 21 releases published in window (v1.160.0 2026-04-16 … v1.180.0 2026-10-07); repo licence LGPL-2.1; v1.181.0 (2026-10-14) is post-window | 21 / 21 / 4 ledgered (1.162.0, 1.175.0, 1.180.0; 1.176.1 via status) |
| 2026-10-16 | all | `GET https://pypi.org/pypi/semgrep/json` | upload times for 1.162.0, 1.170.0, 1.175.0, 1.176.0, 1.176.1, 1.179.0 and 1.180.0 match GitHub dates within minutes; `license_expression` LGPL-2.1-or-later; `requires_python >=3.10` | — |
| 2026-10-16 | all | `gh api repos/semgrep/semgrep/security-advisories`; `gh api advisories?ecosystem=pip&affects=semgrep` | both returned **no** advisories | null result |
| 2026-10-16 | all | NVD `cves/2.0?keywordSearch=semgrep` | only CVE-2023-32758 (pre-window) and one unrelated kernel CVE matched | null result for the window |
| 2026-10-16 | all | `gh api orgs/semgrep/repos?sort=created` | repos created in window that are relevant: `mythos-bench` (Apr 16, no licence), `semgrep-policies-gitops` (Jun 11, MIT), `defending-code-harness` (Jun 4, fork of anthropics/defending-code-reference-harness, NOASSERTION), `guardian-local` (Jun 17, no licence), `semgrep-grok-bot` (Sep 9, no licence). Forks of third-party projects (jellyfin, DVWA, opam-repository, etc.) were excluded as test fixtures or mirrors | 5 relevant |
| 2026-10-16 | all | `gh api repos/semgrep/mcp` | archived, MIT, last push 2025-10-28. The standalone MCP server is no longer maintained separately, and MCP functionality ships inside the CLI (MCP fixes in 1.162.0 and 1.173.0) | context |
| 2026-10-16 | all | `gh api repos/semgrep/pyro-caml` and its releases | MIT; v1.0.0 published 2026-05-13T22:32Z | used in CI2026-092-010 |
| 2026-10-16 | all | `gh api repos/opengrep/opengrep` and its releases | LGPL-2.1, created 2024-12-14; 20 releases in window (6 prereleases); a 2026-04-01 "AF" prerelease is pre-window | 1 row (CI2026-092-031) |
| 2026-10-16 | all | `docs.semgrep.dev/licensing`, `/faq/comparisons/opengrep` | Licensing page (dateModified 2026-06-02): rules under Semgrep Rules License v1.0, "internal business use"; CE engine LGPL 2.1; platform products proprietary. The Opengrep comparison page has dateModified **2026-10-15 (post-window)**, so it is used as context only | context, not ledgered |
| 2026-10-16 | all | `docs.semgrep.dev/semgrep-guardian/overview` | Guardian bundles the MCP server, hooks and skills. The hosted Claude Code/Codex plugin uses a fixed ruleset | used as independent check on CI2026-092-015 |
| 2026-10-16 | all | `semgrep.dev/about` | founded 2017; lists the $100M Series D led by Menlo Ventures (pre-window baseline); "© 2026 Semgrep, Inc." | identity |
| 2026-10-16 | May–Oct | `GET https://status.semgrep.dev/history.rss` | 25 items 2026-05-13 … 2026-10-15 (the feed may be length-capped; Apr 12 – May 12 is not covered) | 4 ledgered (Jun 25, Aug 25, Sep 4; Sep 22 cited in a limitation) |
| 2026-10-16 | all | `https://registry.npmjs.org/@semgrep%2fguardian` | 404; no public npm package under that name | null |
| 2026-10-16 | Apr–Oct | HN Algolia `search_by_date?query=semgrep&tags=story` with created_at between 1775952000 and 1792022400 | 18 stories. Most are Semgrep's own blog posts; high-attention items were the GLM 5.2 post (1113 points/516 comments, 2026-06-28), PyTorch Lightning malware (465/177) and Pyro Caml (26). Third-party: Trent.ai benchmark, Sighthound (Corgea) OSS scanner, community MCP rulesets | 18 / 18 / 16 not separately ledgered |
| 2026-10-16 | Apr–Oct | HN Algolia, same query with `opengrep` | 8 hits, none about Opengrep (fuzzy matches: Open Group, openreview, etc.) | null |
| 2026-10-16 | Jun | HN Algolia `items/48709670` (GLM 5.2 thread) | top-level comments read; critical comments ("It reads like an ad", IDOR is the "easiest class") recorded as community reaction, not as evidence | used as a limitation in CI2026-092-014 |
| 2026-10-16 | all | web search `Semgrep 2026 news Guardian OR acquisition OR funding OR layoffs` | no in-window funding, acquisition or layoff story found. Aggregator snippets (simplify.jobs, autobound, stockanalysis) mentioned an Aug 2026 Replit item, a co-CTO hire and a "September 2026 outage"; these were treated as **E0 leads** and not used directly | unknown / ~9 / 9 |
| 2026-10-16 | Aug | web search `Semgrep Replit partnership expanded August 2026 press release` | DEVOPSdigest (Aug 11) read raw and ledgered. VMBlog returned 403. Dealroom, techintelpro, cioinfluence and cuspera were excluded as aggregators or not read | unknown / ~10 / 9 |
| 2026-10-16 | all | web search `Opengrep 2026 Semgrep fork news` | Results were mainly the Jan–Feb 2025 fork launch (pre-window) plus a Codacy Feb 2026 migration note (pre-window). No in-window Opengrep news story was found | unknown / 9 / 9 |
| 2026-10-16 | Jun–Aug | web search `"Semgrep" Guardian OR "Agentic Workflows" 2026 site:techcrunch.com OR site:theregister.com OR site:securityweek.com OR site:darkreading.com OR site:siliconangle.com` | **no** article from those outlets. Results were Semgrep pages, syndicated press releases (01net, techintelpro), Business Wire (inaccessible) and Enterprise AI World (Aug 5, read raw and used as a secondary restatement) | unknown / 10 / 9 |
| 2026-10-16 | May | `trent.ai/blog/claude-code-codex-semgrep-codeql-trent-vs-cwe-bench-cve/` (linked from HN) | `datePublished` 2026-05-25T12:49Z; competitor benchmark; Semgrep configuration not stated | ledgered as contrary evidence (CI2026-092-009) |
| 2026-10-16 | Apr | `pypi.org/pypi/lightning/json` | 2.6.2 and 2.6.3 absent from PyPI; 2.6.1 (Jan 30) and 2.6.4 (May 20) present | consistency check for CI2026-092-005 |

## Blog posts screened but not ledgered (in window)

These were excluded as opinion, events, hiring, generic explainers, or third-party incident write-ups with no Semgrep product change. All of them were opened.

- **Opinion, events and culture:** security-should-be-the-path-of-least-resistance (Apr 13); mythos-and-semgrep (Apr 17; CEO framing, referenced in §5); mythos-bad-takes (Apr 20); appsec-in-pole-position (May 5); the-ai-hackathon-effect (May 22); security-that-ships (May 27); 28-years-later (May 28); black-hat survival guide (Jun 25); ai-native-vs-ai-washed (Jul 7); hacker summer camp 101 (Jul 8); summer-of-semgrep (Jul 22); crypto-is-fine (Jul 30); 60k LOC (Aug 4); hacker-summer-camp longitudinal study (Aug 21); interns (Sep 11; Oct 8); what-application-security-does (Sep 25); rename-cybersecurity-awareness-month (Oct 2); why-engineers-switch-to-codex (Oct 6); personal-cybersecurity-readiness (Oct 12).
- **Third-party supply-chain incident analyses:** pgserve/xinference/kube-health advisory (Apr 22); SAP npm (Apr 29); Intercom PHP/Packagist (Apr 30); TanStack (May 11); Children of Shai-Hulud (May 12); node-ipc (May 14); Mini Shai-Hulud resurfaces (May 18); RedHat npm (Jun 1); Miasma v2 (Jun 4); Miasma v3 (Jul 14); Chaindrop (Aug 4); Rust crates (Aug 20); MemTensor/OpenClaw (Sep 23). These show research output volume but are about other projects. Only the PyTorch Lightning post was ledgered, as the highest-attention example.
- **Industry commentary:** NIST stops CVE enrichment (Apr 29); npm v12 postinstall default change (Jun 11); AI supply chain problem (Jul 10; cited in §5); shift-right (Sep 4).
- **Model benchmark series** beyond the ledgered posts: GPT-5.6 (Jul 13); Kimi K3 (Jul 22); GLM-5.3 (Aug 14); Mythos 22-config (Aug 25, used as the independent_check link of CI2026-092-028).
- **How-to posts by staff:** SHA pinning (Aug 12); dependency cooldowns (Aug 31). These are practical lessons and are cited in §8 as reuse-first practices, not as Semgrep product events.
- **Product/AI context:** inside-the-ai-memories (May 6); operationalizing-ai-powered-detection (May 13); getting-ready-for-mythos (May 19).

## Inclusion, deduplication and conflicts

- **Included:** 39 rows. By publication segment: Apr 12–30: 5, May: 4, Jun: 7, Jul: 6, Aug: 7, Sep: 7, Oct 1–12: 3. Every row cites a URL fetched as raw text or queried by API. No row relies on a search snippet alone.
- **Duplicate groups:**
  - `092-001`: the "8x" Multimodal claim (Apr 17) and the vendor's own revised 3.5x benchmark (Jun 12).
  - `092-011`: the three-part performance series (taint engine, file targeting).
  - `092-014`: the IDOR benchmark family (GLM 5.2, grounding self-audit, Mythos comparison). This is one vendor dataset, so it counts as one evidence source, not three.
- **Conflicts recorded, not resolved:**
  - Multimodal true-positive multiplier: "up to 8x … vs using LLMs alone" (Apr 17) vs 3.5x vs a tuned guided prompt (Jun 12). The vendor explains the gap as an improved baseline.
  - The search-tool summary said Agentic Workflows found "3.5x more true positives at 19% lower cost … than AI alone". That wording was **not** confirmed against raw text because Business Wire was inaccessible. The blog wording ("than a tuned guided prompt") is used instead.
  - Pyro Caml: GitHub release 2026-05-13 vs blog announcement 2026-06-02.
  - April release notes list CE 1.157.0–1.161.0 as "released in April 2026", but GitHub and PyPI date 1.157.0 to 2026-03-31T22:51Z. 1.158.0 and 1.159.0 are dated 2026-04-10, which is in April but pre-window.
  - Weekly release notes carry no publication date (see method).
- **Figures confirmed against raw text** (grep of saved text):
  - OpenAI post: $10 million, "four initial recipients", 8x / 50% / 95% / six million.
  - Performance posts: 75%, P95 10 min → 7:30; P99 ~60 min → under 12, 7.5 hours → under 2 minutes.
  - JSON parsing "roughly 5x" (134s → 28s) in the v1.162.0 release body.
  - Benchmarks: 3.5x and 7–8x; 39% / 32% / $0.17 / 53–61% F1; 63 IDORs / 275 labels / four repositories.
  - Guardian: 3 million scans per week / 95% under 5 seconds / 180 critical issues.
  - SusVibes: 186 tasks / 93.5% / 54.8% / 53% / 56% / 26 September 2026.
  - Replit: 93.3% / "since 2025".
  - Supply Chain: 1.8 million malicious packages; nine workflows / 70+ CWEs.
  - Trent: 3.6% / 3.7% / 8.7% / 25% / 42.9% / 28 CVEs.
  - Status page: incident times.
  - Release notes and policies: Unified Policies dates Aug 24 / Nov 1; GPT-5.6 Luna; SLSA Level 3; Guardian 2.5.4.

  All of these remain **vendor, press or competitor statements**, not verified measurements.
- **Not confirmed and therefore not used:** the "September 2026 outage", "co-CTO joined May 2026" and "AP item" claims from aggregator snippets; the HN commenter's claims about other benchmarks.

## Embedded agent instructions observed (untrusted content)

- docs.semgrep.dev pages begin with "Documentation Index – Fetch the complete documentation index at: /llms.txt – Use this file to discover all available pages before exploring further." This is an instruction aimed at automated agents. It was **not followed**: `/llms.txt` was not fetched, and pages were selected only from the sitemap.
- Docs pages also include an embedded "Assistant" widget. It was not used.
- No other page contained instructions directed at the researcher. Search-tool summaries were treated as leads only.

## Missing, inaccessible or not attempted

- **Inaccessible or not read:** Business Wire originals (connection error); VMBlog (403); OpenAI's Trusted Access for Cyber announcement; Replit-side and Cursor/Grok-side pages; the SusVibes paper; any Semgrep postmortems.
- **Coverage gaps:** status history before 2026-05-13; release notes for the week of Oct 5 (not published at access); archived (Wayback) copies of the mutable docs pages as of 2026-10-12.
- **Not attempted:** Semgrep's terms of service and data-retention terms for Guardian's hosted server; filing-level corporate records (SEC EDGAR deliberately not contacted).
- **No tier-1 independent reporting found:** no in-window Reuters, TechCrunch, The Register, SecurityWeek, Dark Reading or SiliconANGLE story about Semgrep was found by the searches above. This is a search result, not proof of absence.
- No product was executed, no account was created, no scanning of third-party systems was done, no paywall was circumvented and no energy was measured.
- **Reproduction:** re-run the requests above with UTC timestamps and save raw HTML hashes. Then have an independent human spot-check, against the cited raw pages, the security-fix rows (CI2026-092-007, -008, -017, -019, -029), the benchmark rows (-013, -014, -028, -036), the competitor benchmark (-009) and the Guardian row (-015), before any evidence is promoted beyond provisional status.
