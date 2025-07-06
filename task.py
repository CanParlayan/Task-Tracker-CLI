from datetime import datetime


class Task:
    VALID_STATUSES = ["todo", "in-progress", "done"]

    def __init__(self, task_id, description, status="todo"):
        self.id = task_id
        self.description = description
        if status not in self.VALID_STATUSES:
            raise ValueError(f"Invalid status: {status}. Valid statuses are: {self.VALID_STATUSES}")
        self.status = status
        self.createdAt = datetime.now().isoformat()
        self.updatedAt = self.createdAt

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt,
        }
