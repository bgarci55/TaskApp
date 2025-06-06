import uvicorn
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
import task_manager
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "name": "World"})
app.mount("/static", StaticFiles(directory="static"), name="static")

class TaskIn(BaseModel):
    title: str

class TaskUpdate(BaseModel):
    title: str

class TaskStatus(BaseModel):
    status: str

@app.post("/tasks")
def add_task(task: TaskIn):
    return task_manager.add(task.title)

@app.put("/tasks/{task_id}")
def update_task(task_id: int, update: TaskUpdate):
    return task_manager.update(task_id, update.title)

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    return task_manager.delete(task_id)

@app.post("/tasks/{task_id}/status")
def mark_complete(task_id: int):
    return task_manager.mark_complete(task_id)

@app.get("/")
def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
