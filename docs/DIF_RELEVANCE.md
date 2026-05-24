# DIF Relevance for EncryptVault

> **Canonical source**: [`/home/js/DIDzMonolith/monolith-docs/DIF_KNOWLEDGE_BASE.md`](/home/js/DIDzMonolith/monolith-docs/DIF_KNOWLEDGE_BASE.md)
>
> This file is a short pointer. The deep content (specs, ecosystem, integration patterns, anti-patterns) lives in the canonical knowledge base. Refresh this file only when EncryptVault's DIF needs materially change.

## Why DIF matters for EncryptVault

EncryptVault is a direct, perfect-fit candidate for DIF Confidential Storage. The spec exists precisely for products like this. Adopt it as the underlying data model rather than reinventing.

## DIF specs to adopt

- **Confidential Storage**: the canonical encrypted-data-vault spec, designed for products like EncryptVault
- **Decentralized Web Node (DWN)**: alternative or complementary data layer (Block and Web5 stack)
- **Fuzzy Encryption**: for human-recoverable vault unlock flows
- **DIDComm v2**: vault-to-vault sharing primitives

## Integration patterns from the canonical doc

- Pattern D (Confidential Storage for user-held data) — direct fit

## Concrete next steps

1. Audit the Confidential Storage spec against EncryptVault current data model.
2. Adopt the spec encrypted-data-vault format as the canonical vault layer.
3. Evaluate DWN as an interop target (so EncryptVault can read and write to other Web5 stacks).
4. Use Fuzzy Encryption for the human-recoverable unlock path.

## Last refreshed

May 24, 2026 from DIF homepage and GitHub org listing.
