# Issue #56 — conservative URL identity for ordered query selectors

Date: 2026-10-16. Scope: **offline synthetic source-lead deduplication**, not a completed 1,000-article systematic corpus, authenticated source verification or permission to scrape.

## Regression corrected

The existing `trending_study.news_corpus._canonical_url_key` removes known tracking keys while preserving meaningful source selectors. For a query with repeated key names, e.g., `?step=first&step=second`, the previous unconditional `sorted((key,value))` mapped it to the same key as `?step=second&step=first`. Some websites interpret repeated parameter sequences as order-sensitive. Treating these as certain duplicates can drop a genuinely distinct source record and silently bias a scientific screening denominator.

The modified behavior is intentionally conservative:

- Continue removing only known marketing-tracker fields (`utm_*`, `gclid`, etc.).
- Continue normalizing the ordering of queries when **all retained parameter names are unique**; this preserves deduplication of `?a=1&b=2` and `?b=2&a=1`.
- When any meaningful query key repeats, **retain the original order** of all remaining key/value pairs; reversed repeated selectors no longer collapse.
- Continue retaining source URL, original publication/access dates, provisional statuses and no-authenticated-review restrictions. Do not rewrite existing source records.

## Follow-up: preserve trailing path slash (same-day review)

The same conservative source-identity rule applies to path spelling. An earlier
normalizer used `parts.path.rstrip("/")` and therefore collapsed `/report`
and `/report/`. HTTP servers may route these paths to different content;
without independent source inspection it is not justified to discard either
provisional evidence lead. Keep the supplied path including its trailing slash,
while treating an empty path as the root request path. One additional synthetic
regression preserves both sources. This does not claim the two URLs actually
carry different articles, nor does it authenticate their event-level identity.

## Follow-up: raw query encoding is not source identity

`parse_qsl` decodes query values before comparison, so `?id=alpha%2Fbeta` and `?id=alpha/beta` were incorrectly given one key. The underlying HTTP origin may distinguish their original encoded spellings. The offline source-lead gate now retains raw meaningful query fields, only drops **literal** known marketing-tracker keys, detects repeated keys even after decoding their names, and avoids sorting encoded key names. Unique ordinary parameter keys can still be reordered for deterministic deduplication. Three synthetic tests cover raw selector values, percent-aliased repeated keys and encoded tracking-key ambiguity. More retained leads can increase screening workload; only a human source/content review can adjudicate true duplicates. The original news evidence ledger is not rewritten.

## Follow-up: source URL host safety and raw-control rejection (2026-10-17)

The offline provisional source-ledger validator now rejects lexically unsafe HTTPS
hosts: single-label/local/internal names, non-global IP literals, legacy
numeric IPv4 aliases (e.g., `127.1` and `2130706433`), malformed DNS
labels, and hostnames exceeding the DNS label/total limits. Ordinary
hyphenated/punycode ASCII public-domain syntax remains permitted. It also
rejects whitespace and DEL/control bytes **before** `urlsplit` can normalize
some of those bytes away. Synthetic negative and positive unit tests cover
these boundaries; original source records remain unchanged.

**Important limitation:** This verifies only supplied URL *syntax*. It does
not resolve DNS, detect rebinding or redirects, authenticate source publishers,
authorize scraping, or establish that any URL is independently verified.
A future authorized network client still requires qualified source-access and
connection-time security review. This is a candidate engineering hardening
patch on the existing #56 PR, not a completed scientific corpus or closure.

**Practical repository lesson:** validate raw provenance identifiers and
host spellings before normalization; never upgrade offline lexical checks into
claims of transport safety or trusted research sources.

## Evidence boundary

Three new **fictional, offline** regressions exercise reversed repeated selectors, tracker variants of identical repeated selectors, and ordinary unique query reordering. Passing synthetic tests does not establish that any actual web resource interprets its own query order this way. False negatives (same content with different query order) remain possible; only an independently reviewed event/content-level crosswalk can decide actual duplicates. This is a conservative anti-loss default.

**Reuse-first engineering choice:** change the existing standard-library canonicalizer; no new dependencies, scraper, network calls, source corpus entries or purported reviewer signatures.

## Remaining closure blockers

The 20 provisional items do not constitute a complete screening/correction/rights denominator. Issue #56 still needs source-access/legal review, authentic historical dates, independent factual/source QA, adjudicated two-person screening, event-level duplicate checks, transparent attrition and scope choices before study claims. The target up to 1,000 is a planning target, not a measured population.

## Maintainer lesson

When deduplicating documents, a normalized URL is only an *indexing key*, not proof of identical events. Preserve ambiguous source leads for review instead of suppressing possible counterevidence.

## 2026-10-17 correction: preserve even unique-key query order

The 2026-10-16 rule above that sorted retained **unique** query parameter
names is now superseded. A query containing `a=1&b=2` may be interpreted
differently from `b=2&a=1` by an origin application or an order-sensitive
signature even if neither key repeats. Sorting could therefore silently
suppress one provisional evidence lead. The updated code preserves **all raw
remaining meaningful query-item order** after literal known marketing keys
are stripped. Two additional synthetic regressions test ordinary unique
keys and distinct tracking-tainted variants. The already documented tracker
stripping remains a heuristic with residual collision risk; no real webpage,
publisher identity or event has been authenticated. The trade-off is extra
leads for manual review, explicitly preferable to silent source loss.

**Practical lesson:** URL normalization can reduce review workload but it
cannot replace a separately adjudicated content/event duplicate decision.
