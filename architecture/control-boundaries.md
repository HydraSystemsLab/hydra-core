# Control Boundaries

Hydra is a governed system of scoped authorities. Control boundaries exist so local urgency, technical health, or promising results cannot silently expand permission.

Strategies are replaceable. Independent enforcement remains required.

## Boundary Model

### Research And Decision Engines

Engines may:

- observe permitted inputs and generate research or decision intents
- maintain local state required for those intents
- operate only inside their configured scope and mode
- report health, freshness, and evidence metadata

Engines may not:

- define global trust or permission
- clear recovery or rearm themselves
- promote their mode
- override Guardian, execution, or public-user restrictions

### Hydra Guardian

Guardian may:

- evaluate state and required supervisory gates
- narrow trust, disarm, veto, pause, and require recovery
- enforce the more restrictive outcome when authoritative layers disagree
- define the evidence required for scoped recovery and rearm

Guardian may not:

- originate strategy direction
- treat health as proof of edge
- make a public product available through private permission
- replace execution validation or canonical evidence storage

### Execution Layer

The execution layer may:

- validate an eligible request against constraints, state, scope, destination, and mode
- reject invalid, duplicate, stale, or unauthorized requests
- perform explicitly defined containment actions
- preserve lifecycle evidence for reconciliation

The execution layer may not:

- originate a trade
- promote an operating mode
- reinterpret `SHADOW` as an order-capable mode
- infer permission from a valid payload or healthy connection

### Monitoring And Observability

Monitoring may expose current, sanitized evidence about state, health, decisions, and failures. It may trigger an alert or supervisory evaluation.

Monitoring may not grant permission, silently fill missing state, or present a runner-health result as a strategy or authorization result.

### Advisory And Shadow Values

An advisory component may calculate and record a recommendation for comparison,
but it does not acquire the authority assigned to the component that creates the
live candidate. A shadow advisory value cannot replace or resize an authoritative live candidate.
An enforced gate must evaluate the candidate produced by the named live
authority while preserving the advisory value as a separate observation.

If provenance shows that an advisory value changed the live candidate, reject
and contain the affected request, preserve both values and their identities,
trace the exact call path, and exercise negative authority-boundary tests before
restoration.

### Recovery And Watchdog

Recovery functions may hold a scope in `RECOVERY_REQUIRED`, execute bounded recovery checks, and propose that recorded conditions have been satisfied.

They may not clear the lifecycle condition, rearm, or resume execution merely because a process restarted or time elapsed.

### User-Facing Surfaces

Public and alpha surfaces may display only allowlisted, sanitized state. They may not contain private operational payloads, infer private permission, or turn a display control into an execution control.

Read-only user access and system operating mode are separate. A read-only `SHADOW` surface cannot submit orders even if a private internal scope has different authority.

## Restrictive Composition

For any requested action:

1. identify every applicable authority and scope
2. evaluate independent trust, permission, lifecycle, and mode values
3. apply the intersection of permitted actions
4. treat missing, stale, or contradictory state as restrictive
5. evaluate every remaining required gate

Lower layers cannot override a stricter higher-layer state. A containment action may reduce or close risk only when the failure policy explicitly allows it; containment is not a path to new exposure.

## Boundary Evidence

Every material allow, block, disarm, recovery clearance, rearm, or promotion decision should leave enough public-safe or private evidence to identify:

- scope and authority
- state tuple and observation time
- requested action and mode
- named gates and results
- decision and reason code
- unresolved conditions and evidence classification

Public disclosure may withhold protected detail, but it must not replace missing support with a stronger claim.

Related documents:

- [System Overview](system-overview.md)
- [State Model](state-model.md)
- [Hydra Guardian](hydra-guardian.md)
- [Failure Modes](../governance/failure-modes.md)
