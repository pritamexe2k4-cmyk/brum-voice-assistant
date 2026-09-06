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
| 2026-09-06 | PRP interview; ChatGPT-style + KB behind; mixed answers; animations |
| 2026-09-06 | Platform C (app-like web); modular free→premium models |
| 2026-09-06 | Auth: **none** — private project, no accounts |

---

## Locked decisions

| Area | Choice |
|------|--------|
| Voice | S2S *feel*; providers modular |
| Models | Free/basic MVP → premium later |
| UX | ChatGPT-style; KB behind |
| Answers | Mix chat + web + KB |
| Uploads | Always on; PDF + broad formats |
| Transcript | No |
| UI motion | Idle / listening / processing / speaking |
| Platform | Web that feels like an app |
| Users v1 | Single person |
| Auth | **No accounts** (private link / local project) |
| Data | Open — likely files + embeddings + light settings |

---

## Architecture (working)

- Mic → WebRTC → swappable free voice adapters ↔ tools (search_kb, web) → audio + animations
- No user auth layer in v1
- Storage for uploads/embeddings only (Supabase or local/simple)
- Front: Lovable/React full-screen voice UI

Log: https://github.com/pritamexe2k4-cmyk/brum-voice-assistant/blob/main/research/research.md

---

## Session notes — 2026-09-06

- Auth = none for now.
- Next: confirm data scope, then social / vibe / inspirations / future → Lovable PRD.

---

## Next

- Confirm stored data
- Multiplayer? design vibe, inspirations, future features
- Generate Lovable PRD prompt
