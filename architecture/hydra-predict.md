# Hydra Predict

Hydra Predict is a private prediction-market research and execution architecture governed by Hydra Core doctrine.

It is described publicly as an operating surface, not as a public implementation.

## Purpose

Hydra Predict exists to study and operate prediction-market workflows under strict supervision.

Its first obligation is truth.
If venue state, quote state, or promotion state cannot be reconciled, the system should not treat action as safe.

## What It Is

Hydra Predict focuses on:

- venue truth
- quote reconciliation
- strict paper/live separation
- shadow monitoring
- operator-controlled promotion

It is built around the idea that truth comes before action.
A signal is not enough if the system cannot prove the venue and operating state behind it.

## Operating Posture

Hydra Predict is research-first.

Paper, shadow, and live states must remain clearly separated.
Promotion is an operator-controlled governance decision, not an automatic consequence of a promising result.

## What Is Not Public

Hydra Predict does not publish credentials, private venue configuration, funding-specific material, executable request formats, or live operating procedures.

The public docs describe the boundary.
They do not expose implementation wiring.

## Relationship To Core

Hydra Core defines the doctrine that Predict must follow:

- fail closed on ambiguous state
- reconcile truth before action
- preserve paper/live separation
- promote only when evidence and controls justify promotion
- keep the operator responsible for live authority

Related documents:

- [Hydra Ecosystem](hydra-ecosystem.md)
- [Control Boundaries](control-boundaries.md)
- [State Model](state-model.md)
- [Risk Doctrine](../doctrine/risk-doctrine.md)
