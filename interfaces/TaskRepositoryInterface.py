from abc import abstractmethod


class TaskRepositoryInterface:
    @abstractmethod
    def add(self, task):
        pass

    @abstractmethod
    def get_task(self, task_id):
        pass

    @abstractmethod
    def update_task(self, task_id_data):
        pass

    @abstractmethod
    def delete_task(self, task_id):
        pass
