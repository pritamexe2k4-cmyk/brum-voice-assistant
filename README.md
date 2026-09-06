# Brum — Voice Knowledge Assistant

**One-liner:** Personal voice assistant over *your* docs — owned FastAPI + LangGraph RAG stack (not a ChatGPT skin).

**Repo:** https://github.com/pritamexe2k4-cmyk/brum-voice-assistant  
**Status:** **Docs-only / build not started.** App code waits for Preetam’s explicit **START** signal.

---

## Use

- Upload personal notes/PDFs → ask by voice or text → grounded answers from your KB
- AI Engineer resume demo: LangGraph + pgvector + LangSmith + Docker
- Quiet study / second-brain companion

## Non-use (out of MVP)

- Multi-tenant company SaaS / orgs
- Phone/SIP call-center
- Pure speech-to-speech as the MVP spine
- Lovable / Supabase-as-product lock-in
- MCP / Drive connectors (later)

---

## Stack locks (2026-09-06)

| Layer | Choice |
| --- | --- |
| Voice | **Cascade** STT → LangGraph → TTS first |
| LLM | **API first** (Groq/OpenAI); Ollama adapter later |
| Host | **Docker Compose locally** first → Railway/VPS later |
| API | FastAPI |
| Orchestration | LangGraph + LangChain tools |
| Observe | LangSmith |
| DB | Postgres 16 + pgvector (+ checkpointer) |
| Web | Next.js (App Router) + React |
| Adapters | Swappable STT / TTS / LLM / embeddings |

Pipecat / LiveKit = **post-MVP transport only**, not the brain.

---

## Docs map

| Doc | Purpose |
| --- | --- |
| [docs/PRODUCT_PRESENTATION.md](docs/PRODUCT_PRESENTATION.md) | Product story, use / non-use |
| [docs/WORKFLOW.md](docs/WORKFLOW.md) | Ingest + cascade voice + observe |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | System design + planned monorepo |
| [docs/BUILD_PLAN.md](docs/BUILD_PLAN.md) | Milestones M0–M5 (**no code until START**) |
| [docs/DECISIONS.md](docs/DECISIONS.md) | Locked product/tech decisions |
| [docs/INTERVIEW.md](docs/INTERVIEW.md) | Honest talking points |
| [docs/SCHEMA.md](docs/SCHEMA.md) | Design-only DB sketch |
| [research/research.md](research/research.md) | Living research log |
| [research/BRUM_2026_TECH_DESIGN.md](research/BRUM_2026_TECH_DESIGN.md) | Researchy design brief |
| [research/live-report.md](research/live-report.md) | Deep live research pass |

---

## Success criteria (MVP)

Login → upload docs → text grounded answers with LangSmith traces → voice turn on the **same** graph → `docker compose up` locally → honest resume bullets.

---

## License

Private build for now — license TBD.
