# Brum v1 — Lovable PRD Prompt

Paste everything below the line into Lovable to scope and build.

---

## Product Requirements Prompt: Brum (Phase 1 / Personal MVP)

Build **Brum**, a personal **speech-to-speech voice assistant** with a knowledge base behind the scenes — not another ChatGPT clone. The user opens an app-like web page, talks naturally, and Brum answers using a mix of conversation ability, web search, and the user’s uploaded documents. The long-term vision is a company/team brain-dump voice agent; **v1 is single-user only**.

### One-liner
ChatGPT/Grok-style voice UI + silent personal KB + modular free models → calm full-screen web app you can talk to about your files and the web.

### Problem
Thoughts and docs stay in papers/folders; talking to a generic chatbot loses *your* context. Brum makes knowledge talkable: dump/upload once, converse by voice forever.

### Target user (v1)
- Primary: one person (the builder) for personal use and demos
- Later (out of scope for this build): friends group → companies → students/classes

### Platform
- **Responsive web that feels like a native app** (full-screen voice shell; mobile + desktop)
- No native iOS/Android app in v1
- No user accounts / login in v1 (private project)

### Core UX (inspired by ChatGPT Voice, Grok Voice, persona’d S2S assistants)
- Minimal / calm design: dark, quiet, large orb or soft waveform
- Visual states only (no transcript panel): **idle · listening · processing · speaking**
- Always-available **Upload** entry for knowledge (PDFs and broad file formats; images when pipeline allows)
- KB stays behind the conversation — don’t force a “notebook” mode for every chat
- User talks only to Brum (no multiplayer chat)

### Must-have features (P0)
1. Full-screen voice conversation with mic + speaker (speech-to-speech *feel*)
2. Modular voice/LLM providers — **start on free/basic**; architecture must allow swapping to premium Realtime/S2S later without rewriting UI
3. Knowledge base: upload files → store → retrieve into the voice loop
4. Mixed answers: general chat + web search + KB (no hard cite-or-refuse in v1)
5. Calm state animations for listening / thinking / speaking
6. System persona/identity for Brum (configurable personality)
7. Memory: short-term session context + persist session summaries + light long-term user facts (no visible chat transcript UI)

### Explicit non-goals (v1)
- User accounts / OAuth
- User-to-user messaging
- Strict grounded-only / refuse-when-unknown mode
- Native mobile apps
- Multi-tenant company workspaces
- Notion sync, MCP tool hosts, Google Drive connectors (roadmap only — design hooks OK)

### Data to store
Separate **document RAG** from **agent memory**:
- Uploaded files + metadata + chunks/embeddings
- System identity / persona config
- Working memory: current session turns (in-memory)
- Long-term: session summaries + small semantic user facts
- Optional images via upload pipeline
Do **not** build a full chat-history UI in v1.

### Technical direction (for Lovable planning)
- Front: React (or Lovable default) full-screen voice shell
- Backend: simple API for upload, ingest, retrieve, memory write/read, web-search tool
- Voice: provider adapters (free STT/LLM/TTS cascade acceptable for MVP if true free S2S unavailable; same UI)
- Storage: lightweight (e.g. Supabase storage + DB, or local/simple vector store) — no auth required for single-user private deploy
- Tools callable from the agent: `search_kb`, `web_search`, memory read/write

### Success criteria
- User can open the URL, upload docs, and hold a spoken conversation where Brum uses those docs and/or web when useful
- Animations clearly show listening vs processing vs speaking
- Swapping a model provider is a config/adapter change, not a redesign
- Feels calm and personal, not like a busy dashboard

### Future roadmap (do not build now; leave extension points)
- Friends-group shared KB
- Company multi-user brain dumps + company voice
- Strict cite-or-refuse mode
- Premium Realtime models
- Auth / accounts
- Students/classes
- **MCP servers + Google Drive** so Brum can reach external tools and Drive files easily
- Notion sync

### Design notes
- Dark minimal palette, generous whitespace, one focal orb/waveform
- Upload accessible but secondary (sheet/drawer), never cluttering the voice stage
- Motion: soft, slow, not flashy sci-fi

Please produce a scoped build plan and implement the v1 app accordingly.
