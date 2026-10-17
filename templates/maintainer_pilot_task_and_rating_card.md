# Maintainer burden pilot: task and independent rating card (DRAFT)

**One card per consenting, frozen case. REVIEW REQUIRED before any real use.** Do not store completed participant cards, signatures, handles, private text or source identifiers in public Git.

## Private research operations: do not commit completed card

- Study/protocol version and separate ethics/privacy approval IDs, verified against an **external** register:
- Pseudonymous project and task IDs (no names/emails); restricted linkage-key custodian:
- Date/UTC frozen eligibility, reasons for inclusion/exclusion; frozen task-spec and independent acceptance-suite SHA-256:
- Source/rights permission and sandbox evidence:
- How the actual participant received information, affirmed research participation, separately acknowledged appropriate data-processing terms and can withdraw:
- Task start/closure UTC and 30/90-day eligibility dates:
- Participant roles and possible shared upstream/downstream contributor; reasons work categories might overlap:
- Consented human effort diary provenance (time clock and periodic calibration), reviewer disagreements:
- Unsupported/failed search or agent attempts and whether effort categories counted them:
- Code reviewer and newcomer grader identity **stored only in restricted audit register**, not report or input JSON:
- Participant-level privacy/withdrawal and incident escalation decisions: 

## Independently scored actionability (no agent self-rating)

Pass **only if all are substantiated**:

1. Genuine, task-linked user/problem statement and reproducer or bounded acceptance evidence (not promotional comments)
2. Tested, functionally relevant suggestion with no disqualifying security, license, privacy or rights concern
3. Useful net change versus existing solution; not a duplicate/automated low-information issue
4. Independent checker signed a specific evidence reference and reviewed failed/negative cases too

**Enter one:** `pass` / `fail` / `unknown`; describe objective evidence privately. Unknown includes genuinely unassessable cases, conflicts of interest or unresolved reviewer disagreement, not an implied failure. Independently collect at least two judgments for the rubric calibration cases; freeze resolution and adjudication rules before substantive tasks.

## Newcomer comprehension and repair

- Use identical time budget, sandbox, setup instructions and no hidden agent-authored tests.
- Independent newcomer must explain three preselected invariants/risks, locate the relevant implementation/test, articulate a plausible repair and demonstrate a change passing the frozen independent acceptance check.
- Record time-to-understanding/time-to-fix and uncertainty **only if consented**, note interruption/partial tasks. A failed attempt is a coded negative; not attempted/no assessor is unknown.
- Code one of `pass`, `fail`, `unknown`, with privately stored objective grader evidence and adjudication status.

## Six effort categories (nonoverlapping active minutes)

| Category | Include | Exclude from this category |
| --- | --- | --- |
| upstream_review | Read/reproduce/assess submitted work | Waiting time, downstream coding |
| upstream_support | Maintainer replies, compatibility/security guidance | Passive wall time |
| downstream_search | Discovery, due diligence, abandoned candidate checks | Upstream review |
| downstream_implementation | Integration/new feature or repair coding | Independent acceptance grading |
| downstream_review_repair | Local review, tests, rework, retries | Upstream support |
| downstream_followup | Downstream upgrades/maintenance in fixed horizon | Work after consent withdrawal |

Each category is a nonnegative number of measured/diary minutes or `null` if unknown. **Zero is allowed only when the activity was observed and truly absent; do not replace missing with zero.** Explicitly track overlapping timers; do not double count concurrent participants or agents as one person's active time.

## 30/90-day outcome checkpoints

| Follow-up | Proposed window | Code |
| --- | --- | --- |
| 30 days | 23–37 days after task closure | `completed` / `missing` / `not_started` / `unknown` |
| 90 days | 76–104 days after task closure | same codes |

Record actual queried/observed date privately, actual repair/update or no change, security incidents, and whether a visit was genuinely due. **Completed** means a genuinely recorded assessment occurred (even when result negative); **not_started** means due date not reached; **missing** means a due check had no usable result; **unknown** means unclassifiable due date/consent/source. Do not mark no incident without a performed check.

## Release-screen checklist

- [ ] Genuine independent reviewer and ethics/privacy approvals checked out-of-band
- [ ] Consented right-to-use, clear withdrawal process, allowed retention
- [ ] Unknown and negative outcomes preserved with original case denominator
- [ ] No direct or inferable personal identities, raw URLs, private source, rank, public “bad maintainer” comparison
- [ ] Suppression of small/unique cells and disclosure-risk review before public release
- [ ] Explanation of convenience-sample bias, missingness, follow-up immaturity and noncausal scope

**Export to `trending_study.maintainer_burden` only a metadata-minimized case.** This card is a prospective data-dictionary/rating tool, not an actual enrolled task or the signature of an independent human reviewer.
