# Brum — Interview Talking Points

Be honest. Prefer “designed and building” until Docker demo exists.

## One-liner

“I’m building Brum, a personal voice knowledge assistant: FastAPI + LangGraph RAG over Postgres/pgvector, modular STT/TTS/LLM adapters, LangSmith tracing, Docker Compose.”

## Concepts to own

| Concept | What you say |
| --- | --- |
| RAG | Chunk → embed → retrieve top-k → condition the LLM; owner-scoped vectors |
| LangGraph | Stateful graph (retrieve → reason → respond) with a Postgres checkpointer for `thread_id` |
| LangSmith | Trace every node; golden set for faithfulness / relevance; MLOps lite |
| Cascade vs S2S | Cascade for control + RAG + eval; S2S later as optional transport |
| Adapters | Swap free STT/TTS/LLM for premium without rewriting the graph |
| pgvector | HNSW index; same Postgres as app + checkpoints for simple ops |
| Eval | Offline LLM-as-judge on your PDFs; sample prod traces |

## Demo script (after START + M3)

1. `docker compose up`
2. Login → upload a PDF of your notes
3. Text question → show citations + LangSmith link
4. Same question by voice → STT → same graph → TTS
5. Show adapter file: “here’s where I’d plug Ollama”

## Do **not** claim

- Production multi-tenant company brain
- Sub-200ms pure S2S unless you measured it
- That you invented LangGraph
- Lovable/Supabase as the production architecture

## Resume bullet (honest template)

- Designing and building a personal voice knowledge assistant (FastAPI, LangGraph RAG, Postgres/pgvector, LangSmith, Docker); cascade STT→graph→TTS with swappable adapters.

Refresh to “built / shipped” only after M3+ demo URL exists.
