# Browserbase — provisional six-month technology intelligence screen (053)

> **Provisional source-lead screen (2026-10-16):** this report, its [event ledger](053-browserbase.events.csv) and [search log](053-browserbase.search-log.md) are **provisional, AI-assisted documentary source leads** for [issue #120](https://github.com/MSKazemi/github-trending-1000-study/issues/120). They are **unreviewed by a qualified human**; factual/link review, source-access/rights review and methods review remain **pending**. This screen is not scientific or security sign-off; issue #120 was closed on maintainer instruction (2026-10-16) with these review gates still open; reopen it if review finds a defect.

- **Watchlist:** 053; [issue #120](https://github.com/MSKazemi/github-trending-1000-study/issues/120). Sector: agent execution environments, observability and evaluations. Study lens: **reproducible browser-agent testing**.
- **Window:** 2026-04-12 through 2026-10-12 inclusive; **source-screened on 2026-10-16**. Exact UTC search-run times, full search result counts, immutable page snapshots and an independent reviewer are unavailable.
- **Status:** **provisional dated documentary screen (25 traceable source leads covering all seven calendar segments); not reviewed by a qualified human; factual/link, source-access/rights and methods review pending**. These are not independently verified task outcomes, exhaustive retrieval or human-approved scientific completion. See the [event ledger](053-browserbase.events.csv), the [month-segment queries and inclusion/exclusion log](053-browserbase.search-log.md) and the [study method](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md).
- **Official sources checked:** [Browserbase](https://www.browserbase.com/), [changelog](https://www.browserbase.com/changelog), [blog index and pages 1–5](https://www.browserbase.com/blog), [Stagehand repository](https://github.com/browserbase/stagehand) (releases, release PRs, commits via the GitHub API), [browserbase/skills](https://github.com/browserbase/skills), and the [npm registry record for @browserbasehq/stagehand](https://registry.npmjs.org/@browserbasehq/stagehand). **Claim grading** uses company-watch tiers E0–E4, not the separate [2027 lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md).

## 1. Discovery, coverage and exclusions

The [search log](053-browserbase.search-log.md) covers all seven partial/full month segments. It records 11 web searches that were actually run, 2 planned searches that were **not executed** because the session's web-search budget ran out, and direct reads of official pages, GitHub API records, the npm registry, the CVE Program and NVD APIs, arXiv and three secondary news pages. **This is not exhaustive internet discovery.** Search result totals and screened-result denominators are recorded as **unknown**, not zero.

Two coverage limits matter. First, the public changelog page rendered only 12 entries, from **2026-07-15 onward**. Earlier 2026 changelog entries were not visible, so April–June product coverage relies on blog posts, GitHub releases and npm. Whether the changelog had April–June entries is **unknown**. Second, independent trade-press coverage was thin. The searches surfaced no TechCrunch, Reuters, The Register or InfoQ article about Browserbase dated in the window. The secondary items found ([ByteIota, 2026-08-14](https://byteiota.com/stagehand-v4-browser-agent-sdk-now-2x-faster/); [RuntimeWire, 2026-07-06](https://runtimewire.com/article/browserbase-agents-one-call-browser-agent-api)) repeat vendor claims without testing them. They are recorded as `independent_check_url` corroboration of *publication*, not of performance.

## 2. Corporate/product identity and rights baseline

[Browserbase](https://www.browserbase.com/) sells hosted headless-browser infrastructure for AI agents: cloud browser sessions, Search and Fetch APIs, Functions, session replay/observability, agent identity, and (from June 2026) managed **Browserbase Agents**. The legal entity name, parent company and ownership were **not verified to filing level** as of 2026-10-12. Searches for an acquisition or a 2026 funding round surfaced only aggregator pages, which describe a June 2025 Series B as the latest round. That is baseline context outside the window, not verified here. Searches found **no 2026 acquisition, rename or change of parent**. The founder named in the sources screened is Paul Klein IV; this is secondary, not filing-level.

**Open-source components and licences (checked 2026-10-16):**

| Component | Licence evidence | Note |
|---|---|---|
| [Stagehand](https://github.com/browserbase/stagehand) (TS/Python/Go SDKs, browse CLI, extension, server packages; one monorepo) | MIT, per the GitHub licence API and the [npm](https://registry.npmjs.org/@browserbasehq/stagehand) `license` field for 4.0.0 and 4.2.1 | 4.x versions exist on npm (4.0.0 on 2026-08-10, through 4.2.1 on 2026-10-11) but **no GitHub Release objects** for 4.x were found; release notes live in Changesets PRs |
| [browserbase/skills](https://github.com/browserbase/skills) (Autobrowse and agent skills) | **No licence detected** by the GitHub API, no LICENSE file at the repository root, no `license` field in `package.json` | Public visibility is **not** a reuse grant; treat it as all-rights-reserved until clarified |
| [microsoft/fara](https://github.com/microsoft/fara) (Universal Verifier and CUAVerifierBench, Microsoft-hosted) | MIT per the GitHub API | A Microsoft repository; Browserbase contributed trajectories according to its post |
| [hud-evals/liveweb-samples](https://github.com/hud-evals/liveweb-samples) (HUD) | MIT per the GitHub API | A HUD repository (created 2026-08-12), co-promoted by Browserbase |

The hosted Browserbase platform (sessions, Agents, Functions, Search/Fetch, Model Gateway, replay storage) is a commercial service whose terms, data retention and plan limits were **not reviewed**. MIT-licensed Stagehand does not license the hosted service. Stagehand's star count (25,687 at access) is **not** evidence of adoption or verified reuse.

## 3. Seven-segment dated chronology

| Period | In-window source evidence (source publication dates) | Availability and attribution limits |
|---|---|---|
| Apr 12–30 | [Apr 21 Universal Verifier post](https://www.browserbase.com/blog/building-verifiers-for-computer-use-agents) (with Microsoft Research; [arXiv v1 Apr 5](https://arxiv.org/abs/2604.06240) is **pre-window baseline**); [Apr 27 browse-cli 0.6.0](https://github.com/browserbase/stagehand/releases/tag/%40browserbasehq/browse-cli%400.6.0); [Apr 30 "5x" performance post](https://www.browserbase.com/blog/benchmarks-are-marathons) | The Apr 6 Model Gateway and agent-identity posts, the Apr 7 Platform post and the Apr 5 case studies are **outside** the window. The 5x claim has no baseline in the text. |
| May | [May 6 Autobrowse](https://www.browserbase.com/blog/autobrowse); [May 14 Session Replay API](https://www.browserbase.com/blog/session-replay); [May 20 upstream CDP tab-metadata patch](https://www.browserbase.com/blog/cdp-foreground-tab-tracking) | Autobrowse has no availability label; the CDP patch was **Canary-only** at publication. Stagehand 3.4.0 (May 11) was screened but not ledgered. |
| June | [Jun 3 Stagehand 3.5.0](https://github.com/browserbase/stagehand/releases/tag/%40browserbasehq/stagehand%403.5.0); [Jun 11 Navigate conference announcement](https://www.browserbase.com/blog/navigate) (event Sep 10); [Jun 19 Stagehand 3.6.0 WebMCP](https://github.com/browserbase/stagehand/releases/tag/%40browserbasehq/stagehand%403.6.0); [Jun 21 CVE-2026-12823](https://cveawg.mitre.org/api/cve/CVE-2026-12823); [Jun 25 skills PR #139 permission hardening](https://github.com/browserbase/skills/pull/139); [Jun 25 browse 0.9.0 output change](https://github.com/browserbase/stagehand/releases/tag/browse%400.9.0); [Jun 30 Browserbase Agents](https://www.browserbase.com/blog/introducing-browserbase-agents) | The CVE is a **third-party CNA (VulDB) record**; the fix PR does not cite it, so the linkage is the screener's inference. "GA on every plan" for Agents is a vendor statement. |
| July | [Jul 13 Stagehand 3.7.0 domain allow/block policy](https://github.com/browserbase/stagehand/releases/tag/%40browserbasehq/stagehand%403.7.0); [Jul 28 Model Router](https://www.browserbase.com/changelog) | The 30–40% saving is an unbenchmarked vendor claim. Jul 15 MP4 recording download and the Jul 2 Airtable case study were screened but not ledgered. |
| August | [Aug 10 Stagehand v4](https://www.browserbase.com/blog/stagehand-v4) (npm 4.0.0 the same day); [Aug 17 BYOS CDP logs](https://www.browserbase.com/changelog); [Aug 21 configurable Stagehand caching](https://www.browserbase.com/changelog) | The v4 benchmark is **one run** by the vendor's own description. Aug 6 Fetch-in-dashboard, Aug 19 named Contexts and Aug 21 Search-in-dashboard were screened but not ledgered. |
| September | [Sep 9 Webhooks in Functions](https://www.browserbase.com/changelog); [Sep 9 code mode / LangChain Deep Agents](https://www.browserbase.com/blog/evolving-computer-use-with-code); [Sep 22 Okta Cross App Access](https://www.browserbase.com/blog/browser-agent-identity-okta); [Sep 22 HUD LiveWeb tasks](https://www.browserbase.com/blog/browserbase-hud-frontier-evals); [Sep 24 pause/resume agent runs](https://www.browserbase.com/changelog); [Sep 30 Secrets in Functions](https://www.browserbase.com/blog/introducing-secrets-in-browserbase-functions) | The Okta integration has no Okta-side confirmation in the sources screened. No post-event record of Navigate (Sep 10) was found. The Sep 21 "What is Jev?" post (a third-party Typesafe model) was excluded. |
| Oct 1–12 | [Oct 8 Stagehand 4.2.0 release PR](https://github.com/browserbase/stagehand/pull/2969) (npm 4.2.0 Oct 8; 4.2.1 Oct 11) | **No first-party blog or changelog item** dated Oct 1–12 was visible. The Oct 14 Parallel search provider (listed on the [blog index](https://www.browserbase.com/blog) and [changelog](https://www.browserbase.com/changelog)) is **excluded** as out of window. |

The [CSV](053-browserbase.events.csv) holds **25 separate dated source records** (Apr 3, May 3, Jun 7, Jul 2, Aug 3, Sep 6, Oct 1). The list is purposively selected, not a census of Browserbase releases or a rate of innovation. Published dates are displayed source dates or API timestamps, not archive hashes. `event_date_utc` is blank unless the source gives a distinct underlying date: a release timestamp, a pre-window paper date or a scheduled conference. An `independent_check_url` pointing to npm, arXiv, NVD or a second repository is **documentary corroboration**, not an independent E3 audit.

## 4. Feature, rights and security cross-check

| Evidence cluster | What the cited document supports | Important non-equivalence or counterexample |
|---|---|---|
| [Universal Verifier](https://www.browserbase.com/blog/building-verifiers-for-computer-use-agents) + [arXiv 2604.06240](https://arxiv.org/abs/2604.06240) | A rubric-based verifier for browser-agent trajectories. The authors report "near zero" false positives against WebVoyager (≥45%) and WebJudge (≥22%) judges on CUAVerifierBench (246 trajectories). | Author-built benchmark; no independent replication found. An LLM verifier is still model-graded, which is **not** the same as hidden human acceptance tests (see the AGENTS.md rule against self-authored acceptance). |
| [HUD LiveWeb samples](https://www.browserbase.com/blog/browserbase-hud-frontier-evals) | Four YAML-specified live-site tasks whose answers are pinned to stable facts, MIT-licensed | Only four tasks. The post's own table has a malformed cell, and its text (an AirNow "50% cell") contradicts the table (100.0%). Live sites drift, so pinning reduces drift but does not remove it. |
| [Stagehand v4](https://www.browserbase.com/blog/stagehand-v4), [code mode](https://www.browserbase.com/blog/evolving-computer-use-with-code), [4.2.0](https://github.com/browserbase/stagehand/pull/2969) | Extension-hosted runtime, multi-language thin clients, MCP `run/snapshot/screenshot`, server-side cache with metadata | Breaking API changes contradict the "most scripts move over unchanged" line. "2x faster / 80% more token efficient" rests on one vendor-run crawl (14.2 s vs 22.7 s, a 1.59x throughput ratio). |
| [Stagehand 3.7.0 domain policy](https://github.com/browserbase/stagehand/releases/tag/%40browserbasehq/stagehand%403.7.0) | allowedDomains/blockedDomains in the SDK | No adversarial test of redirect, iframe or prompt-injection bypass was found |
| [CVE-2026-12823](https://cveawg.mitre.org/api/cve/CVE-2026-12823) → [skills PR #139](https://github.com/browserbase/skills/pull/139) | Autobrowse traces (cookies, auth headers, tokens, screenshots) were written with umask-default permissions. PR #139, opened Jun 22 and merged Jun 25, enforces 0600/0700. | Local-only, low-to-medium severity, and CVSS differs by source (see the CSV). The CVE initially named the wrong product. No vendor advisory or tagged release was found, and the PR does not cite the CVE. |
| [Secrets in Functions](https://www.browserbase.com/blog/introducing-secrets-in-browserbase-functions), [Okta XAA](https://www.browserbase.com/blog/browser-agent-identity-okta) | Client-side encryption with a per-project key, and short-lived scoped tokens instead of static API keys | Both are vendor claims. Server-side key handling is undocumented in the post, and there is no Okta confirmation. |
| [Session Replay API](https://www.browserbase.com/blog/session-replay), [BYOS CDP logs](https://www.browserbase.com/changelog) | Replays stream as HLS and are stored 31 days; Enterprise CDP logs can go to the customer's S3 | Observability raises sensitive-data retention risk. Using replays as test evidence needs redaction rules. |
| [browse 0.9.0](https://github.com/browserbase/stagehand/releases/tag/browse%400.9.0) | A default output-contract change for `browse screenshot` | A concrete downstream maintenance cost: scripts that parse stdout break unless they add `--base64` |

## 5. Publicly stated direction versus shipped functionality

| Dated first-party source (≤25-word paraphrase) | Promised horizon | Current research classification |
|---|---|---|
| [Jun 11 Navigate](https://www.browserbase.com/blog/navigate): will share identity-team research on how agent traffic reshapes the web | Sep 10, 2026 event | **Announced only**; no post-event record found |
| [Jun 30 Agents](https://www.browserbase.com/blog/introducing-browserbase-agents): one managed agent replaces per-site scripts; "Optimize" tunes and debugs agents | Immediate | **Vendor-stated GA**; Optimize behaviour not observed |
| [Jul 22 code mode essay](https://www.browserbase.com/blog/code-mode-is-all-you-need): agents should use a small code-execution surface, not many tools; illustrative ~88% context reduction | Uncommitted | **Position/estimate**, one hypothetical workflow, no measured benchmark; carried into v4 on Sep 9 |
| [Sep 30 Web Bot Auth explainer](https://www.browserbase.com/blog/what-is-web-bot-auth): signed agent traffic (RFC 9421 basis); access via sales | Ongoing | **Gated access**; IETF status of Web Bot Auth not stated on the page |
| [Apr 16 internal agents](https://www.browserbase.com/blog/internal-agents): migrating internal agent "bb" to a harness/compute separation | No timeline | **Internal intention**; self-reported productivity numbers (e.g. 99% faster first response) unverified |

Public intention is not scheduled delivery. None of these establish a 2027–2031 company strategy.

## 6. Conditional 2027–2031 outlook (analyst hypotheses, not company statements)

| Testable scenario | Rival cause | Disconfirming observation |
|---|---|---|
| Verifier-graded, pinned-answer live-web tasks (UV, LiveWeb) become a common reproducible test unit for browser agents | Human-labelled static fixtures stay cheaper and more reliable; live-site drift dominates | Repeated runs of pinned tasks show high answer or grader drift, or verifier false-accept rates on independent labels well above the reported "near zero" |
| SDKs converge on "code mode" (agent writes code against a small API) over many tool schemas | Model improvements make tool-call overhead irrelevant; vendor-specific benefit | Independent token/latency tests show no material difference at equal accepted-task rate |
| Agent identity (Web Bot Auth, XAA) becomes the default gate for agent web access | Sites keep blocking or allowing by heuristics; registries centralise power | Few sites verify signatures; agents continue to rely on stealth or captcha solving |

## 7. M1–M7 study relevance

| Construct | Possible observable effect | Prospective measurement, not inferred conclusion |
|---|---|---|
| **M1** coding practice | Shift from hand-written Playwright scripts to agent SDK or managed agents | Opt-in workflow records with and without the agent SDK; availability is not adoption |
| **M2** accepted task quality | Model-graded verification may inflate or deflate success | Compare verifier verdicts with **hidden human labels** on the same trajectories; count every attempt |
| **M3** discovery | Conference, blog and star growth | Not inferable from stars or press; out of scope here |
| **M4** verified third-party reuse | Upstream CDP patch and MIT SDK could be reused downstream | Trace one consented downstream integration; npm downloads and stars are not distinct users |
| **M5** reuse-first | Stagehand/Playwright/existing parser vs new agent code | Frozen comparison on identical fixtures (Section 8) |
| **M6** lifecycle human and energy cost | Breaking v3→v4 and browse 0.9.0 changes, cache staleness, LLM spend | Measure migration and review minutes and metered compute where instrumented; **no token-to-CO2e conversion** |
| **M7** actionable interventions | A reproducible agent-test harness may lower newcomer setup friction | Controlled, independently graded onboarding task |

Vendor adoption claims (35M+ sessions a month; Ramp, Shopify, Lovable, Airtable) are **not** independent task outcomes.

## 8. One falsifiable reuse-first maintainer experiment

**Target:** the repository's committed synthetic fixture [`tests/fixtures/trending.html`](../../../tests/fixtures/trending.html) plus frozen, locally served perturbed copies. **Fully offline, served on localhost**: no live GitHub, no Trending access (`capture` stays disabled under the [source-access decision](../../../docs/SOURCE_ACCESS_DECISION_2026-10-13.md)) and no hosted Browserbase account.

**Frozen task and functional unit:** extract `(rank, owner/name)` for every displayed row from 20 frozen local pages: 12 unmodified, 5 with markup perturbations (renamed classes, reordered attributes), and 3 that should yield an explicit "no valid rows" result. One **accepted page** is an exact match against hidden expected JSON written by a human who has not seen any tool output. No-answer pages stay in the denominator.

**Comparator A (reuse baseline):** the repository's existing deterministic parser, or a pinned plain Playwright script. **Comparator B:** Stagehand `@browserbasehq/stagehand@4.2.1` (MIT) in local-browser mode, using `extract()` with a pinned model, `setDomainPolicy({allowedDomains:["localhost"]})`, and caching disabled for the main run. Both use the same Chromium build and machine.

**Primary endpoint:** accepted pages / 20 assigned pages, including errors and timeouts. **Secondary:** run-to-run identity across 5 repeats (determinism), wall-clock time, LLM spend, human authoring, review and maintenance minutes (including one injected markup change), and any network request outside localhost (must be zero, checked from a captured request log). Do **not** use an LLM verifier (UV or similar) as the acceptance oracle.

**Budget and stop rule:** a cap of USD 5 in model spend and 4 human hours. Stop and keep A if B does not exceed A's accepted count on the perturbed pages, if B is non-identical across repeats on any unmodified page, if any off-localhost request occurs, or if the licence or model terms are unclear. A null or negative result is retained. **No trial executed; no effects estimated.**

## 9. Findings, uncertainties and review outcome (2026-10-16)

- **Observed/shipped (documentary):** Stagehand 3.5–3.7 and 4.0–4.2 releases (npm and GitHub records), the browse CLI releases, skills PR #139, and changelog-listed platform features (Model Router, BYOS CDP logs, caching, webhooks, pause/resume, Secrets).
- **Claims/announcements only:** the 5x performance gain, the "2x faster / 80% more token efficient" claim, Model Router savings, Autobrowse cost reductions, Agents GA scope, the Okta XAA integration, the Navigate content and the internal-agent productivity figures.
- **Contradictory or null evidence:** vendor caveats on the v4 single-run benchmark; the internal table/text inconsistency in the HUD post; the CVE's original wrong-product attribution and differing CVSS scores; the v4 "unchanged migration" claim against the listed breaking changes; no in-window trade-press testing found; no first-party Oct 1–12 blog or changelog item.
- **Unknowns:** legal entity and ownership at filing level; April–June changelog entries; GA/beta labels for several features; hosted-service terms and retention; whether the skills licence will be clarified; real adoption; independent verifier accuracy.
- **Pending:** human factual/link spot check (in particular the CVE↔PR linkage, the npm dates and the changelog-only rows), source-access/rights review, methods review, the two unexecuted searches listed in the [search log](053-browserbase.search-log.md), and any real opt-in trial. Issue #120 is **not** closed by this screen.
