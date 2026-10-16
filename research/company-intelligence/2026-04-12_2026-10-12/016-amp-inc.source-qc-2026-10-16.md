# Amp Inc. (016) — source QC of existing ledger rows and new-row spot check (2026-10-16)

> **Provisional source-lead screen (upgraded 2026-10-16):** this QC note, the [report](016-amp-inc.md), the [event ledger](016-amp-inc.events.csv) and the [search log](016-amp-inc.search-log.md) are **provisional, AI-assisted documentary source leads**, unreviewed by a qualified human; factual/link, source-access/rights and methods review pending. Merging is not scientific or security sign-off; issue [#82](https://github.com/MSKazemi/github-trending-1000-study/issues/82) was closed on maintainer instruction (2026-10-16) with these review gates still open — reopen it if review finds a defect.

**Method:** every pre-existing ledger row's `source_url` was fetched once on 2026-10-16 (public HTTPS GET, generic browser User-Agent, no login, no personal identifier). For each page the HTTP status, the publisher-displayed date (Amp renders it in the page header and in the `/news` index data) and the article text were compared with the row's `published_utc`, `claim_summary` and `status`. This checks **what the publisher currently displays**, not historical page versions, rollout to real accounts, security or task value. No row was deleted and no `event_id` changed.

## A. Existing ledger rows (9 rows from PR #197 / PR #231)

| event_id | URL | Reachable? | Displayed date == published_utc? | Claim / status supported? | Action |
|---|---|---|---|---|---|
| CI2026-016-001 | https://ampcode.com/news/neo | yes (200) | yes — May 6, 2026 | yes — "Today we're starting to roll out the new Amp. Not all of it, not yet. But the first piece: a rebuilt Amp CLI"; remote control, compaction, Plugin API. `preview` fits staged rollout. Page carries later in-place updates (a 2026-05-27 passkey note; a September 2026 note that `ask_user_choice` became built-in) — page is mutable. | none (ok) |
| CI2026-016-004 | https://ampcode.com/news/drop-the-neo | yes (200) | yes — May 27, 2026 | yes — "Amp Neo is now available to everyone"; also states the `--take-me-back` pre-Neo flag was removed. | none (ok) |
| CI2026-016-002 | https://ampcode.com/news/agents-everywhere | yes (200) | yes — June 4, 2026 | yes — sidebar for web/mobile/CLI, "It's rolled out to everyone"; mentions durable execution and plugin API. | none (ok) |
| 016-E03 | https://ampcode.com/news/diffs | yes (200) | yes — June 16, 2026 | yes — review/stage diffs "on desktop or mobile" while a thread has an active environment; duplicate-block detection. | none (ok) |
| 016-E04 | https://ampcode.com/notes/putting-an-agent-in-an-orb | yes (200) | yes — July 02, 2026 (byline date) | broadly yes — the note is an engineering essay on agents verifying their own work on a headless remote machine ("orb"), written two days after the Jun 30 "Agents in Orbs" launch; it is not a design specification and contains no isolation/safety audit. `reported_undetermined` stays appropriate. | none (ok; nuance recorded here) |
| CI2026-016-003 | https://ampcode.com/news/agents-anywhere | yes (200) | yes — July 8, 2026 | yes — `amp.remoteThreadCreation.enabled` setting, headless runner `amp --no-tui`, "Directories don't have to be version controlled". | none (ok) |
| CI2026-016-005 | https://ampcode.com/news/multi-repo-projects | yes (200) | yes — August 27, 2026 | yes — "up to 20 additional repositories per project"; only primary `.agents/setup` runs automatically. | none (ok) |
| CI2026-016-006 | https://ampcode.com/news/intelligently-ordered-diffs | yes (200) | yes — September 1, 2026 | yes — toggle between alphabetical and "intelligent" order; tests/fixtures/generated code muted. | none (ok) |
| CI2026-016-007 | https://ampcode.com/news/github-listeners | yes (200) | yes — October 12, 2026 | yes — PR comments, reviews and CI for latest commit; "first-class support for GitHub Webhooks"; per-issue/PR orbs via Amp GitHub App. | none (ok) |

**Outcome:** 9/9 reachable, 9/9 dates match, 9/9 claims supported; **0 corrections**, 0 unreachable. No `status`, `limitation` or `confidence` value was changed.

**Non-ledger URLs cited by the earlier report / QA files (checked for preservation, not ledger rows):** [Amp news index](https://ampcode.com/news) and [chronicle](https://ampcode.com/chronicle) return the same "Chronicle" index (200). The 2025-12-02 identity sources ([Sourcegraph blog](https://sourcegraph.com/blog/why-sourcegraph-and-amp-are-becoming-independent-companies), [Amp Frontier Corporation](https://ampcode.com/news/amp-frontier-corporation)) are out-of-window baseline; the 2026-10-15 URL clarification about `sourcegraphdev.com` (see [QA file](source-audits/016-amp-inc.2026-10-14-qa.md)) still stands.

## B. Spot-check of new rows added 2026-10-16

All 18 new rows were written only after their page was opened on 2026-10-16. The following re-read confirms the recorded date and the load-bearing wording (8 of 18 rows, >= 5 required):

| event_id | URL | Reachable? | Displayed date == published_utc? | Load-bearing wording found on page | Result |
|---|---|---|---|---|---|
| CI2026-016-008 | https://ampcode.com/news/opus-4.7 | yes (200) | yes — April 25, 2026 | "Opus 4.7 now powers Amp's smart mode"; internal evals "~72%, up from Opus 4.6's ~65%" | ok |
| CI2026-016-009 | https://ampcode.com/news/npm-package-changes | yes (200) | yes — May 14, 2026 | "The Amp CLI is now @ampcode/cli (was @sourcegraph/amp)"; aliases "will be removed on June 15, 2026" | ok |
| CI2026-016-012 | https://ampcode.com/news/end-of-public-threads | yes (200) | yes — June 2, 2026 | "removed public, internet-wide, discoverable thread sharing"; "isn't prompted by any incident" | ok |
| CI2026-016-013 | https://ampcode.com/news/agents-in-orbs | yes (200) | yes — June 30, 2026 | "Orbs are machines where agents can run without supervision"; "billed by the minute" | ok |
| CI2026-016-015 | https://ampcode.com/news/secrets-of-the-orb | yes (200) | yes — July 14, 2026 | "Orbs can now prove their identity using OIDC … without having to inject any secrets" | ok |
| CI2026-016-019 | https://ampcode.com/notes/thats-not-soc-2-compliant | yes (200) | yes — August 13, 2026 (byline) | "when we started working toward SOC 2"; "code review isn't on the list"; "We're 20 people" | ok — status kept `reported_undetermined` because attestation is not stated as achieved |
| CI2026-016-022 | https://ampcode.com/news/free-agent | yes (200) | yes — September 13, 2026 | "free to use when you bring your own compute and model subscriptions/keys"; zero/minimal data-retention extended to all users; "Update (September 30, 2026)" | ok — page edited in place after publication |
| CI2026-016-025 | https://www.westpac.com.au/about-westpac/media/media-releases/2026/7-august/ | yes (read via fetch tool) | yes — 7 August 2026 | "Westpac and Amp Frontier to partner on AI engineering"; Amp Labs as "a special purpose company" | ok — same partnership as CI2026-016-018 (Amp post Jul 29); not double-counted as a separate event |

## C. Integrity notes

- **Mutable pages:** several Amp posts carry in-place updates after publication (Neo: 2026-05-27 and September notes; Proof of Human: 2026-06-25; Free Agent: 2026-09-30; Amp Labs: later Westpac link). `published_utc` uses the original displayed date; updates are noted in `limitation`/`availability`, never used to re-date a row.
- **Leftover authoring placeholder:** the 2026-10-10 "Use Your Claude Plan in Amp" page contained an unrendered authoring note ("Add the tag here once the asset is uploaded") on 2026-10-16 — a sign of later editing; recorded in CI2026-016-024's limitation.
- **Entity naming discrepancy:** Sourcegraph's 2025-12-02 post says the founders "are founding Amp Inc."; Amp's own post of the same day is titled "Amp Frontier Corporation"; Westpac's 2026-08-07 release names "Amp Frontier Corporation (Amp)". The legal entity name was **not** verified against a registry. The ledger keeps `company_label` "Amp Inc." (watchlist label) and records the alias.
- **No agent-directed instructions** were found in any page or search result read for this pass.
- **Low-quality sources excluded:** aggregator/comparison pages returned by search (e.g. tech-insider.org, secondtalent.com, baeseokjae.github.io, theaiagentindex.com) were not opened as evidence; their unsourced pricing, adoption ("40,000 teams") and model-routing claims are not used.
