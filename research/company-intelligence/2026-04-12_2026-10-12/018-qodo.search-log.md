# Qodo (018) — seven-segment search and fetch log (2026-10-16)

> **Provisional source-lead screen (upgraded 2026-10-16):** this log, the [report](018-qodo.md), the [event ledger](018-qodo.events.csv) and the [source-QC note](018-qodo.source-qc-2026-10-16.md) are **provisional, AI-assisted documentary source leads**, unreviewed by a qualified human; factual/link, source-access/rights and methods review pending. Merging is not scientific or security sign-off; issue [#85](https://github.com/MSKazemi/github-trending-1000-study/issues/85) was closed on maintainer instruction (2026-10-16) with these review gates still open — reopen it if review finds a defect.

**Window:** 2026-04-12 … 2026-10-12 inclusive. **Run date:** 2026-10-16 (exact per-call UTC times not recorded). **Tools:** WebFetch (public pages, no login), WebSearch (3 calls; shared budget), read-only `gh api`. **Older logs (left untouched):** the [2026-10-14 seven-query checkpoint and 2026-10-15 supplement](source-audits/018-qodo.2026-10-14-qa.md) records the month-targeted `site:qodo.ai/blog/` queries run on 2026-10-14; this log does not re-run them.

Search engines returned **no total hit counts**; "found/screened/excluded" denominators below are therefore **unknown** unless a listing page was read in full. This is not exhaustive discovery; a segment with few rows is not evidence of inactivity.

## Window-wide fetches and queries (2026-10-16)

| # | Exact fetch / query | Tool | What was read | Decision |
|---|---|---|---|---|
| F1 | `https://www.qodo.ai/blog/` | WebFetch | Blog index listing ~55 posts with displayed dates; only posts dated Aug 27–Oct 12 2026 appear on the first page plus pinned announcements | Used to find in-window posts (rows CI2026-018-021, -023, -024); posts dated Apr–Jul 2026 are **not on the index page** (found earlier by search/archived leads) |
| F2 | `https://docs.qodo.ai/` → `https://docs.qodo.ai/changelog` | WebFetch | Docs changelog: 16 dated entries 28 Apr 26 … 15 Oct 26 (Qodo 2.2.1 … 3.1) | **Primary new source.** Included 2.2.1, 2.5, 2.8, 2.9 as rows; others used to cross-check existing rows; 3.1 (15 Oct) excluded out of window |
| G1 | `gh api repos/The-PR-Agent/pr-agent/commits?path=LICENSE` | gh | 5 LICENSE commits 2023-07-05 … 2026-07-09 | Included fdbcecc (2026-05-20) and d7e94bc (2026-07-09) as rows |
| G2 | `gh api repos/The-PR-Agent/pr-agent/releases?per_page=30` | gh | 19 releases with `published_at` in window (v0.34.1 2026-05-02 … v0.47.0 2026-10-02); v0.34 (2026-04-02) is pre-window | Included v0.34.1, v0.36.1, v0.39.0, v0.43.0, v0.44.0, v0.47.0; excluded the other 13 as routine (listed below) |
| G3 | `gh api repos/The-PR-Agent/pr-agent/security-advisories` | gh | empty list | No published GHSA; recorded in CI2026-018-012 limitation |
| G4 | `gh api orgs/qodo-ai/repos?sort=pushed` | gh | 14 public repos; `qodo-skills` (MIT), `qodo-cover` (AGPL-3.0, last commit 2025-06-24 "Adding EOL"), `agents` (MIT), `claude-plugins-official` fork (Apache-2.0) | Baseline only; qodo-cover EOL is **pre-window** |
| G5 | `gh api repos/qodo-ai/qodo-skills/releases` + `/license` | gh | 23 releases 2026-09-01 … 2026-10-14; LICENSE MIT | Included v2.0.0 (2026-09-08); v2.1.x (Oct 13–14) excluded out of window |
| S1 | `Qodo AI code review news 2026` | WebSearch | Results: Qodo 2.0 (Feb 2026) coverage on itbrief, Globes / dealroom / itbrief $70M Series B, ecosistemastartup benchmark piece | All **pre-window** (Feb–Mar 2026) or vendor-benchmark restatements; excluded. Series B blog is dated Mar 30 2026 on Qodo's index |
| S2 | `PR-Agent "The-PR-Agent" community Qodo handover license` | WebSearch | Futurum note, GitHub repo, marketplace listing, directory/comparison sites | Opened Futurum (row CI2026-018-008, AI-generated, no new facts); directory sites excluded (undated, non-independent) |
| S3 | `Qodo deprecates code generation autocomplete IDE plugin April 2026` | WebSearch | docs.qodo.ai code-completion pages, the Apr 23 post, graphify.net directory | Opened `https://docs.qodo.ai/qodo-ide/code-intelligence/code-completion`: undated notice "The Qodo IDE plugin is being retired on October 30, 2026" — **contradictory evidence** to the Apr 23 post; no row (undated), recorded in report and CI-018-01 limitation |

## Per-segment record

| Segment | Fetches/queries used (IDs above + direct pages) | Pages opened | Included rows (final ledger) | Excluded / notes | Hit counts |
|---|---|---|---|---|---|
| Apr 12–30 | F2, G1, G2, S2, S3; direct: Apr 23 code-generation post, Apr 23 PR-Agent post | 5 | 4: CI-018-01, CI-018-02, CI2026-018-008, CI2026-018-009 | Series B (Mar 30) and PR-Agent v0.34 (Apr 2) pre-window | unknown |
| May | F2, G1, G2; direct: Findings Page post | 3 | 3: CI2026-018-005, CI2026-018-010, CI2026-018-011 | Qodo 2.3.1 Live Preview (20 May, Beta) and 2.3.2 Conversational Chat (27 May, "Alpha") screened, not added (minor); PR-Agent v0.34.2/v0.34.3 (same day as v0.34.1, Docker rename) folded into CI2026-018-010; v0.35.0 (May 14: default model GPT-5.5, CodeQL, SHA-pinned Actions) not added | unknown |
| Jun | F2, G2, G3; direct: Anatomy of a Breaking Change, Qodo 2.4 post, Jun 30 editorial | 4 | 5: CI2026-018-001, CI-018-03, 018-E01, CI2026-018-012, CI2026-018-013 | Qodo 2.3.3 (4 Jun) and 2.3.4 (10 Jun) not added; Qodo 2.4 changelog date 16 Jun vs blog 23 Jun recorded in QC; PR-Agent v0.36.0, v0.37.0 (A2A 1.0), v0.38.0 not added | unknown |
| Jul | F2, G1, G2; direct: Review Effort Modes post | 2 | 3: CI2026-018-002, CI2026-018-014, CI2026-018-015 | Qodo 2.6 (15 Jul; IdP-initiated SSO, REVIEW.md Research Preview) and 2.7 (29 Jul) screened, not added; PR-Agent v0.40.0 (path-traversal fix in Gerrit provider), v0.41.0 not added; TT Lab 2026-07-17 commentary remains an unvetted lead (see [QA supplement](source-audits/018-qodo.2026-10-14-qa.md)), no row | unknown |
| Aug | F1, F2, G2; direct: Aug 27 steering editorial | 3 | 4: CI2026-018-006, CI2026-018-016, CI2026-018-017, CI2026-018-018 | Qodo 2.8.1 (20 Aug) not added; PR-Agent v0.41.1 (Aug 1, not on PyPI at release), v0.42.0 not added | unknown |
| Sep | F1, F2, G2, G5; direct: Agentic Toolbox, Qodo for Codex, Software Map, State of AI Code Quality, Rules Lifecycle Part 2 | 6 | 6: CI2026-018-003, CI2026-018-007, CI-018-05, CI2026-018-004, CI2026-018-019, CI2026-018-020 | Sep 1 "Rules Lifecycle System Part 2" read: explains existing capability, no launch or availability — excluded; Sep 3 "Best Codacy Alternatives" (comparison marketing) and "7 Agent Skills…" (editorial) listed, not opened, excluded; Qodo 2.10 (15 Sep) duplicates CI-018-05; PR-Agent v0.45.0, v0.46.0 not added | unknown (blog index: 7 Sep-dated posts listed) |
| Oct 1–12 | F1, F2, G2; direct: Qodo 3.0, Oct 1 CEO editorial, Oct 5 Jev, Oct 6 Dark Factory, Oct 12 benchmark | 5 | 5: CI-018-06, CI2026-018-021, CI2026-018-022, CI2026-018-023, CI2026-018-024 | Oct 6 "Inside Qodo's Dark Factory" read: internal agent system, no release/availability — excluded (direction context in report); Qodo 3.1 (15 Oct), qodo-skills v2.1.0–2.1.2 (13–14 Oct) **out of window** | unknown (blog index: 5 Oct-dated posts listed) |

**Totals:** 30 ledger rows (13 pre-existing + 17 new). Segment counts 4 / 3 / 5 / 3 / 4 / 6 / 5. Rows sourced from the single living [docs changelog](https://docs.qodo.ai/changelog) are date-scoped entries of one page, like the Tailscale changelog rows.

## Planned queries not executed (WebSearch budget)

- `"Qodo" site:techcrunch.com OR site:theregister.com 2026` — not executed
- `"Qodo" layoffs OR acquisition OR lawsuit 2026` — not executed
- `"PR-Agent" MIT license change July 2026 reason` — not executed (the GitHub commit message gives no reason)
- `"Qodo" security vulnerability CVE 2026` — not executed (only the PR-Agent advisory API was checked)
- `Qodo IDE plugin retired October 30 2026 announcement` — not executed; the retirement notice date of first publication is unknown

## Access and safety

Public pages only; no login, paywall, github.com/trending access, bulk crawl or personal identifiers in requests. Pages have URLs and displayed dates but no archived byte hashes. Instructions aimed at AI agents were not encountered in fetched pages.
