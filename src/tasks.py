import json
from pathlib import Path

DATA_FILE = Path.home() / ".cli_tasks.json"

def load_tasks():
    if not DATA_FILE.exists():
        return []
    return json.loads(DATA_FILE.read_text())

def save_tasks(tasks):
    DATA_FILE.write_text(json.dumps(tasks, indent=2))

def add_task(title):
    tasks = load_tasks()
    tasks.append({"id": len(tasks)+1, "title": title, "done": False})
    save_tasks(tasks)

def list_tasks():
    return load_tasks()

def remove_task(task_id):
    tasks = load_tasks()
    new = [t for t in tasks if t["id"] != task_id]
    if len(new) == len(tasks):
        return False
    for i, t in enumerate(new, start=1):
        t["id"] = i
    save_tasks(new)
    return True
