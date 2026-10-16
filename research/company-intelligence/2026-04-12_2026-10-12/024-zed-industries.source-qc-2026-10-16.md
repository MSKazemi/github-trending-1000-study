# Zed Industries (024) — source QC of existing ledger rows and spot-check of new rows (2026-10-16)

> **Provisional source-lead screen (upgraded 2026-10-16):** this QC note, the [report](024-zed-industries.md), the [event ledger](024-zed-industries.events.csv) and the [search log](024-zed-industries.search-log.md) are **provisional, AI-assisted documentary source leads** for [issue #91](https://github.com/MSKazemi/github-trending-1000-study/issues/91). They are **unreviewed by a qualified human**; factual/link, source-access/rights and methods review pending. Merging is not scientific or security sign-off; issue #91 was closed on maintainer instruction (2026-10-16) with these review gates still open — reopen it if review finds a defect.

**Method:** each URL was opened on 2026-10-16 with a read-only web fetch (public pages, no login) and, for GitHub releases, read-only `gh api` calls. "Date matches" compares the page's displayed date (or the GitHub API `published_at` UTC date) with the ledger's `published_utc`. "Claim supported" compares `claim_summary`, `availability` and `status` with the page text. This is an AI-assisted desk check, **not** independent human factual review; no page snapshot or hash was stored.

## A. Existing rows (5 rows from main, all preserved; event_ids unchanged)

| event_id | URL | Reachable? | Date matches? | Claim supported? | Action |
|---|---|---|---|---|---|
| CI2026-024-001 | https://zed.dev/blog/parallel-agents | yes | yes (displayed Apr 22, 2026) | yes — post introduces parallel agent threads and lets users "Isolate worktrees, when you want to, and decide per thread"; states "Parallel Agents is available in the latest Zed release" (no version named) | none (ok) |
| CI2026-024-002 | https://zed.dev/releases/stable/1.3.5 | yes | yes (displayed May 20, 2026; GitHub release `v1.3.5` `published_at` 2026-05-20) | yes — "Added the ability to create Terminal Threads in the Sidebar and Agent Panel." | none (ok). Note: same feature is also announced in the May 20 blog post [Terminal Threads Are Live in Zed](https://zed.dev/blog/terminal-threads), recorded as a new row in the same duplicate group, not a second event |
| CI2026-024-005 | https://zed.dev/blog/sandboxing | yes | yes (displayed August 5th, 2026; GitHub release `v1.14.2` `published_at` 2026-08-05 lists "Added sandboxing for the Agent's `terminal` and `fetch` tools") | yes — "Sandboxing is enabled by default for all users, starting on the 1.14 release"; covers macOS Seatbelt, Linux Bubblewrap, WSL-only on Windows ("Non-WSL shells on Windows do not support sandboxing"), privilege-escalation prompts and a symlink-swap TOCTOU section | none (ok) |
| CI2026-024-003 | https://zed.dev/blog/introducing-delta | yes | yes (displayed August 12, 2026) | yes — "The first invites to the private beta have gone out today." `preview` is correct | none (ok) |
| CI2026-024-004 | https://zed.dev/blog/delta-public-beta | yes | yes (displayed September 16th, 2026) | yes — "launching the public beta of Delta"; Zed "disabled pull requests on Delta's own repository"; free during public beta, paid plans "coming soon"; Delta has its own domain (delta.dev) | none (ok) |

**Outcome:** 5/5 reachable, 5/5 dates match, 5/5 claims supported. **No status, limitation or confidence change was needed.** No row was deleted and no event_id changed. Observed non-defect detail: the 1.3.5 release page's version list shows versions up to 1.24.2, which are post-window and outside this screen.

**Other URLs preserved from the earlier report** (not ledger rows; reachability checked 2026-10-16): https://zed.dev/ (homepage, reachable; undated, used only for identity). PR links [#203](https://github.com/MSKazemi/github-trending-1000-study/pull/203) and [#238](https://github.com/MSKazemi/github-trending-1000-study/pull/238) are this study's own provenance links.

## B. Spot-check of new rows (all new rows were opened directly; seven re-read for this table)

| event_id | URL | Reachable? | Date matches? | Claim supported? |
|---|---|---|---|---|
| CI2026-024-006 | https://zed.dev/blog/zed-1-0 | yes | yes (April 29, 2026; GitHub `v1.0.0` 2026-04-29) | yes — "1.0 doesn't mean "done""; ACP agents named; Zed for Business "very soon" |
| CI2026-024-008 | https://zed.dev/blog/zed-for-business | yes | yes (May 6, 2026) | yes — "generally available at $30 per seat, per month"; SSO/SOC 2 not yet available |
| CI2026-024-009 | https://github.com/zed-industries/zed/security/advisories/GHSA-fj2r-rmw6-h222 | yes (gh api) | yes (`published_at` 2026-05-08) | yes — `.git/config` `core.fsmonitor` RCE; patched `>=v0.227.1` (pre-window version) |
| CI2026-024-013 | https://github.com/zed-industries/zed/pull/57948 | yes (gh api) | yes (`merged_at` 2026-05-28) | yes — "The AGPL license is no longer used in the zed repository" |
| CI2026-024-016 | https://zed.dev/blog/introducing-deltadb | yes | yes (June 11, 2026) | yes — beta "ready in a few weeks", waitlist → `announced_only` |
| CI2026-024-018 | https://github.com/agentclientprotocol/agent-client-protocol/releases/tag/v1.0.0 | yes (gh api) | yes (`published_at` 2026-06-24) | partially — the release body only lists one unstable config-option change; the "1.0" significance is inferred from the tag, so confidence is kept low |
| CI2026-024-022 | https://github.com/zed-industries/zed/releases/tag/v1.14.2 | yes (gh api) | yes (2026-08-05) | yes — sandboxing line present; corroborates CI2026-024-005 (same duplicate group) |

**Doubtful/limited items flagged for a human reviewer:** (1) CI2026-024-018 — ACP is hosted in a separate `agentclientprotocol` GitHub organization; Zed's stewardship of that org was **not verified**, so the row is context for Zed's ACP strategy, not a Zed-attributed release. (2) May 14 Anthropic billing post — the post itself carries a June 16 update saying the change "is not taking effect yet"; recorded as `reported_undetermined`, not as a shipped change. (3) Some release notes name third-party model versions (e.g. GPT 5.6, Grok 4.5); these are Zed's provider-list claims and were not verified with the model vendors.
