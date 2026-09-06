# Brum research log

**Updated:** 2026-09-06

## Direction (locked via Researchy 2026 design)

- Cascade STT → LangGraph → TTS first (not pure S2S day 1)
- LLM API first (Groq/OpenAI); Ollama adapter second
- Docker Compose locally first → VPS later
- Stack: FastAPI + LangGraph + LangSmith + Postgres/pgvector (`user_id` ready) + Next.js + adapters
- Pipecat/LiveKit = transport UX only, not the brain
- Steal patterns: openarg_backend, home-generative-agent; skip Lovable/Supabase-as-product

## Full report

See [BRUM_2026_TECH_DESIGN.md](./BRUM_2026_TECH_DESIGN.md)

## Build order

1. Compose: Postgres+pgvector + FastAPI + Next shell
2. Auth + user_id schema
3. Ingest + text RAG
4. LangGraph + LangSmith
5. Cascade voice UI
6. Eval set + CI
7. Public demo URL
