import json
import os
from fastapi import HTTPException

FILE_PATH = "data/task_data.json"

def load_tasks():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE_PATH, "w") as f:
        json.dump(tasks, f, indent=2)

def get_new_id(tasks):
    return max([t["id"] for t in tasks], default=0) + 1

def add(title):
    tasks = load_tasks()
    new_id = get_new_id(tasks)
    tasks[new_id] = {"title": title, "progress": 0}
    print("Task added successfully: " + title + " ( TaskID:", new_id, ")")

def update(task_id, new_title):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = new_title
            save_tasks(tasks)
            return task
    raise HTTPException(status_code=404, detail="Task not found.")


# add logic for deleting tasks
def delete(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            return task
    raise HTTPException(status_code=404, detail="Task not found.")

def mark_in_progress(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["progress"] = 1
            save_tasks(tasks)
            return task
    raise HTTPException(status_code=404, detail="Task not found.")

def mark_complete(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["progress"] = 2
            save_tasks(tasks)
            return task
    raise HTTPException(status_code=404, detail="Task not found.")




# def list_todo():
#
# def list_in_progress():
#
# def list_complete():

