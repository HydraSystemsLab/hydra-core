# Hydra Ecosystem

Hydra Core is the public map. The private systems are where implementation lives.

Hydra is a risk-first systems architecture for building and operating market and research automation under supervision.
Core describes how the system is meant to behave.
Quant, Guardian, Predict, and Ember are private implementation surfaces that follow that doctrine.

| Surface | Public Role |
| --- | --- |
| Hydra Core | Public governance layer |
| Hydra Quant | Private trading and research infrastructure |
| Hydra Guardian | Private supervisory and risk layer |
| Hydra Predict | Private prediction-market research architecture |
| Hydra Ember | Private market scanner and research pipeline |

## Why The Public/Private Boundary Exists

Public docs describe how Hydra is meant to behave.
Private repos contain implementation, strategy logic, execution wiring, account configuration, and live operational details.
That split is intentional.
The public surface should make the doctrine understandable without exposing the machinery.

This repository should be useful to a serious reader without turning private operating details into public material.

## Hydra Core

Hydra Core is the public governance layer.

It defines the operating language around risk, control boundaries, state, recovery, and release posture.
It does not publish private system code and is not a software distribution.

## Hydra Quant

Hydra Quant is private trading and research infrastructure.
See [Hydra Quant](hydra-quant.md) for the dedicated public-safe surface doc.

Its public-safe shape is a risk-first execution stack with observation, daily briefs, control-room reporting, bridge health checks, and fail-closed rules.
The current private posture has one approved live-money lane, `C15396`.
Other lanes are treated as shadow, quarantined, or research-only unless evidence and controls justify promotion.

ML remains shadow-only in the current posture.
It acts as a meta-filter or supervisory signal, not as an autonomous trade generator.
B5 remains shadow/no-send unless promoted through controls.

Hydra Quant now includes operator visibility for funded-account inactivity risk.
That visibility does not loosen the strategy.
If an inactivity deadline approaches and no valid live-money signal occurs, account-preservation decisions remain operator-controlled.

Hydra Quant does not force activity by weakening rules.
Missing a trade is acceptable.
Forcing a bad one is not.

## Hydra Guardian

Hydra Guardian is the supervisory and risk layer.
See [Hydra Guardian](hydra-guardian.md) for the dedicated public-safe surface doc.

It handles disarm logic, vetoes, state checks, loss protection, recovery posture, and the decision to do nothing when state is unsafe or unclear.
Guardian is not a strategy.
It is the boundary that stops strategies from becoming uncontrolled.

## Hydra Predict

Hydra Predict is a private prediction-market research and execution architecture.
See [Hydra Predict](hydra-predict.md) for the dedicated public-safe surface doc.

It is built around venue truth, quote reconciliation, strict paper/live separation, shadow monitoring, and operator-controlled promotion.
The posture is research-first: reconcile what is true before acting on what looks interesting.

## Hydra Ember

Hydra Ember is a private market research and scanner pipeline.
See [Hydra Ember](hydra-ember.md) for the dedicated public-safe surface doc.

It focuses on early-signal research, offline data ingestion, replay and walk-forward checks, dashboards, and review packs.
It is a research surface, not a public trading product.

## Shared Operating Doctrine

Across the private systems, the public doctrine is the same:

- survivability over activity
- fail closed when state is stale, contradictory, or missing
- separate strategy intent from supervisory permission
- keep shadow and quarantined lanes from becoming live just because they exist
- promote only when evidence and controls justify promotion
- prefer a missed opportunity to an unsafe action
- keep the operator responsible for exceptional account-preservation decisions

## What Is Intentionally Not Public

Hydra Core does not publish exact strategy rules, private strategy parameters, venue wiring, account-specific operating material, credentials, private research logic, source data, or live run procedures.

The public docs explain the operating model.
They do not expose the machinery.
