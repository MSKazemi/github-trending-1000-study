# Sonar (095) — provisional source-query and inclusion log

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** Companion to the [report](095-sonar.md) and [event ledger](095-sonar.events.csv) for [#163](https://github.com/MSKazemi/github-trending-1000-study/issues/163). Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

**Window:** 2026-04-12…2026-10-12 inclusive (UTC dates). **Accessed:** 2026-10-16.

**Method:**

- Official pages were retrieved as raw HTML with `curl -sL -A 'Mozilla/5.0'`. No personal identifier, email, GitHub handle or credential was sent to any site.
- Text was extracted locally and every number, date, version and quote used in a ledger row was confirmed with `grep`.
- The Discourse JSON API was used for community announcements.
- `gh api` was used for GitHub releases, licences and repository metadata, and the npm registry JSON for `@sonar/scan`.
- The NVD CVE API and the Hacker News Algolia API were used.
- WebSearch was **not** used, because the session search budget was exhausted. WebFetch summaries were not used.

**This is not exhaustive retrieval.** No page snapshots or hashes were archived in the repository, and pages may change after access.

## robots.txt checks (2026-10-16)

| Host | Result | Action |
|---|---|---|
| www.sonarsource.com | `Allow: /` for `*` and explicitly for ClaudeBot/Claude-User/anthropic-ai; `Disallow: /*?` and `/*/tag/` | Query-string URLs (e.g. `?page=2` press pagination) **not fetched**; the sitemap was used instead |
| community.sonarsource.com | `*` disallows `/admin/`, `/search`, `/t/*/*.rss`, `/c/*.rss`, etc. | Only `/categories.json`, `/c/announce/20/l/latest.json?page=N` and `/t/<id>.json` were used (not disallowed) |
| docs.sonarsource.com | `Allow: /` | not needed in the end |
| siliconangle.com | no disallow for `*` | fetched |
| www.straitstimes.com | article path not disallowed; no Claude-specific group | fetched |
| www.edb.gov.sg | `Allow: /` | fetched (context only) |
| www.startupticker.ch | no rules | fetched (syndicated copy) |
| devops.com | path allowed | **HTTP 403**, so inaccessible and not used |
| www.statesman.com | **disallows anthropic-ai, ClaudeBot, Claude-User, Claude-SearchBot** | **not fetched** |
| thenewstack.io | **disallows anthropic-ai, ClaudeBot, Claude-Web** | **not fetched** (7 TNS links on Sonar's coverage page unread) |
| www.jenkins.io | robots.txt 404 (no rules) | advisory fetched |
| nvd.nist.gov / services.nvd.nist.gov | API used | queries below |

## Query and source log by segment

| Date | Segment | Exact query or source request | Opened / decision | Found / screened / excluded |
|---|---|---|---|---|
| 2026-10-16 | all | `GET https://www.sonarsource.com/sitemap.xml` | 1,938 URLs. English `/company/` and `/blog/` URLs with `lastmod` ≥ 2026-04-01 were extracted (397). `lastmod` is **not** a publication date | 397 leads |
| 2026-10-16 | all | `GET /company/press-releases/` (page 1 only) plus 11 press-release URLs from the sitemap | 11 read raw. Dateline dates used | 10 in window; Daybreak (2026-10-13) excluded as post-window |
| 2026-10-16 | all | `GET` each of the 379 `/blog/` URLs; `datePublished` taken from JSON-LD | 95 have `datePublished` in window; 1 index page without a date. Out-of-window pages deleted after extraction | 95 / 26 read / see exclusions |
| 2026-10-16 | all | `GET /blog/rss.xml` and `/rss.xml` | only the last 20 items (2026-09-22…2026-10-14) | used as cross-check only |
| 2026-10-16 | all | `GET community.sonarsource.com/categories.json`; `/c/announce/20/l/latest.json?page=0..N` | 180 topics listed, 108 created in window, 19 opened via `/t/<id>.json` | weekly roundups, course/video and rule-pack posts not ledgered |
| 2026-10-16 | all | `gh api orgs/SonarSource/repos?sort=pushed&per_page=100` | new in-window repos: core-languages-tooling-public, gh-action_azure-artifact-signing, sonar-scanner-cargo, dbd-binaries, terraform-provider-sonarqube (alpha, 0 releases), sonar-linguist-java, terraform-provider-registry-test | only Cargo scanner ledgered |
| 2026-10-16 | all | `gh api repos/SonarSource/{sonarqube-mcp-server, sonarqube-cli, sonarqube-agent-plugins, sonarqube, terraform-provider-sonarqube, sonar-scanner-cargo, sonarlint-vscode, docker-sonarqube}/releases` | in-window counts: MCP 14, CLI 17, agent-plugins 1, sonarqube (Community Build) 6, Cargo 3, sonarlint-vscode 18, docker-sonarqube 18; release bodies read for CLI 0.9.0/1.0.0/1.10.0, MCP 1.16/1.20/1.24/1.28, plugins 2.0.0, Cargo 1.0.0, CB 26.5/26.10 | patch releases folded |
| 2026-10-16 | all | `gh api repos/SonarSource/<repo>/license` (mcp-server, cli, agent-plugins, sonar-java, sonar-python); `repos/SonarSource/sonar-migration-tool` | SSALv1 for MCP server, agent plugins and analyzers. CLI LICENSE text is LGPL-3.0 (API shows NOASSERTION). Migration tool has no licence | — |
| 2026-10-16 | all | `GET https://registry.npmjs.org/@sonar%2fscan` | 5.0.0 published 2026-07-20T08:56:59Z; LGPL-3.0-only | — |
| 2026-10-16 | all | NVD API `keywordSearch=sonarqube` for 2026-04-12..08-09 and 08-10..10-12; `keywordSearch=sonarsource` for 04-12..06-15 and 06-16..10-12; `cveId=CVE-2026-84665` | sonarqube: 0 + 2 (Flawfinder, unrelated; Jenkins SonarQube Scanner plugin, included). sonarsource: 0 + 0. A first sonarsource request with a 121-day range returned HTTP 404 and an empty body, so it was re-run with ≤120-day ranges | 2 / 2 / 1 |
| 2026-10-16 | all | `gh api advisories?...` (keyword filter unsupported) | not usable for Sonar-specific search; only a 2022 SonarQube advisory was returned for `sonar-plugin-api` | null |
| 2026-10-16 | all | HN Algolia `search_by_date` with `created_at_i>1775952000,created_at_i<1792022400`, tags=story: `sonarqube` (2 hits), `sonarsource` (3), `sonar gitar` (0), `sonar` (849, almost all unrelated), URL-restricted `sonarsource.com` (3) | Sonar-related: State of Code PDF (May 12, 2 pts), GPT-5.5 blind-spot blog (Apr 29, 1 pt), Cognitive Complexity PDF (Sep 29, 3 pts); two unrelated Show/Ask HN posts mention SonarQube | no critical or incident thread found |
| 2026-10-16 | all | `GET /company/coverage/` (Sonar's curated press list) | 60+ outbound links extracted; used for independent-source discovery (biased toward favourable coverage) | 6 attempted |
| 2026-10-16 | Apr 12–30 | blogs `byok-encryptions-sonarqube-cloud`, `now-available-sonarqube-plugin-for-claude-code`, `claude-arbitrary-code-execution`, `announcing-gitar-the-future-of-code-validation`; community 181112 | 3 blog rows + 1 community row. The Gitar seed-round post shows `datePublished` 2026-04-15 but its `<title>` reads "Gitar is joining Sonar" and it says Gitar is "emerging from stealth", which conflicts with Gitar posts dated 2024 on the same site. Likely a migration artifact, so **excluded** | — |
| 2026-10-16 | Apr 12–30 | model-evaluation posts (`openai-gpt-5-5-evaluation`, `claude-opus-4-7-evaluation`, `gpt-5-5-biggest-blind-spot`), `linting-ai-assisted-development`, `ai-first-engineering-cisco` | excluded (vendor benchmark commentary/opinion; not Sonar capability changes) | — |
| 2026-10-16 | May | press releases (Remediation Agent ATxSummit, Gitar acquisition, Gartner MQ, AWS award); blogs 2026-3, backlog remediation, architecture management, Gitar welcome/joining, Mini Shai-Hulud; community 182610, 182830; GitHub plugins 2.0.0 | Gartner MQ and AWS award excluded (analyst/partner recognition); "Remediation Agent wins best innovation" award blog excluded | — |
| 2026-10-16 | May | [SiliconANGLE 2026-05-21](https://siliconangle.com/2026/05/21/ai-code-quality-startup-sonar-buys-ai-code-review-startup-gitar/) (datePublished 2026-05-21T14:00Z, Mike Wheatley); [Straits Times 2026-05-21](https://www.straitstimes.com/tech/ai-debugging-tool-developed-tested-by-spore-engineers-rolled-out-to-tackle-rising-risks) (17:44 SGT); [EDB](https://www.edb.gov.sg/en/business-insights/insights/new-ai-debugging-tool-developed-in-singapore-aims-to-tackle-rising-risks.html) (datePublished "24 Jul 2026"; government design partner, so not independent). Statesman (Gitar) **not fetched** (robots). itdigest, aitoday, builtinaustin, tipranks, investorshangout and noah-news **not opened** (aggregators/low-value; E0) | 2 used as independent checks | — |
| 2026-10-16 | June | GitHub CLI 1.0.0, MCP 1.20.0; blogs Advanced Security Team, Codex, Cursor, introducing-sonar-vortex, Copilot CLI, Agent App; community 183664, 183960, 184019, 184062; press release Vortex/Remediation (Jun 30) and AI Engineer World's Fair (Jun 18, excluded as event notice) | 6 rows. `sonarqube-agent-app-in-github` (Jun 2) noted, not ledgered. Fable 5/model-cost posts excluded | — |
| 2026-10-16 | June | startupticker.ch (02.07.2026) | syndicated copy of the Jun 30 press release, **not independent**; not used as a check | — |
| 2026-10-16 | July | community 185016, 185820, 185257, 185876, 185102, 186120; blogs hunter-agent-beta, introducing-sonarqube-server-2026-4, migrating-to-sonarqube-cloud; press release Open Weights letter | 5 rows. The Open Weights letter (Jul 31) is a policy statement and was not ledgered. PySonar dropping Python 3.9 (Jul 8) and the Antigravity plugin (Jul 27) were noted only | — |
| 2026-10-16 | August | community 187471, 187617, 187747; blogs Open Secure AI Alliance, return-of-shai-hulud, your-secrets-are-leaking; press release Hunter GA; [SiliconANGLE 2026-08-27](https://siliconangle.com/2026/08/27/sonar-launches-hunter-agent-to-find-flaws-code-scanners-cant-see/) (Duncan Riley); DevOps.com Hunter article **HTTP 403** | 4 rows; Shai-Hulud research and Gitar ADO/Bitbucket GA noted only | — |
| 2026-10-16 | September | [Jenkins advisory 2026-09-02](https://www.jenkins.io/security/advisory/2026-09-02/) (SECURITY-3989); community 187941, 188084; GitHub Cargo 1.0.0; blogs four-new-languages, rust-support, sonar-extends-technical-debt-governance-to-r; press release 2026.5 LTA; blog 2026.5 LTA | 5 rows. Model-evaluation posts (GPT-6 Astra/Sol, Opus 5.5) and the OpenAI collective-action blog excluded | — |
| 2026-10-16 | Oct 1–12 | blogs Remediation Agent on Server (Oct 1), Vortex on Server (Oct 6); GitHub Community Build 26.10 (Oct 12); press release AI Engineer NY (Oct 8, excluded as event notice) | 3 rows | — |
| 2026-10-16 | post-window | press release and blog for OpenAI Daybreak (Oct 13), blogs on vulnerability reachability, new JS/TS engine, bulk import (Oct 13–14), CLI 1.10.0 (Oct 14), MCP 1.29.0 (Oct 13) | **excluded** as out of window | — |

## Inclusion, deduplication and conflicts

- **Included:** 35 rows, by segment: Apr 12–30: 4, May: 8, Jun: 6, Jul: 5, Aug: 4, Sep: 5, Oct 1–12: 3. Every row cites a URL that was fetched as raw text or queried by API.
  - GitHub release-page URLs in `source_url` were read through the equivalent `gh api repos/.../releases/tags/<tag>` endpoint.
  - No row relies on a search snippet alone.
- **Duplicate/lifecycle groups:**
  - `095-001`: CLI open beta → 1.0.
  - `095-009`: Remediation Agent launch (May 21), GA with Vortex (Jun 30), Server availability (Oct 1).
  - `095-012`: Hunter Agent alpha → open beta → GA.
  - SiliconANGLE and the Straits Times are listed as independent checks on the vendor rows. They are not separate events.
- **Date conflicts recorded, not resolved:**
  - Server 2026.3.0 Docker release 2026-05-19T07:54Z vs blog 2026-05-20.
  - Server 2026.5.0 Docker release 2026-09-25T17:56Z vs press release 2026-09-29.
  - CLI 1.0.0 GitHub release 2026-06-10 vs community GA post 2026-06-17.
  - Remediation Agent "global launch" 2026-05-21 vs "launch"/GA 2026-06-30.
  - Hunter beta: blog 2026-07-09 vs community post 2026-07-10.
  - Gitar seed post `datePublished` 2026-04-15 (see exclusions).
  - Copilot CLI plugin: community 2026-05-20 vs blog 2026-06-01.
- **Figure conflicts:** "75% of the Fortune 100" (Sonar) vs "75% of the Fortune 500" (SiliconANGLE, May 21).
- **Figures confirmed against raw page text (grep of saved text):**
  - Remediation Agent PR: "3.2% false positive rate", "750 billion lines", "seven million developers", "end of June".
  - Gitar PR: "44% less likely", "up to 8%", "up to 67%", "June 11, 2026".
  - Vortex PR: "36%", "$430 million", "more than 40%", "Claude Opus 4.8".
  - Vortex blog: "92%".
  - Hunter alpha post: "200 new security flaws".
  - Claude Code plugin blog: "over 450 secret patterns".
  - Backlog remediation blog: "up to five" fixes per PR.
  - Server 2026.3 blog: "70+" Python rules, "CycloneDX 1.6".
  - Server 2026.4 blog: "up to 90%".
  - R post: "82" rules. Rust blog: "122 curated Clippy rules".
  - Mini Shai-Hulud blog: "~323 packages".
  - Java brownout post: "1:00 PM GMT and 2:00 PM GMT", "July 20".
  - Open Secure AI Alliance blog: "over 600 OSS maintainers".
  - Jenkins advisory: "2.18.3", "2.19.0". NVD: CVSS 8.0.
  - All of these remain **vendor or third-party statements**, not verified measurements.
- **Release timestamps confirmed via API:**
  - CLI: 0.9.0.977 (2026-04-13T10:00:40Z), 0.13.0.1692 (2026-05-19T08:25:20Z), 1.0.0.2628 (2026-06-10T14:47:08Z).
  - MCP 1.20.0.2929: 2026-06-23T11:27:10Z.
  - Agent plugins 2.0.0: 2026-05-07T15:02:32Z.
  - Cargo 1.0.0-105: 2026-09-11T11:17:30Z.
  - Community Build 26.10.0.133078: 2026-10-12T10:01:25Z.
  - Docker images: 2026.3.0, 2026.4.0 (2026-07-22T15:45:43Z), 2026.5.0.
  - `@sonar/scan` 5.0.0: 2026-07-20T08:56:59Z.
  - Sonar Migration Tool v1.0.0.25: 2026-08-04T06:16:48Z.
- **Untrusted-content note:** fetched pages were treated as data. No page contained instructions directed at an AI agent or researcher.
  - The sonarsource.com robots.txt carries a `Content-Signal: ai-train=yes, search=yes, ai-input=yes` line. This is a site policy signal, not an instruction to the researcher.
  - Several Sonar blog posts describe agent hooks (e.g. `.claude/settings.json`) as product guidance or attack examples. None was executed.

## Missing, inaccessible or not attempted

- **Inaccessible or refused by robots.txt:**
  - DevOps.com Hunter article (HTTP 403).
  - The Statesman and The New Stack (robots.txt disallows Claude agents).
- **Not attempted:**
  - Gartner report.
  - Anthropic/OpenAI/GitHub-side pages for the plugins and partnerships.
  - Open Secure AI Alliance charter.
  - Gitar's own docs site (docs.gitar.ai).
  - SonarQube Cloud release notes on docs.sonarsource.com.
  - Pricing pages.
  - Sonar terms of service and data-retention terms for Cloud, Vortex and Gitar.
  - Archived (Wayback) copies.
  - Filing-level corporate and investor records. SEC/EDGAR was deliberately not contacted.
- **Not read:** 69 of the 95 in-window blog posts (most are model evaluations, explainers or opinion pieces) and 89 of the 108 in-window community announcements (mostly roundups, courses and rule packs).
- **No-finding segments:** No independent (non-vendor) reporting was found for April, June, July or October 1–12. No in-window CVE naming SonarQube Server or Cloud themselves was returned by the NVD keyword search.
- No product was executed, no account was created, no paywall was circumvented and no energy was measured.
- **Reproduction:** re-run the requests above with UTC timestamps and save raw HTML hashes. Before any row is promoted beyond provisional status, an independent human should spot-check at least:
  - the acquisition row (CI2026-095-010);
  - the incident/advisory rows (026, 028);
  - the Vortex/ARR row (018);
  - two GitHub release rows.
