# Public Surface Registry

This registry defines the approved public hierarchy for Hydra Systems. It is an
allowlist for public claims, not an inventory of private implementation or
research.

## Hierarchy

| Surface | Public role | Visibility | External availability | Explicit non-claim |
| --- | --- | --- | --- | --- |
| Hydra Systems | Trading-infrastructure operation and umbrella for independent traders and small prop desks | Public company surface | Infrastructure enquiries only | Not a signal vendor, performance claim, or grant of system access |
| Hydra Quant | Proprietary systematic-trading platform under development | Private implementation; public contract only | Defined only by the dated [public posture](../status/public-operating-posture.md) | No implied broker connection, order submission, or live-execution authority |
| Hydra Guardian | Supervisory and risk authority within Hydra Quant | Private implementation; public authority model only | Not offered as a standalone public product | Not a strategy, signal generator, or proof of safety or profit |
| Hydra Guard | Standalone risk-protection tool for MetaTrader 5 traders, separate from Hydra Quant and Hydra Guardian | Product in development | Not yet available; launch will be announced on [hydrasystems.tech](https://hydrasystems.tech) | Not a strategy or signal generator; does not guarantee compliance with any firm's rules or prevent all losses |
| Hydra Core | Public governance and failure-control specifications for Hydra Systems trading infrastructure | Public documents and schemas | Public reference repository | Not trading software and not proof of private-system availability |

## Naming: Guard And Guardian

**Hydra Guardian** is the internal supervisory authority inside Hydra Quant and
is not sold. **Hydra Guard** is a separate product for MetaTrader 5 traders.
They share design principles, not code, authority or availability.

## Registry Rules

- A private implementation is not evidence that a public product is available.
- A named surface does not acquire execution authority through inclusion here.
- Changing availability belongs in the dated [Public Operating Posture](../status/public-operating-posture.md).
- Public hierarchy changes require owner review and a source-of-truth update.
- Internal experiments and research names are not public products or registered
  merely because they exist.

Anything absent from this registry has no approved public product role or
availability claim.
