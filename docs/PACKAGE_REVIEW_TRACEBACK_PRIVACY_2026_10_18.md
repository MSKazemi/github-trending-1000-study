# Issue #22 — full-exception privacy guard for offline package-review input

**Status:** Engineering correction proposed on 2026-10-18; regression tests are synthetic. It does not authenticate publishers, licenses, advisories, artifacts, humans or actual registry data.

## Defect and reproduction boundary

The shared strict JSON reader may chain underlying decoding and filesystem errors that include sensitive user-supplied field names, filenames, or paths. Previously, the package-review wrapper rethrew these inside an `except` block, and the CLI raised `SystemExit` via `argparse.error` while still handling the public exception. The displayed stderr was sanitized, but full exception telemetry could retain the raw cause/context. Malformed HTTPS authorities likewise chained URL parser exceptions.

## Change

- Map shared-reader failures to an allowlisted fixed public diagnostic, then raise **after leaving** the exception handler. Reject any unexpected reader message with a generic error.
- Raise a generic URL-authority error only after leaving the URL parsing handler.
- Call `argparse.error` after exception handling so its `SystemExit` has no underlying private exception context.
- Keep strict JSON input limits, fail-closed evidence checks, offline/no-install behavior and the existing source-provenance limitations unchanged.

## Verification

Run `python -m unittest tests.test_package_review -v` and the complete CI matrix. Four new synthetic tests check formatted exception tracebacks and `__cause__`/`__context__` for duplicate private JSON keys, untrusted reader diagnostics, malformed authorities, and CLI `SystemExit`. Earlier decoder-recursion tests now assert both absent cause/context and suppression. Successful evaluation outputs must be unchanged.

**Limits:** This addresses particular validation tracebacks; it is not a general log-scrubbing guarantee. A programmer who explicitly logs source files or identifiers may still expose them. The source ledger remains self-declared, so package approval, publisher provenance, SPDX matching, advisories, artifact signatures and suitability require independent external checks. Original issue #22 stays open until its scientific/security acceptance is met.

**Practical maintainer lesson:** Test exception *chains and formatted tracebacks*, not only exception messages and CLI stderr. Raising a sanitized message inside `except` can still expose private inputs to full-traceback telemetry.
