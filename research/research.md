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
| 2026-09-06 | Lovable-style PRP interview started (vision, users, flows) |
| 2026-09-06 | This log file created (`research/research.md`) — update every Brum session |

---

## Product north star vs Phase 1 / MVP

**North star**
- Company people speak thoughts (brain dumps) into one shared knowledge base
- Team knowledge mixes; agent helps form aligned “company voice” / brand / dept memory
- Voice↔voice structure; better ideation; one guide agent so everyone understands

**Phase 1 / MVP (now)**
- Personal use first (Preetam)
- Then friends group → later multi groups/companies → students/classes
- Knowledge-based **speech-to-speech** assistant you can talk to about *that* KB (+ some external knowledge later)
- Not another ChatGPT; grounded in your corpus; cite or refuse

**Open (PRP interview)**
- App vs website (leaning: responsive web / app-like for v1)
- Flow style choice pending: NotebookLM sources-first / ChatGPT Voice / AnythingLLM cites / mix

---

## Architecture decisions

- **Voice:** pure speech-to-speech (Realtime-style); RAG via `search_kb` (or similar) tool mid-call
- **Not primary:** cascaded Whisper → LLM → TTS (kept as fallback only if needed)
- **Grounding:** retrieve → answer from chunks or refuse; UI citations from tool results
- **Spine sketch:** browser mic → WebRTC → S2S model ↔ search_kb → vector KB → spoken reply

---

## Key repo links (study / steal patterns)

### Top picks (Phase 1)
1. https://github.com/livekit/agents — WebRTC voice agents; RAG examples
2. https://github.com/pipecat-ai/pipecat — voice pipeline framework; RAG examples
3. https://github.com/openai/openai-realtime-agents — Realtime + tools / Chat-Supervisor (~7k★)
4. https://github.com/Mintplex-Labs/anything-llm — uploads → workspace RAG → citations (~66k★)
5. https://github.com/SalesforceAIResearch/VoiceAgentRAG — voice RAG latency / prefetch cache

### Also useful
- https://github.com/Barty-Bart/openai-realtime-api-voice-assistant-V2 — Realtime + RAG demo
- https://github.com/open-webui/open-webui — RAG UI scale (heavy)
- https://github.com/zylon-ai/private-gpt — private KB API (no voice)
- Brum itself: https://github.com/pritamexe2k4-cmyk/brum-voice-assistant
- PRP draft: https://github.com/pritamexe2k4-cmyk/brum-voice-assistant/blob/main/PHASE1_PRP.md

---

## Papers / eng reads

| Topic | Link |
|-------|------|
| RAG foundation (Lewis 2020) | https://arxiv.org/abs/2005.11401 |
| Self-RAG (Asai 2023) | https://arxiv.org/abs/2310.11511 |
| ALCE citations (Gao 2023) | https://arxiv.org/abs/2305.14627 |
| Citation faithfulness | https://arxiv.org/abs/2412.18004 |
| RALM refuse / know-when-don’t-know | https://arxiv.org/abs/2509.01476 |
| VoiceAgentRAG paper | https://arxiv.org/abs/2603.02206 |
| Enterprise realtime voice agents tutorial | https://arxiv.org/abs/2603.05413 |
| Whisper STT | https://arxiv.org/abs/2212.04356 |
| LiveKit STT/LLM/TTS architecture | https://livekit.com/blog/voice-agent-architecture-stt-llm-tts-pipelines-explained |
| AssemblyAI voice agent architecture | https://www.assemblyai.com/blog/voice-agent-architecture |
| Voice RAG / KB craft (eng) | https://www.dilr.ai/blog/voice-ai-knowledge-base-rag-architecture-enterprise |

---

## Product flow references (for UX)

| Product | Flow gist | Steal |
|---------|-----------|-------|
| ChatGPT Voice | Open → talk ↔ listen → transcript in chat | Frictionless S2S loop |
| NotebookLM | Upload sources → ask grounded notebook | Sources-first KB |
| AnythingLLM | Workspace upload → chat + citation chips (+ optional voice) | Cite UX / workspace |
| Perplexity Voice | Speak → hear answer + see citations | Speak + verify sources on screen |

---

## Session notes

### 2026-09-05
- Repo wipe + rename done; remote only README then PRP.
- Research pack: voice+KB architecture; prefer S2S + tool RAG for Phase 1.
- Resume updated for Brum URL (PDF rebuild still TBD).

### 2026-09-06
- Morning hunt digest paused (unrelated ops).
- Started Lovable-style PRP Q&A: pitch, problem (company single brain), users (personal → friends → companies → students).
- User stuck on app vs web + journey → showed 4 reference flows; awaiting A/B/C/D (or mix).
- Request: keep appending this `research/research.md` every Brum chat.

---

## Next (when Preetam answers)

- Pick flow style (A NotebookLM / B ChatGPT Voice / C AnythingLLM / D mix)
- Lock web vs app for v1
- Finish PRP → paste into Lovable / scaffold
