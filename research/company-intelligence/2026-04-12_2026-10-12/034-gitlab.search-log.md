# GitLab (034) — provisional dated source-query and inclusion log, 2026-10-16

> **Provisional, AI-assisted first-pass screen, not human-reviewed.** This log, the [report](034-gitlab.md) and the [event ledger](034-gitlab.events.csv) are documentary source leads for [issue #101](https://github.com/MSKazemi/github-trending-1000-study/issues/101). Factual/link review, source-access/rights review and methods review are **pending**. Nothing here is scientific sign-off, and issue #101 was closed on 2026-10-16 by maintainer decision with this provisional status recorded; closure is not scientific validation, and the human review gates above remain open.

**Window:** 2026-04-12 to 2026-10-12 inclusive. **Screen date:** 2026-10-16 (`accessed_utc` for every ledger row). **Tools:** one general web-search provider (US results) plus direct page fetches of official GitLab pages, one SEC EDGAR exhibit and selected independent articles. **This is not exhaustive internet discovery.** Search-run UTC times, provider result totals and complete excluded-hit denominators were not captured. They are recorded as `unknown`, not zero. No page snapshots or byte hashes were archived.

## 1. Exact queries run (web search)

| # | Exact query string | Segment targeted | Useful results inspected | Decision |
|---|---|---|---|---|
| Q1 | `GitLab 19.0 release May 2026` | May | GitLab French blog on 19.0 breaking changes; docs `releases/upcoming`; forum 19.4 thread; Nagoya University 19.0.1 notice; endoflife.ai CVE analysis | Led to official release index. Third-party items used only as leads |
| Q2 | `GitLab 18.11 release April 2026 Duo Agent Platform` | Apr 12–30 | `docs.gitlab.com/releases/18/`; efficientlyconnected.com and hendryadrian.com recaps; Jan 2025 Duo beta press release (pre-window) | Official notes used. Recaps excluded as secondary syndication |
| Q3 | `GitLab press release 2026 first quarter fiscal 2027 financial results` | June | GitLab newsroom, Business Wire, q4cdn PDF, edgar.tools mirror, Seeking Alpha | GitLab newsroom page and q4cdn PDF used. Business Wire returned HTTP 403 |
| Q4 | `GitLab acquisition OR acquired OR CEO 2026 news` | entity | html.it (2024-07-18 sale-talks report), gigazine 2024, Techleap 2025 takeover rumour, GitLab press list | **No in-window acquisition found.** Older sale rumours are pre-window baseline only |
| Q5 | `GitLab critical patch release 2026 vulnerability BleepingComputer OR "The Register" OR SecurityWeek` | Aug–Oct | The Hacker News (Aug), Security Affairs, ThaiCERT, cert.ug, GitLab 19.0.9 patch page, hackmag, noted.lol, techjacksolutions PDF | Official patch pages and Security Affairs used. No BleepingComputer, Register or SecurityWeek hit was returned |
| Q6 | `GitLab Transcend June 2026 Orbit "Next Generation Source Code Management" agents` | June | GitLab press release and blog, DevOps.com, workingnotworking.com, letsdatascience, Adaptavist | Press release, GitLab blog and DevOps.com used. Others repeat vendor numbers |
| Q7 | `GitLab Duo CLI generally available July 2026 open source license` | July | GitLab blog (Jul 16), 19.2 release notes, Duo CLI docs | GA confirmed. **CLI licence not found and not verified** |
| Q8 | `GitLab news September 2026 OR August 2026 agentic Duo Agent Platform analysis` | Aug–Sep | Only Jan 2026 Duo Agent Platform GA coverage (IT Brief, dealroom, GitLab press) | No Aug–Sep independent analysis surfaced. Jan 15 2026 GA used as baseline only |
| Q9 | `theregister.com GitLab 2026` | cross-window | Only press releases and FY2026 items | No Register article surfaced. **Absence of results does not mean no coverage** |
| Q10 | `CISA Known Exploited Vulnerabilities CVE-2026-85706 GitLab` | September | eSecurity Planet, TechRadar, SOC Prime, Cybersecurity Dive, CSO Online, InfoWorld | Cybersecurity Dive read and used as the independent row. The others were seen as titles only |
| Q11 | `GitLab layoffs 14% 350 employees June 2026 exit 22 countries` | June | TNW, gigazine, itc.ua, 36kr, People Matters | TNW read and used as the independent check |
| Q12 | `"GitLab Reports Second Quarter Fiscal Year 2027 Financial Results" revenue million` | September | SEC EDGAR 8-K Exhibit 99.1, Business Wire, q4cdn PDFs, Pulse 2.0 | SEC exhibit read and used |

## 2. Direct official-source inspection (fetched 2026-10-16)

- **Release index:** [GitLab 19 release notes](https://docs.gitlab.com/releases/19/) and [GitLab 18 release notes](https://docs.gitlab.com/releases/18/). The index pages carry no dates, so dates come from each release page: [18.11](https://docs.gitlab.com/releases/18/gitlab-18-11-released/) Apr 16, [19.0](https://docs.gitlab.com/releases/19/gitlab-19-0-released/) May 21, [19.1](https://docs.gitlab.com/releases/19/gitlab-19-1-released/) Jun 18, [19.2](https://docs.gitlab.com/releases/19/gitlab-19-2-released/) Jul 16, [19.3](https://docs.gitlab.com/releases/19/gitlab-19-3-released/) Aug 20 and [19.4](https://docs.gitlab.com/releases/19/gitlab-19-4-released/) Sep 17. [19.5](https://docs.gitlab.com/releases/19/gitlab-19-5-released/) is dated **Oct 15** and is **excluded** as out of window. The 19.6 index entry has no content yet.
- **Newsroom:** the [press releases index](https://about.gitlab.com/press/releases/) lists 23 releases dated Apr 14 to Oct 6, 2026. Eleven were opened and read (see the ledger). The rest were screened by title only (see §4).
- **Patch releases:** the [patch-release RSS feed](https://docs.gitlab.com/releases/patch-releases.xml) is about 1.67M characters. Only the first ~300k characters were read (offsets 0, 100000 and 200000), which covered entries from Oct 12 back to Jun 10. **Patch releases from Apr 12 to early June were not enumerated.** We opened 5 critical patch pages: [19.2.4](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-2-4-released/), [19.3.2](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-3-2-released/), [19.0.9](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-0-9-released/), [AI Gateway 19.4.1](https://docs.gitlab.com/releases/patches/other-patches/patch-release-gitlab-ai-gateway-19-4-1-released/) and [19.4.2](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-4-2-released/). The Sep 23 critical patch [19.4.1/19.3.3/19.2.7](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-4-1-released/) was seen in the feed but **not opened**, so it has no ledger row.
- **Blog:** [19.0 breaking-changes guide](https://about.gitlab.com/blog/a-guide-to-the-breaking-changes-in-gitlab-19-0/), [Transcend announcements](https://about.gitlab.com/blog/gitlab-transcend-announcements) and [Duo CLI GA](https://about.gitlab.com/blog/gitlab-duo-cli-generally-available/). We saw the last one only in search results and did not fetch it.
- **Licence baseline:** the [gitlab-org/gitlab LICENSE](https://gitlab.com/gitlab-org/gitlab/-/raw/master/LICENSE) (current `master`, not a historical snapshot).
- **Regulatory filing:** the [Q2 FY2027 Form 8-K Exhibit 99.1](https://www.sec.gov/Archives/edgar/data/0001653482/000162828026059820/gitlab-ex99120260731fy27.htm). The [Q1 FY2027 earnings PDF](https://s204.q4cdn.com/984476563/files/doc_financials/2027/q1/GitLab-1QF2027-Earnings-Press-Release.pdf) could not be parsed by the fetch tool. Its text was extracted locally with `pdftotext` from the fetched copy.

## 3. Month-segment coverage

| Segment | Ledger rows | Coverage note |
|---|---|---|
| Apr 12–30 | 001–005 | Release, deprecation guide, three cloud/model partnership releases. Apr 22 partner award excluded as recognition, not capability |
| May | 006 | **Only one in-window capability record (19.0).** May IR notices (May 19, May 21) excluded as scheduling notices. May patch releases not enumerated. No independent May reporting screened |
| June | 007–012 | Earnings plus restructuring (independent TNW check), Transcend (DevOps.com), Google, 19.1, survey |
| July | 013–014 | 19.2 and commissioned TEI. Jul 8 and Jul 29 routine patch releases seen in feed, not opened |
| August | 015–016 | Critical patch (Security Affairs check) and 19.3 |
| September | 017–021 | 8-K, CVE-2026-85706 cluster (three rows, one `duplicate_event_group`), 19.4 |
| Oct 1–12 | 022–024 | AI Gateway critical patch, Oct 6 announcement, Oct 12 critical patch |

All seven segments have at least one dated record. **May is thin**, and that reflects limited search depth as much as vendor activity.

## 4. Screened and excluded

- **Out of window:** GitLab 19.5 (Oct 15, 2026; MCP server GA, Secrets Manager GA). Duo Agent Platform GA (press release dated Jan 15, 2026). The Q4 FY2026 release (March 2026). The 2024 sale-talk reports and the Oct 2025 takeover rumour. These are baseline context only.
- **Recognition, marketing or scheduling, excluded from the ledger:** Apr 22 Google Cloud partner award, May 19 and Aug 18 results-date notices, May 21 BofA conference notice, Jun 4 Transcend scheduling notice, Jun 17 Gartner Magic Quadrant placement. Analyst placement is not adoption evidence.
- **Executive appointments, excluded from the ledger and noted in the report §2:** Chaim Mazal as CISO (Jun 9) and Thomas Lloyd as Chief Business and Legal Officer (Jul 20). These are press-list titles only and were not opened.
- **Low-reliability third-party source:** [endoflife.ai (Sep 11)](https://endoflife.ai/article-gitlab-cve-2026-85706-six-lines-without-a-fix) claimed six release lines (including 19.0 and 18.11) had no fix for CVE-2026-85706. The article is internally inconsistent: it cites an Oct 12 patch while being dated Sep 11. GitLab's Sep 23 backport supersedes its 19.0 and 18.11 claim. It is kept only as the contrary-claim link on row 021.
- **Mirror domains excluded:** `awskws.duckdns.org` reproduces GitLab pages and is not an official channel. Syndicated recaps (efficientlyconnected.com, hendryadrian.com, workingnotworking.com, letsdatascience.com, 01net.it, chartmill) repeat vendor text and add no independent evidence.
- **Search-snippet-only dates not adopted:** one third-party briefing dated CVE-2026-97229's patch Oct 8. The official page and feed say Oct 12, and the ledger uses Oct 12.

## 5. Inaccessible sources

- `thehackernews.com/2026/08/critical-gitlab-graphql-flaw-could-let.html`: HTTP 403.
- `businesswire.com` Q1 FY2027 release: HTTP 403. The GitLab-hosted PDF and newsroom copy were used instead.
- The AI Gateway patch page shows **no date**. Its `published_utc` comes from the GitLab patch-release feed entry (2026-10-02).
- No paywalled, authenticated or account-only content was accessed. No GitLab account was used, and no software was installed or exercised.

## 6. Reproduction guidance for a human reviewer

Re-run Q1–Q12 with a recorded UTC time and result counts. Read the complete patch-release feed for Apr 12 to Jun 10. Open the unopened Sep 23 19.4.1 critical patch page. Check the Duo CLI and `ee/LICENSE` licence text. Look for independent reporting on Orbit, next-generation SCM, or MCP governance that goes beyond restating vendor numbers. Record any contradictions as new dated notes, and do not overwrite this log.
