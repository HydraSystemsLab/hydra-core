# Hydra Ecosystem

Hydra Systems is the company and umbrella. Hydra Core is its public governance specification; private implementation surfaces remain separate from the public repository.

The canonical classification of named surfaces is the [Public Surface Registry](public-surface-registry.md). That registry, not the existence of private code, determines what public role may be claimed.

## Public And Private Shape

- **Hydra Core** publishes doctrine, architecture, governance, schemas, and operating expectations.
- **Hydra Quant** is the governed trading product/system under development, backed by private implementation.
- **Hydra Guardian** is the independent supervisory and risk authority governing private operation.
- **Hydra Predict** and **Hydra Ember** are private research labs without public product or execution claims.

Current external availability and public-user permissions live only in the dated [Public Operating Posture](../status/public-operating-posture.md).

## Why The Boundary Exists

Public documents should make authority, evidence standards, failure handling, and user permissions verifiable without publishing protected machinery. Private repositories may contain implementation, but they are not public evidence and are not proof of product availability.

Hydra Core does not publish:

- private strategy rules, parameters, thresholds, or model features
- credentials, account configuration, balances, or broker wiring
- private execution routes, request payloads, or protected schemas
- internal hosts, paths, logs, reports, datasets, or research artefacts

## Hydra Core

Hydra Core defines the durable public contract: control boundaries, state semantics, evidence classes, governance history rules, release discipline, and public/private separation. It is a specification, not a public trading implementation.

## Hydra Quant

Hydra Quant is a governed product under development. Engines may occupy research, `SHADOW`, `DEMO`, or `LIVE` modes only after explicit governed promotion within their authorized scope.

Strategy existence does not grant execution authority. Runner health does not grant strategy authority. Internal operational permission and public-user permission remain separate. See [Hydra Quant](hydra-quant.md) and the [private-alpha contract](../product/hydra-quant-private-alpha.md).

## Hydra Guardian

Hydra Guardian is the independent supervisory and risk authority. It can narrow permission, veto actions, require recovery, and prevent lower layers from overriding a stricter state. See [Hydra Guardian](hydra-guardian.md).

## Research Labs

Hydra Predict and Hydra Ember are research surfaces. Research output, model output, replay results, and promising observations do not create execution authority. Promotion requires explicit evidence, bounded authority, and governance review.

## Shared Doctrine

Across governed surfaces:

- trust, permission, lifecycle, and operating mode are independent
- missing or contradictory state fails closed
- observation can continue while execution is blocked
- mode promotion is a governance event, not an automatic response to results
- machine-learning components cannot acquire execution authority implicitly
- public-user permission cannot be inferred from private internal posture
- health and operability claims remain separate from edge and performance claims

The dated public posture may change. These boundaries do not silently change with it.
