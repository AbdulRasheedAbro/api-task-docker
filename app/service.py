from app.repository.base import TaskRepository


class TaskNotFound(Exception):
    pass


class TaskService:
    def __init__(self, repo: TaskRepository):
        self.repo = repo

    def create_task(self, title: str) -> dict:
        title = title.strip()
        if not title:
            raise ValueError("title must not be empty")
        return self.repo.add(title)

    def get_task(self, task_id: int) -> dict:
        task = self.repo.get(task_id)
        if task is None:
            raise TaskNotFound(task_id)
        return task

    def list_tasks(self) -> list[dict]:
        return self.repo.list()

    def delete_task(self, task_id: int) -> None:
        if not self.repo.delete(task_id):
            raise TaskNotFound(task_id)