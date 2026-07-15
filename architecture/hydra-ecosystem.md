# Hydra Systems Hierarchy

Hydra Systems is the trading-infrastructure operation and umbrella. Hydra Core
publishes the governance and failure-control contract for the private system;
it does not publish the implementation.

The [Public Surface Registry](public-surface-registry.md) is the canonical
classification of named public surfaces.

## Public And Private Shape

- **Hydra Systems** builds trading infrastructure for independent traders and
  small prop desks.
- **Hydra Quant** is the proprietary systematic-trading platform under
  development.
- **Hydra Guardian** is the supervisory and risk authority within Hydra Quant.
- **Hydra Core** publishes the system's governance and failure-control
  specifications.

Current availability and public-user permissions live only in the dated
[Public Operating Posture](../status/public-operating-posture.md).

## Public Contract Boundary

The public contract makes authority, evidence standards, failure handling, and
user permissions reviewable without publishing protected machinery. It does not
publish:

- strategy rules, parameters, thresholds, or model features
- credentials, account configuration, balances, or broker wiring
- private execution routes, request payloads, or protected schemas
- internal hosts, paths, logs, reports, datasets, or research artefacts

## Durable Authority Model

Hydra Quant may propose intents inside declared scope. Hydra Guardian can narrow
permission, veto actions, disarm a scope, or require recovery. The execution
layer independently validates permission, destination, mode, constraints, and
lifecycle. No lower layer may relax a stricter authority state.

Across the governed system:

- trust, permission, lifecycle, and operating mode remain independent
- missing or contradictory state fails closed
- observation may continue where safe while execution is blocked
- mode promotion is an explicit governance event
- public-user permission cannot be inferred from private internal posture
- health and operability claims remain separate from edge and performance claims

These boundaries remain durable even when the dated public posture changes.
