# 2026-10-12 issue recheck and conservative pre-search task-screening instrument

**Status:** a narrow **observed public REST metadata recheck** plus **offline synthetic-tested review bookkeeping**. Not human-independent judgments, a frozen task benchmark, an experiment, an AI productivity result, a reuse verification or a sustainability claim. Related [issue #65](https://github.com/MSKazemi/github-trending-1000-study/issues/65).

## What actually happened

The original [six-repository, first-page convenience frame](../examples/task_intake.cross_ecosystem_2026-10-12.json) contains 90 GitHub REST issue/PR rows; the existing deterministic selector picked 16 public non-PR issue leads *before looking for reusable solutions*.

On **2026-10-12**, we made a bounded **16-request** public GitHub REST `GET /repos/{owner}/{repo}/issues/{issue_number}` recheck through the connected GitHub app. **Batch completion UTC:** `2026-10-12T20:25:45.446Z`. The [minimized metadata snapshot](../research-notes/issue-recheck-2026-10-12.json) binds to the source frame using SHA-256 `0ddc27c1aed05b2d42bbf1337b7574d382594d499e1c8784ea6f19ea68e485f0`.

| Recheck measurement | Actual limited result | What cannot be inferred |
|---|---:|---|
| Original hash-selected issue leads | 16 | Not an independent probability sample of OSS tasks |
| Successfully matched GitHub numeric issue IDs and canonical issue links | 16/16 | Not a review of original requirements, patches, licenses or user consent |
| Issue state at recheck | 16 open / 0 closed | Open does not mean actionable, defect is confirmed or task is independent |
| API `updated_at` after the original reduced-intake `updated_at` | 0/16 | Equal timestamps do **not** attest unchanged content, undisclosed references, or complete response history |
| Inaccessible/rate-limited/missing metadata | 0/16 | Only 16 selected records rechecked; no all-GitHub coverage |
| Human reviewer judgments | 0 | Review fields and independent reviewers still missing |
| Independent acceptance suites / verified reuse opportunities / experiments | 0 | No efficacy or environmental conclusion |

**Provenance limitations:** This is a series of public issue API reads, **not** GitHub Trending scraping. Snapshot timestamp is **end of retrieval batch**, not an individually server-attested time. The raw full HTTP responses/headers, etags, intermediary caches and per-request UTC times were **not preserved**. The JSON stores only issue identity, URL, current open/closed or unavailable state, `updated_at`, `closed_at`, and error type; no reporter usernames, issue bodies, private data or raw security details. The first source panel was convenience-selected and is **not a random sample of all open issues**.

## Important methodological finding from unblinded preliminary inspection

During this implementation an **AI-assisted unblinded analyst** also read public issue descriptions. Several selected issues present reproduction details, likely root causes, explicit implementation suggestions or already discussed patches. For example, [Rich #4211](https://github.com/Textualize/rich/issues/4211) contains a concrete negative-cell-width reproduction, [Vite #23735](https://github.com/vitejs/vite/issues/23735) discusses a prospective fix, and [Axum #3913](https://github.com/tokio-rs/axum/issues/3913) discusses a performance hypothesis with comparative measurements. This observation is **not** a double-blind screening result or confirmation that the reported bugs/fixes are correct.

**Protocol implication:** distinguish two genuinely different evaluation designs:

- **Real maintenance workflow:** allow the original public issue, its hints, known fixes, and public context, and measure completing maintenance work as practiced. Clearly state agent may have viewed a proposed answer. Do not interpret performance as independent discovery ability.
- **Independent task-solving benchmark:** have unaffiliated task authors prepare neutral, versioned task specs and independent functional/security acceptance tests without including reporter-suggested fixes; record possible pretrained/public solution leakage. True concealment of previously public fixes cannot be guaranteed. Prefer newly specified, held-out task variants when justified and permitted.

Do **not** use this AI analyst's unblinded observations as either human reviewer's answers. Avoid giving independent screeners this analysis until their initial reviews are filed. Never remove inconvenient tasks because a good reuse solution was not found.

## Offline source-bound screening packet

No new crawler, dependencies or network calls are involved in the tool. Reuse the existing `trending_study.task_intake.sample` for candidate identities and `trending_study.safe_io.publish_json` for write-once outputs.

```bash
python -m trending_study.task_screen prepare \
  --frame examples/task_intake.cross_ecosystem_2026-10-12.json \
  --recheck research-notes/issue-recheck-2026-10-12.json \
  --output /tmp/issue65-screen-packet.json

python -m unittest discover -s tests -v
```

`prepare` verifies the 16 selected issue IDs and URLs, SHA-256 frame binding, completeness, time ordering, absence of added personal/body fields, and consistent observed/unavailable statuses. The deterministic output identifies the public issues but says `human_independence_verified=false`, `experiment_enrollment=blocked`, `review_state=unreviewed`, `task_acceptance=not_frozen`, and `reuse_opportunity=unknown`. A failed fetch stays **unavailable/unknown**, never "not reusable."

## For genuine independent reviewers: submit only after independently screening

Each reviewer should independently receive the **same source-bound packet** but submit **separate data**. Keep signed/consented human identity verification outside the public repository; use distinct pseudonyms and avoid committing private responses. A document's `reviewer_ref` **cannot** cryptographically establish an actual person, independence, consent or that they did the work.

Each reviewer JSON must have exactly:

```json
{
  "schema_version": "1.0",
  "packet_sha256": "<the actual prepare output packet_sha256>",
  "reviewer_slot": "A",
  "reviewer_ref": "<distinct anonymous reviewer reference>",
  "reviewed_at_utc": "<actual ISO8601 UTC timestamp>",
  "decisions": [
    {
      "task_id": "GH-4379284998",
      "label": "defer_unknown",
      "reason_code": "unknown",
      "leakage_signal": "unknown",
      "issue_status_check": "unknown",
      "evidence_ref": null
    }
  ]
}
```

**This JSON snippet is a schema illustration, not a submitted assessment.** Slot B uses `"B"` with a genuinely separate person. Labels: `screenable_for_spec_drafting` (reason `none` with evidence reference), `exclude_candidate` (specific reason plus evidence reference), or `defer_unknown` (unknown/other reason). Reason codes: `none`, `unsafe`, `rights`, `scope`, `underspecified`, `nonreproducible`, `leakage`, `duplicate`, `unknown`, `other`. Report possible public solution hints with `leakage_signal=suspected`; `not_observed` is **not proof** that no leakage exists. `evidence_ref` is a bounded reference, **not** an issue-body copy or personal data field.

**Fail-closed leakage screen (technical guard, not proof):** A candidate proposed as `screenable_for_spec_drafting` is downgraded to `defer_unknown` when any A/B/C report identifies `leakage_signal=suspected` (`deferred_leakage_suspected`) or has not assessed leakage (`deferred_leakage_unknown`). A conflicting or unavailable public issue status is deferred separately as `deferred_source_status`, taking precedence when both risks apply; the leakage signal remains visible in the record. These deferrals preserve all original candidates in the denominator. Unanimous `not_observed` is only a self-reported *lack of observed hints*, not a claim of hidden independent task design, absence from training data, or human review authentication. This gate only controls provisional spec-drafting labels, never experimental enrollment.

An independent adjudicator C may file decisions **only for actual A/B label disagreements** and only after A and B finish. The C timestamp must be **strictly later** than both submitted review timestamps; reviewer pseudonyms must be distinct **case-insensitively**, and the placeholder `unknown` is rejected. These checks prevent obvious duplicate-role claims but **do not authenticate real human independence**. Unknown and unresolved evidence remain unknown. Partial submissions are allowed but produce `missing_independent_review`, never silent negative decisions.

When genuine human reviews are available (not yet):

```bash
python -m trending_study.task_screen audit \
  --frame examples/task_intake.cross_ecosystem_2026-10-12.json \
  --recheck research-notes/issue-recheck-2026-10-12.json \
  --review-a /path/to/approved-private-a.json \
  --review-b /path/to/approved-private-b.json \
  --output /tmp/issue65-structural-audit.json
```

Add `--adjudication /path/to/private-c.json` for genuine disagreements after both have submitted. This audits **the structure of claims**, not their truth. Even unanimous "screenable" reports produce `concordant_provisional`, **0 accepted tasks**, `task_specs_frozen=false` and `experimental_enrollment=blocked`.

## Next substantive, permission-dependent scientific gates

1. Two real independent reviewers review all 16 issue leads **without seeing this unblinded preliminary interpretation**, with structured attrition reasons, evidence references and third-party risk consideration. Re-check if issues changed during their reviews.
2. Independent authors neutralize public solution hints **if using a task-solving design**, then freeze reproducible task specs, negative tests and baseline environments, rather than assuming the GitHub issue body is a hidden challenge.
3. An ethics/privacy steward and statistician approve recruitment, power, randomization, leakage safeguards, license/supply-chain restrictions and nonparticipating upstream maintainer policy.
4. Only then evaluate solution search, compatibility/security, externally accepted functionality, human effort, later support and environmental boundaries. Do not infer carbon from issue status or tokens.

**Practical repository-maintainer lesson (hypothesis, not experimentally demonstrated):** write high-quality reproducible issue reports, maintain a link from proposed fixes to independent tests, and require AI contributions to search, verify and cite existing implementations before generating new components. When using a public issue as an AI benchmark, treat exposed patches as part of the task context, not as hidden independent intelligence tests.
