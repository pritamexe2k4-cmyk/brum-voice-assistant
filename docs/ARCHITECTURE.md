# Brum — Architecture

Status: **planned**. No runtime code in repo yet.

## Voice path: cascade (locked)

```
Browser (Next.js dark orb UI)
  mic MediaRecorder / WebAudio
       │  HTTPS / WS audio
FastAPI
  /auth  /docs  /ingest  /chat  /voice/turn  /health
       │
  STT adapter ──► LangGraph turn
                    retrieve(pgvector) → generate → (tools)
       │
  TTS adapter ──► audio bytes to client
       │
  LangSmith traces
Postgres 16: users | documents | chunks+embeddings | checkpoints | memory_facts
Worker: ingest jobs
MinIO (local) → S3 later
```

**Why cascade for MVP:** text seam at every stage → RAG, citations, LangSmith, swappable free→premium adapters. Pure S2S / LiveKit duplex is **post-MVP transport**, not the product brain.

## Graph nodes (MVP turn)

1. `load_state` — `thread_id`, `user_id`, short history (Postgres checkpointer)
2. `retrieve` — dense pgvector (+ optional BM25/`tsvector` later), filter by `user_id`
3. `grade` (optional) — drop junk chunks
4. `generate` — LLM + citation metadata
5. `speak` — TTS adapter (outside or final node)
6. `summarize_async` — session summary / long-term facts (background)

## Adapters (interfaces)

- `STTAdapter.transcribe(audio, mime) -> str`
- `TTSAdapter.synthesize(text, voice) -> bytes`
- `LLMAdapter` used inside LangGraph
- `EmbeddingProvider.embed(texts) -> vectors`

MVP defaults: API LLM (Groq/OpenAI); Faster-Whisper / Groq Whisper / Deepgram free tier for STT; Edge-TTS / OpenAI TTS / Deepgram Aura for TTS. Ollama as **second** LLM adapter.

## Planned monorepo tree (create on START — not present yet)

```
brum-voice-assistant/
  apps/
    web/                 # Next.js voice UI + auth
    api/                 # FastAPI
  packages/
    shared/              # OpenAPI types / zod (optional)
  docker-compose.yml     # api, web, postgres, minio, worker, redis
  docs/
  research/
  evals/
  README.md

apps/api/app/
  main.py
  routers/               # auth, docs, voice, health
  graphs/                # LangGraph definitions
  nodes/                 # retrieve, generate, summarize
  adapters/              # llm, stt, tts, embeddings
  db/                    # models, pgvector SQL, Alembic
  workers/               # ingest
  evals/                 # LangSmith dataset scripts
```

## Clone targets (patterns to steal)

| Repo | Steal |
| --- | --- |
| [hosseinabadii/LangGraph-RAG-Agent](https://github.com/hosseinabadii/LangGraph-RAG-Agent) | Primary FastAPI+LangGraph+pgvector+JWT+Compose blueprint |
| [JoshuaC215/agent-service-toolkit](https://github.com/JoshuaC215/agent-service-toolkit) | Service packaging + LangSmith feedback |
| [danny-avila/rag_api](https://github.com/danny-avila/rag_api) | Ingest workers + owner-scoped retrieval |
| LiveKit / Pipecat LangGraph adapters | **Post-MVP** transport only |

See [research/live-report.md](../research/live-report.md) for the full table.
