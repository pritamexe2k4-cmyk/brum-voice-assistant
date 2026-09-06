# Brum — project research log

Living notes: what happened, decisions, and useful links. Not a full transcript — enough to understand the project from start → now.

**Repo:** https://github.com/pritamexe2k4-cmyk/brum-voice-assistant  
**Last updated:** 2026-09-06 (IST)

---

## Timeline (short)

| When | What |
|------|------|
| 2026-09-05 | Repo wipe/rename; S2S research; PHASE1_PRP |
| 2026-09-06 | PRP interview through social + data model |
| 2026-09-06 | Design: **minimal / calm (A)** |

---

## Locked decisions

| Area | Choice |
|------|--------|
| Voice / models | S2S feel; modular free→premium |
| UX | ChatGPT-style talk; KB behind; no transcript UI |
| Answers | Mix chat + web + KB |
| Uploads | Always on; PDF + broad formats |
| Platform | App-like web |
| Auth | None |
| Social v1 | User ↔ Brum only |
| Design vibe | **Minimal / calm** — dark, quiet, orb/soft waveform states |
| Inspirations | Open |

---

## Data model (v1)

RAG ≠ memory. Persist uploads+embeddings, identity, working session, summaries, light user facts.

---

## Architecture

Mic → WebRTC → swappable free adapters ↔ tools → audio + calm state animations

Log: https://github.com/pritamexe2k4-cmyk/brum-voice-assistant/blob/main/research/research.md

---

## Next

- Inspirations → future features → Lovable PRD prompt
