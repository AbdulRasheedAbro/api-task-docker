import psycopg
from psycopg.rows import dict_row

from app.repository.base import TaskRepository


class PostgresTaskRepository(TaskRepository):
    def __init__(self, dsn: str):
        self.dsn = dsn

    def _conn(self):
        return psycopg.connect(self.dsn, row_factory=dict_row)

    def add(self, title: str) -> dict:
        # `with` commits on success and rolls back on error
        with self._conn() as conn:
            return conn.execute(
                "INSERT INTO tasks (title) VALUES (%s) RETURNING *",
                (title,),
            ).fetchone()

    def get(self, task_id: int) -> dict | None:
        with self._conn() as conn:
            return conn.execute(
                "SELECT * FROM tasks WHERE id = %s", (task_id,)
            ).fetchone()

    def list(self) -> list[dict]:
        with self._conn() as conn:
            return conn.execute("SELECT * FROM tasks ORDER BY id").fetchall()

    def delete(self, task_id: int) -> bool:
        with self._conn() as conn:
            cur = conn.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
            return cur.rowcount > 0