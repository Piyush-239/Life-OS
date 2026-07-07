# LIFE-OS

> A lifelong AI operating system that grows alongside its owner.

## Vision

LIFE-OS is not another chatbot.

It is a modular, privacy-first AI operating system designed to become a lifelong companion across every device.

Instead of relying only on conversation history, LIFE-OS builds structured long-term memory and continuously evolves through retrieval, planning, and modular services.

The language model is only one component of the system.

---

# Core Principles

- One identity across all devices
- Long-term memory
- Privacy-first
- Modular architecture
- API-first design
- Replaceable AI models
- Event-based memory
- Continuous learning through retrieval
- Learn by building

---

# Current Features

- FastAPI backend
- Ollama integration
- Modular LLM provider
- SQLite database
- SQLAlchemy ORM
- Conversation storage
- Memory extraction
- Memory storage
- Basic web interface

---

# Project Structure

```
LIFE-OS/

server/
    api/
    services/
    database/
    schemas/
    core/
    static/

client/

android/

docs/

experiments/

scripts/

docker/
```

---

# Development Philosophy

Every capability should be an independent module.

Modules communicate through APIs.

Business logic belongs in services.

Routes only expose HTTP endpoints.

The AI model should always be replaceable.

---

# Technology Stack

Backend

- Python
- FastAPI
- SQLAlchemy
- SQLite

AI

- Ollama
- Dolphin 3

Future

- PostgreSQL
- Vector Database
- Whisper
- Piper
- Android
- Docker

---

# Current Roadmap

Phase 1

- Backend
- Memory
- Streaming
- Voice
- File Search

Phase 2

- Desktop Automation
- Browser Automation

Phase 3

- Android Companion

Phase 4

- Vision

Phase 5

- Planning

---

# How to Run

Create virtual environment

```
python -m venv .venv
```

Activate

```
.venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt
```

Run server

```
uvicorn app.main:app --reload
```

Open

```
http://127.0.0.1:8000
```

---

# Current Status

Version

0.1.0

Current Sprint

Streaming responses

---

This project is built as a long-term engineering journey.

The project itself is the curriculum.