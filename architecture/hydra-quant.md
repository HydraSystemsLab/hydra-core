# Hydra Quant

Hydra Quant is private trading and research infrastructure governed by Hydra Core doctrine.

It is not public strategy code.
It is a private implementation surface that must stay inside public control boundaries.

## Purpose

Hydra Quant exists to make market automation observable, constrained, and recoverable.

The aim is not constant activity.
The aim is supervised operation where unsafe state is blocked, ambiguous state fails closed, and promotion requires evidence.

## What It Is

Hydra Quant is a risk-first execution and research stack.

Public-safe components include:

- observation stack
- operator brief
- live control room
- feed and freshness checks
- proof and recovery visibility
- fail-closed checks around live posture
- supervisory boundaries through Hydra Guardian and Hydra Core

These surfaces help an operator understand whether the system is safe enough to act.
They do not replace enforcement.

## Current Public-Safe Posture

The current private posture has one approved live-money lane, `C15396`.
That statement describes current governance state, not a permanent promise.

Other lanes are shadow, quarantined, or research-only unless evidence and controls justify promotion.
B5 remains shadow/no-send in the current posture.
Non-approved lanes are not live just because they exist.

ML remains shadow-only as a meta-filter and supervisory signal.
ML-assisted regime detection exists as part of the context layer, used to understand market state and support supervised decision-making.
It does not create trades, override risk controls, or carry live execution authority on its own.

Funded-account inactivity risk is visible to the operator through a sentinel.
That visibility does not loosen C15396.
Hydra Quant does not force activity by weakening rules.

## What Is Not Public

Hydra Quant does not publish private strategy rules, private parameters, execution wiring, account-specific operating material, live configuration, private evidence files, or operational procedures.

The public docs describe behavior and boundaries.
They do not expose the machinery.

## Relationship To Guardian/Core

Hydra Core defines the public doctrine.
Hydra Guardian enforces supervisory permission.
Hydra Quant operates inside those constraints.

Quant may produce a valid local intent and still be blocked by Guardian or Core-level controls.
That is expected behavior.

## Current Boundaries

- C15396 is the current approved live-money lane.
- ML is shadow/meta-filter only unless separately promoted under governance.
- ML-assisted regime detection is context, not independent execution authority.
- B5 is shadow/no-send in the current posture.
- Quarantined and research lanes require evidence and controls before promotion.
- Activity pressure does not justify weaker rules.

Related documents:

- [Hydra Ecosystem](hydra-ecosystem.md)
- [Hydra Guardian](hydra-guardian.md)
- [Control Boundaries](control-boundaries.md)
- [Risk Doctrine](../doctrine/risk-doctrine.md)
