# October 2026 pilot — capture, checksum and scientific preflight

**Protocol state at 2026-10-12:** pilot proposed (2026-10-15–2026-10-31), not yet performed or approved for recurring automated capture. The proposed confirmatory enrollment (2026-11-01–2027-04-30) remains **conditional**; do not backdate if the pilot, source permissions or preregistration are incomplete.

This is the executable operating procedure for **one explicitly user-initiated, unfiltered public GitHub Trending page**. It does not implement nine language/window surfaces, scheduled scraping, independent upstream attestation, immutable repository IDs, a statistical power analysis, or human-review signoff. Those gaps are intentionally visible rather than silently counted as complete.

## Step 0: Scientific and source access review

Read [Ethics](ETHICS.md), [Selection](SELECTION_PROTOCOL_2027.md), [Preregistration draft](PREREGISTRATION_DRAFT_2027.md) and [Readiness report](PROTOCOL_FREEZE_STATUS_2026_10_12.md). Confirm permitted retrieval frequency and relevant platform terms/robots/access requirements with a human reviewer before recurring collection. **This repository does not launch automatic polling.**

Run the scientific preflight against the explicitly **pending** sample checklist:

```bash
python -m trending_study pilot-preflight \
  --input examples/pilot-preflight.example.json --stage pilot

python -m trending_study pilot-preflight \
  --input examples/pilot-preflight.example.json --stage confirmatory \
  --require-ready
```

The first command reports which documentary prerequisites remain. The second is **expected to return nonzero** for the example: that is a safety feature. A result `ready_for_human_review` is **not** ethics approval, access authorization, preregistration, an independent audit, or confirmation that observations have been collected.

## Step 1: Capture one page once, with provenance (currently BLOCKED)

**STOP — do not execute the capture command at present.** As of 2026-10-13 the CLI hard-blocks live `/trending?since=...` retrieval before any HTTP request, because source-access approval for this study is absent and published [GitHub robots rules](https://github.com/robots.txt) contain `Disallow: /*since=*`. Review the [decision record](SOURCE_ACCESS_DECISION_2026-10-13.md). This is a conservative operating decision, not a legal ruling that every manual public-page visit is unlawful. There is no user-facing override; re-enablement requires an explicit reviewed code/protocol amendment after a genuinely favorable human platform/access assessment.

**Future procedure only, after authorization:** use the **actual current UTC date**, not a backfilled historical date. The example below is preserved to specify the intended manifest and output contract; it currently exits nonzero before writing files:

```bash
UTC_DAY="$(date -u +%F)"
python -m trending_study capture --date "$UTC_DAY" --window daily \
  --output "data/raw/$UTC_DAY-daily.html" \
  --manifest-output "data/raw/$UTC_DAY-daily.manifest.json"
```

Once a documented, independently reviewed re-enablement PR has been approved, the original capture implementation is designed to make **one** user-initiated HTTPS request, validate HTTP status/HTML, write at most 4 MB of raw bytes and create an adjacent capture-time JSON manifest. **In the current release it makes zero live requests and writes no capture files**, regardless of the date or command parameters. Paths under `data/raw` are ignored by Git. Preserve exact bytes in a controlled study data store with appropriate rights; never silently overwrite the first capture on a retry. If a fetch fails or a parser encounters a bot page, record failure/missingness, do not convert to an empty Trending day.

**Limitation:** the manifest is client-recorded metadata. A matching hash detects later local file changes but cannot independently prove that the original HTML came from GitHub, that the server used a particular ranking formula, or that a timestamp could not have been edited. Restrict trusted data handling, preserve original network/tool logs and validate rows independently.

Only `/trending?since=daily|weekly|monthly` is supported in this strict pilot. The planned six filtered language surfaces require an explicit separate schema, known exact URLs and manually verified parser coverage first. Do **not** label captures from the three supported pages as the nine-surface panel.

## Step 2: Validate and parse the *saved* capture

```bash
python -m trending_study pilot-parse \
  --input "data/raw/$UTC_DAY-daily.html" \
  --manifest "data/raw/$UTC_DAY-daily.manifest.json" \
  --output "data/processed/$UTC_DAY-daily.pilot.jsonl" \
  --audit-output "data/processed/$UTC_DAY-daily.audit.json"
```

Checks are performed before output: HTTPS host/path and exact supported window, UTC capture timestamp/date consistency, bytes and SHA-256, declared HTML status/content type, strict UTF-8 decode, and parsed repository rows. A failed check aborts rather than inventing missing values. Each output row carries **`captured_at_utc`** and **`parsed_at_utc`** separately, with `collected_at_utc` explicitly inherited from the original captured-at timestamp. It also preserves manifest SHA-256, raw SHA-256, within-page rank and source URI.

**The pre-existing `parse-trending` command remains a fixture/legacy parser.** Because it accepts a manually supplied observation date and has no capture manifest, new output is explicitly `capture_time_status=unverified_parse_only` and `eligible_for_confirmatory_cohort=false`. It is **not** a defensible prospective baseline.

## Step 3: Perform independent page QA and identity checks

The audit JSON always reports `parser_qa_status=requires_independent_manual_audit`, `stable_repository_id_status=unresolved`, `cohort_enrollment_status=not_enrolled`. This is intentional. For any real pilot results:

- Human reviewers must independently compare **at least 30 eligible rows** across sampled windows against the actual saved page, noting invalid/duplicated rows, parser drift, rank accuracy and skipped rows. Use [manual review template](../templates/pilot_page_audit.md).
- Resolve immutable numeric repository IDs with permitted official GitHub API snapshots, track renames and missing/deleted/private reasons, never claim name-deduplication is identity-deduplication.
- Keep occurrence count distinct from **unique numeric repository ID** count; an unresolved ID is not a verified new repo.
- Preserve every skipped/missing capture, outage, source-window overlap and language coverage limitation in dated logs.
- Do not promote captured rows to confirmatory cohort without eligibility, preregistered sample selection, identity checks and independent review.

## Step 4: Freeze a real preregistration before enrollment

Review and complete [Draft v0.3](PREREGISTRATION_DRAFT_2027.md) and [signoff template](../templates/protocol_signoff.md). Only after documented access approval, audited collector QA, the independently selected task frame, real pilot-based power/precision analysis, privacy/consent for human measurements and qualified methodology review may the team declare the confirmatory design frozen. Set a distinct timestamp/immutable commit and external registration reference where applicable. The `pilot-preflight` tool only checks documentary field completeness; it cannot verify reviewer identities or authorization.

If any gate remains unfulfilled by the proposed November 1 start, **publish a dated amendment moving that start**, rather than describing pilot/historical snapshots as prospective confirmatory data.

## Offline QA, no secrets or live network required

```bash
python -m unittest discover -s tests -v
python -m trending_study --help
```

CI tests synthetic manifest creation, tamper/date/source filtering, legacy timestamp labeling, a **default-denied live capture with zero network requests**, mock-only capture code-path preservation, pilot CLI output, pending/verified documentary gates and nonzero strict gating. **Passing these tests is not the same as real-page parser or scientific-data validation.**

See [Issue #27](https://github.com/MSKazemi/github-trending-1000-study/issues/27), prerequisites [#2](https://github.com/MSKazemi/github-trending-1000-study/issues/2), [#3](https://github.com/MSKazemi/github-trending-1000-study/issues/3), [#21](https://github.com/MSKazemi/github-trending-1000-study/issues/21) and [#25](https://github.com/MSKazemi/github-trending-1000-study/issues/25).

## Additional parser drift gate — 2026-10-12

The current parser now **fails closed** if any recognized `article.Box-row` is truncated, has zero/multiple repository headers/links, invalid canonical link, or a duplicate identity. The pilot audit JSON now records a *structural-only* selector count; it cannot identify rows rendered outside that CSS selector. Read [the row-completeness rationale and independent >=30-real-row audit plan](PARSER_STRUCTURE_QA_2026_10_12.md) before any research decision. Passing synthetic tests is not permission or proof of a correct live page.


## New parser QA evidence step — still not signoff

After explicitly permitted daily/weekly/monthly captures with original UTC/SHA manifests, two real reviewers must independently transcribe **all displayed** ranks and owner/repo links, blind to parser output. Combine these into a local `data/raw/qa-bundle.json` following [the template](../templates/page_audit_bundle.template.json), then run `python -m trending_study audit-pages --bundle data/raw/qa-bundle.json --output data/processed/qa-report.json --min-rows 30 --require-consistent`. This tool distinguishes full-page enumeration from self-consistent partial parsing and handles disagreements/rejections. A `pass` means only recorded **documentary consistency**; method approval, live source review, immutable IDs and preregistration are separate. See [detailed runbook](INDEPENDENT_PAGE_AUDIT_2026_10_12.md).
