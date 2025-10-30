from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")


engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class RedditThread(Base):
    __tablename__ = "reddit_threads"
    id = Column(Integer, primary_key=True, index=True)
    subreddit = Column(String, index=True)
    question = Column(String)
    context = Column(Text)  # raw reddit data in text form

    chats = relationship("ChatMessage", back_populates="thread")


class ChatMessage(Base):
    __tablename__ = "chat_messages"
    id = Column(Integer, primary_key=True, index=True)
    thread_id = Column(Integer, ForeignKey("reddit_threads.id"))
    role = Column(String)  # 'user' or 'assistant'
    content = Column(Text)

    thread = relationship("RedditThread", back_populates="chats")


def init_db():
    Base.metadata.create_all(bind=engine)
