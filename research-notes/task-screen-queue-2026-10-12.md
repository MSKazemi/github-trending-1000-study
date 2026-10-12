# Screen queue: 16 unreviewed, hash-selected public issue leads

**2026-10-12 · Exploratory source-frame checklist, not a trial task cohort.** This queue was deterministically derived from [the 90-row input](../examples/task_intake.cross_ecosystem_2026-10-12.json) using `trending_study.task_intake.sample`: the first 15 latest-created open issue/PR records from each of six conveniently chosen repositories; pull requests excluded; three issue leads per repo where available. The `priority` shown is the first 12 characters of the SHA-256 selector digest, **not an importance/quality score**. This Markdown is a convenience projection, not an independent data source.

| Queue | Original public issue link | SHA-256 selector prefix | Human screening |
|---:|---|---|---|
| 1 | [pallets/click #3406](https://github.com/pallets/click/issues/3406) | `0dd01fd9227a` | Unreviewed |
| 2 | [pallets/click #3097](https://github.com/pallets/click/issues/3097) | `11e243f696b5` | Unreviewed |
| 3 | [pallets/click #3847](https://github.com/pallets/click/issues/3847) | `1904ba013d97` | Unreviewed |
| 4 | [Textualize/rich #4211](https://github.com/Textualize/rich/issues/4211) | `1398062ea992` | Unreviewed |
| 5 | [Textualize/rich #4224](https://github.com/Textualize/rich/issues/4224) | `14614dfe138b` | Unreviewed |
| 6 | [Textualize/rich #4223](https://github.com/Textualize/rich/issues/4223) | `244b0eae3789` | Unreviewed |
| 7 | [psf/requests #7629](https://github.com/psf/requests/issues/7629) | `040b506a5421` | Unreviewed |
| 8 | [psf/requests #7574](https://github.com/psf/requests/issues/7574) | `05d42771fc57` | Unreviewed |
| 9 | [psf/requests #7610](https://github.com/psf/requests/issues/7610) | `200f5a409b65` | Unreviewed |
| 10 | [vitejs/vite #23727](https://github.com/vitejs/vite/issues/23727) | `36e39bdf8f22` | Unreviewed |
| 11 | [vitejs/vite #23735](https://github.com/vitejs/vite/issues/23735) | `568c5636b168` | Unreviewed |
| 12 | [vitejs/vite #23719](https://github.com/vitejs/vite/issues/23719) | `7dd2fbbef926` | Unreviewed |
| 13 | [tokio-rs/axum #3913](https://github.com/tokio-rs/axum/issues/3913) | `2d121012270a` | Unreviewed |
| 14 | [tokio-rs/axum #3914](https://github.com/tokio-rs/axum/issues/3914) | `4a5090f004af` | Unreviewed |
| 15 | [prometheus/prometheus #19984](https://github.com/prometheus/prometheus/issues/19984) | `ba2a2580f26a` | Unreviewed |
| 16 | [prometheus/prometheus #20000](https://github.com/prometheus/prometheus/issues/20000) | `ec92e21980d3` | Unreviewed |

**Current scientific status:** 16/16 are `unreviewed`; task specifications `not_frozen`, independent acceptance `not_frozen`, and reuse opportunities `unknown`; no developer has consented to a study assignment. The original source is a mutable issue page: check current status and potential solution leakage before drafting any task specification. Do not begin by searching for a suitable reusable package, reading agent-generated solutions or building code. Some issues may be unsuitable or have known fixes; record all exclusions without replacing them to improve outcomes.

## Human review workflow

1. Two genuinely independent reviewers each fill [the pre-search screening card](../templates/feasibility_task_review_card.md) for **each of the 16**; reviewers must not see each other's ratings until completed.
2. Preserve pass/fail/unknown, disagreement, exclusions, issue state changes, and any third-party/privacy/security concerns. A selected GitHub issue is **not** automatically a task.
3. Independently freeze neutral functional and negative/security acceptance tests and versioned environments **before** introducing reusable-code candidates or assigning agent/human interventions.
4. Require participant consent, approved study protocol and independently checked source rights before any actual trials. Use the [methodology and documented limitations](../docs/CROSS_ECOSYSTEM_TASK_INTAKE_2026-10-12.md) and [existing preregistration draft](../docs/PREREGISTRATION_DRAFT_2027.md). **Do not claim paper-grade results from this queue.**

To independently reproduce the full selection (including 46 excluded PRs and 28 unsampled issues):

```bash
python -m trending_study.task_intake \
  --input examples/task_intake.cross_ecosystem_2026-10-12.json \
  --output /tmp/oss-screen-queue-2026-10-12.json
```

Inspect the `selected_for_independent_task_screen` rows in `ledger`. Unknown candidate relevance is not a negative gold label.
