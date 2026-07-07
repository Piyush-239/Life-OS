# PROJECT_CONTEXT.md

# LIFE-OS Project Context

## Project Overview

LIFE-OS is a long-term engineering project whose goal is to build a lifelong AI companion rather than another chatbot.

The project is designed to become a personal operating system that can remember, reason, plan, and assist across multiple devices over many years.

The AI model itself is intentionally replaceable. The real intelligence should come from architecture, memory, planning, retrieval, and tool usage.

This project is being built incrementally as both a production-quality software project and a learning journey.

---

# Vision

Create an AI companion that can eventually provide:

* Natural voice conversations
* Long-term memory
* Desktop automation
* Android integration
* Browser automation
* File management
* Project management
* Calendar management
* Knowledge graph
* Vision
* OCR
* Camera understanding
* GPS timeline
* Coding assistance
* Research assistance
* Planning
* Smart home integration
* Wearable support
* Smart glasses support

Voice is intended to become the primary interface.

The web interface exists only for testing and debugging.

---

# Development Philosophy

Build slowly.

Build correctly.

Build modularly.

Every capability should exist as an independent module.

Every module should expose an API.

Never tightly couple the project to one AI model.

Everything should be replaceable.

The project itself is the curriculum.

Whenever a new concept is encountered, learn only enough to continue building.

---

# Current Architecture

Current stack:

Windows 11

Python 3.12

FastAPI

Ollama

Dolphin 3

SQLite

SQLAlchemy

Git

VS Code

Current backend architecture:

Client

↓

FastAPI

↓

Routes

↓

Services

↓

Chat Pipeline

↓

LLM Provider

↓

Database

---

Project structure:

server/

* api/
* services/
* database/
* schemas/
* core/
* static/

client/

android/

docs/

experiments/

scripts/

docker/

---

# Architecture Rules

Routes should only handle HTTP.

Business logic belongs inside services.

Database layer only stores and retrieves data.

Schemas validate API requests and responses.

Keep components loosely coupled.

Design everything so future components can be replaced independently.

---

# Current Features Implemented

Project setup completed.

Virtual environment configured.

Git repository configured.

Private GitHub repository created.

FastAPI backend created.

Health endpoint created.

Status endpoint created.

Basic web interface added.

Static file serving configured.

Ollama integration completed.

LLM Provider abstraction implemented.

Chat endpoint implemented.

Settings system implemented.

SQLite configured.

SQLAlchemy configured.

Conversation model created.

Memory model created.

Conversation storage implemented.

Basic memory extraction implemented.

Memory storage implemented.

Chat pipeline refactored into smaller components.

Current architecture separates orchestration from implementation.

---

# Current Database

Table: conversations

Fields

* id
* user_message
* assistant_message
* created_at

Purpose

Stores conversation history.

---

Table: memories

Fields

* id
* category
* content
* source_conversation_id
* created_at

Purpose

Stores meaningful memories extracted from user messages.

Current philosophy:

Do NOT save every sentence as memory.

Only meaningful long-term facts should become memories.

---

# Current Services

ChatService

Purpose:

Acts as a lightweight orchestrator.

---

ChatPipeline

Purpose:

Runs the complete chat workflow.

Current responsibilities:

* Call LLM
* Save conversation
* Extract memories
* Save memories

Future responsibilities will remain small by creating additional pipelines instead of making ChatPipeline excessively large.

---

ConversationService

Purpose:

Save conversations.

---

MemoryService

Purpose:

Store extracted memories.

---

MemoryExtractor

Purpose:

Identify meaningful facts from user messages.

Current implementation is intentionally simple.

It will become smarter later.

---

LLM Provider

Current provider:

Ollama

Future providers may include any local or cloud model.

No other component should depend directly on Ollama.

---

# Current API

GET /

Returns the web interface.

GET /status

Returns project status.

POST /chat

Receives:

{
"message": "..."
}

Returns:

{
"reply": "..."
}

Streaming endpoint has NOT yet been implemented.

---

# Current Sprint

Streaming Responses

Goals:

Implement real-time token streaming from Ollama to the browser.

Planned work:

* Add stream_chat() to the Ollama provider.
* Add streaming pipeline.
* Add /chat/stream endpoint.
* Use FastAPI StreamingResponse.
* Update JavaScript to display tokens as they arrive.
* Save the completed response only after streaming finishes.

The standard /chat endpoint should remain available for APIs and future Android clients.

---

# Roadmap

Phase 1

* FastAPI
* Local LLM
* Memory
* SQLite
* Streaming
* Memory retrieval
* Prompt builder
* File search
* Voice input
* Voice output

Phase 2

Desktop automation

Browser automation

Semantic search

Timeline

Phase 3

Android companion

Notifications

GPS

Photos

Voice notes

Phase 4

Vision

OCR

Scene understanding

Object recognition

Phase 5

Planning

Reminders

Smart home

Wearables

---

# Important Design Decisions

The AI model is replaceable.

Memory is more important than conversation history.

Voice is the primary interface.

The web UI should remain minimal.

Do not spend development time polishing UI unless it directly helps development.

Prefer backend capabilities over frontend appearance.

---

# Future Long-Term Goal

Eventually LIFE-OS should become an autonomous engineering assistant capable of improving itself safely.

However, self-modification must always occur inside strict guardrails.

Future autonomous development should include:

* Dedicated Git branch
* Automatic testing
* Automatic rollback
* Automatic reporting
* Human approval before merging

The core system should remain protected while plugins and modules can evolve independently.

---

# Mentor Instructions

Assume the role of a senior software architect and teacher.

The project owner is intentionally learning by building.

Explain architectural decisions briefly but clearly.

Prioritize long-term maintainability over quick hacks.

Do not over-engineer unnecessarily.

Focus development on capabilities that move LIFE-OS toward becoming a lifelong AI operating system.

When ending a work session, always provide a Shutdown Checklist including:

* What was completed
* What should be committed
* Which documentation files should be updated
* What the next sprint should accomplish

Always preserve the project's modular architecture and long-term vision.

If proposing a new feature, explain where it belongs within the architecture before implementing it.


## Progress Update (Day 4)

Major architecture refactor completed.

The project now follows a layered architecture:

Browser
→ API
→ ChatService
→ ChatPipeline
→ Brain
→ Database

Brain layer introduced:

- ChatBrain
- MemoryBrain

Streaming pipeline implemented.

Conversation history is stored successfully.

Memory extraction has moved toward AI-driven processing instead of rule-based extraction.

Current blocker:
AI memory retrieval is not yet fully integrated into the prompt pipeline and requires debugging before voice features begin.