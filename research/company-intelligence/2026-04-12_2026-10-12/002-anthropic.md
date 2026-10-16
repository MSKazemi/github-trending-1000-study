# Company 6-month technology intelligence: Anthropic

- **Watchlist ID:** 002; **research issue:** [#68](https://github.com/MSKazemi/github-trending-1000-study/issues/68)
- **Analysis window:** 2026-04-12 through 2026-10-12 inclusive (UTC)
- **Recorded initial source review:** 2026-10-12; automated research assistance; **independent human factual/link reviewer: pending**
- **Stage:** **partial, source-screened working report**, NOT a completed six-month audit or independently corroborated study finding
- **Primary landing page:** https://www.anthropic.com/claude-code; **method:** [company protocol](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md)
- **Evidence semantics:** E1 below denotes first-party publication evidence for *what a vendor says*. It is not the main study's E1 descriptive observational outcome, and cannot validate model quality, adoption, net savings or safety.

## 1. Reproducible search and inclusion audit

| Review UTC date | Channels and actually targeted discovery terms | Result count | Included from directly readable first-party sources | Selection/coverage limitation |
|---|---|---|---|---|
| 2026-10-12 | Open-web search plus official product/news/release pages: `site:anthropic.com/news "Claude Sonnet 5" June 2026; site:anthropic.com/news "Claude Opus 5.5" September 2026` | Not reliably available from retrieval interface | 3 dated events below | Selective source screen; no archived exhaustive query return sets, no independently audited source inclusion |
| 2026-10-12 | Relevant independent published benchmark or investigative evidence | Not comprehensively screened | None independently validated for this report | Independent reproduction and negative cases remain work to do |

**Non-inclusion rule:** Homepage, search snippets, and undated vendor summaries by themselves do not count as dated shipped features. Search-result totals and source sensitivity are **unknown**, never zero. The required systematic April/May/June/July/August/September/October screen, independent reporting check and second-pass URL/date QA are **still pending**. This document is a useful early deliverable, **not issue acceptance**.

## 2. Identity and product boundary

Anthropic's Claude models, Claude Code and the Claude Platform are different product surfaces. The model announcements below do not automatically establish a shipped improvement in Claude Code workflows. Identity snapshot is inferred from linked company-controlled sources; legal/corporate independent verification is outstanding.

## 3. Month-by-month dated material found in this first pass

| Segment | Located eligible in-window item | Primary source | Independent reporting | Coverage / missingness |
|---|---|---|---|---|
| 2026-04-12–30 | No qualifying item validated during this targeted pass (NOT an assertion of zero releases) | — | No independent task audit | Full calendar-month sweep pending; missing evidence ≠ inactivity. |
| 2026-05 | No qualifying item validated during this targeted pass (NOT an assertion of zero releases) | — | No independent task audit | Full calendar-month sweep pending; missing evidence ≠ inactivity. |
| 2026-06 | Introducing Claude Sonnet 5 | [primary](https://www.anthropic.com/news/claude-sonnet-5) | No independent task audit | These sources were directly reviewed; other releases not exhaustively searched. |
| 2026-07 | No qualifying item validated during this targeted pass (NOT an assertion of zero releases) | — | No independent task audit | Full calendar-month sweep pending; missing evidence ≠ inactivity. |
| 2026-08 | No qualifying item validated during this targeted pass (NOT an assertion of zero releases) | — | No independent task audit | Full calendar-month sweep pending; missing evidence ≠ inactivity. |
| 2026-09 | Claude Sonnet 5.5 | [primary](https://www.anthropic.com/claude-sonnet-5-5) | No independent task audit | These sources were directly reviewed; other releases not exhaustively searched. |
| 2026-10-01–12 | Claude Haiku 5.5 | [primary](https://www.anthropic.com/claude-haiku-5-5) | No independent task audit | These sources were directly reviewed; other releases not exhaustively searched. |

## 4. Dated event, claim and capability ledger

| Event | Publication / underlying event | Evidence-backed claim (no external performance certification) | Actual availability or status | Exact source and type | Independent check | Company-watch tier |
|---|---|---|---|---|---|---|
| 002-E01 | 2026-06-30 / 2026-06-30 (announcement or document date; implementation date unverified) | Introducing Claude Sonnet 5: Announced Sonnet 5 for agentic tool use and coding. Published changelog documents a June 30 revision to BrowseComp methodology presentation and an August 10 pricing update: historic page content is mutable. | vendor model offering; benchmarks and pricing self-reported | [First-party source](https://www.anthropic.com/news/claude-sonnet-5) | No independent functional replication in this pass | E1: vendor-dated claim / description |
| 002-E02 | 2026-09-28 / 2026-09-28 (announcement or document date; implementation date unverified) | Claude Sonnet 5.5: Vendor announced revised model capabilities, effort settings, coding use and prices; reported comparative benchmarks are not independently replicated here. | announced available across platforms; plan/model constraints require testing | [First-party source](https://www.anthropic.com/claude-sonnet-5-5) | No independent functional replication in this pass | E1: vendor-dated claim / description |
| 002-E03 | 2026-10-07 / 2026-10-07 (announcement or document date; implementation date unverified) | Claude Haiku 5.5: Vendor introduced a smaller model targeted at cost-sensitive/high-volume tasks and subagent workflows; advertised speed/cost benefit is company-reported. | announced available; third-party task validity unknown | [First-party source](https://www.anthropic.com/claude-haiku-5-5) | No independent functional replication in this pass | E1: vendor-dated claim / description |

**Caution:** For all ledger events, publication and the company's claimed effective event date are treated as coincident only for this initial announcement record; an operational first-deployment or customer-use date has **not** been independently recovered. Additional revision history, pricing and license/API guarantees have not been fully archived. No product was installed or benchmarked.

## 5. Public direction versus future plan

**Attributed 2026 direction, not a guaranteed roadmap:** Anthropic publicly describes differentiated model tiers and effort settings for agentic workflows in the 2026-09-28 and 2026-10-07 announcements. Distinguish stated marketing from a contractual roadmap. No separately dated binding 2027 product commitment was validated.

**Planned 2027–2031 releases verified:** none in this first pass. This means *not established by reviewed primary material*, **not** that no roadmap exists.

## 6. Researcher's conditional 2027–2031 interpretation

Conditional hypothesis: route small retrieval/triage tasks to a smaller model and difficult patch tasks to a larger one to reduce cost per independently accepted task. Rival: coordination, retries and escalation eliminate savings; falsifier: worse final acceptance or higher total reviewer+run cost. This is an **E0 research hypothesis**, not vendor strategy or a demonstrated causal effect.

## 7. Testable connection to the GitHub 1000 study

Relevant constructs: M1 agent/model selection workflows, M2 task quality, M5 appropriate code reuse, M6 whole-life costs. See [M1–M7 operational definitions](../../../docs/AI_ERA_CODING_REUSE_RESEARCH_MISSION.md). The study has **not** measured vendor-driven adoption or avoided energy use. A changed tool workflow, repository star count, or claimed token reduction cannot substitute for independent usability and reuse outcomes.

**Null / rival result worth publishing:** The new practice might yield **no** increase in task acceptance, external reuse or review efficiency while introducing extra tool calls, dependencies, licensing burdens, costs or maintenance.

## 8. One bounded, falsifiable experiment for this study repository

**Candidate:** Pre-freeze five offline issues with independent acceptance tests, including intentional no-reuse cases. Compare one-model execution with an explicit small-model triage plus larger-model implementation workflow; pin exact model versions, prompts, dates, token accounting and human review time.

**Primary outcome:** accepted task completion under a predeclared, **independently authored** rubric; report failures/abstentions in denominator. **Secondary:** 1st-run success for external maintainers (only if actually recruited), median human review/repair minutes, version/cost/permissions and dependency evidence; measure kWh only if metered with an explicit workload/boundary. **Status:** proposed, not performed.

**Stop / reversal rule:** Reject tiered routing if acceptance worsens, sensitive code reaches an unapproved provider, or total lifetime review/runtime cost increases.

## 9. Provisional lesson, remaining work and reviewer status

- **Practical lesson (hypothesis to test, not recommendation):** route small retrieval/triage tasks to a smaller model and difficult patch tasks to a larger one to reduce cost per independently accepted task.
- **Evidence risk:** Do not treat vendor benchmark or unit token-price claims as cost per successful maintained task. Record source edits and model drift; initial benchmark/chart correction is a concrete audit caveat.
- **Not established:** entire six-month event coverage, external model benchmark comparability, true user adoption, measured whole-life CO2e or energy, counter-evidence, legal ownership beyond vendor assertions.
- **Independent 2nd reviewer / link QA:** **pending**. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open.
- **Required next pass:** month-specific queries with preserved dates/results, independent high-quality reporting and corrections, archive exact release/version availability and product license/plan boundary, external functional test or explicitly absent, human review.
- **No corpus inflation:** these first-party announcements are *not* added to the 1,000-news corpus pending independent full article screening and deduplication.

**Related protocols:** [reuse-first playbook](../../../docs/REUSE_FIRST_PLAYBOOK.md) · [evidence-to-lesson grading](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md) · [company report template](../../../templates/company_six_month_intelligence.md).


## 2026-10-14 provisional source-preservation integration (not empirical validation)

An AI-assisted source reviewer checked official Anthropic announcements and dates for Claude Sonnet 5 (June 30), Sonnet 5.5 (September 28), and Haiku 5.5 (October 7). Vendor benchmark, token-price, and claimed speed/efficiency figures were **not independently reproduced** or converted to energy impacts. The Sonnet 5 source has a later August 10 pricing edit and June 30 methodology correction, so a snapshot of its current text is not an immutable record of the original post. This E1 first-pass company shortlist can be preserved as working research per maintainer request, but is **not** accepted as a complete systematic six-month study, independent human factual review or tested recommendation. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open (publication-archive versioning, legal/source review, complete monthly search and measured reuse-first trials are still outstanding); previous draft-stage scientific-review holds are not silently declared satisfied.

## Standardisation upgrade (2026-10-16)

> **PROVISIONAL, AI-ASSISTED, NOT HUMAN-REVIEWED.** This section adds a standard 21-column ledger, [`002-anthropic.events.csv`](002-anthropic.events.csv), a [search log](002-anthropic.search-log.md) and a source check of the earlier text above. Text above this heading is unchanged except for the two closure sentences reworded to the standard form. Provisional screen; the issue may be closed with this status recorded, and human factual/link, rights and methods review gates remain open. Related: [#68](https://github.com/MSKazemi/github-trending-1000-study/issues/68), news corpus [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56).
>
> **Conflict of interest.** This upgrade was prepared with an Anthropic model (Claude) researching Anthropic. Which events were included or left out, how claims are summarised, and which criticisms are reported may lean in Anthropic's favour. A human reviewer must check the selection and wording before any of it is relied on. To reduce the risk, the ledger includes every in-window Claude Code security advisory, user-reported billing and quality incidents, and independent critical research. It does not include Anthropic's own success claims about itself unless they are recorded as vendor statements.

### What the ledger adds

- **49 dated rows** (`CI2026-002-001`…`049`), screened 2026-10-16. Per segment: Apr 12–30: 7 · May: 7 · Jun: 11 · Jul: 3 · Aug: 6 · Sep: 10 · Oct 1–12: 5. No segment is empty. The earlier "no qualifying item validated" for April, May, July and August was a gap in coverage, not a quiet period.
- **Status mix:** 28 shipped, 10 reported_undetermined, 5 announced_only, 3 corrected, 2 preview, 1 reversed/cancelled.
- **Source mix:**
  - 12 GitHub security advisories, from the advisory API. Each is matched to the npm publish time of its patched version.
  - 2 user-filed GitHub issues that have maintainer replies.
  - 7 independent third-party sources: Semafor, thereallo.dev, Systima, Daring Fireball, Embrace The Red, Armature and blog.szypowi.cz.
  - The remaining rows are Anthropic pages, the dated Claude Platform release notes and the Claude Code changelog.
- **Pages not fetched:** several mainstream outlets disallow Claude/Anthropic agents in robots.txt, including TechCrunch, The Verge, AP, CNBC and Reuters. They were not fetched, and their headlines are not used as evidence (search log, access table).

### Crosswalk: earlier report → ledger

| Earlier claim (section) | Ledger event_id | Status after source check |
|---|---|---|
| 002-E01 Claude Sonnet 5, 2026-06-30. Page carries a June 30 BrowseComp methodology correction and an August 10 pricing edit (§3, §4) | CI2026-002-023 | **confirmed.** Both edit notes appear in the raw page text, and the page metadata `publishedOn` is 2026-06-30T18:00Z. The Aug 10 edit makes the introductory $2/$10 per MTok price permanent, and the planned $3/$15 from Sep 1 no longer applies. |
| 002-E02 Claude Sonnet 5.5, 2026-09-28: capabilities, effort settings, coding use and prices (§3, §4) | CI2026-002-042 | **confirmed.** The date is on the page and in the release notes. The page charts cost per task at every effort level and claims "up to 30% less" cost. The release notes confirm availability on the Claude API, Bedrock, Claude Platform on AWS, Google Cloud and Microsoft Foundry, and list five breaking changes from Sonnet 5. |
| 002-E03 Claude Haiku 5.5, 2026-10-07: smaller, cost-sensitive model for subagent workflows (§3, §4) | CI2026-002-046 | **confirmed.** The page says it "pairs well with Opus 5.5 and Sonnet 5.5 as a subagent on coding work" and costs "around 75% less" than Haiku 4.5 (vendor claim). |
| April, May, July and August: no qualifying item validated (§3) | 001–014, 026–034 | **corrected.** See Corrections, item 1. |
| Model tiers and effort settings named only in the Sep 28 and Oct 7 announcements (§5) | 002, 014, 027, 035, 039, 042, 046 | **corrected and extended.** Effort controls (xhigh on Apr 16; the full ladder with Opus 5 on Jul 24) and tiering appear across the window, not only in the last two announcements. |
| 2026-10-14 integration: dates June 30, September 28 and October 7 | 023, 042, 046 | **confirmed** |
| "Initial benchmark/chart correction is a concrete audit caveat" (§9) | 023 | **confirmed.** Further revisions to vendor benchmarks are recorded on the Sonnet 5 page itself (Humanity's Last Exam grader, OSWorld-Verified rerun of Sonnet 4.6). |
| Planned 2027–2031 releases verified: none (§5) | — | **still none.** Only near-term dated vendor statements were found (see below). |

No earlier claim turned out to be unverifiable.

### Corrections to the earlier report (stated here; earlier text left as written)

1. **Coverage.** The earlier report found three September–October model posts. This pass finds dated, in-window material in every segment. Most of it matters more to a coding-agent study than model launches do: harness regressions and their postmortem (005), billing and usage incidents (001, 007), nine Claude Code security advisories, and changes to default autonomy (029).
2. **Omitted model events.**
   - The earlier §3 table lists Sonnet 5.5 as the September item but omits Claude Opus 5.5 (Sep 22, 039), the first model of the 5.5 family.
   - It also omits Claude Fable 5.1 / Mythos 5.1 (Sep 1, 035).
   - Most importantly, it omits Claude Fable 5 / Mythos 5 (Jun 9, 015). US export controls suspended access to that model line on Jun 12 (016), and access was restored on Jul 1 (024; Semafor 022 independently reports the Jun 26 approval for Mythos 5). This is the largest availability event in the window.
3. **The routing hypothesis in §6 and §8 has a vendor-native comparator.** The release notes document an **advisor tool** (public beta 2026-04-09, just before the window) and a Managed Agents **advisor** roster entry (2026-08-07). Both pair a cheaper executor model with a stronger advisor. Under the repository's reuse-first rule, any test of small-model triage plus large-model implementation should include this existing feature as a comparator before a custom router is built.
4. **Breaking-change cost.** The earlier report treats model releases as capability upgrades. Each 2026 model release in the ledger also came with API breaking changes in the release notes:
   - non-default `temperature` / `top_p` / `top_k` returning 400;
   - forced `tool_choice` returning 400;
   - restrictions on disabling thinking;
   - thinking blocks bound to a model or account;
   - tokenizer changes of roughly 1.0–1.35x (Sonnet 5) and about 30% (Fable 5 notes).

   Per-token price comparisons in §9 therefore understate migration and token-count effects.

### New events found (themes)

- **Security of the coding-agent boundary.** Twelve advisories were published in the window:
  - 9 for Claude Code: sandbox escapes via symlinks and git worktrees, a trust-dialog bypass, WebFetch exfiltration via a pre-approved domain, a TOCTOU file write, a plugin SHA-pin bypass, and others;
  - 3 for Claude Desktop/Cowork.

  For all nine Claude Code advisories, the patched npm release came before the advisory. The gap ranges from 9 days to about 5 months.
- **Autonomy defaults versus independent attack results.** Auto mode became the default for Pro, Max and Team on Aug 14 (029). An independent researcher then reported a 60–80% prompt-injection success rate on a small sample, against a 0.00% figure from a vendor-commissioned evaluation (034).
- **Harness transparency.**
  - An independent binary analysis reports hidden, gateway-dependent markers added to the system prompt (025).
  - An independent measurement reports roughly 33k vs 7k tokens of scaffolding against OpenCode (026).
  - AGENTS.md support (038) was found to depend on a remote feature flag (040). The vendor changelog changed this in 2.1.281 on the same day.
  - Text watermarking (030) drew criticism (031).
- **Reuse surface.**
  - Stainless acquisition: an SDK and MCP-server generator (011).
  - Python SDK 1.0 switched to the `httpx2` fork (033).
  - Files and Skills APIs became GA; the computer-use and browser-use toolsets became available (032).
  - `ant apply` with a lockfile (036).
  - An Apache-2.0 vulnerability-discovery harness repository (013).
  - An opt-in OSS Scanner. The vendor reports nearly 5,000 unverified reports sent to maintainers at their request (047).
- **Lifecycle.**
  - Model retirements in the window: Haiku 3, Sonnet 4/Opus 4 and Opus 4.1.
  - Sonnet 4.5 retirement is scheduled for Nov 30 (044).
  - Usage Policy update effective Nov 12 (048).

### M1–M7 notes for new events (issue #68 ordering)

The `study_construct` column uses the issue #68 ordering: M1 agent workflow, M2 code discovery, M3 verified reuse, M4 accepted quality, M5 review/maintenance, M6 rights/security, M7 human and lifecycle costs.

| Construct | What the new events show | What they cannot show |
|---|---|---|
| M1 agent workflow | Dynamic workflows (014), Claude Tag (019), auto-mode default (029), Managed Agents orchestration (010), AGENTS.md (038/040) | Adoption or effect on accepted work |
| M2 code discovery | Armature's study of which services agents pick (037; commercially interested source) | Whether those picks are good reuse |
| M3 verified reuse | SDK/MCP generation (011), GA Skills/Files APIs (032), Apache-2.0 harness (013), open-weights stance (028) | Any downstream reuse; no import was traced |
| M4 accepted quality | Postmortem shows that harness defaults (effort, context clearing, prompt wording) degraded quality without any model change (005); vendor usage research classifies "success" itself (018) | Independent acceptance rates |
| M5 review/maintenance | Breaking API changes with each model; SDK dependency fork (033); deprecations (044); OSS Scanner shifts triage work onto maintainers (047) | Measured migration or triage minutes |
| M6 rights/security | Twelve advisories, disclosure lag, prompt injection under auto mode (034), hidden client markers (025), export-control suspension (016), retention requirements (015, 035), watermark (030/031), usage policy (048) | Exploitation in the wild; legal assessment |
| M7 human/lifecycle cost | Cache-TTL and billing incidents (001, 007), usage-limit changes (008), scaffolding overhead (026), price changes (023, 039, 046) | Energy or emissions. Tokens are not kWh, and no energy figure is given. |

### Vendor-stated near-term plans (dated, not a roadmap)

- Auto mode as the default "across all" remaining surfaces, including the API and cloud platforms, "in the coming month" (029, Aug 7).
- Watermarking for future models; detection API in private preview (030, 035).
- Sonnet 4.5 retirement on 2026-11-30 (044).
- Usage Policy effective 2026-11-12 (048).
- Mythos access to expand "to the broader set" of Glasswing partners (024).

None of these is a binding commitment, and no 2027–2031 product plan was found.

**Researcher's conditional interpretation (E0 hypothesis).** If default autonomy keeps rising (029) while independent injection results stay high (034) and boundary advisories keep appearing, then maintainers using such agents will face growing review and isolation costs (M5/M6). Those costs could offset throughput gains.

- **Falsifiers:** independent replications showing near-zero injection success under default settings; a falling rate of boundary advisories per release over two or more quarters; measured review minutes per accepted task not rising.
- **Rival explanation:** the advisory count reflects better disclosure practice and bug-bounty volume, not worse security.

### Revised small experiment for this repository (proposed, not performed)

**Instruction-file portability and isolation check.** This repository already relies on `AGENTS.md`.

- **Tasks:** freeze 5 offline issues from this repo with independently written acceptance tests, including one with no viable solution.
- **Arms:** run each task in a disposable, network-restricted container under two conditions:
  - (a) `AGENTS.md` only, on Claude Code at version 2.1.281 or later with telemetry off;
  - (b) a one-line `CLAUDE.md` that points to `AGENTS.md`.
- **Comparator:** the same tasks done by hand by the maintainer, with time recorded.
- **Accepted-task unit:** the hidden acceptance tests pass, `python3 -m unittest discover -s tests` passes, and an independent human reviewer confirms that the repository rules were followed (no network capture, no backfilled timestamps).
- **Guardrails:** permission prompts on, not auto mode, because of 034. No secrets in the container. Pin and record the exact client version.
- **Spending:** subscription use only, with no paid API spend without approval.
- **Measurement:** human review and repair minutes per accepted task. Tokens and energy are not inferred.
- **Stop rule:** stop if either agent arm breaks a repository rule, or if review minutes exceed the manual-comparator minutes on 3 of the 5 tasks.

### Remaining limits

- No product was run, and no benchmark was replicated.
- The selection bias described under *Conflict of interest* is unresolved.
- Mutable vendor pages were not archived.
- Status-page incidents, Claude apps release notes and Agent SDK changelogs were not covered.
- Robots-blocked mainstream reporting is missing, which limits the independent counter-evidence available.

A PyPI JSON request made before its robots rule was checked is disclosed in the search log. Its data was deleted unused.
