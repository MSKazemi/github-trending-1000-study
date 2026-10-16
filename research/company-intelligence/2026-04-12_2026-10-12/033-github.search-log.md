# GitHub (033): source-query and inclusion log (standardisation upgrade)

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED (screened 2026-10-16).** Companion to the [report](033-github.md) and [event ledger](033-github.events.csv) for [#100](https://github.com/MSKazemi/github-trending-1000-study/issues/100). Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.

**Window:** 2026-04-12 to 2026-10-12 inclusive (UTC dates). **Accessed:** 2026-10-16. **Scope:** the issue's study angle: OSS discovery and star/Trending-relevant data, contributor and review workflows, Copilot agents and their APIs/SDKs, GitHub Actions and supply-chain security (npm, Dependabot, Advisory Database), licensing, platform reliability, and product retirements. Out of scope: model-availability notices (several per week), Enterprise Server/billing administration minutiae, Visual Studio/JetBrains/Eclipse monthly roll-ups, marketing and beginner tutorials. Microsoft-wide items (VS Code, Agent Framework, Foundry) belong to watchlist 004.

**Method:** robots.txt checked for every host before fetching. github.blog content came through its WordPress REST API (`/wp-json/wp/v2/changelogs` and `/posts`, which robots.txt permits: `User-agent: *` with an empty `Disallow`) and raw page HTML, with a generic `Mozilla/5.0` User-Agent and 1.5 s between requests. No email address, name, account handle or credential was sent to any third-party site. GitHub data came from the authenticated `gh` CLI (local version 2.45.0, which predates the CLI telemetry introduced in v2.91.0) against api.github.com. No page on github.com itself was fetched. Every number, version, date and quote in a ledger row was checked against raw text or an API response; the exceptions are listed under "Not confirmed". SEC/EDGAR was not contacted. No WebSearch was used (session budget). Search-engine result totals are therefore unknown, not zero. No page snapshots are archived in the repository.

## Earlier branch carried forward

`origin/research/company-intel-2026-033-github` (commits `1e7a612` 2026-10-12, `bcfc529` and `e7d40b3` 2026-10-14) was read. `git diff origin/main...origin/research/company-intel-2026-033-github` is **empty**: its tip `e7d40b3` is already an ancestor of main, so all three commits only touched `033-github.md` and are already in the report. It holds **no unique sources** beyond the report; its ten G033 rows and the original Copilot-app lead were re-verified and carried into the ledger (see the report's crosswalk). That branch was not modified.

## Query and source log

| Date | Segment | Exact request | Opened / decision | Found / used |
|---|---|---|---|---|
| 2026-10-16 | all | robots.txt for github.blog, github.com, docs.github.com, www.githubstatus.com, desktop.github.com, resources.github.com, githubnext.com, hn.algolia.com, cli.github.com, www.wiz.io, mitchellh.com, www.theregister.com, www.bleepingcomputer.com, noma.security, awesomeagents.ai, orchidfiles.com, www.tomshardware.com, archestra.ai | github.blog, docs.github.com, wiz.io, noma.security, awesomeagents.ai (explicitly allows ClaudeBot and Claude-User), orchidfiles.com (article paths), tomshardware.com (article paths, no Claude rule) and archestra.ai allow the paths used. githubstatus.com disallows only `/api/` and `/embed/`. desktop.github.com, resources.github.com, githubnext.com, hn.algolia.com and mitchellh.com return 404 (no rules). github.com has a group for ClaudeBot/anthropic-ai with many disallows (e.g. `/*/*/stargazers`, `/copilot/`), so no github.com page was fetched and the API was used instead. theregister.com disallows `*` and ClaudeBot but **explicitly allows `Claude-User`**: two articles were fetched identifying truthfully as `Claude-User`. bleepingcomputer.com serves a Cloudflare challenge even for robots.txt, so it was not fetched | — |
| 2026-10-16 | all | `GET https://github.blog/wp-json/wp/v2/changelogs?after=2026-04-12T00:00:00&before=2026-10-13T00:00:00&per_page=100&page=1..6` | **509 changelog entries** (X-WP-Total). Count by UTC month of `date_gmt`: Apr 45, May 68, Jun 107, Jul 92, Aug 70, Sep 87, Oct 40. All titles screened by hand against the scope above. Edge check `after=2026-04-09`/`before=2026-04-13` and `after=2026-10-12`/`before=2026-10-14`: nothing on 2026-04-11/12; entries dated 2026-10-13 (e.g. secret scanning blocking Anthropic keys by default, GitHub App least-privilege improvements) **excluded** as out of window | 46 changelog pages opened (raw HTML); 45 ledger rows |
| 2026-10-16 | all | `GET https://github.blog/wp-json/wp/v2/posts?after=…&before=…` (2 pages) | **126 blog posts** in the window; titles screened; 14 opened through `/wp-json/wp/v2/posts/<id>` (content, `date_gmt`, `modified_gmt`) | 10 rows; 2 used as companion evidence (PR-limits post, supply-chain post); 2 not used (Universe announcement, agent-scale Git infrastructure post) |
| 2026-10-16 | all | Date handling | Changelog URL slugs carry the US-Pacific publication date. 23 of 509 entries have a slug date one day earlier than `date_gmt`. The ledger uses the UTC date; two affected rows (005, 058) note the slug date | — |
| 2026-10-16 | Apr 12–30 | changelog: third-party agent model selection; individual-plan changes; CLI telemetry; Copilot Business signup pause; Python dependency graphs; code review Actions minutes. Posts: usage-based billing, availability update, git push RCE | all included | 9 rows |
| 2026-10-16 | Apr 12–30 | `gh api repos/cli/cli/releases/tags/v2.91.0` | published 2026-04-22T10:40:12Z | used in row 004 |
| 2026-10-16 | Apr 12–30 | HN Algolia `query=GitHub`, stories, window, points>300 (271 hits; ~200 listed) | independent leads opened: Wiz CVE-2026-3854 breakdown, "Ghostty Is Leaving GitHub", "Inside GitHub's Fake Star Economy" (awesomeagents.ai, dated 2026-04-13), The Register on Hashimoto (Claude-User). Not opened: "GitHub Stacked PRs" (2026-04-13, github.github.com/gh-stack: a GitHub Pages site, not checked), "HERMES.md…" and other non-GitHub items | 3 rows |
| 2026-10-16 | May | changelog: MCP secret scanning GA; Agent tasks REST API; Copilot app technical preview; Copilot for Eclipse open source; npm staged publishing. Post: investigation update (breach) | all included | 6 rows |
| 2026-10-16 | May | `gh api repos/microsoft/copilot-for-eclipse` + releases | created 2026-03-16, MIT, first release 0.1.0 on 2026-04-22, 27 releases in window | row 017 |
| 2026-10-16 | May | HN: "GitHub confirms breach of 3,800 repos via malicious VSCode extension" (bleepingcomputer.com, 2026-05-20, 1054 points); "GitHub is investigating unauthorized access…" (x.com) | **not fetched** (Cloudflare challenge; x.com not attempted). GitHub's own post used | — |
| 2026-10-16 | May | Tom's Hardware ban of researcher "Nightmare-Eclipse" (2026-05-27) | read raw; included as reported_undetermined | 1 row |
| 2026-10-16 | June | changelog: billing live; SDK GA; sandboxes preview; agent apps; Agentic Workflows; Models closed to new customers; Copilot app GA; PR limits; release-notes credit; author-search change; pull_request_target defaults; Desktop 3.6; stargazer restrictions; licence compliance. Posts: Copilot app (Build), Advisory Database volume | all included | 16 rows |
| 2026-10-16 | June | `gh api repos/github/copilot-sdk` releases | MIT; 141 releases in window; v1.0.0 2026-06-02T15:00:59Z (rust/ and java/ v1.0.0 the same hour) | row 022 |
| 2026-10-16 | June | `gh api repos/github/gh-aw` releases | MIT; 141 releases in window (v0.68.2 to v0.91.9), 25 not flagged prerelease | row 025 |
| 2026-10-16 | June | `gh api repos/desktop/desktop` releases | release-3.6.0 2026-06-24T09:33:36Z (3.6.1–3.6.6 follow) | row 033 |
| 2026-10-16 | June | `gh api -i repos/torvalds/linux/stargazers?per_page=1`; `repos/cli/cli/stargazers?per_page=1` (authenticated, non-collaborator) | both **HTTP 404 Not Found** with documentation_url `…#list-stargazers`; `repos/torvalds/linux` still reports `stargazers_count` | row 035 (observation, not a dated event) |
| 2026-10-16 | June | `gh api advisories?type=reviewed&published=<month>&per_page=100 --paginate` for Mar–Jun 2026 | 1,640 / 1,584 / 1,705 / 1,607 reviewed advisories by the API's `published` field, against the blog's "1,560 reviewed advisories" for May "the highest in its history". The two metrics are likely defined differently (source publication date vs GitHub review date); **conflict recorded, not resolved** | row 034 |
| 2026-10-16 | June | Orchid Files "I discovered a large-scale malware distribution campaign on GitHub" (2026-06-18, via HN 987 points) | read raw; included | 1 row |
| 2026-10-16 | July | changelog: Models retirement date; Copilot app for all plans; Dependabot cooldown; Code Quality GA; Actions malicious-workflow hold; stacked PRs preview; Models retired. Posts: $100M Sponsors; supply-chain disruption (companion) | all included | 8 rows |
| 2026-10-16 | July | Noma Security "GitLost…" (via HN 2026-07-08) | read raw; page shows "Jul 6, 2026"; no time zone, so the UTC date is assumed; sitemap lastmod 2026-10-01 (later edit) | 1 row |
| 2026-10-16 | July | How-To Geek "Why developers are ditching GitHub for Codeberg…" (HN 2026-07-09) | not opened (robots not checked; opinion piece; Ghostty row already covers the migration signal) | — |
| 2026-10-16 | August | changelog: Spark deprecation; Agent Plugins 1.0; Classroom decommissioned; policies and billing changes. Post: August 17 outage | all included | 5 rows |
| 2026-10-16 | August | `gh api repos/agentplugins/agent-plugins-spec` | created 2026-04-03, licence NOASSERTION, no releases | row 047 |
| 2026-10-16 | August | Wiz "Red Agent … Snowflake … GitHub Copilot-Assisted PR" (2026-08-17) | read raw; the author's 1957 UTC update weakens the Copilot attribution; included with that correction | 1 row |
| 2026-10-16 | August | `GET https://www.githubstatus.com/incidents/zkxwbgr0cnmx` | 200, but incident update text is rendered client-side and was not extractable. The outage duration comes from the GitHub blog only | — |
| 2026-10-16 | August | HN "Cursor launches Origin, GitHub alternative" (2026-08-17) | not opened: a competitor announcement (watchlist 012), not GitHub evidence | — |
| 2026-10-16 | September | changelog: code review approvals; star-history endpoint; code review experience; Node 20 removal; default-enablement policy. Post: Rust port | all included | 6 rows |
| 2026-10-16 | September | `GET https://docs.github.com/en/rest/activity/starring?apiVersion=2022-11-28`; `gh api -H 'X-GitHub-Api-Version: 2026-03-10' repos/cli/cli/stargazers/history?per_page=2` and `…/stargazers/count` | docs describe "Get repository star history" and "Get stargazer count"; history returned weekly `total` + `days` arrays; count returned `{"count":46661}` on 2026-10-16 | row 053 |
| 2026-10-16 | September | The Register "Microsoft agentically ports Copilot runtime to Rust for $120K" (2026-09-18; routed here from watchlist 004's log) | read raw as `Claude-User`; included as derivative independent coverage | 1 row |
| 2026-10-16 | Oct 1–12 | changelog: stacked PRs GA; local sandboxing GA; code review billing controls; push attribution. Post: ReviewBench | all included | 5 rows |
| 2026-10-16 | cross-window | HN `query=Copilot Rust` (2 hits), `query=Copilot` points>250 (11 hits) | Copilot hits outside GitHub scope (Windows Copilot, M365 Cowork, Copilot for Word) not used; VS Code co-author trailer belongs to 004 | — |

## Inspected and excluded (selection)

- **Model availability / deprecation notices** (for example Claude Opus 4.7–5.5, GPT-5.5–6.1, Gemini 3.5–3.8 Flash, Kimi, Grok, MAI-Code): 44 entries matched a title regex for model availability/deprecation. They are high-frequency catalogue churn, and the ledger records the billing and policy frame instead. Their number is itself a maintenance signal (M7) but is not counted here.
- **Monthly IDE roll-ups** (VS Code, Visual Studio, JetBrains, Eclipse), **weekly Copilot release digests** (9, from 2026-08-07), **usage-metrics and usage-report additions** (24 by title regex) and **enterprise billing/cost-centre controls**: excluded as administrative, except where they change review or billing for code review (rows 008, 062).
- **GitHub Universe 2026 announcement** (2026-06-04): opened; it gives no event dates or product commitments, so it was excluded.
- **Monthly availability reports** (April–August): titles screened, not opened. The two reliability posts in the ledger cover the window's major incidents.
- **SHA-1 in HTTPS sunset** (2026-09-15) and **CodeQL releases** (2.25.2–2.27.2): out of the study angle.

## Inaccessible or not used

- bleepingcomputer.com: Cloudflare challenge, not fetched (breach report of 2026-05-20).
- x.com / twitter.com status posts: not attempted.
- github.com HTML pages (including stacked-PR and Copilot pages): not fetched. The API and github.blog were used instead.
- githubstatus.com incident detail: fetched, but the update text was not extractable (client-side rendering).
- CMU ICSE 2026 fake-star paper: cited only through the awesomeagents.ai report, not opened.

## Not confirmed against raw text

- Row 001: the CMU study figures (6 million stars, 18,617 repositories, 78 Trending repositories) are as reported by the secondary outlet; the paper itself was not read.
- Row 038: the GitLost publication date is the page's displayed "Jul 6, 2026" without a time zone.
- Row 035: the date the stargazer restriction took effect is unknown. Only the 2026-10-16 state was observed.

## Empty or thin segments

No segment was empty. Per segment (UTC `published_utc`): Apr 12–30 **12**, May **7**, Jun **17**, Jul **9**, Aug **6**, Sep **7**, Oct 1–12 **5**. Counts reflect selection from 509 changelog entries and 126 posts, not GitHub's level of activity (June had 107 changelog entries).

## Embedded instructions and untrusted content

- The breach post (row 016) and the git-push RCE post (row 011) contain shell commands for GHES administrators (`curl … rotate-gpg.sh`, `ghe-cluster-each …`). None were run.
- The Rust-port post (row 054) quotes prompts its author gave to agents ("Squash into a single commit, then rebase … force push", "do not spawn a subagent"). These are quoted article content aimed at the author's agents, not instructions to this screen, and were treated as data.
- The CLI telemetry notice (row 004) and docs pages contain setup commands (`gh config set telemetry …`, `curl -H "Authorization: Bearer <YOUR-TOKEN>" …`). None were run beyond the read-only `gh api` calls listed above.
- No page contained instructions addressed to AI agents that were acted on.
