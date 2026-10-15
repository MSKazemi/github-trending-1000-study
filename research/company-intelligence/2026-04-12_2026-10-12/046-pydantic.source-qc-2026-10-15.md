# Pydantic #046 — bounded source-check handoff (2026-10-15)

**Scope:** Assistant-performed primary-source spot checks for [issue #113](https://github.com/MSKazemi/github-trending-1000-study/issues/113) and the existing [26-row event ledger](046-pydantic.events.csv). **Not** an independent qualified human factual review or a reproduction of vendor functionality. Sources were read retrospectively on October 15; historical signed response snapshots, source-search denominators, installed-version tests, legal review and actual user outcomes remain unavailable.

## Source facts and falsification boundaries

| First-party source | Narrow source-supported observation | What cannot be inferred |
| --- | --- | --- |
| [Pydantic AI v2 launch, 2026-06-23](https://pydantic.dev/articles/pydantic-ai-v2) | The company announces the capability/hooks API, a distinct Harness layer, opt-in long-tail providers and a reduction from six to **three months** in the between-major-version no-breaking-change policy. | Feature announcement is not measured compatibility or productivity for third-party agents; the author's asserted no-break experience is not an independently reproduced cohort. |
| [Monty incident postmortem, 2026-05-07](https://pydantic.dev/articles/hack-monty-postmortem) | The company acknowledges successful sandbox escape/secret exfiltration in its contest, associated with unsafe Rust/garbage-collection-root invariants, followed by a patch. | A patch and internal postmortem do not demonstrate that all later sandbox versions are safe, or that `pydantic-ai` itself shares the same isolation property. |
| [PydanticAI official advisory index](https://github.com/pydantic/pydantic-ai/security/advisories) and [GHSA-6fqq-452j-qhrp](https://github.com/pydantic/pydantic-ai/security/advisories/GHSA-6fqq-452j-qhrp) | The upstream index identifies an October 2, 2026 high-severity advisory concerning concurrency-limited model streams and resource release. | Advisory publication does not establish live exploitation frequency or quantify security losses; package/license/version applicability needs separate release-specific verification. |

**Chronology rule:** the postmortem date is May 7, not the April 20 bounty announcement date; a later edit to the April article is not proof that the vulnerability or fix was already publicly known on April 20. June 23 is an *announcement/public-release claim*, not an independently executed test. Keep two sources about one release in the same event group; avoid counting independent URL count as independent functionality replication.

## Concrete reuse experiment for the maintainer (unexecuted)

Take 12 **pre-frozen, synthetic-only** typed tool-call tasks in an isolated repository; compare the *existing* hand-written argument validation with a version-pinned PydanticAI capability-based implementation using the **same** task specification, independent invalid-input and unauthorized-action tests. Retain the full task denominator, including refusals, failed patches and reversions. Measure accepted functional outcomes, schema rejection errors, review/repair minutes, migration burden over a supported major upgrade and dependency vulnerability/license findings. Stop before deployment on any unauthorized action, secret/PII egress, incompatible rights or unreviewed migration. Do not treat synthetic green tests as real-user benefit, energy savings or safety certification.

## Reviewer request and status

A qualified non-author reviewer still must check primary artifact timestamps, exact release/affected versions, policy/licensing, publisher identity, duplicate groups, negative findings and the M1–M7 construct mapping. The seven-month event search remains **purposive, not exhaustive**. **Keep PR #303 in draft and issue #113 open** until its stated review/promotion gates are met; this assistant's spot check is not independent human approval.

**Practical lesson:** pair every typed-agent release story with a failing unauthorized-input test and version-pinned upgrade/repair budget. Recording regressions or unknowns is more useful than inferring production reliability from product publicity.
