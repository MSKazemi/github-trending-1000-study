# Zed Industries: 2026 six-month AI software intelligence (source-screened working report)

**Issue:** [#91](https://github.com/MSKazemi/github-trending-1000-study/issues/91) · **Watchlist ID:** 024 · **Window:** 2026-04-12–2026-10-12 inclusive (UTC) · **First research pass:** 2026-10-12 · **Status:** partially screened; independent/human review outstanding.

> **Methodological status:** This report offers directly attributed, dated primary materials and one preregisterable repo experiment. It does **not** complete the issue's systematic seven-segment literature/media search, prove vendor claims, document actual user adoption, or establish benefits of any tool. Independent product/ownership due diligence and second-person factual review remain required.

## 1. Reproducible scope and search audit

**Search expressions used as a targeted discovery strategy (2026-10-12, public web and the publisher sites):** `site:zed.dev/blog 2026 "parallel agents" "sandboxing" "Delta public beta"`. The vendor blog/chronicle/product directory and in-window individual results were checked. The retrieval interface did not preserve reliable search-result totals or a complete excluded-URL set: **found/screened/excluded counts beyond the 3 selected leads are not available**. This is *not* a systematic-review search log. Re-run dated queries per each month and save the underlying result list before claiming coverage.

**Eligibility:** publication date 2026-04-12–2026-10-12 and a material product, incident, governance or architectural event. For an event reported on one day that occurred earlier, the first release/effective date remains **unknown** until independently established. Do not count news repetitions as separate innovations. Search-page returns are not an unbiased denominator.

| Calendar segment | In-window lead found in this pass | Primary source | Missingness |
|---|---|---|---|
| 2026-04-12..30 | Introducing Parallel Agents in Zed (2026-04-22) | [source](https://zed.dev/blog/parallel-agents) | Source-read leads only; supplementary events possible. |
| 2026-05 | No verified event in this bounded source screen | — | NOT a zero-event assertion; calendar segment was not comprehensively screened. |
| 2026-06 | No verified event in this bounded source screen | — | NOT a zero-event assertion; calendar segment was not comprehensively screened. |
| 2026-07 | No verified event in this bounded source screen | — | NOT a zero-event assertion; calendar segment was not comprehensively screened. |
| 2026-08 | Sandboxing (2026-08-05) | [source](https://zed.dev/blog/sandboxing) | Source-read leads only; supplementary events possible. |
| 2026-09 | Replace PRs with Delta – Now in Public Beta (2026-09-16) | [source](https://zed.dev/blog/delta-public-beta) | Source-read leads only; supplementary events possible. |
| 2026-10-01..12 | No verified event in this bounded source screen | — | NOT a zero-event assertion; calendar segment was not comprehensively screened. |

## 2. Identity, ownership and baseline separation

Zed Industries publishes Zed editor and Delta collaboration product; Delta beta should not be conflated with universal availability or a replacement for GitHub's contribution workflows. Zed is described as open source; verify exact components and licenses.

**Official starting point:** https://zed.dev/. Homepage content alone is not dated release evidence; where ownership is inferred from a company announcement, independent legal registry verification remains a separate step. Pre-April announcements are historical baseline, not in-window events.

## 3. Individual dated primary-source events and feature map

| ID | Publication date / underlying actual event | What is directly documented | Availability status | Original link and source class | Independent audit | Working tier |
|---|---|---|---|---|---|---|
| 024-E01 | 2026-04-22; **actual first-shipment date not independently established** | Introducing Parallel Agents in Zed: Vendor announces per-thread agent and worktree control; states available in latest editor version | shipped (vendor-reported; version/plan limits not independently tested) | [product-announcement](https://zed.dev/blog/parallel-agents) | No independent functional replication | E1 company-working |
| 024-E02 | 2026-08-05; **actual first-shipment date not independently established** | Sandboxing: Technical article documents OS sandbox restrictions for agent terminal/fetch, operating-system caveats, privilege prompts and symlink race hazards; vendor security claim not independently audited here | shipped (vendor-reported; version/plan limits not independently tested) | [security-design](https://zed.dev/blog/sandboxing) | No independent functional replication | E2 company-working |
| 024-E03 | 2026-09-16; **actual first-shipment date not independently established** | Replace PRs with Delta – Now in Public Beta: Vendor introduces Delta collaborative agent-code review beta and claims Git compatibility; not evidence GitHub PRs are obsolete | preview (vendor-reported; version/plan limits not independently tested) | [product-announcement](https://zed.dev/blog/delta-public-beta) | No independent functional replication | E1 company-working |

**Availability semantics:** `shipped` means the *publisher reports release*, not that our team installed/tested it. `preview` denotes an expressly preview/beta or other constrained offering. `reported_undetermined` denotes engineering analysis or vendor result whose real-world deployment is not verified. `corrected` denotes incident/disclosed mitigation. `announced_only` is not a delivered feature. Do not treat a product benchmark, download/install count, funding announcement, star rank or a vendor-created survey as independently established task value.

**Evidence grades:** the company-watch E0/E1/E2 grades here are **not equivalent** to the study's causal/practical E0–E5 lesson evidence. E1 is first-party traceable announcement/argument; E2 is documentary multi-page corroboration or technical artifact *without* reproduced function. **No E3 independent performance replication, no E4 external multi-context impact evidence**. Where a source is only indexed rather than read completely, its E0 lead remains awaiting full verification.

## 4. Public strategy vs hypothetical outlook (2027–2031)

**Company-attributed public direction:** Zed's public posts show active interest in parallel agent workflows, OS-level access restrictions and conversational collaboration; Delta replacement ambition is not proven market adoption.

**Confirmed binding future releases:** none established by this pass. Announced intentions do not amount to delivery schedules.

**Analyst hypothesis, not a company promise (E0):** Least-privilege sandboxing and isolated worktrees could improve safe agent contributions; beta alternative version-control workflows may hinder discoverability/interoperability.

**Confounding / alternative mechanism:** Developers might get equivalent verification from simpler CI/PR policies, with no need to move collaboration into another platform. A disconfirming result is a randomized or matched test showing no added independently accepted task value, or higher lifetime cost and security incidents despite more generated work.

## 5. Connection to study constructs M1–M7

- **M1 workflow chronology:** preserve date and exact feature availability; do not equate tool release with verified developer adoption.
- **M2 accepted code quality/effort:** independently judge fixed tasks and failures/abstentions, rather than patch counts or anecdotes.
- **M3 visibility:** stars and promotion are *attention*, never sufficient for actual reuse.
- **M4 externally reproducible adoption:** require clean external first-use and downstream integration with an eligible denominator.
- **M5 reuse versus new build:** compare package discovery + license/security/version checks against bounded new build.
- **M6 lifecycle sustainability:** include planning, reviews, inference, CI, runtime, upgrades and upstream maintenance; **no token-to-kWh or carbon conversion**.
- **M7 ethical adoption:** only organic, task-verified contributor/user onboarding evidence—not purchased stars or low-value PR activity.

## 6. One practical falsifiable repository experiment

**Repository for initial pilot:** `MSKazemi/github-trending-1000-study`, with only its existing offline code/docs/fixture surfaces. **Proposed—not executed:**

Introduce no new runtime dependency initially: apply an agent permissions checklist and worktree isolation to 6 low-risk study PR tasks, compare to sequential branch approach while keeping GitHub PR review; simulate forbidden writes/network access and record explicit failures, independent acceptance and reviewer minutes.

**Acceptance design:** before assignment, a person other than the implementing agent must freeze the task description, user success conditions and hidden tests. Use fixed versions, identical safe fixtures and matched task difficulty; record the sampling frame and every refusal, timeout, unsuccessful run or abstention. **Primary endpoint:** fraction of independently accepted tasks with an explicit denominator and uncertainty. **Secondary:** downstream clean-install success, matching legal package identity/license, reviewer-repair minutes, money actually billed or clearly modeled and version drift at 30/90 days. Report kWh/CO2e only if instrumented with a documented system boundary and sensitivity analysis.

**Stop / rollback rule:** Keep GitHub standard PRs unless external contributor reproduction and audit trail demonstrably improve without lock-in or security regressions.

**Expected null/negative scenario:** no difference in accepted-task results, higher maintainer or review costs, poorer security, portability or upstream rights, or inability to obtain externally valid task ratings. Do not turn a null result into a fabricated positive lesson.

## 7. Scientific and security limitations

- The sources above are primarily vendor-operated. Independent investigative reporting, complete month searches, detailed feature/version license audits and disagreement resolution remain uncompleted.
- Distinguish **date a report was published** from actual launch or customer-availability; these are unknown where not explicitly documented.
- No vendor installation, benchmark run, respondent sampling, source-code security assessment, trial enrollment, verified third-party reuse, power calculation or environmental measurement was carried out.
- An AI assistant drafting its own report is **not** an independent scientific reviewer. Date and link spot checks are preliminary, not full blind confirmation.
- Vendor prices/savings, context benefits and release claims require same-task external replication and lifecycle boundaries before becoming recommendations.
- Do not automatically ingest untrusted code, post to upstream communities or grant tools network/secret access to gather evidence.

## 8. Conditional practical maintainer lesson

**Low-risk practice to test:** inspect existing tools, record their exact versions/rights, freeze user acceptance, measure agent/maintainer costs and keep human-governed review; promote only evidence-backed, type-specific conclusions, including failures. This is an **experiment suggestion** rather than a demonstrated method of increasing repository popularity or reducing energy.

**Review gates:** verify all dates and page links; complete each of 7 calendar-segment result logs; add independent cross-source and negative reporting; judge exact license/API/access levels; perform independent QA; connect to any event index without duplicates; then decide whether to merge and eventually close #91. A draft report alone is not issue completion.

**Study anchors:** [company method](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md) · [evidence-to-lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md) · [2027 central mission](../../../docs/AI_ERA_CODING_REUSE_RESEARCH_MISSION.md) · [reusable-component study](../../../docs/REUSE_FIRST_EXPERIMENT.md).

## Branch reconciliation and no-loss audit (2026-10-13)

The source-screened report above from [PR #203](https://github.com/MSKazemi/github-trending-1000-study/pull/203) is preserved verbatim, including its methodological caveats and first experiment. Its dated source-log `.events.json` is also copied unchanged. The later [PR #238](https://github.com/MSKazemi/github-trending-1000-study/pull/238) provided additional publisher evidence and a separate candidate experiment; these are retained below and in the CSV. Repeated URLs in JSON and CSV are **the same vendor announcement**, not two independent confirmations. The published dates and statuses were spot-checked against linked first-party pages by an AI reviewer, **not a qualified independent human**.

| Published date | Additional source not in original CSV | Caveat |
|---|---|---|
| 2026-08-05 | [Sandboxing](https://zed.dev/blog/sandboxing): Vendor describes OS-level sandbox limits on agent terminal/fetch, not an independent security audit. | Security boundary and symlink race conditions need independent threat-model review. |

**Consolidated sources:** 5 distinct URLs in the CSV, 4 preserved from the newer screen and 1 added. The original JSON retains 3 individually attributed working observations and does not represent a second independent source pool.

**2026-10-13 incremental source note:**

## Incremental source recheck (2026-10-13; first-party documentary audit)

This adds 4 specifically dated publisher statements; links and content were checked in public source results and/or primary pages on 2026-10-13. The [machine-readable event ledger](024-zed-industries.events.csv) follows the existing [company-intelligence field register](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md) with E1 **first-party claim** grades only. It does **not** imply systematic full seven-segment coverage, legal transaction authentication, independently tested products, or independently measured code outcomes.

| Publisher date | Primary publication | Specific company statement | Availability / evidence limit |
|---|---|---|---|
| 2026-04-22 | [Introducing Parallel Agents in Zed](https://zed.dev/blog/parallel-agents) | Zed introduced parallel agent threads and optional worktree isolation. | `shipped`; Parallelism can add conflicting writes or hidden review load. |
| 2026-05-20 | [Zed Stable Release 1.3.5](https://zed.dev/releases/stable/1.3.5) | Zed's versioned changelog recorded terminal-thread creation from sidebar and agent panel. | `shipped`; No independent multi-agent acceptance test was performed. |
| 2026-08-12 | [Introducing Delta](https://zed.dev/blog/introducing-delta) | Zed presented Delta as a multiplayer agent-code review environment. | `preview`; Beta invitation does not mean generally available, data rights unknown. |
| 2026-09-16 | [Replace PRs with Delta – Now in Public Beta](https://zed.dev/blog/delta-public-beta) | Zed announced Delta public beta and its own internal PR-replacement workflow. | `preview`; Company internal case study is not a verified broad developer outcome. |

**Correction to first pass / interpretation:** Zed's April parallel-agent threads were reported available in the current release; May stable version 1.3.5 documents terminal threads. Delta was initially a PRIVATE beta on Aug 12 and PUBLIC beta from Sep 16. Zed's own use of Delta is an internal case study, not external validation that pull requests should be universally replaced.

**Negative/independent evidence needed:** Review threat model for repo/worktree isolation and external ACP agents, DeltaDB replication/privacy/rights, actual time-to-accepted-merge and newcomer interoperability.

**Date precision:** `published_utc` and `accessed_utc` contain calendar dates, **not** authenticated exact UTC instants. Empty `event_date_utc` means underlying event-time not independently verified; do not fill it from publication date. Article revision history, frozen snapshots/SHA, exact search hit counts, exclusions, full seven monthly segments and actual independent human factual review remain pending. Do not interpret absence of a lead as evidence of zero releases.

**Proposed reproducibility step:** select real user tasks before learning system outcomes, freeze independent acceptance tests, time-box existing-code searches, check exact version/licensing/security, preserve all failed and incomplete assigned tasks, and compare full human reviewer/maintenance cost with matched functionality. No study task was executed, no real user/energy outcome measured, and no CO2e estimate made. This draft and issue #91 must remain under review until acceptance gates pass.


**Outstanding review gate:** complete seven-segment discovery/search denominators, source revisions, identity/terms checks and genuine independent reviewer approval before labeling company analysis complete. No product installed, no experiment executed, no observed adoption or environmental benefit. Issue #91 remains open.

### Preserved later working draft

The complete 2026-10-13 alternate source-screen text, including its initial search description, limitations and separate proposed repository experiment, is preserved **verbatim** in [the alternate report archive](source-archives/024-zed-industries.2026-10-13-first-screen.md). It is documentary draft provenance, not independent validation of publisher claims or a completed study.
