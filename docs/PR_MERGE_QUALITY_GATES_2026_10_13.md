# PR merge quality and research-integrity review — 2026-10-13

**Status:** engineering review record, NOT scientific signoff, external security certification, completed sampling, or evidence of real sustainability outcomes. Tracker: [#248](https://github.com/MSKazemi/github-trending-1000-study/issues/248).

## Evidence and decisions

During this review, the GitHub main branch metadata reported **protected=false**. The original CI ran only the Python 3.10/3.12 unit-test suite. That is not enough to ensure independently reviewed enterprise-quality merges, source authentication, or scientific approval. GitHub permissions for branch rules are not exposed by the connected review actions. An authorized repository owner must configure and verify rules separately.

The active PR inventory after the merges below was **44 open, all drafts** (point-in-time, subject to concurrent changes). Draft research/source screens must remain drafts until their independently verified source/date/consent/method gates are satisfied. A green synthetic unit test does not make a provisional company claim or human-subject observation publishable.

| PR | Reviewed action | Technical and science boundary |
|---|---|---|
| [#239](https://github.com/MSKazemi/github-trending-1000-study/pull/239) | **Merged**, squash [7efb2a8](https://github.com/MSKazemi/github-trending-1000-study/commit/7efb2a8fdc042999745263228c0f8631c9f613ed). Four GitHub Actions checks passed on final head (Python 3.10 and 3.12). | Fixed malformed GitHub URLs, unrecorded filter paths and invalid type handling. A concurrent merge brought independently useful exact query allowlisting and a 1,000-rank cost bound; both sets of source, tests and documentation were retained through explicit reconciliation. Still no authenticated Trending page data or independently verified utility effects. |
| [#241](https://github.com/MSKazemi/github-trending-1000-study/pull/241) | **Merged**, squash [af898e6](https://github.com/MSKazemi/github-trending-1000-study/commit/af898e626c2ff0a51ee07ff0d687522e17544a93). Four GitHub Actions checks passed on final head. | Requires a clean HTTPS source URL before a literature record can be marked included, while pending leads may remain unlinked. URL syntax is NOT DOI/source authenticity, peer review or scientific truth. |
| Concurrently merged #170, #182, #190, #208, #218 and #219 | Recorded as merged on GitHub during review; not claimed to have received independent domain approval through this session. | Preserve their original empirical source, task, reviewer, consent, and environmental measurement blockers. A merge is an engineering action, not data acceptance. |

### Mandatory review checklist

1. Read the **complete PR diff** against the latest main, compare with overlapping PRs and file inventories, preserve useful source leads/tests/documents before merging.
2. Inspect security, privacy, untrusted input paths and URLs, overwrite rules, third-party code execution risks, source licensing and permission.
3. Confirm methodology and denominators: stable repository identities, event UTC provenance, independent task acceptance, reviewer evidence, missing versus zero, negative/null findings, no synthetic-as-observed conversion.
4. Require CI on the **exact final PR head**: Python 3.10/3.12 unit tests plus syntax, bundled JSON integrity and CLI smoke checks once the enhanced workflow is merged. Rerun after base reconciliation; check main after merge.
5. Require a non-draft, mergeable, fully reviewed PR with all blocking comments resolved. Merge with an expected head SHA, not an earlier green commit; never force main or delete source material to hide conflicts.
6. Update documentation, tests, contracts and provenance together. Record why something was rejected, preserved or replaced in the canonical module, and disclose AI assistance.
7. Obtain separate qualified **human** research/ethics/security signoff when required. Code and CI checks cannot authenticate participants, evidence, GitHub origin, package trust, or complete CO2 lifecycle boundaries.

### CI improvements included with this review record

The companion workflow update preserves the existing test job name and both Python versions, while adding standard-library Python compilation of source/tests, JSON parsing for examples and references with duplicate-key and nonstandard-number rejection, CLI entrypoint smoke checks, and a bounded job timeout. No live scraping, package installation or test dependence on provider network connectivity is added.

**Remaining limitations:** no automated static typing or vulnerability scan, test-coverage target, signed provenance of third-party research sources, realistic performance tests or end-to-end live data QA. The currently tagged checkout/setup-python GitHub Actions require a separate verified immutable-SHA pinning review; do not guess action hashes.

### Required GitHub-owner action

Configure and verify a repository ruleset covering main: require a PR, at least one independent human approval, dismiss stale approvals, require resolved conversations and the two named Python CI checks, prohibit force-push/delete and restrict direct pushes. Consider CODEOWNERS for research protocol/security-critical modules, plus documented emergency exceptions. The branch-protection state must be checked after an authorized admin changes the settings. This tool did not enable branch protections.

### Practical reusable-code lesson

Protect quality and research provenance before scaling agent contributions. One reviewed, reusable implementation with independently accepted user outcomes and complete cost/safety accounting is preferable to multiple conflicting generated branches. Successful CI, popularity and PR volume do not prove real reuse or green impact.
