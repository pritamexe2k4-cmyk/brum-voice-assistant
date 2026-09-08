# Brum — Voice Knowledge Assistant

Personal voice + RAG assistant (**Brum**). Runtime stack transported from a working RAGVoice-AI reference so you can run Brum locally under this repo name.

## What runs here
- **RAG:** documents → chunks → OpenAI embeddings → FAISS (`vector_store/`)
- **Orchestration:** LangGraph multi-agent (`src/multi_agent_rag.py`)
- **Voice path (optional keys):** LiveKit + Deepgram STT + Cartesia TTS (`src/agent.py`)

## Quick start (Windows)

```powershell
cd C:\Users\preet\OneDrive\Desktop\brum-voice-assistant
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env.local
# put OPENAI_API_KEY in .env.local (required for RAG)
python src\rag_system.py
```

With only OpenAI you get FAISS + retrieval tests. Full voice needs LiveKit / Deepgram / Cartesia in `.env.local`.

## Layout
- `src/` — Brum runtime (RAG, agents, voice entry)
- `documents/` — sample KB docs
- `vector_store/` — local FAISS index (regenerate with `rag_system.py`)
- `research/` — Brum product decisions log
- `PHASE1_PRP.md`, `docs/` — product specs

## Note
Client UI / Brum product redesign can continue separately; this commit makes the **runnable voice+RAG engine** live inside `brum-voice-assistant`.
