# Architecture
# Architecture

## Current Architecture

Client

↓

FastAPI

↓

Chat Service

↓

Chat Pipeline

↓

LLM Provider

↓

Memory Services

↓

SQLite

---

## Project Structure

server/

- api/
- services/
- database/
- schemas/
- core/
- static/

---

## Rules

Routes only handle HTTP.

Services contain business logic.

Database only stores data.

Schemas validate requests and responses.

Future modules should follow the same pattern.