# app/services/amenity_service.py

from app.models.amenity import Amenity

class AmenityService:
    _amenities = {}

    @staticmethod
    def create_amenity(data):
        """Create a new amenity and store it"""
        new_amenity = Amenity(name=data['name'])
        AmenityService._amenities[new_amenity.id] = new_amenity
        return new_amenity

    @staticmethod
    def get_all_amenities():
        """Retrieve all amenities"""
        return list(AmenityService._amenities.values())

    @staticmethod
    def get_amenity_by_id(amenity_id):
        """Retrieve an amenity by ID"""
        return AmenityService._amenities.get(amenity_id)

    @staticmethod
    def update_amenity(amenity_id, data):
        """Update an existing amenity"""
        amenity = AmenityService._amenities.get(amenity_id)
        if not amenity:
            return None
        amenity.name = data.get('name', amenity.name)
        return amenity
