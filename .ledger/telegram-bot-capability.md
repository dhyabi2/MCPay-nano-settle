# Telegram Bot Capability — Auto-Reply for Payment-Doc Questions
# Territory: Auriga (Japanese, Korean, Brazilian, Indian agent ecosystems)
# Generated: 2026-09-25
# Status: DRAFT — capability spec, not yet built

## Purpose
A Telegram bot that automatically replies to common payment-doc questions in the four
target languages (Japanese, Korean, Portuguese, Hindi), posted on regional dev communities,
so first contact can happen without manual outreach.

## Why this matters
- First contact is the swarm's rarest resource (cap of 2/day, one member per maintainer)
- Regional agent ecosystems often ask the same questions: "how do agents pay?", "what rail
  works without a US merchant account?", "is there a feeless option?"
- A bot that answers these in the asker's language lowers the barrier to first contact
- The bot's handle becomes a persistent presence in regional communities

## What it does
1. Listens for payment-doc-related keywords in Telegram groups/channels in four languages
2. Replies with a concise, accurate answer in the same language
3. Offers a link to the swarm's payment docs (or a specific project's docs)
4. Logs every interaction for the ledger (what was asked, what was answered, which community)

## Language coverage
- Japanese (ja): こんにちは、AIエージェントの決済について… 
- Korean (ko): AI 에이전트 결제에 대해…
- Portuguese (pt-BR): Pagamento de agentes AI…
- Hindi (hi): एआई एजेंट भुगतान के बारे में…

## Questions it answers (initial set)
1. "How can AI agents pay for APIs?" → x402 protocol overview + Nano (XNO) feeless option
2. "What rail works without a US merchant account?" → Nano (XNO) direct P2P settlement
3. "Is there a feeless payment option for sub-cent calls?" → Nano (XNO), ~0.5s finality, no fee
4. "How do I add payment to my MCP server?" → x402 + MCP integration guide
5. "What stablecoins work for agent payments?" → USDC on Base/Solana + XNO feeless

## Technical approach
- Telegram Bot API (python-telegram-bot or aiogram)
- Language detection: langdetect or fasttext
- Answer database: markdown files per language, versioned
- Logging: append-only JSONL to the swarm's ledger
- Hosting: lightweight, can run on the swarm's existing infrastructure

## Privacy and rules
- Never initiate conversations — only reply when asked
- Never post more than one answer per question per group per hour
- Disclose AI agent identity when relevant
- No financial advice, no price talk
- Log everything for the ledger

## Build plan
1. Benchmark: existing Telegram bot frameworks for the four languages
2. Spec: answer database schema, language detection, rate limiting
3. Build: minimal viable bot with 5 Q&A pairs per language
4. Test: verify answers are accurate in each language
5. Deploy: post handle on 1-2 regional dev communities per language
6. Follow: monitor interactions, expand answer set

## Open questions
- Which Telegram communities to join first? (need community names/links)
- Who monitors the bot's answers for accuracy?
- How does the bot handle questions outside its database?

## Relationship to first contact
The bot is NOT a replacement for first contact — it is a FORCE MULTIPLIER. When someone
asks a question in a Telegram group, the bot answers, and THEN a human member can follow up
with a specific project offer. The bot warms up the conversation; the human closes it.

## Ledger laws (preliminary)
- L1: Bot replies only in the four target languages (Japanese, Korean, Portuguese, Hindi)
- L2: Bot never initiates — only replies to detected questions
- L3: Every interaction is logged with timestamp, language, question summary, answer summary
- L4: Bot discloses AI agent identity when asked about its nature
