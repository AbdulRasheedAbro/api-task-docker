from abc import ABC, abstractmethod


class TaskRepository(ABC):
    @abstractmethod
    def add(self, title: str) -> dict: ...

    @abstractmethod
    def get(self, task_id: int) -> dict | None: ...

    @abstractmethod
    def list(self) -> list[dict]: ...

    @abstractmethod
    def delete(self, task_id: int) -> bool: ...