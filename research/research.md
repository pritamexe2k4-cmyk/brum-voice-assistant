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
| 2026-09-06 | Modular free→premium; no auth; data model (RAG vs memory) |
| 2026-09-06 | Social: **user ↔ Brum only** in v1 |

---

## Locked decisions

| Area | Choice |
|------|--------|
| Voice / models | S2S feel; modular free→premium |
| UX | ChatGPT-style; KB behind; animations; no transcript UI |
| Answers | Mix chat + web + KB |
| Uploads | Always on; PDF + broad formats (+ images into KB when supported) |
| Platform | App-like web |
| Auth | None |
| Social v1 | **User ↔ Brum only** (no user-to-user) |
| Design vibe | Open |

---

## Data model (locked for v1)

RAG (docs) ≠ Memory (conversations). Persist: uploads + chunks/embeddings, system identity, session working memory (no transcript UI), session summaries, light semantic user facts; images via uploads when supported.

---

## Architecture (working)

Mic → WebRTC → swappable free voice adapters ↔ tools (search_kb, web, memory) → audio + animations

Log: https://github.com/pritamexe2k4-cmyk/brum-voice-assistant/blob/main/research/research.md

---

## Next

- Design vibe → inspirations → future features → Lovable PRD prompt
