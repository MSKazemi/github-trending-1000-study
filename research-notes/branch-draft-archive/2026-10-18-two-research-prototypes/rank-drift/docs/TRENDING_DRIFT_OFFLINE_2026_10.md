# Snapshot overlap and rank drift (issue #6)

**Status 2026-10-12:** deterministic offline *synthetic-capable* instrument; **no real Trending capture analyzed or permission established**. This does not close #6.

```bash
python -m trending_study.trending_drift --input page_pair.json
python -m unittest tests.test_trending_drift -v
```

Example **fictional** input:

```json
{
  "before": {"observed_at_utc": "2026-10-01T00:00:00Z", "window": "daily",
    "language": null, "source_sha256": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "repository_ids": [101, 102, 103]},
  "after": {"observed_at_utc": "2026-10-02T00:00:00Z", "window": "daily",
    "language": null, "source_sha256": "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
    "repository_ids": [102, 101, 104]}
}
```

**Metrics:** set Jaccard on immutable numeric repository IDs (not mutable names); Kendall tau-a only on IDs shared by both snapshots and **null** for fewer than two shared items; finite-list extrapolated rank-biased overlap (RBO) with configurable `p`, **only when both full list depths are equal**. Explicitly refuse mismatched languages/windows, repeated IDs, unverified timestamp formats or reversed capture order. Present a null metric as unestimable, not zero.

**Important source-integrity boundary:** the SHA-256 strings in this input are **self-declared**. This analyzer does not authenticate original HTML, audit every visible row, calculate real parser recall or validate source access rules. Before empirical use, verify immutable capture+manifest against actual saved page bytes, independently label 30+ real rows, record parser failures and rank gaps, then preregister page pairs and denominators. Different page lengths are not silently padded for RBO. All outputs are *properties of supplied lists*, never an estimate of GitHub's private ranking algorithm or causal user demand.

**Follow-on work:** stratified temporal drift and language coverage; prospective held-out ranking proxy and sensitivity to missing pages; paired uncertainty accounting for overlap from the same repositories. Avoid interpreting tiny sampled windows as stable platform-level effects.

**Practical lesson:** visibility rank can be volatile even when an open-source tool remains useful. Track external first-use and downstream integration separately; do not optimize a maintainer's work solely for daily rank.

See [Trending audit](TRENDING_ALGORITHM_AUDIT.md), [independent page QA](INDEPENDENT_PAGE_AUDIT_2026_10_12.md) and [mission outcomes](AI_ERA_CODING_REUSE_RESEARCH_MISSION.md).
