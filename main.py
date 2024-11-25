from fastapi import FastAPI, HTTPException, Path, Query, Header, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise Exception("API_KEY not set in environment variables")

# Create FastAPI app
app = FastAPI()

# Task database (in-memory for simulation)
task_db = [
    {"task_id": 1, "task_title": "Laboratory Activity", "task_desc": "Create Lab Act 2", "is_finished": False}
]

# Models
class Task(BaseModel):
    task_title: str
    task_desc: str
    is_finished: bool = False

# Middleware for API Key Authentication
def api_key_auth(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail={"error": "Unauthorized access. Invalid API key."})

# Helper functions
def find_task(task_id: int):
    return next((task for task in task_db if task["task_id"] == task_id), None)

# API Version 1
@app.get("/apiv1/tasks/{task_id}", dependencies=[Depends(api_key_auth)])
def get_task_v1(task_id: int = Path(..., gt=0)):
    task = find_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail={"error": "Task not found"})
    return {"status": "ok", "task": task}

@app.post("/apiv1/tasks", dependencies=[Depends(api_key_auth)])
def create_task_v1(task: Task):
    new_task_id = max(task["task_id"] for task in task_db) + 1 if task_db else 1
    new_task = task.dict()
    new_task["task_id"] = new_task_id
    task_db.append(new_task)
    return JSONResponse(content={"status": "ok", "task": new_task}, status_code=201)

@app.patch("/apiv1/tasks/{task_id}", dependencies=[Depends(api_key_auth)])
def update_task_v1(task_id: int, updated_task: Task):
    task = find_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail={"error": "Task not found"})
    task.update(updated_task.dict(exclude_unset=True))
    return JSONResponse(content={"status": "ok", "task": task}, status_code=204)

@app.delete("/apiv1/tasks/{task_id}", dependencies=[Depends(api_key_auth)])
def delete_task_v1(task_id: int):
    task = find_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail={"error": "Task not found"})
    task_db.remove(task)
    return JSONResponse(content={"status": "ok"}, status_code=204)

# API Version 2 (Enhanced with Exception Handling)
@app.get("/apiv2/tasks/{task_id}", dependencies=[Depends(api_key_auth)])
def get_task_v2(task_id: int = Path(..., gt=0)):
    task = find_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail={"error": "Task not found"})
    return {"status": "ok", "task": task}

@app.post("/apiv2/tasks", dependencies=[Depends(api_key_auth)])
def create_task_v2(task: Task):
    new_task_id = max((task["task_id"] for task in task_db), default=0) + 1
    new_task = task.dict()
    new_task["task_id"] = new_task_id
    task_db.append(new_task)
    return JSONResponse(content={"status": "ok", "task": new_task}, status_code=201)

@app.patch("/apiv2/tasks/{task_id}", dependencies=[Depends(api_key_auth)])
def update_task_v2(task_id: int, updated_task: Task):
    task = find_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail={"error": "Task not found"})
    task.update(updated_task.dict(exclude_unset=True))
    return JSONResponse(content={"status": "ok", "task": task}, status_code=204)

@app.delete("/apiv2/tasks/{task_id}", dependencies=[Depends(api_key_auth)])
def delete_task_v2(task_id: int):
    task = find_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail={"error": "Task not found"})
    task_db.remove(task)
    return JSONResponse(content={"status": "ok"}, status_code=204)
