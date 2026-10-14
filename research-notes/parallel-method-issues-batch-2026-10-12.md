# Parallel research-method issue batch — initiated 2026-10-12, reviewed 2026-10-13

**Repository:** [MSKazemi/github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study). **Historical batch status:** ten independently scoped PRs were opened; their then-current GitHub Actions checks were inspected on 2026-10-13 (Europe/Rome) before this note was appended. Later PR/head states require rechecking. This is **an execution record, not an empirical study, preregistration, completed issue acceptance or approval to merge**. Each issue stays open pending its own original acceptance criteria and human review.

## Ten bounded contributions

| Issue | Draft PR | Output | Evidence boundary |
|---|---|---|---|
| [#5](https://github.com/MSKazemi/github-trending-1000-study/issues/5) | [#187](https://github.com/MSKazemi/github-trending-1000-study/pull/187) | `trending_study/rubric_agreement.py`, synthetic tests and `docs/RUBRIC_AGREEMENT_INSTRUMENT_2026_10.md` | Kappa arithmetic only; not a human-blind 100-repo audit |
| [#6](https://github.com/MSKazemi/github-trending-1000-study/issues/6) | [#188](https://github.com/MSKazemi/github-trending-1000-study/pull/188) | `trending_study/trending_drift.py`, tests, `docs/TRENDING_DRIFT_OFFLINE_2026_10.md` | List-comparison logic only; no legitimate live Trending capture/hidden ranking recovery |
| [#7](https://github.com/MSKazemi/github-trending-1000-study/issues/7) | [#189](https://github.com/MSKazemi/github-trending-1000-study/pull/189) | `trending_study/literature_ledger.py`, tests, `docs/LITERATURE_SCREENING_LEDGER_2026_10.md` | No comprehensive databases searched/independent paper audit |
| [#8](https://github.com/MSKazemi/github-trending-1000-study/issues/8) | [#206](https://github.com/MSKazemi/github-trending-1000-study/pull/206) | `docs/INDEPENDENT_USER_TASKS_DESIGN_2026_10.md`, explicit synthetic task card | No real users, trial or consent |
| [#11](https://github.com/MSKazemi/github-trending-1000-study/issues/11) | [#208](https://github.com/MSKazemi/github-trending-1000-study/pull/208) | `trending_study/lesson_registry.py`, tests, `docs/LESSON_REGISTRY_AUDIT_2026_10.md` | User-supplied evidence, reviewers and code commit remain unverified |
| [#12](https://github.com/MSKazemi/github-trending-1000-study/issues/12) | [#210](https://github.com/MSKazemi/github-trending-1000-study/pull/210) | `docs/ADOPTION_MAINTENANCE_EVIDENCE_DESIGN_2026_10.md` and synthetic signals | No real downstream or longitudinal adoption observations |
| [#15](https://github.com/MSKazemi/github-trending-1000-study/issues/15) | [#211](https://github.com/MSKazemi/github-trending-1000-study/pull/211) | `trending_study/quiet_reuse_frame.py`, tests and synthetic independent sampling frame | Registry completeness, seed randomness and inclusion weights not verified |
| [#18](https://github.com/MSKazemi/github-trending-1000-study/issues/18) | [#214](https://github.com/MSKazemi/github-trending-1000-study/pull/214) | `trending_study/energy_boundary.py`, tests and `docs/ENERGY_BOUNDARY_INSTRUMENT_2026_10.md` | No actual energy meter/provider power data; single grid scenario cannot imply full CO2e |
| [#22](https://github.com/MSKazemi/github-trending-1000-study/issues/22) | [#216](https://github.com/MSKazemi/github-trending-1000-study/pull/216) | `trending_study/package_review.py`, tests and `docs/PACKAGE_IDENTITY_PREINSTALL_GATE_2026_10.md` | Does not resolve real registry/licensing/security attestations or approve installation |
| [#24](https://github.com/MSKazemi/github-trending-1000-study/issues/24) | [#217](https://github.com/MSKazemi/github-trending-1000-study/pull/217) | `docs/UPSTREAM_MAINTAINER_BURDEN_PILOT_2026_10.md` and synthetic record; this batch audit note | No maintainers contacted or actual support minutes measured |

**Execution method:** each branch started independently from `main`, one core issue per draft PR; source-only offline tools use the Python standard library and fail closed on important unknown/malformed inputs; no live scraping or downloaded dependency execution. GitHub's `.github/workflows/ci.yml` uses `python -m unittest discover -s tests -v` on Python 3.10 and 3.12. Each of the ten PR heads had a **successful** workflow result when inspected immediately before recording this note; subsequent commits require fresh CI verification. A passing CI run is *not* independent scientific validation.

## No-go conditions not discharged by this batch

- No independent full-page human Trending QA, legitimate live capture permission or signed cohort protocol.
- No consent, blinded external developer acceptance, actual 50+ task/component independent review or real longitudinal outcome.
- No authentic DOI-corpus coverage, peer-review conclusions, actual kWh, calibrated emissions or verified license/security trust decisions.
- No causal evidence that coding agents improve net reuse, useful output, organic discoverability or sustainability.
- No PR merged or issue closed on the strength of synthetic fixtures alone.

## Five testable 2027 maintainer lessons

1. **First-use acceptance over stars:** define a runnable external-user task and compare validated success, not README length or GitHub Trending position.
2. **Evidence conservation:** code-reuse search failures do not prove no suitable library; use a source, version, license, tested task and explicit unknowns before creating new code.
3. **Reproducibility before growth:** preserve cohort IDs/time/source hashes, holdout windows and screening denominators; no retrospective reconstruction of earlier data.
4. **Human and upstream costs count:** measure review, support, retries, upgrades and failed attempts rather than treating token volume or PR count as useful productivity.
5. **Green claims need full boundary:** collect local/CI/runtime/provider/embodied costs with known provenance and sensitivity; do not convert tokens to carbon or assume unknown energy is zero.

These are **candidate practices or measurement safeguards**, not demonstrated effect-size recommendations. Apply them as bounded tests to the maintainer's own repositories and preserve null/negative results.

**Next review:** individually inspect each PR diff/CI, bring in an independent method reviewer where required, prioritize the real observational audit/pilot, and only close tasks against their original acceptance criteria.

## 2026-10-13 integration addendum (status may change)

After the original batch, canonical [#182](https://github.com/MSKazemi/github-trending-1000-study/pull/182) incorporated the useful rank-bias calculation from [#188](https://github.com/MSKazemi/github-trending-1000-study/pull/188), which was closed unmerged; [#208](https://github.com/MSKazemi/github-trending-1000-study/pull/208) merged the consolidated lesson-registry schema, and the independent literature-screening [#189](https://github.com/MSKazemi/github-trending-1000-study/pull/189) and documentation rubric [#183](https://github.com/MSKazemi/github-trending-1000-study/pull/183) were subsequently reported merged. These historical changes do **not** imply any external source/human/energy validation. Consult each PR's authoritative current GitHub state, not the earlier table's draft status, before integrating further branches. Preserve distinct evidence and only merge current-head CI-verified code after a review.
