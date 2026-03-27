# Glossary

This glossary defines public terms used across Hydra Core.
The goal is consistency, not exhaustiveness.

## Armed
`Armed` means execution permission is presently available if all other active controls also agree.
It is conditional permission, not a guarantee that execution will occur.

## Ambiguous
`Ambiguous` means the system cannot prove its state with enough confidence to continue safely.
Ambiguous state is treated defensively and fail-closed.

## Control Boundary
A `control boundary` is a responsibility line between system layers that prevents one layer from silently taking over another layer's safety function.

## Degraded
`Degraded` means some capability is impaired enough to reduce trust or narrow permitted behavior, even if the whole system is not fully offline.

## Disarmed
`Disarmed` means execution permission has been withdrawn.
Observation, investigation, and recovery work may continue, but new execution should not.

## Enforcement
`Enforcement` means the system can actually block, veto, halt, or disarm unsafe behavior.
It is stronger than documentation, alerts, or operator intent.

## Observability
`Observability` is the evidence surface that makes system state, decisions, and unresolved conditions visible enough to support supervision and recovery.

## Recovery-Required
`Recovery-required` means the system cannot return to normal operation until explicit reconciliation and validation have been completed.

## Safe
`Safe` means the system can presently demonstrate coherent control state, trustworthy observability, and valid enforcement conditions.

## Supervisory Layer
The `supervisory layer` is the authority above strategy logic that determines whether the system should be allowed to continue operating.
In Hydra's public model, Hydra Guardian fills this role behind Hydra Quant.

## Unsafe
`Unsafe` means the system has identified a condition that makes continued operation unacceptable and requires containment rather than continuation.
