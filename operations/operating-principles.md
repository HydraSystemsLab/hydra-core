# Operating Principles

## Default Bias

Hydra prefers inactivity to unverified activity. Observation may continue where safe, but new exposure requires the full state invariant and every required gate.

## Independent State

Trust, permission, lifecycle, and mode are recorded separately. Missing or contradictory state fails closed, and the stricter applicable authority controls.

## Loss Handling

Loss does not justify larger size, weaker constraints, a mode change, or a bypass. Defined exposure and loss limits must be enforced; failure to enforce them is a control incident.

## Disarm And Recovery

A disarm is a safety outcome. It blocks new exposure without claiming that every other system function is offline.

`RECOVERY_REQUIRED` is cleared only after explicit reconciliation and validation. Lifecycle normalization and rearm are separate decisions. Restart, process health, and elapsed time are insufficient.

## Operating Mode

`OBSERVE_ONLY`, `SHADOW`, `DEMO`, and `LIVE` define distinct action domains. Promotion is a governance event. A result, healthy runner, or configuration change cannot promote mode automatically.

## Evidence And Claims

System operability, runner health, execution readiness, strategy edge, and public-user permission are separate claims. Evidence classes are labelled and cannot be merged.

## Observability

Hydra should produce enough current, authoritative evidence to explain what happened, what was blocked, which scope and gate applied, what remains unresolved, and what recovery requires.

## Change Control

Changes must state their governance classification, public/private impact, evidence impact, state-model impact, ledger impact, and validation. A change that cannot be explained should not be promoted.
