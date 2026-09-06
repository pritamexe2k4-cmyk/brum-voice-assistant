# Brum — Decisions Log

Updated: 2026-09-06 · Sources: Preetam + Researchy 2026 design / live report.

| ID | Decision | Choice | Why | Revisit when |
| --- | --- | --- | --- | --- |
| D1 | Voice architecture | **Cascade** STT → LangGraph → TTS first | Text seam for RAG, citations, LangSmith, adapters; resume story | Need full-duplex barge-in |
| D2 | LLM day-1 | **API** (Groq/OpenAI) | Reliable demos without GPU ops | Privacy / offline push |
| D3 | Local LLM | **Ollama adapter second** | Nice resume bullet; not MVP blocker | After cascade demo works |
| D4 | Host | **Docker Compose local first** | Prove RAG before cloud tax | Need shareable URL → Railway/VPS |
| D5 | Product spine | **Owned** FastAPI + LangGraph + pgvector + Next | Not Lovable/Supabase-as-product | Never for MVP |
| D6 | LiveKit / Pipecat | **Post-MVP transport only** | Must not become the brain | After M3 solid |
| D7 | Auth | FastAPI JWT (or Clerk if timeboxed) | Owned + `user_id` isolation | Shipping panic |
| D8 | Schema tenancy | `user_id` on docs/chunks from day 1; nullable `org_id` | Multi-tenant-ready without building orgs | Company product later |
| D9 | Cite-or-refuse | Softened for v1 — mixed KB + chat OK | Personal companion UX | Stricter enterprise mode |
| D10 | Accounts for MVP | Yes (auth) once build starts | Owner-scoped KB | — |
| D11 | Lovable scaffold | Archive / ignore | Rejected managed product path | Do not revive as spine |

## Explicit non-goals (MVP)

- Company multi-tenant brain
- MCP + Drive as required
- Phone / SIP
- Pure S2S as the only path
