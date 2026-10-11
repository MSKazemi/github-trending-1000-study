# Trustworthy reuse: identity, provenance, licensing and supply-chain safety

**Status:** protocol design, not a product security certification. A star-rich/trending package is not automatically safe, licensed or maintained. This document describes evidence to collect **without ever auto-installing arbitrary search hits**.

## Specific hazards
1. AI coding agents can recommend **nonexistent packages** (package hallucination), creating an opportunity for adversaries to publish the missing name. Verify package exists *in an official registry*, owner and release history before accepting a recommendation.
2. A real package may be typosquatted, abandoned, hijacked, malicious or a lookalike of the expected author. A single registry listing, Scorecard badge or GitHub URL does not remove this risk.
3. Code may be copied or forked without licensing rights or notices. A public repository without explicit license is **not** automatically freely reusable. Check exact repository and package artifact terms, license expression and transitive obligations.
4. Source repository differs from packaged artifact (build process, CI credentials, compromised releases). Provenance and reproducible build information may be missing.
5. Long chains of transitive dependencies create operational and security cost. One vulnerability scan at integration time does not predict 90/180-day security exposure.
6. Maintainers need adequate support capacity and a responsible disclosure process; lack of a security policy is a risk signal, not proof of exploitability.

## Workflow and source authority
| Gate | Required evidence | Suggested standards/services | Limitation |
|---|---|---|---|
| Identity | exact package registry namespace, owner/publisher, source URL, version/digest, release time | official package registry, [Package URL/purl](https://github.com/package-url/purl-spec) | account or metadata may be compromised |
| License | source and artifact license, SPDX expression, code notices, transitive dependencies | [SPDX License List](https://spdx.org/licenses/) | automated detection misses conflicting headers and obligations |
| Source provenance | commit, tag/release and build trace | [SLSA v1.2](https://slsa.dev/spec/v1.2/), [provenance](https://slsa.dev/spec/v1.2/provenance) | provenance records origin/process, not malware-free behavior |
| Known vulnerability | exact version, advisory ID, patch availability, severity, date | [OSV API](https://google.github.io/osv.dev/api/) | absence of advisory != absence of flaw |
| Project posture | verified repo policy, branch protections, releases, reviews, CI and disclosure practice | [OpenSSF Scorecard](https://openssf.org/projects/scorecard/), [OSPS Baseline](https://baseline.openssf.org/) | scores are heuristic practice signals, not functionality/security guarantees |
| Dependency composition | SBOM or lockfile with resolved versions and transitive packages | [SPDX](https://spdx.dev/), CycloneDX where applicable | SBOM may omit dynamic/runtime dependencies |
| Execution | isolation, least privilege, fixed resources, repeatable tests | local sandbox/container with no sensitive network or credentials | sandbox limits and supply-chain execution risks still require human review |
| Maintenance | current release/support policy, upgrade path, known breakage | changelog, changelog test, maintainer docs | quiet mature repos can be perfectly viable |
| Reuse reciprocity | provenance, attribution, upstream fixes or sponsorship where possible | CONTRIBUTING, license notices | economic/ethical feasibility varies by project |

## Secure trial acceptance
- Never execute a candidate merely because the agent wrote a command. Human approves exact commands/packages for high-risk and unknown provenance. Use time-limited, network-restricted sandboxes with no secrets and reproducible logs where possible.
- Do not browse to arbitrary code-host URLs and execute setup scripts blindly.
- Label each assessment with UTC timestamp, exact version/source, verifier identity/role, tests, signed or authentic provenance where applicable, unresolved unknowns and failure causes.
- Apply project-type and risk-specific gate; low-risk educational artifact may not need production-grade supply-chain proof, while production systems do.
- When no candidate passes, recommend **a bounded new implementation or scope reduction** rather than installing unsafe code to maximize 'reuse rate'.

## Research measurement
**Safety-gated precision@5:** among top-K candidates fully adjudicated, count candidates that are task-suitable AND license-compatible AND meet the predeclared safety threshold; report unresolved count separately. Other metrics: package nonexistence rate per query (using official registry), false positive trust recommendations, patch/maintenance burden 90/180 days, build-provenance coverage and licensed-use compliance. Measure by language/ecosystem and tool version, with double review.

## Source literature / standards
- [USENIX: We Have a Package for You! — analysis of package hallucinations](https://www.usenix.org/publications/loginonline/we-have-package-you-comprehensive-analysis-package-hallucinations-code)
- [SLSA 1.2 supply-chain spec](https://slsa.dev/spec/v1.2/)
- [OpenSSF Scorecard](https://openssf.org/projects/scorecard/)
- [OpenSSF Project Security Baseline](https://baseline.openssf.org/)
- [OSV vulnerability API](https://google.github.io/osv.dev/api/)
- [SPDX License List](https://spdx.org/licenses/)

Do not use a single score as an independent 'safe to use' certification.
