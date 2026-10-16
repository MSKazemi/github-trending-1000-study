# Issue #222 — human gate for first genuine requisition status observation

**Prepared:** 2026-10-15 (UTC-date granularity). **Status:** engineering handoff; **not** source access approval, consent, employer-observed dataset, longitudinal measurement or human research signoff. Existing offline validator: [trending_study/hiring_observations.py](../../trending_study/hiring_observations.py), synthetic unit regression: [tests/test_hiring_observations.py](../../tests/test_hiring_observations.py).

## Source/rights go-no-go (must be filled by qualified non-author reviewer)

| Decision | What must be independently documented | Current value |
| --- | --- | --- |
| Official source/role identity | Exact employer, canonical job/requisition URL, location variants, company/ATS publisher ownership; distinguish index-only text from direct description | **Unknown; dependency #220** |
| Platform access, rights and cadence | Source-specific terms/robots permissions; acceptable manual/API method, local retention/redistribution rights, allowed follow-up rate; no alternative scraping workaround | **Not approved** |
| Protocol lock | Preselected cohort and denominator, true prospective UTC start, inclusion/exclusion, separate auth and case-handling; no backdating October leads | **Not signed** |
| Human/private data | Do not record applicants, interviewees, named employees, application tracking or confidential source data; authorize any needed opt-in process | **Not approved** |
| Independent quality control | Second person checks selected source link/contents/status, duplicate identity and missing-event interpretation without seeing expected outcome | **Not observed** |

All entries are **deliberately unresolved**. An agent must not turn this template into human approval by changing text.

## Event interpretation that must survive live source checks

- `listed_live`: directly seen listing body, with contemporaneous status/content digest; **not** a hiring count or a forecast of a shipped feature.
- `index_only` and `indexed_text_only`: title/snippet lead only, not complete job description.
- `inaccessible`, `not_listed_in_bounded_search`, `removed_or_redirected`: missing or non-observation; **never infer closed/filled** from disappearance.
- `explicitly_closed`: require dated, specifically attributable employer evidence; keep distinction between *listing closed* and *position filled*, with no estimated fill rate.
- `reopening` and `reposting`: maintain employer+requisition IDs, location variants, revision order, earlier informative state, link evidence and uncertainty; never relabel a new requisition as an old hire.
- `right_censored`: keep every unobserved future closure in denominator and record last actually seen time, not date of analysis as if it were last observed.

## Offline preflight and acceptance handoff

1. Confirm test fixtures remain labelled synthetic and no collector, scheduler, bypass or real login was added to this branch.
2. Run `python -m unittest discover -s tests -p test_hiring_observations.py -v` and the full Python 3.10/3.12/3.13/3.14 CI matrix at the **exact PR head**; also verify artifact validators.
3. Non-author human methods/privacy reviewer approves or rejects the source and prospective frame **before** any real observation. Preserve the signed decision and contrary findings in a separately dated record.
4. Execute only allowed manual/API source checks with actual UTC, immutable SHA and missingness logging, then independently adjudicate identity and status. Publishing this checklist is not execution.
5. Review evidence/rights, check current main and the actual PR diff before an expected-head merge. Recheck post-merge CI and close #222 **only** if the actual scientific acceptance is independently satisfied.

**Practical maintainer lesson:** a job disappearance is an access/status event, not evidence of a filled vacancy. Model missingness explicitly in versioned ledgers; never coerce it to a hiring forecast, zero, or positive business outcome.
