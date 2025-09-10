from typing import Optional

from pydantic import BaseModel


class TaskInSchema(BaseModel):
    title: str
    status: Optional[str]
    description: Optional[str] = None