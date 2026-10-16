# Docker — provisional six-month technology intelligence screen (037)

> **PROVISIONAL, AI-ASSISTED FIRST-PASS SCREEN (2026-10-16). NOT HUMAN-REVIEWED.** This report, its [event ledger](037-docker.events.csv) and its [search log](037-docker.search-log.md) are an **AI-assisted documentary source-lead screen**. No qualified human has reviewed them. Factual/link review, source-access/rights review and methods review are all **pending**. Nothing here is a verified chronology, a product test, an adoption measure or an empirical reuse result; [issue #104](https://github.com/MSKazemi/github-trending-1000-study/issues/104) was closed on 2026-10-16 by maintainer decision with this provisional status recorded; closure is not scientific validation, and the human review gates remain open. No evidence item has been minted for the [#56 evidence corpus](https://github.com/MSKazemi/github-trending-1000-study/issues/56); the independent news rows below are **candidates** for #56 only after human verification.

- **Company watchlist ID:** 037
- **Research issue:** [#104](https://github.com/MSKazemi/github-trending-1000-study/issues/104); linked corpus issue [#56](https://github.com/MSKazemi/github-trending-1000-study/issues/56).
- **Ownership and product boundaries (as of 2026-10-12):** see section 2. Docker, Inc. is the publisher of every first-party source used here. Corporate ownership was **not** verified at filing level.
- **Product URL and company newsroom:** [docker.com](https://www.docker.com/), [newsroom](https://www.docker.com/company/newsroom/), [blog](https://www.docker.com/blog/), [Docker Desktop release notes](https://docs.docker.com/desktop/release-notes/), [Docker Engine 29 release notes](https://docs.docker.com/engine/release-notes/29/), [Docker Agentic Platform release notes](https://docs.docker.com/agentic-platform/release-notes/), [Docker Sandboxes release notes](https://docs.docker.com/ai/sandboxes/release-notes/), [docker/compose releases](https://github.com/docker/compose/releases).
- **Analysis window:** 2026-04-12 to 2026-10-12 inclusive (UTC dates as displayed by sources).
- **Researcher / factual reviewer / review date:** AI-assisted first pass, sources accessed 2026-10-16 / human reviewer **pending** / review date **pending**.
- **Status:** screened (provisional). Not independently checked, not published as a finding.
- **Source coverage:** 25 dated ledger rows, at least one in each of the seven calendar segments. Search queries and exclusions are in the [search log](037-docker.search-log.md). Search-engine result counts, query-run UTC times and archived page snapshots were **not** captured. They are unknown, not zero. **Claim grading** uses the company-watch E0–E4 tiers from the [method](../../../docs/COMPANY_INTELLIGENCE_METHOD_2026_10.md), not the separate [2027 lesson protocol](../../../docs/EVIDENCE_TO_LESSON_PROTOCOL.md).

## 1. Search and inclusion audit

| Search run UTC | Site/engine | Full query and dates | Found | Screened | Included | Excluded/why | Coverage limitation |
|---|---|---|---:|---:|---:|---:|---|
| 2026-10-16 (time not captured) | Public web search, direct fetches of official pages, GitHub REST API | Exact queries are listed per segment in the [search log](037-docker.search-log.md) | unknown | unknown | 25 | see log | Not exhaustive. Some blog posts were seen only as titles in the blog index, and these were not counted. Page bodies were summarised by a fetch tool. Specific sentences for eight Desktop release items were re-fetched verbatim as a spot check. |

The ledger is a **purposive selection of material events**, not a census of Docker releases. Docker shipped weekly Desktop releases and frequent Engine and Compose patch releases in the window. Only items relevant to agent isolation, supply-chain security, credentials, reuse or contributor governance were kept. One CVE or launch that has several sources is recorded once with a shared `duplicate_event_group`. An independent outlet that only relays a vendor announcement is **not** counted as independent confirmation.

## 2. Verified company/product identity and baseline

- **Entity.** Every first-party source is published by **Docker, Inc.** The [2026-08-18 press release](https://www.docker.com/press-release/docker-strengthens-leadership-team-with-appointments-of-mat-velloso-as-cpo-and-vinh-le-as-cfo/) uses that name and a Palo Alto dateline. [The Register (2026-09-24)](https://www.theregister.com/ai-and-ml/2026/09/24/dockers-new-sandboxes-aim-to-contain-ai-agents-for-real/5298964) names Mark Cavage as president and COO.
- **Ownership: not verified.** No in-window source states whether Docker, Inc. is privately held or who its investors are. The press release says nothing about ownership. No 2026 acquisition, merger or funding round was found. A search result attributing a CEO name to the company could not be confirmed and was discarded (see the search log). Treat "privately held, independent" as **unverified**.
- **Product boundaries used here.**
  - Open-source **Docker Engine** (Moby).
  - **Docker Compose**, an open-source repository under the docker org.
  - **Docker Desktop**, a proprietary product with subscription terms.
  - **Docker Hub**, a hosted registry.
  - **Docker Sandboxes** (`sbx` CLI, microVM-based agent sandboxes) and **Docker Cloud Sandboxes**, the hosted version under the "Docker Agentic Platform".
  - **Gordon**, Docker's AI agent.
  - **Docker AI Governance**, a sales-gated policy control plane.
  - **Docker Model Runner**, a local model runtime.
  - **Docker Hardened Images (DHI)**.
  - **Docker VMM**, the Desktop virtualization backend.
  - The **Sandbox Kit Specification**, published at [github.com/docker/sandbox-kit-spec](https://github.com/docker/sandbox-kit-spec). The GitHub API reports `Apache-2.0` and a creation date of 2026-09-16.
  Do not infer that a Desktop or hosted feature carries the Engine's open-source license.
- **Pre-window baseline (context only, not counted).** The blog index shows these items before 2026-04-12:
  - 2026-03-31 "Docker Sandboxes: Run Agents in YOLO Mode, Safely"
  - 2026-03-13 NanoClaw sandbox integration
  - 2026-04-02 "Docker Offload now Generally Available"
  - 2026-04-07 Engine 29.4.0
  The Gordon beta also predates the window. Docker Hardened Images were made free under Apache-2.0 in December 2025, according to a secondary search summary that was not re-checked here.

## 3. Month-by-month discoveries (six calendar months + partial endpoints)

| Month | Announcements/changes (ledger IDs) | Primary URLs | Independent reporting | Notes or no-result limitations |
|---|---|---|---|---|
| 2026-04-12..30 | -001: Desktop 4.71.0 disables Model Runner by default and fixes CVE-2026-5843 (Apr 27) | [Desktop notes](https://docs.docker.com/desktop/release-notes/) | heise (May 27, row -006) | Title-only blog items not counted: Apr 14 DHI retrospective, Apr 16 "Why MicroVMs", Apr 23 Trivy/KICS supply-chain post. No press release in April. |
| 2026-05 | -002/-003: Engine 29.4.2 then 29.4.3 Copy Fail hardening (May 1, May 6). -004: AI Governance (May 12). -005: Gordon GA (May 19). -006: heise on CVE-2026-5843 (May 27). | [Engine 29 notes](https://docs.docker.com/engine/release-notes/29/), [Copy Fail blog](https://www.docker.com/blog/mitigating-cve-2026-31431-copy-fail-in-docker-engine/), [AI Governance](https://www.docker.com/blog/docker-ai-governance-unlock-agent-autonomy-safely/), [Gordon GA](https://www.docker.com/blog/meet-gordon-dockers-ai-agent-for-your-entire-container-workflow/) | [heise](https://heise.de/-11308355) | No independent coverage of AI Governance or Gordon GA was found. Only secondary blogs repackaged them. |
| 2026-06 | -007: Athena coalition (Jun 15). -008: DCT/Notary v1 retirement schedule (Jun 16). -009: Desktop 4.80 removes the experimental `docker sandbox` plugin (Jun 29). | [Athena](https://www.docker.com/blog/docker-joins-the-athena-coalition-a-cross-industry-collaboration-for-supply-chain-security/), [DCT retirement](https://www.docker.com/blog/docker-content-trust-retirement-and-migration-guidance/) | none found | Docker made no press release this month. |
| 2026-07 | -010: `cagent` removed in favour of `docker agent` (Jul 6). -011: Engine 29.7.0 fixes CVE-2026-17106 (Jul 30). -012: NVIDIA Open Secure AI Alliance (Jul 30). -013: Docker Hub OIDC for GitHub Actions (Jul 31). | [NVIDIA alliance](https://www.docker.com/blog/docker-joins-nvidia-open-secure-ai-alliance/), [OIDC](https://www.docker.com/blog/docker-oidc-connections-for-github-actions-available-for-docker-orgs/) | none found | Engine 29.6.2 (Jul 16, five BuildKit CVEs) was seen but not given a row, to keep the ledger bounded. |
| 2026-08 | -014: Gordon three-mode tool safety (Aug 10). -015: Docker VMM public beta (Aug 12). -016: CPO/CFO appointments (Aug 18). -017: Agentic Platform initial release of cloud sandboxes (Aug 26). | [VMM beta](https://www.docker.com/blog/docker-vmm-public-beta/), [leadership PR](https://www.docker.com/press-release/docker-strengthens-leadership-team-with-appointments-of-mat-velloso-as-cpo-and-vinh-le-as-cfo/), [Agentic Platform notes](https://docs.docker.com/agentic-platform/release-notes/) | none found | The Aug 3 "AI Governance audit logs to SIEM" post was seen only as a title and is not counted. |
| 2026-09 | -018/-020: Cloud Sandboxes launch and The Register coverage (Sep 24). -019: Sandbox Kit Spec and the CNCF intention (Sep 24). -021: Desktop 4.93 ECI enforcement fix (Sep 28). -022: Compose `AI_POLICY.md` (Sep 29). -023: Engine 29.8.2 CVEs (Sep 30). | [Press release](https://www.docker.com/press-release/cloud-sandboxes-extending-secure-ai-agent-isolation-beyond-the-laptop/), [Cloud Sandboxes blog](https://www.docker.com/blog/introducing-cloud-sandboxes-start-on-your-laptop-finish-in-the-cloud/), [Kit spec/CNCF blog](https://www.docker.com/blog/docker-sandbox-kit-spec-cncf/), [compose#13550](https://github.com/docker/compose/pull/13550) | [The Register](https://www.theregister.com/ai-and-ml/2026/09/24/dockers-new-sandboxes-aim-to-contain-ai-agents-for-real/5298964), [DevOps.com](https://devops.com/docker-introduces-open-sandbox-kit-spec-for-ai-agent-permissions/) (Sep 28) | Both outlets relay Docker's claims. Neither reports independent testing. |
| 2026-10-01..12 | -024: Desktop 4.94 fixes API keys written in clear to logs and diagnostics (Oct 5). -025: Docker Hub PAT-transfer advisory CVE-2026-105445 (Oct 12). | [Hub advisory](https://www.docker.com/blog/docker-hub-security-advisory-cve-2026-105445/) | [BleepingComputer](https://www.bleepingcomputer.com/news/security/docker-hub-flaw-let-attackers-impersonate-users-tamper-with-images/) (Oct 13, outside the window, used as a check URL only) | Seen but not counted: Compose v5.6.0 (Oct 2), sbx 0.47.0 (Oct 5), Engine 29.9.0 (Oct 8). Excluded as out of window: Oct 14 Harbor evals post, Engine 29.9.1. |

## 4. Dated event evidence and capabilities

The full rows are in [037-docker.events.csv](037-docker.events.csv), with 21 columns in the same schema as the Tailscale (099) ledger. The clusters below are what matter for the study.

| Event IDs | Published / underlying event | Claim or observed feature | Availability and limitations | Source (type) | Independent check | Grade |
|---|---|---|---|---|---|---|
| -017, -018, -020 | Aug 26 initial release; Sep 24 public launch | Hosted microVM agent sandboxes that share the CLI, policies and Kits with local `sbx`. Per-second billing at USD 0.07–1.12 per hour. 1 h default and 24 h maximum session. `sbx move` copies the filesystem, not a running process. | **Two different "release" dates** for one product line. The Aug 26 entry is labelled "Initial release" and the Sep 24 entry "Experimental public release". The press release says "available now". These are recorded as one duplicate group with status `preview`, not GA. | Release notes (E2), press release (E1/E2) | The Register relays a **vendor-staged** escape demo. No independent test. | E2 for existence, E1 for isolation claims |
| -019 | Sep 24 | The Sandbox Kit Spec v3 packages agent, tools and access rules as OCI images under Apache-2.0. Docker says it is "bringing the spec to CNCF". | The repo marks the spec experimental, with a final version targeted for Q4 2026. **CNCF acceptance is not documented.** DevOps.com reports Docker Sandboxes is the only conforming runtime. | Blog (E1), GitHub repo/API (E2 for license) | DevOps.com relays the claim | E2 license, E1 CNCF |
| -009, -010 | Jun 29, Jul 6 | The experimental `docker sandbox` plugin was removed in favour of `sbx`, and `cagent` was removed in favour of `docker agent`. | Interface churn: two agent-related CLIs were renamed or removed within about three months. | Desktop release notes (E2) | none | E2 |
| -005, -014 | May 19, Aug 10 | Gordon reached GA with per-action approval and session-scoped permissions. It later gained Strict/Balanced/Autonomous tool-safety modes. | Vendor-described controls. Autonomous and auto-approve modes reduce human checkpoints. Privacy claims are not verified. | Blog (E1) + release notes (E2) | none | E2 existence, E1 safety |
| -004 | May 12 | AI Governance: central policy over agent network, filesystem, credentials and MCP tools, with SIEM export. | Sales-gated. No GA/preview label. No public plan matrix. | Blog (E1) | none | E1 |
| -001, -006 | Apr 27, May 27 | Model Runner MLX backend container-to-host code execution (CVE-2026-5843). The fix ships in 4.71.0 and **Model Runner is now off by default**. | heise reports affected versions from 4.56.0 and no known attacks. Aggregators disagree on the CVSS score; NVD lists 8.8 (CNA v4.0), 8.2 (CNA v3.1) and 8.6 (NVD v3.1), all High. | Release notes (E2), heise (independent news) | heise is an independent publisher, but it did not reproduce the flaw | E2 |
| -002, -003 | May 1, May 6 | Copy Fail (CVE-2026-31431) container mitigation. 29.4.2's seccomp block **broke 32-bit binaries** and was replaced in 29.4.3 by AppArmor/SELinux rules. | **Negative result.** A security hardening shipped, regressed compatibility and was corrected within 5 days. Mitigation depends on host LSM enforcement. The real fix is a kernel patch. | Release notes + blog (E2) | none independent | E2 |
| -011, -021, -023, -024 | Jul 30 – Oct 5 | Engine and Desktop security fixes. These include **ECI not enforced** in three cases, one of them engine switching (Desktop 4.93) and **stored API keys written in clear to logs and diagnostics** (Desktop 4.94). | Vendor-disclosed defects. Affected-version ranges were not fully read. These are counterevidence to unqualified "secure by default" messaging. | Release notes (E2) | none | E2 |
| -025 | Advisory Oct 12; fix Sep 30; bug from 2024-08-26 | Docker Hub PATs were transferred to a named owner on account-to-organization conversion without rotation, so an attacker could impersonate that owner at the registry. Rated critical. Transferred PATs were deactivated Oct 8. | The **vendor** states it found no evidence of exploitation after reviewing about 304,000 pushes. Unused tokens leave no logs. | Advisory (E2) | BleepingComputer relays the advisory (outside the window) | E2 |
| -013 | Jul 31 | Docker Hub accepts GitHub Actions OIDC, giving short-lived per-run tokens in place of stored PATs/OATs. | Team/Business/DHI/DSOS organisations only, GitHub Actions only, at most five rulesets. | Blog (E2) | none | E2 |
| -008 | Jun 16 | DCT/Notary v1 retirement. Brownouts in July and August; **full shutdown on 2026-12-08, after the window**. Migration path: digest pinning plus Cosign or Notation. | Announced schedule only. The "<0.05% of Hub pulls" figure is a vendor number. | Blog (E1) | none | E1 |
| -022 | Sep 29 | docker/compose adopts `AI_POLICY.md`: AI use is disclosed in the PR description, a human is responsible for the output, and PRs stay scoped. AI-assisted PRs for previously unreported problems need an issue and maintainer approval first; requiring approved issues for every AI-assisted PR is left to each repo. The final commit adopts the centralized moby/.github policy. | This is policy text, not evidence of enforcement. The final wording was read from `AI_POLICY.md` on 2026-10-16 (spot-check). | GitHub PR + API (E2) | none | E2 |
| -007, -012, -015, -016 | Jun 15 – Aug 18 | Athena coalition, NVIDIA Open Secure AI Alliance, VMM public beta (GA targeted for end of October), CPO/CFO hires. | Memberships list no deliverables. The VMM performance claims have **no published numbers**. | Blog / press release (E1) | none | E1 |

No row reaches **E3 or E4**: none of the sources is an independent controlled test of Docker isolation, governance or agent quality.

## 5. What the company says it intends to do

| Public direction (quotes ≤25 words) | Link/date | Promised horizon | Status | Missing/contradictory context |
|---|---|---|---|---|
| "Today, we're bringing the spec to CNCF, under their neutral governance" | [Kit spec blog, 2026-09-24](https://www.docker.com/blog/docker-sandbox-kit-spec-cncf/) | None given. DevOps.com reports "later this fall". | Announced intention, not completed | No CNCF project status, maturity level or vote is documented. The CNCF CTO quote says only that the community "looks forward to working with Docker". |
| "Centralized governance is coming soon for enterprises through Docker AI Governance." | [Cloud Sandboxes blog, 2026-09-24](https://www.docker.com/blog/introducing-cloud-sandboxes-start-on-your-laptop-finish-in-the-cloud/) | "coming soon" | Tentative | AI Governance was already described as "available now" on 2026-05-12. Cloud-sandbox coverage is what is pending. |
| Docker VMM GA targeted for end of October 2026, becoming the default engine for new installs, with Linux support at GA | [VMM beta blog, 2026-08-12](https://www.docker.com/blog/docker-vmm-public-beta/) | End of October 2026 | Planned target | The blog itself calls this a target. No benchmark data has been published. |
| DCT and Notary v1 full shutdown on 2026-12-08 | [DCT blog, 2026-06-16](https://www.docker.com/blog/docker-content-trust-retirement-and-migration-guidance/) | 2026-12-08 | Planned (scheduled) | Execution falls after the window. |
| Gordon as one agent layer across Desktop, Scout, Offload, Sandboxes and Model Runner (paraphrase) | [Gordon GA blog, 2026-05-19](https://www.docker.com/blog/meet-gordon-dockers-ai-agent-for-your-entire-container-workflow/) | None | Uncommitted direction | No dated roadmap was given. |
| OIDC: "other CI providers will follow based on demand" (paraphrase) | [OIDC blog, 2026-07-31](https://www.docker.com/blog/docker-oidc-connections-for-github-actions-available-for-docker-orgs/) | Demand-dependent | Uncommitted | No providers or dates are named. |
| CPO: Docker "can unlock the productivity boost promise of AI agents without giving away control or compromising on security" | [Press release, 2026-08-18](https://www.docker.com/press-release/docker-strengthens-leadership-team-with-appointments-of-mat-velloso-as-cpo-and-vinh-le-as-cfo/) | None | Positioning statement | This is marketing language, not a product commitment. |

## 6. Independent interpretation: direction and alternative scenarios (2027–2031, conditional)

These are the **researcher's hypotheses**. They are not Docker strategy and not forecasts made by Docker.

| Hypothesis for 2027–2031 | Supporting observations | Rival explanations | Disconfirming signals | Confidence/unknowns |
|---|---|---|---|---|
| H1. Packaging an agent's tools **and** its permissions as an OCI artifact (Kits) could become a portable, reviewable unit for agent tasks, as Dockerfiles did for builds. | -019 (Apache-2.0 spec, CNCF intention); -017/-018 (shared local/cloud policy) | Vendor-led specs often stay single-implementation. Other projects may standardise first, for example devcontainers or competing sandbox runtimes. | No CNCF acceptance by end-2027. Docker Sandboxes remains the only conforming runtime. Spec versions break compatibility again. | Low. Only one runtime conforms today, and the spec is experimental. |
| H2. Agent isolation will move from containers to microVM sandboxes as the default for unattended coding agents. | -009, -017, -018, and the vendor-staged Docker-socket demo (-020) | Container hardening (ECI, rootless, LSM profiles) may be judged sufficient. Teams may also use cloud-native ephemeral runners instead. | Independent escape tests show no material difference for typical agent tasks, or the cost and latency overhead deters use. | Low–medium. All isolation evidence here is vendor-produced. |
| H3. Registry credential practice will shift from long-lived tokens to workload identity. | -013 (OIDC), -025 (PAT-transfer flaw), -024 (keys in logs) | Plan gating (-013 excludes Personal/Pro) may keep small maintainers on PATs. | OIDC remains GitHub-Actions-only and paid-tier-only through 2027. | Medium for direction, unknown for uptake. |
| H4. Large upstream OSS projects will codify AI-contribution rules (disclose, human-responsible, scoped). | -022 adopts a centralized moby/.github policy | One-off maintainer preference, or policy without enforcement. | Policies are rolled back, or have no measurable effect on review time or rejected-PR rates. | Medium for policy spread, unknown for effect. |
| H5. Rapid agent-feature churn will impose real migration cost on downstream users. | -009, -010 (two CLI removals or renames in about 3 months); -002 to -003 (a 5-day reversal of a security hardening) | Normal early-product iteration that will stabilise. | Few breaking changes to `sbx` or `docker agent` after 2027. | Medium. |

## 7. Implications for the GitHub 1000 study

| M1–M7 construct | Possible observable effect | Study design to test it | Negative/null explanation | Measurement boundary |
|---|---|---|---|---|
| **M1** AI coding-agent change | More agent runs happen inside disposable sandboxes rather than on the developer's host | Opt-in, consented logs of where agent sessions execute, with sandbox vs host as the condition | Sandboxing changes where code runs, not how it is written | No collection of real agent traces without consent (see the task-cost-ledger rules in AGENTS.md) |
| **M2** accepted task quality | Isolation might reduce destructive side effects without lowering accepted-task rates | A frozen task set with independent hidden acceptance tests, sandboxed vs unsandboxed, counting **all** attempts | Isolation overhead or missing tools inside the sandbox could lower success | Only tasks that need no live GitHub capture, which remains disabled |
| **M3** discoverability | None directly | Not tested | — | Stars and press coverage (-020) are not adoption |
| **M4** verified third-party reuse | Kits or Compose files reused by downstream repos | Trace consented downstream repositories that pin a published Kit or image digest and run it successfully | Downloads and pulls do not show working reuse | Docker Hub pull counts are excluded as a reuse measure |
| **M5** reuse-first, security and rights | Reusing pinned official images, digest pinning and Cosign signing instead of bespoke scripts | Compare a reused pinned base image against a custom environment script on the same task | Base-image CVE churn (-011, -023) could add maintenance | Desktop is proprietary with subscription terms. Engine, Compose and Kit spec rights need per-component checks. |
| **M6** lifecycle human and energy cost | Setup minutes, image update and review minutes, CI minutes | Instrument human minutes and CI wall-time. Report energy only if metered. | Container builds can add CI time and storage | **No token-to-kWh or CO2e conversion.** No energy numbers are reported here. |
| **M7** actionable interventions | A one-command reproducible test environment for newcomers | Section 8 | May show no improvement over a plain venv | Synthetic or authorized opt-in tasks only |

## 8. One practical, falsifiable change for the maintainer's own repositories

**Repository/component:** [github-trending-1000-study](https://github.com/MSKazemi/github-trending-1000-study). The target is the offline test suite and the documented synthetic CLI smoke tests only. Live Trending `capture` stays **disabled**, and nothing in this experiment touches GitHub network access.

**Candidate practice (not yet validated):** a reproducible, digest-pinned container entry point for the offline gate, reusing an official Python base image with no new tooling code. Compare it with the existing documented virtual-environment path.

**Treatment/control and frozen comparable task:**
- **Control A:** fresh clone, then the existing documented Python setup, then `python -m unittest discover -s tests -v` and the three smoke tests named in AGENTS.md (`value_gate`, `reuse_gate`, `pilot-preflight`).
- **Treatment B:** the same clone and the same commands, run inside one `docker run` against an official `python` image **pinned by digest**, with the network disabled at run time (`--network none`).
- Both arms use the same commit SHA and the same Python minor version.
- **Accepted-task unit:** one fresh-environment attempt that completes all four commands with exit code 0 and the expected `not_ready` preflight verdict. A human who did not write the setup confirms the outcome.
- **Denominator:** every attempt, including setup failures and abandoned runs. Freeze 10 attempts per arm on two host operating systems before starting.

**Success and guardrails:**
- **Primary measure:** accepted attempts divided by all attempts.
- **Secondary measures:** human minutes to first green run, number of undocumented steps, and image or base CVE count from an existing scanner if one is already available.
- **Guardrails:** no secrets or tokens in the image or the build context. The image is pinned by digest, never by `latest`. No Docker Hub login is needed. Docker Desktop licensing terms must be confirmed for the host, or Engine used on Linux. If any CI job is added, it must not change the existing Python 3.10/3.12/3.14 jobs.

**Measured human work:** setup minutes, the reviewer's acceptance minutes, and monthly maintenance minutes for digest bumps, logged in the [task cost ledger](../../../docs/TASK_COST_LEDGER_2026-10-12.md) format with explicit missingness. **No carbon or energy estimate** unless CI runtime energy is actually metered.

**Stop/reversal rule:** keep the plain venv path and drop B if any of the following happens:
- B's accepted rate is not higher than A's.
- B needs more than 15 minutes of extra maintenance per month.
- B introduces a secret, network dependency or licence ambiguity.
- The digest-pinned image accrues an unpatched critical CVE for more than 14 days.

A null result is a valid outcome and must be recorded. **No trial has been executed and no effect has been estimated.**

## 9. Findings, uncertainties and review outcome

- **Observed/shipped (documentary E2, vendor-reported):**
  - Gordon GA (-005).
  - OIDC for GitHub Actions (-013).
  - Model Runner off by default (-001).
  - Copy Fail mitigations (-003).
  - `sbx` replacing the `docker sandbox` plugin (-009) and `docker agent` replacing `cagent` (-010).
  - Compose AI policy (-022).
  - Multiple Engine and Desktop security fixes (-011, -021, -023, -024).
  - The Hub PAT advisory and remediation (-025).
- **Preview or announced only:**
  - Cloud Sandboxes (-017/-018), labelled experimental public release.
  - Docker VMM public beta (-015).
  - The Kit spec's CNCF transfer (-019).
  - DCT shutdown on 2026-12-08 (-008).
  - Athena and NVIDIA alliance memberships (-007, -012).
  - AI Governance enterprise coverage of cloud sandboxes.
- **Conjectures and unknowns:**
  - Corporate ownership at filing level.
  - Exact Cloud Sandboxes availability scope between Aug 26 and Sep 24.
  - Whether any isolation claim survives independent testing.
  - Real adoption of any feature.
  - Affected-version ranges for -021 and -024.
- **Important contradictory or null evidence:**
  - Docker's own release notes contain several defects that cut against unqualified "secure by default" messaging: a security hardening that broke compatibility and was reversed within five days (-002 then -003), ECI not enforced in three cases (-021), API keys written in clear to logs (-024), and a registry token flaw open for about two years (-025).
  - The Register and DevOps.com relay vendor claims without independent tests.
  - No independent coverage was found for Gordon GA or AI Governance.
- **Reviewer links and audit date:** human factual/link review **pending**. Source-access/rights review **pending**. Methods review **pending**. Sources were accessed 2026-10-16 by an AI-assisted first pass. Public pages may change, and no archived snapshots or hashes were taken.

## Independent source spot-check (2026-10-16)

A second AI-assisted pass re-read all 25 ledger rows plus the entity claim against the cited sources on 2026-10-16. Figures, dates and version-to-item mappings were matched against raw page text (`curl` plus text grep, with each Desktop and Engine release-note section split by version heading). CVE IDs and scores were checked against the NVD CVE API and the GitHub advisory APIs, and repository facts against the GitHub REST API. No page was archived or hashed.

| Row(s) checked | Outcome | Note |
|---|---|---|
| Entity (section 2) | confirmed | Press release: "PALO ALTO, Calif. – August 18, 2026 – Docker, Inc."; The Register names "Docker president and COO Mark Cavage" at WeAreDevelopers. Ownership is still unverified |
| 001, 006 | confirmed (note added) | "Model Runner is now disabled by default" and the CVE-2026-5843 fix are in Desktop 4.71.0 (2026-04-27). heise, May 27, 2026: affected "from version 4.56.0", fixed in 4.71.0, no reported attacks. NVD scores (8.8 / 8.2 / 8.6, all High) are now recorded |
| 002, 003 | confirmed | Engine 29.4.2 (2026-05-01) blocked AF_ALG and socketcall; 29.4.3 (2026-05-06) replaced the deny that "broke 32-bit programs" with AppArmor/SELinux rules. Copy Fail blog posted May 27, 2026 cites moby/moby#52506. The Desktop 4.72.0 (2026-05-06) kernel backport is confirmed. NVD: CVE-2026-31431 is a Linux kernel CVE, 7.8 High |
| 004 | confirmed | Posted May 12, 2026: "Docker AI Governance is available now"; SIEM export |
| 005 | confirmed | Posted May 19, 2026: "Now generally available"; Desktop 4.74+; "Start free"; optional auto-approve |
| 007, 012 | confirmed | Athena posted Jun 15, 2026 ("founding participant"; no member list); NVIDIA alliance posted Jul 30, 2026 |
| 008 | confirmed | Posted Jun 16, 2026: write brownouts Jul 14 and 15, read brownouts Aug 10 and 12, full shutdown Dec 8, 2026; "fewer than 0.05%" of Hub pulls; Kyverno and Ratify named |
| 009, 010, 014 | confirmed | Desktop 4.80.0 (2026-06-29) removed the experimental `docker sandbox` plugin; 4.81.0 (2026-07-06) removed `cagent`; 4.86.0 (2026-08-10) added Strict/Balanced/Autonomous and fixed CVE-2026-17106 |
| 011 | confirmed | Engine 29.7.0 (2026-07-30) updates go-archive to v0.3.0 for CVE-2026-17106 / GHSA-hfg8-hc9c-6c3h. NVD: CNA CVSS 4.0 7.1 High |
| 013 | confirmed | Posted Jul 31, 2026: Team, Business, DHI and DSOS organisations; `docker/login-action` v4.5.0+; up to five rulesets; immutable-ID subject claims for repos created after July 15, 2026 |
| 015 | confirmed | Posted Aug 12, 2026: Desktop v4.86; GA "targeted for the end of October 2026" as the default engine; Linux at GA |
| 016 | confirmed | See entity row |
| 017, 018, 020 | confirmed | Agentic Platform notes: Aug 26, 2026 "initial release" (1 to 24 h timer, billed by the second, deny over allow); Sep 24, 2026 "experimental public release". Cloud Sandboxes blog posted Sep 24, 2026: $0.07 to $1.12 per hour, one hour default, up to 24 hours. Register demo with the mounted Docker socket confirmed |
| 019 | confirmed; DevOps.com part unverifiable | Kit spec blog posted Sep 24, 2026: "Today, we're bringing the spec to CNCF, under their neutral governance"; Apache 2.0. GitHub API: repo created 2026-09-16, Apache-2.0. README: "experimental", final version "targeted for Q4 2026". The CNCF CTO's "looks forward to working with Docker" wording is in the press release (row 018); the blog version differs. DevOps.com returned 403, so "only conforming runtime" and "later this fall" were not re-checked |
| 021 | corrected | Desktop 4.93.0 (2026-09-28) lists **three** ECI non-enforcement fixes (an engine left running while another was in use; an administrator policy arriving after engine start; sign-in completing after engine start), not one. The CSV claim and the report text are corrected |
| 022 | corrected | PR #13550 merged 2026-09-29T13:46:13Z; Compose v5.6.0 published 2026-10-02. The final `AI_POLICY.md` was read on 2026-10-16. It does **not** require approved issues for all PRs: that is optional per repo. It does require an issue and maintainer approval first for AI-assisted PRs on previously unreported problems, and it says to skip AI attribution trailers. The claim, the limitation and the report text are corrected |
| 023 | corrected | Engine 29.8.2 (2026-09-30) lists all the stated CVEs. CVE-2026-53493 is a **containerd** advisory (GHSA-pg57-6jwg-q645, NVD CNA GitHub, CVSS 4.0 6.9 Medium) that Docker lists among Engine fixes. CVE-2026-92543 (moby GHSA-7cfq-22r6-qp73, CNA 7.6 High), CVE-2026-92542 (moby GHSA-6m9p-4h64-m6vh, 6.9 Medium), CVE-2026-93315 (5.8) and CVE-2026-93326 (6.0) all exist in NVD with matching descriptions |
| 024 | confirmed | Desktop 4.94.0 (2026-10-05): "Fixed stored API keys being written in clear to Docker Desktop logs and included in diagnostics bundles"; local logging driver default |
| 025 | confirmed (note added) | Advisory posted Oct 12, 2026: exposure from August 26, 2024 20:33 UTC to the fix on September 30, 2026; about 304,000 pushes examined; transferred PATs deactivated October 8; rated critical. NVD (published 2026-10-13, Awaiting Analysis): Docker CNA CVSS 4.0 **9.4 Critical**. This resolves the "not verified" item in the search log |

**Outcome counts:** 26 checks (25 rows plus the entity claim): 23 confirmed (two with added notes; row 019's DevOps.com sub-claims unverifiable because of a 403), 3 corrected, 0 wrong. All nine Engine/Desktop/Hub CVE IDs checked exist in NVD with matching descriptions. No fabricated URL, figure or CVE ID and no contamination from another company was found. Event IDs are unchanged.

*This is an AI-assisted source spot-check. It is not a qualified human factual, rights or methods review, and those reviews remain pending.*
