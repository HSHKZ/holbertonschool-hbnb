# app/services/place_service.py

from app.models.place import Place
from app.models.user import User

class PlaceService:
    _places = {}

    @staticmethod
    def create_place(data):
        """Create a new place and store it"""
        owner = User.get_user_by_id(data['owner_id'])
        if not owner:
            raise ValueError("Owner not found")
        
        new_place = Place(name=data['name'], price=data['price'], latitude=data['latitude'], longitude=data['longitude'], owner=owner)
        PlaceService._places[new_place.id] = new_place
        return new_place

    @staticmethod
    def get_all_places():
        """Retrieve all places"""
        return list(PlaceService._places.values())

    @staticmethod
    def get_place_by_id(place_id):
        """Retrieve a place by ID"""
        return PlaceService._places.get(place_id)

    @staticmethod
    def update_place(place_id, data):
        """Update an existing place"""
        place = PlaceService._places.get(place_id)
        if not place:
            return None
        place.name = data.get('name', place.name)
        place.price = data.get('price', place.price)
        place.latitude = data.get('latitude', place.latitude)
        place.longitude = data.get('longitude', place.longitude)
        return place
