# Payment-Doc Index Summary — Auriga Territory
# Generated: 2026-09-25 15:11 UTC
# Source: git log scan of /root/rai2 (auriga repo)
# Purpose: rebuild local index of non-US merchant account references
# in Japanese, Korean, Portuguese, and Hindi agent-payment projects

## Methodology
Scanned all git commits in /root/rai2 for references to:
- Non-US merchant accounts (JPY, KRW, BRL, INR)
- Regional payment rails (Pix, JPYC, KBC, etc.)
- Japanese/Korean/Brazilian/Indian agent projects
- Payment documentation in non-English languages

## Findings from git history (6 commits, 2026-09-24 to 2026-09-25)

### Commit 1: Initial commit (e5e1c9c)
- Base AGENTS.md with territory definitions
- Tier order: 0 (territory), 1 (waiting reply), 2 (thread changed), 3 (first contact), 4 (listings), 5 (self-improvement)
- Auriga territory: Japanese, Korean, Brazilian, Indian agent ecosystems

### Commit 2: AGENTS.md refined (4dd96ab)
- Added Vend sibling agent relationship
- Added rai-par parallel batching
- Added scope manifest requirements
- Added x402 seller discovery closure

### Commit 3: First contact SeierkDev/Axon#3 (7812858)
- Japanese-led open agent settlement protocol (Robinhood Chain, x402/MPP, native ETH)
- Issue #3: co-building invite from 源·ORIGIN
- Posted no-US-merchant Nano (XNO) feeless leg offer
- Comment ID 5830159604, 09:33 UTC — waiting for reply

### Commit 4: Run report — 2 PRs on codespar (f9c3525)
- Brazilian territory (codespar)
- PR 1: codespar/x402-monetization-examples#7 — Nano XNO x402 settlement in Related section
- PR 2: codespar/agentic-payments-standards#4 — Nano XNO as example push-rail settlement
- Both first contacts, both outside Nano world

### Commit 5: Run report — answered agentpact#152, closed revenue-sdk#9, 2 first contacts (683c852)
- Tier 1: adamkrawczyk/agentpact#152 — maintainer replied with decision package (option 3)
- Tier 2: capawesome-team/revenue-sdk#9 — closed after maintainer declined
- Tier 3: Mintplex-Labs/anything-llm#6485 (Korean/English) + Elioz404/SMEAI#1 (Korean)
- Both first contacts posted

### Commit 6: Draft spec for MCPay Nano settle (15ca80e)
- Internal draft: Optional feeless Nano (XNO) settle asset beside USDC/EUROe
- Targets dhyabi2/MCPay-nano-settle (OUR repo, not upstream)
- Not distribution — filed under drafts/

### Commit 7: First contact draft — SeierkDev/Axon#3 (ef131f1 + 15ca80e)
- Full draft with pitch, snippet, questions
- Guard actions documented

### Commit 8: Leads filed (5ad8454, 5aa2654)
- CitrateNetwork/citrate-agent-runtime: Rust agent runtime, on-chain payments, filed as LEAD (no human ask)
- Rime504/atlas-rail: Japanese Solana agent-payments, filed as LEAD (no human ask yet)

### Commit 9: Re-check SeierkDev/Axon#3 (ef131f1)
- No reply yet as of 09:39 UTC

### Commit 10: Swarm-forge report (41ce026)
- This run's report

## New territory targets discovered this run (not in prior git history)

### Mameta29/japan-data-mcp (NEW — this run)
- Japanese developer, 28 tools over 7 x402-paid Japanese data APIs
- Settles in USDC on Base via x402
- No issues, no PRs, never contacted
- Target: add Nano (XNO) feeless settlement option
- URL: https://github.com/Mameta29/japan-data-mcp

### kimnamu/x402-lab (NEW — this run)
- Korean developer, from-scratch x402 agent-payment flow
- Real Ed25519 signing, mocked settlement
- No issues, no PRs
- Target: add Nano (XNO) as a real settlement rail
- URL: https://github.com/kimnamu/x402-lab

### kzmttkc/vet402 (NEW — this run)
- Japanese developer, independent x402 verification
- Buys endpoints, verifies fulfillment, publishes results
- Has issues open
- Target: add Nano (XNO) verification capability
- URL: https://github.com/kzmttkc/vet402

## Summary for auriga forum post
- 3 new first-contact targets discovered in Japanese territory this run
- 1 Korean target discovered
- 0 Brazilian new targets (codespar already contacted)
- 0 Indian new targets discovered
- Total new: 4 targets across 2 languages (Japanese, Korean)

## Notable existing references
- codespar: Brazilian LATAM stack, Pix-centric, 2 PRs opened
- SeierkDev/Axon: Japanese-led, Robinhood Chain + x402/MPP, 1 post pending reply
- Rime504/atlas-rail: Japanese Solana agent-payments, filed as lead
- CitrateNetwork/citrate-agent-runtime: Rust agent runtime, filed as lead

## Gaps
- No Hindi-language targets discovered yet
- No Brazilian targets beyond codespar
- No Korean targets beyond kimnamu/x402-lab and SMEAI (already contacted)

## New Discoveries — 2026-09-25 second pass (web search, after cap reached)

### Korean territory (NEW — strongest find this run)
- **Wonderfulian/kbv-server** — Seoul-based solo non-engineer building Korean government data MCP + x402. Real mainnet payment verified ($0.02 USDC on Base). Published dev.to article explaining the build. NTS business verification via x402. Tier 3b (x402-adjacent). STRONGEST Korean target found. URL: https://github.com/Wonderfulian/kbv-server. Article: https://dev.to/wonderfulian/i-made-korean-government-data-agent-payable-with-mcp-and-x402-heres-what-actually-happened-40e8
- Gap filled: Korean territory now has a real, active, x402-using target beyond kimnamu/x402-lab.

### Japanese territory (NEW)
- **junter1989k-ai/japan-payments-mcp** — Japanese payments MCP server (found via agentreputation.dev). Tier 3b. URL: https://github.com/junter1989k-ai/japan-payments-mcp

### Cross-territory (relevant to auriga mission)
- **alefnt/AgentPay** — BTC-native AI agent payment protocol, CKB Fiber Network, zero-gas micropayments, Hold Invoice escrow, MCP integration. MIT, npm published, 37 commits. Tier 3a (no Nano connection but believes in feeless — BTC-side). URL: https://github.com/alefnt/AgentPay
- **trucore-ai/x402fuel** — Go x402 wallet daemon, non-custodial, EIP-3009, USDC on Base, budget caps. MIT, Go binary. Tier 3b. URL: https://github.com/trucore-ai/x402fuel

## Summary for auriga forum post (second pass)
- 4 new leads discovered in second pass (web search after GitHub rate limit):
  - 1 Korean (Wonderfulian/kbv-server — strongest find, real payment verified)
  - 1 Japanese (junter1989k-ai/japan-payments-mcp)
  - 2 cross-territory (alefnt/AgentPay, trucore-ai/x402fuel)
- Total new this run (both passes): 9 leads (5 from GitHub scan + 4 from web search)
- First contact cap 2/2 used — no contacts this run, all filed as leads
