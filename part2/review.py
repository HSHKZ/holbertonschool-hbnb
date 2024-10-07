from app.models.hbnb_model import HbnbModel

class Review(HbnbModel):
    def __init__(self, user_id, place_id, text):
        super().__init__()
        self.user_id = user_id
        self.place_id = place_id
        self.text = text

    def to_dict(self):
        review_dict = super().to_dict()
        review_dict.update({
            'user_id': self.user_id,
            'place_id': self.place_id,
            'text': self.text
        })
        return review_dict
