from app.planner.planner import ExecutivePlanner
from app.memory import (
    MemoryExtractor,
    MemoryValidator,
    MemoryRetriever,
    ImportanceScorer,
    MemoryService,
)
from app.chat import ChatPipeline, StreamingChatPipeline
from app.tools import Calculator, WebSearch, ToolExecution
from app.services.conversation.service import ConversationService


class ExecutionRouter:

    def __init__(self):
        self.planner = ExecutivePlanner()
        self.memory_extractor = MemoryExtractor()
        self.memory_validator = MemoryValidator()
        self.memory_retriever = MemoryRetriever()
        self.importance_scorer = ImportanceScorer()
        self.memory_service = MemoryService()
        self.chat_pipeline = ChatPipeline()
        self.stream_chat_pipeline = StreamingChatPipeline()
        self.calculator = Calculator()
        self.web_search = WebSearch()
        self.tool_execution = ToolExecution()
        self.conversation_service = ConversationService()

    def format_memory_store_reply(self, approved_memories) -> str:
        if not approved_memories:
            return "Got it! I'll remember that."

        parts = []
        for m in approved_memories:
            key = m["key"].replace("_", " ").strip()
            val = m["value"].strip()

            if key.lower().startswith("my "):
                key = "your " + key[3:]
            elif not key.lower().startswith("your "):
                key = "your " + key

            parts.append(f"{key} is {val}")

        return f"Got it! I'll remember that {', '.join(parts)}."

    def handle(self, message: str) -> str:
        plan = self.planner.plan(message)
        intent = plan["intent"]

        print(f"[ROUTER] {intent}")

        if intent == "memory_store":
            candidates = self.memory_extractor.extract(message)
            print("[MEMORY] extracted")
            all_memories = self.memory_service.get_all()
            approved = self.memory_validator.validate(
                candidates,
                all_memories,
            )
            print("[MEMORY] validated")

            reply = self.format_memory_store_reply(candidates)

            if approved:
                for memory in approved:
                    memory["importance"] = (
                        self.importance_scorer.score(
                            memory
                        )
                    )

                conversation = (
                    self.conversation_service.save(
                        user_message=message,
                        assistant_message=reply,
                    )
                )
                self.memory_service.save(
                    approved,
                    conversation.id,
                )
                print("[MEMORY] saved")
            else:
                self.conversation_service.save(
                    user_message=message,
                    assistant_message=reply,
                )

            return reply

        elif intent == "memory_query":
            summary_keywords = [
                "about me",
                "know about me",
                "everything you know",
                "who am i",
                "do you know me",
            ]
            cleaned_message = message.lower().strip()
            is_summary = any(
                kw in cleaned_message for kw in summary_keywords
            )

            all_memories = self.memory_service.get_all()

            if is_summary:
                print("[MEMORY] retrieved all memories for summary")
                relevant = all_memories
            else:
                relevant = self.memory_retriever.retrieve(
                    message,
                    all_memories,
                )
                print("[MEMORY] retrieved")

            return self.chat_pipeline.run(message, relevant)

        elif intent == "calculator":
            result = self.calculator.calculate(message)
            self.conversation_service.save(
                user_message=message,
                assistant_message=result,
            )
            return result

        elif intent == "web_search":
            result = self.web_search.search(message)
            self.conversation_service.save(
                user_message=message,
                assistant_message=result,
            )
            return result

        elif intent == "tool":
            result = self.tool_execution.execute(message)
            self.conversation_service.save(
                user_message=message,
                assistant_message=result,
            )
            return result

        elif intent == "chat":
            return self.chat_pipeline.run(
                message,
                memories=[],
            )

        else:
            print(
                f"[Router] Forwarding unimplemented intent '{intent}' to Chat LLM"
            )
            return self.chat_pipeline.run(
                message,
                memories=[],
            )

    def handle_stream(self, message: str):
        plan = self.planner.plan(message)
        intent = plan["intent"]

        print(f"[ROUTER] {intent}")

        if intent == "memory_store":
            candidates = self.memory_extractor.extract(message)
            print("[MEMORY] extracted")
            all_memories = self.memory_service.get_all()
            approved = self.memory_validator.validate(
                candidates,
                all_memories,
            )
            print("[MEMORY] validated")

            reply = self.format_memory_store_reply(candidates)

            if approved:
                for memory in approved:
                    memory["importance"] = (
                        self.importance_scorer.score(
                            memory
                        )
                    )

                conversation = (
                    self.conversation_service.save(
                        user_message=message,
                        assistant_message=reply,
                    )
                )
                self.memory_service.save(
                    approved,
                    conversation.id,
                )
                print("[MEMORY] saved")
            else:
                self.conversation_service.save(
                    user_message=message,
                    assistant_message=reply,
                )

            yield reply

        elif intent == "memory_query":
            summary_keywords = [
                "about me",
                "know about me",
                "everything you know",
                "who am i",
                "do you know me",
            ]
            cleaned_message = message.lower().strip()
            is_summary = any(
                kw in cleaned_message for kw in summary_keywords
            )

            all_memories = self.memory_service.get_all()

            if is_summary:
                print("[MEMORY] retrieved all memories for summary")
                relevant = all_memories
            else:
                relevant = self.memory_retriever.retrieve(
                    message,
                    all_memories,
                )
                print("[MEMORY] retrieved")

            for chunk in self.stream_chat_pipeline.run(
                message,
                relevant,
            ):
                yield chunk

        elif intent == "calculator":
            result = self.calculator.calculate(message)
            self.conversation_service.save(
                user_message=message,
                assistant_message=result,
            )
            yield result

        elif intent == "web_search":
            result = self.web_search.search(message)
            self.conversation_service.save(
                user_message=message,
                assistant_message=result,
            )
            yield result

        elif intent == "tool":
            result = self.tool_execution.execute(message)
            self.conversation_service.save(
                user_message=message,
                assistant_message=result,
            )
            yield result

        elif intent == "chat":
            for chunk in self.stream_chat_pipeline.run(
                message,
                memories=[],
            ):
                yield chunk

        else:
            print(
                f"[Router] Forwarding unimplemented intent '{intent}' to Streaming Chat LLM"
            )
            yield f"[LIFE-OS: Routing intent '{intent}' to chat engine]\n"
            for chunk in self.stream_chat_pipeline.run(
                message,
                memories=[],
            ):
                yield chunk
