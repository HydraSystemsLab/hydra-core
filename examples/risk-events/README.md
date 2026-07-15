# Synthetic Risk Event Examples

Every JSON file in this directory is a **synthetic, sanitized documentation example**. The examples are not historical events, do not describe an account or engine, and must not be copied into the public ledger as facts.

They demonstrate:

- required structured-V1 fields
- independent state axes
- evidence classification
- the current-authorization disclaimer
- strict public-safe extensions

The deliberately old example dates are arbitrary teaching values, not Hydra history. Each file carries `x-example-only: true` and a public summary beginning with “Synthetic example”.

Validate them with:

```bash
/usr/bin/python3 scripts/validate_public_surface.py --check schemas
```

See the [Risk Event Schema](../../governance/risk-event-schema.md) and [Ledger Policy](../../governance/risk-event-ledger-policy.md).
