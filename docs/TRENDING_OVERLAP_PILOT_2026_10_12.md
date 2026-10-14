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
with spaces normalized to hyphens). Host spoofing, noncanonical origins, nested or encoded language paths,
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

**2026-10-14 companion engineering implementation:** The missing **offline** explicit-frame language coverage and chronological heldout rank-proxy methods, with no future-feature or cross-split identity leakage, are now specified and tested in [the issue #6 coverage/rank-proxy runbook](TRENDING_COVERAGE_AND_RANK_PROXY_2026_10_14.md). Existing Jaccard/Kendall/RBO calculations remain unchanged; do not create a competing RBO CLI.

**Still unresolved scientific field work:** independently inspect authorized real saved pages, actual source license/access policy and filter completeness; build a justified at-risk denominator; independently verify pre-capture feature times and preregister the temporal cut before viewing any real heldout scores. Never infer the opaque GitHub selection algorithm, true user adoption or a causal effect of Trending. Without human approval and real evidence this issue is engineering-ready, **not empirically answered**.

**Practical repository lesson to test:** If project visibility fluctuates
rapidly even on comparable pages, do not interpret a single trending rank or
one-day star burst as evidence of reusable functionality. Instead instrument
clean-install, independent adoption and 30/90-day maintenance outcomes.
See [black-box audit proposal](TRENDING_ALGORITHM_AUDIT.md).

## Enterprise quality review correction (2026-10-13)
The scorer now **rejects unregistered URL query parameters**, not just a `since` mismatch. Previously, a URL containing `&spoken_language_code=...` or another ranking filter could pass as a supported surface, even though no field in the observation schema recorded that filter; it could bias comparisons. Only an exact single `since=daily|weekly|monthly` is allowed until an explicitly versioned filter schema is introduced. A strict 1,000-row input limit prevents unexpectedly large quadratic pairwise rank analysis. This bound is intentionally much larger than ordinary Trending pages, and any real larger page requires explicit review of its capture provenance and algorithmic cost. Additional synthetic regression tests protect both invariants. These are parser/input hardening changes, not original evidence that GitHub Ranking reflects software usefulness.

### Additional security and input type validation (2026-10-13)

The same evidence-gated implementation also rejects uncanonical GitHub authorities (including explicit ports), nested/encoded language separators and malformed `window` or `dataset_kind` types. Reviewer-added synthetic regressions exercise those cases. These checks augment—not replace—the already-merged exact query allowlist and 1,000-rank cap. No real GitHub Trending or user-value observations are implied.
