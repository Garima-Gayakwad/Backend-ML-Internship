from fastapi import FastAPI, HTTPException
from typing import Optional
from models import Task
import task_service
app = FastAPI(title="Garima's Task Manager API")

@app.get("/")
def home():
    return {"message": "Welcome to the Task Manager API!"}

@app.post("/tasks") # POST /tasks -> Create a new task
def add_task(task: Task):
    try:
        return task_service.create_task(task)
    except task_service.DuplicateTaskID as e:
        # HTTP 400 Bad Request if user gives a duplicate ID
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/tasks") # GET /tasks -> Get all tasks (with optional query param ?completed=true)
def get_tasks(completed: Optional[bool] = None):
    return {"tasks": task_service.get_all_tasks(completed)}

@app.get("/tasks/{task_id}") # GET /tasks/{task_id} -> Get task by ID
def get_task(task_id: int):
    try:
        return task_service.get_task_by_id(task_id)
    except task_service.TaskNotFound as e:
        # HTTP 404 Not Found
        raise HTTPException(status_code=404, detail=str(e))

@app.put("/tasks/{task_id}") # PUT /tasks/{task_id} -> Update task
def update_task(task_id: int, task: Task):
    try:
        return task_service.update_task(task_id, task)
    except task_service.TaskNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.delete("/tasks/{task_id}") # DELETE /tasks/{task_id} -> Delete task
def delete_task(task_id: int):
    try:
        return task_service.delete_task(task_id)
    except task_service.TaskNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))