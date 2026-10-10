from datetime import datetime, timezone

from app.repository.base import TaskRepository


class InMemoryTaskRepository(TaskRepository):
    def __init__(self):
        self._tasks: dict[int, dict] = {}
        self._next_id = 1

    def add(self, title: str) -> dict:
        task = {
            "id": self._next_id,
            "title": title,
            "done": False,
            "created_at": datetime.now(timezone.utc),
        }
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task

    def get(self, task_id: int) -> dict | None:
        return self._tasks.get(task_id)

    def list(self) -> list[dict]:
        return list(self._tasks.values())

    def delete(self, task_id: int) -> bool:
        return self._tasks.pop(task_id, None) is not None