# Is GitHub Trending a valid metric? Construct and validity audit

**Updated:** 2026-10-11. GitHub's public [Trending](https://github.com/trending) page says it displays what the community is excited about, with relative rows, total stars, forks and period-specific stars-gained labels. It does **not** disclose the complete ranking function or eligible candidate universe. The [third-party collection methodology](https://githubtrending.today/methodology/) explicitly separates page order, display labels and unknown algorithm weights. This is an audit **proposal**, not a completed verification.

## What is valid vs unsupported
| Page element | Observable, valid operational variable | Invalid leap |
|---|---|---|
| Appeared in snapshot | Boolean observed page membership on exact UTC capture/filter/window | 'Successful' or 'useful' repository |
| Displayed order | Within-page rank with page length captured | Quality index or true global popularity rank |
| Stars today/week/month | The **displayed** label as reported by GitHub at that instant | A verified exact count within our own UTC 24h/7d/30d intervals |
| Total stars/forks | Metadata snapshot | Unique working users, deployment, reuse or user satisfaction |
| Repeated captures | Exposure frequency within sampled surfaces | All actual Trending impressions or clicks |
| Appearance probability | Under defined observed eligible sampling frame | All-GitHub eligible probability unless denominator established |
| Language filtered pages | GitHub category appearances | Worldwide language adoption or objective fairness |

## Specific threats and validation tests
1. **Opaque ranking algorithm:** there is no published formula/candidate frame to validate rank accuracy as one objective score. Report ranking *stability and consistency*, never 'we reverse-engineered GitHub'.
2. **Burst/virality:** promotional events, paid attention, novelty and existing audiences may produce stars independent of code utility. Track reported period stars and release/publicity context where ethically documented; do not accuse individuals without evidence.
3. **Sampling intervals:** 'Today', weekly and monthly pages overlap, and one UTC snapshot/day misses intra-day turnover. Record actual time, filter, page length, capture failures, source checksum and intervals; do not treat snapshots as independent events.
4. **Timezone/window disagreement:** the displayed period stars do not prove alignment with UTC collection dates; compare prospectively collected count-differences only when timestamps bracket matched intervals. Report distribution of error and unclear window boundaries, not 'fake' by default.
5. **Language & project-type biases:** code repos, curated lists, frameworks, datasets and templates differ; non-English projects may be underrepresented depending on selected filters. Stratify and compare to a **specified candidate frame**, not 'all GitHub' without a probability sample.
6. **Age advantage and cold start:** absolute stars correlate with project lifetime, but a new repo can experience a burst. Distinguish total stars, net new stars, relative growth and selection.
7. **Temporally unstable site:** GitHub may modify UI, language mapping or selection rules. Keep parser version and manually validated random page snapshots; detect list size / HTML drift; never reuse old parser blindly.
8. **Manipulation/campaigns:** star exchanges and bots can change attention signals. No precise public 'fraud probability' without permitted evidence; use anomaly sensitivity analysis with non-accusatory labels.
9. **Search/SEO selection:** people who are most visible may attract stars and contributors even if the software is unusable. Trending is a **selected collider**, not independent evidence of engineering practices causing success.
10. **Lagged adoption:** user need and downstream reuse can emerge months later; 30/90/180-day follow-up plus direct task tests rather than same-day rankings.

## Validity framework and planned metrics
- **Content/face validity:** does the variable measure *observed visibility*? Yes, provided verified capture; does it measure *usefulness*? Not directly.
- **Reliability:** same-page repeated captures (when permitted), duplicate/parse audit, capture uptime %, within-filter list overlap (Jaccard/RBO), rank reproducibility (Kendall tau-b on intersection), time-of-day sensitivity.
- **Convergent validity:** stars-gained label vs independently timestamped daily star-delta **with matched boundaries**; report difference and uncertainty, missing count.
- **Discriminant validity:** hypothesize weak/non-uniform association between rank and audited onboarding, functional reuse, safety; test, do not assume negative or positive.
- **Predictive validity:** predict *future independently verified use* or stable 90-day user-task success for a subset, not only future stars, and report controls + CI. No causality.
- **Fairness/coverage:** compare project type, age, language, ecosystem against an explicitly constructed at-risk candidate frame, with its sampling bias stated.
- **Failure analysis:** document no captures, rank changes, star-label anomalies, revisions and GitHub UI drift.

## Key conclusion, stated carefully
GitHub Trending is a **valid source of observed page inclusion/order at a time** when captures are validated. It is a **weak, unvalidated proxy** for usefulness, reproducibility, sustainability or software reuse. We must **not drop** it; we must attach an explicit construct label and independently measure genuine value.

## Alternatives beyond Trending
Dependency registry usage *as a proxy* (not automatic proof of real users); package import/dependency graphs with known false positives; independently audited upstream reuse and integration PRs; clean install/task passes; opt-in repeat user jobs; verified scientific replication, maintenance and security. These complement rather than replace longitudinal attention metrics.

References: [green bibliography G13–G14](../references/green_reuse_sources_2026.json), [selection](SELECTION_PROTOCOL_2027.md), [black-box ranking audit](TRENDING_ALGORITHM_AUDIT.md).
