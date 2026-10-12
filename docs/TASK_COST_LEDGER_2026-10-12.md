# Task-level agent and human cost ledger (issue #10)

**Prepared:** 2026-10-12. **Status:** offline instrument + fully **synthetic** demonstration, not real task data, participant consent, an independent productivity measurement, a registered trial, or a carbon/energy study.

## Purpose and scientific boundary

Task output, cost, and trustworthy reuse must share the **same all-assigned-task denominator**. This small standard-library-only instrument audits a privacy-minimized human/agent activity ledger against the existing [2x2 task trial](TRIAL_PILOT_INSTRUMENT.md). It **does not** instrument Codex/Copilot/Claude, intercept private prompts, authenticate an event, verify participant identity, collect telemetry, authorize scraping, or automatically obtain research consent.

A task that failed, was refused or abandoned, or remains pending **must** have one cost-ledger row; it cannot disappear just because it generated no accepted code. If time/token/cost coverage is incomplete, the corresponding aggregate remains **null**, not zero. Trial arm and accepted status are sourced exclusively from the separately audited trial frame/outcomes, **not** claimed by the cost ledger.

## Deterministic offline walkthrough

Requires Python 3.10+ and no third-party packages, network calls, or model API key.

\`\`\`bash
python -m trending_study.trial assign \
  --frame examples/trial_frame.synthetic.json \
  --output /tmp/assigned-costs.synthetic.json
python -m trending_study.task_costs \
  --frame examples/trial_frame.synthetic.json \
  --assignments /tmp/assigned-costs.synthetic.json \
  --outcomes examples/trial_outcomes.synthetic.json \
  --input examples/task_costs.synthetic.json \
  --output /tmp/task-costs-report.synthetic.json
python -m unittest discover -s tests -v
\`\`\`

Outputs are **write-once**. Use an unused file path on each run, or omit \`--output\` to print JSON to stdout. Existing destinations and input/output aliases are rejected; the process never overwrites study artifacts.

The sample has nine fictional screened task candidates, eight assigned and one excluded before assignment. Accepted, failed, refused, abandoned and pending labels are synthetic trial fixtures. Six artificial agent events illustrate two model calls plus a tool/retry for one task, missing telemetry, monetary provenance, and human/agent concurrent activity. In this synthetic fixture, **the preexisting T07 outcome has 120 reported human minutes but only a one-hour lock-to-closure interval**. It is therefore left **unmeasured at interval level** by this ledger; this synthetic inconsistency must not be treated as valid human-time evidence.

## Schema contract: \`task_costs\` v1.0

Top-level input JSON has exactly: \`schema_version="1.0"\`, \`dataset_kind\`, \`protocol_id\`, and \`task_costs\`. The latter is **one entry for every assigned task** in \`--assignments\`, with no excluded IDs, duplicates or omissions. Dataset kind and protocol ID must match the validated trial.

Each task object has exactly:

| Field | Type | Meaning |
|---|---|---|
| \`task_id\` | opaque pseudonymous ID | Must match exactly one assigned task. Never a username/email/account ID. |
| \`coverage\` | object | \`human\`, \`events\`, \`monetary\`, each \`complete\`, \`partial\`, or \`missing\`. **Self-declared**, not authentication. |
| \`human_intervals\` | list | Each interval has \`actor_slot\`, \`category\`, \`started_at_utc\`, \`ended_at_utc\`. Approved categories: \`plan\`, \`prompt\`, \`review\`, \`repair\`, \`ship\`, \`followup\`, \`other\`. |
| \`agent_events\` | list | Each event has the exact keys below; never raw content/arguments/outputs. |
| \`budget\` | object or null | Optional self-declared caps **locked no later than the assigned frame's lock UTC**; timestamps alone do not prove prior registration. |

Event keys: \`event_id\`, \`session_id\`, \`kind\` (\`model_call\`, \`tool_call\`, \`ci_job\`, \`retry\`, \`idle\`), \`started_at_utc\`, \`ended_at_utc\`, \`model_id\`, \`tool_id\`, \`input_tokens\`, \`output_tokens\`, \`cached_input_tokens\`, \`amount_usd\`, \`cost_basis\`.

- Model-call events need an opaque model/version identifier and null tool ID. Token metrics are **provider-reported or explicitly unknown** (integer or null); \`cached_input_tokens\` denotes the cached subset of \`input_tokens\`, not additional tokens. Do not mix unlike provider definitions without normalization.
- Tool-call/CI events need an opaque tool/version identifier; non-model events cannot invent model tokens. Retries/idle markers cannot separately charge for a model/tool operation and double count billed attempts. Separate successful/failed model/tool attempts appear as their own event rows.
- Chargeable events have decimal **string** USD amounts with up to six fractional places or null. For a known amount, the basis must be \`provider_billed\`, \`provider_estimate\`, or \`synthetic\`. \`synthetic\` costs are forbidden in \`pilot\` data. Cash cost and active time are different quantities.
- Budget keys: \`locked_at_utc\`, \`max_human_minutes\`, \`max_tool_calls\`, \`max_retries\`, \`max_event_cost_usd\`. A null cap means \`not_set\`. Exceeding a cap is flagged; unknown spend/coverage yields \`unknown\`. This auditor **does not stop an agent** or enforce prospective spending limits.

Exact allowed-key validation rejects accidental prompt, identity, source code, command, URL and tool-argument fields; it **cannot** fully guarantee anonymization from arbitrary opaque strings. Review and minimize all data before collecting and publishing it.

## Computations and safeguards

- \`human_active_minutes\` is the **sum of nonoverlapping intervals** when \`coverage.human=complete\`. It must match the independently audited outcome's reported human minutes, to within one second. Actor-slot intervals must not overlap **even across tasks**. A single person using two aliases cannot be detected. Unobserved or partial human time stays null, without silently assuming zero.
- \`model_calls\`, \`tool_calls\`, \`retries\`, and \`recorded_event_wall_minutes\` become complete only if **all agent events are declared covered**. Event wall time uses the **union of recorded event intervals**, so simultaneous agents are not summed into impossible extra elapsed time. It is *not* the complete agent session or human wall clock.
- \`input_tokens\`, \`output_tokens\`, and \`cached_input_tokens\` are totals only if all model-call events were covered and each relevant count was known. Otherwise, null. Provider token accounting varies.
- \`observed_event_cost_usd\` is complete only if events and monetary coverage are complete and all chargeable amounts are known. The result is a **bounded scoped event cost**, *not* full task spending. Human wages, subscription allocation, unrecorded CI, equipment, energy, and maintenance are **outside this amount** unless separately represented by authorized instrumented event costs. \`cost_by_basis_usd\` explains whether values were billed, estimated or synthetic; it is not an invoice verifier.
- The overall and per-arm summaries retain every assigned task and the audited acceptance status. A missing task cost makes the relevant cohort total **null**, preserving missingness rather than using only successful cases. Zero accepted means cost-per-accepted-task is undefined (null); pending tasks prevent a final accepted-per-hour ratio.
- UTC timestamps, strict decimal amounts, duplicate event IDs, malformed trial hashes, rights/security gate failures, and post-hoc budget timestamps fail closed. Some temporal inconsistencies cannot be excluded without verified task-start markers.

## Study requirements before any real pilot

1. Obtain actual documented participant opt-in and appropriate ethics/data-rights assessment; preserve consent and withdrawal rights in a **controlled** store.
2. Freeze task definitions, allocation, acceptance conditions, budgets and measurement plan before work; use an approved preregistration when advancing to confirmatory inference.
3. Use only suitably authorized aggregate/truncated provider metrics; no private code, raw prompts, emails, secrets or identifying session metadata in this public repository. Prefer encrypted access-controlled raw telemetry outside Git, with retention and redaction policies.
4. Verify coverage against independently retained provider billing/agent instrumentation where allowed; \`complete\` and budget-lock fields are merely declarations.
5. Record consented human active intervals, including retries/rework and overlapping participant activities, and reconcile with the trial outcome ledger; record dropped records as *missing*.
6. Report resource/cost definitions and provider-specific token semantics, including possible model changes and cached-token billing differences, **before** making comparisons. Keep measured, estimated and synthetic dollars separate.
7. No claims of kWh, gCO2e, reduction in emissions or agent ROI can be inferred from this report. See [cost methods](TOKEN_TIME_ECONOMICS.md), [lifecycle protocol](FULL_LIFECYCLE_BREAK_EVEN_2027.md) and [ethics](ETHICS.md).

## Link to CTO research priority

This is the smallest concrete offline implementation of **CT2 (agent-native systems economics)** in [the October 2026 advisory memo](MICROSOFT_CTO_RESEARCH_LENS_2026-10-12.md). It contributes to issue [#10](https://github.com/MSKazemi/github-trending-1000-study/issues/10). It does **not** complete the full issue: no authorized data collection adapter, robust session lifecycle reconciliation, independent calibration against human/provider logs, power analysis, or real economic findings exist.

### Practical maintainer lesson

Do not compare Codex and Claude by generated code or the number of tool calls. Compare the same independently tested, user-relevant task with a frozen specification, all failures/returns to humans, actual time/cost bills, and later maintenance. A portfolio team can test this schema privately and report **aggregate**, authorized results after review—never copy raw participant traces into this public repository.
