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

---

## Product north star vs Phase 1 / MVP

**North star:** company brain-dumps → shared KB → one voice guide agent  
**MVP:** personal ChatGPT-style S2S; KB behind; mixed answers; upload always; animations; **app-like web**

**Scale ladder:** you → friends group → companies → students/classes

---

## Locked decisions

| Area | Choice |
|------|--------|
| Voice | Pure speech-to-speech |
| UX | ChatGPT-style; KB silent behind |
| Answers | Mix conversation + web + KB (strict ground/refuse later) |
| Uploads | Always available; PDF + broad formats |
| Transcript | No |
| UI motion | Idle / listening / processing / speaking |
| Platform | Web that feels like an app (full-screen voice shell) |
| Users v1 | Single person (Preetam) |

---

## Architecture (working)

- Mic → WebRTC → Realtime S2S model ↔ tools (search_kb, web) → audio out + state animations
- Uploads/storage: lean Supabase (or equiv) for files + metadata
- Front: Lovable/React full-screen voice UI

Refs: livekit/agents · pipecat · openai-realtime-agents · anything-llm · VoiceAgentRAG  
Log: https://github.com/pritamexe2k4-cmyk/brum-voice-assistant/blob/main/research/research.md

---

## Session notes — 2026-09-06

- Chose platform **C** (web feels like app).
- Next: tech confirmation, auth, data, social?, vibe, inspirations, future → final Lovable PRD.

---

## Next

- Confirm AI/tech lean
- Auth / data / design / inspirations / future features
- Generate Lovable PRD prompt
