# FlutterFlow — provisional six-month technology intelligence screen (031)

> **PROVISIONAL / AI-assisted, not human-reviewed (2026-10-16).** This report, its [event ledger](031-flutterflow.events.csv) and [search log](031-flutterflow.search-log.md) are a **first-pass documentary source-lead screen** prepared with AI assistance. No qualified human has reviewed them. Factual/link review, source-access/rights review and methods review are **pending**. It is not a verified chronology, licence determination, product test or empirical reuse result, and [issue #98](https://github.com/MSKazemi/github-trending-1000-study/issues/98) was closed on 2026-10-16 by maintainer decision with this provisional status recorded; closure is not scientific validation, and the human review gates above remain open. No row has been promoted to the [#56 evidence corpus](https://github.com/MSKazemi/github-trending-1000-study/issues/56).

- **Company watchlist ID:** 031 — [issue #98](https://github.com/MSKazemi/github-trending-1000-study/issues/98); linked corpus initiative [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56).
- **Ownership and product boundaries (as of 2026-10-12):** see §2; FlutterFlow Inc., no parent found.
- **Product URL and official channels:** [flutterflow.io](https://flutterflow.io/), [changelog](https://www.flutterflow.io/flutterflow-changelog), [docs](https://docs.flutterflow.io/flutterflow-cli/build), [GitHub organization](https://github.com/FlutterFlow), [pub.dev flutterflow_cli](https://pub.dev/packages/flutterflow_cli/versions), [community announcements](https://community.flutterflow.io/announcements), [status page](https://status.flutterflow.io/).
- **Analysis window:** 2026-04-12 to 2026-10-12 inclusive; sources read 2026-10-16.
- **Researcher / factual reviewer / review date:** AI-assisted first pass / **pending** / **pending**.
- **Status:** screened (provisional). **19 dated ledger rows**, every calendar segment covered by at least one first-party record; **no in-window independent news coverage found**.
- **Method:** [company-intelligence protocol](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md); [template](../../../templates/company_six_month_intelligence.md). Grades are company-watch E0–E4, not the separate [evidence-to-lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md).

## 1. Search and inclusion audit

Full queries, opened pages, exclusions and inaccessible sources are in the [search log](031-flutterflow.search-log.md). Summary:

| Search run | Site/engine | Scope | Found | Screened | Included | Excluded/why | Coverage limitation |
|---|---|---|---:|---:|---:|---|---|
| 2026-10-16 | flutterflow.io changelog (direct) | 9 in-window entries | 9 | 9 | 8 entries → 9 rows | none | displayed dates only; no archive hashes |
| 2026-10-16 | GitHub REST API (FlutterFlow org) | repos created/released in window | 10 created | 10 | 5 rows | 10 repos created in window (4 cited in rows); 6 without dated release or claim relevance (e.g. `campus-extensions` with no licence, patched `flutter_webrtc`, `flutter_cef`) not given rows | `created_at` ≠ public-visibility date |
| 2026-10-16 | pub.dev API (`flutterflow_cli`) | versions in window | 14 | 14 | 2 rows | individual betas folded into a row | registry licence field "unknown" |
| 2026-10-16 | general web search (13 queries) | press, reviews, FFDC, pricing, incidents | unknown | unknown | 2 rows (Product Hunt, PricingSaaS) | spam mirrors, undated blogs, aggregators | no outlet-specific search; US index |
| 2026-10-16 | status.flutterflow.io history | incidents | — | — | 0 | **inaccessible** (load error) | outages unknown, not zero |

## 2. Verified company/product identity and baseline

- **Entity:** FlutterFlow Inc. is named as licensor in the [Codex plugin LICENSE](https://github.com/FlutterFlow/flutterflow-codex/blob/main/LICENSE). [Y Combinator](https://www.ycombinator.com/companies/flutterflow) lists FlutterFlow as **Active**, batch W21, founded 2020, founders Abel Mengistu and Alex Greaves, San Francisco; **no parent company or acquisition found**. Not checked at filing/registry level.
- **Brands:** FlutterFlow (visual Flutter app builder with code export), **FF Designer** (AI screen design; launched Feb 2026, pre-window), **Dreamflow** ([dreamflow.app](https://dreamflow.app/), "From the team behind FlutterFlow", footer "© 2025 Dreamflow"; legal pages on flutterflow.io — separate legal entity status not verified), **Campus** (Jul 2026 launch listing), FlutterFlow MCP/CLI/AI SDK.
- **Pre-window baseline (not in-window events):** a [2026-02-02 founder post](https://community.flutterflow.io/announcements/post/a-flutterflow-update-ffdc-save-the-date-ZfzSRQkzRupLcSW) says FlutterFlow's pace of innovation slowed while Dreamflow was built separately, and promises more engineering focus on FlutterFlow and a full roadmap at FFDC (May 27–28, 2026). This is context for the in-window release cadence, not a measured effect.
- **Open vs proprietary:** the builder and hosted service are proprietary. Public repos vary: [flutterflow-cli](https://github.com/FlutterFlow/flutterflow-cli) BSD-3-Clause (pub.dev shows licence "unknown"), [flutterflow-claude](https://github.com/FlutterFlow/flutterflow-claude) MIT, [flutterflow-codex](https://github.com/FlutterFlow/flutterflow-codex/blob/main/LICENSE) **BSL 1.1** (source-available, use restricted to FlutterFlow products, change date 2055-04-22), [dart_acp](https://github.com/FlutterFlow/dart_acp) Apache-2.0.

## 3. Month-by-month discoveries

| Month | Announcements/changes | Primary URLs | Independent reporting | Notes or no-result limitations |
|---|---|---|---|---|
| 2026-04-12..30 | Apr 17 Shadertoy→Flutter Claude skill repo; Apr 23 Child Slots, Supabase OAuth, shader uploads, code-export fixes; Apr 27–30 CLI 0.0.32-beta → 0.0.34 | [repo](https://github.com/FlutterFlow/shadertoy_to_flutter_skill), [changelog](https://www.flutterflow.io/changelog/shader-uploads-supabase-oauth-aspect-ratio-widget), [pub.dev](https://pub.dev/packages/flutterflow_cli/versions) | none found | CLI minimum Dart SDK moved 2.17 → 3.7 |
| 2026-05 | May 7 FlutterFlow MCP; May 18 GenUI (A2UI) + generators on Designer engine; FFDC May 27–28 | [MCP](https://www.flutterflow.io/changelog/flutterflow-mcp), [GenUI](https://www.flutterflow.io/changelog/genui-page-component-gen-updates) | none found; [Flutter docs](https://docs.flutter.dev/ai/genui.md) label upstream `genui` alpha | **No dated first-party FFDC recap found** |
| 2026-06 | Jun 8 Activity Logging removed from Business plan table (third-party tracker); Jun 17 FlutterFlow 7.0 | [PricingSaaS](https://pricingsaas.com/companies/flutterflow), [7.0](https://www.flutterflow.io/changelog/flutterflow-7-0) | PricingSaaS is a page-diff tracker, not reporting | 7.0 date conflict (see §9) |
| 2026-07 | Jul 1 Claude Code plugin (MIT) and Codex plugin (BSL) tagged; Jul 15 Campus on Product Hunt; Jul 27 native AI agent in Desktop + plugins | [Claude plugin release](https://github.com/FlutterFlow/flutterflow-claude/releases/tag/v0.1.2), [Codex LICENSE](https://github.com/FlutterFlow/flutterflow-codex/blob/main/LICENSE), [Campus](https://www.producthunt.com/products/flutterflow/launches/campus-4), [changelog](https://www.flutterflow.io/changelog/native-ai-agent-claude-code-codex-plugins) | none found | plugins shipped ~4 weeks before changelog entry |
| 2026-08 | Aug 13 Supabase Upsert/RPC/full-text search; client-code credential flagging | [changelog](https://www.flutterflow.io/changelog/supabase-upsert-rpc-full-text-search) | none found | status-page history inaccessible |
| 2026-09 | Sep 2 Project Search, Try/Catch, agent adds Gemini/Antigravity; Sep 23 CLI 0.0.41; Sep 24 Storyboard, pub.dev package search; Sep 25 plugin install-break fix; Sep 30 dart_acp repo | [Sep 2](https://www.flutterflow.io/changelog/project-search-try-catch-modern-calendar), [pub.dev API](https://pub.dev/api/packages/flutterflow_cli), [Sep 24](https://www.flutterflow.io/changelog/storyboard-revenuecat-find-and-replace), [plugin CHANGELOG](https://github.com/FlutterFlow/flutterflow-claude/blob/main/CHANGELOG.md), [dart_acp](https://github.com/FlutterFlow/dart_acp) | none found | Sep 2 page shows a Sep 10 update |
| 2026-10-01..12 | Oct 6 FlutterFlow 7.2: Flutter 3.47.1, FlutterFlow Dynamic Links, Test Mode Logs, deprecation cutoffs | [changelog](https://www.flutterflow.io/changelog/flutter-3-47-dynamic-links-test-mode-logs) | upstream Google docs on [Dynamic Links](https://firebase.google.com/support/dynamic-links-faq) and [Gemini 2.5](https://firebase.google.com/docs/ai-logic/data-governance) | cutoffs fall after the window |

## 4. Dated event evidence and capabilities

All rows: [ledger](031-flutterflow.events.csv). Highlights:

| Event ID | Published / event date | Claim or observed feature | Availability and limitations | Source (type) | Independent check | Grade |
|---|---|---|---|---|---|---|
| 031-004 | 2026-05-07 | MCP lets existing agents (Claude Code, Cursor, "any agent") edit FlutterFlow projects; validate locally, push | vendor "launched"; API token; scopes undocumented | changelog (E2) | [docs](https://docs.flutterflow.io/flutterflow-cli/build) (same vendor): optimistic-concurrency push, `validate` dry run; out of scope: deploy, secrets | E2 |
| 031-005 | 2026-05-18 | GenUI Chat: agent composes defined components into runtime UI via A2UI, Firebase AI Logic (Gemini) | shipped per vendor; **upstream `genui` alpha** | changelog | [Flutter docs](https://docs.flutter.dev/ai/genui.md) (Google) | E2 |
| 031-007 | 2026-06-17 | 7.0: Live Sessions over MCP; Test Pilot AI QA; custom-code folders; Edge Functions | "now available"; Test Pilot uses credits | changelog | none independent | E2 |
| 031-009 | 2026-07-01 | Codex plugin under BSL 1.1; non-compete use grant; change date 2055 | source-available, **not open source** | LICENSE file | GitHub release metadata | E2 |
| 031-011 | 2026-07-27 | Claude Code/Codex inside FlutterFlow Desktop (macOS); plugins; clipboard API key | shipped per vendor | changelog | plugin repos tagged from Jul 1 | E2 |
| 031-012 | 2026-08-13 | Flags API credentials that may land in generated client code | vendor-described warning | changelog | none | E2 |
| 031-016 | 2026-09-25 | Plugin fresh installs failed (CLI pin 0.0.38 vs SDK 0.0.41 floor); hook switched to auto-upgrade | fixed in 0.1.7 | public CHANGELOG | pub.dev date of 0.0.41 (Sep 23) | E2 |
| 031-018/019 | 2026-10-06 | 7.2: Flutter 3.47.1; Dynamic Links replacement; raised platform minimums; legacy Firebase access ends Oct 29; Gemini 2.5 Flash shutdown Oct 16 | shipped + scheduled cutoffs | changelog | Google Firebase docs | E2 |
| 031-006 | 2026-06-08 | Activity Logging dropped from Business plan table | **unconfirmed** | third-party tracker | none | E1 |
| 031-010 | 2026-07-15 | Campus "one project space for humans and AI agents" | listing only | Product Hunt | none | E1 |

**Feature inventory (vendor assertion unless noted):**
- **Agent integration (M1):** MCP server (May), Live Sessions over MCP (Jun), embedded Claude Code/Codex (Jul), Gemini/Antigravity (Sep), Claude Code + Codex plugins (GitHub-observable, Jul), Agent Client Protocol Dart SDK repo (Sep, metadata only). Direction: FlutterFlow is positioning its hosted project as the **source of truth that third-party agents edit**, rather than shipping only its own model.
- **Quality/testing (M2):** Test Pilot AI QA from plain-English specs, Test Mode Logs with "Fix with AI", Try/Catch/Finally action blocks. No independent accuracy data.
- **Reuse surfaces (M4/M5):** Child Slots, Child Widget parameters, custom-code folders, libraries publishable via CLI (paid plan with branching), pub.dev package search for custom dependencies (no licence/security vetting described).
- **Security:** credential-in-client-code flagging, Gemini API key restriction guidance, clipboard-sourced API key in plugins; the Codex plugin's own commit history notes the `--api-key` flag exposes the key in argv and a **plaintext credential store** ([commit 9260839, 2026-06-30](https://github.com/FlutterFlow/flutterflow-codex/commit/926083966b5b6146bc0133dbae1698b7980c24d3)). No vendor security advisory found in window.
- **Maintenance/upstream churn (M6):** Firebase Dynamic Links replacement (upstream shut down 2025-08-25), Flutter 3.47.1 move with raised minimum OS versions, RevenueCat 10 behaviour change, Gemini 2.5 Flash shutdown affecting GenUI Chat apps, legacy Firebase connection cutoff, CLI/SDK version-floor breakage.
- **Code export:** only indirect evidence — Apr 23 fixes for fonts/icons "missing from downloaded code" and wrong generated function names; Data Type folders now mirrored in generated code (Sep 24). No independent export-quality assessment found.

## 5. What the company says it intends to do

| Public direction (paraphrase, ≤25 words quoted) | Link/date | Horizon | Status | Missing/contradictory context |
|---|---|---|---|---|
| Faster iteration, more frequent updates, more resources and engineering focus on FlutterFlow; full roadmap at FFDC | [2026-02-02 post](https://community.flutterflow.io/announcements/post/a-flutterflow-update-ffdc-save-the-date-ZfzSRQkzRupLcSW) (pre-window) | 2026 | stated intention | In-window cadence (9 changelog entries, 7.0 and 7.2) is **consistent with** but does not prove this; no FFDC roadmap document found |
| "A FlutterFlow project is the source of truth"; CLI for "precision and automation", not a builder replacement | [CLI docs](https://docs.flutterflow.io/flutterflow-cli/build), last updated 2026-10-12 | current | documented design stance | Docs page is current-state, not a dated commitment |
| Firebase Dynamic Links replaced; legacy Firebase access ends 2026-10-29; Gemini 2.5 Flash shuts down 2026-10-16 | [Oct 6 changelog](https://www.flutterflow.io/changelog/flutter-3-47-dynamic-links-test-mode-logs) | Oct 2026 | scheduled (announced_only) | Google gives only "October 2026" for Gemini 2.5 shutdown |
| Codex plugin converts to Apache-2.0 on 2055-04-22 | [LICENSE](https://github.com/FlutterFlow/flutterflow-codex/blob/main/LICENSE) | 2055 | licence term | 29-year horizon; licence may be changed by licensor for future versions |

No dated in-window public roadmap was found. Commercial messaging is not treated as future fact.

## 6. Independent interpretation: conditional 2027–2031 scenarios (researcher's hypotheses, not company statements)

| Hypothesis | Supporting observations | Rival explanations | Disconfirming signals | Confidence/unknowns |
|---|---|---|---|---|
| H1: Visual builders become **agent-editable hosted models** (MCP/ACP), so third-party coding agents operate on a proprietary project graph rather than on exported source | MCP (May), Live Sessions (Jun), embedded Claude/Codex (Jul), Gemini/Antigravity (Sep), dart_acp (Sep) | Industry-wide MCP fashion; marketing reaction to agent tools; may be a thin wrapper with low use | FlutterFlow deprecates MCP/CLI, or independent tasks show agents edit exported Flutter source as well or better | low–medium; no usage data |
| H2: Reuse rights fragment: **permissive** for SDK glue (MIT/BSD/Apache) but **source-available/non-compete** (BSL) for agent tooling | MIT Claude plugin vs BSL Codex plugin in the same week | Single licensing decision, not a strategy; may be harmonised later | Codex plugin relicensed permissively, or BSL applied to all repos | low; n=2 plugins |
| H3: Maintenance burden for builder users is increasingly **driven by upstream AI/cloud churn** (model shutdowns, Firebase service retirements, Flutter minimums) | Oct 6 cutoffs; Gemini 2.5 shutdown; Dynamic Links; CLI/SDK version skew | Normal platform churn independent of AI | Change-notice counts per release stay flat through 2027 relative to 2025 | low; no baseline counted |
| H4: AI QA (Test Pilot) substitutes for some hand-written tests | Test Pilot features, scheduled runs on commit | Vendor-reported only; flaky AI tests may increase review work | Independent comparison shows lower defect detection than conventional integration tests | unknown |

## 7. Implications for the GitHub 1000 study (M1–M7)

| Construct | Possible observable effect | Study design to test it | Negative/null explanation | Measurement boundary |
|---|---|---|---|---|
| **M1** AI coding-agent change | Agent edits shift from exported code to hosted-project MCP edits | Opt-in logs: share of changes by MCP vs exported source in consented projects | Feature unused; edits remain manual | no telemetry access; vendor counts not available |
| **M2** accepted task quality | Agent MCP edits pass/fail independent acceptance tests | Frozen tasks, hidden tests, all attempts in denominator | Same pass rate as hand edits | no trial executed |
| **M3** discoverability | Product Hunt/launch ranking visibility | Track whether launch visibility predicts consented downstream use | Ranking ≠ use | stars/launch rank are not adoption |
| **M4** verified third-party reuse | Public plugins/skills forked and used | Trace consented downstream dependants of MIT plugin vs BSL plugin | Licence irrelevant at small scale | GitHub forks ≠ reuse |
| **M5** reuse-first / rights / security | BSL non-compete limits reuse; pub.dev search adds unvetted deps; auto-upgrade hook bypasses pinning | Licence/provenance audit of generated project dependency lists | No measurable risk difference | no SBOM collected |
| **M6** lifecycle human/energy cost | Upstream deprecations force rebuilds/redeploys | Count required maintainer actions per release notice; time them | Effort negligible | **no energy or CO2e estimate**; only metered if instrumented |
| **M7** actionable interventions | Pinned toolchain + skew canary vs pin-only vs auto-upgrade | See §8 | — | — |

## 8. One practical, falsifiable change for the maintainer's own repositories

**Repository/component:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study) (Python, offline synthetic fixtures). FlutterFlow itself is **not** adopted; the transferable lesson is the **CLI/SDK version-skew failure** documented in row 031-016 (a plugin's pinned dependency fell behind a remote floor and broke fresh installs for ~2 days by changelog dates).

**Candidate practice (not yet validated):** a **non-blocking toolchain-skew canary**: one extra CI job that runs the existing offline checks on the newest available Python (prerelease allowed) and reports failures as warnings, so skew is seen before contributors hit it — instead of either relying only on a fixed matrix (the equivalent of a silent pin) or auto-upgrading pins (the plugin's chosen fix).

**Comparator:** the current `ci.yml` (SHA-pinned `actions/checkout` and `actions/setup-python`; Python 3.10/3.12/3.13/3.14 matrix; `compileall`, artifact checker, `unittest`, CLI `--help` entrypoints) **vs** the same workflow **plus** the canary job. The repository is stdlib-only (no `requirements.txt`/`pyproject.toml`), so the skew surface is the Python interpreter and pinned Actions, not third-party packages.

**Accepted-task unit:** one *fresh-checkout run* = clean checkout + the existing CI steps + the AGENTS.md smoke commands (`value_gate`, `reuse_gate`, `pilot-preflight` on the committed examples) exit with their documented status, judged by a frozen pass/fail script written **before** the trial by someone other than the agent proposing it.

**Guardrails:** push/PR-triggered only (no new scheduled job); no network capture (the `capture` hard stop stays disabled); no new dependency; no change to test semantics or required checks; canary never blocks merges; any Action version change keeps SHA pinning.

**Measured human work:** maintainer minutes to add the job, minutes per canary alert to triage, false-alert count, extra CI minutes per run (from CI logs). No carbon or energy figure is reported unless a metered value exists.

**Primary endpoint:** over 90 days, interpreter/Action skew failures detected by the canary **before** they reach a required matrix job or a contributor report, out of all such failures found by any route (including those found only by people).

**Stop rule:** remove the canary if (a) false or irrelevant alerts exceed true detections after 30 days, (b) triage exceeds 30 maintainer minutes/month with zero true detections, or (c) it ever needs network access to restricted sources. A null result (no skew in 90 days) is recorded as null, not as success. **No trial executed; no effect estimated.**

## 9. Findings, uncertainties and review outcome

- **Observed/shipped (documentary, E2):** nine dated changelog entries; GitHub-observable plugin releases (MIT Claude plugin, BSL Codex plugin); 14 in-window pub.dev CLI versions (0.0.32-beta.1 on 2026-04-27 to 0.0.41 on 2026-09-23; count corrected from 15 by the 2026-10-16 spot-check); a documented plugin install breakage and fix. These are records of what the vendor published, not verified functionality.
- **Claims/announcements only:** MCP edit correctness, Test Pilot QA accuracy, "higher quality" generators, Campus capabilities, scheduled October cutoffs.
- **Conjectures and unknowns:** user adoption of MCP/agents (no data), outages (status history inaccessible), Dreamflow in-window activity (none found), FFDC roadmap content (no dated recap), independent reception (no in-window independent press found), exact legal relationship of Dreamflow to FlutterFlow Inc.
- **Important contradictory or null evidence:** FlutterFlow 7.0 dated Jun 17 by the vendor vs an undated venue page tying it to FFDC May 27–28; plugin repos shipped ~4 weeks before the changelog announced them; pub.dev shows CLI licence "unknown" while GitHub reports BSD-3-Clause; the vendor blog published nothing in window.
- **Reviewer links and audit date:** none yet. Required before acceptance: human factual/link spot-check of all 19 rows, licence re-check of each repo at a pinned commit, and methods review. Request reviewer feedback on the PR; do **not** close #98.

## Independent source spot-check (2026-10-16)

An independent reviewer agent (not the author of this screen) re-fetched the cited sources on 2026-10-16 and compared dates and every specific figure against raw page text (`curl` + grep for flutterflow.io, pub.dev API JSON, Product Hunt embedded JSON, Google docs) or the GitHub REST API (`gh api`). Classification: confirmed / corrected / unverifiable / wrong.

| Row(s) checked | Outcome | Note |
|---|---|---|
| Entity (§2) | confirmed | YC page: Active, batch W21, founded 2020, founders Abel Mengistu and Alex Greaves, San Francisco; Codex LICENSE names FlutterFlow Inc. as licensor. No registry-level check. |
| 031-001 | confirmed | `gh api`: created 2026-04-17T19:07Z, MIT, description matches. |
| 031-002 | confirmed | Page dated April 23, 2026; "31 bug fixes"; code-export, Local Run offline, AspectRatio text present. |
| 031-003 | confirmed | pub.dev API: 0.0.32-beta.1 2026-04-27 … 0.0.34 2026-04-30; SDK floor `>=2.17.0` (0.0.31) → `>=3.7.0` (0.0.32-beta.1). |
| §1 / §9 pub.dev count | **corrected** | In-window versions are **14**, not 15 (0.0.32-beta.1 … 0.0.41; 0.0.31 is 2026-04-10 and 0.0.42 is 2026-10-15, both outside). Text fixed. |
| 031-004 | confirmed | Page dated May 7, 2026; names Claude Code, Cursor, "any agent"; validate locally and push; API token. pub.dev 0.0.35 on 2026-05-06. CLI docs `datetime` 2026-10-12, optimistic-concurrency and out-of-scope text present. |
| 031-005 | confirmed | Page dated May 18, 2026; A2UI and Firebase AI Logic (Gemini); Flutter genui docs say "alpha and is likely to change". |
| 031-006 | confirmed (still E1) | PricingSaaS: "Jun 8, 2026 … FlutterFlow drops Activity Logging from Business plan"; tracking since Apr 29, 2026. "Week 24" is the reviewer-derivable ISO week, not page text. |
| 031-007 | confirmed | Page dated June 17, 2026; Live Sessions & MCP, Test Pilot (schedule/commit/GitHub deploy), Edge Functions, "No more 30-minute limit", audio. |
| 031-008 / 031-009 | confirmed | Releases v0.1.2 "Initial release" 2026-07-01T16:54Z, v0.1.3–v0.1.6 Jul 2/15; Codex v0.1.0 2026-07-01, v0.1.1 2026-07-15; repo created 2026-06-29/06-30. LICENSE (current `main`, not a pinned commit): BSL 1.1, Additional Use Grant and competing-product clause, Change Date April 22, 2055 → Apache-2.0. Commit 9260839 (2026-06-30) adds the LICENSE and notes argv exposure and plaintext credential store. |
| 031-010 | confirmed (still E1) | Product Hunt: Campus, "Launched on July 15th, 2026", embedded `dailyRank":"3"`. FF Designer listing Feb 19th, 2026 also confirmed. |
| 031-011 / 012 / 013 / 015 | confirmed | Dates Jul 27, Aug 13, Sep 2 (updated Sep 10), Sep 24; "8 Bug Fixes"; credential-flagging text; 29 Sep-2 bug-fix items counted (6 under AI Agent reliability); "22 features and improvements and 18 bug fixes". |
| 031-014 / 016 | confirmed | 0.0.41 published 2026-09-23T16:53Z, no 0.0.40; plugin CHANGELOG `[0.1.7] — 2026-09-25` states pin 0.0.38, SDK 0.0.41 needs CLI ≥ 0.0.41, auto-upgrade at most every 6h, forward-only; tag v0.1.7 2026-09-25. |
| 031-017 | confirmed | dart_acp created 2026-09-30, Apache-2.0, 0 GitHub releases. Org has exactly 10 repos created in window. |
| 031-018 / 019 | confirmed, limitation added | Page dated October 6, 2026; 7.2, Flutter 3.47.1, Android API 24 / iOS 15 / macOS 12, "14 features and improvements and 29 bug fixes", RevenueCat 10, Oct 14/29 and Oct 16 dates. Firebase FAQ: shutdown August 25th, 2025; AI Logic page: "October 2026". **Added to 019:** the same cutoffs already appear in the Sep 2 (updated Sep 10) and Sep 24 entries, so Oct 6 is not the first notice. |
| Pre-window community post | confirmed | `publishedAt` 2026-02-02T21:54Z; Dreamflow/innovation-slowed text and FFDC May 27–28, 2026. |
| Changelog completeness | confirmed | Index lists exactly 9 entries dated 2026-04-23 … 2026-10-06. |

Outcome: all 19 ledger rows plus 4 report-level items (entity, pre-window post, changelog completeness, §1 pub.dev count) checked → 19 rows confirmed (row 019 with an added limitation), 3 report items confirmed, 1 report item corrected (pub.dev count 15 → 14); 0 unverifiable, 0 wrong. No fabricated URL, date or figure found; no cross-company contamination found. Not re-checked: status page, Dreamflow pages, upstream genui/A2UI provenance, licence at a pinned commit.

*This is an AI-assisted spot-check, not qualified human review; the human factual/link, rights and methods reviews remain pending.*
