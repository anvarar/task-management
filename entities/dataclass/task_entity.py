from datetime import datetime
from dataclasses import dataclass


@dataclass
class TaskEntity:
    id: int
    title: str
    description: str
    status: str
