# State Model

Hydra uses a small set of public-safe operating states to describe whether execution is permitted, constrained, or blocked.
These states are governance states, not market predictions.

Their purpose is to make permission legible.

## State Principles

- safe state must be demonstrable, not assumed
- ambiguous state is treated as unsafe until resolved
- armed and disarmed describe permission, not confidence
- degraded state may still allow observation while blocking new exposure
- recovery is a controlled process, not an automatic reset

## Operating States

### Safe
Safe means the system can presently demonstrate coherent control state, trustworthy observability, and valid enforcement conditions.

Allowed behavior:

- supervised execution may proceed
- normal monitoring and control checks continue

Blocked behavior:

- none beyond normal risk and supervisory constraints

### Unsafe
Unsafe means the system has identified a condition that makes continued operation unacceptable.
Examples include breached constraints, invalid protective conditions, or supervisory failures that require immediate containment.

Allowed behavior:

- containment actions
- evidence preservation
- controlled transition toward disarm or recovery-required state

Blocked behavior:

- new execution
- optimistic continuation
- rearm without verification

### Ambiguous
Ambiguous means the system cannot prove what state it is in with enough confidence to continue safely.
State may be stale, contradictory, incomplete, or missing.

Allowed behavior:

- fail-closed behavior
- reconciliation, validation, and recovery checks
- operator review using authoritative truth surfaces

Blocked behavior:

- new execution
- automatic rearm
- treating absence of evidence as evidence of safety

Ambiguous state must be treated defensively because uncertainty about exposure, constraint validity, or supervisory authority is itself a risk event.
If the system cannot prove that it is safe, it must behave as though it is not.

### Armed
Armed means the system is permitted to execute if all other active controls also agree.
It does not mean execution is mandatory or unrestricted.

Allowed behavior:

- supervised execution when the rest of the control model remains valid

Blocked behavior:

- bypassing strategy, execution, or supervisory checks

Armed status should be read as conditional permission.

### Disarmed
Disarmed means execution permission has been withdrawn.
This may be caused by risk, integrity, observability, or recovery concerns.

Allowed behavior:

- observation
- investigation
- repair and verification work

Blocked behavior:

- new execution
- silent resumption
- operator assumption that elapsed time clears the condition

### Degraded
Degraded means some supporting capability is impaired enough to reduce trust or shrink what the system is allowed to do, but not every function is necessarily offline.

Allowed behavior:

- constrained monitoring
- bounded diagnostics
- selective containment based on the degraded surface

Blocked behavior:

- any activity that depends on the degraded capability being trustworthy
- broad resumption before the degradation is understood

Degraded state should bias toward narrower permissions, not broader ones.

### Recovery-Required
Recovery-required means the system cannot return to normal operation until explicit reconciliation and validation have been completed.
This often follows disarm, restart ambiguity, execution ambiguity, or other integrity events.

Allowed behavior:

- recovery procedures
- validation of exposure, constraints, liveness, and control state
- governed preparation for possible rearm

Blocked behavior:

- automatic return to active execution
- treating restart alone as recovery

## State Interactions

These states are related but not interchangeable:

- a system may be `disarmed` because it is `unsafe`
- a system may be `disarmed` because it is `ambiguous`
- a system may be `degraded` without being fully `unsafe`, while still blocking execution
- a system may be technically recoverable but remain `recovery-required` until verification is complete
- a system should only be treated as operational when it is both `safe` and `armed`

## Public Operating Bias

Hydra treats permission conservatively.
The bias is:

- prefer inactivity to unverified activity
- prefer explicit disarm to silent drift
- prefer verified recovery to optimistic restart

In this model, fail-closed behavior is not a special mode.
It is the expected response whenever safe state cannot be demonstrated.

Related documents:

- [Control Boundaries](control-boundaries.md)
- [Operating Principles](../operations/operating-principles.md)
- [Failure Modes](../governance/failure-modes.md)
