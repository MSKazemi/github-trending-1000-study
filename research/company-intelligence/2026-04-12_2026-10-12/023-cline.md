# Cline — provisional six-month technology intelligence screen (023)

> **Provisional source-lead screen (upgraded 2026-10-16):** this report, its [event ledger](023-cline.events.csv), [search log](023-cline.search-log.md) and [source-QC note](023-cline.source-qc-2026-10-16.md) are **provisional, AI-assisted documentary source leads**. They are **unreviewed by a qualified human**; factual/link review, source-access/rights review and methods review remain **pending**. Merging is not scientific or security sign-off; issue [#90](https://github.com/MSKazemi/github-trending-1000-study/issues/90) was closed on maintainer instruction (2026-10-16) with these review gates still open — reopen it if review finds a defect.

- **Watchlist:** 023; [issue #90](https://github.com/MSKazemi/github-trending-1000-study/issues/90).
- **Window:** 2026-04-12 through 2026-10-12 inclusive; **source-screened 2026-10-16** (first passes 2026-10-12/13/14, preserved below). Exact UTC search-run times, search-engine result totals, immutable page snapshots and an independent reviewer are unavailable.
- **Status:** provisional dated documentary screen — **23 ledger rows** (4 pre-existing, 19 added) covering all seven calendar segments; not reviewed by a qualified human. Not independently verified task outcomes, exhaustive retrieval or human-approved scientific completion.
- **Official sources checked:** [cline.bot](https://cline.bot/), [blog](https://cline.bot/blog), [cline/cline releases](https://github.com/cline/cline/releases), [repository security advisories](https://github.com/cline/cline/security/advisories), [repository licence](https://github.com/cline/cline/blob/main/LICENSE). Claim grading is company-watch E0–E4, not the separate [evidence-to-lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md).

## 1. Discovery, coverage and exclusions

The [search log](023-cline.search-log.md) records every query and fetch actually run, per segment, with inclusion/exclusion reasons. The main enumeration was read-only `gh api` over the public `cline/cline` releases (**209** release tags between 2026-03-25 and 2026-10-13 across four product lines) and repository security advisories (3, of which 2 in-window), plus WebFetch of dated blog posts and 4 web searches. The previous version's statement that April, July (beyond the benchmark post), August and early October had no verified events was a coverage gap, now filled; this is a dated correction, not evidence inflation. Release counts measure publishing activity, **not** innovation rate, quality or adoption. Search-engine totals are **unknown, not zero**.

## 2. Identity and rights baseline

- **Entity:** the public GitHub organisation [cline](https://github.com/cline) (homepage https://cline.bot) publishes the product. The legal entity name ("Cline Bot Inc." in the task prompt) was **not verified** against a corporate registry. Late-January 2026 secondary reports (search snippets only, not opened) say OpenAI hired several Cline staff and that this was "not an acquisition"; this is **pre-window baseline and unverified**, and no change of ownership is asserted here.
- **Products in window:** VS Code extension (3.79 → 4.1.23; JetBrains shares the core), Cline CLI (3.0.0 → 3.0.70, rebuilt on the SDK), the open-source agent runtime `@cline/sdk`, Cline Desktop / "Cline Code" (macOS from Jul 22; Windows beta per Sep 14 post), the Kanban board server, and the paid ClinePass subscription.
- **Licences:** repository [cline/cline](https://github.com/cline/cline) declares **Apache-2.0** (GitHub licence metadata, 2026-10-16). The SDK blog post itself names no licence; the Desktop post says the Mac app is "fully open source" without stating the Windows build's licence. Hosted services (Cline provider, ClinePass, connectors) are **not** covered by the code licence; plan terms were not reviewed. Third-party models/providers have their own terms.
- **Security baseline (pre-window):** [GHSA-9ppg-jx86-fqw7](https://github.com/cline/cline/security/advisories/GHSA-9ppg-jx86-fqw7) (2026-02-17) — unauthorized npm publish of `cline@2.3.0` with a modified postinstall script — predates the window and is excluded from the ledger.

## 3. Seven-segment dated chronology

| Segment | In-window source evidence (displayed publication dates) | Availability and attribution limits |
|---|---|---|
| Apr 12–30 | [Apr 15 Cline mobile how-to](https://cline.bot/blog/cline-mobile-how-to-vibe-code-from-your-phone) (Kanban board reachable from a phone via Tailscale); [Apr 16 v3.79.0](https://github.com/cline/cline/releases/tag/v3.79.0) (Opus 4.7, remote-config `globalSkills`, "action injection security risk" fix) | How-to exposes a local agent server beyond loopback — relevant to the May advisory; security fix has no advisory/CVE |
| May | [May 8 GHSA-5c57 / CVE-2026-44211](https://github.com/cline/cline/security/advisories/GHSA-5c57-rqjx-35g2) critical Kanban WebSocket hijack; [May 12 CLI v3.0.0 on the SDK](https://github.com/cline/cline/releases/tag/cli-v3.0.0); [May 13 SDK announcement](https://cline.bot/blog/introducing-cline-sdk-the-upgraded-agent-runtime) | No patched version named for CVE-2026-44211 in GitHub/GitLab records; SDK post says IDE extensions still migrating |
| June | [Jun 15 plugins/hooks](https://cline.bot/blog/extend-cline-with-plugins-and-hooks); [Jun 23 GHSA-3cj3 / CVE-2026-59723](https://github.com/cline/cline/security/advisories/GHSA-3cj3-hqcr-g934) Hub dashboard hijack; [Jun 26 v4.0.0 SDK-backed extension](https://github.com/cline/cline/releases/tag/v4.0.0); [Jun 28 v4.0.1 rollback](https://github.com/cline/cline/releases/tag/v4.0.1); [Jun 29 ClinePass $9.99/month](https://cline.bot/blog/clinepass-best-of-value-for-open-weight-models) | **Shipped then reversed within two days** — explicit negative result; Hub fix version range differs between advisory records |
| July | [Jul 22 Desktop v0.0.2 — first public macOS release](https://github.com/cline/cline/releases/tag/desktop-v0.0.2); [Jul 24 recursive self-improvement benchmark](https://cline.bot/blog/recursive-self-improvement-for-coding-agents); [Jul 31 v4.1.0 A/B loader, staged rollout from 1%](https://github.com/cline/cline/releases/tag/v4.1.0) | Benchmark is vendor-run (Terminal-Bench 2.1, Kimi K3, 88.8%); rollout share is vendor-controlled |
| August | [Aug 5 v4.1.4 plan-mode hard block](https://github.com/cline/cline/releases/tag/v4.1.4); [Aug 18 eval traces published](https://cline.bot/blog/open-sourcing-evals-for-open-weight-agents); [Aug 26 code-review agent on the SDK](https://cline.bot/blog/building-a-code-review-agent-with-cline-sdk); [Aug 26 v4.1.16 credential redaction/hook fixes](https://github.com/cline/cline/releases/tag/v4.1.16) | Vendor-stated 100% SDK rollout reached **Aug 23** (reported Sep 2); eval data has no stated licence |
| September | [Sep 2 migration retrospective](https://cline.bot/blog/how-we-migrated-11-million-users-to-clines-biggest-harness-upgrade); [Sep 14 Desktop announcement](https://cline.ghost.io/cline-desktop-an-open-source-app-for-open-weight-models/); [Sep 17 v4.1.19 Windows executable-hijack fix](https://github.com/cline/cline/releases/tag/v4.1.19); [Sep 22 v4.1.20 parallel sub-agents, hook-context regression fix](https://github.com/cline/cline/releases/tag/v4.1.20) | "11 million users" (Sep) vs "over 7m developers" (May) are vendor figures, not verified adoption; Desktop "announcement" post-dates first macOS release by ~8 weeks |
| Oct 1–12 | [Oct 2 Desktop v0.0.42 connectors (beta-gated)](https://github.com/cline/cline/releases/tag/desktop-v0.0.42); [Oct 7 v4.1.23](https://github.com/cline/cline/releases/tag/v4.1.23) (MCP output paging, approval race fix, fix of a 4.1.22 regression) | Oct 13 releases and the Oct 15 NVIDIA Nemotron post are **excluded** (out of window) |

`published_utc` is the displayed source date (GitHub `published_at` date for releases); `event_date_utc` is filled only where the source states a distinct underlying date (Aug 23 rollout completion). Blog-sitemap `lastmod` values show several posts were edited after publication.

## 4. Feature, rights and security cross-check

| Evidence cluster | What the cited documents support | Non-equivalence / counter-evidence |
|---|---|---|
| SDK as reusable runtime: [SDK post](https://cline.bot/blog/introducing-cline-sdk-the-upgraded-agent-runtime) → [CLI 3.0.0](https://github.com/cline/cline/releases/tag/cli-v3.0.0) → [v4.0.0](https://github.com/cline/cline/releases/tag/v4.0.0) → [v4.0.1 rollback](https://github.com/cline/cline/releases/tag/v4.0.1) → [v4.1.0 A/B loader](https://github.com/cline/cline/releases/tag/v4.1.0) → [Sep 2 retrospective](https://cline.bot/blog/how-we-migrated-11-million-users-to-clines-biggest-harness-upgrade) | One harness now backs CLI, extension and Desktop; vendor reports staged rollout with automatic legacy fallback | First big-bang migration **regressed and was reverted**; user issue reports (e.g. [#11944](https://github.com/cline/cline/issues/11944), plugin sandbox not bundled) are individual reports. A reusable SDK is not evidence of third-party reuse |
| Extensibility: [plugins/hooks](https://cline.bot/blog/extend-cline-with-plugins-and-hooks), Customize marketplace (v4.0.0), Agent Plugins in Desktop, [code-review agent tutorial](https://cline.bot/blog/building-a-code-review-agent-with-cline-sdk) | Hooks before/after run, tool and model calls; plugins bundle tools/skills/MCP servers | Hook regressions recurred: `PreToolUse` context dropped (fixed v4.1.11), hook workspace mis-resolution (v4.1.16), `UserPromptSubmit`/`TaskStart` context dropped (v4.1.20). A regex deny-list is not a sandbox |
| Local agent servers: [CVE-2026-44211](https://github.com/cline/cline/security/advisories/GHSA-5c57-rqjx-35g2) (Kanban, CVSS 9.6), [CVE-2026-59723](https://github.com/cline/cline/security/advisories/GHSA-3cj3-hqcr-g934) (Hub, CVSS 8.8) | Two in-window cross-origin WebSocket flaws in localhost servers, the second compounded by auto-approve defaults | Kanban advisory lists **no fixed version** ([GitLab record](https://advisories.gitlab.com/npm/cline/CVE-2026-44211/)); Hub fix range disagrees between [repo advisory](https://github.com/cline/cline/security/advisories/GHSA-3cj3-hqcr-g934) (≤3.0.24) and [GitHub global record](https://github.com/advisories/GHSA-3cj3-hqcr-g934) (<3.0.30) |
| Approval/safety defaults: v4.0.0 command auto-approval off by default; [v4.1.4 plan-mode hard block](https://github.com/cline/cline/releases/tag/v4.1.4); [v4.1.16](https://github.com/cline/cline/releases/tag/v4.1.16) per-tool MCP auto-approve boxes hidden as no-ops; [v4.1.19](https://github.com/cline/cline/releases/tag/v4.1.19) Windows planted-executable fix; v4.1.17 checkpoint restore refuses to drop later commits | Vendor moved several controls from prompting to enforcement | The vendor's own note that per-tool MCP approval boxes "were no-ops" means users had a false sense of granularity before Aug 26. Planted-executable fix has no advisory/CVE |
| Model portability: hundreds of providers; v4.1.20 / v4.1.22 / v4.1.23 change default models for many unpinned providers | Provider switching is a core product property | Silent default-model changes undermine reproducibility unless a model is pinned |
| Benchmarks: [Jul 24 Terminal-Bench 2.1 88.8%](https://cline.bot/blog/recursive-self-improvement-for-coding-agents), May 13 Terminal-Bench 2.0 figures, Sep 14 Desktop post | Vendor-run results with some disclosed caveats (invalidated reruns, human babysitting) | Not independently replicated; harness tuned against the benchmark it reports |

**Independent coverage screened:** [TestingCatalog (May 13, labelled Sponsored)](https://www.testingcatalog.com/cline-releases-open-source-agent-runtime-sdk-for-coding-agents.md) and [RuntimeWire (Sep 14)](https://runtimewire.com/article/cline-launches-desktop-coding-agent-open-weight-models) restate vendor material — **not** independent confirmation. The GitHub-reviewed and GitLab advisory records are third-party *databases* of the vendor's disclosure, not independent reproductions. No critical investigative reporting was found within the search budget (absence ≠ none).

## 5. Publicly stated direction versus shipped functionality

| Dated first-party statement | Stated intention | Classification on 2026-10-12 |
|---|---|---|
| [May 13 SDK post](https://cline.bot/blog/introducing-cline-sdk-the-upgraded-agent-runtime): "We are in the process of migrating our VS Code and Jetbrains extensions." | Rebuild all surfaces on one SDK | VS Code: **shipped after one rollback**, 100% per vendor as of Aug 23. JetBrains: not separately verified |
| [Jun 15 plugins post](https://cline.bot/blog/extend-cline-with-plugins-and-hooks): plugins reusable "across the CLI, VS Code, JetBrains, and the SDK" | One plugin format across surfaces | Partly shipped (extension marketplace in v4.0.0/4.1.x; Desktop Agent Plugins Sep 3); JetBrains parity unverified |
| [Sep 14 Desktop post](https://cline.ghost.io/cline-desktop-an-open-source-app-for-open-weight-models/) | Dedicated open-source workspace for open-weight models, scheduled tasks, marketplace | **Preview/beta** (pre-1.0, Windows beta, connectors beta-gated) |
| [Jun 29 ClinePass](https://cline.bot/blog/clinepass-best-of-value-for-open-weight-models) | Low-cost subscription for open-weight models | Shipped (paid service); value/rate-limit claims unverified |

No dated 2027+ roadmap commitment was found. Stated intentions are not delivery schedules.

## 6. Conditional 2027–2031 outlook (analyst hypotheses, not company strategy)

| Hypothesis | Rival explanation | Disconfirming observation |
|---|---|---|
| A shared open runtime (SDK) lowers the cost of building task-specific agents (e.g. review agents) versus bespoke loops | Frequent SDK releases (32 tags Jul 15–Oct 8, still 0.0.x) make pinning and upgrades costlier than a small custom loop | Pinned-SDK prototype needs more maintenance minutes over 90 days than a minimal custom loop for the same accepted tasks |
| Moving controls from prompts to enforced hooks/plan-mode blocks reduces unsafe agent actions | Repeated hook regressions and localhost-server CVEs show enforcement layers add their own attack surface | Adversarial fixture suite shows equal or higher policy-violation rate with hooks enabled |
| Model portability helps reproducibility across changing providers | Unpinned default-model churn makes results drift | Same pinned task replay differs materially across catalog refreshes even with model pinned |

## 7. M1–M7 study relevance

| Construct | Prospective measurement (not an inferred conclusion) |
|---|---|
| **M1** coding-practice change | Record which surface (IDE/CLI/SDK/Desktop) and approval mode opt-in maintainers actually use; releases ≠ usage |
| **M2** accepted task quality | Independently authored hidden acceptance tests; count failures, refusals, rollbacks (cf. 4.0.0 → 4.0.1) |
| **M3** discovery | Vendor user counts (7m → 11m) and stars are attention, not reuse |
| **M4** verified third-party reuse | Trace a consented downstream project actually embedding `@cline/sdk` at a pinned version |
| **M5** reuse-first | Compare pinned `@cline/sdk` against a minimal standard-library loop and existing CI tools for one frozen task |
| **M6** lifecycle cost | Upgrade/rollback/review minutes and CI time; **no token-to-kWh/CO2e conversion** |
| **M7** safe adoption | Local-server exposure, auto-approve defaults and secret redaction tested before any opt-in pilot |

## 8. One falsifiable reuse-first maintainer experiment (proposed, not executed)

**Target:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study) offline surfaces only (synthetic fixtures; live Trending `capture` stays disabled under the source-access decision).

**Frozen task (set by a person other than the implementer, before assignment):** "Given a PR diff touching `trending_study/`, produce review findings that a hidden, independently written checklist of 10 seeded defects (plus 10 clean diffs) can score." All 20 diffs stay in the denominator, including timeouts and refusals.

**Comparator A (reuse):** a review agent built on a **pinned** `@cline/sdk` release (exact version + commit + Apache-2.0 licence recorded), run in a throwaway container with no network secrets, no credentialed CI, and command auto-approval off. **Comparator B (minimal build):** the repo's existing `python3 -m unittest` suite and validators plus a ≤150-line standard-library script, no agent. Same model/provider budget cap for A if a model is used; B uses none.

**Primary endpoint:** seeded defects found ÷ 10 and false-positive flags ÷ 10 clean diffs, scored by the hidden checklist. **Secondary:** setup + review + repair minutes (measured), dependency count added, licence/provenance check pass, and 30-day upgrade effort given SDK release cadence. Energy only if metered, with system boundary.

**Guardrails/stop rule:** stop A immediately on any write outside the container, any secret read, or any local server listening beyond loopback (cf. CVE-2026-44211/59723). **Do not adopt A** unless it detects ≥3 more seeded defects than B *and* total maintainer minutes (including upgrade/review) are not higher; otherwise keep B. A null or negative result is reported as such.

## 9. Evidence quality, limitations and review checklist (2026-10-16)

- **Inventory:** 23 CSV rows — 12 GitHub release notes (E2 documentary), 2 security advisories (E2), 9 first-party blog posts (E1). No E3/E4 evidence: nothing was installed, run or independently replicated.
- **Negative/contrary results retained:** v4.0.0 regression and rollback; two in-window localhost WebSocket CVEs (one with no named fix); repeated hook regressions; MCP per-tool approval boxes were no-ops; Desktop "announcement" lags first release; inconsistent vendor user figures.
- **Unknowns:** legal entity and ownership at filing level; Marketplace/Open VSX/npm publish dates and provenance; JetBrains parity; Windows Desktop licence; actual user adoption; real-world exploitation of the CVEs (none claimed).
- **Pending:** qualified human factual/link review, source-access/rights review, methods review, archived snapshots, and any controlled task trial. AI-assisted drafting is not independent review.

**Study anchors:** [company method](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md) · [evidence-to-lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md) · [2027 central mission](../../../docs/AI_ERA_CODING_REUSE_RESEARCH_MISSION.md) · [reusable-component study](../../../docs/REUSE_FIRST_EXPERIMENT.md) · [news intake #56](https://github.com/MSKazemi/github-trending-1000-study/issues/56).

## Earlier screen (preserved)

Full prior texts remain in git history, the unchanged [`023-cline.events.json`](023-cline.events.json) (3 working observations, review date 2026-10-12) and the [archived 2026-10-13 alternate screen](source-archives/023-cline.2026-10-13-first-screen.md). Summary of what the previous version of this file claimed:

- **Origin:** first-pass report from [PR #202](https://github.com/MSKazemi/github-trending-1000-study/pull/202) (2026-10-12), reconciled with the alternate screen from [PR #237](https://github.com/MSKazemi/github-trending-1000-study/pull/237) (2026-10-13), plus a 2026-10-14 desk check of the SDK page and a 2026-10-14 "controlled integration review". Official starting point cited: https://cline.bot/.
- **Claimed events (4 CSV rows, 3 JSON rows):** May 13 SDK announcement (`shipped`, E1/E2) — [source](https://cline.bot/blog/introducing-cline-sdk-the-upgraded-agent-runtime); Jun 15 plugins/hooks (`reported_undetermined`) — [source](https://cline.bot/blog/extend-cline-with-plugins-and-hooks); Jul 24 recursive self-improvement benchmark, "88.8% score and cost figures … NOT independently replicated" — [source](https://cline.bot/blog/recursive-self-improvement-for-coding-agents); Sep 14 Desktop (`preview`) — [source](https://cline.ghost.io/cline-desktop-an-open-source-app-for-open-weight-models/). Searches logged then: `site:cline.bot/blog 2026 "SDK" "plugins" "Desktop"; site:cline.ghost.io September 2026 "Desktop"`.
- **Claimed gaps:** April, July (other than the benchmark), August and Oct 1–12 had "no verified event in this bounded source screen" — explicitly *not* a zero-event assertion. This upgrade fills those segments.
- **Claimed caveats (still valid):** SDK repository is Apache-2.0 but main is mutable, so pin exact versions/commits; February 2026 unauthorized npm publish is pre-window supply-chain baseline; empty `event_date_utc` means unverified, not equal to publication date; no installation, adoption or energy outcome measured.
- **Prior experiment:** freeze a user task to run the existing parser via a pinned `@cline/sdk` harness vs a minimal standard-library CLI, with independent tests, permission boundaries and maintenance hours; stop if benefits do not exceed migration/security/maintenance costs. Section 8 refines this into a review-agent task with seeded defects.
- **QC outcome of the preserved rows (2026-10-16):** all 4 reachable, dates match, claims supported; limitation text clarified for 001/003/004 — see [source QC](023-cline.source-qc-2026-10-16.md). The archived alternate screen linked the Desktop item to the blog index https://cline.bot/blog rather than the article; the ledger uses the article URL.
