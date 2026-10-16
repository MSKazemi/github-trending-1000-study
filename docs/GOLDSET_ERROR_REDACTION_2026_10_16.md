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
