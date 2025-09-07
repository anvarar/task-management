from entities.dataclass.task_entity import TaskEntity
from entities.task import TaskModel
from interfaces.TaskRepositoryInterface import TaskRepositoryInterface


class SqlAlchemyTaskRepository(TaskRepositoryInterface):
    def __init__(self, session):
        self.session = session

    def add(self, task: TaskEntity):
        model = TaskModel(title=task.title, description=task.description, status=task.status)
        self.session.add(model)
        self.session.commit()
        return TaskModel(id=model.id, title=model.title, description=model.description, status=model.status,
                         created_at=model.created_at,
                         updated_at=model.updated_at)

    def get_task(self, task_id):
        # task_id should be primary key
        model = self.session.get(TaskModel, task_id)
        if not model:
            return None
        else:
            print(model)
            return model

    def update_task(self, task_id_data):
        model = self.session.get(TaskModel, task_id_data.id)
        if not model:
            raise ValueError("No data Found")
        model.id = task_id_data.id
        model.title = task_id_data.title
        model.description = task_id_data.description
        model.status = task_id_data.status
        self.session.commit()

    def delete_task(self, task_id):
        model = self.session.get(TaskModel, task_id)
        if model:
            self.session.delete(model)
            self.session.commit()