from pydantic import BaseModel
from datetime import datetime


class TaskOutSchem(BaseModel):
    id: int
    title: str
    description: str
    created_at: datetime
    updated_at: datetime
