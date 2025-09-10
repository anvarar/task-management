from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class TaskEntity:
    title: str
    description: str
    status: str
    id: Optional[int] = field(default=None)
