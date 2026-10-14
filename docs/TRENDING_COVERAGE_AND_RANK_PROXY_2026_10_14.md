# GitHub Trending issue #6: explicit-frame coverage and out-of-time rank-proxy audit

**2026-10-14 | Status: offline engineering instrument, not empirical findings or an approved preregistration.** The previous [within-page overlap and rank agreement evaluator](TRENDING_OVERLAP_PILOT_2026_10_12.md) already implements Jaccard, common-item Kendall tau, finite discounted prefix overlap, and explicitly extrapolated same-depth RBO. This companion completes the **software/fixture** portions of language-frame coverage and chronological rank-proxy evaluation. It does not validate an actual GitHub Trending page or estimate an undisclosed GitHub ranking formula.

## Reproducible offline commands

Requires Python 3.10+ and standard library only. These examples are **entirely synthetic**; hashes, dates and IDs are placeholders, not independently verified source records.

~~~bash
python -m trending_study.trending_overlap --input examples/trending_overlap.synthetic.json
python -m trending_study.trending_audit coverage --input examples/trending_language_coverage.synthetic.json
python -m trending_study.trending_audit proxy --input examples/trending_rank_proxy.synthetic.json
python -m unittest discover -s tests -v
python -m trending_study.data_integrity --root .
~~~

The new CLI reads a bounded, regular, non-symlink JSON file with the repository's existing strict decoder. It opens the actual file descriptor with `O_NOFOLLOW` and `O_NONBLOCK`, verifies the descriptor is a regular file, and caps **bytes actually read**, not only an earlier file-size check. Platforms without secure `O_NOFOLLOW` support fail closed rather than fall back to race-prone path-only checks. This mitigates a symlink-swap/time-of-check-time-of-use race and prevents a FIFO from blocking indefinitely. A concurrently modified regular file is still untrusted input, not immutable evidence. Duplicate keys, nonstandard NaN/Infinity, unrepresentable non-finite numbers, invalid UTF-8 and unsupported fields fail closed; error text counts unknown field names rather than repeating potentially private names. Decoder errors (including duplicate JSON keys) are summarized without repeating source-key names, as those names may contain sensitive text. It makes **zero network requests** and does not collect, enrich or process raw HTML. Neither model nor output validates source permission, cohort eligibility, human review or real observed data.

## 1. Coverage with an explicit denominator

Input version: `trending-coverage-1.0`.

~~~text
{
  "schema_version": "trending-coverage-1.0",
  "dataset_kind": "synthetic | self_reported_audit",
  "surfaces": [
    {
      "frame_id": "...",
      "frame_as_of_utc": "UTC timestamp before target page capture",
      "frame_source_sha256": "64-hex content checksum",
      "frame_definition": "what the at-risk candidate frame contains/excludes",
      "frame_sampling": "how these frame IDs were assembled",
      "frame_page_url": "exact intended page URL, frozen before capture",
      "frame_window": "daily | weekly | monthly",
      "frame_language_filter": "matching language label or null",
      "eligible_repository_ids": [positive unique numeric GitHub repository IDs],
      "capture": {existing Trending overlap capture schema}
    }
  ]
}
~~~

Each capture **reuses** the strict existing page contract: `capture_id`, canonical HTTPS `page_url`, `window=daily|weekly|monthly`, explicit nullable `language_filter`, strict `captured_at_utc`, 64-hex `source_sha256` and all `repository_ids` in displayed rank order. The frame must be defined **strictly earlier** than its capture and have at least one stable ID. Its declared URL/window/language must **exactly match** the later capture, preventing substitution of a different valid language page after selecting the frame. Frame and page source SHA-256 digests must differ, preventing the same capture artifact from being reused as its own predeclared candidate frame. Source hashes and declarations are checked for **structure only**, not their authenticity. A page's language filter cannot be silently changed to compare different denominators. One output row is produced per supplied frame/capture pair.

For frame `F` (an explicitly **listed, predeclared set**) and its contemporaneous observed page set `T`, report:

| Output | Exact definition |
| --- | --- |
| `denominator_predeclared_frame_ids` | `|F|` |
| `numerator_observed_frame_ids` | `|F intersect T|` |
| `frame_observed_fraction` | `|F intersect T| / |F|` |
| `frame_ids_not_on_page` | `|F minus T|` |
| `page_ids_outside_frame` | `|T minus F|` |
| `observed_page_ids` | `|T|` |

**Correct scope:** this fraction is defined only for the supplied at-risk frame. A convenience or incomplete frame is **not a random sample**; even a field labeled "probability" cannot establish probability sampling without verified design/inclusion probabilities. Each language surface and the unfiltered surface has its own denominator. Do not sum, average, or interpret cross-language frames as disjoint repository populations (repos can span languages); the output deliberately sets `cross_language_population_coverage=null`.

### Synthetic sanity check

The Python fixture has four fictional eligible IDs, of which two appear on the supplied Python page: `2/4 = 0.5`. One additional page entry falls outside that frame. The Rust fixture has two eligible IDs, one of which appears: `1/2 = 0.5`. Those values show **math and error handling only**. Neither result says Python and Rust have equal Trending opportunity, coverage or selection fairness.

## 2. Chronological heldout proxy for **within-page displayed rank**

Input version: `trending-rank-proxy-1.0`.

~~~text
{
  "schema_version": "trending-rank-proxy-1.0",
  "dataset_kind": "synthetic | self_reported_audit",
  "protocol_locked_at_utc": "UTC timestamp separating old and future pages",
  "protocol_reference": "specific self-reported protocol/freeze reference",
  "pages": [
    {
      "capture": {existing Trending overlap capture schema},
      "features": [
        {
          "repository_id": 101,
          "recorded_at_utc": "UTC timestamp before that page",
          "feature_source_sha256": "64-hex content checksum",
          "prior_7d_star_delta": 4,
          "prior_stars": 100,
          "prior_forks": 10
        }
      ]
    }
  ]
}
~~~

**Target:** pairwise ordering among repositories that were **already on one recorded page**. It is *not* a prediction of Trending appearance, recommendation quality, usefulness, adoption, or the hidden candidate universe. Features are self-declared **prior-to-capture** snapshots; their collection method, the 7-day delta's endpoint alignment and their license/access approval still require verification. A current/future snapshot may never be labeled as a pre-capture feature.

**Frozen and bounded evaluation procedure:**

1. Require at least four strictly chronological captures of the **same exact page URL, daily/weekly/monthly window and language filter**, with a minimum of two IDs each. Each displayed ID must have exactly one feature record and a feature timestamp **strictly earlier** than its target capture. Unknown values are rejected, never imputed to zero; declared integer metadata must fit signed 64-bit magnitude (and stars/forks cannot be negative).
2. Divide pages at `protocol_locked_at_utc`: at least two training pages strictly before it and two heldout pages strictly after it. Reject captures exactly at lock time, unsorted captures, overlapping stable repository IDs across the split, unrecognized fields and duplicate records. The distinct-ID constraint deliberately prioritizes strong leakage control over retaining repeated-popularity observations.
3. Freeze three simple, interpretable candidate predictors **before holdout**: descending `prior_7d_star_delta`, `prior_stars`, and `prior_forks`. These represent three independent **single-feature baselines**, **not** a fitted machine-learning model or estimated causal ranking weights.
4. On each **training** page, score each predictor over all pairs `(i,j)` where displayed rank `i` precedes `j`: 1 for the expected higher feature value, 0 for inverted and **0.5** for a feature tie. Compute `n(n-1)/2` pair comparisons per page; macro-average accuracy across training pages. Choose the highest training macro score; exact ties use the fixed predictor order above.
5. Evaluate that **unchanged selected predictor** on later heldout pages and publish per-page `pairs`, `feature_ties`, `pairwise_accuracy`, and equally weighted `heldout_macro_pairwise_accuracy`. Never select or tune a model using those heldout scores.

For bounded runtime, the evaluator rejects inputs exceeding **250,000 total within-page pair comparisons** across all pages, before trying the three predictors; this is an engineering resource limit, not a sampling rule. Larger studies must explicitly version/review the cap rather than silently truncate pages. A feature SHA-256 must also differ from its target page's SHA-256, preventing reuse of the same artifact as a purported independent earlier feature source. Neither condition authenticates the actual data.

The fabricated fixture chooses `prior_7d_star_delta` on the training pages (accuracy `1.0`); its heldout page-pair scores are `2/3` and `3/3`, macro average `5/6`. This is **not a measured Trending association**. The implementation leaves `holdout_frozen_by_external_review=false`, `selection_universe_known=false`, `independent_verification=false` and `eligible_for_confirmatory_cohort=false`.

### Limitations and validity threats

- Rank labels come from a self-reported page capture. No independent live-page annotation, source license approval, dataset access, verified protocol freeze or temporal feature audit occurs in this CLI.
- Conditioning on the displayed page is selection on a potentially outcome-related variable. It prevents estimating general population inclusion probabilities or the causal effect of being ranked.
- Within-page pair comparisons share repositories and are **dependent**, so the reported macro pairwise accuracy is descriptive. No p-values, standard errors, confidence intervals or significance claims are produced.
- Repeated repositories *within* one split can correlate page scores. Cross-split repository IDs are forbidden, but unmeasured time-varying confounding, data freshness and incomplete frame construction remain.
- Observing two chronological groups does not prove preregistration: the lock timestamp is self-reported and might be retrospective. Before a real prospective evaluation, precommit the protocol, candidate feature meanings, UTC cut, source snapshot schedule, sample size and analysis plan under independent review.
- `prior_7d_star_delta` is defined using earlier measurements; it is **not** the Trending page's displayed period-star label and is not reconstructed from current API star counts.
- Historical page ranking may change with GitHub UI, filters or undisclosed scoring; the instrument never claims to reverse-engineer or reproduce that scoring.

## 3. Verification and future promotion gates

**Engineering checks:** offline unit/CI suite tests exact denominators, tie scoring, training-only selection, missing data, future timestamps, malformed/mismatched surfaces, illegal URL variants, frame provenance, cross-split reuse, duplicate IDs/JSON keys, disallowed extra private fields, nonstandard numbers, symlinks, non-regular FIFO input, path substitution between validation and open, growth after file-size inspection, unknown/duplicate field-name redaction from CLI diagnostics, and oversized CLI input.

**Scientific go/no-go (not complete):** independently approved platform access; authorized real captures with SHA + true UTC times; full-page independent ranking QA from issue #2; evidence that each frame was assembled before the target page and defines a defensible denominator; protocol/methods sign-off; verified metadata snapshots predating each target, including 7-day delta intervals; independent replication on actual future pages and honest missingness and sampling limitations. Human approval must precede presenting a self-reported audit as empirical findings. Real comparative analyses belong in a subsequent **prospective preregistered study**, not in synthetic tests.

## 4. Practical lessons for repository maintainers

- Treat discovery-channel rank as **observed attention**, not evidence that a component can solve a user task.
- Publish *both* the numerator and the at-risk denominator whenever comparing language/ecosystem visibility. Unknown eligibility must remain unknown.
- Freeze measurement rules and independently verify timestamped baselines **before** comparing future periods; refuse post-treatment features masquerading as baselines.
- Test reusable components via installation/functional acceptance, licensing/security review and 30/90/180-day maintenance evidence before recommending them as superior to custom code.
- Preserve negative, inconclusive and missing observations: a high predictive score on selected Trending repos would still not demonstrate additional real users, reduced human effort or lower carbon emissions.

See [the black-box audit design](TRENDING_ALGORITHM_AUDIT.md), [construct validity caveats](TRENDING_VALIDITY_AUDIT.md), [source-access stop gate](SOURCE_ACCESS_DECISION_2026-10-13.md), and [roadmap](ROADMAP.md).
