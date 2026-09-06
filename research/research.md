# Brum — project research log

Living notes: what happened, decisions, and useful links. Not a full transcript — enough to understand the project from start → now.

**Repo:** https://github.com/pritamexe2k4-cmyk/brum-voice-assistant  
**Last updated:** 2026-09-06 ~11:07 IST

---

## Timeline

| When | What |
|------|------|
| 2026-09-05 | Repo wipe/rename; S2S research; PHASE1_PRP |
| 2026-09-06 | Lovable PRP interview completed |
| 2026-09-06 | Final `LOVABLE_PRD_PROMPT.md` generated |
| 2026-09-06 | Lovable project created (Brum Voice Companion) — editor: https://lovable.dev/projects/5bb6c568-2c3d-41f2-b984-d37a31b0faed — preview: https://id-preview--5bb6c568-2c3d-41f2-b984-d37a31b0faed.lovable.app |
| 2026-09-06 ~10:21–~11:05 IST | **First build COMPLETED** (msg `umsg_01m1tgxcvremvvts1tzs9fsrvr`, commit `a459b1c2…`, ~10.6 credits). Voice shell + KB live. |
| 2026-09-06 ~10:32–~11:06 IST | **Logo integration COMPLETED** (msg `umsg_01m1th063heccrse12tkfj7nt7`, commit `bfbaa323…`, ~1.7 credits). Favicon + header orb mark applied. |

### First build — what shipped
- Full-screen calm dark UI with interactive pulse orb (idle / listening / processing / speaking)
- Tap-to-toggle + hold-to-talk mic UX; no chat transcript panel
- Knowledge drawer: upload PDFs/Word/text → chunk + `pgvector` embeddings
- End-to-end pipeline: STT → context-aware reasoning (KB + Wikipedia/DuckDuckGo) → TTS
- Supabase-backed storage for files/metadata; anonymous, no auth

### Logo message — what shipped
- Saved `public/brum-logo.png`, favicon.png, apple-touch-icon.png
- Cropped orb asset in header beside wordmark (`mix-blend-screen`)
- Dark minimal aesthetic preserved; central orb remains primary UI

---

## Locked v1 decisions

| Area | Choice |
|------|--------|
| Product | Personal S2S voice + KB behind (not ChatGPT clone) |
| UX | ChatGPT/Grok-style talk; minimal calm orb/waveform; no transcript |
| Answers | Mix chat + web + KB |
| Uploads | Always on; PDF + broad formats |
| Platform | App-like web |
| Auth | None |
| Social | User ↔ Brum only |
| Models | Modular free/basic → premium later |
| Data | RAG ≠ memory (uploads, identity, session, summaries, user facts) |
| Inspirations | ChatGPT Voice, Grok Voice, S2S+KB+persona |

## Future (not v1)

Friends → company → students; strict ground/refuse; premium Realtime; auth; **MCPs + Google Drive** for easy access; Notion.

## Key links

- https://github.com/pritamexe2k4-cmyk/brum-voice-assistant
- https://github.com/pritamexe2k4-cmyk/brum-voice-assistant/blob/main/LOVABLE_PRD_PROMPT.md
- https://github.com/pritamexe2k4-cmyk/brum-voice-assistant/blob/main/PHASE1_PRP.md
- Lovable editor: https://lovable.dev/projects/5bb6c568-2c3d-41f2-b984-d37a31b0faed
- Lovable preview: https://id-preview--5bb6c568-2c3d-41f2-b984-d37a31b0faed.lovable.app
- https://github.com/livekit/agents · https://github.com/pipecat-ai/pipecat · https://github.com/openai/openai-realtime-agents · https://github.com/Mintplex-Labs/anything-llm · https://github.com/SalesforceAIResearch/VoiceAgentRAG
