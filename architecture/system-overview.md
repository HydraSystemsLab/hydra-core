# System Overview

Hydra Systems separates decision generation, supervisory authority, execution validation, observability, recovery, and user-facing truth. The separation limits what any one component can authorize.

## Conceptual Components

### Research And Decision Engines

Engines may propose intents within a defined research or operating scope. Strategy existence, a generated intent, or runner health does not grant execution authority or prove strategy edge.

### Hydra Guardian

Hydra Guardian is the independent supervisory and risk authority. It evaluates scoped trust, permission, lifecycle, mode, and required gates. It may narrow permission, veto actions, disarm, or require recovery; it does not generate strategy direction.

### Execution Layer

The execution layer validates eligible requests against current constraints, scope, destination, mode, idempotency, and lifecycle state. It preserves acknowledgements, rejects, fills, and terminal outcomes needed for authoritative reconciliation.

### Monitoring And Observability

Observability makes control state, decisions, freshness, and unresolved contradictions legible. A healthy dashboard or runner is evidence only for the named health contract; it is not permission or edge.

### Recovery And Watchdog Functions

Recovery functions detect continuity loss and hold the affected scope behind reconciliation. Restart and elapsed time do not clear `RECOVERY_REQUIRED` or rearm a system.

### Public And Alpha Surfaces

Public documents and an authenticated alpha Control Room are sanitized views over canonical state. They cannot grant private execution authority. Stale public posture becomes `UNKNOWN/REVIEW_REQUIRED` rather than remaining apparently current.

## Execution Invariant

> Execution is eligible only when trust is `SAFE`, permission is `ARMED`, lifecycle is `NORMAL`, the configured operating mode permits execution, and every required gate passes.

Each condition applies to the named scope. A stricter higher-layer state controls, missing state fails closed, and public-user permission remains separate from internal permission.

## Design Objectives

- mechanically block defined unsafe actions while documented controls operate as designed
- preserve narrow failure domains and independent supervisory authority
- prefer authoritative reconciliation to optimistic continuity
- keep observation available where safe while execution is blocked
- separate system health, execution readiness, strategy edge, evidence class, and user permission
- make promotion an explicit governance event

This architecture reduces defined risks; it does not guarantee safety, security, or profitability.

Related documents:

- [Control Boundaries](control-boundaries.md)
- [State Model](state-model.md)
- [Hydra Guardian](hydra-guardian.md)
- [Threat Model](../governance/threat-model.md)
