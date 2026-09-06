# Brum — project research log

Living notes: what happened, decisions, and useful links. Not a full transcript — enough to understand the project from start → now.

**Repo:** https://github.com/pritamexe2k4-cmyk/brum-voice-assistant  
**Last updated:** 2026-09-06 (IST)

---

## Timeline (short)

| When | What |
|------|------|
| 2026-09-05 | Repo wipe/rename; S2S research; PHASE1_PRP |
| 2026-09-06 | PRP: ChatGPT-style + KB behind; mixed answers; animations; app-like web |
| 2026-09-06 | Modular free→premium models; no auth |
| 2026-09-06 | **Data model locked** (RAG vs memory tiers) |

---

## Locked decisions

| Area | Choice |
|------|--------|
| Voice / models | S2S feel; modular free→premium |
| UX | ChatGPT-style; KB behind; animations; no transcript UI |
| Answers | Mix chat + web + KB |
| Uploads | Always on; PDF + broad formats (+ images into KB when supported) |
| Platform | App-like web |
| Auth | None (private project) |
| Social v1 | Likely user↔Brum only (confirming) |

---

## Data model (locked for v1)

Keep **RAG (documents)** and **Memory (conversations)** separate.

| Store | Contents | v1 |
|-------|----------|-----|
| Document KB | Uploaded files, chunks, embeddings | Yes |
| System identity | Persona, rules, tool/config | Yes |
| Short-term / working | Current session turns (RAM / session) | Yes — not shown as transcript |
| Long-term episodic | Session **summaries** after calls | Yes |
| Long-term semantic | Small “about user” facts | Yes |
| Images/media | Via upload pipeline into KB | Yes if format OK; no album product |
| Web result cache | — | No v1 |
| Full chat history UI | — | No (memory summaries only) |

Refs: RAG vs memory (HydraDB / Mem0-style split); Redis agent-memory tiers; voice programme memory (session vs cross-call).

---

## Architecture (working)

Mic → WebRTC → swappable free voice adapters ↔ tools (search_kb, web, memory read/write) → audio + animations  
Storage: files + vector chunks + memory summaries + identity config

Log: https://github.com/pritamexe2k4-cmyk/brum-voice-assistant/blob/main/research/research.md

---

## Next

- Confirm social (user↔Brum only)
- Design vibe, inspirations, future features
- Generate Lovable PRD prompt
