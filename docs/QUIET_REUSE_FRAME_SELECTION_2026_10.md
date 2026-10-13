# Independent OSS sampling frame (including older, overlooked components) — #15

**Status 2026-10-12:** reproducibility helper with **fictional registry entries only**; this does **not** establish a real denominator, probabilistic industry sample, reuse prevalence or 50 independently reviewed task/component pairs. Work toward [#15](https://github.com/MSKazemi/github-trending-1000-study/issues/15), not acceptance of the issue.

```bash
python -m trending_study.quiet_reuse_frame --input examples/quiet_reuse_frame.synthetic.json
python -m unittest tests.test_quiet_reuse_frame -v
```

The JSON specifies a **preassembled external frame** `repositories` with unique stable numeric repository IDs, `package_id`, independently preserved `source_url`, `stratum`, and `snapshot_at_utc`. `quotas`, a `seed` and `frozen_at_utc` are declared *before outcome inspection*. Per-stratum selection orders IDs by SHA-256(seed : repository ID), not stars, Trending exposure, later reuse or LLM rankings. Output records an order-invariant frame checksum, stratum counts, undersupplied quotas and nominal selected fractions. These fractions are **not unbiased sampling weights** until the independence, registry inclusion mechanism and random seed design are audited.

## Why this matters scientifically

Trending disproportionately measures platform attention and could omit long-lived foundational packages and small components. A complete, auditable **registry/dependency frame separate from Trending** is needed for a fair discovery/usefulness contrast. Preserve old components as eligible; use creation/release cohorts *as strata*, not retroactive evidence of AI usage. Do not select controls for having downstream success after treatment: that induces collider/selection bias.

## Real sampling workflow still required

1. Document approved source API/registry(s), package↔GitHub source mapping, duplicate packages per repo, immutable numeric GitHub identities, snapshot clock and unavailable package metadata. An official package URL alone does not authenticate source ownership.
2. Freeze inclusion/exclusion criteria, pre-period signals, stratification by project archetype, language, age/year and baseline visibility. Record package loss, private artifacts and missing registry coverage separately.
3. Audit frame coverage and exclusions **before** computing outcomes. If a stratum has missing entries, report it and correct prospectively, never silently increase case counts.
4. Freeze a verifiably random seed (or label deterministic demonstration only) and compute known inclusion fractions under a defensible complete frame; account for registry/platform noncoverage and within-repo dependency duplication.
5. After inclusion, use two independent raters and frozen task tests to identify functional compatibility, source version, license, security and upstream support; select a target 50+ real task/component pairs **without cherry-picking successful reuse**.
6. Compare Trending and independent cohort outcomes with matching and uncertainty, without generalizing the registry sample to all open source.

**Safety:** this sampler makes **zero** network calls and does not run or import packages from results. It validates supplied syntax/timing; independent source/frame verification remains human work. See [reuse gold standard](REUSE_GOLD_STANDARD_2027.md), [selection protocol](SELECTION_PROTOCOL_2027.md), [ethics](ETHICS.md) and [scientific governance](SCIENTIFIC_GOVERNANCE_2027.md).

**2027 maintainer lesson:** when searching for existing solutions, include older, small, well-maintained libraries that never Trending-rank; still validate task, version, license and security rather than trusting stars or novelty.

## 2026-10-13 sampling-frame leakage audit

Change: the selection CLI now accepts **only** the predeclared per-row keys `repository_id`, `package_id`, `stratum`, `source_url`, and `snapshot_at_utc`. A blacklist of obvious labels was insufficient because future reuse outcomes could be renamed as innocuous metadata. The freeze timestamp may not be future-dated; registry/source URLs must use clean HTTPS with no embedded credentials or fragment.

**Prospective sample design:** form the denominator from registry/dependency and archive sources independently of GitHub Trending and *before* collecting downstream reuse outcomes. Freeze and hash the complete candidate frame, stratum definitions (old/low-attention/new; project type, language/ecosystem and license eligibility), quota and publicly audited seed-generation procedure. A deterministic hash sort is reproducible but is **not** itself a true random draw unless its seed was chosen independently of outcomes; `nominal_sampling_fraction` is not a validated inclusion probability or population estimator.

**Validation:** compare the selection pipeline on additional old/low-star components and visible projects only after independent eligibility adjudication and selection-probability review; preserve unavailable, low-visibility, out-of-ecosystem and license/ownership-incompatible records in attrition. Issue #15's requirement for at least **50 real independently validated task/component pairs** is **not yet met**. No claim of global reuse missed by Trending is defensible from this synthetic frame.

**Source for protocol quality:** [Runeson & Höst (2009)](https://doi.org/10.1007/s10664-008-9102-8), on case selection and explicit chain of evidence. It does not establish this frame's coverage.

**Practical maintainer lesson:** make your library discoverable by task, package identity and tested integration—not only recent Trending rank. Measure outsider reuse and downstream maintenance with an independent sampling frame.
