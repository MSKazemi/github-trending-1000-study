# Prospective, bounded control-candidate sampler — issue #3 (2026-10-18)

**Stage:** proposed offline engineering instrument. This is NOT a frozen registration, approved field collection, a random sample of all GitHub, validated matching, or a control cohort. All fixture repository IDs and queries are fictional. Study A (observational Trending and comparison candidates) remains separate from Study B (consented agent/human task experiment).

## The actual decision it supports

Issue #3 needs a pre-outcome way to sample comparison *candidates* from an independently documented GitHub REST search frame while preserving stable numeric repo IDs, matching strata, provenance and missingness. A fixed hash rank makes a declared sample reproducible across machines and input-row order. It does not make GitHub's search ranking/frame representative or the fixed seed independent of researcher choices.

Run from the repository root:

    python -m trending_study.control_sampling --input examples/control_frame.synthetic.json

The input must have exact schema version 1.0, a self-reported evidence kind, a frozen timestamp, opaque seed, source-frame SHA-256/query/capture timestamps, prespecified calendar-week/language/project-type/age/stars-band strata with quotas, candidate stable repository IDs and pre-source snapshots, and a separately declared list of observed Trending repository IDs. Unknown and excluded candidates remain counted but unselected. Known observed-Trending IDs are always held out, even when a candidate declares preliminary eligibility. Source captures after freeze, candidate snapshots after their source capture, cross-stratum duplicate IDs, duplicate profile quotas, nonstandard timestamps and any extra output/future fields fail closed.

The algorithm sorts each stratum by SHA-256 of fixed namespace + seed + stratum ID + numeric repo ID, selecting the first K eligible candidates; no dependence on input order or subsequent outcomes. The returned plan hash binds every supplied source metadata digest, query, seed, cutoff, stratum quota, candidate status, and observed Trending list. Record the entire original input and output as restricted versioned artifacts **before** looking at any outcomes; this code cannot authenticate when such an external freeze happened.

## Required analysis caveats

- A row merely **not seen in supplied Trending captures** is *not* a verified never-trending repository. Prospective crossover and eventual control contamination must be explicitly tracked at each follow-up.
- The returned within-supplied-frame fraction is a *nominal descriptive fraction*, not a verified inclusion probability, inverse-probability weight, GitHub population coverage estimate or causal sampling weight. Frame/search completeness, ranking/pagination truncation and seed independence are unverified.
- Calendar-week/age/stars/project-type bins are *declared strata*. Whether they are measured correctly at the required **pre-exposure** time needs source checks; present-day metadata cannot be silently backdated.
- Quota shortfalls and unknown/ineligible/trending holds remain visible. Never replace shortfalls with convenient cases or reselect after outcome inspection.
- Actual source rights/robots/Terms, extraction/export permissions, independent candidate qualification, matching balance diagnostics, outcome windows, attrition, valid power simulation, data ethics, and signed preregistration all remain outstanding in #3 and #27.
- Any proposed downstream contrast must use fixed baseline covariate windows, standardized mean differences/overlap, stratification and sensitivity checks approved before outcomes. An actual conditional association does not automatically imply a causal Trending effect.

## Synthetic regression coverage and practical lessons

The tests assert deterministic order independence; seed/stratum/status/observed-list hash changes; strict invalid-source/invalid-field rejection; no future leakage; valid and invalid ISO weeks; duplicate IDs and profiles; honest unknown/trending exclusions; empty provisional selection with shortfall reporting; and redacted CLI exception chains. No network call, dependency install, secrets, participant recruitment, live capture, manual annotation, or claims of 1,000 observed repositories occur.

**Practical repository lesson:** the design can enforce stable ID, pre-declared strata and immutable *content commitments* without pretending the sampled frame is random, source-licensed, unbiased, or signed before observation. A good sampling tool should surface denominator failures, not quietly repair them after seeing results.
