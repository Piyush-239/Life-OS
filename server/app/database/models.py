from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database.base import Base


class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True)
    user_message = Column(String)
    assistant_message = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    memories = relationship("Memory", back_populates="conversation")


class Memory(Base):
    __tablename__ = "memories"

    id = Column(Integer, primary_key=True)

    category = Column(String, nullable=False)

    key = Column(String, nullable=False)

    value = Column(String, nullable=False)

    source_conversation_id = Column(
        Integer,
        ForeignKey("conversations.id"),
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )

    conversation = relationship(
        "Conversation",
        back_populates="memories",
    )