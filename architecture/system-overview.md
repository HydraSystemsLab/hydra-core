# System Overview

## Concept
Hydra is a multi-engine system:
- multiple independent decision engines (per market / strategy type)
- a shared risk core that enforces constraints globally
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

### Risk Core
The risk core enforces constraints, including (non-exhaustive):
- max loss limits
- exposure limits
- disarm states
- rule-based gating

Risk decisions are authoritative.

### Execution Layer
The execution layer:
- validates orders against constraints
- ensures protective parameters are present and sane
- normalises requests
- logs outcomes and rejects

## Design Goals
- survivability > performance
- enforcement > discretion
- observability > opacity
- simplicity at the boundaries
