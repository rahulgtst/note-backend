import uuid
from sqlalchemy import Column, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base


class User(Base):
    __tablename__ = "users"

    _id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    password = Column(String(200), nullable=False)
    lastUpdate = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    createdOn = Column(DateTime, default=datetime.utcnow)

    notes = relationship("Note", back_populates="owner", cascade="all, delete-orphan")


class Note(Base):
    __tablename__ = "notes"

    _id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=True)
    lastUpdate = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    createdOn = Column(DateTime, default=datetime.utcnow)

    userId = Column(String(36), ForeignKey("users._id", ondelete="CASCADE"), nullable=False)
    owner = relationship("User", back_populates="notes")
