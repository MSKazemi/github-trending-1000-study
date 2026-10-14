# Qodo (#018): no-loss reconciliation of overlapping company research PRs

**Date recorded:** 2026-10-13. **Study window:** 2026-04-12 through 2026-10-12 inclusive. **Issue:** [#85](https://github.com/MSKazemi/github-trending-1000-study/issues/85). **Status:** **PR source crosswalk, not a completed Qodo research report**. No independent two-human-researcher factual validation, controlled product testing, company adoption, ecological benefit, external evaluation or systematic seven-segment source recall is claimed.

## Problem and exactly which materials may be lost

Three branches independently propose the same canonical report `research/company-intelligence/2026-04-12_2026-10-12/018-qodo.md`:

- [PR #198](https://github.com/MSKazemi/github-trending-1000-study/pull/198) (closed **unmerged**, head `614bb47f3c5083ae3ec1668935f872985c0623af`): report and **four-item JSON lead ledger**, `018-qodo.events.json`, with E1 first-party source attribution.
- [PR #213](https://github.com/MSKazemi/github-trending-1000-study/pull/213) (draft when inspected; head `4e9ade4ead17265465560e61ed83d263d001891b`): more extensive report and **six-row, 22-field CSV ledger**, `018-qodo.events.csv`, including crucial PR-Agent governance and license caveats.
- [PR #232](https://github.com/MSKazemi/github-trending-1000-study/pull/232) (draft when inspected; head `9f181aad203b6c077242d0b84a42318ddaf53891`): another report with **three additional, nonoverlapping Qodo source leads** not included in #213's CSV.

**Do not merge one `018-qodo.md` over another or treat multiple source items covering one announcement as independent confirmations.** This crosswalk is designed to preserve source provenance across all three branches. It does not merge their narrative interpretations or certify their event dates.

## First-party article leads across all three PRs

This table is a **candidate URL and provenance register**. Entries are not 10 independently tested outcomes, nor a complete six-month company screen. At least two first-party articles below were inspected directly on 2026-10-13; otherwise the candidate's web accessibility and date should be rechecked as part of issue #85 before including it as dated evidence.

| Lead | Candidate canonical article | Origin PRs | Review task or bounded observation |
|---:|---|---|---|
| 01 | [Source](https://www.qodo.ai/blog/an-update-on-code-generation-at-qodo/) | [#213](https://github.com/MSKazemi/github-trending-1000-study/pull/213) | Change in code-generation strategy; vendor announcement; date and retirement scope require independent check |
| 02 | [Source](https://www.qodo.ai/blog/qodo-is-handing-pr-agent-over-to-the-community/) | [#213](https://github.com/MSKazemi/github-trending-1000-study/pull/213) | First-party community/Apache-2.0 transition announcement dated 2026-04-23; independent current-license discrepancy |
| 03 | [Source](https://www.qodo.ai/blog/introducing-qodo-2-4-the-next-layer-of-code-quality-governance/) | [#213](https://github.com/MSKazemi/github-trending-1000-study/pull/213) | Vendor quality/governance release notice; deployment constraints not independently checked |
| 04 | [Source](https://www.qodo.ai/blog/why-your-ai-coding-agent-shouldnt-review-its-own-code-the-case-for-an-independent-verification-layer/) | [#198](https://github.com/MSKazemi/github-trending-1000-study/pull/198), [#213](https://github.com/MSKazemi/github-trending-1000-study/pull/213) | Vendor argument for independent review; opinion, not evidence of measured efficacy |
| 05 | [Source](https://www.qodo.ai/blog/introducing-qodos-agentic-toolbox/) | [#198](https://github.com/MSKazemi/github-trending-1000-study/pull/198), [#213](https://github.com/MSKazemi/github-trending-1000-study/pull/213), [#232](https://github.com/MSKazemi/github-trending-1000-study/pull/232) | Agentic review/toolbox announcement; availability, rights and testing pending |
| 06 | [Source](https://www.qodo.ai/blog/introducing-qodos-software-map/) | [#198](https://github.com/MSKazemi/github-trending-1000-study/pull/198), [#213](https://github.com/MSKazemi/github-trending-1000-study/pull/213) | Cross-repository context/software map; provisional preview status, test pending |
| 07 | [Source](https://www.qodo.ai/blog/the-anatomy-of-a-breaking-change/) | [#232](https://github.com/MSKazemi/github-trending-1000-study/pull/232) | Distinct breaking-change source lead not in #213 event ledger |
| 08 | [Source](https://www.qodo.ai/blog/the-right-depth-for-every-pr-introducing-review-effort-modes/) | [#232](https://github.com/MSKazemi/github-trending-1000-study/pull/232) | Dated 2026-07-28 first-party page: review depth Fast/Balanced/Auto/Deep; research preview, not verified productivity |
| 09 | [Source](https://www.qodo.ai/blog/state-of-ai-code-quality-report-2026/) | [#232](https://github.com/MSKazemi/github-trending-1000-study/pull/232) | Potential vendor-produced code-quality report; inspect method/denominator and sample bias before claiming results |
| 10 | [Source](https://www.qodo.ai/blog/introducing-qodo-3.0/) | [#198](https://github.com/MSKazemi/github-trending-1000-study/pull/198), [#213](https://github.com/MSKazemi/github-trending-1000-study/pull/213) | Qodo 3.0 announcement; observed product acceptance/testing not yet evaluated |

Other linked artifacts from the PR materials (not additional independent company-release events): [Qodo homepage](https://www.qodo.ai/), [official blog index](https://www.qodo.ai/blog/), [The-PR-Agent/pr-agent repository](https://github.com/The-PR-Agent/pr-agent), and the [current mutable LICENSE reference](https://github.com/The-PR-Agent/pr-agent/blob/main/LICENSE).

## Verified narrow licensing conflict: use commit-pinned evidence

The [Qodo 2026-04-23 first-party handover article](https://www.qodo.ai/blog/qodo-is-handing-pr-agent-over-to-the-community/) states an intended or announced return of PR-Agent to **Apache-2.0**, while the separately fetched public GitHub `The-PR-Agent/pr-agent` **main LICENSE on 2026-10-13** begins `MIT License`. To make this reproducible, the checked file had blob SHA `43fff0c98b18eba319298a18dae01a57ba0eac97` at [commit `330f0813b5fe0d1f54b794077c2d02aa85a1fb63`](https://github.com/The-PR-Agent/pr-agent/blob/330f0813b5fe0d1f54b794077c2d02aa85a1fb63/LICENSE).

This establishes **different first-party assertions at different timepoints**, not proof of the exact historical license change sequence, rights of each file/dependency, or publisher breach. The study must verify the exact **release/tag/commit/artifact** and its bundled license plus dependencies before recommending reuse. Never cite a mutable `main` license as a timeless package guarantee; keep the original April statement to track the apparent change.

The directly read [2026-07-28 Qodo Review Effort Modes announcement](https://www.qodo.ai/blog/the-right-depth-for-every-pr-introducing-review-effort-modes/) explicitly calls its automated review-depth routing a **research preview**. It offers a plausible comparison of risk-aware review tiers, but no independent acceptance, reviewer time, task correctness, or token-to-CO2e impact has been established here.

## Reconciliation instructions (must be completed BEFORE making a canonical report mergeable)

1. Freeze the three existing report branches and ledger head SHAs above as an auditable baseline; do not delete their source material or silently rewrite archived observations.
2. Use `canonical source URL + underlying event + publication/event date` as the **human-audited reconciliation key**. De-duplicate the overlapping three Qodo announcement articles (`agentic-toolbox`, `software-map`, `qodo-3.0`) between #198 and #213; do not double count evidence from one publisher. Preserve source-specific contradictory claims and revision notes.
3. Choose **one versioned event-ledger schema** (e.g., the detailed CSV from #213), then map all four JSON leads and unique #232 leads explicitly, retaining `origin_pr`, original `event_id` and source URL. Do not automatically declare an event `shipped` from a vendor announcement or silently remap unverified status.
4. Check exact link accessibility, author/date/updated-at, availability (GA vs preview), plan/region, model/source license and independently reported incidents against official docs and credible reporting. Record queries and search dates **for every calendar-month segment** of the interval; incomplete months stay **unknown**.
5. Require qualified **independent human factual/licensing review** and research-methods checks when escalating claims. Keep research issue #85 and its original draft PRs open until real acceptance criteria, source log and conflicts are complete.
6. Test one **falsifiable maintainer-repository experiment**: compare fixed-effort vs risk-adaptive review on prospectively frozen maintenance tasks, with independent correctness/security acceptance and false-positive counts, full human reviewer minutes and inference/API costs. Treat resource/energy reductions as a hypothesis unless measured.

## Practical maintainer lesson

**For your repositories:** When several agents contribute to the same documentation or research result, maintain one **canonical evidence/event ledger**, immutable origin PR references, explicit draft/review status, and independent source/legal checking. Merge duplicate evidence by source identity, **not** by whichever PR finished first or has more rows. This is also a green-software lesson: unnecessary duplicate implementation and re-review can waste effort, but a quantified energy/CO2e saving requires actual measurement.
