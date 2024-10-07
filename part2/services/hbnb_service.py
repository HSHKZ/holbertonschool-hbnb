class HbnbService:
    def __init__(self, repository):
        self.repository = repository
    
    def get_all_objects(self):
        return self.repository.get_all()

    def add_object(self, obj):
        self.repository.add(obj)
