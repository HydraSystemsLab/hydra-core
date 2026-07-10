# Hydra Quant

Hydra Quant is the governed trading product/system under development within Hydra Systems. Its implementation is private; its public operating contract is defined by Hydra Core.

A planned private alpha is governed by the public product contract. Current product phase, public-user availability, and permissions are stated only in the dated [Public Operating Posture](../status/public-operating-posture.md).

## Purpose

Hydra Quant is intended to make market-system decisions observable, constrained, recoverable, and honestly evidenced. It does not promise constant activity, profitability, or progression to execution.

## Durable Architecture

Public-safe component classes may include:

- market and regime observation
- research and decision engines
- supervisory evaluation through Hydra Guardian
- execution validation within explicitly authorized modes
- canonical ledgers and evidence provenance
- feed, state, and lifecycle health checks
- operator and user-facing truth surfaces

These classes describe architecture, not current availability. No private strategy logic, protected parameters, broker wiring, account configuration, or operational path is published here.

## Authority And Promotion

An engine may remain research-only or be configured in `OBSERVE_ONLY`, `SHADOW`, `DEMO`, or `LIVE` mode after the required governed decision. Mode and authority are scoped; neither transfers implicitly between engines, environments, users, or layers.

- Strategy existence does not grant execution authority.
- A healthy runner does not grant strategy authority or prove edge.
- `SAFE` control state does not prove profitability.
- `ARMED` is conditional permission within the configured mode, never an instruction.
- `ARMED` in `SHADOW` permits shadow processing only and never order submission.
- A private internal permission does not grant public-user permission.
- A private implementation does not prove that an external product is available.

Machine-learning or statistical components may inform research or bounded supervisory context. They cannot generate, enlarge, or inherit execution authority implicitly. Any promotion requires explicit evidence, defined authority boundaries, negative testing, and governance review.

## Hydra Control Room

Hydra Control Room is the planned user-facing interface. The current public document is a [conceptual placeholder](../product/control-room-concept.md), not a production screenshot and not evidence of live account state or performance.

## Private-Alpha Boundary

The planned initial alpha is governed by the [Hydra Quant Private-Alpha Contract](../product/hydra-quant-private-alpha.md). That contract excludes public-user broker connection, order submission, and live execution; current permissions remain defined only by the dated posture.

No progression from shadow to demo or live is promised. Any future change would require an explicit governance decision and an updated dated posture.

## Evidence Boundary

Historical backtest, replay, forward shadow, demo execution, and verified live execution are separate evidence classes under the [Public Evidence Policy](../governance/public-evidence-policy.md). They cannot be combined into one track record.

System operability, runner health, execution readiness, strategy edge, and public-user permission are separate claims.

Related documents:

- [Hydra Ecosystem](hydra-ecosystem.md)
- [Public Surface Registry](public-surface-registry.md)
- [Hydra Guardian](hydra-guardian.md)
- [Control Boundaries](control-boundaries.md)
- [State Model](state-model.md)
