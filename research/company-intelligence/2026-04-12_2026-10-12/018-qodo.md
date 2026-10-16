# Qodo — provisional six-month company-intelligence screen (018)

> **Provisional source-lead screen (upgraded 2026-10-16):** this report, its [event ledger](018-qodo.events.csv), [search log](018-qodo.search-log.md) and [source-QC note](018-qodo.source-qc-2026-10-16.md) are **provisional, AI-assisted documentary source leads**. They are **unreviewed by a qualified human**; factual/link, source-access/rights and methods review pending. Merging is not scientific or security sign-off; issue [#85](https://github.com/MSKazemi/github-trending-1000-study/issues/85) was closed on maintainer instruction (2026-10-16) with these review gates still open — reopen it if review finds a defect.

- **Watchlist:** 018; [issue #85](https://github.com/MSKazemi/github-trending-1000-study/issues/85). Sector: AI code review / code-quality governance; open-source PR-Agent lineage.
- **Window:** 2026-04-12 through 2026-10-12 inclusive; **upgraded and source-QC'd on 2026-10-16**. Exact search-run UTC times, search hit totals, archived page captures and an independent reviewer are unavailable.
- **Status:** **30 dated source leads covering all seven calendar segments** (13 pre-existing rows re-checked, 1 status corrected; 17 new rows). Not independently verified task outcomes, exhaustive retrieval or human-approved scientific completion.
- **Official channels checked:** [Qodo blog index](https://www.qodo.ai/blog/), [Qodo docs changelog](https://docs.qodo.ai/changelog), [The-PR-Agent/pr-agent](https://github.com/The-PR-Agent/pr-agent) releases and LICENSE history, [qodo-ai GitHub org](https://github.com/qodo-ai). **Method:** [company protocol](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md), [M1–M7 mission](../../../docs/AI_ERA_CODING_REUSE_RESEARCH_MISSION.md). Grades are company-watch E0–E4 working labels, not the separate [2027 lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md).

## 1. Discovery, coverage and exclusions

The [2026-10-16 search log](018-qodo.search-log.md) records every fetch, `gh api` call and WebSearch actually run, per segment, with inclusion/exclusion decisions; the earlier [2026-10-14 seven-query checkpoint](source-audits/018-qodo.2026-10-14-qa.md) is preserved unchanged. The main improvement over the earlier screen is the **versioned docs changelog** (Qodo 2.2.1 … 3.0 with explicit Alpha/Beta/Research Preview/GA labels) and **GitHub release/commit metadata** for PR-Agent and `qodo-skills`. Independent journalism inside the window was **not found** in three searches; one third-party analyst page (Futurum) turned out to be LLM-generated and adds no independent facts. Hit counts are unknown, not zero; few rows in a month is not evidence of inactivity.

Excluded as out of window: Qodo Series B blog (Mar 30 2026), PR-Agent v0.34 (Apr 2), `qodo-cover` end-of-life commit (2025-06-24), Qodo 3.1 changelog (15 Oct), `qodo-skills` v2.1.x (13–14 Oct).

## 2. Corporate/product identity and rights baseline

| Item | What the cited source supports (as of 2026-10-16) | Limits |
|---|---|---|
| Qodo (formerly CodiumAI) | Commercial code-review / code-quality governance platform (Git review, rules system, Software Map, Agentic Toolbox, IDE plugin); CEO Itamar Friedman signs the Apr 23 and Oct 1 posts | Legal entity, parent and ownership were **not** checked at filing level |
| Code generation | [Apr 23 post](https://www.qodo.ai/blog/an-update-on-code-generation-at-qodo/): plan "to deprecate Qodo's existing code generation features" (IDE autocomplete, code-generation chat) | No removal date in the post. An **undated** [docs notice](https://docs.qodo.ai/qodo-ide/code-intelligence/code-completion) says "The Qodo IDE plugin is being retired on October 30, 2026" — contradicts the post's "IDE plugin still remains part of the platform"; first-appearance date unknown |
| **PR-Agent** (OSS) | Moved from `qodo-ai/pr-agent` to the community org [The-PR-Agent](https://github.com/The-PR-Agent/pr-agent) ([Apr 23 announcement](https://www.qodo.ai/blog/qodo-is-handing-pr-agent-over-to-the-community/)); maintainers named incl. an external maintainer and a Qodo-affiliated core maintainer | Governance independence from Qodo not audited |
| PR-Agent licence history | `LICENSE` commits via read-only GitHub API: Apache-2.0 at 2023 launch (per Qodo) → AGPL-3.0 (earlier) → **Apache-2.0** at [`fdbcecc`](https://github.com/The-PR-Agent/pr-agent/commit/fdbcecc8cdd9c276919cd9b8f41c981e8ca642ef) (Git date 2026-05-20) → **MIT** at [`d7e94bc`](https://github.com/The-PR-Agent/pr-agent/commit/d7e94bc27a8ad0456090a07e075cecd6e6459626) (Git date 2026-07-09; blob `43fff0c98b18eba319298a18dae01a57ba0eac97`, also at commit `330f0813b5fe0d1f54b794077c2d02aa85a1fb63`). Repo `license.spdx_id` = MIT on 2026-10-16 ([LICENSE](https://github.com/The-PR-Agent/pr-agent/blob/main/LICENSE)) | **Caveats kept:** Git dates are self-reported, unauthenticated metadata; the reason for the MIT change, contributor consent, transitive dependency licences and the licence of any specific packaged release (PyPI/Docker) were **not** examined. The history is consistent with the announced Apache-2.0 return being carried out and later superseded by MIT — not with the announcement being false. Pin a commit and re-read its `LICENSE` before any reuse |
| `qodo-ai/qodo-skills` | MIT-licensed agent-skill packages behind the Agentic Toolbox plugins; 23 releases Sep 1–Oct 14 | Skills require the proprietary Qodo CLI/account at runtime; MIT on the skill text does not license the service |
| `qodo-ai/qodo-cover` | AGPL-3.0 test-generation tool; last commit 2025-06-24 "Adding EOL" | Pre-window baseline only |
| Hosted Qodo platform | Proprietary SaaS / single-tenant / on-prem (Qodo 3.0 claims full on-prem and air-gapped deployment, self-hosted models) | Plan terms, data processing and pricing not checked |

## 3. Seven-segment dated chronology

| Period | In-window source evidence (displayed publication dates) | Availability / attribution limits |
|---|---|---|
| Apr 12–30 (4) | Apr 23 [code-generation deprecation](https://www.qodo.ai/blog/an-update-on-code-generation-at-qodo/) and [PR-Agent handover](https://www.qodo.ai/blog/qodo-is-handing-pr-agent-over-to-the-community/) (+ [Futurum AI-generated note](https://futurumgroup.com/insights/qodo-hands-pr-agent-to-the-community-will-open-governance-accelerate-ai-code-review/), same event); Apr 28 Qodo 2.2.1 install wizards ([changelog](https://docs.qodo.ai/changelog)) | Deprecation is announced_only (no date); Futurum is a syndication, not confirmation |
| May (3) | May 2 [PR-Agent v0.34.1](https://github.com/The-PR-Agent/pr-agent/releases/tag/v0.34.1), first release under the new org; May 13 [Findings Page v2.3 beta](https://www.qodo.ai/blog/introducing-findings-page/); May 20 LICENSE AGPL→Apache commit | Findings Page is beta |
| June (5) | Jun 16 [PR-Agent v0.36.1](https://github.com/The-PR-Agent/pr-agent/releases/tag/v0.36.1) credential-exposure mitigation; Jun 23 [Qodo 2.4](https://www.qodo.ai/blog/introducing-qodo-2-4-the-next-layer-of-code-quality-governance/) and [Cross Repo Review](https://www.qodo.ai/blog/the-anatomy-of-a-breaking-change/) (same beta); Jun 30 [independent-verification editorial](https://www.qodo.ai/blog/why-your-ai-coding-agent-shouldnt-review-its-own-code-the-case-for-an-independent-verification-layer/); Jun 30 Qodo 2.5 (changelog) | Qodo 2.4 features are **Beta** (status corrected 2026-10-16); changelog dates 2.4 to 16 Jun vs blog 23 Jun |
| July (3) | Jul 5 [PR-Agent v0.39.0](https://github.com/The-PR-Agent/pr-agent/releases/tag/v0.39.0) (AGENTS.md by default, SKILL.md); Jul 9 LICENSE Apache→MIT commit; Jul 28 [Review Effort Modes](https://www.qodo.ai/blog/the-right-depth-for-every-pr-introducing-review-effort-modes/) research preview | Git dates unauthenticated; effort modes not GA |
| August (4) | Aug 16 Qodo 2.8 Agentic Toolbox **Beta** (changelog); Aug 22 [PR-Agent v0.43.0](https://github.com/The-PR-Agent/pr-agent/releases/tag/v0.43.0) PyPI restored; Aug 27 [steering editorial](https://www.qodo.ai/blog/how-do-you-efficiently-steer-ai-coding-agents/); Aug 30 [PR-Agent v0.44.0](https://github.com/The-PR-Agent/pr-agent/releases/tag/v0.44.0) webhook-secret hardening | Editorial cites mixed external studies; not a trial |
| September (6) | Sep 7 Qodo 2.9 — Agentic Toolbox **GA**, legacy v1 commands removed Oct 1 (changelog); Sep 8 [qodo-skills v2.0.0](https://github.com/qodo-ai/qodo-skills/releases/tag/v2.0.0); Sep 9 [Agentic Toolbox](https://www.qodo.ai/blog/introducing-qodos-agentic-toolbox/) and [Qodo for Codex](https://www.qodo.ai/blog/introducing-qodo-for-codex/); Sep 15 [Software Map beta](https://www.qodo.ai/blog/introducing-qodos-software-map/); Sep 23 [vendor survey](https://www.qodo.ai/blog/state-of-ai-code-quality-report-2026/) | Survey is vendor-commissioned (Censuswide, 500 devs + 300 leaders, U.S.) |
| Oct 1–12 (5) | Oct 1 [Qodo 3.0](https://www.qodo.ai/blog/introducing-qodo-3-0/) and [CEO direction post](https://www.qodo.ai/blog/what-every-software-factory-needs-that-no-model-will-provide/); Oct 2 [PR-Agent v0.47.0](https://github.com/The-PR-Agent/pr-agent/releases/tag/v0.47.0); Oct 5 [Jev evaluation](https://www.qodo.ai/blog/does-jev-make-ai-code-review-more-efficient/); Oct 12 [model benchmark](https://www.qodo.ai/blog/which-llm-should-review-your-code/) | PR Triage Research Preview; analytics dashboard Beta; benchmark proprietary |

See the [CSV](018-qodo.events.csv) for all 30 rows. `event_date_utc` is blank throughout: no source establishes a rollout date distinct from publication. Multiple rows cite the single living [docs changelog](https://docs.qodo.ai/changelog); each is one dated entry.

## 4. Feature and capability map

| Capability cluster | Status in cited sources | Reuse/integration surface | Non-equivalence |
|---|---|---|---|
| PR review engine (Git apps: GitHub, GitLab, Bitbucket, Azure DevOps, Gerrit) | Shipped platform; Gerrit parity in 3.0 | Git-provider apps, on-prem | Vendor precision/recall claims are self-benchmarked |
| Findings Page / analytics dashboard | Beta (May 13; dashboard Beta in 3.0) | Portal | Findings are automated reports, not adjudicated defects |
| Cross Repo Review → automatic discovery → Software Map / Blast radius | Beta (Jun 16/23), Beta (Jun 30), Beta (Sep 15), Research Preview (Sep 7) | Portal; context for review agents | No accuracy data; one cross-repo beta event, not two |
| Rules system: Rules Miner, Skill Review Standards, mined patterns | Beta (Jun) | Rules/skills tab; `qodo-get-rules` skill | Mined rules may encode past mistakes; no evaluation |
| Review Effort Modes (Fast/Balanced/Deep/Auto) | Research Preview (Jul 28) → Beta (Sep 7) | Review setting | Not GA; cost reduction unvalidated |
| Agentic Toolbox (Claude Code, Codex, Kiro, MCP clients) | Beta (Aug 16) → GA (Sep 7) | MIT `qodo-skills` + proprietary CLI/service | Data egress and permissions not audited |
| PR Triage, PR Insights, spec/design-review agents, web search | Research Preview | Portal | Preview only |
| Code generation (autocomplete/chat) | Deprecated (announced Apr 23); IDE plugin retirement Oct 30 per undated docs notice | — | Removal timing unresolved |
| PR-Agent OSS (community) | 19 GitHub releases in window; MIT since Jul 9 commit | Self-hosted CLI, GitHub Action, Docker, PyPI (restored Aug 22) | Separate project; Qodo's hosted product is not PR-Agent |

## 5. Publicly stated direction versus shipped functionality

| Dated first-party source | Stated intention | Classification |
|---|---|---|
| [Apr 23 code-generation update](https://www.qodo.ai/blog/an-update-on-code-generation-at-qodo/) | Exit code generation, arguing (paraphrase) that the tool that writes code should not also verify it; may re-enter later | Deprecation announced; IDE plugin retirement date (Oct 30) only on an undated docs page |
| [Apr 23 PR-Agent handover](https://www.qodo.ai/blog/qodo-is-handing-pr-agent-over-to-the-community/) | Community governance, return to Apache-2.0, possible foundation later | Apache-2.0 executed (May 20 commit), then superseded by MIT (Jul 9); foundation move not observed |
| [Sep 15 Software Map](https://www.qodo.ai/blog/introducing-qodos-software-map/) | Add reviewer findings to heat map; later per-connection risk scoring | Announced only |
| [Oct 1 CEO post](https://www.qodo.ai/blog/what-every-software-factory-needs-that-no-model-will-provide/) | Be the independent quality layer of the "agentic software factory" built on a codified "wisdom base" | Strategy rhetoric; no dated deliverable |
| Oct 6 "Dark Factory" post (excluded row; [search log](018-qodo.search-log.md)) | Internal SWE/Reviewer/SRE agent team; "designing for engineering organizations more broadly" | Internal system, no availability |

**Shipped vs stated pattern:** most in-window Qodo features reached users as Beta or Research Preview; the only explicit GA label in the window is the Agentic Toolbox (Sep 7 changelog). Vendor posts dated after the changelog sometimes describe a feature as new a week after the changelog entry (Qodo 2.4).

## 6. Conditional 2027–2031 outlook (analyst hypotheses, not company statements)

| Hypothesis | Rival explanation | Disconfirming observation |
|---|---|---|
| Separating generation from verification (different vendor/model for review) catches more defects per reviewer minute | Same-model review with good tests is equally effective; separation mostly adds cost | Seeded-defect trials show no recall gain at equal reviewer time |
| Permissive relicensing (AGPL→Apache→MIT) increases third-party reuse/contribution to PR-Agent | Contributor growth is driven by model-support churn and the handover itself | Contributor and downstream-dependency counts flat or falling after Jul 9 versus before |
| Rule/skill packages (`AGENTS.md`, `SKILL.md`, Qodo rules) become a portable governance layer across agents | Instruction files have weak, mixed effects (cited by Qodo's own Aug 27 post) | Controlled tasks show no acceptance gain from repo rules versus none |

## 7. M1–M7 study relevance

| Construct | Observation from this screen | Prospective measurement |
|---|---|---|
| **M1** agent workflow | Shift from generation to verification; Toolbox plugs into Claude Code/Codex/Kiro | Opt-in records of agent + independent-review workflows |
| **M2** accepted quality | Only vendor benchmarks (Oct 12) and a small vendor DevRel evaluation (Oct 5) | Independently frozen seeded/backtracked defects; count all attempts |
| **M3** discovery | Install wizards, onboarding presets | Time-to-first-accepted-review for newcomers |
| **M4** verified third-party reuse | PR-Agent community releases; PyPI gap and restore | Traced downstream installs with consent; not stars (13.4k) |
| **M5** reuse-first / rights | Licence history AGPL→Apache→MIT; MIT skills over proprietary runtime | Commit-pinned licence + dependency audit before reuse |
| **M6** lifecycle cost | Vendor reports >100x cost spread across models; breaking webhook/CI changes in PR-Agent | Measured review minutes, CI time, upgrade effort; **no token-to-CO2e conversion** |
| **M7** maintainer interventions | Fail-closed webhooks and Action errors (v0.44/v0.47) | Test whether fail-closed defaults reduce silent failures without raising support load |

## 8. One falsifiable reuse-first maintainer experiment (not executed)

**Repository:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study), offline only, using the synthetic [parser fixture](../../../tests/fixtures/trending.html) and the existing unit suite. No live GitHub Trending collection.

**Reusable practice:** reuse **PR-Agent pinned at a specific commit** (re-read that commit's `LICENSE`; MIT at `330f0813…`) in read-only, non-blocking mode, instead of building a custom review bot.

**Comparator:** A = existing human review + unit tests; B = A plus the pinned PR-Agent `/review` output on the same patches, with the repo's `AGENTS.md` either included (v0.39.0 default) or excluded (`repo_context_files = []`) as a secondary factor.

**Task acceptance test:** before any run, a non-author freezes 12 synthetic patches (8 with seeded defects in parser/CLI code, 4 clean) and hidden acceptance tests. Primary endpoint: defects caught before merge / all seeded defects, at equal reviewer time; secondary: false-positive comments, reviewer minutes, CI minutes, LLM spend if billed.

**Verified external-use signal:** none expected; a downstream reuse claim requires a consented third party running the same pinned configuration.

**Cost cap and stop rule:** ≤ 4 maintainer hours and a fixed LLM budget; stop if any credential is exposed to the tool, the licence/dependency audit is unclear, false positives exceed true positives, or B shows no gain in defects caught. The plausible outcome "no improvement" must be preserved.

## 9. Limitations

- All Qodo evidence is first-party (blog, docs changelog); PR-Agent evidence is maintainer-authored GitHub metadata. No neutral audit, no independent journalism in window found, no task test.
- Living pages (changelog, docs) have no archived captures; the IDE-plugin retirement notice is undated.
- Benchmarks (Oct 12) and survey (Sep 23) are vendor-produced; no figure from them is admitted as evidence.
- Git dates are unauthenticated; dependency licences, packaged-release licences and governance were not audited.
- 3 WebSearch calls only (shared budget); 5 planned queries not executed (see [search log](018-qodo.search-log.md)).
- Duplicate events: `CI-018-03` / `CI2026-018-001` (one cross-repo beta); Agentic Toolbox appears in `CI2026-018-016` (Beta), `-019` (GA), `-003` (blog), `-020` (skills release) as stages of one capability.

---

## Earlier screen (preserved)

The previous canonical version (merged 2026-10-15) was a 13-row "PROVISIONAL INITIAL EVIDENCE SCREEN" adapted from closed PR [#213](https://github.com/MSKazemi/github-trending-1000-study/blob/4425557fbb54f8e137dfa69afbfa4cb94dbc9e48/research/company-intelligence/2026-04-12_2026-10-12/source-archives/018-qodo.2026-10-12-pr-213-original-report.md), with material from closed PR [#198](https://github.com/MSKazemi/github-trending-1000-study/pull/198), draft PR [#232](https://github.com/MSKazemi/github-trending-1000-study/pull/232) and the preservation PR [#300](https://github.com/MSKazemi/github-trending-1000-study/pull/300). Full texts live in git history and the archives: [PR #198 original report](source-archives/018-qodo.2026-10-12-pr-198-original-report.md), [PR #213 original report](source-archives/018-qodo.2026-10-12-pr-213-original-report.md), [first-pass JSON](source-archives/018-qodo.2026-10-12-first-pass.events.json), [first-screen Markdown](source-archives/018-qodo.2026-10-13-first-screen.md), [original 22-column ledger](source-archives/018-qodo.2026-10-12-source-ledger.csv), [event-ID crosswalk](source-archives/018-qodo.2026-10-14-event-id-crosswalk.json) (guarded by [this offline test](../../../tests/test_qodo_event_id_crosswalk.py)), the [five-company no-loss crosswalk](../../../research-notes/five-company-no-loss-crosswalk-2026-10-14.md) and the [Qodo PR/source crosswalk](../../../research-notes/qodo-no-loss-pr-source-crosswalk-2026-10-13.md). It also referenced [news corpus issue #56](https://github.com/MSKazemi/github-trending-1000-study/issues/56); no #56 news IDs have been minted from this screen.

**What it claimed (summary):** Qodo was shifting from general-purpose generation to code-review governance, cross-repository context and reviewable work packages; six original E1 vendor events (code-generation direction, PR-Agent handover, Qodo 2.4 marked `shipped`, Agentic Toolbox, Software Map `preview`, Qodo 3.0 `shipped`); the archived Qodo 3.0 URL `introducing-qodo-3.0/` was corrected to `-3-0/`; seven later vendor leads (Cross Repo Review, Review Effort Modes, State of AI Code Quality survey, Findings Page, steering editorial, Qodo for Codex, and the #198 lead `018-E01`); months May, July and August were originally "not documented". The 2026-10-16 upgrade keeps all 13 event IDs, corrects Qodo 2.4 to `preview`, and fills every month.

**PR-Agent licence contradiction (2026-10-13, preserved):** the April 23 announcement said Apache-2.0, while [the live repository](https://github.com/The-PR-Agent/pr-agent) `main` [LICENSE](https://github.com/The-PR-Agent/pr-agent/blob/main/LICENSE) read MIT (blob `43fff0c98b18eba319298a18dae01a57ba0eac97`). This was resolved on 2026-10-15 by the commit history below, not by treating the announcement as wrong.

**Independent commentary lead (2026-10-15, preserved):** [TT Lab commentary](https://ttlab.hopto.org/blog/2026-07-17-ai-code-review-measured-evidence?lang=en), dated July 17, 2026, no named author, dynamic-DNS host, critiques LLM-injected defects and LLM-judge scoring in vendor review benchmarks. Still an unvetted lead; **no statistic admitted**; not re-read on 2026-10-16.

### Provisional-merge spot check — 2026-10-15 (AI-assisted; not independent human review)

On 2026-10-15 the Findings Page (May 13, v2.3 beta), Review Effort Modes (Jul 28, research preview), Qodo for Codex (Sep 9, Codex marketplace) and the State of AI Code Quality survey (Sep 23, Censuswide 500 + 300) were re-read and matched; all were re-confirmed on 2026-10-16 ([QC note](018-qodo.source-qc-2026-10-16.md)). The `LICENSE` history of The-PR-Agent/pr-agent showed commit [`fdbcecc`](https://github.com/The-PR-Agent/pr-agent/commit/fdbcecc8cdd9c276919cd9b8f41c981e8ca642ef) (Git date 2026-05-20, "From GNU AGPL v3.0 to Apache License 2.0") and commit [`d7e94bc`](https://github.com/The-PR-Agent/pr-agent/commit/d7e94bc27a8ad0456090a07e075cecd6e6459626) (Git date 2026-07-09, "From Apache-2.0 to MIT"). `CI-018-06` keeps a platform-level `shipped` label with PR Triage recorded as Research Preview.
