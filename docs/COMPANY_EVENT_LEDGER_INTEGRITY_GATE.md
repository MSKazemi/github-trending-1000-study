# Company event-ledger structural integrity gate

**Scope:** offline, deterministic research artifact checks, contributed under [issue #240](https://github.com/MSKazemi/github-trending-1000-study/issues/240). This check extends the existing `scripts/check_research_artifacts.py` gate, rather than adding a competing CLI or performing network access.

## What runs automatically

The existing `python scripts/check_research_artifacts.py --root .` command validates all repository research JSON/JSONL/CSV syntax. It also recognizes `research/company-intelligence/<start>_<end>/NNN-slug.events.csv` and checks:

- Both existing **21-field** canonical indices and **22-field** variant with optional `evidence_tier` (including the earlier OpenAI event ledger).
- Required field names, no unexpected fields and correct three-digit company ID matching the filename.
- Distinct event IDs, valid calendar dates, inclusive publication-date boundaries from the directory, and chronological row order.
- Source status limited to protocol values (including `preview`, `announced_only`, `shipped`, `reported_undetermined`, correction, reversal and unavailable).
- Nonempty publisher/title/attribution fields and syntactically safe public HTTPS links, rejecting embedded URL credentials, bad ports and whitespace.

**Deliberate distinction:** a *changelog URL can legitimately identify multiple dated events*. The check does **not** reject duplicate publisher URLs; it requires distinct event IDs and dated provenance. Nor should same-publisher URLs be counted as statistically independent confirmations. Source archives remain governed by the generic syntax gate and are not silently rewritten to match today's working schema.

The existing Python unit-test discovery also runs `tests/test_company_event_ledger_integrity.py`, with adversarial fixtures and a check over the committed canonical indices.

## What it cannot claim

A syntactically valid `https://` address may lead to missing, changed, misleading, copyrighted or unauthorized content. Passing the gate **does not access any URL** or verify company/date/owner/release assertions, exact licenses, rights, code quality, field observations, real adoption, independent review or carbon savings. In particular, a file's `E0` or `E1` label is a working evidence classification, **not authenticated independent confirmation**.

For any company issue, still follow [the systematic search and review protocol](COMPANY_INTELLIGENCE_METHOD_2026_10.md): preserve exact seven-month-segment queries, true search-result and exclusion denominators (or mark unavailable), original and revised source versions, counter-evidence, matched event IDs, exact artifact licenses, and a real qualified human methods/factual signoff. Do not publish a completed study or auto-merge scientific conclusions from green CI.

## Reproduction

```bash
python scripts/check_research_artifacts.py --root .
python -m unittest tests.test_company_event_ledger_integrity -v
python -m unittest discover -s tests -v
```

All inputs are repository files or synthetic test data; no third-party library, access token, scraping, mutable remote service or network permission is required.

**Practical maintainer lesson:** distinguish *automatically checkable document contracts* from *independently verifiable science*. Machine checks are ideal for preventing silent corruption, but must not certify the authenticity or usefulness of third-party statements.
