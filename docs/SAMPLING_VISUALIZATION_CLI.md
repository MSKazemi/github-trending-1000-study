# F01/T02 observed-only sampling audit

**Status: implementation, not empirical findings.** Tracking issue #37. See docs/FIGURE_TABLE_PLAN_2027_2031.md.

## Offline invocation (synthetic fixture)

```bash
python -m trending_study parse-trending --input tests/fixtures/trending.html --date 2026-10-11 --window daily --output /tmp/fixture.jsonl
python -m trending_study.visualize_sampling --input /tmp/fixture.jsonl --output-dir /tmp/sampling-report --synthetic
python -m unittest discover -s tests -v
```

The fixture is **invented test data**. The `--synthetic` flag labels all outputs accordingly. Omitting it never authenticates external observations: the output still says USER_SUPPLIED_UNVERIFIED. No requests, scraping, package installations or sampling are performed.

## Outputs and limitations

- `F01_observed_sampling.svg`: observed-only flow from input occurrences to distinct names, resolved stable GitHub IDs and unresolved names. Eligible cohort and follow-up remain NOT MEASURED.
- `T02_observed_counts.md`: raw counts by selected Trending window, with explicit NOT MEASURED cells for true eligibility, scheduled capture completeness and 30/90/180-day follow-up.
- `sampling_audit.json`: counts, UTC date boundaries, observation-only status, unverified/synthetic flag, caveats and SHA256 of the supplied input file.

Input is strict JSONL with repository, observation_date, window, rank, source_sha256, source_file, collected_at_utc (UTC), and trending_url. Optional repository_id must be a positive integer or null. An observed name mapped to conflicting numeric IDs halts; a renamed repo with one ID counts once. Raw source hash and URLs are structurally validated, not cross-verified against actual captured HTML.

**Final empirical F01/T02 remain unimplemented.** The input alone cannot prove capture schedule completeness, identify unseen repos, reconstruct historical observations, adjudicate inclusion, count cohorts reliably when stable IDs are missing, audit independently sampled controls or establish prospective follow-up. These are unknown, never zero. An externally audited capture manifest, immutable ID mapping, exclusion ledger and valid followups must be added before making scientific claims.

GitHub Actions runs offline Python 3.10/3.12 unit tests, including synthetic cases for ID changes, failed input validation and report labels. No carbon, adoption, utility or statistical effect is calculated.
