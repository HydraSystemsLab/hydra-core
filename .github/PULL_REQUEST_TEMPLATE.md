# Pull Request

## Summary

Describe the public contract change and why it is needed.

## Change Classification

- [ ] Editorial
- [ ] Clarifying governance
- [ ] Governance
- [ ] Architecture-significant
- [ ] Security hardening

## Required Impact Review

### Public/Private Review

- [ ] No private strategy logic, parameters, credentials, accounts, paths, endpoints, logs, payloads, schemas, or protected research is exposed.
- [ ] Synthetic examples are unmistakably labelled.

### Dynamic-Posture Impact

- [ ] No changing posture is introduced outside the canonical Markdown and JSON posture records.
- [ ] Posture records were updated together, or this change has no posture impact.

### Evidence-Claim Impact

- [ ] Evidence tier, metadata, limitations, and claim boundary are correct, or this change makes no evidence claim.
- [ ] Health, readiness, edge, and user permission remain separate claims.

### State-Model Impact

- [ ] Trust, permission, lifecycle, and mode remain independent.
- [ ] The execution invariant and restrictive precedence remain intact.

### Ledger Impact

- [ ] Ledger impact was assessed under the ledger policy.
- [ ] No event facts, identifiers, timestamps, transitions, or evidence were invented.

**Reviewed interval:**

Choose exactly one disposition:

- [ ] Event drafted
- [ ] Event deferred with reason
- [ ] Event excluded by policy
- [ ] No ledger impact

Keep protected event facts out of the pull request until public/private review
is complete.

### Security Impact

- [ ] Security and disclosure impact was reviewed.
- [ ] Sensitive findings were reported privately, not included here.

## Validation

List commands run and their exact results.

## Screenshots Or Concept Media

Provide public-safe, clearly labelled conceptual media, or state `N/A`. Do not attach real account or private-alpha material without review.

## Linked Issue

Link the public issue, or explain why an issue was not required. Never link a public security disclosure.

## Release-Note Impact

Describe release-note and migration impact, or state `None`.

## Final Checks

- [ ] Internal links and anchors resolve.
- [ ] JSON and examples validate against their schemas.
- [ ] No unlabeled placeholder or fake screenshot is present.
- [ ] No guaranteed-return or unsupported performance wording is introduced.
- [ ] No tag, release, merge, or auto-merge action is part of this PR.
