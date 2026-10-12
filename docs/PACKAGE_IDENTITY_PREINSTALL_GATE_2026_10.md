# Version-specific pre-install security and license screen — issue #22

**Status:** offline **self-declared evidence validator**, 2026-10-12; not a package scanner, legal opinion, signature verifier or installation utility. Partially addresses [#22](https://github.com/MSKazemi/github-trending-1000-study/issues/22).

```bash
python -m trending_study.package_review --input REVIEW.json
python -m unittest tests.test_package_review -v
```

The JSON includes `candidate`: `ecosystem`, `package_name`, exact `version`, `registry_url` (HTTPS without embedded secrets), `artifact_sha256`, `first_available_at_utc`, `spdx_expression` (null means unknown and cannot be a license pass); `task_frozen_at_utc`; and the exact six `checks` keys: `registry_identity`, `license_compatibility`, `known_advisories`, `release_provenance`, `functional_fit`, `maintenance_suitability`. Each check declares `status: pass|fail|unknown` and a pass has an HTTPS `evidence_url`.

**Decision rules:** any supplied failed gate ⇒ `reject`; unknown ⇒ `defer`; all pass ⇒ `review_ready` **not install approval**. A first-availability timestamp after the frozen user task is rejected to avoid retrospective leakage. All reported checks are self-declared; HTTPS format does **not** authenticate the registry, digest, reviewer, file content, OSV feed, source or release history.

## Required actual security evidence (not implemented by this tool)

1. Resolve exact official registry namespace and publisher; preserve version+artifact digest and issuance date through an authorized source API. Confirm package and source identities separately, including renames and withdrawn versions.
2. Inspect exact distributed artifact vs source commit, signature/attestation provenance where available, SPDX expression against downstream obligations, all licenses and transitive dependency constraints.
3. Query appropriately timed OSV/vendor disclosures; a negative scan is not proof of absence of vulnerabilities. Record advisory date relative to task and evaluation dates, as well as maintenance signals, compatibility, permissions and missingness.
4. Validate functional fit with independently frozen tests in a secret-free isolated environment **only after explicit approval**. Record all failed package searches and avoid typosquat probes that install candidates.
5. Have a qualified independent reviewer verify URLs/digests/owner, license and threat model before reliance. Security tools and OpenSSF scores are evidence layers, not approvals.

**Practical lesson:** for every suggested reusable library in your repositories, insist on exact registry version and verified license/provenance before copying or installing it. Neither GitHub stars nor a 'green' scanner proves safe reuse.

See [supply-chain protocol](SUPPLY_CHAIN_PROVENANCE_2027.md), [reuse-first guide](REUSE_FIRST_PLAYBOOK.md) and [independent gold-set judging](REUSE_GOLD_STANDARD_2027.md).
