# Independent adoption and long-term maintenance measures (issue #12)

**2026-10-12: measurement design, not collected adoption data.**

## What counts and what does not
GitHub stars, forks, Trending appearances, package downloads, CI counts and page views are **attention/activity/proxy signals**. They are not unique users, functioning installations, accepted end-user tasks or evidence of causal benefit. Unknown traffic remains null. Never infer personal AI usage from code appearance.

| Archetype | Defensible primary adoption evidence (if available and permitted) | Selective-observability warning |
|---|---|---|
| Library | independently verified downstream dependency/integration at exact version + exercised API | optional/transitive/test-only dependencies, vendoring, private use |
| CLI | consented real-user task completion and repeat use | installs, mirrored downloads and CI inflate counts |
| Service | consented organization-specific production integration with accepted task evidence | self-hosted/private usage absent |
| Research artifact | independent rerun of a specified scientific workflow plus citation to used method | citations often do not imply successful reuse |
| Template/agent skill | independent task executed using generated scaffold, with output checked | downloads and forks need not run |
| Documentation-only | consenting reader solves independently specified question | pageviews/crawlers do not measure comprehension |

## Record and denominators
Use stable repository ID (not only mutable owner/name); archetype, fixed UTC baseline, measured source and legal basis, instrument version, unit (organization, integration, task or person; NEVER silently interchange), opt-in source approval, eligibility count, attempted count, independent passes, failures, unknowns, refusals and censored followups. Keep identities/personal traces out of public data. At 30/90/180 days use actual observation dates, prespecified schedule and a one-row-per-eligible-unit trace:
- observed independently verified integration retained / eligible verified integrations at baseline;
- successful repeat task / eligible invited baseline users (attrition reported);
- supported update within horizon / baseline components eligible for that followup;
- burden minutes, security/rights regressions and abandonment reason where consented.

A missing response is **not** an adoption failure or zero minutes. Provide conservative bounds on success among all eligible: observed successes/N through (observed successes + missing)/N, and show complete-case point only as a sensitivity estimate. Separate structural ineligibility from lost-to-followup. For zero denominator report null, not zero.

## Sampling and comparison
Stratify by package/ecosystem, age, project type, visibility and language; include little-known reused mature OSS and observed non-Trending controls. Track baseline adoption *before* measured attention. Compare adoption and maintenance outcomes as associations with adjustment and sensitivity analysis, not as proof that Trending rank creates use. Non-observed-in-Trending is not never-trending. Include selection probabilities where known; do not impute a global GitHub frame. Register all outcomes and intervals before looking at followup results.

## Bias register and research stop conditions
Selection by willingness to share logs; survival/attrition; automated dependency graphs; dependency freshness; silent CLI use; bot downloads; private deployments; identity deduplication; vendor semantics/version drift; observer effects; inability to authenticate self-reports. Halt publication of independent adoption estimates if outcome units, legal basis, denominator or independent validation are missing.

## Maintainer experiment (2027)
Publish a pinned clean-install task with a versioned example, then recruit consenting unaffiliated users and measure independent pass rate at first contact and repeated task satisfaction at 30/90 days. Compare against the pre-change baseline and record all failures and effort. Treat improvements as a hypothesis until independently replicated.

**Implementation follow-ups:** build source-specific machine-readable evidence adapter, independent review, opt-in repeat-use collection, privacy retention approval and bounds-reporting tests. This document only partially implements #12.


## 2026-10-15: bounded offline CLI input gate (#306)

The \`python -m trending_study.adoption_bounds --input examples/adoption_signals.synthetic.json\`
command reuses the strict research decoder with a descriptor-based bounded
reader. It refuses duplicate JSON keys, NaN/Infinity, non-UTF-8 input,
nonregular paths (including FIFOs), leaf symlinks where the OS supports
no-follow, and files above 16 MiB. The actual read is bounded independent
of size metadata, and diagnostics omit source paths and duplicate-key text.
It is not a sandbox against a maliciously replaced ancestor directory.

**Practical lesson:** validating research formulas alone is insufficient
when the CLI silently overwrites duplicate JSON keys or trusts unbounded file
reads. Keep missingness explicit, use one strict decoder at public input
boundaries, and never call this a real adoption result.
