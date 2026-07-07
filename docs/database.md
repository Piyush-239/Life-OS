# Database

## conversations

Fields

- id
- user_message
- assistant_message
- created_at

Purpose

Stores chat history.

---

## memories

Fields

- id
- category
- content
- source_conversation_id
- created_at

Purpose

Stores important facts extracted from conversations.

---

Future Tables

users

events

projects

tasks

locations

documents

photos

embeddings