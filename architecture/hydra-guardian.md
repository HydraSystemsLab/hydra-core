# Hydra Guardian

Hydra Guardian is the private supervisory and enforcement layer behind Hydra Quant.

It exists because strategy logic and execution logic are not sufficient substitutes for governance.
Guardian is concerned with whether the system should be allowed to continue operating at all.

## What It Is

Hydra Guardian is the control layer that evaluates system health, state validity, and enforcement conditions above the level of any single engine.

Conceptually, it sits between intent generation and continued permission to execute.
Its purpose is not to produce trades.
Its purpose is to constrain, pause, disarm, or veto unsafe operation.

## What It Monitors

Guardian monitors the classes of conditions that determine whether system state is trustworthy enough to keep running, including:

- engine state and whether that state remains internally consistent
- risk state, disarm state, and whether constraints remain authoritative
- feed liveness and whether market inputs are stale or missing
- execution liveness and whether intents are being acknowledged, rejected, or stranded
- restart and recovery state when the system is resuming after interruption
- supervisory signals from monitoring and watchdog processes

The exact implementation is private, but the public operating model is simple: Guardian treats stale, contradictory, or missing state as a control problem, not just an observability problem.

## What It Enforces

Guardian enforces system-level safety conditions such as:

- fail-closed behavior when state cannot be validated
- disarm or pause behavior when loss, execution, or control conditions become unsafe
- restart gating until system state is coherent again
- bounded recovery rather than blind resumption
- authoritative veto when lower layers request actions that should not proceed

This makes Guardian an enforcement function, not a dashboard.

## What It Can Veto

Guardian may veto:

- new execution requests when system state is stale or ambiguous
- continued engine activity after a hard risk or integrity event
- restart or rearm attempts that occur before verification
- actions that would reintroduce exposure while supervisory state is unresolved

The public rule is that uncertain permission is treated as no permission.

## Relationship To Hydra Quant

Hydra Quant contains the private strategy and execution systems that operate within Hydra's rules.
Guardian is not a strategy component inside Quant.
It is the supervisory layer that determines whether Quant is permitted to continue acting.

Quant may generate valid intents at the strategy level and still be blocked at the Guardian level.
That is expected behavior.

The separation matters:

- Quant is responsible for acting within market logic and execution rules
- Guardian is responsible for enforcing whether the system remains safe enough to act

This separation helps preserve independent failure domains and prevents strategy urgency from overriding supervisory control.

## Operating Bias

Guardian is intentionally conservative.
When the system cannot demonstrate safe state, the expected result is veto, pause, or disarm.

Related documents:

- [System Overview](system-overview.md)
- [Operating Principles](../operations/operating-principles.md)
- [Failure Modes](../governance/failure-modes.md)
- [Risk Event Ledger](../governance/risk-event-ledger.md)
