# Brum — project research log

Living notes: what happened, decisions, and useful links. Not a full transcript — enough to understand the project from start → now.

**Repo:** https://github.com/pritamexe2k4-cmyk/brum-voice-assistant  
**Last updated:** 2026-09-06 (IST)

---

## Timeline (short)

| When | What |
|------|------|
| ~early | Idea: company voice brain-dumps → shared KB → team voice assistant |
| 2026-09-05 | Wiped `production-rag` → `brum-voice-assistant`; S2S research; PHASE1_PRP |
| 2026-09-06 | PRP interview; research log; ChatGPT-style + KB behind |
| 2026-09-06 | Features: mixed chat/web/KB; uploads always; no transcript; animations |
| 2026-09-06 | Platform: **C — web that feels like an app** |
| 2026-09-06 | Voice models: **modular**; free/basic first → premium after MVP pipeline |

---

## Product north star vs Phase 1 / MVP

**North star:** company brain-dumps → shared KB → one voice guide agent  
**MVP:** personal ChatGPT-style S2S; KB behind; mixed answers; upload always; animations; **app-like web**; **free/modular models**

**Scale ladder:** you → friends group → companies → students/classes

---

## Locked decisions

| Area | Choice |
|------|--------|
| Voice | Pure speech-to-speech *feel*; providers modular |
| Models | Free/basic for MVP; swap to premium later without rewrite |
| UX | ChatGPT-style; KB silent behind |
| Answers | Mix conversation + web + KB (strict ground/refuse later) |
| Uploads | Always available; PDF + broad formats |
| Transcript | No |
| UI motion | Idle / listening / processing / speaking |
| Platform | Web that feels like an app |
| Users v1 | Single person (Preetam) |
| Auth | Open (A private link vs B Supabase login) |

---

## Architecture (working)

- Mic → WebRTC → **swappable** voice adapters (free STT/LLM/TTS or free Realtime-class) ↔ tools (search_kb, web) → audio + animations
- Design for provider interfaces so premium Realtime/ElevenLabs/etc. plug in later
- Uploads/storage: lean Supabase (or equiv)
- Front: Lovable/React full-screen voice UI

Note: true premium S2S may need paid keys; free path may be cascaded free STT→LLM→TTS behind the same UI until upgrade.

Refs: livekit/agents · pipecat · openai-realtime-agents · anything-llm · VoiceAgentRAG  
Log: https://github.com/pritamexe2k4-cmyk/brum-voice-assistant/blob/main/research/research.md

---

## Session notes — 2026-09-06

- No paid keys now → modular free/basic models; premium after pipeline works.
- Awaiting auth (A/B), then data / social / vibe / inspirations / future.

---

## Next

- Auth pick
- Data, multiplayer?, design vibe, inspirations, future
- Generate Lovable PRD prompt
