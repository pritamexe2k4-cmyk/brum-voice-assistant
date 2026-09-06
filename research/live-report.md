# Project Brum — Live Research Report

**Product:** Personal Voice Knowledge Assistant (resume showcase for AI Engineer roles)  
**Access date:** ~2026-09-06 (UTC; IST = UTC+5:30)  
**Method:** Live WebSearch, WebFetch, and GitHub MCP (`search_repositories`, `search_code`, `get_file_contents`) only. Stars/stats below are exactly what the GitHub API returned on this date — do not treat as cached training data.

**Uncertainty flag:** Vendor latency/cost figures vary by region, model, and measurement method. Prefer “architectural direction” over exact ms claims unless you benchmark Brum yourself.

---

## 1. Similar open-source repos

Closest fits for **voice + RAG** and/or **LangGraph + FastAPI + pgvector**. Prefer FastAPI+LangGraph alignment. LiveKit/Pipecat noted only where they plug without forcing platform lock-in.

### A. Closest stack matches (steal patterns)

| Repo | Stars (API ~2026-09-06) | Stack | Steal | Skip |
|------|-------------------------|-------|-------|------|
| [hosseinabadii/LangGraph-RAG-Agent](https://github.com/hosseinabadii/LangGraph-RAG-Agent) | **5** | FastAPI + LangGraph ReAct + Postgres/pgvector + JWT auth + Streamlit + Docker; async ingest; Postgres checkpointer | **Primary blueprint.** Thread-scoped RAG, JWT user isolation, NDJSON streaming (`llm_chunk` / `tool_call` / `tool_result`), `langchain-postgres`, Docker Compose with `pgvector/pgvector:pg16` | Streamlit UI (Brum wants Next.js); no voice |
| [JoshuaC215/agent-service-toolkit](https://github.com/JoshuaC215/agent-service-toolkit) | **4,470** | LangGraph + FastAPI service + Streamlit client + Docker + Postgres checkpointers + LangSmith feedback + Ollama docs + basic Chroma RAG | Service layout (`agents/`, `service/`, `client/`), streaming protocol, Docker watch, multi-agent routing, LangSmith star feedback, AG-UI option | Streamlit default UI; Chroma not pgvector; voice is secondary |
| [danny-avila/rag_api](https://github.com/danny-avila/rag_api) | **891** | FastAPI + LangChain + Postgres/pgvector; batched async embedding; JWT-scoped retrieval; multi-embed provider (OpenAI/Ollama/HF/…) | Production ingest workers: batch size, queue, parallel consumers, owner-scoped deletes, pool pre-ping/recycle | Not LangGraph; LibreChat-oriented; no voice |
| [StabRise/scaledp-chat](https://github.com/StabRise/scaledp-chat) | **9** | FastAPI + LangGraph/LangChain + PGVector + SQLAlchemy + Alembic + Poetry + Docker + Vercel AI SDK frontend notes | Monorepo hygiene: Alembic, settings prefix, CI, structured `web/api` | Niche ScaleDP domain; small community |
| [mazzasaverio/fastapi-langchain-rag](https://github.com/mazzasaverio/fastapi-langchain-rag) | **53** | FastAPI + LangChain LCEL + PGVector | Minimal RAG API skeleton | Older LCEL patterns; no LangGraph/voice |

**README sources:** fetched via GitHub `get_file_contents` for LangGraph-RAG-Agent, agent-service-toolkit, rag_api, scaledp-chat (~2026-09-06).

### B. Voice + LangGraph (optional later; not MVP core)

| Repo | Stars | Stack | Steal | Skip / risk |
|------|-------|-------|-------|-------------|
| [ahmad2b/langgraph-voice-call-agent](https://github.com/ahmad2b/langgraph-voice-call-agent) | **47** | LiveKit Agents + LangGraph adapter + Deepgram STT/TTS + Silero VAD; RemoteGraph to `langgraph dev` | How to wrap a compiled graph as LiveKit LLM; thread_id via participant metadata; local LiveKit Compose | LiveKit infra + worker model; phone/SIP adjacent — **out of MVP scope** if it becomes the product spine |
| [dqbd/langgraph-livekit-agents](https://github.com/dqbd/langgraph-livekit-agents) | **82** | LangGraphAdapter → LiveKit VoicePipelineAgent | Minimal adapter pattern (messages stream → ChatChunks) | Thin demo; LiveKit-centric |
| [livekit/agents](https://github.com/livekit/agents) | **14,028** | Official realtime voice agent framework | Reference for VAD/STT/TTS orchestration if you add duplex later | Platform gravity; Brum should own FastAPI graph first |
| [pipecat-ai/pipecat](https://github.com/pipecat-ai/pipecat) | **15,256** | Open-source voice/realtime framework (Daily + community) | Adapter ideas for cascading STT→LLM→TTS without rewriting graph | Easy to become the app; keep as optional transport later |
| [dograh-hq/dograh](https://github.com/dograh-hq/dograh) | **5,589** | Self-hosted voice platform (Pipecat-based); S2S or cascade; telephony | Study BYOK / cascade vs S2S product design | Multi-tenant/telephony — explicitly **out** for Brum MVP |
| Official LiveKit LangChain plugin write-up | n/a | [livekit.com/blog/langchain-to-livekit](https://livekit.com/blog/langchain-to-livekit) | `LLMAdapter` needs Pregel graph with `messages` key | Don’t redesign Brum around LiveKit for resume MVP |

### C. Voice + RAG (non-LangGraph; pattern only)

| Repo | Stars | Notes |
|------|-------|-------|
| [Adii2202/RAG-AI-Voice-assistant-](https://github.com/Adii2202/RAG-AI-Voice-assistant-) | **48** | Voice-to-voice RAG assessment; steal UX flow ideas, not architecture |
| [ebongard/renfield](https://github.com/ebongard/renfield) | **38** | Self-hosted assistant + RAG + voice satellites; heavy / offline-oriented |
| [ShayneP/livekit-rag-thinking](https://github.com/ShayneP/livekit-rag-thinking) | **20** | Demo of filling silence during RAG latency — steal “thinking filler” UX |

### D. Framework / reference (cite, don’t clone as product)

| Repo | Stars | Use for Brum |
|------|-------|--------------|
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | **41,109** | Core orchestration |
| [mayooear/ai-pdf-chatbot-langchain](https://github.com/mayooear/ai-pdf-chatbot-langchain) | **16,593** | Classic PDF RAG + LangGraph (archived; Next.js) — UX inspiration only |
| [google-gemini/gemini-fullstack-langgraph-quickstart](https://github.com/google-gemini/gemini-fullstack-langgraph-quickstart) | **18,327** | Fullstack agent shape |

**Takeaway for Brum:** No single high-star repo is “FastAPI + LangGraph + pgvector + ChatGPT-Voice UI.” Closest greenfield clone target is **LangGraph-RAG-Agent** (backend) + **agent-service-toolkit** (service packaging) + **custom Next.js cascade voice** (your differentiator). Treat LiveKit/Pipecat as a **post-MVP transport**, not the MVP.

---

## 2. Architecture: Cascade STT→LangGraph→TTS vs Realtime S2S

### Definitions

- **Cascade:** Audio → STT (text) → LangGraph retrieve→reason→respond (text) → TTS → audio. Text exists at every boundary.
- **Realtime S2S:** Audio → single speech model → audio (OpenAI Realtime, Gemini Live, Hume EVI, etc.). Text is optional/parallel.

Sources: [Deepgram — S2S vs Cascade](https://deepgram.com/learn/speech-to-speech-vs-cascade-voice-agent-architecture) (fetched ~2026-09-06); [Gradium cascade tradeoffs 2026](https://gradium.ai/content/cascaded-voice-agent-vs-speech-to-speech-2026); [Proof of Tech trade study](https://proofoftech.org/blog/cascaded-vs-end-to-end-speech/); [dreaming.press S2S vs cascaded](https://dreaming.press/posts/speech-to-speech-vs-cascaded-voice-agents.html); [concret.io comparison](https://www.concret.io/blog/cascade-vs-speech-to-speech-voice-agent-architecture).

### Tradeoff matrix (resume-demo relevant)

| Dimension | Cascade (STT→LangGraph→TTS) | Realtime S2S |
|-----------|----------------------------|--------------|
| **Latency** | Additive (STT + LLM + TTS). Streaming/overlap helps; published production ranges often ~1.5–3s EOU→audio for naive stacks; well-tuned cascades can go lower. **Flag:** numbers disagree across vendors. | Often lower perceived lag (single model). Moshi/open S2S claims ~200ms class — **unverified for your stack**. |
| **Cost** | Optimize per stage (cheap STT/TTS + mid LLM). Deepgram cites $200 free credits; Aura-2 ~$0.030/1k chars (pricing page ~2026-09-06). | Audio-token / session pricing; Deepgram notes Realtime-style history re-send can push **observed cost ≫ sticker** (up to ~4× claimed). |
| **Control** | Swap LLM/STT/TTS independently; RAG tools, citations, guardrails attach to text. | All-or-nothing model; tool/RAG reliability still maturing. |
| **Debug / LangSmith** | Perfect fit: transcript, retrieval hits, node spans, TTS input all traceable. | Opaque; need parallel ASR for audit. Weak for “show me the RAG path” interviews. |
| **Resume demo** | Shows **your** graph, adapters, pgvector, evals — engineers can inspect. | Feels like “I wrapped OpenAI Realtime” unless you own heavy custom infra. |
| **UX** | Half-duplex cascade is fine for ChatGPT-Voice-like push-to-talk / turn-based; barge-in needs VAD work. | Native full-duplex / paralinguistics better. |

### Recommendation

| Phase | Pick | Why |
|-------|------|-----|
| **MVP** | **Cascade STT → LangGraph → TTS** | Matches stated MVP; maximizes control, LangSmith story, swappable adapters, budget; text intermediates for citations. |
| **Later** | Optional duplex transport (LiveKit/Pipecat) **or** S2S front door that still calls your graph for hard RAG turns | Only after cascade is solid and you need sub-second barge-in. Prefer **hybrid**: S2S greeting / small talk; cascade for knowledge answers (pattern discussed in 2026 industry blogs — treat as design idea, not a shipped Brum feature). |

**Do not** make S2S the MVP backbone for a knowledge RAG resume project.

---

## 3. LangGraph + LangSmith + pgvector production patterns (2025–2026)

### Graph nodes (Brum-shaped)

Minimal production graph for personal voice KB:

1. **`ingest_query`** — normalize user text (from STT), attach `user_id` / `thread_id`.
2. **`retrieve`** — pgvector similarity (+ optional metadata filters: `user_id`, `doc_id`); return chunks + scores.
3. **`grade_docs` (optional)** — drop irrelevant chunks (saves tokens/hallucinations).
4. **`reason` / `generate`** — answer with citations; stream tokens.
5. **`respond`** — package text for TTS + UI (citations list, confidence).

Pattern seen in LangGraph-RAG-Agent: ReAct agent with `retrieve_user_documents` tool + checkpointer memory (README via GitHub MCP).

### Checkpointers & memory

Official docs ([Persistence](https://docs.langchain.com/oss/python/langgraph/persistence), [Checkpointers](https://docs.langchain.com/oss/python/langgraph/checkpointers), fetched ~2026-09-06):

| Layer | Use | Production choice |
|-------|-----|-------------------|
| **Checkpointer** | Thread-scoped short-term memory, resume, HITL | `AsyncPostgresSaver` from `langgraph-checkpoint-postgres` (LangGraph source explicitly recommends Postgres for production; `InMemorySaver` for tests only — confirmed via `search_code` on `langchain-ai/langgraph`) |
| **Store** | Cross-thread facts / prefs | `PostgresStore` with optional pgvector index ([PostgresStore reference](https://reference.langchain.com/python/langgraph.store.postgres/store/postgres/base/PostgresStore)) |
| **Config** | Always pass `thread_id` (+ `user_id` in metadata) | Keep `thread_id` ≤ 255 chars (PostgresSaver column limit — docs) |

**Ops:** call `setup()` once for migrations; prune old checkpoints (docs warn of unbounded growth); prefer separate pools if SQLAlchemy uses asyncpg while checkpointer uses psycopg3 (pattern noted in community `search_code` hits).

### Tracing / evals (LangSmith)

Docs: [LangSmith Observability](https://docs.langchain.com/langsmith/observability), [LangGraph observability](https://docs.langchain.com/oss/python/langgraph/observability), [Evaluate a graph](https://docs.langchain.com/langsmith/evaluate-graph) (~2026-09-06).

**MVP wiring:**

```bash
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=...
LANGSMITH_PROJECT=brum-mvp
```

- Tag traces: `environment`, `user_id`, `session_id`, `voice=cascade`.
- Evaluate: golden Q&A dataset over your uploaded docs; score **faithfulness**, **citation presence**, **retrieval hit rate**; use `aevaluate` if nodes are async.
- Online: collect thumbs / stars (agent-service-toolkit pattern) → LangSmith feedback.
- Redact secrets in traces (docs mention anonymizers).

### Ingest workers

Steal from [danny-avila/rag_api](https://github.com/danny-avila/rag_api) README:

- Chunk → embed in **batches** (`EMBEDDING_BATCH_SIZE`, queue, `PARALLEL_EXECUTION`).
- Async job after upload: API returns `document_id` + `status=indexing`; worker writes to pgvector with `user_id` metadata.
- Scope all retrieval/deletes by owner (their 2026 hardening narrative is a good interview talking point: never trust client-supplied ids alone).
- Connection pool: `pre_ping`, `recycle` for managed Postgres.
- For Brum: FastAPI BackgroundTasks is OK for MVP; Redis/ARQ or Celery if files > few MB or concurrent uploads.

### Same-Postgres strategy (opinionated)

One Postgres instance, three concerns:

1. App tables (users, documents, jobs) — SQLAlchemy/Alembic  
2. Vectors — `langchain-postgres` / pgvector collections  
3. Checkpoints — `langgraph-checkpoint-postgres` schemas  

Keeps Docker Compose simple and resume story coherent (“one durable store”).

---

## 4. Frameworks & adapters

### Backend: FastAPI

- Async routes: `/auth`, `/documents`, `/chat/stream`, `/voice/turn` (audio in → audio out).
- Streaming: NDJSON or SSE for text; return `audio/mpeg` or chunked WAV/Opus for TTS.
- OpenAPI docs are free resume candy.

### Frontend: Next.js voice UI

Patterns from [CodersArts FastAPI+Next voice](https://www.codersarts.com/post/how-to-build-an-ai-voice-assistant-with-openai-fastapi-and-next-js) and LiveKit React starter ([livekit-examples/agent-starter-react](https://github.com/livekit-examples/agent-starter-react), **934** stars — UI reference only):

- **MediaRecorder** → upload blob / WebSocket PCM.
- Status machine: `Ready → Listening → Uploading → Thinking → Speaking`.
- Calm dark theme; big mic; transcript + citations panel; text fallback.
- Optional later: LiveKit room for duplex — not required for cascade MVP.

### Auth

| Option | Fit for Brum | Notes |
|--------|--------------|-------|
| **Auth.js (NextAuth) + JWT to FastAPI** | Good, owned | More DIY; resume shows you wired JWKS/HS256 |
| **Clerk + FastAPI JWT verify** | Fastest polished UI | Official 2026 guides: frontend SDK + `clerk-backend-api` / JWKS on Python ([Clerk Python backend](https://clerk.com/articles/how-to-add-authentication-to-a-python-backend)); example repo [ysskrishna/fastapi-nextjs-clerk](https://github.com/ysskrishna/fastapi-nextjs-clerk) |
| **Pure FastAPI JWT** | Matches LangGraph-RAG-Agent | Best “I built it” story; email/password or magic link |

**MVP pick:** FastAPI JWT (signup/login/refresh) **or** Clerk if you want shipping speed. Avoid multi-tenant org features (out of scope).

### STT / TTS adapters (free → premium)

Design a protocol:

```text
STTAdapter.transcribe(audio: bytes, mime) -> str
TTSAdapter.synthesize(text: str, voice: str) -> bytes
LLMAdapter.chat / used inside LangGraph
```

| Tier | STT | TTS | Notes (live web ~2026-09-06) |
|------|-----|-----|------------------------------|
| Free / local | faster-whisper / OpenAI Whisper API trial | Browser SpeechSynthesis (dev only) / Kokoro self-host | Best budget; quality/latency vary |
| Credits | Deepgram ($200 free credit claimed on pricing/marketing pages) | Deepgram Aura / Flux promos (Flux free window called out through 2026-09-12 on Deepgram pricing — **time-boxed**) | Good MVP default |
| Mid | OpenAI Whisper / gpt-4o-transcribe | OpenAI TTS (~$15/1M chars cited by third-party roundups — verify on openai.com) | Simple one-vendor bill |
| Premium | Deepgram Nova / AssemblyAI | ElevenLabs (free tier ~10k chars/mo; commercial license often paid — [Voxrater free voice AI](https://voxrater.com/insights/best-free-voice-ai/)) | Demo wow; watch cost |

**Uncertainty:** Third-party price aggregators disagree; always re-check provider pricing pages before budgeting.

### Deploy: Docker → Railway / Fly / VPS

| Path | When | Notes |
|------|------|-------|
| **Docker Compose local** | Entire MVP + demos on laptop | `api`, `web`, `postgres` (pgvector image), optional `worker` |
| **Railway** | Fast public demo | pgvector templates ([railway.com/deploy/postgres-with-pgvector-engine](https://railway.com/deploy/postgres-with-pgvector-engine)); dashboard DX |
| **Fly.io** | Global / CLI-first | Managed Postgres includes pgvector ([Fly MPG docs](https://fly.io/docs/mpg/)); Basic plan listed ~$38/mo — may be heavy for a resume project |
| **Cheap VPS** (Hetzner/DO) | Max control, lowest steady cost | You own backups, TLS, upgrades |

Comparisons: [Northflank Railway vs Fly 2026](https://northflank.com/blog/railway-vs-flyio), [kunalganglani Fly vs Railway](https://www.kunalganglani.com/blog/fly-io-vs-railway).

---

## 5. Opinionated perfect design for Brum

### Exact stack (MVP)

- Package managers: Node workspace + Python uv/poetry
- API: FastAPI, Pydantic v2, SQLAlchemy 2 async, Alembic
- Agents: LangChain + LangGraph StateGraph (retrieve, reason, respond)
- Observability: LangSmith tracing + golden eval set
- DB: Postgres 16 + pgvector (vectors, app data, checkpoints)
- Auth: FastAPI JWT (owned) or Clerk if timeboxed
- Web: Next.js App Router + Tailwind + calm dark voice UI
- Voice: Cascade Deepgram STT -> adapters -> OpenAI/Deepgram TTS
- LLM: OpenAI-compatible API primary; Ollama adapter stubbed
- Packaging: Docker Compose; Railway for public demo later
- Out of MVP: company multi-tenant, Drive sync, telephony, pure S2S

### Folder layout

brum/
  apps/api/   FastAPI (main, api routers, agents, adapters, ingest, db, core)
  apps/web/   Next.js (voice UI, auth, documents)
  packages/shared/  optional shared types
  docker-compose.yml
  evals/
  README.md

### Core workflows

1. Auth -> JWT session
2. Upload docs -> chunk -> embed -> pgvector (user scoped)
3. Text chat -> LangGraph stream + citations + LangSmith
4. Voice turn -> STT adapter -> same graph -> TTS adapter -> playback
5. Eval -> faithfulness + retrieval recall on fixture docs

### Resume talking points (honest)

Say:
- Shipped greenfield voice RAG: FastAPI + LangGraph + pgvector + Next.js
- retrieve-reason-respond graph with Postgres checkpointer and LangSmith
- Swappable STT/TTS/LLM adapters and budget cascade voice path
- Async indexing, owner-scoped retrieval, Dockerized deploy

Do not overclaim:
- Not a company multi-tenant or telephony platform
- Not measured sub-200ms full-duplex S2S unless you built it
- Applied LangGraph well; did not invent the framework

### Build milestones

- M0: Compose Postgres+pgvector, FastAPI health, Next.js dark shell
- M1: Auth + upload + chunk/embed + text RAG streaming
- M2: LangGraph + Postgres checkpointer + LangSmith traces
- M3: Cascade voice turn + status UX
- M4: Adapter interfaces, evals, demo video, Railway deploy
- M5 stretch: Ollama adapter, RAG thinking filler, optional LiveKit duplex

### Open decision picks

1. LLM API vs Ollama: pick cloud OpenAI-compatible API default; stub Ollama. Why: reliable demos without GPU ops. Revisit for offline/privacy.
2. Docker local vs VPS: Docker Compose for build; Railway for public URL. Why: shareable demo without ops tax; Fly managed Postgres Basic ~USD 38/mo is steep for a showcase. Revisit for traffic/compliance.
3. Cascade vs pure S2S: Cascade STT->LangGraph->TTS. Why: control, citations, LangSmith, cost, adapters. Revisit only for barge-in; prefer transport layer over replacing the graph.

---

## Sources (access ~2026-09-06)

### GitHub API stars via search_repositories
- https://github.com/hosseinabadii/LangGraph-RAG-Agent (5)
- https://github.com/JoshuaC215/agent-service-toolkit (4470)
- https://github.com/danny-avila/rag_api (891)
- https://github.com/StabRise/scaledp-chat (9)
- https://github.com/ahmad2b/langgraph-voice-call-agent (47)
- https://github.com/dqbd/langgraph-livekit-agents (82)
- https://github.com/livekit/agents (14028)
- https://github.com/pipecat-ai/pipecat (15256)
- https://github.com/dograh-hq/dograh (5589)
- https://github.com/langchain-ai/langgraph (41109)
- https://github.com/Adii2202/RAG-AI-Voice-assistant- (48)

### Docs and articles via WebFetch / WebSearch
- https://docs.langchain.com/oss/python/langgraph/persistence
- https://docs.langchain.com/oss/python/langgraph/checkpointers
- https://docs.langchain.com/oss/python/langgraph/observability
- https://docs.langchain.com/langsmith/observability
- https://docs.langchain.com/langsmith/evaluate-graph
- https://reference.langchain.com/python/langgraph.store.postgres/store/postgres/base/PostgresStore
- https://deepgram.com/learn/speech-to-speech-vs-cascade-voice-agent-architecture
- https://deepgram.com/pricing
- https://livekit.com/blog/langchain-to-livekit
- https://gradium.ai/content/cascaded-voice-agent-vs-speech-to-speech-2026
- https://proofoftech.org/blog/cascaded-vs-end-to-end-speech/
- https://fly.io/docs/mpg/
- https://railway.com/deploy/postgres-with-pgvector-engine
- https://clerk.com/articles/how-to-add-authentication-to-a-python-backend
- https://www.codersarts.com/post/how-to-build-an-ai-voice-assistant-with-openai-fastapi-and-next-js

---

End of live report. Re-run GitHub searches before citing stars in a public README; counts move daily.
