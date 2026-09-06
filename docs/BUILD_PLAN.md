# Brum — Build Plan

**Gate:** Do **not** execute any milestone code until Preetam sends an explicit **START** signal. This file is the order of work only.

**Success criteria (end state):**  
Login → upload docs → text grounded answers with LangSmith traces → voice turn on the **same** graph → Docker runs locally → honest resume bullets.

**Out of MVP:** multi-tenant company, MCP/Drive, phone/SIP, pure S2S spine, Lovable lock-in.

---

## Milestones (execute only after START)

### M0 — Compose skeleton
- Docker Compose: Postgres+pgvector, empty FastAPI health, empty Next shell
- No real RAG/voice yet
- **Stop here until confirmed healthy**

### M1 — Auth + ingest + text RAG
- Auth + `user_id` schema
- Upload → chunk → embed → pgvector
- Text chat streaming with owner-scoped retrieval
- **Prove KB before adding voice**

### M2 — LangGraph + LangSmith
- Graph: retrieve → reason → respond
- Postgres checkpointer (`thread_id`)
- LangSmith tracing on every node

### M3 — Cascade voice UI
- Mic → STT adapter → **same graph** → TTS adapter
- Calm orb states: idle / listening / processing / speaking

### M4 — Polish + demo
- Adapter interfaces cleaned
- Eval dataset (20–50 Qs) + one eval script
- Public demo URL + README architecture diagram

### M5 — Stretch (optional)
- Ollama LLM adapter
- Thinking-filler UX during RAG latency
- Optional LiveKit duplex transport (graph still owned)

---

## Proceed order (checklist)

1. [ ] START signal from Preetam
2. [ ] M0 Compose skeleton
3. [ ] M1 Auth + upload + text RAG
4. [ ] M2 LangGraph + checkpointer + LangSmith
5. [ ] M3 Cascade voice UI
6. [ ] M4 Evals + deploy + diagram
7. [ ] M5 stretch only if time

## Rule

Docs and research may update anytime. **Application code** (FastAPI/Next/LangGraph implementation) waits for START.
