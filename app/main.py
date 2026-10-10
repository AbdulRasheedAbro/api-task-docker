import os
from fastapi import FastAPI
from app.repository.postgres import PostgresTaskRepository
# from app.repository.memory import InMemoryTaskRepository
from app.service import TaskService
from app.routes import build_router

repo = PostgresTaskRepository(os.environ["DATABASE_URL"])
# repo = InMemoryTaskRepository()
app = FastAPI()
app.include_router(build_router(TaskService(repo)))