# Operating Principles

## Default Mode
Hydra should be boring.

The system is expected to:
- trade infrequently when conditions do not align
- stop when guardrails trigger
- resume only when conditions return

## Loss Handling
Losses do not trigger increased aggression.
After losses, the system becomes more conservative, not less.

## Disarms
A disarm is not an error.
A disarm is a safety outcome.

Once disarmed:
- execution stops
- further intents are rejected or ignored
- the system requires explicit safe conditions to resume

## Observability
Hydra must produce enough telemetry to answer:
- what happened
- why it happened
- what was prevented
- what would have happened without the guardrails

## Change Control
Changes must be deliberate.
If a change cannot be explained, it should not ship.
