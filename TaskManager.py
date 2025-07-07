from datetime import datetime
from typing import List, Optional

from Task import Task, logger
from TaskStatus import TaskStatus
from TaskStorage import TaskStorage


def _format_datetime(iso_string: str) -> str:
    """Format ISO datetime string for display"""
    try:
        dt = datetime.fromisoformat(iso_string.replace('Z', '+00:00'))
        return dt.strftime("%Y-%m-%d %H:%M")
    except ValueError:
        return iso_string


def _display_tasks(tasks: List[Task]):
    """Display tasks in a formatted way"""
    status_emojis = {
        TaskStatus.TODO: "⏳",
        TaskStatus.IN_PROGRESS: "🔄",
        TaskStatus.DONE: "✅"
    }

    print("\n" + "=" * 80)
    print("📋 TASK LIST")
    print("=" * 80)

    for task in sorted(tasks, key=lambda t: t.id):
        emoji = status_emojis.get(task.status, "❓")
        created = _format_datetime(task.created_at)
        updated = _format_datetime(task.updated_at)

        print(f"{emoji} ID: {task.id} | {task.description}")
        print(f"   Status: {task.status.value.upper()}")
        print(f"   Created: {created} | Updated: {updated}")
        print("-" * 80)


class TaskManager:
    """Main task management class"""

    def __init__(self, storage_path: str = "tasks.json"):
        self.storage = TaskStorage(storage_path)

    def add_task(self, description: str) -> bool:
        """Add a new task"""
        if not description.strip():
            logger.error("Task description cannot be empty")
            return False

        tasks = self.storage.load_tasks()
        new_id = max((task.id for task in tasks), default=0) + 1
        new_task = Task(id=new_id, description=description.strip())
        tasks.append(new_task)

        if self.storage.save_tasks(tasks):
            print(f"✓ Task '{description}' added successfully (ID: {new_id})")
            return True
        return False

    def update_task(self, task_id: int, description: str) -> bool:
        """Update task description"""
        if not description.strip():
            logger.error("Task description cannot be empty")
            return False

        tasks = self.storage.load_tasks()
        for task in tasks:
            if task.id == task_id:
                task.description = description.strip()
                task.update_timestamp()
                if self.storage.save_tasks(tasks):
                    print(f"✓ Task ID {task_id} updated successfully")
                    return True
                return False

        print(f"❌ Task with ID {task_id} not found")
        return False

    def delete_task(self, task_id: int) -> bool:
        """Delete a task"""
        tasks = self.storage.load_tasks()
        original_count = len(tasks)
        tasks = [task for task in tasks if task.id != task_id]

        if len(tasks) == original_count:
            print(f"❌ Task with ID {task_id} not found")
            return False

        if self.storage.save_tasks(tasks):
            print(f"✓ Task ID {task_id} deleted successfully")
            return True
        return False

    def mark_task_status(self, task_id: int, status: TaskStatus) -> bool:
        """Mark task with specific status"""
        tasks = self.storage.load_tasks()
        for task in tasks:
            if task.id == task_id:
                if task.status == status:
                    print(f"ℹ️  Task ID {task_id} is already {status.value}")
                    return True

                task.status = status
                task.update_timestamp()
                if self.storage.save_tasks(tasks):
                    print(f"✓ Task ID {task_id} marked as {status.value}")
                    return True
                return False

        print(f"❌ Task with ID {task_id} not found")
        return False

    def mark_in_progress(self, task_id: int) -> bool:
        """Mark task as in progress"""
        return self.mark_task_status(task_id, TaskStatus.IN_PROGRESS)

    def mark_done(self, task_id: int) -> bool:
        """Mark task as done"""
        return self.mark_task_status(task_id, TaskStatus.DONE)

    def list_tasks(self, status_filter: Optional[str] = None) -> List[Task]:
        """List tasks with optional status filter"""
        tasks = self.storage.load_tasks()

        if not tasks:
            print("📝 No tasks found")
            return []

        if status_filter:
            try:
                filter_status = TaskStatus(status_filter)
                tasks = [task for task in tasks if task.status == filter_status]
                if not tasks:
                    print(f"📝 No {status_filter} tasks found")
                    return []
            except ValueError:
                print(f"❌ Invalid status: {status_filter}")
                print(f"Valid statuses: {', '.join([s.value for s in TaskStatus])}")
                return []

        # Display tasks
        _display_tasks(tasks)
        return tasks
