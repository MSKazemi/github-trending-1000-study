# Repository-wide scientific and software audit — 2026-10-12

**Status:** inspection report, not empirical research results, formal peer review, security certification or preregistration. **Review target:** `main` commit `d17b5e91b12407e4910ca180088c0b8372dd566c` plus outstanding PRs #34, #35, #38, #42 and #43. **Tracking:** [issue #44](https://github.com/MSKazemi/github-trending-1000-study/issues/44). Authored with substantial AI assistance; human validation and merge are required.

## Executive conclusion

**Engineering foundation: promising; scientific evidence readiness: not yet reached.** The repository implements principled offline, standard-library-only research helpers and differentiates verified observations from synthetic examples. It explicitly rejects the equivalence of GitHub Trending/stars with software usefulness and of tokens with kWh. The primary threats are **unfrozen research designs, missing real audit data, source-capture integrity, insufficient human gold judgments, and open but not yet integrated workflow PRs**. No 1,000-repository cohort, live human-reviewed Trending capture, independent code-reuse success sample, accepted-task randomized experiment, or net environmental saving is demonstrated.

**Decision:** continue methods development and narrow pilot preparation, **do not present observational/causal/green findings**, and do not commence confirmatory recruitment until documented independent review and source permissions pass.

## Coverage and independent verification

| Evidence surface | Audited state | What this means |
|---|---|---|
| Repository inventory | 85 tracked files, 13 directory tree entries on `main` | 7 Python modules, 6 Python test modules, 46 research Markdown docs, 5 reference JSON registers, 6 templates, 1 CI workflow |
| Real empirical data | `data/raw` and `data/processed` each contain only `.gitkeep` | No actual study observation cohort committed; PR #38 has convenience-sampled *public issue leads*, not adjudicated tasks |
| Latest `main` CI | [run 38224561557](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38224561557): Python 3.10 and 3.12 successful; Python 3.12 log says **44 tests** | Offline/synthetic functionality tested; not a live parser QA, ethics check or statistical result |
| Recent unmerged judgment PR | [run 38228419415](https://github.com/MSKazemi/github-trending-1000-study/actions/runs/38228419415): successful matrix; Python 3.12 log says **67 tests** | Tests pass at PR head; identified interface edge case below still needs regression coverage |
| Pull requests | 5 open: #34, #35, #38, #42, #43; no submitted reviews found | They are **not on main**; GitHub currently reports #34/#38 non-mergeable and #35/#42/#43 mergeable—recheck after base moves |
| Issues | P0 scientific/source gates #2, #3, #4, #21, #22, #23, #25, #27 and other research items remain | Do not mark tasks implemented merely because a proposal document or synthetic unit test exists |
| Local Markdown references | 52 file inspections (51 distinct paths), 501 parsed links, including 316 relative paths; none resolved to a missing tracked path in this simple check | **Not** a full GitHub anchor or external-link validity check; nested Markdown and dynamically generated links are not exhaustively parsed |
| Bibliography and figure registers | JSON parses successfully; 35 + 16 + 15 + 12 curated research/strategy sources (78 records), and 32 planned figure/table entries (18 F, 14 T); no duplicate IDs within a register | Only a **spot-check** of external scientific assertions was performed; complete DOI/version/date screening is still needed per #7/#13 |
| GitHub protection/security settings | Repository rulesets endpoint returned `[]`; main branch protection endpoint returned HTTP 403 ("Resource not accessible by integration") | No conclusion can be drawn about all protections; repository owner must check required reviews/status checks manually |

**Tool limitation:** the auditing environment could read the live connected GitHub repository and GitHub Actions logs, but an independent container `git clone` failed because that container could not resolve `github.com`. The full checked-out suite was therefore **not locally rerun by this audit**; the above test counts come from GitHub's reported job logs. No network/security penetration test was performed.

## Severity-ranked finding register

Priority is **risk to scientific data integrity or publication readiness**, not demonstrated exploitability.

| ID | Priority | Type | Evidence and consequence | Owner/fix tracker |
|---|---|---|---|---|
| A01 | **P0** | Verified source-code overwrite hazard | `trending_study/__main__.py:capture` writes `Path(args.output).write_bytes(raw)` with no exclusive-create check, and writes the manifest separately. Reusing a capture path can destroy a previous raw source. `parse_trending` permits `--input` and `--output` to be identical, so it can replace raw HTML with JSONL. This contradicts immutable capture provenance. | [#4](https://github.com/MSKazemi/github-trending-1000-study/issues/4); regression tests and fail-closed exclusive/staged writes |
| A02 | **P0** | Parser validity not established | `extract_repos` raises only on **zero** extracted entries. Layout drift can yield a positive but **incomplete** subset: checksums confirm captured *bytes*, not rank/row completeness. Current primary HTML fixture contains only two synthetic entries. The pilot audit correctly labels QA pending. | [#2](https://github.com/MSKazemi/github-trending-1000-study/issues/2); independently compare ≥30 real entries across permitted surfaces, inspect page count, malformed/skipped/duplicate rows and rank discrepancies |
| A03 | **P0** | Missing prospective authorization | `docs/PREREGISTRATION_DRAFT_2027.md` explicitly says **not frozen/registered**; `docs/PROTOCOL_FREEZE_STATUS_2026_10_12.md` lists 11 unresolved collection/ethics/statistical approval gates. Proposed 2026-11-01 enrollment is conditional, not an entitlement to backdate. | [#27](https://github.com/MSKazemi/github-trending-1000-study/issues/27), [#3](https://github.com/MSKazemi/github-trending-1000-study/issues/3), [#13](https://github.com/MSKazemi/github-trending-1000-study/issues/13); independent signoff and preanalysis freeze |
| A04 | **P0** | No observational cohort/power analysis | No verified 1,000 distinct repo IDs, longitudinal 30/90/180d follow-ups, independent non-Trending control frame, valid filtered-language panel or prespecified enrollment manifest in `main`. "1,000" is a target only. | [#2](https://github.com/MSKazemi/github-trending-1000-study/issues/2), [#3](https://github.com/MSKazemi/github-trending-1000-study/issues/3), [#4](https://github.com/MSKazemi/github-trending-1000-study/issues/4), [#15](https://github.com/MSKazemi/github-trending-1000-study/issues/15) |
| A05 | **P0** | No independently validated reuse gold set | `goldset.py` processes **supplied** labels; a "viable" checkbox is not true functional/legal/security proof. Real task specs, frozen independent hidden tests, true source-time eligibility, reviewer independence and multi-channel deep audit remain unverified. | [#21](https://github.com/MSKazemi/github-trending-1000-study/issues/21), [#22](https://github.com/MSKazemi/github-trending-1000-study/issues/22); PRs #38/#43 are useful **tools**, not completed human audits |
| A06 | **P0 before any environmental claim** | No physical footprint comparison | No paired end-to-end human/CI/model/runtime/maintenance measurements; cloud energy may be inaccessible. ISO SCI and net lifecycle boundaries are discussed appropriately, but token counts cannot establish energy/carbon savings. | [#18](https://github.com/MSKazemi/github-trending-1000-study/issues/18), [#23](https://github.com/MSKazemi/github-trending-1000-study/issues/23); measured vs modeled vs unknown |
| A07 | **P1**, confirmed cross-module logic conflict | `#43` blinded-review → gold-set contract | If a candidate is `not_viable` **only because availability fails** (released after task baseline), `blind_review._judgment` accepts that decision among its five gates. The exported `goldset_input` omits the availability gate. Existing `goldset.evaluate` requires a failed one of the other four gates for `not_viable` and rejects this valid temporal-negative case. This is a **static code-path demonstration**, not an executed real-data test. | [PR #43](https://github.com/MSKazemi/github-trending-1000-study/pull/43) audit comment; add cross-module regression and preserve temporal reason explicitly |
| A08 | **P1** | Integration and review debt | #34 prospective task allocator, #38 public issue intake, #43 blinded-review, #35 source watch and #42 AI-era mission remain in separate open PRs. No submitted review found; #34/#38 were reported non-mergeable at time of audit. Neither successful branch CI nor a written plan means the capability has reached `main`. | Rebase each against current `main`, resolve conflicts, review methodology, merge in dependency order, rerun entire suite |
| A09 | **P1** | Unfrozen/multi-version protocol interfaces | Visibility `docs/PROTOCOL.md` v0.1, `STUDY_DESIGN.md` and draft v0.3, task-reuse extensions and `DATA_DICTIONARY.md` v0.1 coexist. The legacy parser produces `schema_version=0.1` and `pilot-parse` emits `pilot-1.0`, with additional fields not normalized into a single versioned schema. These are documented, but consumers must not silently coerce cohorts. | [#13](https://github.com/MSKazemi/github-trending-1000-study/issues/13), [#27](https://github.com/MSKazemi/github-trending-1000-study/issues/27); explicit canonical protocol + validated schema migration |
| A10 | **P1** | Limited CI scope | Current workflow only runs Python unittest on 3.10/3.12. No automated real-page parser QA, HTML drift alarm, schema contract matrix, Markdown checking, coverage threshold or static analysis in this workflow. A unit pass does not establish correctness of live sampling or real human inference. | [#2](https://github.com/MSKazemi/github-trending-1000-study/issues/2) plus separate CI-improvement task after source QA |
| A11 | **P2** | Onboarding/version drift | `README.md` still shows a fixed `2026-10-11` live capture example that fails on later UTC dates; a newer valid `UTC_DAY="$(date -u +%F)"` + manifest SOP appears later. Package `trending_study.__version__` is `0.1.0` while CLI `VERSION` is `0.2.0`. | Consolidate README to dynamic UTC/date+manifest commands; synchronize versions; avoid publishing obsolete quickstarts |
| A12 | **P2** | Distribution/reuse polish | The repository works through `python -m ...` from root but has no published package metadata/console-script installation declaration in the audited tree. README is long and splits mission across older attention RQs vs newer reuse-first direction; PR #42 already addresses strategic/maintainer clarity. | Review [#42](https://github.com/MSKazemi/github-trending-1000-study/pull/42); add a five-minute researcher path and optional packaging only after first verified workflow |
| A13 | **P2** | Reference assurance | Registers are correctly labeled *curated/not systematic*, but most source records still require reproducible bibliographic screening and source claim-to-page mapping before academic claims. GitHub/Stack Overflow blog/survey statements must not be presented as peer-reviewed causal estimates. | [#7](https://github.com/MSKazemi/github-trending-1000-study/issues/7), [#13](https://github.com/MSKazemi/github-trending-1000-study/issues/13) |

### Concrete non-destructive regression scenarios for A01/A07

For A01, in a **throwaway temporary directory only**, copy `tests/fixtures/trending.html` to `raw.html`, then pass that same disposable file as `--input` and `--output` to `python -m trending_study parse-trending --date 2026-10-12 --window daily`. From the inspected implementation, this replaces the HTML input with JSONL. **Never try this on actual study data.** The expected fixed behavior is an error **before any write**, and a unit test asserting original bytes remain unchanged. Separately test duplicate capture output and manifest collisions, partial writes, retry and crash recovery.

For A07, create a synthetic task with baseline before component release; candidate's **only** failed gate is `availability`, both reviewers say `not_viable`, and all four legacy gold-set gates say `pass`. Run `blind_review.audit(...)` then `goldset.evaluate(result["goldset_input"])`. The conversion currently produces no failed legacy gate and the latter rejects it. Add an explicit temporal-availability dimension to the shared schema or a separate upstream rejection category; **do not falsify a functional failure** to satisfy an older validator.

## Open PR disposition, not merge authorization

| PR | Subject | At audit | Recommendation |
|---|---|---|---|
| [#34](https://github.com/MSKazemi/github-trending-1000-study/pull/34) | Synthetic task frame/randomized allocation/ITT ledger | Open; connector reported non-mergeable; unreviewed | Review assignment concealment, exclusion/cluster balance and frozen tests; resolve base drift |
| [#35](https://github.com/MSKazemi/github-trending-1000-study/pull/35) | Time-scoped literature and news monitoring | Open; reported mergeable; unreviewed | Verify DOI/venue/version claims before merging source registry |
| [#38](https://github.com/MSKazemi/github-trending-1000-study/pull/38) | Small real public issue-lead intake | Open; reported non-mergeable; unreviewed | Preserve **convenience/truncated** source-frame caveat; ensure intended users do not call issue leads accepted tasks |
| [#42](https://github.com/MSKazemi/github-trending-1000-study/pull/42) | Modern AI-era research and practical maintainer mission | Open; reported mergeable; unreviewed | Accept only as proposed framework, reconcile with primary protocol; useful front-page clarity |
| [#43](https://github.com/MSKazemi/github-trending-1000-study/pull/43) | Blinded candidate packet + adjudication | Open; reported mergeable; unreviewed | Add availability-only nonviable integration test; real reviewer independence and evidence remain external |
 
## Strengths worth preserving

1. Honest `not_ready`, `unknown`, `not_enrolled` and self-report disclaimers throughout offline tools; no claimed 1,000 actual observations.
2. Real UTC/SHA capture manifest design, exact Trending URL check in strict pilot mode, and explicit separation of capture from parse time.
3. No external Python runtime dependencies for the current command-line utilities; secrets excluded in `.gitignore` and `data/raw`/`data/processed` ignored.
4. Tests for malformed HTML, synthetic capture tampering, metadata and consent gate placeholders; GitHub Actions uses limited `contents: read` permissions.
5. Clear separation between attention, independently verified user benefit, agent attribution, supply-chain risk, developer time and physical energy—stronger than star-count storytelling.
6. License, maintainership externalities, right to reuse, research privacy and null results are addressed in methods rather than ignored.

## Scientific source spot-check (NOT full bibliography review)

- Official [ISO/IEC 21031:2024](https://www.iso.org/standard/86612.html) is indeed titled *Information technology — Software Carbon Intensity (SCI) specification* (2024-03); the study must still measure/justify every emissions input and functional unit.
- Official [Stack Overflow Developer Survey 2026 agent question](https://survey.stackoverflow.co/2026/ai/data/ai-code-agent) reports Claude Code 65.5%, GitHub Copilot 58.7%, Codex 29.5% for **12,255 respondents to that multi-select question**. These are **not worldwide agent-usage prevalence, repo-level authorship, causal productivity or equivalent agent categories**. The related source-register caveat is appropriate.
- No blanket validation of the other ~76 bibliography records, persistent DOI links, paywalled texts, benchmark extraction or full standard text is claimed.

## Concrete readiness roadmap — gates, not promised dates

| Order | Required deliverable | Proof necessary to close | Existing tracker |
|---|---|---|---|
| 1 | Prevent destructive overwrite + audit true parsing | No-overwrite tests, safe file transaction, permitted real-page ≥30 manual entries with completeness metrics | #4 / #2 |
| 2 | Decide one canonical protocol/measurement dictionary | Named methods lead, reconciled Study A and B endpoints, amended conditional dates, clear version and signed preregistration | #27 / #13 / #3 |
| 3 | Finish task intake→blind review→gold-set compatibility | All three modules reviewed, availability case tested, exact candidate versions and privacy/reviewer evidence independently checked | #21 / #22 / PRs #38/#43 |
| 4 | First opt-in permission-safe real **pilot**, not a confirmatory trial | Prospective task frame and frozen independent acceptance suite; failures/no-reuse tasks retained; full audit ledger | #21 / #25 |
| 5 | Size and analyze the planned cohorts or amend N | True IDs, unbiased recruitment frame accounting, control sampling, attrition and prospective measured dates | #3 / #4 / #15 |
| 6 | Measure end-to-end effort and any environmental sub-study | Task equivalence, human-time and CI/provider telemetry, emissions boundary with uncertainty, upstream support costs | #10 / #18 / #23 / #24 |
| 7 | Publish an evidence-graded lesson and replication package | Independently verified results, effect size/CI, applicability and negative conditions; no star-only claims | #8 / #11 / #12 |

**Stop rule:** if raw-source provenance, permissions, independent acceptance tests or statistical estimand cannot be validated, publish an honest feasibility/negative-methods result and **do not silently proceed to confirmatory inference**.

## Practical lessons the maintainer can use on other repositories *today*

These are **engineering actions to test**, not claims that they increase stars by a measured percentage:

- Start each repository with the specific external user task and a 5-minute clean-room runnable example; ask an uncoached second person to try it and log success/failure.
- Search the existing local code, package registries and upstream projects *before* generating a new implementation. Record a time-boxed alternative, exact version, license, advisories and why the choice passes a frozen task.
- Prefer small composable APIs, reproducible releases, a clear `LICENSE` and `SECURITY` channel when risk justifies one, supported-version matrix, and tests that exercise failure modes.
- Treat GitHub stars and Trending as **discovery**, not adoption. Record independently verified installations, downstream integrations, reproducible research reuse and 30/90-day maintainer burden where permissions permit.
- Set the same no-overwrite/provenance invariants for code/data generation in every repository; green engineering starts with not destroying or regenerating trustworthy work.
- Never present tokens or lines saved as carbon saved; pair equivalent accepted outcomes with a defensible lifecycle/resource boundary.
- Work through bounded, reviewed PRs with CI, a genuinely tested first-run command and evidence/limitations in the docs; keep unmerged roadmap work labeled *proposed*.

**Audit outcome:** complete source inventory and reasoned issue triage; **not** permission to merge any pending scientific method change automatically. Update this record with the eventual fix commit/CI result/human approval for each item.
