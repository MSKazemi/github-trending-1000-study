# Source-access decision: GitHub Trending capture defaults to blocked (2026-10-13)

**Status:** engineering stop gate implemented in a proposed PR, **not** independent legal, platform or scientific signoff. **Research stage:** method/pilot preparation, no live Trending study captures in this decision. **Primary issue:** [#2](https://github.com/MSKazemi/github-trending-1000-study/issues/2); related protocol [#27](https://github.com/MSKazemi/github-trending-1000-study/issues/27).

## Decision and evidence

**Decision: NO-GO for this repository's automated live `/trending?since=...` capture until documented human source-access clearance and a reviewed code/protocol amendment.**

1. The [GitHub-published robots.txt](https://github.com/robots.txt), in the public response available for the 2026-10-13 audit, contains `User-agent: *` followed by `Disallow: /*since=*`; the current collector constructs `https://github.com/trending?since=daily|weekly|monthly`. **The available web retrieval may be cached; its exact current live deployment and interpretation must be rechecked by the responsible human before any authorization.** A robots rule is not a complete legal opinion and an explicit one-off human browser visit is not automatically identical to a crawler.
2. The [GitHub Terms of Service](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service), effective April 27, 2026, and applicable platform, API, rate and redistribution policies must be considered by the study's responsible operator. A publicly readable page or an application with working code does **not** independently establish research access rights.
3. Existing [README access guidance](../README.md), [ethics](ETHICS.md), [preregistration draft](PREREGISTRATION_DRAFT_2027.md) and [pilot-preflight pending gates](PROTOCOL_FREEZE_STATUS_2026_10_12.md) clearly recognize the missing review, but the prior `capture` implementation could still send a request without any completed permission decision. This discrepancy is an actionable code-level safety defect.
4. **No granted access letter, permissible cadence decision, signed human reviewer approval, real source capture, genuine human 30-row QA or frozen protocol was supplied or inferred during this audit.** Neither the author's control of this repository nor AI-generated text proves GitHub authorized the proposed data collection.

## Implemented preventive control

The `trending_study capture` entry point now calls `require_trending_source_access()` **after path/date checks and before network access**. In this revision that function always raises a clear error. It has **no CLI flag, token, environment variable or JSON-card override**. A hypothetical “I approved it” checkbox cannot lift the gate. Re-enabling requires an explicit subsequent source-code PR, not a quiet runtime bypass.

- **Expected behavior for valid current-day paths:** error exit code 2, zero network requests, no newly written capture or manifest files. Invalid/colliding output paths still fail with their original deterministic write-once errors.
- **Offline support retained:** local `parse-trending`, source-hash/manifest `pilot-parse`, `audit-pages`, synthetic fixtures, and independently lawful official GitHub REST API workflows. Existing read-only parsing remains explicitly **not** confirmatory cohort evidence.
- Synthetic unit tests are allowed to mock `require_trending_source_access` **only while `urlopen` is also mocked** to exercise the unchanged manifest logic. Such a test is not a documented permission decision. No live GitHub network request is made by CI.

The gate intentionally protects the **default** study workflow rather than asserting what every conceivable manual action on GitHub legally permits. It does not create a defense against somebody changing and redistributing the source code: that is why reviewed governance and upstream permission remain necessary.

## Path to lawful evidence, without silently changing research questions

**Option A — written permission or method accepted by the platform.** A human reviewer obtains and archives an externally verifiable permission/access decision for the exact requested page URLs, time windows, frequency, user agent, geographic scope, data retention/redistribution and expected volume. A methods/statistical reviewer then approves the corresponding prospective sampling plan. Only after these steps should a carefully scoped re-enable PR be considered. Live source validity still requires raw capture/manifest provenance and **at least 30 real independently hand-reviewed displayed entries** across authorized surfaces, with explicit coverage, rank and parser-rejection outcomes.

**Option B — platform-supported REST API and/or GH Archive.** These can provide useful project metadata or public events under their own API/access conditions and make a different reproducible study possible. **They do not reproduce GitHub's opaque Trending algorithm, daily rank, or historical Trending exposures.** Study A's sampling frame, selection estimand, missingness, control population and any confirmatory hypothesis must be amended and prospectively reviewed; never relabel API-sampled repositories “observed Trending.” Study B's opt-in task/reuse experiment may be advanced separately with its own independent task, acceptance and consent gates.

**Option C — negative feasibility result.** If rights, source completeness or power cannot be established, publish a transparent methodological feasibility/blocked-source conclusion rather than backdate artificial Trending captures, fabricate a 1,000-repository cohort or infer causal green-coding lessons.

## Checklist for a future re-enable review

- [ ] Human reviewer confirms **current** GitHub robots, Terms and appropriate platform support/permission evidence at actual decision time.
- [ ] Authorized exact URL/window/language surfaces, frequency, allowed collection method, request headers, rate bounds, privacy, retention and downstream reuse are written down and independently reviewed.
- [ ] A dated signed study protocol amendment reconciles the 3 implemented unfiltered surfaces with the separately proposed 9-surface frame, enrollment dates, controls and statistical power.
- [ ] New tests prove default-deny on absent/stale/revoked source permission, no requests for disallowed surfaces, no uncontrolled retries, and preservation of source-byte immutability. Do not accept an unauthenticated self-declared boolean as definitive authorization.
- [ ] Prospective raw + SHA-256/UTC manifests and two genuinely independent annotators audit >=30 **real** source entries; report incomplete/rejected pages, ranks and all missingness.
- [ ] Independent ethics/methods and maintainer review completed before any cohort-eligible declaration. Passing synthetic CI is not any of these approvals.

**Scheduling note:** the previously proposed 2026-10-15 pilot and 2026-11-01 enrollment are conditional. If this gate remains blocked, record a new approved prospective timetable rather than converting old/unpermitted screenshots into baseline evidence.

## Practical lessons for other repositories

1. Put an irreversible **fail-closed permission gate in code**, not solely in an ethics document. Prefer a source-reviewed code amendment to a self-attested `--force` override.
2. Bind the observed source surface to its actual scientific estimand. Official APIs may be good alternatives, but they cannot magically reproduce a different ranking or historical observation.
3. Keep the no-network offline test path separate from field-data validation; a perfect unit suite does not authenticate source origin, rights, reviewer independence or real-world user value.
4. Block invalid research before it consumes developer/agent time, tokens or storage, while documenting a concrete legal next step and a meaningful alternative study.

*Drafted using AI assistance; this record is an attributable project engineering decision and a proposal for human verification, not an opinion or approval issued by GitHub or an independent institutional reviewer.*
