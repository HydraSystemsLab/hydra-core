# Hydra Core

Hydra Core is the public governance and failure-control specification for Hydra
Systems trading infrastructure.

**Hydra Systems builds trading infrastructure for independent traders and small
prop desks.** Core documents how that infrastructure constrains authority,
contains failure, preserves evidence, and returns to service deliberately.

[Formal specifications](docs-map.md) · [Current public posture](status/public-operating-posture.md) · [Private-alpha contract](product/hydra-quant-private-alpha.md) · [Security](SECURITY.md) · [Hydra Systems](https://hydrasystems.tech)

## Why Controlled Failure Matters

Automated trading systems fail through stale state, duplicate action, ambiguous
authority, broken continuity, and unsafe recovery as well as through incorrect
decisions. Hydra Core defines the boundaries that keep those failures narrow,
observable, and recoverable.

The central invariant is:

> Execution is eligible only when trust is `SAFE`, permission is `ARMED`,
> lifecycle is `NORMAL`, the configured operating mode permits execution, and
> every required gate passes.

Eligibility is conditional, never an instruction. Missing or contradictory
state fails closed.

## System Hierarchy

- **Hydra Systems** — the infrastructure operation and umbrella.
- **Hydra Quant** — the proprietary systematic-trading platform under
  development.
- **Hydra Guardian** — the supervisory and risk authority within the system.
- **Hydra Core** — the public governance and failure-control specification.

The [Public Surface Registry](architecture/public-surface-registry.md) is the
canonical classification of these named surfaces.

## Formal Specifications

- [Control Boundaries](architecture/control-boundaries.md)
- [Multi-Axis State Model](architecture/state-model.md)
- [Failure Modes](governance/failure-modes.md)
- [Threat Model](governance/threat-model.md)
- [Public Evidence Policy](governance/public-evidence-policy.md)
- [Risk Event Ledger and Schema](governance/risk-event-ledger.md)
- [Operator and Recovery Expectations](operations/operator-runbook.md)
- [Complete Documentation Index](docs-map.md)

## Current Public Boundary

Hydra Core remains pre-v1. Hydra Quant is in private-alpha preparation. Planned
initial external access is read-only and shadow-only; public-user broker
connection, order submission, and live execution remain disabled.

The dated [Public Operating Posture](status/public-operating-posture.md) is the
only source for changing availability and permission. When it expires,
consumers must report `UNKNOWN/REVIEW_REQUIRED` rather than assume continuity.

Public documents do not expose strategy logic, parameters, credentials,
accounts, broker wiring, operational paths, logs, or protected research. They
also do not establish profitability, availability, certification, or regulatory
approval.

## Repository Status

No software release, tag, or reuse licence has been published. See the
[Release Posture](governance/release-posture.md), [Versioning Policy](governance/versioning-policy.md),
and [Contributing Guide](CONTRIBUTING.md) before relying on or proposing changes
to this pre-v1 contract.
