# Issue #6 — synthetic Trending temporal-overlap pilot

**2026-10-12 · implementation stage 1; no observed GitHub Trending validity result.**

An offline, standard-library comparison of exactly two *supplied* ranked pages on the same
URL, language filter and daily/weekly/monthly window is available as:

```bash
python -m trending_study.trending_overlap --input examples/trending_overlap.synthetic.json
python -m unittest tests.test_trending_overlap -v
```

Input v1.0 is \`schema_version\`, \`dataset_kind\` = \`synthetic\` or
\`self_reported_audit\`, and two \`captures\` with unique \`capture_id\`, strict
UTC \`captured_at_utc\`, exact \`page_url\`, \`window\`, nullable
\`language_filter\`, \`source_sha256\` and all displayed \`repository_ids\` in
rank order. The URL is parsed and restricted to HTTPS `github.com/trending`
(or `/trending/<language>` when a non-null filter is declared); the explicit
`since=daily|weekly|monthly` query value must match `window`, and the
decoded language slug must agree with the declared filter (case-insensitive,
with spaces normalized to hyphens). Host spoofing, noncanonical origins or ports, nested/encoded language paths, unexpected query keys,
fragments, duplicate `since` values and future UTC capture timestamps
(more than five minutes ahead of the validator clock) fail closed. The small
skew allowance is not third-party time authentication.

Numeric IDs must be independently resolved from original page names; this
tool does not infer them from HTML or verify that source hashes represent
authentic captures. Invalid/incomplete input fails closed.

Output denominators: \`page_sizes\` (supplied displayed entries per capture),
\`union_unique_ids\`, \`common_unique_ids\`; set Jaccard = common/union;
Kendall tau on common IDs uses only comparable rank pairs and is null if fewer
than two IDs overlap. \`discounted_prefix_overlap_lower_bound\` is
\((1-p)\sum_{d=1}^{\max(n_a,n_b)} p^{d-1} \cdot |A_{1:d}\cap B_{1:d}|/d\),
with \`p=0.9\` by default. It excludes any extrapolated tail and is **not**
an infinite-list RBO estimate or cross-language coverage statistic. The
source-pages' contents and reviewer independence are not authenticated.

**Canonical metric consolidation with [PR #188](https://github.com/MSKazemi/github-trending-1000-study/pull/188):** this *same* offline analyzer now also reports `rbo_extrapolated_equal_depth` when both observed page lists have exactly the same positive depth `k`. It equals the finite discounted prefix term above **plus** `p^k × (|A_(1:k) ∩ B_(1:k)| / k)`. It becomes `null` for unequal observed depths, with `rbo_extrapolation_reason="unequal observed page lengths"`. The additional term assumes last-depth agreement persists into the unobserved tail; it is not a measured population ranking effect or proof about future GitHub Trending results. For unequal depths, use the separately reported finite discounted-prefix lower bound only. The two metrics share the same `prefix_persistence`, capture provenance rules, denominators and no-cohort-eligibility restriction; **no second Trending measurement CLI should be created** solely for RBO.

**Remaining issue work:** independently inspect saved live pages and source
license/access policy; measure multi-timepoint rank drift and filter-level
coverage *against an explicit eligible frame*; audit timestamp/window
alignment; preregister prospective rank-proxy features, train/holdout
chronological split and leakage safeguards. Never infer the opaque Github
selection algorithm, true user adoption, or causal effect of Trending.

**Practical repository lesson to test:** If project visibility fluctuates
rapidly even on comparable pages, do not interpret a single trending rank or
one-day star burst as evidence of reusable functionality. Instead instrument
clean-install, independent adoption and 30/90-day maintenance outcomes.
See [black-box audit proposal](TRENDING_ALGORITHM_AUDIT.md).

## PR review hardening (2026-10-13)

Security/methods review added strict rejection of unexpected query parameters and noncanonical GitHub origins (including explicit ports) so differently filtered pages cannot be silently compared. Filtered languages must map to exactly one safe slug; nested paths or encoded separators are rejected. Malformed container types now raise the documented `OverlapError`, not an unchecked Python type error. Synthetic regression tests cover all these cases; this still does not authenticate GitHub data or 30/90/180-day follow-up.
