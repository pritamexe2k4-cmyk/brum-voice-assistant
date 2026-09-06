# Brum — Workflow (developer view)

Status: **design only** until START. No app code yet.

## 1) Ingest

1. Authenticated user uploads PDF / MD / DOCX / TXT
2. Object store (local MinIO → S3 later) keeps the file
3. Async worker: page-aware chunk → embed → HNSW upsert into `kb_chunks` with `user_id`
4. Document status: `pending` → `indexing` → `ready` / `failed`

## 2) Text turn (prove RAG before voice)

1. Client sends text + `thread_id`
2. FastAPI invokes LangGraph with `user_id` + `thread_id`
3. Nodes: load_state → retrieve (pgvector, owner-scoped) → optional grade → generate (citations metadata) → respond
4. Stream tokens (SSE/NDJSON); LangSmith traces each node
5. Optional background: summarize session → `memory_facts`

## 3) Cascade voice turn (same graph)

1. Mic → MediaRecorder / WebAudio → upload or WS audio
2. **STT adapter** → text
3. **Same LangGraph** as text turn
4. **TTS adapter** → audio bytes → client playback
5. UI states: idle → listening → processing → speaking

## 4) Observe (MLOps lite)

- `LANGSMITH_TRACING=true`, project `brum-dev` / `brum-prod`
- Tag traces: `environment`, `user_id`, `session_id`, `voice=cascade`
- Golden Q&A eval set (20–50) for faithfulness / relevance / citation presence

## Scaling later

- Separate Redis/ARQ or Celery worker for ingest
- Connection pool on Postgres (`pre_ping`, `recycle`)
- Hybrid dense + `tsvector` retrieval
- Multi-tenant = nullable `org_id` (schema-ready, product later)
