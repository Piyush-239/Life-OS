from app.database.models import Conversation
from app.database.session import SessionLocal


class ConversationService:
    def save(self, user_message: str, assistant_message: str) -> Conversation:
        session = SessionLocal()

        try:
            conversation = Conversation(
                user_message=user_message,
                assistant_message=assistant_message,
            )

            session.add(conversation)
            session.commit()
            session.refresh(conversation)
            return conversation

        finally:
            session.close()