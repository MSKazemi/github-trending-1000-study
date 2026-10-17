# Candidate package provenance instrument v1.0 (issue #22)

**2026-10-12: offline self-reported evidence consistency, NOT security approval.**

Run `python -m trending_study.package_trust --input examples/package_trust.synthetic.json`.
Each immutable candidate record requires an exact package URL (`pkg:` purl), a version, ecosystem, official registry evidence URL, capture UTC, a source commit SHA and release URL, plus separate `identity`, `license`, `security`, `provenance`, `maintenance` and `functional` status (pass/fail/unknown). Each pass must include reviewer-supplied evidence URL in `evidence`; status is **never independently verified** by this CLI.

The only output decision is `review_required`, `block_candidate`, or `ready_for_independent_review`, **not** auto-install or certification. If a gate fails, block. If any gate unknown or evidence missing, review; all self-reported pass marks only permit independent verification. Typosquats, fake package names, stale advisories, inherited licenses, confusing source vs released artifact and undocumented maintenance each require manual controls. No arbitrary script or dependency is executed and no external network is accessed.

Next: use authorized official registry reads, release-era exact-version OSV query, reviewed SPDX source/artifact compatibility, verified signatures/SLSA evidence and independent test acceptance. Preserve exact returned response timestamp and error type. A registry listing and no known OSV advisory are necessary evidence, **not** a safety warranty. The package candidate's release must predate the frozen user-task date to be considered historical reusable software.

**Practical 2027 lesson:** For every agent-recommended dependency, verify exact identity/version, legal use and supply-chain provenance before copying or installing. Where trust cannot be established, choose a smaller bounded implementation, existing reviewed dependency or no-build alternative. This stage advances #22 but cannot close it without authenticated independent gold review.
