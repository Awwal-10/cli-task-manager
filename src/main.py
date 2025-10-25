import sys
import json
import os

TODO_FILE = "todo.json"

def load_todos():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return json.load(f)

def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f)

def add_task(task):
    todos = load_todos()
    todos.append(task)
    save_todos(todos)
    print(f"Added: {task}")

def list_tasks():
    todos = load_todos()
    if not todos:
        print("No tasks yet!")
    else:
        for i, task in enumerate(todos, 1):
            print(f"{i}. {task}")

def remove_task(index):
    todos = load_todos()
    try:
        removed = todos.pop(index - 1)
        save_todos(todos)
        print(f"Removed: {removed}")
    except IndexError:
        print("Invalid task number.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 src/main.py [add/list/rm] [task]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        add_task(" ".join(sys.argv[2:]))
    elif command == "list":
        list_tasks()
    elif command == "rm":
        if len(sys.argv) < 3:
            print("Please provide a task number to remove.")
        else:
            remove_task(int(sys.argv[2]))
    else:
        print("Unknown command.")
