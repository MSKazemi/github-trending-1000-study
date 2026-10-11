# Offline project-idea decision gate

The stdlib-only decision aid `python -m trending_study.value_gate` evaluates a **user-authored** project card and returns a transparent recommended **next validation action**, not a star estimate, market prediction, security certification, or scientific effectiveness score.

## Run
```bash
python -m trending_study.value_gate --input examples/idea_card.example.json
python -m unittest discover -s tests -v
```

The included card is **synthetic**, contains no observed users/tasks, and should return `run_independent_task_test` with unknown effort/tokens.

## Card contract v1.0
- `project_name`, `project_type`, `target_user`, `problem_statement`, `existing_alternative`, `differentiator`, `acceptance_task`: strings
- `risk_level`: `low | medium | high` (self-assessed); `security_review`: `not_done | pass | issues_found | not_applicable`
- `independent_evidence`: `{ "kind": "none|self-test|external-interview|independent-task|repeat-use|research-replication", "count": integer >=0 }`. **Self-reported**; the tool does not verify it.
- `task_evaluation`: `attempted`, `succeeded` nonnegative ints, `acceptance_criteria_frozen` bool
- Optional `effort`: `planning_minutes,prompt_minutes,review_minutes,repair_minutes,ship_minutes,followup_minutes` nonnegative numbers; input/output token counts optional ints
- Optional `budgets`: `max_human_minutes`, `max_total_tokens` numeric thresholds chosen by the user, **not** science-derived
- Counts that have not been collected should stay explicit as absent (for costs) or zero verified observations with proper measurement meaning (for tasks).

## Decision states
`define_problem`, `compare_existing_alternatives`, `freeze_acceptance_task`, `security_review_before_release`, `repair_and_retest`, `run_independent_task_test`, `seek_independent_evidence`, `test_repeat_value`, `continue_with_followup`.

The tool evaluates guards in that order, and security flags can override promising adoption claims. A positive response means **continue evaluation**, never 'proven valuable'. Evidence levels are qualitative labels and can be self-reported; no numerical threshold is a validated predictor of project value.

## Important boundaries
- **Not a classifier** trained on 1,000 repositories: there is no dataset yet.
- No network, secrets, source code access, identity collection or GitHub permission needed.
- Under-reported maintenance effort and unverified external use can overstate value.
- More tokens can be rational when they reduce defects or enable a useful outcome. Optimize **accepted value per total cost**, not minimal tokens irrespective of effectiveness.
- Review legal, privacy and security issues separately for real apps.
