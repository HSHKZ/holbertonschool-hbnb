from app.repositories.in_memory_repository import InMemoryRepository
from app.services.hbnb_service import HbnbService

class HbnbFacade:
    def __init__(self):
        self.repository = InMemoryRepository()
        self.service = HbnbService(self.repository)

    def get_all_objects(self):
        return self.service.get_all_objects()

    def add_object(self, obj):
        self.service.add_object(obj)
