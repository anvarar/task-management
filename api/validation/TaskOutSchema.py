from pydantic import BaseModel
from datetime import datetime


class TaskOutSchema(BaseModel):
    id: int
    title: str
    description: str
    status: str
    created_at: datetime
    updated_at: datetime

    def format_task(model, schema_cls):
        data = {
            k: v for k, v in vars(model).items()
        }
        print("#"*50)
        print(data)
        return schema_cls(**data)
    # or
    # @staticmethod
    # def format_task(task_instance):
    #     task_dict = {c.name: getattr(task_instance, c.name) for c in task_instance.__table__.columns}
    #     return TaskOutSchema(**task_dict)