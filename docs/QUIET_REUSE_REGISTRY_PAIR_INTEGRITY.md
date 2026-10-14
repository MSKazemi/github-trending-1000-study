# Offline registry pair-packet integrity

Issue #15's registry pilot is an offline, source-bounded package-name lead
frame. It neither installs packages nor validates a human research cohort.

The `audit-pairs` command validates the complete packet's schema before
counting submitted reviewer decisions. A valid content fingerprint is necessary
but does not replace schema validation. `nominated_pair_count` must equal the
number of pair records; pair IDs, task IDs and task/component combinations
must be unique, and every nominated task must appear in the packet's task frame.
Malformed identities, unsupported schema versions, inconsistent uncertainty
flags and undeclared fields are rejected. One submitted decision cannot be
multiplied by repeating a pair record.

All three subcommands use the existing `data_integrity.decode_research_json`
reader. Duplicate object keys, nonstandard or non-finite numeric values,
overflow, underflow and invalid UTF-8 fail before publishing a result.
Outputs retain the existing write-once publication contract.

Run the offline regression checks with:

```bash
python -m unittest discover -s tests -p test_quiet_reuse_registry.py -v
python -m unittest discover -s tests -v
```

Every new reviewer, task and package fixture is synthetic. Reviewer identity,
independence, source rights, source authenticity, task correctness, release
availability, license and security still require actual external verification.
Neither a content fingerprint nor a successful structural audit establishes
scientific acceptance. The output flags for authenticated human reviewers and
issue #15 scientific acceptance remain false.

An additional unresolved boundary exists in `prepare-pairs`: the submitted
selection is trusted for its package-membership list. Source and plan hashes
do not bind the selected package records themselves. Preserve the original
selection alongside its source manifest/plan and arrange a separately reviewed
binding check before using nominations as verified in-frame research records.
The present correction addresses packet counting and JSON ambiguity only;
it does not change the sampling protocol or authenticate the real registry
listing.

Reuse review: the existing standard-library-only public strict JSON helper and
write-once publisher satisfy this task without another dependency or JSON
parser. The MIT-licensed repository's existing validators and tests were
inspected. Python's official JSON documentation describes duplicate-key and
nonstandard-number defaults: <https://docs.python.org/3/library/json.html>.
No public-package installation or external code execution was needed.
