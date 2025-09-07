from entities.dataclass.task_entity import TaskEntity
from interfaces import TaskRepositoryInterface


class TaskService:
    def __init__(self, task_repo: TaskRepositoryInterface):
        self.repo = task_repo

    def create_task(self, title: str, description: str, status: str):
        task = TaskEntity(title=title, description=description, status=status)
        return self.repo.add(task)

    def get_task(self, task_id: int):
        return self.repo.get_task(task_id)

    def update_task(self, task_id: int, **fields):
        existing_task_id_data = self.repo.get_task(task_id)
        if not existing_task_id_data:
            raise ValueError(f"No data found for task_id:{task_id}")
        updated_task_id_data = TaskEntity(id=existing_task_id_data.id,
                                          title=fields.get('title', existing_task_id_data.title),
                                          description=fields.get('description', existing_task_id_data.description),
                                          status=fields.get('status', existing_task_id_data.status))
        return self.repo.update_task(updated_task_id_data)

    def delete_task(self,task_id):
        self.repo.delete_task(task_id)
