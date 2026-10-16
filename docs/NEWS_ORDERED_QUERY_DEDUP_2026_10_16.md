# Issue #56 — conservative URL identity for ordered query selectors

Date: 2026-10-16. Scope: **offline synthetic source-lead deduplication**, not a completed 1,000-article systematic corpus, authenticated source verification or permission to scrape.

## Regression corrected

The existing `trending_study.news_corpus._canonical_url_key` removes known tracking keys while preserving meaningful source selectors. For a query with repeated key names, e.g., `?step=first&step=second`, the previous unconditional `sorted((key,value))` mapped it to the same key as `?step=second&step=first`. Some websites interpret repeated parameter sequences as order-sensitive. Treating these as certain duplicates can drop a genuinely distinct source record and silently bias a scientific screening denominator.

The modified behavior is intentionally conservative:

- Continue removing only known marketing-tracker fields (`utm_*`, `gclid`, etc.).
- Continue normalizing the ordering of queries when **all retained parameter names are unique**; this preserves deduplication of `?a=1&b=2` and `?b=2&a=1`.
- When any meaningful query key repeats, **retain the original order** of all remaining key/value pairs; reversed repeated selectors no longer collapse.
- Continue retaining source URL, original publication/access dates, provisional statuses and no-authenticated-review restrictions. Do not rewrite existing source records.

## Evidence boundary

Three new **fictional, offline** regressions exercise reversed repeated selectors, tracker variants of identical repeated selectors, and ordinary unique query reordering. Passing synthetic tests does not establish that any actual web resource interprets its own query order this way. False negatives (same content with different query order) remain possible; only an independently reviewed event/content-level crosswalk can decide actual duplicates. This is a conservative anti-loss default.

**Reuse-first engineering choice:** change the existing standard-library canonicalizer; no new dependencies, scraper, network calls, source corpus entries or purported reviewer signatures.

## Remaining closure blockers

The 20 provisional items do not constitute a complete screening/correction/rights denominator. Issue #56 still needs source-access/legal review, authentic historical dates, independent factual/source QA, adjudicated two-person screening, event-level duplicate checks, transparent attrition and scope choices before study claims. The target up to 1,000 is a planning target, not a measured population.

## Maintainer lesson

When deduplicating documents, a normalized URL is only an *indexing key*, not proof of identical events. Preserve ambiguous source leads for review instead of suppressing possible counterevidence.
