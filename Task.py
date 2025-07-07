import logging
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import *

from TaskStatus import TaskStatus

# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class Task:
    """Task data class with better structure"""
    id: int
    description: str
    status: TaskStatus = TaskStatus.TODO
    created_at: str = None
    updated_at: str = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().isoformat()
        if self.updated_at is None:
            self.updated_at = self.created_at

    def update_timestamp(self):
        """Update the updated_at timestamp"""
        self.updated_at = datetime.now().isoformat()

    def to_dict(self) -> Dict[str, Any]:
        """Convert task to dictionary with proper status conversion"""
        data = asdict(self)
        data['status'] = self.status.value
        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Task':
        """Create Task instance from dictionary"""
        return cls(
            id=data['id'],
            description=data['description'],
            status=TaskStatus(data['status']),
            created_at=data.get('created_at', data.get('createdAt')),  # Backward compatibility
            updated_at=data.get('updated_at', data.get('updatedAt'))  # Backward compatibility
        )
