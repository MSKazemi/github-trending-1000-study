# AI software engineering economics: total effort, not generated tokens

**Status:** metric specification and worked synthetic examples, not observed project findings.

## Unit of account
One **accepted user-relevant task** with a predefined, independent definition of done. Denominator should include failed and abandoned attempts; report them separately. 'Generated lines of code', tokens alone, or minutes until first code completion are not acceptable primary outcomes.

## Time and effort
Define:
- `H_plan`: human problem definition, context gathering, design, acceptance tests
- `H_prompt`: writing/refining prompts and agent instructions
- `H_review`: human inspection, verification, security and test review
- `H_fix`: debugging/regression repair/rework
- `H_ship`: packaging, deployment, documentation, onboarding
- `H_followup`: maintenance/support hours during stated follow-up window
- `H_other`: explicitly accounted nonoverlapping work
- `T_wall`: elapsed wall-clock from start to accepted deliverable; report separately
- `T_agent`: agent runtime/wait; **do not blindly add it to human hours** if developer performed concurrent work.
**Total human effort** = sum of nonoverlapping human-active categories; define and exclude calendar overlap before summing. For concurrent agents, log each cost separately without double-counting human elapsed time.

## Token and infrastructure accounting
`input_tokens`, `output_tokens`, `cached_input_tokens` (if provided) and `model` /`tool_version` recorded **per accepted task and per attempt**, including retries. Provider token accounting and caching semantics vary; avoid naive aggregation across providers. Include API spend **actually charged**, subscribed plan allocation when relevant (clearly explained), CI/compute/storage/review overhead and ongoing costs. **Cash cost $0 is not evidence that time or risk cost is zero.**

## Derived quantities (do not use without their denominators)
- **Accepted task throughput** = number of independently accepted tasks / human-active hours over period; if no accepted tasks, report zero and costs.
- **End-to-end completion ratio** = accepted task attempts / started task attempts; include abandoned attempts.
- **Verified time saving** = baseline task duration - assisted duration, where both use equivalent acceptance criteria; report distribution and uncertainty.
- **Human-adjusted ROI** = (estimated verified task benefit in agreed units - direct monetary costs - valued human effort - forecast maintenance exposure) / explicitly defined invested cost. Report **components**, not just one ROI.
- **Tokens per accepted task** = total billable/equivalent tokens including unsuccessful attempts / number accepted. If 0 accepted, report undefined rather than 0.
- **Verification share** = H_review+H_fix divided by total human hours (when positive).
- **Post-release debt** = hours attributable to regressions/maintenance over predefined 30/90 day window.
- **Wasted exploration proxy** = logged time spent on work abandoned before a testable useful outcome; this can still produce useful knowledge, so classify 'learning value' separately.

## A transparent illustrative scenario — NOT study data
Prototype A: 2 hours generation + 8 hours fixing + 4 hours support, 1 accepted task. Prototype B: 6 hours careful coding + 1 hour fixing + 1 hour support, 1 accepted task. A appears faster on initial code; B has lower total effort (8h vs 14h) under the toy assumptions. If A had produced many *independently accepted* tasks, comparison might reverse. Evaluate **like-for-like outcomes and risk**.

## Guardrails against cost manipulation
- Version-lock acceptance suites before comparing tools. Blind review where possible.
- Do not divide by cherry-picked tasks or exclude unsuccessful attempts.
- Report free vs paid plans, price/time version, calendar/concurrency accounting, caching, tool calls and costs missing.
- A faster insecure or unmaintainable artifact is not 'efficient' solely because it used fewer tokens.
- Separate ideation, implementation and sustained deployment by stage: they have different valid productivity measures.
- Use privacy-preserving aggregated logs; don't publish raw confidential prompt transcripts or secrets.

## Practical budget policy (proposed)
For each candidate user task, set a **user-chosen cap** for wall time, human time, max retries and token spend *before execution*; stop to inspect reasons on budget overrun instead of blindly prompting more. A manual comparison baseline should be evaluated at least periodically. This is a discipline, not a validated universal optimal threshold.
