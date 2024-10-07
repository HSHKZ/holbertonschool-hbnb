# app/models/place.py

import uuid

class Place:
    def __init__(self, name, price, latitude, longitude, owner):
        self.id = str(uuid.uuid4())
        self.name = name
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner  # Reference to a User object
