# Changelog

## Version 0.1.0

Initial project setup.

Completed

- FastAPI
- Project structure
- Settings
- Ollama integration
- SQLite
- SQLAlchemy
- Conversation storage
- Memory extraction
- Memory storage
- Basic web interface

Current work

Preparing streaming responses.

# Day 4

## Added

- Introduced Brain architecture.
- Added ChatBrain.
- Added MemoryBrain.
- Refactored ChatPipeline to use Brain modules.
- Added PromptBuilder with system prompt support.
- Added streaming pipeline architecture.
- Added MemoryService.get_all().
- Started AI-based memory extraction.
- Started AI-based memory retrieval.

## Changed

- LLM provider now supports normal and streaming responses.
- Chat pipeline is now modular instead of directly calling the LLM.

## Known Issues

- AI memory retrieval is not yet fully connected.
- Memory extraction works, but retrieval still requires debugging.