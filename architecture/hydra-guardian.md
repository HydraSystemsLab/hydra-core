# Hydra Guardian

Hydra Guardian is the independent supervisory and risk authority governing Hydra Quant's private implementation. It is a governed private surface, not a public product or strategy.

## Authority

Guardian evaluates whether a requested action remains inside documented trust, permission, lifecycle, mode, and gate boundaries. It can:

- veto a requested action
- narrow a scoped trust posture
- disarm a scope
- require recovery and reconciliation
- prevent lower-layer state from relaxing a stricter restriction
- require evidence before lifecycle normalization or rearm

Guardian decisions are authoritative within their defined scope when system safety or integrity is in question. They still cannot create public-user permission or override a stricter external authority.

## Inputs

Public-safe input classes include:

- current and prior scoped state
- intent and decision metadata
- feed and control freshness
- execution acknowledgements, rejects, fills, and unresolved lifecycle events
- constraint and loss-domain status
- restart, recovery, and reconciliation status
- public-safe incident and dependency signals

Missing, stale, contradictory, or untrusted inputs are control conditions, not merely dashboard defects.

## Outputs

Guardian may produce:

- a named gate verdict and public-safe reason
- a veto or block
- a scoped disarm
- a recovery requirement
- a restriction on permitted actions
- a separately governed recommendation for recovery clearance or rearm

A result such as `PASS`, `AMBER`, `RED`, or `FROZEN` must identify the gate tested. It is not a universal safety or profit verdict.

## State Behavior

Guardian follows the [Multi-Axis State Model](state-model.md):

- `SAFE` is coherent control state, not positive expectancy
- `ARMED` is conditional scoped permission, not an instruction
- `RECOVERY_REQUIRED` cannot be cleared by restart or time
- `SHADOW` cannot authorize order submission
- `DEGRADED`, `AMBIGUOUS`, and `UNSAFE` block new exposure except defined containment
- contradictory authority resolves to the more restrictive permitted-action set

## Machine-Learning Boundary

A model may provide a bounded input to research or supervision only under explicit authority. It cannot acquire execution permission, change mode, override risk, or become an autonomous trade authority through performance, configuration, or integration side effects.

Promotion of model authority requires defined evidence, negative testing, scope, failure behavior, and governance review.

## Non-Claims

Guardian does not guarantee safety, security, profitability, or loss prevention. Its defensible objective is to mechanically block defined unsafe actions while the documented boundaries and enforcement controls are operating as designed.

Related documents:

- [Control Boundaries](control-boundaries.md)
- [Hydra Quant](hydra-quant.md)
- [Failure Modes](../governance/failure-modes.md)
- [Threat Model](../governance/threat-model.md)
