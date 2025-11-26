from datetime import datetime
from sqlalchemy import (
    Column, Integer, String, Boolean, DateTime
)
from .db import Base


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    description = Column(String(500))
    completed = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __str__(self):
        return f"Task(id={self.id}, title='{self.title}', completed={self.completed})"

    def __repr__(self):
        return f"Task(id={self.id}, title='{self.title}', completed={self.completed})"
