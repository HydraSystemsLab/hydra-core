# Security Policy

Hydra Core is a public governance specification with documentation schemas, validation tooling, and workflow configuration. Security reports relevant to this repository and its public/private boundary are welcome.

## Report Privately

Never report a vulnerability, credential, secret, account detail, private path, endpoint, log, payload, or protected implementation detail in a public issue, pull request, discussion, or commit.

The current verified private contact route is [audit@hydrasystems.tech](mailto:audit@hydrasystems.tech). Use the subject prefix `SECURITY: hydra-core`.

This is the existing general Hydra Systems inquiry mailbox. Repository owners should confirm that it remains monitored for coordinated security reports before this prerelease leaves draft. GitHub private vulnerability reporting has not been verified and is not claimed as a reporting route.

## Relevant Scope

Examples include:

- a secret or protected detail exposed in repository content or history
- a validator bypass that permits prohibited private material or dynamic posture
- unsafe workflow permissions, untrusted-code execution, or dependency behavior
- a schema or example that could cause consumers to interpret stale or permissive state as current
- a public/alpha payload or authorization design issue that risks cross-user or private-data leakage
- a documentation defect that materially misstates security, authority, recovery, or public-user permission

Private strategy requests, trading performance disagreements, and general product feedback are not security reports.

## Information To Provide

Where safe, include:

- affected repository file, commit, or public surface
- concise impact and affected boundary
- reproducible steps using synthetic or redacted data
- whether any secret or protected data may already be exposed
- suggested containment if known
- a safe private contact for follow-up

Do not send active credentials when a redacted description is enough. If sensitive evidence is necessary, ask for handling instructions first.

## Response And Coordination

Hydra Systems will acknowledge and assess reports when practical, coordinate containment and disclosure according to risk, and preserve reporter communication where possible. No fixed response or remediation service level is promised.

Please allow time for containment before public disclosure. A correction may be released without publishing exploit details, secrets, or private implementation.

## Supported Public-Governance Versions

Hydra Core is pre-v1 and has no published software release. Security corrections target the current `main` governance contract and any explicitly identified active prerelease candidate. Historical snapshots and the existing freeze tag are records, not promises of ongoing security updates.

## No Bounty Promise

No bug bounty, payment, safe-harbor program, or reward is promised by this policy. Any future program requires separate owner-approved terms.
