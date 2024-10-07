class InMemoryRepository:
    def __init__(self):
        self.storage = {}

    def add(self, obj):
        obj_id = obj.get('id')
        if obj_id in self.storage:
            raise ValueError("Object already exists")
        self.storage[obj_id] = obj

    def get_all(self):
        return list(self.storage.values())
