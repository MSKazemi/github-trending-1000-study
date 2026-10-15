# Repository-wide technical and scientific checkpoint — 2026-10-13

**Inspection target:** `main` commit `008a7ee162a852f10d424625b0b58ae1186faaa1`, checked 2026-10-13. **Audit type:** GitHub-tracked full-tree inventory + selective risk-based review of main CLI, source manifests, write-once storage, tests, CI, top-level docs and protocol evidence. **Not** a complete line-by-line source review, a security penetration test, scientific replication or independent human approval. An independent container clone failed DNS resolution for github.com; the GitHub connector supplied the latest read-only inventory and source files. Counts are a snapshot, not permanent metrics.

## Inventory and reproducibility surface

| Observed GitHub tree fact | Count or state | Assessment |
|---|---:|---|
| Recursive tracked tree entries | 165 | Not all are files: 152 blobs and 13 directories |
| Python modules in `trending_study/` | 14 | Standard-library-only CLI, offline measurement/review/gate instruments |
| Python test modules in `tests/` | 15 | Most committed data/fixtures are synthetic and explicitly labeled |
| Research Markdown docs under `docs/` | 73 | Substantial protocol and methods material; plans must not be confused with evidence |
| Total Markdown files | 91 | Curation is large relative to actual observed data |
| Open PRs (at check) | 46 | Many source/industry-screen and overlapping methodological branches; conflict review remains essential |
| CI | `.github/workflows/ci.yml` | Python 3.10 and 3.12 `unittest`; no actual platform-source attestation or human review |
| Python package metadata | No `pyproject.toml`, `setup.py` or `setup.cfg` on main | Clean-room `pip install`/console-script reuse not documented as supported; future P2 packaging task |
| Exposed version strings | `trending_study.__version__=0.3.0`, main CLI `VERSION=0.4.0`, network User-Agent `/0.2` | P2 metadata drift: converge release identity when adding a clean-install distribution test; not proof of study invalidity |
| Committed actual Trending observations | No observed cohort in `data/raw` or `data/processed` tracked tree | These directories have `.gitkeep` only. This does **not** prove no separately stored private data exist. |

## Most important gap and chosen action

**P0 — The code previously allowed an outbound live request to a blocked/pending research surface.** Documentation explicitly warned not to collect `https://github.com/trending?since=...` until approval; published [robots guidance](https://github.com/robots.txt) includes `Disallow: /*since=*` and the collector's `capture` function previously called `urlopen()` without a source-permission check. This was a **verified documentation/code mismatch**, not evidence that a request was actually made. The risk is to source access, scientific reproducibility, data rights and the feasibility of the entire primary observational study.

**Selected one bounded engineering remedy:** [fail-closed source-access decision](SOURCE_ACCESS_DECISION_2026-10-13.md) with an explicit no-bypass code guard, negative zero-network regressions and coherent README/ethics/pilot/agent guidance. It is safer to prevent a misleading or disallowed experiment than to add more unverified findings. The `capture` implementation remains available for future *reviewed code amendment*, but its live network path is presently disabled. Preserve the low-dependency offline helpers.

## Other critical items — not declared complete by this PR

| Priority | Risk | Required external or next engineering evidence |
|---|---|---|
| P0 | No permitted/independently quality-audited actual Trending row sample | [#2](https://github.com/MSKazemi/github-trending-1000-study/issues/2): human access decision, immutable raw captures, at least 30 real independently annotated rows across approved windows and correct coverage/precision |
| P0 | Unfrozen research sampling/estimands and conditional 2026 pilot/start | [#27](https://github.com/MSKazemi/github-trending-1000-study/issues/27): dated protocol version, statistical review, privacy/consent, power and proper registration; don't silently migrate from Trending to official API |
| P0 | No independently accepted real reuse tasks, repeat downstream use, or lifecycle CO2 savings | [#65](https://github.com/MSKazemi/github-trending-1000-study/issues/65), [#21](https://github.com/MSKazemi/github-trending-1000-study/issues/21), [#18](https://github.com/MSKazemi/github-trending-1000-study/issues/18): actual opt-in human review and task tests; physical/inference energy boundary |
| P1 | Open PR concurrency and overlapping instruments | [Integration tracker #64](https://github.com/MSKazemi/github-trending-1000-study/issues/64): select one canonical API for any duplicated tool, verify current-head CI, source/rights/methods review before merges |
| P1 | Static/synthetic CI ≠ live parser QA, license/right-to-reuse or external user-task success | Maintain explicit external gates; add only truthful auditable experiments with frozen acceptance and missingness |
| P2 | Reusability/documentation drift; no distribution metadata | After the P0 science gates, prototype reproducible install and independent first-user tests, not a vanity package release |

## Validity and honest boundaries

- **No 1,000-repository cohort, causal study, permission grant, source-page gold-standard audit, reviewer independence, token-to-kWh conversion or green impact has been established by this check.**
- A robots disallow is a significant access-policy signal for automated clients but not, alone, a definitive legal conclusion about every type of human or API access. An accountable human must review current live policy and contact platform support when appropriate.
- CI success can only support the behavior of submitted code and synthetic fixtures. It does not determine whether a source has a lawful and statistically valid sampling frame, or whether future results are scientifically sound.
- This audit did not independently run the whole checkout because GitHub DNS resolution was unavailable to the local container. If this branch passes GitHub Actions, report that exact run/head as evidence of tested software behavior, not as local execution or human signoff.

## Practical lessons for the maintainer's other repositories

**Protection first:** if a documented access, ethics or deployment restriction is central to correctness, make the corresponding path fail closed, and test *zero* unintended effects. **Reuse before expansion:** 46 concurrent PRs and many overlapping docs make canonical interfaces and integration discipline valuable. **Publish measured utility later:** first-user success with independent task acceptance and maintenance costs is worth more than another generated feature or unverified metric. **Preserve unknowns:** missing source rights, work/energy telemetry and human judgments are not zero or positive results.

**Provenance:** created with AI assistance from dated tracked GitHub evidence. Independent scientific, privacy and maintainer review still required. See the [older October 12 audit](REPOSITORY_AUDIT_2026-10-12.md) for historical comparison, not as a substitute for this refreshed status.
