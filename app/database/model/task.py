from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from app.database.base import Base
from app.database.mixins.serializer import Serializer


class Task(Base, Serializer):
    __tablename__ = "task"

    task_uid = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    solution_time = Column(Integer, nullable=False)  # in minutes
    color = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.now, nullable=False)

    actions = relationship("Action", back_populates="task")

    # for logging
    def __repr__(self):
        return f"<Task(task_uid={self.task_uid}, title='{self.title}')>"
