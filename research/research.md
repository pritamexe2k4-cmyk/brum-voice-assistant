# Brum — project research log

Living notes: what happened, decisions, and useful links. Not a full transcript — enough to understand the project from start → now.

**Repo:** https://github.com/pritamexe2k4-cmyk/brum-voice-assistant  
**Last updated:** 2026-09-06 (IST)

---

## Timeline

| When | What |
|------|------|
| 2026-09-05 | Repo wipe/rename; S2S research; PHASE1_PRP |
| 2026-09-06 | Lovable PRP interview completed |
| 2026-09-06 | Final `LOVABLE_PRD_PROMPT.md` generated |
| 2026-09-06 | Lovable project created (Brum Voice Companion) — editor: https://lovable.dev/projects/5bb6c568-2c3d-41f2-b984-d37a31b0faed — preview: https://id-preview--5bb6c568-2c3d-41f2-b984-d37a31b0faed.lovable.app — first build status: **running** (agentFinished=false after ~10min poll) |

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
