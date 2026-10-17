# Three-issue engineering and tracker disposition — 2026-10-17

**Repository:** [MSKazemi/github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study)

**Truthful outcome labels:** one bounded **offline engineering implementation** can be closed as completed *after tested integration* (#10). Two highly overlapping **research tracker issues** can be closed as **duplicates/superseded tracking**, never as successful research (#9 and #16), but only *after* transferring every distinctive acceptance requirement to active canonical issues. All actual scientific/ethics/source gates stay open. No prospective protocol was preregistered, no human was recruited/reviewed, and no empirical result was obtained in this maintenance step.

## Selection rationale and acceptance crosswalk

### #10 — Complete the bounded cost/token accounting software, do not fabricate a study

[Issue #10](https://github.com/MSKazemi/github-trending-1000-study/issues/10) originally requests four engineering deliverables: versioned schema with synthetic fixture; null versus zero; full accepted/failed task denominators; no raw prompts, identities or secrets. Existing [merged PR #66](https://github.com/MSKazemi/github-trending-1000-study/pull/66) had provided the principal offline instrument. This follow-up patches the remaining concrete security defects: unrestricted bespoke JSON input/symlink following; private JSON decoder errors in nested CLI exceptions; malformed private UTC timestamp causes; huge direct Python numeric overflow. It reuses the project's strict 16 MiB descriptor-checked JSON reader, with tests asserting complete exception cause/context absence, safe filesystem input types, null/denominator invariants and existing write-once behavior.

**Disposal after CI:** `closed, completed` for **offline instrumentation only**. The broader pilot demands in the 2026-10-12 issue progress notes are explicitly **not waived** or claimed achieved. Continue in:

- [#17](https://github.com/MSKazemi/github-trending-1000-study/issues/17): independently frozen task acceptance and all randomized/failed/refused/attrited tasks; genuine opt-in and privacy/ethics approval, consented human work intervals, tool/agent-session concurrency reconciliation, verified provider token semantics/invoices, missingness/cost baselines and 30/90 day user-task followup
- [#24](https://github.com/MSKazemi/github-trending-1000-study/issues/24): consented upstream maintainer time, comprehension and followup, rather than collapsing their effort into downstream coding time
- [#18](https://github.com/MSKazemi/github-trending-1000-study/issues/18) and [#23](https://github.com/MSKazemi/github-trending-1000-study/issues/23): measured/calibrated or clearly unknown kWh/carbon and post-release lifecycle/rebound, no unsupported ROI
- An opt-in **live adapter is explicitly out of scope** of completed offline #10; a separately approved protocol/instrumentation decision is necessary. Never claim success from the synthetic fixture.

### #9 — Unify the AI-assisted/manual study tracker under #17, not its empirical result

[Issue #9](https://github.com/MSKazemi/github-trending-1000-study/issues/9) substantially overlaps [#17](https://github.com/MSKazemi/github-trending-1000-study/issues/17)'s randomized human/agent × ordinary/reuse-first trial. The following distinct points **must be preserved verbatim in substance** in the active #17 issue and protocol before #9 is marked `duplicate`:

| #9 requirement | Canonical destination | Remaining status |
| --- | --- | --- |
| AI-allowed versus manual/non-AI workflow definition, with contamination checks | #17 assignment/arm policy; historical Study B distinction in `docs/PROTOCOL_RECONCILIATION_DECISIONS_2026_10_12.md` D06 | **Unfrozen:** human/agent is not automatically the same construct as AI-allowed/no-AI |
| Greenfield versus mature project interaction/strata | #17 prospectively declared task/project blocking and moderator analysis | **No enrolled data** |
| Fixed acceptance before assignment, consent, risk/safety filters | #17 independent frozen acceptance and actual consent/ethics | **Unapproved** |
| Realistic pilot power, all dropped/refused/abandoned assignments, ITT/per-protocol, cluster CIs | #17 trial power and all-task denominator; #3 independent power/control sampling | **Not preregistered** |
| Independent blinded functional review/adjudication, +30/+90 rework and maintenance | #17 blinded gold outcomes and longitudinal followup | **No human review or followup** |
| All human prompt/review/repair time and simultaneous agent work, no code-volume surrogate | #17 measurement; offline #10 code only; upstream #24 | **Uncalibrated** |

**Disposition after transfer:** `closed, duplicate of #17` for **tracker consolidation**. A closure is **not** evidence that an AI-vs-human experiment has started or passed ethics, power or sampling review. Future design choices must be frozen **before treatment assignment** rather than edited retroactively.

### #16 — Unify Trending predictive-validity tracking under #6 + #19

[Issue #16](https://github.com/MSKazemi/github-trending-1000-study/issues/16) overlaps existing [#6](https://github.com/MSKazemi/github-trending-1000-study/issues/6) rank/drift instruments and [#19](https://github.com/MSKazemi/github-trending-1000-study/issues/19) independently judged downstream reuse. Its distinctive falsifiable **rank versus actual utility** question must **not** be lost:

| #16 requirement | Canonical destination | Remaining status |
| --- | --- | --- |
| Verify exact source page inclusion, position, selected language/period/window, capture error ledger and layout QA | #6 plus source/permission dependency #2 | **No authenticated prospective raw captures** |
| Compare star deltas **only when exposure/outcome windows align**, with signed deltas and unknown/missing denominators | #6 descriptive temporal rank/drift, limitations and interval estimation | **No real same-window sample** |
| Stratify by type, age and language, and measure uncertainty with CIs while reporting null/negative findings | #6 prespecified strata and confidence limits | **No externally validated estimates** |
| Independently verify downstream integrations or equivalent functional user tasks, with rights/license/security and baseline accepted-task tests | #19 reuse candidate evaluation; #8 independent user-task validity | **No independently accepted tasks** |
| Assess whether rank predicts independent reuse better than baseline popularity using prospectively matched controls, no outcome leakage | #6 exposure/rank covariates; #19 independently blinded reuse outcomes; #3 prespecified matching/power/control frame | **No eligible paired sample** |
| GitHub rank/stars are attention proxies, **not** success labels, causal effects or known secret algorithm weights | #6 / #19 constraints and negative-result documentation | **Maintain explicit nonclaim** |

**Disposition after transfer:** `closed, duplicate/superseded by #6 and #19` for **tracking only**. It is **not** a declaration that GitHub Trending has been validated as predicting use or that source permissions, causal identification or real human acceptance are established.

## Audit gate and sequence

1. Commit the narrow offline #10 bug fix with synthetic privacy/negative-path tests, its documentation and this exact acceptance crosswalk on a single reviewable branch. Do not change raw research fixtures or participant data.
2. Obtain **five current-head CI successes** (Python 3.10, 3.12, 3.13, 3.14 and research-artifacts). GitHub merge with expected-head SHA and non-squashed history; test the *integrated main commit* and compare code blobs.
3. Before **any** closure, append the unique #9 requirements to the active #17 issue, and append #16's source/rank requirements to #6 and the independently accepted reuse/task outcome requirements to #19. Append #10's still-open live/measurement/consent gates to #17, #24, #18/#23.
4. Re-fetch canonical issue bodies and verify that each distinct missing acceptance is explicitly tracked and each target issue remains **open**. Only then close #9 and #16 using GitHub's **duplicate** reason; close #10 as **completed (offline engineering scope)**.
5. Place audit links/merge SHA/CI outcomes in the three closed issue discussions; do not interpret green CI as any human methods/rights signoff. If a canonical target cannot be edited or verified, **do not close** its source issue.

## Practical lessons for repository maintainers

- One issue should own each distinctive scientific question; close redundant **trackers** as duplicates only after a no-loss acceptance crosswalk is visible on the open parent.
- A merge proves a bounded software change landed; a study needs authentic source rights, consent, independent functional judgments, negative results and often externally preregistered treatment definitions.
- Reuse strict bounded input readers instead of per-script JSON snippets, and test both visible stderr and the entire exception cause/context graph for private data leaks.
- Prefer an honest single completed engineering issue and two clearly labeled duplicate closures over manufacturing three nonexistent research findings.
- Preserve dated protocol versions, unfrozen hypotheses, and unknown denominators. Human-versus-agent and AI-allowed-versus-no-AI are related but **not identical** without an explicitly declared intervention policy.
