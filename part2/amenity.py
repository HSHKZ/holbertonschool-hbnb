from app.models.hbnb_model import HbnbModel

class Amenity(HbnbModel):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def to_dict(self):
        amenity_dict = super().to_dict()
        amenity_dict.update({
            'name': self.name
        })
        return amenity_dict
