from app.models.hbnb_model import HbnbModel

class Place(HbnbModel):
    def __init__(self, name, description, city, price_per_night):
        super().__init__()
        self.name = name
        self.description = description
        self.city = city
        self.price_per_night = price_per_night
        self.amenities = []

    def to_dict(self):
        place_dict = super().to_dict()
        place_dict.update({
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'price_per_night': self.price_per_night,
            'amenities': [amenity.to_dict() for amenity in self.amenities]
        })
        return place_dict

    def add_amenity(self, amenity):
        """Link an amenity to the place"""
        if amenity not in self.amenities:
            self.amenities.append(amenity)
