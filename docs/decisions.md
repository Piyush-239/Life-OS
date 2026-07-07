# Architecture Decisions

## AI Provider

Decision:

Use Ollama locally.

Reason:

Privacy and offline capability.

Future:

Should be replaceable.

---

## Database

Decision:

SQLite first.

Reason:

Simple development.

Future:

PostgreSQL.

---

## Memory

Decision:

Store only meaningful facts.

Do not store every conversation.

Reason:

Scalability.

---

## Chat Pipeline

Decision:

Business logic belongs inside ChatPipeline.

Reason:

Keeps ChatService small and allows future streaming and planner pipelines.

---

## UI

Decision:

Minimal interface.

Reason:

Voice is the primary interface.

The web UI is only for debugging and testing.