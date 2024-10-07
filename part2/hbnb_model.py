import uuid
from datetime import datetime

class HbnbModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Update 'updated_at' attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the instance"""
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
