# Maintainers, human understanding, and social costs of reuse

**Status: proposed study extension; no new participant data collected.**

## The often-missed stakeholder: the upstream maintainer
Reuse may reduce downstream coding effort while shifting review, support, compatibility fixes, reports, and security work to maintainers. A project with many dependents can have only a few people supporting it. The net *social* benefit of reuse cannot be inferred from saved developer tokens or from forks/stars alone.

## Questions
- Does reuse-first reduce **combined** developer and upstream maintainer work, or merely shift it?
- Do coding agents create disproportionate low-value reports, patches, or support requests relative to accepted tasks?
- Can an independent new maintainer understand and extend the resulting software at 30/90 days?
- Does the project objective justify an independent implementation for interoperability, offline use, resilience, accessibility, education, or research reproducibility?

## Proposed measurements
| Construct | Metric or operational test | Caveat |
|---|---|---|
| Upstream support burden | Human review and support minutes attributable to consented integration | Public response timestamps cannot reveal actual effort |
| Review efficiency | Confirmed actionable upstream reports / all reports submitted in opt-in pilot | Manual blindness and category coding needed |
| Knowledge transfer | Fresh developer successfully repairs or extends the code in a timed, fixed task | Skill differences need blocking and repeat trials |
| Comprehension | Structured explanation of assumptions/risks graded by independent reviewer | Rubric must be piloted |
| Concentration risk | Critical ownership, maintainers and documented handover pathways | Commit-based bus factor is an imperfect proxy |
| Sustainability | Documented upkeep, release process, upgrade instructions and compatibility tests | Quiet projects can be stable and usable |
| Reciprocity | Meaningful upstream fixes, credit, improved docs, support or sponsorship when feasible | Not mandatory for all contexts; account for ethics |

## Required safeguards
Do not run uncontrolled agent PR or issue-submission experiments on uninvolved maintainers. Use sandboxes or explicit maintainer permission. Count downstream and upstream effort separately where only partial observation is possible, and mark missing upstream time unknown. Do not rank or disparage individual maintainers. Preserve correct source credits and license terms. Different project types have different public-good/learning values.

References: [Census III](https://www.linuxfoundation.org/press/open-source-usage-trends-and-security-challenges-revealed-in-new-study), [maintainer perspectives](https://www.linuxfoundation.org/blog/maintainer-motivations-challenges-and-best-practices-on-open-source-software-security), [CHAOSS Starter Health](https://www.chaoss.community/kb/metrics-model-starter-project-health/).

## 2026-10-16 bounded offline input and aggregate safety patch (issue #24)

**Proposed engineering correction, not real participant research:** The existing `trending_study.maintainer_burden` CLI previously read JSON using plain `json.loads(path.read_text())`, which could silently accept duplicate keys/nonstandard NaN, follow input symlinks or read unbounded nonregular files. It now reuses the **canonical strict, bounded, descriptor-checked read-only JSON loader** in `trending_study.data_integrity`, without a new parser or dependency. CLI errors do not echo private path names, JSON keys or participant identifiers.

A second check rejects cases where individually finite human-minute entries (`1e308` in an adversarial synthetic test) would sum to an `Infinity` aggregate. Both per-case and cross-case totals must remain finite, and overlarge direct Python integers fail with a controlled `BurdenError`. This prevents invalid nonstandard JSON output and fictitious infinite burden summaries without changing the formula, consent rule, or treating unknown as zero.

The additional tests use only temporary **fictional** data and exercise duplicate keys, NaN/Infinity, overflowing/underflowing numeric literals, symlinks, directories, and finite-input aggregate overflow. They cannot demonstrate real opt-in consent, authentic active-human time, independent task quality, source rights, sampling power, longitudinal causality or downstream/upstream net benefit. The accepted schema remains provisional; source-independent human/ethics/methods review is still required before any human study or public empirical claims.

**Practical maintainer lesson:** validate raw source bytes and arithmetic outputs, not only individual field values. A legitimate-looking finite input does not imply that a sum is representable or that research evidence was actually measured. Prefer the existing shared safe loader to inconsistent one-off JSON readers.

## 2026-10-17 privacy-schema integrity follow-up (issue #24)

A follow-up review of the same offline instrument found two additional **structural** fail-open cases: records with undeclared fields such as raw interview text or participant email were silently accepted, and two contradictory provenance flags (`synthetic` versus `not_empirical_data`) could produce misleading dataset classifications. That combination must not pass an instrument advertised as privacy-minimized or support a reproducible synthetic/empirical denominator.

The proposed v0.1 validator now requires **exact declared top-level case fields and five named outcome fields**, bounded opaque case/project/task/workflow identifiers, bounded status tokens, an explicit matching pair of synthetic indicators, and a bounded maximum case count. Embedded raw private notes, extra object fields, newline-bearing identity strings, nonsensical unhashable consent values and inconsistent synthetic flags fail with fixed messages. This does not establish true pseudonymity: a valid opaque token can still encode a person's identity, and raw input files must remain outside public Git unless independently approved.

The v0.1 input also rejects self-reported `human_review_state=approved` or `data_release_approval=approved`: **no ordinary input value or green test may mint qualified human approval**. Real signed methods/ethics verification and release authorization require an independently designed, versioned process. Existing real, consented-but-unverified pilot records can remain pending under the provisional schema, but must never be called approved for public release. The aggregate continues to return `independent_review_authenticated=false` and `approved_for_public_release=false`.

Seven synthetic adversarial test methods cover unknown sensitive top-level and nested fields, missing required fields, mismatched provenance flags, self-asserted approvals, unsuitable free text, unhashable status values, unbounded case counts, and privacy-safe CLI diagnostics. No real participants were contacted, no scraping/telemetry was enabled, and this patch is not evidence of project usefulness, avoided maintainer work, or net climate benefit. **Issue #24 remains open** for genuine opt-in study, ethics/source rights and independent human methods review.

**Practical lesson for your repositories:** reject *unexpected* fields at privacy-sensitive JSON boundaries, not just malformed values of the fields you happen to use. Cross-check redundant dataset-status flags and require out-of-band, auditable human signoff instead of trusting self-reported approval strings.
