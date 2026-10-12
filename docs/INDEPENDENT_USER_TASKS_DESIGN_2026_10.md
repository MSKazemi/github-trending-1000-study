# Independent user-task usefulness instrument — bounded #8 contribution

**2026-10-12 status:** prospective instrument and fictional example **only**. No users recruited, no consent obtained, no observed installations/reuse events, no preregistration and no validation pilot. [Issue #8](https://github.com/MSKazemi/github-trending-1000-study/issues/8) remains open.

## Research target, task and comparison

Define a useful outcome **before** comparing documentation, codebases or assistants. A task is one specific user need, one target project type, pinned software version, fixed hardware/environment and a test whose answer is not given to the developer/agent under evaluation. Unit of analysis: a **consenting user's attempted task**; report both user and task denominators and cluster repeated tasks by user/project. Do not use stars/forks/downloads as independent successes.

Use [synthetic structured card](../examples/usefulness_task.synthetic.json) for fields. Its fictional values are **not empirical data** and should never be fed into confirmatory analyses.

| Archetype | Bounded prospective task | Independent acceptance evidence | What can be N/A |
|---|---|---|---|
| CLI/automation | install to clean nonprivileged environment; run supplied example; inspect output | command/version/checksum, exit code, task-specific output validator, independent observer | GUI navigation |
| Programming library | install pinned release and call documented API in a fresh minimal program | import/ABI compatibility, tests, task output and dependency/license screen | launch UI |
| Research method/data artifact | reproduce specified published table/figure on legally shareable fixture | preserved input SHA, versioned code, numerical tolerance and logs | production uptime |
| Hosted or desktop app | register *only with consent*, complete one protected-domain-safe user journey | independent user task completion and observed time/errors | package import; service uptime where unsupported |

## Prespecify outcomes and denominator rules

- **Primary:** `accepted`: `pass|fail|unknown|not_applicable`; define exact acceptance before exposing variants. Unknown includes lost logs/cannot observe and must remain in the *assigned-attempt* denominator for sensitivity bounds, not silently disappear.
- **Secondary:** time-to-first-success (including failed attempts), independent repeat use under consent, support/review minutes, repair cost, adverse behavior and installed downstream integrations. A second attempt by the same person is not another independent user.
- **Opportunities:** declare `attempted`, `assigned`, `consented`, `observed`, `withdrawn` distinctly; consent withdrawal handling and retention follow policy. A project may have no telemetry; absent data do not mean nobody uses it.
- **Follow-up:** plan 30/90-day measurement and censor incomplete exposure; do not forward-fill old acceptance or assume retention from a star.
- **Adjudication:** independent rater(s) blind to whether AI/reuse/marketing variant was used; failures and no-solution tasks remain in the denominator, contradictions adjudicated with dated record.

## Minimal proposed design before real human testing

1. Independently recruit a representative-for-target-population **opt-in** mix, record eligibility, consent, project archetype and experience group without unnecessarily identifying participants. Get ethics review where required.
2. Freeze question, task frame, functional rubric, sample size rationale, randomization/blocking and source SHA **before** the intervention. Avoid mixing software and documentation changes.
3. Compare baseline vs one intervention, counterbalance task difficulty if feasible, stop on security/privacy harm, and preregister an intention-to-treat analysis including abandoned/failed tasks.
4. Independently execute clean-room first-run checks and manual log validation; compare outcomes with uncertainty and subgroup sensitivity. Report blocked cases and null/negative findings.
5. Release only aggregated, privacy-screened data and a reproducible task pack, not unconsented raw transcripts or private host telemetry.

## What this delivers now and what remains

**Delivered:** an explicit multi-archetype operational rubric, missing/N/A/withdrawn handling, study card example and task comparator with a separate stop condition. **Not delivered:** task recruitment, independently hidden acceptance suites, consent, power analysis using real variance, execution or validity evidence. Existing trial scaffolding [docs](TRIAL_PILOT_INSTRUMENT.md) and [tool](../trending_study/trial.py) should be **reused** rather than building a duplicate randomizer.

## One practical lesson for your repositories

On one library or CLI README, ask consenting external developers to independently complete the same clean-install task with existing vs revised docs under frozen acceptance criteria. Capture genuine success/repair minutes, rather than trying to maximize README length or README SEO. Stop if the new documentation confuses users or increases unsupported setups. See [value mission](AI_ERA_CODING_REUSE_RESEARCH_MISSION.md).
