from typing import Optional

from pydantic import BaseModel


class TaskInSchema(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[str]
