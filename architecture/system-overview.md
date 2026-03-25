# System Overview

## Concept
Hydra is a multi-engine system:
- multiple independent decision engines (per market / strategy type)
- Hydra Guardian as the supervisory and enforcement layer behind Hydra Quant
- an execution layer that validates, normalises, and logs actions

The system is designed so that:
- engines can be wrong
- execution can be delayed
- markets can regime-shift
…and the system still survives.

## Components
### Engines
Engines generate intents (e.g., trade proposals) based on their own rules.
Engines do not control global risk.

### Hydra Guardian
Hydra Guardian is the named supervisory and enforcement layer.
It enforces system-level constraints, including (non-exhaustive):
- max loss limits
- exposure limits
- disarm states
- rule-based gating

Guardian decisions are authoritative when system safety is in question.

### Execution Layer
The execution layer:
- validates orders against constraints
- ensures protective parameters are present and sane
- normalises requests
- logs outcomes and rejects

### Monitoring And Recovery
Monitoring, observability, and watchdog functions exist to verify whether state remains trustworthy enough to continue operating.
When state becomes stale, ambiguous, or unsafe, the expected behavior is pause, veto, disarm, or gated recovery rather than optimistic continuation.

## Design Goals
- survivability > performance
- enforcement > discretion
- observability > opacity
- simplicity at the boundaries

Related documents:

- [Hydra Guardian](hydra-guardian.md)
- [Risk Doctrine](../doctrine/risk-doctrine.md)
- [Failure Modes](../governance/failure-modes.md)
