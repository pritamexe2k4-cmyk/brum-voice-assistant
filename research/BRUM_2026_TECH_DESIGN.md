# Brum — 2026 Technical Design & Research Brief
**Access date:** 2026-09-06 (IST) · **Product:** Voice Knowledge Assistant (resume showcase)  
**Note:** Grok Build CLI returned 402 (balance exhausted); this pass used live WebSearch/WebFetch + GitHub API. Re-run via Grok when credits are topped up.

---

## 1) Similar open-source repos (steal vs skip)

| Repo | Stars (GitHub API 2026-09-06) | Stack signal | Steal | Skip |
| --- | --- | --- | --- | --- |
| [pipecat-ai/pipecat](https://github.com/pipecat-ai/pipecat) | 15,256 | Voice pipeline framework (Daily) | Turn-taking, STT/TTS adapter patterns, barge-in ideas | Do **not** make Pipecat the product core — it competes with “owned LangGraph spine” story |
| [livekit/agents](https://github.com/livekit/agents) | 14,028 | Realtime voice agent framework | WebRTC transport patterns; [agent-starter-react](https://github.com/livekit-examples/agent-starter-react) (934★) for Next voice UI | Optional later for WebRTC; MVP can use MediaRecorder + WS without LiveKit lock-in |
| [pipecat-ai/voice-ui-kit](https://github.com/pipecat-ai/voice-ui-kit) | 409 | React voice UI kit | Orb / listening-state UI inspiration | Keep UI owned in Next.js |
| [rokbenko/ai-playground](https://github.com/rokbenko/ai-playground) | 320 | LangChain/LangGraph/LangSmith/pgvector tutorials | Concrete LG+pgvector snippets | Tutorial soup — not architecture |
| [goruck/home-generative-agent](https://github.com/goruck/home-generative-agent) | 295 | LangGraph + pgvector + voice topics + Ollama/cloud | Adapter pattern for local vs cloud LLM | Home Assistant domain — don’t copy product |
| [colossus-lab/openarg_backend](https://github.com/colossus-lab/openarg_backend) | 144 | FastAPI + LangGraph + Postgres/pgvector + Celery | FastAPI+LG+Celery ingest worker layout | Domain-specific connectors |
| [WANGLEVY9/VidForge](https://github.com/WANGLEVY9/VidForge) | 110 | LangGraph + pgvector + React + cost tracing | Monorepo + tracing mindset | Video pipeline — not Brum |

**Verdict:** Study Pipecat/LiveKit for *voice transport UX*, but **own** the brain as LangGraph+RAG on FastAPI — that is the resume differentiator.

Sources: GitHub `search_repositories` API, 2026-09-06.

---

## 2) Voice architecture: cascade vs S2S (2026)

Industry consensus (OpenAI Voice Agents docs; LiveKit “Pipeline vs Realtime”; Deepgram; Inworld):

| | **Cascade STT → LangGraph → TTS** | **Pure S2S / Realtime** |
| --- | --- | --- |
| Latency / feel | Higher; can still stream TTS (~100–250ms first audio with good TTS) | Best naturalness, barge-in, prosody |
| Control | Full text at every seam → RAG, tools, PII, audit | Opaque; tool/RAG injection harder |
| Swap adapters | Easy (free STT/TTS → premium) | Vendor-locked speech model |
| Resume / LangSmith story | Excellent (every node traced) | Weak for “owned graph” narrative |
| Cost | Predictable per stage | Can spike on long sessions |

**Recommendation for Brum MVP:** **Cascade first.**  
OpenAI’s own guide: chained pipeline when you need control / extending a text agent; S2S when naturalness is primary. Brum’s core value is **KB-backed reasoning + owned LangGraph** — that needs the text seam. Ship cascade; add optional S2S “companion mode” later as a swappable transport that still calls `search_kb` tools.

Sources:  
- https://developers.openai.com/api/docs/guides/voice-agents  
- https://livekit.com/blog/realtime-vs-cascade  
- https://deepgram.com/learn/speech-to-speech-vs-cascade-voice-agent-architecture  
- https://inworld.ai/resources/cascaded-vs-speech-to-speech-voice-architecture  

---

## 3) LangGraph + LangSmith + pgvector production patterns (2025–2026)

### Graph nodes (MVP turn)
1. `load_state` — thread_id, user_id, short history  
2. `retrieve` — hybrid dense (pgvector) + optional BM25/`tsvector`  
3. `grade` / gate (optional) — drop junk chunks  
4. `generate` — LLM with citations metadata (even if UI hides transcript)  
5. `speak` — TTS adapter (outside graph or final node)  
6. `summarize_async` — write session summary / long-term facts (background)

### Persistence
- **PostgresSaver** checkpointer for LangGraph threads (enterprise pattern to avoid state divergence)  
- Same Postgres hosts **pgvector** tables + app auth — one DB for MVP ops story  
- Schema: every KB row has `user_id` (and nullable `org_id`) from day 1 — multi-tenant-ready without building orgs yet  

### Ingest
- Upload API → object store (local MinIO → S3 later) → **async worker** (Celery/ARQ/RQ) chunk → embed → upsert  
- Index with HNSW; prefer halfvec where supported (pgvector 0.7+ memory wins cited in 2026 writeups)

### MLOps lite (LangSmith)
- Trace every graph node from day 1 (`LANGCHAIN_TRACING_V2`)  
- Curate a 20–50 example dataset (your PDFs Q&A)  
- Offline evals: faithfulness / relevance / correctness (LLM-as-judge, temp=0)  
- Prod: sample ~10% traces + always-on errors  
- Official concepts: https://docs.langchain.com/langsmith/evaluation  

Sources:  
- https://datastorage.com/articles/building-a-production-ready-rag-architecture-in-2026/  
- https://www.c-sharpcorner.com/article/handling-state-divergence-in-distributed-langgraph-a-guide-for-enterprise-rag/  
- https://markaicode.com/stack/langgraph-langchain-stack/  
- https://docs.langchain.com/langsmith/evaluation  

---

## 4) Recommended frameworks (opinionated for Brum)

| Layer | Pick | Why |
| --- | --- | --- |
| API | **FastAPI** | Async, fits LangGraph, Celery workers; resume-standard |
| Orchestration | **LangGraph** + LangChain tools | Stateful RAG graph; interview gold |
| Observe | **LangSmith** | Traces + datasets + evals = MLOps lite |
| DB | **Postgres 16 + pgvector** | One box, hybrid search later, ownership |
| Files | MinIO locally → S3 | Upload pipeline without Supabase lock-in |
| Web | **Next.js (App Router) + React** | App-like full-screen voice UI |
| Auth | **Auth.js (NextAuth) + FastAPI JWT** or **Clerk** if you want speed | Prefer Auth.js+JWT for “owned”; Clerk OK if timeboxed |
| STT MVP | Faster-Whisper / Groq Whisper / Deepgram free tier | Adapter interface |
| TTS MVP | Edge-TTS / OpenAI TTS / Deepgram Aura | Adapter interface |
| LLM MVP | **Groq or OpenAI API** (not Ollama day 1) | Reliable demo; Ollama as second adapter |
| Deploy | **Docker Compose** → Railway/Fly/small VPS | Honest “I deployed it” |

---

## 5) Perfect technical design for Brum (lock this)

### Architecture (MVP)
```
Browser (Next.js dark orb UI)
  mic MediaRecorder / WebAudio
       │  WS or HTTPS chunks
FastAPI
  /auth  /docs  /ingest  /voice/turn  /health
       │
  STT adapter ──► LangGraph turn
                    retrieve(pgvector) → generate → (tools)
       │
  TTS adapter ──► audio bytes to client
       │
  LangSmith traces
Postgres: users | documents | chunks+embeddings | checkpoints | memory_facts
Worker: ingest jobs
```

### Monorepo layout
```
brum-voice-assistant/
  apps/
    web/                 # Next.js voice UI + auth
    api/                 # FastAPI
  packages/
    shared/              # OpenAPI types / zod
  docker-compose.yml     # api, web, postgres, minio, worker, redis
  docs/
  research/
  README.md
apps/api/
  app/
    main.py
    routers/             # auth, docs, voice, health
    graphs/              # langgraph definitions
    nodes/               # retrieve, generate, summarize
    adapters/            # llm.py stt.py tts.py embeddings.py
    db/                  # models, pgvector SQL
    workers/             # ingest
    evals/               # LangSmith datasets scripts
```

### Core workflows
1. **Ingest:** upload → store → chunk (page-aware) → embed → HNSW upsert → status  
2. **Voice turn:** audio → STT → graph.invoke(thread_id, user_id) → TTS → play + status animations  
3. **Observe:** LangSmith project `brum-dev` / `brum-prod`; weekly eval on fixed dataset  

### Resume talking points (honest)
- “Designed and built a personal voice knowledge assistant: FastAPI + LangGraph RAG over Postgres/pgvector, modular STT/TTS/LLM adapters, LangSmith tracing, Docker Compose deploy.”  
- Highlight: **owned orchestration**, hybrid-ready retrieval schema, adapter pattern, eval harness — not “used ChatGPT Voice API.”  
- Until code lands: keep “designing & building”; refresh bullets when first Docker demo works.

### Build order (job-hunt optimized)
1. Docker Compose: Postgres+pgvector + FastAPI hello + empty Next shell  
2. Auth + `user_id` schema  
3. Ingest worker + retrieve API (text chat first — faster to prove RAG)  
4. LangGraph graph + LangSmith traces  
5. Cascade voice UI (mic → STT → graph → TTS) + calm orb states  
6. Eval dataset (20 Qs from your notes) + one CI eval script  
7. Public demo URL + README architecture diagram  

### Open decisions — **recommended locks**
1. **LLM:** **API first (Groq/OpenAI)** — demo reliability; add Ollama adapter second for “local” bullet.  
2. **Host:** **Docker Compose locally first**, then one VPS/Railway when voice demo works — don’t burn days on cloud before RAG works.  
3. **Voice:** **Cascade first** — matches LangGraph+RAG+LangSmith story; S2S later as optional transport.

---

## 6) What *not* to do
- Rebuild on Lovable/Supabase-as-product  
- Make LiveKit/Pipecat the brain (transport only, if at all)  
- Pure S2S before RAG graph exists  
- Skip `user_id` on chunk tables  
- Claim “production multi-tenant company brain” on resume before it exists  

---

*Prepared for Preetam + Spider · Researchy · 2026-09-06*
