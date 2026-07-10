# Hydra Core

Hydra Core is the public governance and architecture specification for how Hydra Systems defines authority, evidence, failure handling, and operating boundaries around its governed systems.

[Hydra Systems website](https://hydrasystems.tech) · [Docs Map](docs-map.md) · [Current Public Posture](status/public-operating-posture.md) · [Private Alpha Contract](product/hydra-quant-private-alpha.md) · [Public Evidence Policy](governance/public-evidence-policy.md) · [Security](SECURITY.md)

| Contract status | Current public statement |
| --- | --- |
| Hydra Core | Pre-v1 |
| Hydra Quant | Private-alpha preparation |
| Initial external mode | Read-only and shadow-only (forward shadow) |
| Public-user broker connection | Disabled |
| Public-user order submission | Disabled |
| Public-user live execution | Disabled |

The table is a compact view of the dated canonical posture. If that record expires, consumers must display `UNKNOWN/REVIEW_REQUIRED`, not continue presenting its values as current.

## What Hydra Core Is

Hydra Systems is the company and umbrella. Hydra Core is its public governance surface for:

- system authority and control boundaries
- trust, permission, lifecycle, and operating-mode semantics
- failure containment, recovery, and rearm expectations
- public evidence classes and claim discipline
- selected historical governance records
- public/private information boundaries
- release and change-control expectations

Hydra Quant is the governed trading product/system under development. Hydra Guardian is the independent supervisory and risk authority. The [Public Surface Registry](architecture/public-surface-registry.md) defines the approved public classification of every named surface in scope.

## What Hydra Core Is Not

This repository is not:

- public strategy or execution software
- a live operating-status console
- a broker or account connection service
- a signal, copy-trading, or financial-advice service
- evidence of guaranteed profitability or stable returns
- formal verification, regulatory approval, or third-party certification
- proof that a private implementation is externally available

No real production dashboard screenshot currently exists. The [Control Room document](product/control-room-concept.md) is an explicitly labelled conceptual placeholder.

## Who It Is For

- operators and builders reviewing governed automation boundaries
- systematic traders evaluating evidence and decision legibility
- risk-aware alpha testers reviewing shadow software
- contributors improving public governance, schemas, and documentation quality

It is not intended for requests for private strategy logic, protected research, credentials, accounts, or actionable real-time entries and exits.

## Public/Private Boundary

Public materials define roles, states, evidence standards, and operating expectations. They do not expose private strategy rules, parameters, thresholds, model features, broker wiring, credentials, accounts, host details, paths, logs, order payloads, protected schemas, or research artefacts.

Internal operational permission and public-user permission are separate. A historical live event or private engine permission does not grant public access. Current private engine-level permission is deliberately not disclosed by the public posture record.

## Architecture Overview

Research and decision engines may propose intents. Hydra Guardian may narrow permission, veto, disarm, or require recovery. The execution layer independently validates scope, destination, mode, constraints, and lifecycle. Observability supports reconciliation; it does not grant authority. Recovery remains gated until recorded conditions are verified.

Start with:

- [System Overview](architecture/system-overview.md)
- [Control Boundaries](architecture/control-boundaries.md)
- [Hydra Guardian](architecture/hydra-guardian.md)
- [Failure Modes](governance/failure-modes.md)
- [Threat Model](governance/threat-model.md)

## Multi-Axis State Invariant

Hydra records four independent axes:

- trust: `SAFE`, `DEGRADED`, `AMBIGUOUS`, `UNSAFE`
- permission: `ARMED`, `DISARMED`
- lifecycle: `NORMAL`, `RECOVERY_REQUIRED`
- mode: `OBSERVE_ONLY`, `SHADOW`, `DEMO`, `LIVE`

> Execution is eligible only when trust is `SAFE`, permission is `ARMED`, lifecycle is `NORMAL`, the configured operating mode permits execution, and every required gate passes.

`ARMED` is conditional permission, never an instruction. `ARMED` in `SHADOW` authorizes shadow processing only and never order submission. Missing or contradictory state fails closed. See the [Multi-Axis State Model](architecture/state-model.md).

## Evidence Discipline

Hydra keeps five evidence classes separate:

1. historical backtest
2. replay
3. forward shadow
4. demo execution
5. verified live execution

They cannot be merged into one track record or added into one sample count. System operability, runner health, execution readiness, strategy edge, and public-user permission are also separate claims. Hydra makes no profit guarantee and promises no progression from shadow to demo or live.

See the [Public Evidence Policy](governance/public-evidence-policy.md) and the [Risk Event Ledger](governance/risk-event-ledger.md).

## Repository Map

- [Docs Map](docs-map.md) — complete navigation and reading paths
- `architecture/` — system roles, boundaries, state, and registered surfaces
- `doctrine/` — bounded risk-first principles
- `governance/` — evidence, failures, threats, releases, versions, and historical ledger policy
- `operations/` — public operator and recovery expectations
- `product/` — planned alpha and Control Room contracts
- `status/` — the only canonical changing public posture
- `schemas/` — machine-readable public contracts
- `examples/` — synthetic, sanitized schema examples
- `release-notes/` — proposed or published version notes
- `scripts/` and `tests/` — public-surface validation

## Contributing And Security

Read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing changes. Governance-bearing work is issue-first. Never submit private strategy material, credentials, accounts, logs, or protected implementation.

Report security concerns privately under [SECURITY.md](SECURITY.md). Do not disclose vulnerabilities or secrets in a public issue.

## Release Posture

Hydra Core remains pre-v1. `v0.1.0-pre-alpha.1` is proposed and not published. No tag or GitHub release is created by this hardening change.

- [Release Posture](governance/release-posture.md)
- [Versioning Policy](governance/versioning-policy.md)
- [Proposed Release Notes](release-notes/v0.1.0-pre-alpha.1.md)
- [Changelog](CHANGELOG.md)

## Licensing Status

No reuse terms have been published. Public visibility does not make this repository open source or grant permission to copy, modify, or redistribute its contents. Documentation licensing remains an owner decision separate from any future software licensing decision.
