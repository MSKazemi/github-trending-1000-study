# Cline (023) — source QC of existing ledger rows and spot-check of new rows (2026-10-16)

> **Provisional source-lead screen (upgraded 2026-10-16):** this QC note, the [report](023-cline.md), [event ledger](023-cline.events.csv) and [search log](023-cline.search-log.md) are **provisional, AI-assisted documentary source leads**, unreviewed by a qualified human; factual/link, source-access/rights and methods review pending. Merging is not scientific or security sign-off; issue #90 was closed on maintainer instruction (2026-10-16) with these review gates still open — reopen it if review finds a defect.

**Method:** each existing `source_url` was opened read-only on 2026-10-16 (WebFetch, public pages, no login). "Date matches" compares the page's displayed publication date with `published_utc`. "Claim supported" checks `claim_summary` and `status` against the page text. No row was deleted and no `event_id` changed. This is an AI desk check, **not** an independent human factual review; pages are mutable and no byte-level snapshot was taken.

## A. Existing rows (4 rows present on `main` before this upgrade)

| event_id | URL | Reachable? | Date matches? | Claim supported? | Action |
|---|---|---|---|---|---|
| CI2026-023-001 | https://cline.bot/blog/introducing-cline-sdk-the-upgraded-agent-runtime | yes | yes — page displays May 13, 2026 (sitemap `lastmod` 2026-05-14 is an edit timestamp, not publication) | yes — page announces open-sourcing the core harness as `@cline/sdk`; says CLI and kanban already run on it and "We are in the process of migrating our VS Code and Jetbrains extensions." `shipped` is supported for the SDK/CLI only, not for the IDE extensions | none to status; **limitation clarified** (IDE migration pending at publication; page itself names no licence — Apache-2.0 comes from the GitHub repo metadata) |
| CI2026-023-003 | https://cline.bot/blog/extend-cline-with-plugins-and-hooks | yes | yes — page displays June 15, 2026 (sitemap `lastmod` 2026-07-29 indicates a later edit) | yes — plugins wrap tools/providers/hooks; hooks fire before/after run, tool and model calls; only a regex deny-list guard example is shown. `reported_undetermined` kept: the post asserts cross-surface reuse but the extension only exposed plugins from v4.0.0 (2026-06-26), rolled back two days later (see CI2026-023-009/010) | **limitation clarified** (later-edit lastmod; extension availability depended on the SDK rollout) |
| CI2026-023-002 | https://cline.bot/blog/recursive-self-improvement-for-coding-agents | yes | yes — July 24, 2026 | yes — Terminal-Bench 2.1 with Kimi K3, 79/89 = 88.8% confirmation run costing $49.8, baseline 77.5%; authors disclose two invalidated reruns, human babysitting and human PR review | none (status `reported_undetermined` correct) |
| CI2026-023-004 | https://cline.ghost.io/cline-desktop-an-open-source-app-for-open-weight-models/ | yes (Ghost host; same article is listed on cline.bot as `/blog/cline-desktop-an-open-source-app-for-open-weight-models`) | yes — 14 Sep 2026 | yes — early desktop app, "Mac and Windows (beta)", Mac app stated fully open source, parallel agents; quoted Terminal-Bench figures are CLI-harness results, not a Desktop evaluation | **limitation clarified**: GitHub release `desktop-v0.0.2` (2026-07-22) was already the "First public release of Cline Code for macOS", so Sep 14 is a publicity/Windows-beta date, not first availability — recorded as a NEW row CI2026-023-011, not by editing this row's dates |

**Outcome for existing rows:** 4/4 reachable, 4/4 displayed dates match, 4/4 claims supported; 0 `corrected`, 0 `unavailable/unknown`. Three rows received clarified `limitation` text only (001, 003, 004). Other columns untouched.

**Earlier-report URLs without a ledger row (also checked):** `https://cline.bot/blog` (blog index; reachable, lists Sep 14 Desktop post — it is an index, not the Desktop article itself, so the archived first screen's Desktop link pointed at an index page) and `https://cline.bot/` (homepage, reachable; undated, not event evidence).

## B. Spot-check of new rows

Re-opened after the 19 new rows were written (read-only `gh api repos/cline/cline/releases/tags/<tag>`, `gh api /advisories/<GHSA>` and WebFetch of the blog page), 2026-10-16:

| event_id | URL | Reachable? | Date matches? | Claim supported? | Note |
|---|---|---|---|---|---|
| CI2026-023-010 | https://github.com/cline/cline/releases/tag/v4.0.1 | yes | yes — `published_at` 2026-06-28T02:48:38Z | yes — "Roll the stable VS Code extension back to the pre-SDK-migration codebase to resolve regressions reported in 4.0.0" | `reversed/cancelled` appropriate |
| CI2026-023-011 | https://github.com/cline/cline/releases/tag/desktop-v0.0.2 | yes | yes — 2026-07-22T00:08:44Z | yes — "First public release of Cline Code for macOS" | conflicts with a secondary aggregator naming v0.0.4; GitHub record kept |
| CI2026-023-014 | https://github.com/cline/cline/releases/tag/v4.1.0 | yes | yes — 2026-07-31T04:00:52Z | yes — staged rollout "starting at 1%" with legacy fallback | ok |
| CI2026-023-020 | https://github.com/cline/cline/releases/tag/v4.1.19 | yes | yes — 2026-09-17T07:51:57Z | yes — body contains `NoDefaultCurrentDirectoryInExePath` fix for planted `rg.exe`/`git.exe`/`powershell.exe` | no GHSA in repo advisory list |
| CI2026-023-012 | https://github.com/cline/cline/security/advisories/GHSA-3cj3-hqcr-g934 | yes (via `gh api`) | yes — repo advisory `published_at` 2026-06-23T18:59:04Z | yes — Origin unchecked on `/browser`, auto-approve default | **discrepancy kept, not resolved:** repo advisory says vulnerable `<= 3.0.24`; GitHub global record (reviewed 2026-09-24, NVD-published 2026-07-08) says `< 3.0.30`, first patched 3.0.30 |
| CI2026-023-007 | https://github.com/cline/cline/security/advisories/GHSA-5c57-rqjx-35g2 | yes | yes — 2026-05-08 (GitLab advisory DB also May 8, updated Jun 9; NVD publication 2026-06-01 per GitHub global record) | yes — critical, CVSS 9.6, `<= 2.13.0`, no fixed version listed | `reported_undetermined` because no patch is named |
| CI2026-023-019 | https://cline.bot/blog/how-we-migrated-11-million-users-to-clines-biggest-harness-upgrade | yes | yes — displayed September 2, 2026 | yes — "As of August 23, the rollout is at 100%"; first attempt rolled back | `event_date_utc` 2026-08-23 is the vendor-stated rollout date, not independently observed |

**Spot-check outcome:** 7/7 reachable, dates match, claims supported. Two recorded unresolved discrepancies (Hub advisory version range; first public Desktop version). Nothing was marked `corrected` in error; `corrected` on CI2026-023-012/020 means a vendor-disclosed fix, not an independently tested remediation.

## C. Not verified / unavailable

- `nvd.nist.gov/vuln/detail/CVE-2026-44211` and `…/CVE-2026-59723` returned only a JavaScript shell ("NVD - Home") to the fetch tool; NVD dates above come from GitHub's global advisory record (`nvd_published_at`), not from NVD directly.
- The eval ledger site named in CI2026-023-016 was not opened.
- No page snapshots/hashes were taken; all pages are mutable.
- Data seen while browsing contained no instructions aimed at AI agents.
