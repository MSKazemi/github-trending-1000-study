# Dated bounded source-screen checkpoint — 006-amazon

**As-of:** 2026-10-14. **PR:** [#229](https://github.com/MSKazemi/github-trending-1000-study/pull/229). **Window:** 2026-04-12 to 2026-10-12 inclusive. **Working-ledger candidate URL leads:** 9. **Research stage:** FIRST-PASS / INCOMPLETE; not accepted, externally corroborated results.

## Reproducibility and constraints

All seven month-targeted **queries below were executed on 2026-10-14** with a public web search index. Result order and completeness are not reproducible from this snapshot; the tool did **not** provide per-query total hit counts, a complete list of returned hits, archived page bytes, or the engine's indexing details. Thus the *query-result denominator*, total screened/excluded URL count, completeness and recall are all **unknown**, not zero. The sample URLs are selected retrieved official leads, not a systematic search result census.

AI-assisted inspection of readable publisher pages may verify what a publisher **wrote** and its displayed publication date, but cannot authenticate historical page revisions, confirm feature availability in a user account, establish a copyright license, independently test a benchmark, or provide the required independent human approval. Do not upgrade the original evidence tier from this exercise alone.

## Seven targeted calendar-segment queries actually submitted

| Segment | Exact submitted query | Observed official link / initial screen note | Result denominator |
|---|---|---|---|
| Apr 12–30 | `site:aws.amazon.com/blogs/devops/ 2026 April Kiro Q Developer transition` | [Selected observed source](https://aws.amazon.com/blogs/devops/amazon-q-developer-end-of-support-announcement/) — Apr 30 Q Developer IDE and paid subscription *future* end of support, not full 2026 shutdown | Hit total unknown; screen denominator unknown |
| May | `site:kiro.dev/blog/ 2026 May Kiro web specs` | [Selected observed source](https://kiro.dev/blog/introducing-kiro-web/) — May 18 Kiro Web preview for specific paid plans | Hit total unknown; screen denominator unknown |
| Jun | `site:aws.amazon.com/blogs/devops/ 2026 June Kiro agent` | [Selected observed source](https://aws.amazon.com/blogs/devops/supercharge-your-cloud-operations-with-the-kiro-power-for-aws-devops-agent/) — Jun 19 vendor Kiro power for AWS DevOps Agent, not observed deployment | Hit total unknown; screen denominator unknown |
| Jul | `site:aws.amazon.com/blogs/security/ 2026 July coding agents framework` | [Selected observed source](https://aws.amazon.com/blogs/security/balancing-speed-and-safety-a-control-framework-for-ai-coding-agents/) — Jul 30 author-time/build-time security framework is methodological advice, not evidence of risk reduction | Hit total unknown; screen denominator unknown |
| Aug | `site:aws.amazon.com/blogs/security/ 2026 August AWS Continuum agent` | [Selected observed source](https://aws.amazon.com/blogs/security/aws-partners-with-anthropic-and-openai-to-bring-aws-continuum-into-developer-workflows/) — Aug 5 AWS Continuum is described as *preview*; neutral vulnerability precision not tested | Hit total unknown; screen denominator unknown |
| Sep | `site:kiro.dev/blog/ 2026 September Kiro IDE CLI` | [Selected observed source](https://kiro.dev/changelog/web/introducing-workflows/) — Sep 30 dated Workflows release and opt-in Kiro Web scope; exact permalink retained in event CSV | Hit total unknown; screen denominator unknown |
| Oct 1–12 | `site:kiro.dev/blog/ 2026 October 1 12 Kiro CLI 3` | [Selected observed source](https://kiro.dev/blog/cli-3/) — Oct 9 announcement distinguishes early October prompt rollout from **future** month-end general default | Hit total unknown; screen denominator unknown |

**Interpretation:** A row with no qualifying retrieved URL records *unknown screened coverage*, never a zero-release finding. A reported publication date is not necessarily the first moment a feature was generally available. Links are leads and their article contents can change. May updates to pre-window April articles, and items after October 12, must not be silently counted as new eligible releases. Total independently screened or excluded URLs remain unavailable; no systematic recall assertion is made.

## Specific corrections, counterclaims, and practical test

1. Primary source and AWS user guide distinguish Amazon Q Developer *IDE plugins and paid subscriptions* due Apr 30 2027 from Q Developer in AWS Console and first-party experiences (not impacted). See https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-developer-ide-end-of-support.html.
2. Kiro Web preview May 18 is plan-limited. The Sep 30 reusable workflow feature is explicitly opt-in according to its dated changelog. An opt-in product launch is not an independent measured accepted-task outcome.
3. Recheck scope before importing agentic security components: AWS Continuum is labelled Preview in its Aug 5 blog, while the July 30 security framework is guidance.
4. Useful maintainer test: freeze a testable design/spec-first maintenance task, compare to an existing test-first baseline, measure reviewed correctness, rejected tasks, CI/runtime and human effort.

## Required review and non-claims

- [ ] Independent qualified human source, date, entity, permissions and methods sign-off; this AI-assisted checkpoint is not that review.
- [ ] Repeat every month segment against publisher archives AND credible independent reporting, keeping full returned-hit denominators, checked URLs, excluded URLs, immutable captures and query timestamps (not supplied by the current tool).
- [ ] Resolve claims of GA vs preview vs announced and contradictory exact-artifact license/access states without promoting original vendor-only confidence grades to E3/E4.
- [ ] Check security, permission boundaries, downstream actual acceptance, real outside reuse, vendor pricing, full human/CI lifecycle costs and any environmental metrics **by measurement**, not by marketing or token counts.
- [ ] Obtain final-head CI and safe integration verification; retain the underlying company issue open until genuine scientific acceptance.

This file is a **source-screen audit trail**, not an endorsement, user study, company ranking, proof of safer code, causal claim or permission to publish completed research.


## 2026-10-15 secondary-source and artifact QA supplement

**Access/read status:** A dated AI-assisted public-source desk check. Selected pages were read or located via public web search on 2026-10-15. URLs and journalistic observations are reproducible *leads*, not signed/archived historical captures, systematic recall, independent human signoff or measured task outcomes. Retrospective study publication cutoff is **2026-10-12**; post-window analysis must remain separate.

### AWS — third-party caution and exact service boundary

- **First-party notice, 2026-04-30:** [AWS Amazon Q Developer end-of-support announcement](https://aws.amazon.com/blogs/devops/amazon-q-developer-end-of-support-announcement/) says Q Developer **IDE plugins and paid subscriptions** reach end of support **2027-04-30**. AWS Console, Chat Apps, and other first-party surfaces are expressly excluded from that sunset. [AWS user documentation](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-developer-ide-end-of-support.html) separately repeats the IDE scope. This is a publisher-reported policy, not evidence of all Amazon Q services terminating in 2026.
- **Independent newsroom reporting, 2026-04-29:** [The Register — Amazon tells its engineers to review all AI output](https://www.theregister.com/software/2026/04/29/amazon-tells-its-engineers-to-review-all-ai-output/5224124) reports employee/executive perspectives on AI coding, hallucinations, off-task agent behavior and review requirements. This is useful as adversarial reporting; interviews do not provide a denominator or controlled comparison of AWS Kiro acceptance/cost.
- **First-party versioned product item, 2026-09-30:** [Kiro Web Workflows changelog](https://kiro.dev/changelog/web/introducing-workflows/) says the workflow was **opt-in**, not universally enabled. Avoid backdating planned default rollouts and measure end-to-end independent acceptance rather than how many workflows run.

**Practical repository consequence:** keep agent-generated changes behind human review, immutable test fixtures and bounded permissions; when planning CLI migration, version-pin both the old Q Developer IDE state and the replacement Kiro workflow and explicitly record support dates, access and failover.
