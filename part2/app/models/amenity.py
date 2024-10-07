# app/models/amenity.py

import uuid

class Amenity:
    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
