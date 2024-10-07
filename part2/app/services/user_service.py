# app/services/user_service.py

from app.models.user import User

class UserService:
    _users = {}

    @staticmethod
    def create_user(data):
        """Create a new user and store in the repository"""
        new_user = User(
            email=data['email'],
            password=data['password'],
            first_name=data.get('first_name'),
            last_name=data.get('last_name')
        )
        UserService._users[new_user.id] = new_user
        return new_user

    @staticmethod
    def get_all_users():
        """Retrieve all users"""
        return list(UserService._users.values())

    @staticmethod
    def get_user_by_id(user_id):
        """Retrieve a user by their ID"""
        return UserService._users.get(user_id)

    @staticmethod
    def update_user(user_id, data):
        """Update an existing user's information"""
        user = UserService._users.get(user_id)
        if not user:
            return None
        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)
        return user
