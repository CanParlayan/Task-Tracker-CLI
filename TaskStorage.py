import json
from pathlib import Path
from typing import List

from Task import logger, Task


class TaskStorage:
    def __init__(self, file_path: str = "tasks.json"):
        self.file_path = Path(file_path)
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        """Create file if it doesn't exist"""
        if not self.file_path.exists():
            self.save_tasks([])

    def load_tasks(self) -> List[Task]:
        """Load tasks from JSON file"""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return [Task.from_dict(task_data) for task_data in data]
        except (json.JSONDecodeError, FileNotFoundError) as e:
            logger.error(f"Error loading tasks: {e}")
            return []

    def save_tasks(self, tasks: List[Task]) -> bool:
        """Save tasks to JSON file"""
        try:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump([task.to_dict() for task in tasks], file, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            logger.error(f"Error saving tasks: {e}")
            return False
