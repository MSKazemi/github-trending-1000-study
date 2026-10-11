# Auditing GitHub Trending as a black-box ranking and selection system

GitHub exposes [Trending](https://github.com/trending), with daily/weekly/monthly and language views, but the full ranking formula, candidate-generation rules and exposure data are not public. Our goal is **measured properties of displayed lists**, not reverse engineering with privileged knowledge.

## Auditable questions
- A1 **Temporal stability:** Jaccard overlap of consecutive daily/weekly/monthly page sets; rank-biased overlap and Kendall tau restricted to shared items. Different pages and lengths need matched comparisons.
- A2 **Exposure concentration:** counts/percentage of observed entries by language, age, star-size bin and repo type. Compare to an **explicitly constructed** public-repository sampling frame, not 'GitHub overall' absent a valid denominator.
- A3 **Newcomer coverage:** proportion of observed entries first created within 30/90 days; don't infer bias until denominator differences are estimated.
- A4 **Rank proxy:** evaluate how well displayed 'stars gained in period', existing total stars, age and language help explain within-page position. Predictive association does not reveal causal ranking weights.
- A5 **Filter consistency:** repeat measurements with and without language filters; ranks are only comparable within the same page/filter.
- A6 **Algorithm change:** monitor abrupt shifts in list size, data-format labels, language mix and rank-order agreement; log parser revisions and site changes.

## Algorithmic methods
- Top-k overlap J(A,B)=|A∩B|/|A∪B|; calculate separate daily, weekly and language views.
- Rank stability: Kendall tau-b on common repo IDs (report size of intersection, avoid interpreting tiny intersections); optionally rank-biased overlap with truncation declared.
- Ranked-list agreement: NDCG@K using **explicit target relevance**, e.g. next-30-day growth; this evaluates how well Trending predicts that *future outcome*, not whether ranking is objectively correct.
- Cohort visibility model: logistic regression and calibrated gradient-boosted trees for observed appearance vs independently sampled at-risk repo controls; require fixed sampling frame, sampling probabilities and proper resampling weights before interpreting calibration.
- Ranking model: within-query pairwise comparisons/learning-to-rank on captures; split chronologically by **repository** to prevent leakage and report macro-averaged across page captures. Features measured AFTER appearance are disallowed in truly prospective models.
- Drift: rolling window distribution checks (Jensen-Shannon divergence, descriptive), plus predefined thresholds confirmed against audit before announcing algorithm changes.

## When not to use a metric
- **Precision/recall of GitHub's actual Trending algorithm:** unavailable without the complete eligible candidate set and hidden ground-truth rules.
- **Click-through rate, impressions, view-to-star conversion:** no public per-repository Trending impressions; repo traffic needs permissions. Do not invent metrics.
- **Ranking fairness:** cannot establish population parity without an unbiased exposure-eligible frame. Discuss coverage differences, not discrimination findings.
- **Causal effect of being featured:** cannot identify by raw before/after comparison because star bursts can trigger selection. Consider a separately approved regression-discontinuity/instrument design only if eligibility thresholds and assumptions are externally validated (unlikely with opaque rules).
- **Recovered GitHub algorithm:** any model is an approximation with measurement error, selection effects and nonstationarity.

## Validation procedure
Use saved, timestamped HTML plus a manually reviewed page annotation. For each analyzed period, preserve n listed, capture-time interval, exact filter, data availability and parsing failures. Avoid an API-based claim that an 'official Trending API' exists without documenting the interface (metadata API is not the Trending list).
