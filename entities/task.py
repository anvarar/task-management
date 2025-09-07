from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from config.db import Base


class TaskModel(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=True)
    description = Column(String(255), nullable=True)
    status = Column(String(20), default="Not completed")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
