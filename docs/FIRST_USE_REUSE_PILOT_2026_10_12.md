# First-use reuse-before-generation pilot: one existing GitHub repository

**Design recorded:** 2026-10-12. **Issue:** [#83](https://github.com/MSKazemi/github-trending-1000-study/issues/83). **Target:** [MSKazemi/github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study), source reference `4d524c460e6992f08fbc57118cdbd9962feb2098`. **Status:** automated synthetic engineering demonstration and independently evaluable *task proposal*, **not** a recruited user trial, randomized experiment, independent blinded acceptance or completed 2027 data collection.

## Why this is worth doing — without reimplementing existing software

A future researcher should be able to take a saved HTML file and identify listed GitHub Trending repositories, original displayed ranks and exact source bytes without online access. The public project **already has** an offline parser and write-once output behavior; an additional standalone parser duplicates functionality without evidence of better user outcomes.

This narrow task operationalizes [reuse before generation](REUSE_FIRST_PLAYBOOK.md) and the conditional [2027–2031 software strategy](STRATEGIC_TECH_OUTLOOK_2027_2031_2026_10_12.md) (the latter is currently in [PR #60](https://github.com/MSKazemi/github-trending-1000-study/pull/60), not necessarily on main). It does not modify the original [study protocol](PROTOCOL.md), [all-task trial](REUSE_FIRST_EXPERIMENT.md), or [independent gold standard](REUSE_GOLD_STANDARD_2027.md).

## U01 — frozen proposed first-use task

| Property | Exact design |
|---|---|
| External user intent | Given **locally saved** Trending HTML, obtain a ranked, auditable JSONL list without contacting GitHub or other services |
| Scope | Supported `article.Box-row` fixture layout only, unfiltered daily view, CLI executed from source checkout with Python 3.10+ |
| Synthetic input | Existing checked-in `tests/fixtures/trending.html` with two fictional repositories and a non-repository footer link |
| Acceptance names (in source order) | `alpha-org/first-project`; `example-user/another.repo` |
| Acceptance ranks | Exactly `[1, 2]`, with no spurious footer entry |
| Byte evidence | Every emitted `source_sha256` equals SHA-256 of the unchanged input file; actual source provenance from GitHub **not** authenticated by a hash |
| Critical non-claim | Every row must state `capture_time_status=unverified_parse_only` and `eligible_for_confirmatory_cohort=false`; supplied `--date` does not prove capture time |
| Summary | Exactly two occurrences and two distinct *displayed names*; not two authenticated immutable repository IDs |
| Negative gates | Malformed supported row must fail with no output; output path already occupied must fail without overwriting |
| Evaluator | Project-authored, fully visible offline tests in `tests/test_first_use_reuse_pilot.py`; a genuinely independent evaluator/hidden holdout does not yet exist |
| Follow-up | Future humans with consent, independent acceptance and platform permissions; no current adoption or energy measurement |

**Do not reinterpret synthetic names, operator-supplied dates, self-authored test assertions, or CI success as authentic GitHub observation, independent task utility, legal clearance or environmental benefit.**

## U01 — reproduce it, without installing extra dependencies

From a clean checkout at repository root (no private credentials or network needed):

```bash
python -m unittest discover -s tests -p 'test_first_use_reuse_pilot.py' -v
python -m trending_study.reuse_gate --input examples/first_use_reuse_pilot.example.json
python -m unittest discover -s tests -v
```

For a human-readable manual CLI demonstration on a POSIX shell, use a new temporary path so research artifacts are not overwritten:

```bash
tmp_dir="$(mktemp -d)"
python -m trending_study parse-trending \
  --input tests/fixtures/trending.html \
  --date 2026-10-12 --window daily \
  --output "$tmp_dir/parse-only.jsonl"
python -m trending_study summarize --input "$tmp_dir/parse-only.jsonl"
```

The date here is a **fictional fixture metadata label**; the command performs parsing only. For a genuinely captured source, see [manifest/permission preflight](PILOT_CAPTURE_AND_PREFLIGHT.md) and [independent page QA](INDEPENDENT_PAGE_AUDIT_2026_10_12.md); U01 cannot replace those gates. Avoid rerunning the same output path: the existing CLI intentionally refuses overwrite.

## Reuse-versus-build decision (NOT comparative experimental results)

| Alternative | Engineering evidence as of this pilot design | Decision / unresolved risks |
|---|---|---|
| **A: existing `trending_study parse-trending` + `summarize`** | Existing CLI and test fixture inspected, published MIT license for original repository code, no new dependency needed for fixture; automated target tests now supplied | Preferred *candidate to validate*, **not independently approved**: real-world parser completeness, license obligations for specific downstream use, threat model and long-term maintenance still need scrutiny |
| **B: build a new bounded parser on Python `html.parser`** | Python stdlib primitive exists; no complete alternative implementation, accepted outcome, development-time log, security review or lifecycle metric obtained | **Not built or benchmarked**; only build if an independently verified gap justifies the extra maintenance and cost |
| **C: do nothing** | Does not deliver the stated JSONL end-user outcome | Negative alternative retained for value/cost decision, not a successful task |
| **Other libraries/old quiet OSS** | Not comprehensively searched; source universe incomplete | Search failures cannot prove no existing candidates; broaden discovery if U01 does not meet requirements |

The [machine-readable evidence card](../examples/first_use_reuse_pilot.example.json) intentionally leaves every candidate gate `unknown` and the existing `reuse_gate` must recommend `verify_existing_candidates`. This guards against converting an internal fixture test into a self-certified external success.

## How to convert U01 into actual 2027 science (after approvals)

1. **Independently sample tasks before searching** (include no-viable-reuse/abandoned tasks in the all-task denominator). U01 is a deliberately selected *reuse-positive demonstration*, so it must **never** be used to estimate average reuse-first treatment benefit.
2. Obtain rights/source-access and consent/privacy permissions for the actual trial. Independently write time-heldout tests; keep them outside evaluated agents' input.
3. For comparison, use the existing [2×2 protocol](REUSE_FIRST_EXPERIMENT.md) only if powered, preregistered and consented; normal workflows remain allowed to reuse. A new-build implementation is **not** artificially forced for a biased straw-man comparison.
4. Record exact task start/end UTC, source commit, Python/tool/model versions, human-active minutes, agent tokens when available, failed attempts, accepted functionality and independent evaluator signoff **per assignment**. Keep missing values `unknown`, not zero.
5. Measure true integration/security/license suitability, optional external first-run users and 30/90/180-day support/upgrade burden. Energy and carbon only with declared metering boundaries and uncertainty.
6. Report negative/null/inconclusive cases and upstream maintainer burden; do not extrapolate from this single fictional HTML file.

### Evidence and cost ledger (not fabricated)

| Construct | Status today |
|---|---|
| Real independent end-user attempts | **Not collected** |
| Consent, human eligibility, independent hidden acceptance | **Not obtained** |
| Correctness for internal synthetic fixture | **An automated test is proposed/committed**; consult actual PR CI results, not a claimed research outcome |
| New-build comparison results | **Not implemented / unmeasured** |
| Human elapsed/active minutes | **Not measured** |
| Model identity and tokens / provider costs | **Not measured** |
| kWh, CO2e, environmental rebound | **Not measured** |
| License-security-maintenance suitability for real downstream integration | **Unknown** |
| 30/90/180-day follow-ups | **Not observed** |

**A useful practical lesson (hypothesis, not measured causal effect):** before building a new parser, try the existing scoped CLI on a real independently defined user task, retain fail-closed provenance, and only code when a verified gap survives that check. The work intentionally reuses `trending_study.reuse_gate`, `parse-trending`, `summarize`, and the existing HTML fixture rather than adding an overlapping pipeline.

**No code-science conflation:** green CI can verify a deterministic engineering behavior; it cannot verify a human first-use result, reveal GitHub's opaque Trending algorithm, establish independently reproducible real-page recall, or establish carbon reductions.
