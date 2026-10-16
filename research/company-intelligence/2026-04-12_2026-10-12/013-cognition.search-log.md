# Cognition (013): source query and inclusion log for the standardisation upgrade

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** This log accompanies the [report](013-cognition.md) and the [event ledger](013-cognition.events.csv) for [#79](https://github.com/MSKazemi/github-trending-1000-study/issues/79). Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

**Window:** 2026-04-12 to 2026-10-12 inclusive (UTC dates). **Accessed:** 2026-10-16. **Method:** robots.txt was checked on every host before any page was fetched. Pages were retrieved as raw HTML with `curl` using a generic `Mozilla/5.0` User-Agent. No personal identifier, email address or credential was sent to any site. Text was extracted locally, and every number, date, version and quote used in a ledger row was confirmed with a regex search of the saved text. `gh api` was used for GitHub metadata, the NVD CVE API for the CVE row, the Wayback Machine CDX API and `id_` captures for earlier page versions, and the Hacker News Algolia API for independent discovery. WebSearch was not used, because the session's search budget was exhausted. **This is not exhaustive retrieval.** Search-engine totals were not available and are recorded as unknown, not zero. No page snapshots or hashes are committed, and the pages may change after access.

## Robots.txt decisions

| Host | Decision |
|---|---|
| cognition.com (cognition.ai redirects here) | `User-Agent: *` allows everything except `/downloads/`. Fetched. |
| docs.devin.ai | Disallows only `/cdn-cgi/` and `/_next/`. Fetched the release notes, Desktop changelog and Outposts doc. |
| devin.ai | ClaudeBot is grouped with `*` and allowed except `/top-secret` and `/assets/downloads/`. Fetched two blog posts. |
| windsurf.com | Allows everything. `/changelog` redirects to `docs.devin.ai/desktop/changelog`. |
| techcrunch.com | **Disallows `anthropic-ai`, `ClaudeBot` and `Claude-Web` for `/`.** Not fetched. |
| bloomberg.com | **Disallows `Claude-User`, `ClaudeBot`, `Claude-SearchBot`, `Claude-Web` and `anthropic-ai` for `/`, allowing only `/professional` and `/company`.** News pages not fetched. |
| arxiv.org | `/abs` and `/html` allowed. Fetched. |
| dioxuslabs.com, catalins.tech, hn.algolia.com, services.nvd.nist.gov, web.archive.org | No applicable disallow, or no robots file (404). Fetched. |

## Query and source log by segment

| Date | Segment | Exact request | Decision | Found / opened / ledgered |
|---|---|---|---|---|
| 2026-10-16 | all | `GET https://cognition.com/sitemap.xml` | Lists 92 blog URLs. `lastmod` values are bulk re-index times, not publication dates, so they were not used as dates. | 92 / – / – |
| 2026-10-16 | all | `GET https://cognition.com/blog` (index) | Index dates (MM.DD.YY) agree with each post's JSON-LD `datePublished`. In-window posts run from 04.14.26 to 09.25.26. No Oct 1–12 post exists. | 39 in window / 39 opened / 21 rows |
| 2026-10-16 | all | `GET https://docs.devin.ai/release-notes/2026` | 71 dated entries from January 9 to October 14, 2026, with 52 in the window. All sub-headings were parsed. Selected entries were read in full. | 52 / 52 skimmed / 15 rows |
| 2026-10-16 | all | `GET https://windsurf.com/changelog` → `https://docs.devin.ai/desktop/changelog` | Versioned entries v2.0.44 (Apr 15) to v3.10.67 (Oct 12). | 35 in window / all skimmed / 5 rows (plus 4 rows cross-checked) |
| 2026-10-16 | all | `gh api orgs/CognitionAI/repos`, `repos/CognitionAI/terraform-provider-devin/releases`, `repos/CognitionAI/devin-outpost-k8s`, `repos/DioxusLabs/dioxus` | In-window repositories: terraform-provider-devin (Apache-2.0), devin-outpost-k8s (MIT), plugin-template and team-marketplace-template (MIT), devin-marketplace (MIT), devin-connect (Apache-2.0), devin-cli and actions (no licence detected). | 8 new repos / 1 row; the others are noted in report text |
| 2026-10-16 | all | HN Algolia `search_by_date` with `query=Cognition`, `Devin` and `Windsurf`, `tags=story`, `created_at_i` between 1775952000 and 1792022400, `hitsPerPage=200`, pages 0–3 | nbHits: Cognition 722, Devin 780, Windsurf 39. Most hits are unrelated (neuroscience "cognition", people named Devin, Windscribe). Relevant hits were screened by title and domain. | about 60 relevant / 10 opened / 4 E0 rows; also led to 3 independent rows (arXiv, Dioxus Labs, catalins.tech) |
| 2026-10-16 | Apr 12–30 | blog posts: plans, SWE-check, Devin in Windsurf, multi-agents, cloud agents, Devin CLI, Mercedes-Benz, Singapore; release notes Apr 15–29; Desktop v2.0.44–v2.1.32 | 7 rows (5 blog, 2 release notes). The multi-agents and cloud-agents essays were excluded as opinion or engineering background with no dated change. The Singapore office was excluded as a regional sales expansion outside the study angle. | 8 posts / 8 opened / 7 |
| 2026-10-16 | May | blog posts: HIL/SIL, Android emulator, Auto-Triage, Windows VMs, Series D, testing; release notes May 1–29; Desktop v2.2.17, v2.3.9, v2.3.15 | 5 rows. Android and Windows VM support were excluded as platform breadth with no reuse or rights implication. The HIL/SIL and testing posts were excluded as customer and engineering narrative. | – / – / 5 |
| 2026-10-16 | May | HN item for `colossus.com/article/scott-wu-tapes-cognition` (May 11) | Robots.txt allows the page, but it was not opened (an interview profile). Logged as an unopened lead. | 1 / 0 / 0 |
| 2026-10-16 | June | blog posts: Devin Desktop, AI guarantee, AI productivity, FrontierCode, Fusion; devin.ai rename post; release notes Jun 3–26; Desktop v3.0.12–v3.3.18 | 7 rows. | – / – / 7 |
| 2026-10-16 | July | blog posts: Security Swarm, Remediation Program, FrontierCode 1.1, model trustworthiness, SWE-1.7, FedRAMP, Fable vs Opus, One Year, TierZero, DOE Genesis MOU, Interaction, LTM; devin.ai Security Swarm eval; Outposts doc; arXiv 2607.21832 (abs and html) | 7 rows. The Remediation Program, Fable vs Opus, DOE MOU and LTM posts were excluded as services, pricing essay or government and partner announcements. FrontierCode 1.1 and TierZero were folded into other rows. "One Year" is used only for identity text. | – / – / 7 |
| 2026-10-16 | August | release notes Aug 5–28; Desktop v3.6.27–v3.8.20; HN items 49273255, 49366053, 49369004 | 6 rows, including 2 E0 title-only rows. Bloomberg and TechCrunch were **not read** because robots.txt disallows them. | – / – / 6 |
| 2026-10-16 | September | blog posts: Series E, RSA-260, SWE-2, Dioxus, Fusion local, AWS SCA, São Paulo, $1B run rate; dioxuslabs.com post; catalins.tech review; release notes Sep 2–30; Desktop v3.9.19–v3.10.48; NVD CVE-2026-81376; HN items 49530437, 49915596, 49913868 | 13 rows. RSA-260 was excluded as a research demonstration, São Paulo as a regional expansion, and local Fusion was folded into the Fusion rows. tokenstead.ai (SWE-2 benchmark listing) was not opened (aggregator). Two "open-source alternative to Devin" Show HN posts and the "cognition-claude-proxy" repo were excluded as third-party projects. | – / – / 13 |
| 2026-10-16 | Oct 1–12 | release notes Oct 2, 5, 7 and 9; Desktop v3.10.67 (Oct 12) | 3 rows. The Oct 14 release notes and the Oct 13 runtimewire article are **post-window** and excluded. | – / – / 3 |
| 2026-10-16 | cross-window | Wayback CDX `url=cognition.com/blog/devin-fusion`, `url=cognition.ai/blog/series-d`, `url=cognition.com/blog/series-d`; captures `20260630003605id_`, `20260715204100id_`, `20260527220950id_` | Confirmed that the Fusion page was revised and that the Series D page was edited without notice (see conflicts). | 3 captures read |

## Per-month row counts

Apr 7 · May 5 · Jun 7 · Jul 7 · Aug 6 · Sep 13 · Oct 1–12 3. **Total: 48.** E0 title-only rows: 4. No month had zero results.

## Deduplication, conflicts and corrections

- **Duplicate groups:**
  - `013-019` is one Fusion cost claim: the original 35% figure on Jun 29 and the in-place revision dated Aug 7.
  - `013-029` is one Cascade retirement: off by default for enterprise on Aug 7, removed on Sep 8.
  - `013-031` is one Series E round: reported talks at $40B (Aug 12) and about $1B at $47B (Sep 2), then the announcement of over $2B at $48B (Sep 8).
- **Undisclosed edit:** the 2026-05-27 Wayback capture of the Series D post says "the most used model in Windsurf" and "local agents in Windsurf". The live page reads "Devin Desktop" in both places. The edit is not flagged on the page. The domain also moved from cognition.ai to cognition.com between the Jun 13 and Jun 21 captures.
- **Disclosed revision:** the Fusion headline changed from "35% Lower Cost" (captures from Jun 30 and Jul 15) to "up to 60%". The page now says "We initially reported a 35% cost reduction at publication" and gives "data last updated 8/7/2026". The benchmark version also changed, from FrontierCode to FrontierCode 1.1 Extended.
- **Availability conflicts:** the SWE-2 blog (Sep 10) says "available starting today in Devin Desktop and CLI". The Sep 21 release notes call it a research preview on the web agent selector that enterprise admins must enable. Outposts were "disabled by default" at launch (Jul 22), while current docs, accessed after the window, say they are available on Pro, Max and Teams.
- **Date conflicts resolved by the primary source:** the existing report's September lead (secondary indexes said Sep 2 or Sep 3) is **Sep 2** on the primary page. Its October AGENTS.md lead (secondary index Oct 12; the earlier text also said Oct 9) is **Oct 9**. The Devin CLI is Apr 27 on the blog and Apr 29 in the Desktop changelog (v2.1.29); both dates are kept.
- **Upstream security lag:** NVD published CVE-2026-81376 (Visual Studio Code, CVSS 3.1 9.6) on 2026-09-08T18:20Z. Devin Desktop's changelog lists the fix in v3.10.31, dated 2026-09-16.
- **Independent study:** the arXiv paper reports 220,612 PRs from 489 repositories in one section and 539 unique repositories in another. Both figures are recorded and the discrepancy is not resolved.

## Figures confirmed against raw text

- **Pricing:** $20, $200, $80 and $500/month; the 2-week Review trial.
- **SWE-check:** delta F1 0.09 → 0.
- **Windsurf 2.0:** up to 50 USD of promotional usage.
- **Mercedes-Benz:** 200,000 lines; eight months → eight days; four-week pilot.
- **Series D:** $1B at $26B, $492M, >10x, 89%.
- **AI Productivity Guarantee:** up to $10M.
- **FrontierCode 1.1:** 75 of 1000+ criteria relaxed.
- **Fusion:** 35% (captures), 60% (live) and 39% (Sep 11).
- **Security Swarm:** 72%, 50 vulnerabilities, 14 languages.
- **SWE-1.7:** Kimi K2.7 base, 1000 TPS, 42.3%.
- **Series E:** $2B at $48B; $492M → almost $900M.
- **SWE-2:** 50.0%, within one point, 64% cheaper.
- **Revenue:** $1B run rate.
- **CVE-2026-81376:** CVSS 9.6, affected versions below 1.136.2.
- **arXiv study:** 43.0%, 84.3%, 73.5%, 63.9%, 59.6%; 220,612 PRs; 489 and 539 repositories.
- **Session resume window:** 30 → 14 days.
- **Terraform provider:** v0.1.0 to v0.3.0 release dates.

All of these are **vendor, preprint or press statements**, not measurements made for this study. Figures in E0 rows ($40B, $47B) come from Hacker News titles only.

## Untrusted-content note

All fetched pages were treated as data. The Devin blog CLI post contains an install command (`curl -fsSL https://cli.devin.ai/install.sh | bash`). It was recorded as evidence and **not executed**. No page contained instructions addressed to an AI agent.

## Missing, inaccessible or not attempted

- **Blocked by robots.txt for Claude agents:**
  - TechCrunch (including the May 29 Scott Wu article cited by the earlier report, the Aug 19 denial and the Sep 30 Factory allegation).
  - Bloomberg (the May 27, Aug 12, Aug 19, Sep 2 and Sep 25 articles).
- **Not attempted:**
  - Posts on X/Twitter.
  - The FedRAMP Marketplace listing.
  - AWS-side confirmation of the Strategic Collaboration Agreement.
  - OpenAI-side terms for "Sign in with ChatGPT".
  - Kimi K2.7 licence terms.
  - Cognition terms of service and data-retention terms for Memory.
  - The colossus.com interview.
  - SEC or other filing-level records (excluded by rule).
- **Not done:** no product was executed, no account was created and no energy was measured.
- **Reproduction:** re-run the requests above with UTC timestamps and save raw HTML hashes. An independent human should spot-check the Fusion revision (`013-019` and `013-030`), the CVE lag row (`013-040`), the arXiv row (`013-026`) and the four E0 rows before any evidence is promoted beyond provisional status.
