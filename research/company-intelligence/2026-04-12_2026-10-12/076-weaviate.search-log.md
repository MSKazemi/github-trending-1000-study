# Weaviate (076) — provisional source-query and inclusion log

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** Companion to the [report](076-weaviate.md) and [event ledger](076-weaviate.events.csv) for [#144](https://github.com/MSKazemi/github-trending-1000-study/issues/144). Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

**Window:** 2026-04-12 to 2026-10-12 inclusive (UTC dates). **Accessed:** 2026-10-16.

**Method:**
- Raw HTML was retrieved with `curl` using a generic `Mozilla/5.0` User-Agent. No personal identifier, email address or credential was sent to any site. sec.gov/EDGAR was not contacted.
- Text was extracted locally, and every number, version, date and quote used in a ledger row was confirmed with keyword search against that text.
- `gh api` was used for GitHub releases, tags, commits, repository metadata, licence files at tags and the GitHub Advisory Database. The NVD CVE API, the PyPI JSON API and the npm registry were also queried.
- Two public web searches were run as leads only. WebFetch was not used for any figure.

**This is not exhaustive retrieval.** Search-engine result totals were not exposed and are recorded as unknown, not zero. No page snapshots or hashes were archived in the repository, so pages may change after access.

## Query and source log by segment

| Date | Segment | Exact query or source request | Opened / decision | Found / screened / excluded |
|---|---|---|---|---|
| 2026-10-16 | all | `GET https://weaviate.io/blog/rss.xml` | 20 items only (2026-05-21..10-15); insufficient for April–May | 20 / 20 / see below |
| 2026-10-16 | all | `GET https://weaviate.io/blog`, `/blog/page/2`, `/blog/page/3` | slug-to-date mapping recovered; 23 in-window posts + 2 post-window | 25 / 25 opened as raw HTML |
| 2026-10-16 | all | `GET https://weaviate.io/sitemap.xml`; `https://docs.weaviate.io/sitemap.xml` | 601 / 408 URLs; no per-page lastmod (site) — used for discovery only | — |
| 2026-10-16 | all | `gh api repos/weaviate/weaviate/releases --paginate` filtered `published_at >= 2026-04-01` | 86 release objects; 74 stable + 8 RCs in window; 14 release bodies fetched; v1.39.3, v1.38.7, v1.37.10, v1.36.18 read in full, v1.37.0, v1.38.0, v1.39.0, v1.40.0 read via section headings and keyword search; the other six fetched but not read beyond titles | 12 rows; most patch releases represented by title only and not ledgered |
| 2026-10-16 | all | `gh api repos/weaviate/weaviate/security-advisories`; `gh api advisories?ecosystem=go&affects=github.com/weaviate/weaviate`; `advisories?cve_id=...` | repo-level advisories: only a 2023 item; global DB: GHSA-jqpm-wf57-qx5c (2026-06-08) in window; GHSA-667j-56pf-pq9c and GHSA-8456-r8c8-j656 found via CVE lookup (both unreviewed) | 3 in-window |
| 2026-10-16 | all | `GET https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch=weaviate` | 7 results; in-window: CVE-2026-11500 (Jun 8), CVE-2026-59093 (Jul 2), CVE-2026-105145 (Oct 4); CVSS values read from JSON | 7 / 7 / 4 pre-window or third-party (MindsDB) excluded |
| 2026-10-16 | all | `gh api repos/weaviate/weaviate/commits?path=LICENSE`; `contents/LICENSE`, `contents/wl` and `contents/wl/LICENSE-WEAVIATE` at tags v1.37.0…v1.40.0 | licence commits 2026-08-26 (×4), 09-15 (×2), 09-30; `wl/` absent through v1.39.3 and v1.38.21, present from v1.39.4; v1.40.0 `wl/` contains namespaces, backupdedupe, selfrecovery | 3 commit rows |
| 2026-10-16 | all | `gh api orgs/weaviate/repos?sort=created` (30 newest) | in-window new repos: suggest-query-demo (MIT), weaviate-test-reporter (BSD-3), hermes-weaviate-engram (MIT), engram-plugins (no licence detected), weaviate-otel-collector (none), scaling-reranked-retrieval (MIT), production-best-practices-training (none), homebrew-tap (none), weaviate-cloud (MIT) | weaviate-cloud and engram-plugins used |
| 2026-10-16 | all | `GET https://pypi.org/pypi/weaviate-client/json`, `/weaviate-agents/json`; `GET https://registry.npmjs.org/weaviate-client` | upload times per version; licence metadata (BSD 3-clause; weaviate-agents: none in PyPI metadata; npm BSD-3-Clause) | — |
| 2026-10-16 | all | `gh api` releases for weaviate-python-client, typescript-client, weaviate-go-client, java-client, csharp-client, weaviate-cloud | Python 4.21.0–4.23.1; TS 3.13.0–3.15.0; Go v5.7.3 and v6 alpha→RC; Java 6.2.0–6.3.1; C# 1.1.0–1.2.0 | 5 rows; Java/C# not ledgered (feature-parity releases) |
| 2026-10-16 | Apr 12–30 | posts `aws-shared-cloud-launch`, `engram-deep-dive`, `weaviate-1-37-release` | first two ledgered; 1.37 blog folded into v1.37.0 row | — |
| 2026-10-16 | Apr–Jul | web search `Weaviate vector database news 2026 funding OR acquisition OR layoffs OR CEO` | result summary pointed to DigitalOcean release notes → fetched raw and ledgered (Apr 28, Jul 1). CB Insights, Owler, tech.eu funding tracker, Ramp, dio.me, kunalganglani, firstaimovers: aggregators or trackers, **E0**, not used. No in-window funding/acquisition/leadership news found | unknown / ~9 / 8 |
| 2026-10-16 | May | posts `retrieval-quality-rag-overview`, `tokenization-text-analysis-weaviate`, `coding-assistant-weaviate-mcp`, `rbac-overview` | 2 rows; May 6 and May 14 posts excluded (explainers) | — |
| 2026-10-16 | May | `gh api repos/weaviate/mcp-server-weaviate` + commits + README | deprecation commit 2026-05-25, merge 2026-05-26; no licence detected | 1 row |
| 2026-10-16 | June | posts `engram-generally-available`, `weaviate-free-tier`, `data-import-best-practices`, `weaviate-1-38-release` | 3 rows; data-import how-to excluded | — |
| 2026-10-16 | June | `gh api repos/weaviate/Verba` + commits + README | archived; final commit "goodbye" 2026-06-08; README "Project Discontinued" | 1 row |
| 2026-10-16 | July | posts `query-profiling`, `building-foundry-ai-creative-workflows` | both excluded (explainer of a 1.37 preview feature; demo-app series) | — |
| 2026-10-16 | July | `GET https://www.vulncheck.com/advisories/weaviate-privilege-escalation-via-unchecked-permissions-in-rbac-role-assignment`; `gh api repos/weaviate/weaviate/pulls/11493` | advisory read raw (CVSS 8.7 v4; date 7/2/2026); PR merged 2026-05-28T09:33Z | 1 row |
| 2026-10-16 | August | posts `search-mode-effort`, `building-foundry-where-workflows-break`, `weaviate-1-39-release` | 1 row + 1.39 blog folded into v1.39.0 row; Foundry part 2 excluded | — |
| 2026-10-16 | September | posts `charts-tables-pdfs`, `building-foundry-creative-search`, `hfresh`, `4-bit-rotational-quantization`, `engram-memory-practical-guide` | HFresh and RQ4 ledgered; charts/PDF how-to, Foundry part 3, Engram guide excluded | — |
| 2026-10-16 | September | web search `Weaviate license key enterprise "Weaviate License" open source 2026` | [PromptQuorum review](https://www.promptquorum.com/power-local-llm/weaviate-review) fetched raw (datePublished 2026-09-19) and ledgered as an unassessed third-party description; ki-syndikat, usagepricing, eesel, vantaige, is4.ai, firstaimovers, modern-datatools excluded (aggregators, E0) | unknown / 9 / 8 |
| 2026-10-16 | Oct 1–12 | posts `weaviate-security-release-googlemodules-2026`, `engram-for-claude-code` | both ledgered | — |
| 2026-10-16 | post-window | posts `pathseer-filtered-vector-search` (Oct 14), `weaviate-security-release-nearobject-2026` (Oct 15); releases v1.40.1 (Oct 13), wcloud v0.1.2 (Oct 13) | **excluded** as out of window; nearObject post mentioned only as context for the v1.39.3 row | — |
| 2026-10-16 | cross-window | HN Algolia `search_by_date?query=weaviate&tags=story` and `tags=comment`, `created_at_i` 1775952000–1792022400 | 9 stories (several vendor-submitted blog links; one third-party GUI "Show HN", Aug 26); 33 comments (job-ad keyword lists, incidental mentions). No critical discussion of the licence change found | 9+33 / all / 0 rows |
| 2026-10-16 | cross-window | `GET https://weaviate.io/company/about-us`, `/company/investors`, `/pricing` | latest press item: 2023 Series B; no in-window corporate event | — |

## Inclusion, deduplication and conflicts

- **Included:** 37 rows: Apr 6, May 4, Jun 8, Jul 4, Aug 3, Sep 7, Oct 5. Every row cites a URL that was fetched as raw text or queried by API. No row relies on a search snippet alone.
- **Duplicate groups:**
  - `076-003`: Engram, preview deep dive (Apr 21) and GA (Jun 3).
  - `076-004`: Go client v6, alpha.1 and rc.0.
  - `076-006`: DigitalOcean, Apr 28 and Jul 1.
  - `076-012`: v1.38.0 release notes and the 1.38 blog.
  - `076-025`: licence split, four rows (two commits, the enterprise-text commit and the third-party review).
  - `076-026`: v1.39.3 release and the Oct 1 security disclosure.
- **Date conflicts recorded, not resolved:**
  - Python client 4.21.0: PyPI 2026-04-23T10:37Z vs GitHub release 2026-04-28T13:36Z.
  - Python client 4.23.0: GitHub 09:00Z vs PyPI 14:23Z, same day.
  - CVE-2026-59093: fix merged 2026-05-28, shipped 2026-06-05, CVE published 2026-07-02.
  - Google-module fix: released 2026-09-07, disclosed 2026-10-01.
  - DigitalOcean page: "Last verified 27 Apr 2026", but JSON-LD date 2026-07-01.
- **Label conflicts:**
  - MCP server: "GA" (1.38 blog) vs "Preview" (v1.38.0 notes).
  - Built-in MCP availability: "from v1.37.1" (standalone README) vs v1.37.0 notes.
  - Boost and MMR: "GA" in the 1.39 blog while the v1.39.0 notes carry no GA label.
  - v1.40.0: "Breaking Changes: none" alongside licence gating of Namespaces.
- **Figures confirmed against raw text:**
  - US East (N. Virginia) and Frankfurt (AWS post);
  - "many millions of active Weaviate databases" and "rapidly approaching double-digit millions" (free-tier post);
  - nDCG@10 57.5 vs 13.0, weaviate-agents 1.8.0 (Search Mode post and PyPI);
  - "45% heap reduction" (RQ4);
  - "Cost Optimized profile" (HFresh);
  - CVSS 7.1 and "< v1.39.3" (Google modules);
  - "up to 1,000 runs per month" (Engram plugin);
  - CVSS 8.8 and 8.7 (CVE-2026-59093, NVD JSON and VulnCheck page);
  - CVSS 5.0 / 1.3 / 4.6 (CVE-2026-11500, NVD JSON) and GHSA severity "low";
  - CVSS 3.1 5.3 (CVE-2026-105145);
  - `wv8.<license_id>` key form and "makes no network requests" (commit message).
  All of these remain **vendor or third-party statements**, not verified measurements.
- **Not ledgered, noted:** Ramp vendor-share figures conflict between a search snippet (June 2026: 15%) and the live page (October 2026: 10%). This is a spend-tracker estimate, graded E0. A search summary also claimed "Weaviate 1.32 … March 2026"; release tags contradict it, so it was not used.

## Embedded instructions seen (treated as data, not followed)

- `weaviate.io/blog/coding-assistant-weaviate-mcp` contains an "Agent runbook: autonomous setup" section. It holds scripts that an agent is meant to copy and run, including cloning a third-party repository into `/tmp`. **Not executed.**
- `docs.digitalocean.com/release-notes/weaviate/` contains a "For AI agents:" note that points to an `llms.txt` index. **Not followed.**
- The `weaviate/weaviate` repository root contains a `CLAUDE.md` with imperative instructions for coding agents ("you MUST address it in the same change set"). It was read only as M1 context. **Not followed.**
- The Engram plugin post contains shell and plugin-install commands for users. **Not run.**

## Missing, inaccessible or not attempted

- `https://status.weaviate.io/` returned no response (curl code 000), so no incident history was available.
- `https://weaviate.io/enterprise-edition`, the link named in the licence text, returned HTTP 404 on 2026-10-16.
- Docs URLs `https://weaviate.io/developers/weaviate/more-resources/deprecations` and `https://docs.weaviate.io/deploy/configuration/license-key` returned 404, and no licence-key documentation page was found in the docs sitemap.
- VulDB pages were not fetched. Their statements are cited only as carried in NVD and GHSA records.
- Not read: Weaviate terms of service and Engram data-handling terms, the DigitalOcean preview legal terms, and the agents-typescript-client 1.7.0 release.
- No independent journalism about Weaviate was found in the window, and the licence change in particular had no press coverage that we found. Only two web searches were possible because the session search budget was nearly exhausted.
- No product was installed or executed, no account was created, nothing was scanned, no paywall was circumvented and no energy was measured.
- **Reproduction:** re-run the requests above with UTC timestamps and save raw HTML hashes. Before any evidence is promoted beyond provisional status, an independent human should spot-check:
  - the licence rows (CI2026-076-025, 029, 031, 032, 036);
  - the security rows (013, 020, 026, 033, 035);
  - the MCP label conflict (002, 012, 018).

## Spot-check access note (2026-10-16)

- weaviate.io robots.txt (`User-agent: *`) disallows `/blog/rss.xml`, `/*?*` and feed paths. The independent spot-check therefore did not fetch the RSS feed and used individual post pages only. The original RSS request above was made against that rule.
