# Brum research log

**Updated:** 2026-09-06

## Direction (locked via Researchy 2026 design)

- Cascade STT → LangGraph → TTS first (not pure S2S day 1)
- LLM API first (Groq/OpenAI); Ollama adapter second
- Docker Compose locally first → VPS/Railway later
- Stack: FastAPI + LangGraph + LangSmith + Postgres/pgvector (`user_id` ready) + Next.js + adapters
- Pipecat/LiveKit = transport UX only, not the brain
- Steal patterns: LangGraph-RAG-Agent, agent-service-toolkit, rag_api; skip Lovable/Supabase-as-product

## Full reports

- [BRUM_2026_TECH_DESIGN.md](./BRUM_2026_TECH_DESIGN.md)
- [live-report.md](./live-report.md)

## Build order

1. Compose: Postgres+pgvector + FastAPI + Next shell
2. Auth + user_id schema
3. Ingest + text RAG
4. LangGraph + LangSmith
5. Cascade voice UI
6. Eval set + CI
7. Public demo URL

## Extra clone targets (Researchy live pass 2026-09-06)

| Repo | Stars (API ~2026-09-06) | Role |
| --- | --- | --- |
| [hosseinabadii/LangGraph-RAG-Agent](https://github.com/hosseinabadii/LangGraph-RAG-Agent) | 5 | **Primary blueprint** — FastAPI+LangGraph+pgvector+JWT+Compose |
| [JoshuaC215/agent-service-toolkit](https://github.com/JoshuaC215/agent-service-toolkit) | 4470 | Service packaging + LangSmith feedback |
| [danny-avila/rag_api](https://github.com/danny-avila/rag_api) | 891 | Ingest workers + owner-scoped retrieval |
| [ahmad2b/langgraph-voice-call-agent](https://github.com/ahmad2b/langgraph-voice-call-agent) | 47 | Post-MVP LiveKit adapter only |
| [dqbd/langgraph-livekit-agents](https://github.com/dqbd/langgraph-livekit-agents) | 82 | Post-MVP LiveKit adapter only |

## Session notes

- 2026-09-06: Rejected Lovable/Supabase product path; locked owned LC/LG/LS stack.
- 2026-09-06: Researchy design + live report absorbed; docs pack prepared; **no application code until Preetam START**.

## 2026-09-08 � RAGVoice runtime transported into Brum
- Copied local Desktop `RAGVoice-AI` engine into `brum-voice-assistant` (src, documents, vector_store, requirements).
- Goal: run the project under the **Brum** repo/name; UI/client can come later.
- `.env.local` not committed; use `.env.example`.
- Upstream reference: https://github.com/george07-t/RAGVoice-AI
