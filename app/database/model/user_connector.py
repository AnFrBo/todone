from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from app.database.base import Base
from app.database.mixins.serializer import Serializer

class UserConnector(Base, Serializer):
    __tablename__ = "user_connector"

    user_connector_uid = Column(Integer, primary_key=True)
    user_id_1 = Column(Integer, ForeignKey("user.user_uid"), nullable=False)
    user_id_2 = Column(Integer, ForeignKey("user.user_uid"), nullable=False)
    status = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.now, nullable=False)

    # for logging
    def __repr__(self):
        return f"<UserConnector(user_connector_uid={self.user_connector_uid}, user_id_1={self.user_id_1}, user_id_2={self.user_id_2})>"

