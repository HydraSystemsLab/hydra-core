# Release Posture

Hydra Core remains pre-v1. This document defines public release maturity and the public/private boundary; changing product availability belongs only in the dated [Public Operating Posture](../status/public-operating-posture.md).

## Repository Scope

`hydra-core` publishes:

- architecture and control boundaries
- doctrine and operating expectations
- governance and evidence policy
- public schemas and sanitized examples

It is a public specification, not a public trading-software distribution. Private strategy code, execution wiring, credentials, account material, operational logs, and protected research are outside scope.

## Current Release Maturity

Pre-v1 means public governance semantics are still being tightened and may require migration. It does not make the documented controls optional.

The proposed release candidate is `v0.1.0-pre-alpha.1`. It is not a tag or published release. Version meaning and change classification are defined in the [Versioning Policy](versioning-policy.md).

## Public And Private Boundary

Hydra Systems is the trading-infrastructure operation and umbrella. Named
surfaces and their approved public roles are defined by the [Public Surface
Registry](../architecture/public-surface-registry.md).

- Hydra Quant is the proprietary systematic-trading platform under development.
- Hydra Guardian is the supervisory and risk authority within the system.
- Hydra Core is the public governance and failure-control specification.

Public documentation does not imply that a private system is externally available. Internal operational permission is distinct from public-user permission and is not disclosed through the public posture record.

## Pre-v1 Stability Objective

The repository is converging on stable meanings for:

- independent trust, permission, lifecycle, and mode axes
- fail-closed precedence and recovery
- public evidence classes and claim boundaries
- historical governance recording
- public/private information boundaries

A future v1 would signal stability of the public governance contract. It would not mean that private strategy development is complete, that private implementation is public, or that profitability has been proved.

## Canonical Current Posture

For current public release stage, product stage, external access, and public-user permissions, consult the [Public Operating Posture](../status/public-operating-posture.md). If that record is stale, its consumer-facing status is `UNKNOWN/REVIEW_REQUIRED`.
