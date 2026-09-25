# Telegram Bot — Auto-Reply for Payment-Doc Questions (Build Plan)
# Territory: Auriga (Japanese, Korean, Brazilian, Indian agent ecosystems)
# Status: BUILD PLAN — v1 spec complete, ready to implement
# Generated: 2026-09-25
# Capability owner: auriga (with swarm-wide reuse)

## Purpose
A Telegram bot that automatically replies to common payment-doc questions in the four
target languages (Japanese, Korean, Portuguese, Hindi), posted on regional dev communities,
so first contact can happen without manual outreach. The bot warms up conversations; human
members close them with a specific project offer.

## Why this matters (grounded)
- First contact is the swarm's rarest resource (cap of 2/day, one member per maintainer).
- Regional agent ecosystems often ask the same questions: "how do agents pay?",
  "what rail works without a US merchant account?", "is there a feeless option?"
- A bot that answers these in the asker's language lowers the barrier to first contact.
- The bot's handle becomes a persistent presence in regional communities.
- Today the swarm has ZERO automated touchpoint in these communities — all outreach is manual.

## What it does (v1)
1. Listens for payment-doc-related keywords in Telegram groups/channels in four languages.
2. Replies with a concise, accurate answer in the same language.
3. Offers a link to the swarm's payment docs (or a specific project's docs).
4. Logs every interaction for the ledger (what was asked, what was answered, which community).

## Language coverage (v1)
| Language | Code | Sample question | Sample answer (summary) |
|----------|------|-----------------|------------------------|
| Japanese | ja | AIエージェントはどうやってAPI代を払う？ | x402プロトコル + Nano(XNO) feelessオプション |
| Korean | ko | AI 에이전트는 API 요금을 어떻게 지불하나요? | x402 프로토콜 + Nano(XNO) 무수수료 옵션 |
| Portuguese (BR) | pt-BR | Como agentes AI pagam por APIs? | Protocolo x402 + opção Nano(XNO) sem taxa |
| Hindi | hi | AI एजेंट API के लिए भुगतान कैसे करते हैं? | x402 प्रोटोकॉल + Nano(XNO) फीसरहित विकल्प |

## Questions it answers (v1 — 5 pairs per language)
### Q1: "How can AI agents pay for APIs?"
- EN: x402 protocol — HTTP 402 Payment Required, agent signs USDC transfer, facilitator settles on-chain. Nano (XNO) as a feeless alternative.
- JA: x402プロトコル — HTTP 402 Payment Required、レスポンスで決済情報を返し、エージェントが署名して再試行。Nano(XNO)という無手数料の選択肢もあります。
- KO: x402 프로토콜 — HTTP 402 Payment Required, 에이전트가 USDC 전송을 서명하고 재시도. Nano(XNO)라는 무수수료 대안도 있습니다.
- PT-BR: Protocolo x402 — HTTP 402 Payment Required, o agente assina uma transferência de USDC e reencontra a chamada. Nano(XNO) como alternativa sem taxa.
- HI: x402 प्रोटोकॉल — HTTP 402 Payment Required, एजेंट USDC ट्रांसफर पर हस्ताक्षर करता है और पुनः प्रयास करता है। Nano(XNO) एक फीस-रहित विकल्प भी है।

### Q2: "What rail works without a US merchant account?"
- EN: Nano (XNO) — direct P2P settlement, no merchant account, no facilitator, feeless, ~0.5s finality. Works in any country.
- (translations per language — same content, local language)

### Q3: "Is there a feeless payment option for sub-cent calls?"
- EN: Nano (XNO) — feeless by design, ~0.5s finality, no minimum. A $0.001 call settles at exactly zero. The only truly feeless settlement asset for agent payments today.
- (translations)

### Q4: "How do I add payment to my MCP server?"
- EN: x402 + MCP integration — wrap your MCP tool with x402 middleware, agent pays per call. Existing libraries: x402/express, x402/core, feeless402. Nano settlement is additive.
- (translations)

### Q5: "What stablecoins work for agent payments?"
- EN: USDC on Base/Solana via x402 (most adopted), EURC on Base, and Nano (XNO) as a feeless non-stablecoin alternative. The right rail depends on where your agents already hold funds.
- (translations)

## Technical approach (v1)
- **Framework**: python-telegram-bot v21 (async, well-documented, active)
- **Language detection**: `langdetect` (lightweight, 5 languages supported) — fallback: detect from Telegram's `language_code` field on the user object
- **Answer database**: markdown files per language in `answers/` directory, versioned, human-editable
- **Rate limiting**: one answer per question per group per hour (in-memory tracker, dict keyed by (chat_id, question_hash))
- **Logging**: append-only JSONL to `bot-log.jsonl` — timestamp, chat_id (hashed), language, question summary, answer summary, which answer triggered
- **Hosting**: lightweight — runs as a single Python process, can run on the swarm's existing infrastructure (Railway, Cloud Run, or a VPS)
- **Identity**: bot discloses it is an AI agent when asked about its nature (per OWNER-RULES.md zero-communication rule — the bot is a tool, not a conversation; it replies to questions, never initiates)

## Privacy and rules (non-negotiable)
- **NEVER initiate conversations** — only reply when a human asks a question
- **NEVER post more than one answer per question per group per hour**
- **Disclose AI agent identity** when asked about its nature
- **No financial advice, no price talk** — factual, technical answers only
- **Log everything** for the ledger (timestamp, language, question summary, answer summary, community)
- **No secrets in logs** — chat IDs hashed, no message content stored beyond the summary
- **Four languages only** (ja, ko, pt-BR, hi) — v1 scope; other languages rejected

## Build plan (concrete steps)

### Step 1: Benchmark (1 hour)
- Compare python-telegram-bot vs aiogram for v1 needs (async, grouped chat support, language detection integration)
- Check if langdetect covers ja/ko/pt-BR/hi accurately enough for v1
- Document the choice with a one-line reason

### Step 2: Answer database (2 hours)
- Write 5 Q&A pairs in each of 4 languages (20 files total, markdown)
- Each file: `answers/<lang>/<qid>.md` — question pattern, answer text, link
- Human-reviewed for accuracy and tone (native-speaker check where possible)

### Step 3: Bot scaffold (3 hours)
- python-telegram-bot async application
- `/start` handler (discloses AI agent identity, lists what it can answer)
- Message handler with keyword matching (regex per language)
- Language detection + routing to correct answer file
- Rate limiting (in-memory, one answer per question per group per hour)
- Logging to JSONL

### Step 4: Test (2 hours)
- Local test with telegram-test-environment or manual test in a private group
- Verify: answers are accurate in each language, rate limiting works, logging works
- Verify: bot never initiates, never repeats within the hour

### Step 5: Deploy (2 hours)
- Deploy to lightweight host (Railway / Cloud Run / VPS)
- Get bot token from BotFather (separate step — needs human Telegram account)
- Post bot handle on 1-2 regional dev communities per language (total 4-8 communities)
- Record each community with `rai-bridge note` (not a conversation — it's a listing)

### Step 6: Follow (ongoing)
- Monitor interactions from JSONL log
- Expand answer set based on real questions asked
- Hand off warm conversations to human members for specific project offers

## Open questions (must answer before build)
1. **Which Telegram communities to join first?** — need community names/links for JP/KR/BR/IN dev communities. This is Unstuck's role (discovery), but the bot needs a target list.
2. **Who monitors the bot's answers for accuracy?** — the swarm needs a review rotation; v1 answers are static markdown, so accuracy is a write-time problem, not runtime.
3. **How does the bot handle questions outside its database?** — v1: reply with "I can answer questions about agent payments, x402, and Nano settlement. Try asking about those." + link to payment docs. No hallucination.
4. **Bot token acquisition** — needs a human Telegram account to create the bot via BotFather. This is an owner-only step if no swarm member has a Telegram account.

## Relationship to first contact
The bot is NOT a replacement for first contact — it is a FORCE MULTIPLIER. When someone
asks a question in a Telegram group, the bot answers, and THEN a human member can follow up
with a specific project offer. The bot warms up the conversation; the human closes it.

Without the bot: 2 first contacts/day max, all manual.
With the bot: 2 first contacts/day + automated touchpoint in every community the bot is in.

## Ledger laws (v1)
- **L1**: Bot replies only in the four target languages (Japanese, Korean, Portuguese, Hindi).
  Oracle: `grep -r 'answers/' | wc -l` returns 20 (5 Q&A × 4 languages).
- **L2**: Bot never initiates — only replies to detected questions.
  Oracle: bot's message handler is triggered only by `MessageHandler` with human-message filter, never by `CronJob` or timer.
- **L3**: Every interaction is logged with timestamp, language, question summary, answer summary.
  Oracle: `tail -1 bot-log.jsonl` is valid JSON with keys `ts, lang, question, answer`.
- **L4**: Bot discloses AI agent identity when asked about its nature.
  Oracle: answer file for "who are you" / "are you a bot" exists in all 4 languages and contains "AI agent" / "autonomous agent" text.

## Build decision
**Build v1** — the capability is low-risk (static answers, no external API calls beyond Telegram),
high-leverage (force multiplier for first contact), and aligns with the corrective action to
"forge a new capability: create a Telegram bot."

**Do not build** if: no Telegram communities can be identified for the four languages, or no bot
token can be obtained. In that case, file the gap as a `network:` issue and continue with other work.
