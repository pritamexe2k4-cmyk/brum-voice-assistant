# Brum — Product Presentation

**One line:** Talk to your own knowledge — a personal voice assistant over *your* docs, built as an owned AI system (not ChatGPT with a skin).

**Repo:** https://github.com/pritamexe2k4-cmyk/brum-voice-assistant  
**Status:** Docs-ready · application code **not started** (awaiting START).

---

## Problem

Notes and PDFs sit unused. Generic chatbots don’t know *your* material. Teams later may need one shared brain — Brum starts with one user, same spine.

## Solution

Upload docs → embed into Postgres/pgvector → talk (or type) → answers from your KB (+ optional web later), with LangSmith traces and Docker you own.

## Target users

| Now | Later |
| --- | --- |
| You (personal second brain) | Friends group → company voice → classes |

---

## Use cases (YES)

1. **Study / interview prep** — upload notes, ask by voice, answers from *your* material
2. **Personal second brain** — dump PDFs/MD, retrieve without hunting files
3. **AI Engineer demo** — LangGraph RAG + LangSmith + Docker Compose
4. **Quiet work companion** — talk while walking; short spoken answers
5. **Future team brain** — same pipeline, multi-user KB (**not built yet**)

## Non-use cases (NO)

1. **Not a general ChatGPT clone** — weak without your uploads
2. **Not a phone dialer / call-center bot**
3. **Not multi-tenant SaaS / company prod** — no SSO/orgs yet
4. **Not medical/legal source of truth** — assist, don’t certify
5. **Not offline-only by default** — needs LLM/STT/TTS (API or local later)
6. **Not Lovable/Supabase-locked** — greenfield owned stack
7. **Not pure S2S spine for MVP** — cascade first for control + traces

---

## Workflow (how it works)

```
Upload docs → chunk → embeddings → Postgres/pgvector
                    ↓
User speaks → STT → LangGraph turn:
                 retrieve KB → reason/generate → answer
                    ↓
              TTS → play audio
                    ↓
         LangSmith traces the graph
```

**Auth:** login → your KB only (`user_id` on every row)  
**Observe:** LangSmith  
**Ship:** Docker Compose → Railway/VPS

---

## Stack (locked target)

FastAPI · LangChain · LangGraph · LangSmith · Postgres+pgvector · Next.js/React · Auth · Docker · swappable LLM/STT/TTS adapters

---

## Success

You can log in, upload, ask by text then voice, get a KB-aware answer, see a LangSmith trace, run it on your machine.
