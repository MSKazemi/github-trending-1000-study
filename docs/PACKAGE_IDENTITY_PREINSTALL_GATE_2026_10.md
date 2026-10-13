# Version-specific pre-install security and license screen — issue #22

**Status:** offline **self-declared evidence validator**, 2026-10-12; not a package scanner, legal opinion, signature verifier or installation utility. Partially addresses [#22](https://github.com/MSKazemi/github-trending-1000-study/issues/22).

```bash
python -m trending_study.package_review --input REVIEW.json
python -m unittest tests.test_package_review -v
```

The JSON includes `candidate`: `ecosystem`, `package_name`, exact `version`, `registry_url` (HTTPS without embedded secrets), `artifact_sha256` (64-hex when verified or explicit `null` when not yet known), `first_available_at_utc`, `spdx_expression` (null means unknown and cannot be a license pass); `task_frozen_at_utc`; and the exact six `checks` keys: `registry_identity`, `license_compatibility`, `known_advisories`, `release_provenance`, `functional_fit`, `maintenance_suitability`. Each check declares `status: pass|fail|unknown` and a pass has an HTTPS `evidence_url`.

**Decision rules:** any supplied failed gate ⇒ `reject`; unknown ⇒ `defer`; all pass ⇒ `review_ready` **not install approval**. A first-availability timestamp after the frozen user task is rejected to avoid retrospective leakage. All reported checks are self-declared; HTTPS format does **not** authenticate the registry, digest, reviewer, file content, OSV feed, source or release history.

## Required actual security evidence (not implemented by this tool)

1. Resolve exact official registry namespace and publisher; preserve version+artifact digest and issuance date through an authorized source API. Confirm package and source identities separately, including renames and withdrawn versions.
2. Inspect exact distributed artifact vs source commit, signature/attestation provenance where available, SPDX expression against downstream obligations, all licenses and transitive dependency constraints.
3. Query appropriately timed OSV/vendor disclosures; a negative scan is not proof of absence of vulnerabilities. Record advisory date relative to task and evaluation dates, as well as maintenance signals, compatibility, permissions and missingness.
4. Validate functional fit with independently frozen tests in a secret-free isolated environment **only after explicit approval**. Record all failed package searches and avoid typosquat probes that install candidates.
5. Have a qualified independent reviewer verify URLs/digests/owner, license and threat model before reliance. Security tools and OpenSSF scores are evidence layers, not approvals.

**Practical lesson:** for every suggested reusable library in your repositories, insist on exact registry version and verified license/provenance before copying or installing it. Neither GitHub stars nor a 'green' scanner proves safe reuse.

See [supply-chain protocol](SUPPLY_CHAIN_PROVENANCE_2027.md), [reuse-first guide](REUSE_FIRST_PLAYBOOK.md) and [independent gold-set judging](REUSE_GOLD_STANDARD_2027.md).

## 2026-10-13 preinstall fail-closed improvements

The candidate check now rejects moving aliases (`latest`, `main`, `HEAD`, ranges), verifies **PyPI** official `pypi.org` host and exact package name/version in the declared registry URL (other ecosystems still require their own official-identity check), and treats SPDX `NONE`/`NOASSERTION` as **non-granting** for a license pass. It rejects evidence URLs with credentials/fragments, and future frozen task timestamps. A package with first-availability after the historical task cutoff is **rejected**, even if its publication date is future-dated. SHA-256 values and asserted sources remain **unverified strings** until independently fetched/compared.

**Additional fail-closed engineering review (2026-10-13):** Even if an alleged package release is after the frozen task baseline, **all six submitted checks and evidence URLs must still be structurally valid**; temporal rejection does not bypass schema validation or conceal unknowns. The rejection output retains `temporal_availability` and any independently unknown/failing gates. The validator binds only declared **PyPI** package names and versions to the official registry URL: non-PyPI ecosystems are automatically `defer` with `official_registry_identity_binding` in `unknown_checks`, regardless of self-reported six-pass assertions. This is intentional; official binding for npm/Maven/NuGet/etc. requires ecosystem-specific implementations and independent tests. A malformed PyPI name containing path/query controls is rejected. No review-ready result is installation permission; `automatic_install_approved` is always false.

**Checks still required for any real deployment:** resolve exact package URL (purl) and artifact content hash from an authorized registry; verify registry/maintainer identity, signs of typosquatting, version-specific OSV advisories and update timestamps, full SPDX license expression and obligations, provenance/SLSA if available, dependency graph/SBOM, permissioned sandboxed functionality and support lifecycle. Query OSV with exact package/version and process complete pagination; "no returned advisory" is **not** a security guarantee. Never auto-install on any automatic `review_ready` report.

**Technical references:** [SPDX normative license-expression grammar](https://spdx.github.io/spdx-spec/v3.0.1/annexes/spdx-license-expressions/); [OSV version-specific query API](https://github.com/google/osv.dev/blob/master/docs/api/post-v1-query.md); [Package URL specification](https://github.com/package-url/purl-spec). These are check sources, not evidence that any candidate in this study passed those checks.

**Practical lesson:** before an agent adds a dependency to your repo, pin official package identity and version, audit license/security/maintenance, test in an isolated environment, and retain the *rejected candidate* as evidence for future reuse searches.


## 2026-10-13 unknown-artifact follow-up

The pre-install screen now accepts **explicit `artifact_sha256: null`** as unresolved evidence, not as a zero hash, an automatically excluded package, or a verified artifact. It always includes `artifact_sha256` among `unknown_checks` and returns `defer` unless another declared gate fails (then `reject`). Omitting the field entirely remains a malformed-input error. Even six self-reported passing gates **cannot** produce `review_ready` without an exact declared artifact digest; a declared hex digest is not independently authenticated by this CLI. Two negative regressions cover the missing/unknown states. This preserves viable *candidate discovery* while refusing unverified *installation*.

## 2026-10-13 quality regression: exact-release lexical validation

The offline validator now accepts pinned **release-like** strings with ordinary letters, such as `1.0.post1` and `1.2.0-nightly.1`, while rejecting whitespace, tabs/newlines, range or wildcard characters, paths and moving aliases. Earlier character-class escaping accidentally treated letters `t` and `n` as forbidden; two regression tests detect both the false rejection and invalid selectors. This is **syntactic filtering only**: arbitrary release-like text can still describe a nonexistent or unpublished artifact. No release is trusted or installed without independently checking the exact official registry and artifact bytes. For non-PyPI ecosystems, the parser currently checks HTTPS syntax but **does not verify the official registry host**; these inputs require independent identity review.

**Integration warning:** [PR #186](https://github.com/MSKazemi/github-trending-1000-study/pull/186) implements a separate `package_trust` API for the same issue; do not present the two outputs as independent security confirmations or merge both as unrelated security decisions. Align a single versioned public interface and retain useful test cases/docs before removing either implementation. Changes in this branch remain a proposal subject to actual security and maintainer review.
