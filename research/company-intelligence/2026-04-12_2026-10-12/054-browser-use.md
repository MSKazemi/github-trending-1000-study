# Browser Use — provisional six-month technology intelligence screen (054)

> **Provisional source-lead screen (2026-10-16):** this report, its [event ledger](054-browser-use.events.csv) and [search log](054-browser-use.search-log.md) are **provisional, AI-assisted documentary source leads**. They are **unreviewed by a qualified human**; factual/link review, source-access/rights review and methods review remain **pending**. Committing them is not scientific or security sign-off; issue #121 was closed on maintainer instruction (2026-10-16) with these review gates still open; reopen it if review finds a defect.

- **Watchlist:** 054; [issue #121](https://github.com/MSKazemi/github-trending-1000-study/issues/121). Sector in the issue: agent execution environments, observability and evaluations. Study angle: open browser automation, grounded test outcomes.
- **Window:** 2026-04-12 through 2026-10-12 inclusive; **source-screened on 2026-10-16**. Exact UTC search-run times, full result counts, immutable page snapshots and an independent reviewer are unavailable.
- **Status:** **provisional dated documentary screen (26 traceable source leads covering all seven calendar segments); not reviewed by a qualified human; factual/link, source-access/rights and methods review pending**. Not independently verified task outcomes, exhaustive retrieval or human-approved scientific completion. [Event ledger](054-browser-use.events.csv), [month-segment queries and inclusion/exclusion log](054-browser-use.search-log.md), [study method](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md).
- **Official sources checked:** [Browser Use](https://browser-use.com/), [changelog](https://browser-use.com/changelog), [blog index](https://browser-use.com/posts), [OSS repository](https://github.com/browser-use/browser-use) and its [GitHub releases](https://github.com/browser-use/browser-use/releases), the [repository security advisories](https://github.com/browser-use/browser-use/security/advisories), [browser-harness](https://github.com/browser-use/browser-harness), [benchmark](https://github.com/browser-use/benchmark) and [docs](https://docs.browser-use.com/). **Claim grading** uses company-watch E0–E4 tiers, not the separate [2027 lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md).

## 1. Discovery, coverage and exclusions

The [search log](054-browser-use.search-log.md) covers all seven segments. The vendor's own dated channels were the most productive: the dated blog index, the dated changelog (in-window entries 2026-04-12, 07-01, 07-17, 07-20, 08-10, 08-17, 08-24; **no changelog entry after 2026-08-24 was shown** when read on 2026-10-16) and GitHub releases 0.12.7 to 0.13.11 retrieved through the GitHub REST API. Independent reporting was **sparse**. Searches found no in-window TechCrunch/Register/VentureBeat/Verge coverage, no in-window funding or acquisition report, and no in-window GitHub-reviewed advisory for the `browser-use` package. The one independent in-window item retained is a Hacker News Show HN thread (2026-04-24). The web-search budget for this session ran out before a planned academic/independent-benchmark query (see log). Independent coverage is therefore **under-searched, not shown to be absent**.

First-party pages are good evidence of what Browser Use *said* and when. They are not evidence of quality, adoption or security effectiveness. Customer stories (Composio, Vesta, both 2026-09-21) are noted in §4 and excluded from the ledger as vendor-hosted testimonials. Marketing listicles and glossaries (2026-10-01, 10-06, 10-07, 10-12) are excluded. Out-of-window items are excluded: the 2026-04-03 free tier/pricing changelog entry, the 2026-04-09 free-tier post, the 2026-10-15 Firecrawl comparison, the 2025-05 `allowed_domains` advisory (GHSA-x39x-9qw5-ghrf / CVE-2025-47241) and the 2025-12 `bu-30b-a3b-preview` open-weights model.

## 2. Corporate/product identity and rights baseline

- **Entity:** "Browser Use". The homepage footer shows only "© 2026 Browser Use", with no registered legal name or jurisdiction (read 2026-10-16). Blog bylines name Gregor Zunic as co-founder and CTO. The company's own [2025-03-22 post](https://browser-use.com/posts/seed-round) is titled "We Raised $17M to Build the Future of Web for Agents". This is **pre-window baseline**, and the round was not re-verified at filing level. **No in-window acquisition, rename or parent change was found.** Search results are not proof that none occurred, so ownership is **unverified at filing level**.
- **Offerings (as read 2026-10-16):**
  - the MIT-licensed Python library [browser-use/browser-use](https://github.com/browser-use/browser-use) (GitHub API `license: MIT`, created 2024-10-31);
  - **Browser Use Cloud**: hosted agents, stealth remote browsers and an LLM gateway, proprietary and paid;
  - in-house models (`ChatBrowserUse`, `bu-2-0`);
  - **Browser Harness**, MIT, created 2026-04-17.
- **Rights caveats:** MIT covers the library and harness code only. It does not cover the hosted Cloud, the stealth Chromium fork or fingerprint pool, which are not shown to be open. The [benchmark repository](https://github.com/browser-use/benchmark) has **no LICENSE file** (GitHub API `license: none`), and its README asks users not to publish decrypted tasks. Reuse rights for the benchmark data are **unclear** and need a rights review before any study use.
- **Name collision:** Anthropic documents its own client-side ["Browser use tool"](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool) (`browser_toolset_20260801`). It is a distinct product, and that page does not name Browser Use the company. Browser Use 0.13.11 ships a driver for it (CI2026-054-026). Searches and future coders must not merge the two.

## 3. Seven-segment dated chronology

| Period | In-window source evidence (source publication dates) | Availability and attribution limits |
|---|---|---|
| Apr 12–30 | [Apr 12 changelog: BYOK, Code Mode, sensitive data](https://browser-use.com/changelog); [Apr 19 Browser Harness post](https://browser-use.com/posts/bitter-lesson-agent-harnesses) (repo created Apr 17); [Apr 24 Show HN thread](https://news.ycombinator.com/item?id=47890841); [Apr 25 BUX launch](https://browser-use.com/posts/bux-launch-blog) | Apr 12 is the inclusive first day. The Apr 3 pricing entry and the Apr 9 free-tier post are **excluded** as pre-window. The Apr 13 reverse-CAPTCHA experiment post is excluded as non-product (retired experiment) |
| May | [May 9 production architecture for the OSS library](https://browser-use.com/posts/production-architecture-browser-use); [May 19 v0.12.7 security hardening](https://github.com/browser-use/browser-use/releases/tag/0.12.7); [May 23 v0.12.8 with reverts](https://github.com/browser-use/browser-use/releases/tag/0.12.8) | The v0.12.8 restricted-profile `evaluate()` guard was **reverted in the same release**. This is a negative/rollback record |
| June | [Jun 8 v0.13.0 Rust-backed beta agent](https://github.com/browser-use/browser-use/releases/tag/0.13.0); [Jun 10 BU Bench V1 score post](https://browser-use.com/posts/claude-fable-browser-agent-benchmark); [Jun 15 Firecracker microVM browsers](https://browser-use.com/posts/firecracker-browser-infra) | The Rust agent is **beta**. Benchmark and cost figures are self-measured |
| July | [Jul 1 CLI 3.0 / v0.13.3](https://github.com/browser-use/browser-use/releases/tag/0.13.3); [Jul 1 QA skill post](https://browser-use.com/posts/qa-automation-ai-agents); [Jul 12 AgentCore sandbox migration](https://browser-use.com/posts/agentcore-migration); [Jul 17 Browser Harness v4 API public](https://browser-use.com/changelog) | The Jul 1 changelog and v0.13.3 release are **one event**. The Jul 20 recording-controls changelog was read but not itemised. Default recording is *off* for API calls and *on* for UI sessions |
| August | [Aug 5 judge-variance methods post](https://browser-use.com/posts/benchmark-behind-the-benchmark); [Aug 6 x402 crypto payments](https://browser-use.com/posts/x402-launch); [Aug 16 v0.13.8 default model switch](https://github.com/browser-use/browser-use/releases/tag/0.13.8) (reversed Sep 4); [Aug 17 scheduled agents + Agency approval skill](https://browser-use.com/changelog); [Aug 24 BYOK billing correction](https://browser-use.com/changelog); [Aug 26 BU Bench V2 commit](https://github.com/browser-use/benchmark/commit/04c0423bf1af87350c486506c085f4de98116f2a); [Aug 26 RL-environment rubric post](https://browser-use.com/posts/long-horizon-rl-environments) | The Aug 10 session-sharing/usage changelog was read but not itemised. The two Aug 26 sources share duplicate group 054-020 |
| September | [Sep 3 Stripe Link payments](https://browser-use.com/posts/pay-with-link); [Sep 4 v0.13.10 exact-pinned deps](https://github.com/browser-use/browser-use/releases/tag/0.13.10); [Sep 15 "Bitter Lesson of Browser Agents"](https://browser-use.com/posts/bitter-lesson-browser-agents); [Sep 24 correction of seven BU Bench V2 cases](https://github.com/browser-use/benchmark/commit/cc09d941feb5ad2e103c99af6b4792305ac5d3ec) (V2.1 metadata Sep 25) | Composio/Vesta customer stories (Sep 21) are vendor-hosted testimonials, **not ledger events** |
| Oct 1–12 | [Oct 7 v0.13.11 Claude toolsets driver](https://github.com/browser-use/browser-use/releases/tag/0.13.11) | At release, the release note says the required Anthropic SDK was **not yet public**. The Oct 1/6/12 posts are SEO/listicle content and excluded. The [Oct 15 Firecrawl comparison](https://browser-use.com/posts/browser-use-vs-firecrawl) is **out-of-window** |

See the [CSV](054-browser-use.events.csv) for **26 dated source records**: Apr 4, May 3, Jun 3, Jul 4, Aug 7, Sep 4, Oct 1. This is a purposive selection of material events, not every release or post, and not a rate of innovation. GitHub release `published_utc` values come from the GitHub REST API `published_at` field. Blog and changelog dates are the displayed page dates. `event_date_utc` is filled only where a repository timestamp gives a distinct same-day artifact date. An `independent_check_url` pointing to another Browser Use page is *documentary corroboration*, not neutral E3 evidence.

## 4. Feature, rights and security cross-check

| Evidence cluster | What the cited document supports | Important non-equivalence or counterexample |
|---|---|---|
| [Browser Harness](https://browser-use.com/posts/bitter-lesson-agent-harnesses) → [CLI 3.0](https://github.com/browser-use/browser-use/releases/tag/0.13.3) → [v4 API](https://browser-use.com/changelog) | The vendor moved from a fixed action set to raw-CDP, agent-editable helpers, then exposed the same harness as CLI, coding-agent skill and hosted API | Agent-edited helper code is an unreviewed-code surface. The [Show HN](https://news.ycombinator.com/item?id=47890841) thread raises auditability and prompt-injection concerns. No independent safety evaluation was found |
| [v0.12.7](https://github.com/browser-use/browser-use/releases/tag/0.12.7), [v0.12.8](https://github.com/browser-use/browser-use/releases/tag/0.12.8), [v0.13.10](https://github.com/browser-use/browser-use/releases/tag/0.13.10) | Daemon-socket auth token and owner-only permissions, download/upload path containment, IP-blocklist canonicalisation, redaction-order fix, CVE dependency bumps, exact-pinned dependencies | No in-window GitHub-reviewed advisory exists for `browser-use`, so the hardening is **not** paired with disclosed vulnerabilities. A Show HN commenter alleged an unanswered private RCE report. This is **unverified (E0)**, and no link to these fixes is established |
| [Firecracker](https://browser-use.com/posts/firecracker-browser-infra) and [AgentCore](https://browser-use.com/posts/agentcore-migration) posts | Per-session microVM isolation, a private VPC, allowlisted egress, no secrets on the VM (vendor description) | No audit or pen-test is cited. The post cites a #1 BrowserArena ranking at $0.02/hr. The undated [Notte-operated Browser Arena page](https://notte.cc/arena), read 2026-10-16, lists Browser Use **rank 6, 99.0% reliability, 4,538 ms, $0.06/hr**. Both sources are interested parties, and snapshot timing is unknown. Treat this as **unresolved contrary evidence** |
| [BU Bench V1](https://browser-use.com/posts/claude-fable-browser-agent-benchmark), [judge variance](https://browser-use.com/posts/benchmark-behind-the-benchmark), [V2](https://github.com/browser-use/benchmark/commit/04c0423bf1af87350c486506c085f4de98116f2a) / [V2 correction](https://github.com/browser-use/benchmark/commit/cc09d941feb5ad2e103c99af6b4792305ac5d3ec) | Public rerunnable runner with encrypted tasks. The vendor discloses that 11 judges on identical runs spanned **62.5%–83.7%**. Seven V2 tasks needed contract corrections | This is strong *self-disclosed* evidence that LLM-judged "success" is fragile. Headline benchmark numbers are not grounded acceptance outcomes. There is no license file, and encrypted tasks limit public audit |
| [QA skill](https://browser-use.com/posts/qa-automation-ai-agents) | An agent explores the app and returns a 1–5 rubric score with evidence | A rubric score is **not** a deterministic acceptance test. No false-pass/false-fail rate is reported |
| [x402](https://browser-use.com/posts/x402-launch), [Stripe Link](https://browser-use.com/posts/pay-with-link), [Agency skill](https://browser-use.com/changelog) | Agent-initiated payments. Link requires per-purchase human approval and single-use cards. Agency asks approval before external actions | Approval-gate coverage and bypass resistance are undocumented. x402 spending controls are not described beyond a CLI cap example |
| [v0.13.8](https://github.com/browser-use/browser-use/releases/tag/0.13.8) → [v0.13.9](https://github.com/browser-use/browser-use/releases/tag/0.13.9) | The default `ChatBrowserUse` model switched to a preview "mini" model, then reverted after about 19 days | Unpinned users silently got different agent behaviour. This is a reproducibility hazard and argues for pinning model IDs in tests |
| [v0.13.11 Claude toolsets](https://github.com/browser-use/browser-use/releases/tag/0.13.11) | Driver for Anthropic's browser toolset | The release note says it needed a then-unpublished Anthropic SDK. Functional availability is undetermined |

## 5. Publicly stated direction versus shipped functionality

| Dated first-party source | Company-stated direction (paraphrase) | Current research classification |
|---|---|---|
| [Apr 19 harness post](https://browser-use.com/posts/bitter-lesson-agent-harnesses) | "Don't wrap the LLM. Don't wrap its tools either." Give models raw CDP and self-editable helpers | Shipped as OSS code. Effectiveness claims are **untested** independently |
| [Jun 8 v0.13.0](https://github.com/browser-use/browser-use/releases/tag/0.13.0) | Rust-backed agent offered as beta alongside the unchanged Python agent | **Beta/preview**. No GA date was stated |
| [Jun 15 Firecracker post](https://browser-use.com/posts/firecracker-browser-infra) | The next optimisation is snapshotting after Chromium is running | **Planned/announced only** |
| [Sep 15 bitter-lesson post](https://browser-use.com/posts/bitter-lesson-browser-agents) | Reuse proven coding-agent harnesses plus a simple browser tool. "As models change, rethink the harness." | **Direction statement** without a dated roadmap. Supported by a single 18-run vendor case |
| [Homepage](https://browser-use.com/) (read 2026-10-16) | "SUPERFAST mode" waitlist banner | **Announced/waitlist only**. Undated, not ledgered |

A stated intention is not a scheduled delivery. These statements do not establish Browser Use's 2027–2031 strategy.

## 6. Conditional 2027–2031 outlook (analyst hypotheses, not company statements)

| Testable analyst scenario | Rival cause | Disconfirming observation |
|---|---|---|
| Thin raw-CDP harnesses reused inside general coding agents may displace bespoke browser-action frameworks | Model vendors' own browser/computer-use toolsets (e.g. Anthropic's) may absorb the layer | Fixed-task comparisons show no accepted-task gain or higher review burden versus Playwright scripts or vendor toolsets |
| Judge-variance disclosure may push browser-agent evaluation toward rubric + frozen-trace + deterministic checks | Marketing incentives keep single headline scores | Next-version public benchmarks still report single-judge percentages without variance |
| Agent payments (x402/Link) may normalise approval-gated autonomous purchasing | Fraud/abuse and regulation may restrict it | Feature withdrawals, incident reports or narrowed availability |

## 7. M1–M7 study relevance (definitions per [mission](../../../docs/AI_ERA_CODING_REUSE_RESEARCH_MISSION.md))

| Construct | Prospective measurement, not inferred conclusion |
|---|---|
| **M1** coding-workflow change | Dated chronology of browser control being packaged as *skills for coding agents* (Jul 1 CLI 3.0 skill install, QA skill). Availability is not adoption |
| **M2** accepted task quality / review cost | Compare LLM-judged QA scores against deterministic, independently authored acceptance tests on the same UI tasks, including all failed/timed-out runs. The vendor's own judge spread (62.5–83.7%) is the motivating hazard |
| **M3** discovery | Only observational: README/llms.txt and skill-registry distribution changes (v0.13.11 docs). Stars and downloads on the homepage are **not** verified use |
| **M4** verified third-party reuse | Trace one consented downstream integration (e.g. a project that pins `browser-use` and runs it in CI) rather than citing vendor customer stories |
| **M5** reuse-first | Existing Playwright test suites vs browser-use/Browser Harness vs a minimal new script, under the same frozen task |
| **M6** lifecycle human and energy cost | Measure setup/review/flake-triage minutes, API spend and CI runtime where instrumented. **No token-to-energy or CO2e conversion.** The vendor's "60–66% fewer tokens" is not an energy result |
| **M7** actionable interventions | Test whether adding a pinned-model, deterministic-assertion browser smoke test to a repo's CI improves independently verified first-use success. Preregistered and opt-in only |

## 8. One falsifiable maintainer experiment

**Target:** a maintainer repository with a small web UI or documentation site (or a local synthetic fixture app). **Not** GitHub Trending pages: the study's live `capture` is disabled under the source-access decision, and no browser-agent tool makes unapproved scraping permissible.

**Question (reuse-first):** for UI smoke-testing, does adding an LLM browser agent beat reusing a conventional deterministic Playwright test, once acceptance is grounded?

- **Frozen functional unit:** 10 fixed user tasks on a pinned local build of the app, for example "submit the form with valid input and see confirmation X". Include **3 deliberately broken builds** (seeded defects) and **2 tasks with no valid completion path**. Hidden pass/fail assertions are written by someone other than the agent operator before any run.
- **Comparator A (reuse baseline):** a hand-written Playwright test per task, which reuses existing tooling.
- **Comparator B:** `browser-use` pinned to an exact version and an exact LLM model ID (never the library default, given the v0.13.8→0.13.9 default reversal), run locally with the same tasks and **graded only by the hidden deterministic assertions**, not by its own judge.
- **Primary endpoint:** independently accepted correct verdicts / **all** task × build cells, counting timeouts, refusals and crashes as failures. Report false-pass on seeded-defect builds separately.
- **Secondary endpoints:** maintainer authoring and triage minutes, flake rate over 5 reruns, API spend, CI wall-time. Report energy only if actually metered; never estimate it from tokens.
- **Guardrails:** no real credentials, no logged-in personal profiles, no network access beyond the local app, MIT license check of the pinned versions, and dependency audit of the pinned lockfile.
- **Stop rule:** stop and keep Playwright if B's false-pass rate on seeded defects exceeds A's, if any secret or out-of-scope network access occurs, or if B's maintainer minutes per accepted task exceed A's after 2 iterations. The result may be **no improvement**; record it.
- **Status:** **No trial executed, no effects estimated.**

## 9. Evidence quality, alternative outcomes and release checklist (2026-10-16)

- **Dated source inventory:** 26 CSV records across all seven segments. This is a purposive evidence screen, not a product census or representative sample. Most rows are **E1/E2 first-party** sources. One row is an **E0** community lead (Show HN). No E3/E4 independent validation was found.
- **Negative and corrective records kept:**
  - v0.12.8 in-release revert;
  - v0.13.8 default-model change reversed in v0.13.9;
  - Aug 24 BYOK billing correction;
  - Sep 24 correction of seven benchmark task contracts.
- **Contradictions:** the vendor's BrowserArena claim (Jun 15) conflicts with an undated Notte-operated leaderboard, and timing is unresolved. The vendor also reports a 21-point judge spread that undercuts its own single-score benchmark headline (Jun 10).
- **Unknowns:**
  - legal entity, ownership and funding at filing level;
  - whether the HN-alleged RCE report exists or was fixed;
  - independent security assessment of Cloud isolation;
  - real adoption (homepage star and download figures are not verified use);
  - benchmark data license;
  - Anthropic SDK availability for the v0.13.11 toolsets;
  - complete search hit counts.
- **Pending:**
  - human factual/link spot-check of sampled rows (especially release-note paraphrases and blog numbers);
  - source-access/rights review (benchmark has no license; encrypted tasks);
  - independent methods review;
  - any real opt-in task comparison.

**Issue #121 was closed on maintainer instruction (2026-10-16); this screen alone is not scientific completion — reopen it if factual, rights or methods review finds a defect.** on the basis of this screen.
