# Public Surface Registry

This registry defines the public classification of named Hydra Systems surfaces. It is an allowlist for public product claims, not an inventory of every internal experiment.

## Classifications

| Classification | Meaning |
| --- | --- |
| Public governance surface | Public doctrine, architecture, schemas and policy |
| Product under development | Intended for future external use but not necessarily available |
| Governed private surface | Private implementation governed by Core |
| Research lab | Experimental surface without a public product claim |
| Archived/quarantined | No active promotion claim |

## Registered Surfaces

| Surface | Public role | Implementation visibility | Classification | Source of truth | External availability | Explicit non-claim |
| --- | --- | --- | --- | --- | --- | --- |
| Hydra Core | Public governance and architecture specification | Public documents and schemas | Public governance surface | [README](../README.md) | Public reference repository | Not trading software and not proof of private-system availability |
| Hydra Quant | Governed trading product/system under development | Private implementation; public contract only | Product under development | [Hydra Quant](hydra-quant.md) | Private-alpha preparation; see [public posture](../status/public-operating-posture.md) | No public-user broker connection, order submission, or live execution |
| Hydra Guardian | Independent supervisory and risk authority for governed private systems | Private implementation; public authority model only | Governed private surface | [Hydra Guardian](hydra-guardian.md) | Not offered as a public product | Not a strategy, signal generator, or proof of safety or profit |
| Hydra Predict | Experimental prediction-domain research | Private | Research lab | [Hydra Predict](hydra-predict.md) | No public availability claim | No public product, execution, or promotion claim |
| Hydra Ember | Experimental market-scanning research | Private | Research lab | [Hydra Ember](hydra-ember.md) | No public availability claim | No public trading product or execution authority |

## Registry Rules

- A private implementation is not evidence that a public product is available.
- A named surface does not acquire execution authority through inclusion here.
- Changing external availability belongs in the dated [public operating posture](../status/public-operating-posture.md), not this durable registry.
- Adding a surface requires an owner-reviewed public role, source-of-truth document, visibility classification, availability statement, and explicit non-claim.
- Internal project names are not added merely because they exist.

Absence from this registry does not prove that no other internal research exists. It means no public role or product claim is made here.
