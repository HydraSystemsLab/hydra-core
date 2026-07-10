# Contributing

Hydra Core accepts focused public contributions to doctrine, architecture, governance, evidence standards, schemas, examples, and documentation quality.

This repository does not solicit private strategy code, broker wiring, credentials, account configuration, operational logs, protected research, or executable trading functionality.

## Before Opening A Change

Use a public issue first for governance-bearing changes so scope and public wording can be reviewed before implementation. Do not use a public issue for security or sensitive material; follow [SECURITY.md](SECURITY.md).

Documentation corrections and small non-semantic fixes may proceed directly to a pull request.

## Accepted Scope

- clarity and consistency improvements
- failure-mode and threat-model coverage
- public-safe evidence and schema improvements
- tests for documentation validation
- link, navigation, accessibility, and workflow hardening
- well-supported governance questions

There is no promise that external strategies, signals, models, data, or execution integrations will be accepted.

## Public/Private Rules

Never submit:

- strategy rules, protected thresholds, parameters, or model features
- credentials, tokens, accounts, balances, or broker configuration
- private paths, hosts, endpoints, repository URLs, reports, or logs
- order payloads, private schemas, or execution wiring
- actionable real-time entries or exits
- unverified current engine status or unsupported performance claims

Use synthetic, sanitized examples. If in doubt, withhold the detail and explain the governance concept.

## Branch And Pull Request Conventions

- branch from the latest clean `main`
- use a focused descriptive branch name
- do not rewrite shared history or mix unrelated changes
- make logical commits with concise imperative messages
- complete the pull request template
- leave owner decisions, licensing, and sensitive operational changes explicit

## Required Review Checks

### Change Classification

Select the highest class from the [Versioning Policy](governance/versioning-policy.md): editorial, clarifying governance, governance, architecture-significant, or security hardening.

### Dynamic-Posture Check

Changing product stage, availability, user mode, or permission belongs only in both canonical posture records. Evergreen architecture must not carry changing engine status.

### Evidence-Claim Check

Name the evidence tier, claim, sample, limitations, and provenance required by the [Public Evidence Policy](governance/public-evidence-policy.md). Do not merge tiers or infer edge from health.

### Ledger-Impact Check

Use the [Risk Event Ledger Policy](governance/risk-event-ledger-policy.md). Do not invent an event to accompany a documentation change.

### State-Model Check

Keep trust, permission, lifecycle, and mode independent. Preserve the full execution invariant and restrictive precedence.

## Local Validation

Use an isolated public toolchain; do not rely on private project environments.

```bash
/usr/bin/python3 -m venv .venv
.venv/bin/python -m pip install --requirement requirements-docs.txt
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/validate_public_surface.py --check all
.venv/bin/python scripts/validate_public_surface.py --check external
npm ci --ignore-scripts
npx --no-install markdownlint-cli2 "**/*.md" "#node_modules"
git diff --check
```

The external-link check requires network access and uses bounded retries and timeouts.

## Licensing

No reuse license has been published. Contributions do not create or imply a license, CLA, DCO, or transfer of rights. Licensing is an owner decision and should be resolved before accepting contributions that require clear reuse terms.
