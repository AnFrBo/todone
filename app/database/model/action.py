from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base import Base
from app.database.mixins.serializer import Serializer

class Action(Base, Serializer):
    __tablename__ = "action"

    action_uid = Column(Integer, primary_key=True)
    user_uid = Column(Integer, ForeignKey("user.user_uid"), nullable=False)
    task_uid = Column(Integer, ForeignKey("task.task_uid"), nullable=False)
    started_at = Column(DateTime, nullable=True)
    finished_at = Column(DateTime, nullable=True)
    last_update = Column(DateTime, default=datetime.now, nullable=False)

    user = relationship("User", back_populates="actions")
    task = relationship("Task", back_populates="actions")

    # for logging
    def __repr__(self):
        return f"<Action(action_uid={self.action_uid}, user_uid={self.user_uid}, task_uid={self.task_uid})>"
