# Brum — Workflow (developer view)

## Happy path
1. User signs in  
2. Uploads PDF/MD → ingest job chunks + embeds → `pgvector`  
3. Opens voice UI → mic → STT  
4. LangGraph nodes: load history → retrieve → (optional tools) → generate → TTS  
5. LangSmith records each node (latency, inputs/outputs)  
6. Session summary may write long-term facts

## Scaling later
- Separate worker for ingest  
- Connection pool on Postgres  
- Cache hot embeddings  
- Rate-limit LLM calls per user  
- Multi-tenant = row-level `user_id` / `org_id` on KB tables
