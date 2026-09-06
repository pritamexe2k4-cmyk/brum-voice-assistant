# Brum — Product Presentation

**One line:** Talk to your own knowledge — a personal voice assistant over *your* docs, built as an owned AI system (not ChatGPT with a skin).

**Repo:** https://github.com/pritamexe2k4-cmyk/brum-voice-assistant

---

## Problem

Notes and PDFs sit unused. Generic chatbots don’t know *your* material. Teams later need one shared brain — Brum starts with one user, same spine.

## Solution

Upload docs → embed into a vector store → talk (or type) → answers grounded in your KB (+ optional web), with traces and deploy you own.

## Target users

| Now | Later |
| --- | --- |
| You (personal second brain) | Friends group → company voice → classes |

---

## Use cases (YES)

1. **Study / interview prep** — upload notes, ask by voice, get answers from *your* material  
2. **Personal second brain** — dump PDFs/MD, retrieve later without hunting files  
3. **Demo for AI Engineer roles** — show LangGraph RAG + LangSmith + Docker  
4. **Quiet work companion** — talk while walking; short spoken answers  
5. **Future team brain** — same pipeline, multi-user KB (not built yet)

## Non-use cases (NO)

1. **Not a general ChatGPT clone** — weak without your uploads  
2. **Not a phone dialer / call-center bot** (yet)  
3. **Not multi-tenant SaaS / company prod** — no SSO/orgs yet  
4. **Not medical/legal source of truth** — assist, don’t certify  
5. **Not offline-only by default** — needs LLM/STT/TTS (API or local)  
6. **Not Lovable/Supabase-locked** — greenfield owned stack

---

## Workflow (how it works)

```
Upload docs → chunk → embeddings → Postgres/pgvector
                    ↓
User speaks → STT → LangGraph turn:
                 retrieve KB → LLM (+ tools) → answer
                    ↓
              TTS → play audio
                    ↓
         LangSmith traces the graph
```

**Auth:** login → your KB only  
**Observe:** LangSmith  
**Ship:** Docker Compose → VPS/Railway

---

## Stack (rebuild target)

FastAPI · LangChain · LangGraph · LangSmith · Postgres+pgvector · Next.js/React · Auth · Docker · swappable LLM/STT/TTS adapters

---

## Success

You can log in, upload, ask by voice, get a KB-aware answer, see a LangSmith trace, run it on your machine/VPS.
