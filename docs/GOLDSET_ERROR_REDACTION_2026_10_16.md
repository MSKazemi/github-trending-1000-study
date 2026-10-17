# Offline pooled-reuse goldset: diagnostic privacy boundary (issue #19)

**Date:** 2026-10-16. **Evidence class:** a local engineering regression, not a human-approved reuse benchmark. Related to [issue #19](https://github.com/MSKazemi/github-trending-1000-study/issues/19) and the previously merged strict-input change [PR #420](https://github.com/MSKazemi/github-trending-1000-study/pull/420).

## Problem and bounded correction

The existing goldset CLI accepted a structured task/candidate pool only after strict, bounded, regular-file JSON checks. However, its *schema* errors still interpolated the submitted `task_id`, `candidate.id` and `system.name` into `GoldsetError` text. Because `main` sends these errors to stderr, failed offline runs could accidentally expose proprietary task identifiers or internal package names in CI logs, terminal captures or issue reports.

This focused patch preserves all existing scoring logic and output shape, but replaces caller-controlled identifier strings in **errors** with fixed safe labels: `task`, `candidate`, and `system`. Duplicate task, candidate and system identifiers are rejected without echoing the submitted values. Fixed gate names and descriptive validation reasons remain, so a maintainer can still diagnose which category failed without publishing private content.

Two new standard-library-only regression methods use distinctive synthetic secret markers in task, candidate, system and filename fields. They exercise invalid gates, duplicate objects and unknown ranked IDs as well as the actual CLI stderr boundary. They assert that no private marker is emitted on rejection. This does **not** prevent intentional identifiers in a successful local JSON summary (the program is still a user-controlled offline analytics tool); output handling and export remain an operator responsibility.

## Human/scientific and security limitations

- This avoids one diagnostic leak, not arbitrary process-memory, shell-command, file permission or log retention exposure.
- Neither passing strict JSON parsing nor redacted errors authenticate source packages, licenses, provenance, independent labels or repository reuse outcomes.
- #19 acceptance still requires a permitted, frozen real-task corpus; independent functional/license/security adjudication; proper lexical/embedding/hybrid comparisons; full failed/unobserved denominators; external methods review; and observed costs.
- No new dependency, network request, package install, protocol enrollment, aggregate statistic or unapproved source collection is introduced.
- Merge only with required exact-head five-job GitHub Actions, full diff review and actual qualified maintainer signoff. Passing self-written tests is **not** evidence of independent approval.

## Practical maintainer lesson

A privacy-safe JSON reader is not enough if higher-level validators echo user-controlled identifiers after successful parsing. Include **CLI stderr** and exception content in regression testing, and preserve stable error *classes* rather than leaking invalid user data. Report success with independently accepted tasks, not stars, lines of code or apparent pool relative recall.

## 2026-10-16 strict field-level data minimization

The pooled goldset validator additionally fails closed on undeclared fields at its root, task, candidate and retrieval-system boundaries. An unknown key may contain raw private prompts, email addresses, credentials or otherwise unconstrained material; silently ignoring it can make the record appear to conform to the audited schema. The error deliberately prints the fixed structural level only, never an unknown caller-provided key or value. The existing optional candidate `adjudicator_ref` is retained.

One synthetic negative regression inserts a private-marker field at each nesting level and verifies refusal with redacted diagnostics. This is a **data-minimization and integrity guard**, not a guarantee that the original permitted text fields contain no sensitive material and not independent verification of the pooled candidate labels, external users or software fitness. #19 remains open for its controlled real-task benchmark.

## Follow-up: underlying datetime exception tracebacks

A further static audit found that `datetime.fromisoformat` may include the malformed caller-provided timestamp in its own `ValueError`. The original `raise GoldsetError(...) from exc` retained that raw exception as a chained cause. The top-level CLI displayed only a fixed category, but a system that recorded complete exceptions could expose submitted timestamp text. The parser now records failure, leaves the `except` block, and raises a generic `GoldsetError` **without** a raw cause or exception context. Synthetic tests inspect `traceback.format_exception`, `__cause__` and `__context__` for both task baseline and candidate release timestamps. Successful output is unchanged, and intentionally submitted identity fields can still appear in successful summaries; this is not a guarantee for arbitrary telemetry or log processors.

## 2026-10-17 CLI chained-exception correction

The prior command-line wrapper used `ArgumentParser.exit()` within
`except ResearchJSONError`. Even though the printed error text was generic,
a traceback-capturing caller could inspect the underlying decoder exception
through `SystemExit.__context__`. The wrapper now captures a bounded fixed
error category, exits **after** the exception handler, and only surfaces
controlled `GoldsetError` diagnostics. Synthetic tests inspect the complete
formatted `SystemExit` traceback, cause/context and stderr for a private
duplicate JSON key. This does not protect intentional successful output or
arbitrary caller instrumentation; data and human review remain unverified.
