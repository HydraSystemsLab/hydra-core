# Release Posture

Hydra Core is pre-v1 by design.
This repository exists to stabilize the public governance surface before any later v1 decision.

## Scope

`hydra-core` is the public repository for:

- architecture
- doctrine
- governance
- operating expectations

It is not a public software distribution.
It does not publish private implementation code.

## Public And Private Boundary

Hydra is described publicly as related but distinct layers:

- Hydra Core as the public governance and architecture surface
- Hydra Quant as the private strategy and execution environment
- Hydra Guardian as the private supervisory and enforcement layer behind Hydra Quant

Public documents in this repository describe the operating model and control expectations around those layers.
They do not imply that Hydra Quant or Hydra Guardian are publicly available.

## What Pre-v1 Means Here

Pre-v1 means the public governance language is still being tightened and stabilized.
It does not mean the governance model is optional.

During pre-v1:

- terminology may still be refined for clarity
- document structure may still be improved
- governance coverage may expand where important failure classes need clearer treatment

What should remain stable even before v1:

- risk-first doctrine
- fail-closed bias
- the separation between replaceable strategies and non-optional enforcement
- the requirement that recovery follow verification

## What V1 Would Mean Later

A future v1 would mean the public governance surface has become stable enough to serve as a durable reference for serious operators and builders.
It would not mean:

- the strategy stack is finished
- private systems have become public
- experimentation inside private strategy environments has ended

V1 would describe stability of public architecture and governance meaning, not finality of private implementation.
