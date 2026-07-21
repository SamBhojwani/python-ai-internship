from sqlalchemy import Column, Integer, String
from app.database import Base
from sqlalchemy import DateTime, ForeignKey, Text
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)


class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    category = Column(String, nullable=True)
    response_time_ms = Column(Integer, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)