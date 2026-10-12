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
