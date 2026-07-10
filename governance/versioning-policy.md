# Versioning Policy

Hydra Core uses semantic-style versions for the public governance contract. It remains pre-v1, so compatibility expectations are explicit and every governance-bearing change requires migration notes.

Release maturity and public/private scope are defined in [Release Posture](release-posture.md). Changing current product posture is defined only in the dated [Public Operating Posture](../status/public-operating-posture.md).

## Version Form

Published versions use:

`vMAJOR.MINOR.PATCH[-PRERELEASE]`

The proposed first hardened candidate is:

`v0.1.0-pre-alpha.1`

It is proposed only. No tag or GitHub release is created by this repository change.

## Pre-v1 Semantics

While `MAJOR` is `0`:

- `MINOR` may contain governance- or architecture-incompatible changes
- `PATCH` contains compatible clarification, correction, or policy hardening within the same minor contract
- a prerelease suffix identifies a candidate that is not a stable public contract
- every incompatible change must name affected documents and migration expectations

Pre-v1 does not mean controls are optional. It means readers must consult the exact version or commit and review migration notes before treating a contract as compatible.

## Prerelease Labels

- `pre-alpha.N` — governance structure and initial product contract are still under active hardening
- `alpha.N` — the public contract supports a bounded alpha posture, without implying general availability
- `beta.N` — the public contract supports a bounded beta posture after explicit review
- `rc.N` — candidate for a stable release with no known planned governance incompatibility

Labels describe Hydra Core contract maturity. They do not grant Hydra Quant access, mode promotion, strategy authority, or public-user execution.

## Change Classification

Every pull request selects the highest applicable class:

| Class | Meaning | Version impact before v1 |
| --- | --- | --- |
| Editorial | Formatting, typo, or navigation change with no semantic effect | Usually patch or no release |
| Clarifying governance | Makes an existing rule more precise without changing authority or required behavior | Patch |
| Governance | Changes enforcement, evidence, recovery, permission, or operating expectations | Minor unless explicitly compatible |
| Architecture-significant | Changes a public responsibility or authority boundary | Minor with migration notes |
| Security hardening | Narrows exposure or strengthens validation without publishing protected detail | Patch or minor according to compatibility |

If classification is uncertain, use the more significant class until owner review resolves it.

## Compatibility

A change is incompatible when a conforming reader, implementation, validator, or governance process must change to preserve the same meaning. Examples include:

- renaming or redefining a state value
- changing the execution invariant or authority precedence
- changing required evidence metadata
- changing a schema-required field or enum
- moving responsibility between Core, Guardian, execution, recovery, or user surfaces
- changing correction or disclosure semantics

Adding optional explanatory prose is not automatically incompatible. Adding a required gate or narrowing permission may be intentionally incompatible even when it is safer.

## Schema Versions

Document release versions and schema versions are related but independent:

- a schema `schema_version` changes when its machine contract changes
- compatible optional schema additions increment the schema minor or patch according to the schema's own published rule
- incompatible schema changes require a new major schema version or a new schema file
- examples must declare and validate against their exact schema version

Pre-v1 repository versions do not justify silently breaking a schema with the same `schema_version`.

## Release Discipline

Before proposing a version:

- classify every change
- identify public/private and dynamic-posture impact
- identify state, evidence, ledger, and security impact
- provide migration notes for incompatible semantics
- run the documented validation suite
- review the complete diff for protected information
- prepare release notes without creating a tag or release until separately authorized

Ledger qualification and correction rules are defined only in the [Risk Event Ledger Policy](risk-event-ledger-policy.md). A repository release note does not fabricate a governance event.

## V1 Criterion

A future v1 requires owner review that the public governance contract is stable enough for durable external reliance. It would not prove private implementation completeness, strategy edge, regulatory status, or profitability.

Related documents:

- [Release Posture](release-posture.md)
- [Risk Event Ledger Policy](risk-event-ledger-policy.md)
- [Proposed v0.1.0-pre-alpha.1 Notes](../release-notes/v0.1.0-pre-alpha.1.md)
