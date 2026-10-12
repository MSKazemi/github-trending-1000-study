# Research conversation checkpoint — 2026-10-12

**Source:** the current project's most recent user request and previously recorded strategy. This is a public-safe project note, not a verbatim export of assistant/tool messages or unrelated chats.

## U9 — Authorize moving from the five-year strategy to real implementation
> Go head

## Concrete research action taken (2026-10-12)
The immediately preceding five-year strategy explicitly recommended proceeding with [Issue #27](https://github.com/MSKazemi/github-trending-1000-study/issues/27) — freeze a reproducible task-first research design only once prerequisites are satisfied. Review of repository code exposed one dangerous prospective-observation weakness: the fixture/legacy parser labeled the moment of *parsing* as collected-at time, while a supplied observation date could be any past date. That is inadequate for valid +7/30/90/180-day follow-up baselines.

The implementation is **phase-limited**: a manifest created at actual user-initiated fetch time (UTC, byte length, original raw SHA-256, source page and HTTP response metadata); a strict parser verifying its raw-file integrity/URL/date; documentary pilot versus confirmatory preflight gates that fail closed until evidentiary human review; synthetic offline tests; a draft v0.3 preregistration and explicit status/SOP/audit/signoff forms.

The initial proposed 2026-10-15–31 pilot is **not recorded as performed**. Main November 1, 2026 recruitment **cannot** be called frozen when source permissions, nine-page language coverage, real-page 30-row independent audit, immutable IDs, independent task frame, power/consent and qualified scientific review are incomplete. No retrospective or fabricated data or human participation appears in this note.

## Artifacts and links
- [Pilot operating procedure](../docs/PILOT_CAPTURE_AND_PREFLIGHT.md)
- [Preliminary registration draft](../docs/PREREGISTRATION_DRAFT_2027.md)
- [Unresolved readiness ledger](../docs/PROTOCOL_FREEZE_STATUS_2026_10_12.md)
- [Original strategy](../docs/FIVE_YEAR_ROADMAP_2027_2031.md)
- [Pending scientific work](https://github.com/MSKazemi/github-trending-1000-study/issues/27)

## Next evidence required
Independent access review; a permitted real capture with checksum manifest; >=30 manual row checks across windows; ID dedup; a prespecified task-frame and sample-power simulation; consent and external reviewers. **Until then, outputs are pilot tools—not measured science.**


## U10 — Continue hands-on parser validation (verbatim)
> go head

## Research actions (2026-10-12)
Following the user-approved issue #27 pilot instrument, the selected next work is GitHub [issue #2](https://github.com/MSKazemi/github-trending-1000-study/issues/2): prove that a Trending parser does not silently omit repository rows. Existing strict `article.Box-row` structural validation can still produce an internally consistent **positive subset** when a row is drawn using a different selector. The new `page_audit.py` / `audit-pages` CLI compares capture manifest integrity to two human-supplied, complete-page independent row lists and emits per-window and aggregate exact rank-identity TP/FP/FN and abstention metrics; unknown/disagreed annotations remain unscored. A synthetic 36-row daily/weekly/monthly regression suite explicitly simulates selector drift, mismatches, forged labels, duplicate captures and path traversal risks. All results are **software unit tests, not collected Trending findings**.

The code execution runtime could not resolve `github.com` during a single user-initiated attempt to inspect robots.txt and daily HTML. Web page text surfaced an old cached snapshot without raw HTML/provenance; none of this counts as a real observed 30-row audit. No source access restriction was bypassed. Live source-permission verification, two genuine human annotators, 30+ real rows and statistical preregistration remain future approval gates. Full methods: [independent audit documentation](../docs/INDEPENDENT_PAGE_AUDIT_2026_10_12.md); source limitations remain described in [study protocol](../docs/PROTOCOL_FREEZE_STATUS_2026_10_12.md).

## U11 — Faculty-style computer-science review (user request)

> As a stand for full props or in the computer science, what you suggest?

This was interpreted as a request for **hypothetical senior professors' perspectives** on the study, not actual external reviewers or endorsements. After checking `main` research protocols and critical gaps, the recommendations emphasized independently sampled tasks, controlled reuse-first versus usual coding comparisons, trustworthy coding-agent attribution, contribution/maintainer costs, genuine software reuse, real adopted functionality and qualified lifecycle footprint rather than GitHub stars or token proxies.

The [dated faculty-style report](../docs/FACULTY_STYLE_RESEARCH_RECOMMENDATIONS_2026-10-12.md) was submitted in [PR #61](https://github.com/MSKazemi/github-trending-1000-study/pull/61) and **merged** as documentation. The literature review on 2026-10-12 checked primary publisher/conference sources including [Huang et al., MSR 2026](https://doi.org/10.1145/3793302.3793622) (missed reuse opportunities in the sampled AI PRs), [Gao et al., MSR 2026](https://doi.org/10.1145/3793302.3793573) (roughly 80% of one sampled agent-coauthored PR population merged without *explicit* review feedback), and [Hamza et al., ESEM 2026](https://doi.org/10.4230/LIPIcs.ESEM.2026.67) (some review differences also observed in non-agent comparison developers). **These are external findings with study-specific limitations, not original results of this repository.**

## U12 — Proceed to methods implementation (user request)

> Go ahead.

### Completed bounded action

- Checked the live repository, the existing synthetic task allocation and public-issue candidate code, issue #2 source validity and the earlier faculty report.
- Discovered that [GitHub robots.txt](https://github.com/robots.txt) includes `Disallow: /*since=*`, matching the project's older `/trending?since=...` collector URLs. **No live Trending collection was attempted**; the README now documents the source-access no-go pending independent review/permission.
- Independently of future reuse opportunities, preselected six familiar ecosystem repositories for **exploratory convenience sampling**: `pallets/click`, `Textualize/rich`, `psf/requests`, `vitejs/vite`, `tokio-rs/axum`, and `prometheus/prometheus`. Queried each public GitHub REST first page using `per_page=15`, `state=open`, `sort=created`, `direction=desc`. The reduced metadata input is labeled with the query-completion UTC `2026-10-12T20:11:31.062Z`.
- Observed **90 page rows, 44 non-PR issue leads and 46 PR exclusions**; applied the existing frozen-seed SHA-256 sampler, giving **16 issue leads** for later human screening. Source responses/HTTP headers were not preserved; Git-tracked reduced metadata cannot prove the whole GitHub issue universe or source replay. All 16 remain **unreviewed**, acceptance not frozen, reuse opportunity **unknown**.
- Added the six-source [reduced metadata frame](../examples/task_intake.cross_ecosystem_2026-10-12.json), [methods/validity report](../docs/CROSS_ECOSYSTEM_TASK_INTAKE_2026-10-12.md), [16 clickable issue leads](task-screen-queue-2026-10-12.md), [independent review template](../templates/feasibility_task_review_card.md) and regression tests enforcing source rows, PR exclusion, unknown statuses, privacy minimization and selection-to-queue agreement.
- [PR #63](https://github.com/MSKazemi/github-trending-1000-study/pull/63) merged after checks **passed** on Python 3.10 and 3.12. [Issue #65](https://github.com/MSKazemi/github-trending-1000-study/issues/65) explicitly tracks the unfinished **two-human-reviewer screening, frozen specs/negative tests, prospective permission/consent/power and independent judgment gates**. The README links all research outputs.
- Existing issues #21/#25 may be closed for synthetic tooling; **closed is not evidence** of completed real-world review or a randomized causal experiment.

### Scientific outcome/status after this turn

The public REST issue *metadata* and source counts above are actual observed exploratory **intake facts**, not hypotheses. **There are still zero independently accepted tasks, zero actual user/agent randomized attempts, no verified sample of 1,000 Trending repositories, no live 30-row independent Trending page QA, and no defensible net carbon saving estimate.** Human screening may exclude some or all 16 issues; prespecify exclusions and do not swap them for apparently reusable tasks. A future experiment must retain failed and no-known-solution attempts, avoid leaked fixes and quantify independent accepted functionality and complete cost.

**2027 lesson to test, not assume:** agents should search for safe, compatible existing solutions first, verify rights/provenance and independent functionality, and choose reuse, upstream improvement or deliberate new code based on a full human/lifecycle comparison—not stars or tokens.
