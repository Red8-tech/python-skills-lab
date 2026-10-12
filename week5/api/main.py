import os

from dotenv import load_dotenv
from fastapi import (
    Depends,
    FastAPI,
    HTTPException,
    Query,
    status,
)
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, Field


load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

if not API_TOKEN:
    raise RuntimeError("API_TOKEN is missing from .env")


app = FastAPI(
    title="Task Management API",
    description="A practice REST API built with FastAPI and Pydantic.",
    version="1.0.0",
)


security = HTTPBearer()

def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    if credentials.credentials != API_TOKEN:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )
    
    return credentials.credentials


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str = Field(default="", max_length=500)
    completed: bool = False

class Task(TaskCreate):
    id: int


tasks: dict[int, Task] = {}
next_id = 1


@app.get("/")
def home():
    return {"message": "Welcome to the Task Management API"}


# 1. Create task — POST /tasks
@app.post(
    "/tasks",
    response_model=Task,
    status_code=status.HTTP_201_CREATED
)
def create_task(
    task_data: TaskCreate,
    token: str = Depends(verify_token),
):
    global next_id

    task = Task(id=next_id, **task_data.model_dump())
    tasks[next_id] = task
    next_id += 1

    return task


# 2. List tasks — GET /tasks
@app.get(
    "/tasks",
    response_model=list[Task]
)
def list_tasks(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1, le=100),
    token: str = Depends(verify_token),
):
    task_list = list(tasks.values())
    return task_list[skip:skip + limit]


# 3. Get one task — GET /tasks/{task_id}
@app.get(
    "/tasks/{task_id}",
    response_model=Task
)
def get_task(
    task_id: int,
    token: str = Depends(verify_token),
):
    task = tasks.get(task_id)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


# 4. Update task — PUT /tasks/{task_id}
@app.put(
    "/tasks/{task_id}",
    response_model=Task
)
def update_task(
    task_id: int,
    updated_data: TaskCreate,
    token: str = Depends(verify_token),
):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    updated_task = Task(id=task_id, **updated_data.model_dump())
    tasks[task_id] = updated_task

    return updated_task


# 5. Delete task — DELETE /tasks/{task_id}
@app.delete(
    "/tasks/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_task(
    task_id: int,
    token: str = Depends(verify_token),
):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    del tasks[task_id]
