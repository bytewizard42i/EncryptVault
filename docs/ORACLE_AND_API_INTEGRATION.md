# Oracle Pattern & API Integration Guide — EncryptVault

> How external data gets into Midnight smart contracts, and which free APIs are relevant to EncryptVault (secure seed phrase & key storage).

---

## Why Smart Contracts Can't Call APIs Directly

Midnight smart contracts (Compact) run inside **zero-knowledge proof circuits**. Every node must get the exact same result. External API calls are non-deterministic, which breaks proofs. Instead, we use the **oracle pattern**: a trusted off-chain service feeds data into the chain.

```
┌──────────────┐      ┌──────────────────┐      ┌─────────────────────┐
│ External API │ ───> │  Oracle Service   │ ───> │  Midnight Contract  │
│ (Blockchain) │      │  (Your Backend)   │      │  (Compact / ZK)     │
└──────────────┘      └──────────────────┘      └─────────────────────┘
                        Signs attestation         Verifies signature
                        Packages wallet proof     Stores: "wallet active"
                        Strips private keys       Never sees secrets
```

| Layer | Can call APIs? |
|-------|---------------|
| **Frontend / Express server** | ✅ Yes |
| **Midnight contract (Compact)** | ❌ No — oracle pattern required |

---

## Recommended Free APIs for EncryptVault

### Blockchain & Wallet Data

| API | Description | Auth | URL |
|-----|-------------|------|-----|
| **Etherscan** | Ethereum explorer — balances, txn history, token holdings | apiKey | https://etherscan.io/apis |
| **Covalent** | Multi-chain data aggregator (Ethereum, Polygon, BSC, etc.) | apiKey | https://www.covalenthq.com |
| **The Graph** | Blockchain indexing via GraphQL queries | apiKey | https://thegraph.com |
| **Nownodes** | Blockchain-as-a-service — node access for 50+ chains | apiKey | https://nownodes.io |
| **Watchdata** | Ethereum blockchain API access | apiKey | https://docs.watchdata.io |
| **Bitquery** | On-chain GraphQL APIs & DEX data | apiKey | https://graphql.bitquery.io |

### Cryptocurrency Pricing

| API | Description | Auth | URL |
|-----|-------------|------|-----|
| **CoinGecko** | Crypto prices, market cap, volume — 10K+ coins | None | https://www.coingecko.com/en/api |
| **CoinCap** | Real-time crypto market data | None | https://coincap.io |
| **Exchangerate.host** | Forex + crypto exchange rates | None | https://exchangerate.host |

### Security & Breach Detection

| API | Description | Auth | URL |
|-----|-------------|------|-----|
| **HaveIBeenPwned** | Check if credentials were in a data breach | apiKey | https://haveibeenpwned.com |
| **GitGuardian** | Scan for exposed secrets (API keys, credentials) | apiKey | https://api.gitguardian.com |
| **EmailRep** | Email address threat scoring | None | https://emailrep.io |

---

## EncryptVault-Specific Oracle Use Cases

### 1. Wallet Activity Proof
```
[Etherscan API] → [Oracle: "wallet has 3 txns in 30 days"] → [Contract: "wallet active"]
                                                                Proves: wallet is in active use
                                                                Reveals: nothing about balance or txns
```

### 2. Multi-Chain Portfolio Attestation
```
[Covalent multi-chain] → [Oracle: "assets across 4 chains"] → [Contract: "diversified portfolio"]
                                                                 Proves: user has multi-chain presence
                                                                 Reveals: no balances, no addresses
```

### 3. Seed Phrase Backup Verification
```
[User submits encrypted backup hash] → [Oracle: "hash matches stored backup"] → [Contract: "backup verified"]
                                                                                   Proves: backup exists and is current
                                                                                   Reveals: nothing about the seed phrase
```

### 4. Compromised Key Detection
```
[GitGuardian + breach DBs] → [Oracle: "no exposure found"] → [Contract: "keys secure"]
                                                                Proves: no known leaks of this key
                                                                Reveals: nothing about the key itself
```

---

## Critical Security Note

EncryptVault deals with the most sensitive data in crypto — seed phrases and private keys.

- **NEVER** send seed phrases or private keys to any external API
- **NEVER** store unencrypted secrets on-chain (even Midnight's shielded state)
- The oracle pattern for EncryptVault only attests **facts about** keys, never the keys themselves
- All encryption/decryption happens **client-side only**

---

## demoLand vs realDeal

| Mode | How APIs are used |
|------|-------------------|
| **demoLand** | Mock wallet data, simulated balances. No real API calls. No real keys. |
| **realDeal** | Oracle calls Etherscan/Covalent for wallet attestations. Client-side encryption only. Zero secrets leave the user's device. |

---

## Reference

- Public APIs catalog: https://github.com/public-apis/public-apis
- Midnight docs: https://docs.midnight.network
- EncryptVault architecture: See `README.md` in this repo
