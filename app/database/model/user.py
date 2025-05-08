from datetime import datetime

from sqlalchemy import Column, Date, DateTime, Integer, String
from sqlalchemy.orm import relationship

from app.database.base import Base
from app.database.mixins.serializer import Serializer


class User(Base, Serializer):
    __tablename__ = "user"

    user_uid = Column(Integer, primary_key=True)
    user_name = Column(String, nullable=False)
    user_mail = Column(String, nullable=True)
    user_birthday = Column(Date, nullable=True)
    created_at = Column(DateTime, default=datetime.now, nullable=False)

    actions = relationship("Action", back_populates="user")

    # for logging
    def __repr__(self):
        return f"<User(user_uid={self.user_uid}, user_name='{self.user_name}')>"
