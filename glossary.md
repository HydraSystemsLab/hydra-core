# Glossary

These public definitions are normative unless a more specific contract narrows them.

## Armed

`ARMED` is conditional permission for a named scope and configured mode if all other state and gates pass. It is never an instruction to trade. In `SHADOW`, it permits shadow processing only.

## Ambiguous

`AMBIGUOUS` is a trust value meaning authoritative state cannot be proved because it is missing, stale, contradictory, or unreconciled. It blocks new exposure.

## Control Boundary

A responsibility and authority line that prevents one layer from silently taking over another layer's control function.

## Degraded

`DEGRADED` is a trust value for a known impairment that narrows reliable behavior. It blocks new exposure except explicitly defined containment.

## Demo

`DEMO` is an operating mode that may permit eligible orders only in a segregated demo or simulation domain. Demo evidence is not live evidence.

## Disarmed

`DISARMED` means scoped execution permission is absent or withdrawn. Observation and recovery may continue, but new exposure is blocked.

## Enforcement

The ability to block, veto, halt, disarm, constrain, or require recovery for a defined action. Documentation and alerts alone are not enforcement.

## Evidence Tier

One of five non-combinable classes: historical backtest, replay, forward shadow, demo execution, or verified live execution.

## Execution Eligibility

The condition in which trust is `SAFE`, permission is `ARMED`, lifecycle is `NORMAL`, the configured mode permits the requested execution, and every required gate passes. Eligibility is not an instruction, edge claim, or public-user permission.

## Fail Closed

Resolve missing, stale, invalid, or contradictory control state toward the restrictive permitted-action set rather than assuming permission.

## Forward Shadow

Prospective decisions recorded as data arrives while order submission is disabled. Forward shadow is not execution evidence.

## Guardian

Hydra Guardian, the independent supervisory and risk authority that governs private operation and may narrow permission or require recovery.

## Live

`LIVE` is an operating mode in which live-domain orders may be eligible within explicit private authority. It does not imply current authorization, public-user access, or profitability.

## Normal

`NORMAL` is the lifecycle value meaning no unresolved recorded recovery condition applies to the scope. It does not imply trust or permission.

## Observe Only

`OBSERVE_ONLY` is an operating mode permitting observation and diagnostics without order submission.

## Public-User Permission

Authority granted to an external user. It is separate from private internal operational permission and cannot be inferred from it.

## Recovery Required

`RECOVERY_REQUIRED` is the lifecycle value requiring explicit reconciliation and validation before lifecycle normalization. Restart and time cannot clear it.

## Safe

`SAFE` is a trust value meaning required control state is coherent for the named scope and time. It does not mean risk-free, profitable, or authorized.

## Shadow

`SHADOW` is an operating mode that processes current inputs and records hypothetical decisions without order submission.

## Supervisory Authority

An authority above strategy intent that may narrow what lower layers are permitted to do. In the public model, Hydra Guardian performs this role for Hydra Quant.

## Unsafe

`UNSAFE` is a trust value for a known condition that makes new exposure unacceptable or indicates a material control failure. It requires containment and governed recovery as defined.
