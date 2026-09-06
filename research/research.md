# Brum — project research log

Living notes: what happened, decisions, and useful links. Not a full transcript — enough to understand the project from start → now.

**Repo:** https://github.com/pritamexe2k4-cmyk/brum-voice-assistant  
**Last updated:** 2026-09-06 (IST)

---

## Timeline (short)

| When | What |
|------|------|
| ~early | Idea: company voice brain-dumps → shared KB → team voice assistant (not ChatGPT clone) |
| 2026-09-05 | Wiped old `production-rag` → README-only; renamed → `brum-voice-assistant` |
| 2026-09-05 | Resume: Brum link, drop Agentic Ops, IncluHub metrics |
| 2026-09-05 | Phase 1 research: top voice+KB repos, architecture, papers |
| 2026-09-05 | Locked **pure speech-to-speech** (not cascaded STT→LLM→TTS) |
| 2026-09-05 | Draft `PHASE1_PRP.md` for customize-and-return |
| 2026-09-06 | Lovable-style PRP interview; `research/research.md` created |
| 2026-09-06 | UX: ChatGPT-style voice + KB behind |
| 2026-09-06 | Features: mixed answers (chat+web+KB); no hard ground/refuse; uploads always; no transcript; voice-state animations |

---

## Product north star vs Phase 1 / MVP

**North star**
- Company people speak thoughts (brain dumps) into one shared knowledge base
- Team knowledge mixes; agent helps form aligned “company voice” / brand / dept memory
- Voice↔voice structure; better ideation; one guide agent so everyone understands

**Phase 1 / MVP (now)**
- Personal use first → friends group → companies → students/classes
- Pure speech-to-speech, ChatGPT-style UI, KB behind
- Answers may mix conversation + web search + KB (strict cite-or-refuse deferred)
- Upload docs always available (PDF + other formats)
- No transcript; interactive listening/thinking/speaking animations

**Still open**
- App vs website vs web-that-feels-like-app

---

## P0 features (locked so far)

1. Speech-to-speech talk loop (ChatGPT-style)
2. KB behind the scenes + **always-available uploads** (PDF + broad formats)
3. Mixed intelligence: basic chat + web + KB (no hard grounding requirement in v1)
4. Voice-state animations (idle / listening / processing / speaking) — no transcript UI
5. Personal single-user first

**Deferred:** strict refuse-when-not-in-KB; citation chips; multi-user company brain

---

## Architecture decisions

- **Voice:** pure speech-to-speech (Realtime-style); tools for KB search + web search
- **Not primary:** cascaded Whisper → LLM → TTS
- **Grounding:** soft for v1 (mixed sources OK); strict mode later for company
- **Spine:** browser/app mic → WebRTC → S2S model ↔ tools (search_kb, web) → spoken reply + UI animations
- **UX:** ChatGPT Voice front; uploads/settings for KB

---

## Key repo links (study / steal patterns)

1. https://github.com/livekit/agents
2. https://github.com/pipecat-ai/pipecat
3. https://github.com/openai/openai-realtime-agents
4. https://github.com/Mintplex-Labs/anything-llm
5. https://github.com/SalesforceAIResearch/VoiceAgentRAG
- Brum: https://github.com/pritamexe2k4-cmyk/brum-voice-assistant
- PRP: https://github.com/pritamexe2k4-cmyk/brum-voice-assistant/blob/main/PHASE1_PRP.md
- This log: https://github.com/pritamexe2k4-cmyk/brum-voice-assistant/blob/main/research/research.md

---

## Papers / eng reads

| Topic | Link |
|-------|------|
| RAG foundation (Lewis 2020) | https://arxiv.org/abs/2005.11401 |
| Self-RAG (Asai 2023) | https://arxiv.org/abs/2310.11511 |
| ALCE citations (Gao 2023) | https://arxiv.org/abs/2305.14627 |
| Citation faithfulness | https://arxiv.org/abs/2412.18004 |
| RALM refuse | https://arxiv.org/abs/2509.01476 |
| VoiceAgentRAG | https://arxiv.org/abs/2603.02206 |
| Enterprise realtime voice agents | https://arxiv.org/abs/2603.05413 |
| Whisper | https://arxiv.org/abs/2212.04356 |
| LiveKit voice architecture | https://livekit.com/blog/voice-agent-architecture-stt-llm-tts-pipelines-explained |
| AssemblyAI voice architecture | https://www.assemblyai.com/blog/voice-agent-architecture |

---

## Session notes

### 2026-09-05
- Repo wipe/rename; S2S research; PHASE1_PRP draft; resume Brum link.

### 2026-09-06
- PRP interview: vision, users, ChatGPT-style + KB behind.
- Softened grounding: mixed chat/web/KB OK for v1.
- Uploads always on (all formats); no transcript; need processing animations.
- Awaiting platform pick (web / native app / web-feels-app).

---

## Next

- Lock platform
- Continue PRP (AI/tech, auth, data, design vibe, inspirations, future)
- Generate final Lovable PRD prompt
