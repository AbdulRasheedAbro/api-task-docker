from datetime import datetime

from fastapi import APIRouter, HTTPException, Response
from pydantic import BaseModel

from app.service import TaskNotFound, TaskService


class TaskCreate(BaseModel):
    title: str


class TaskOut(BaseModel):
    id: int
    title: str
    done: bool
    created_at: datetime


def build_router(service: TaskService) -> APIRouter:
    router = APIRouter()

    @router.post("/tasks", response_model=TaskOut, status_code=201)
    def create_task(body: TaskCreate):
        try:
            return service.create_task(body.title)
        except ValueError as e:
            raise HTTPException(status_code=422, detail=str(e))

    @router.get("/tasks", response_model=list[TaskOut])
    def list_tasks():
        return service.list_tasks()

    @router.get("/tasks/{task_id}", response_model=TaskOut)
    def get_task(task_id: int):
        try:
            return service.get_task(task_id)
        except TaskNotFound:
            raise HTTPException(status_code=404, detail="task not found")

    @router.delete("/tasks/{task_id}", status_code=204)
    def delete_task(task_id: int):
        try:
            service.delete_task(task_id)
        except TaskNotFound:
            raise HTTPException(status_code=404, detail="task not found")
        return Response(status_code=204)

    return router