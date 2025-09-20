import json
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(title, due_date=None):
    tasks = load_tasks()
    tasks.append({"title": title, "due_date": due_date, "done": False})
    save_tasks(tasks)
    print(f"✅ Task added: {title}")

def list_tasks():
    tasks = load_tasks()
    for i, task in enumerate(tasks, 1):
        status = "✔" if task["done"] else "✗"
        due = f"(due {task['due_date']})" if task["due_date"] else ""
        print(f"{i}. [{status}] {task['title']} {due}")

if __name__ == "__main__":
    print("Simple Task Manager")
    add_task("Finish Deloitte application", "2025-09-30")
    list_tasks()
