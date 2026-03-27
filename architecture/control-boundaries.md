# Control Boundaries

Hydra is designed as a governed operating system, not as a single block of trading logic.
Its control boundaries exist so that local urgency cannot override system safety.

Strategies are replaceable.
Enforcement is not.

## Boundary Model

### Strategies / Engines
Strategies and engines are responsible for:

- generating intents within their own market logic
- maintaining local decision state needed to produce those intents
- accepting supervisory constraints and stop conditions

Strategies and engines are not responsible for:

- defining global permission to continue operating
- overriding disarm, veto, or recovery gates
- deciding system-wide risk posture

Conceptual flow:

- outbound: trade intents, local state, health signals
- inbound: permission, veto, disarm, pause, recovery constraints

### Hydra Guardian
Hydra Guardian is the supervisory and enforcement layer behind Hydra Quant.
It is responsible for:

- evaluating whether the system remains safe enough to act
- enforcing disarm, veto, pause, and rearm conditions
- treating stale, contradictory, or missing state as a control problem
- preserving authoritative control when lower layers disagree or become uncertain

Hydra Guardian is not responsible for:

- generating alpha or trade ideas
- expressing market preference
- acting as a substitute for execution validation or observability storage

Conceptual flow:

- inbound: intents, state validity signals, observability inputs, recovery status
- outbound: approval, denial, disarm, gating, supervisory decisions

### Execution Layer
The execution layer is responsible for:

- validating executable requests against required constraints
- normalising requests into a safe execution form
- returning acknowledgements, rejects, and terminal outcomes
- preserving execution evidence needed for later reconstruction

The execution layer is not responsible for:

- deciding whether the system should remain armed
- reinterpreting supervisory policy on its own authority
- originating strategy direction

Conceptual flow:

- inbound: approved execution requests and required constraints
- outbound: execution outcomes, rejects, status changes, lifecycle evidence

### Monitoring / Observability
Monitoring and observability are responsible for:

- making system state visible enough to evaluate safety
- exposing evidence for what happened, what was blocked, and what remains unresolved
- surfacing liveness, anomalies, and contradiction between layers

Monitoring and observability are not responsible for:

- granting permission to trade
- replacing enforcement with dashboards or alerts
- assuming that visibility alone is a control mechanism

Conceptual flow:

- inbound: state changes, decisions, execution outcomes, liveness signals
- outbound: operator truth surfaces, anomaly signals, governance evidence

### Recovery / Watchdog
Recovery and watchdog functions are responsible for:

- detecting when continuity has been interrupted or state trust has degraded
- holding restart and recovery behind verification
- restoring operation only through governed re-entry conditions

Recovery and watchdog functions are not responsible for:

- silently clearing supervisory concerns
- treating restart as proof of safety
- bypassing disarm or ambiguity handling

Conceptual flow:

- inbound: liveness failures, stale state, unresolved control conditions
- outbound: recovery-required signals, restart gating, bounded recovery actions

## Why Boundaries Matter

These boundaries are not organizational preferences.
They are survivability controls.

Without them:

- strategy urgency can override supervision
- execution can continue while control state is unresolved
- observability becomes post-hoc explanation instead of operational truth
- recovery can become an ungoverned path back into exposure

With them:

- failure domains stay smaller
- authority remains legible
- ambiguous state can be contained quickly
- recovery follows verification rather than optimism

The public rule is simple:
each layer should do one class of control work clearly enough that a failure in one layer does not silently erase the safeguards of another.

Related documents:

- [System Overview](system-overview.md)
- [State Model](state-model.md)
- [Hydra Guardian](hydra-guardian.md)
