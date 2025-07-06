from datetime import datetime

from json_functions import *
from task import *


def add_task(file_path, description=None):
    if not os.path.exists(file_path):
        tasks = []
    else:
        tasks = json_read(file_path)
        if tasks is None:
            tasks = []
    new_id = max((task["id"] for task in tasks), default=0) + 1
    task = Task(new_id, description)
    tasks.append(task.to_dict())

    if json_write(file_path, tasks):
        print(f"Task '{description}' added successfully (ID {new_id})")


def update_task(file_path, task_id, description=None):
    tasks = json_read(file_path)
    if tasks is None:
        return
    task_id = int(task_id)

    for task in tasks:
        if task["id"] == task_id:
            if description is not None:
                task["description"] = description
            task["updatedAt"] = datetime.now().isoformat()
            break
    else:
        print(f"Task with ID {task_id} not found.")
        return
    if json_write(file_path, tasks):
        print(f"Task ID {task_id} updated successfully.")


def delete_task(file_path, task_id):
    tasks = json_read(file_path)
    if tasks is None:
        return
    task_id = int(task_id)
    tasks = [task for task in tasks if task["id"] != task_id]
    if json_write(file_path, tasks):
        print(f"Task ID {task_id} deleted successfully.")
    else:
        print(f"Failed to delete task ID {task_id}.")


def mark_in_progress(file_path, task_id):
    tasks = json_read(file_path)
    if tasks is None:
        return
    task_id = int(task_id)
    for task in tasks:
        if task["id"] == task_id:
            if task["status"] != "todo":
                print(f"Task ID {task_id} is already in progress or done.")
                return
            task["status"] = "in-progress"

            task["updatedAt"] = datetime.now().isoformat()
            if json_write(file_path, tasks):
                print(f"Task ID {task_id} marked as in-progress successfully.")
            else:
                print(f"Failed to update task ID {task_id}.")
            break
    else:
        print(f"Task with ID {task_id} not found.")
        return


def mark_done(file_path, task_id):
    tasks = json_read(file_path)
    if tasks is None:
        return
    task_id = int(task_id)
    for task in tasks:
        if task["id"] == task_id:
            if task["status"] == "done":
                print(f"Task ID {task_id} is already done.")
                return
            task["status"] = "done"
            task["updatedAt"] = datetime.now().isoformat()
            if json_write(file_path, tasks):
                print(f"Task ID {task_id} marked as done successfully.")
            else:
                print(f"Failed to update task ID {task_id}.")
            break
    else:
        print(f"Task with ID {task_id} not found.")
        return


def list_tasks(file_path, status=None):
    tasks = json_read(file_path)
    if tasks is None:
        return
    if not tasks:
        print("No tasks found.")
        return
    if status is None:
        for task in tasks:
            print(f"ID: {task['id']}, Description: {task['description']}, "
                  f"Status: {task['status']}, Created At: {task['createdAt'].replace('T', ' ')[:19]}, Updated At: "
                  f"{task['updatedAt'].replace('T', ' ')[:19]}")
    else:
        for task in tasks:
            if task['status'] == status:
                print(f"ID: {task['id']}, Description: {task['description']}, "
                      f"Status: {task['status']}, Created At: {task['createdAt'].replace('T', ' ')[:19]}, Updated At:"
                      f" {task['updatedAt'].replace('T', ' ')[:19]}")
