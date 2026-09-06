# Brum — Schema (design only)

No migrations in repo yet. Create on START (M1).

## Principles

- Every KB row carries `user_id` (and nullable `org_id` for later)
- One Postgres 16 + pgvector for app data, vectors, and LangGraph checkpoints
- Never trust client-supplied ids alone — scope queries by auth subject

## Tables (sketch)

### `users`
- `id` (uuid PK)
- `email` (unique)
- `password_hash` or external subject
- `created_at`

### `documents`
- `id` (uuid PK)
- `user_id` (FK, indexed)
- `org_id` (nullable)
- `filename`, `mime`, `storage_uri`
- `status` (`pending` | `indexing` | `ready` | `failed`)
- `error` (nullable)
- `created_at`, `updated_at`

### `kb_chunks`
- `id` (uuid PK)
- `document_id` (FK)
- `user_id` (FK, indexed) — denormalized for fast filters
- `org_id` (nullable)
- `chunk_index`, `content`, `page` (nullable)
- `embedding` `vector(N)` — N matches embedding model
- HNSW index on `embedding`

### `memory_facts` (long-term)
- `id`, `user_id`, `thread_id` (nullable), `fact`, `created_at`

### LangGraph checkpoints
- Managed by `langgraph-checkpoint-postgres` / `AsyncPostgresSaver` schemas
- Always pass `thread_id` (+ `user_id` in metadata)

### Jobs (optional MVP)
- `ingest_jobs`: `id`, `document_id`, `user_id`, `status`, `attempts`, timestamps

## RPC / query pattern

`match_kb_chunks(query_embedding, match_count, p_user_id)` — **must** filter `user_id = p_user_id`.
