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
