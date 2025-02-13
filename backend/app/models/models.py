
from sqlalchemy import Column, String, Integer, DateTime

from backend.app.core.mysql import Base


class Message(Base):
    __tablename__ = 'message'
    __table_args__ = {'mysql_charset': 'utf8mb4'}

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    message = Column(String(255), nullable=True)
    message_time = Column(DateTime, nullable=False)