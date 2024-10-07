from app.models.hbnb_model import HbnbModel

class User(HbnbModel):
    def __init__(self, email, password, first_name=None, last_name=None):
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def to_dict(self):
        user_dict = super().to_dict()
        user_dict.update({
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name
        })
        return user_dict
