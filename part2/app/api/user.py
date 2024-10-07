# app/api/user.py

from flask import request
from flask_restx import Namespace, Resource, fields
from app.services.user_service import UserService

user_ns = Namespace('users', description='User management operations')

user_model = user_ns.model('User', {
    'id': fields.String(readOnly=True, description='The user unique identifier'),
    'email': fields.String(required=True, description='The user email address'),
    'first_name': fields.String(description='First name of the user'),
    'last_name': fields.String(description='Last name of the user')
})

user_create_model = user_ns.model('UserCreate', {
    'email': fields.String(required=True, description='The user email address'),
    'password': fields.String(required=True, description='The user password'),
    'first_name': fields.String(description='First name of the user'),
    'last_name': fields.String(description='Last name of the user')
})

user_update_model = user_ns.model('UserUpdate', {
    'first_name': fields.String(description='First name of the user'),
    'last_name': fields.String(description='Last name of the user')
})

@user_ns.route('/')
class UserList(Resource):
    @user_ns.marshal_list_with(user_model)
    def get(self):
        """Retrieve a list of all users"""
        return UserService.get_all_users(), 200

    @user_ns.expect(user_create_model)
    @user_ns.marshal_with(user_model, code=201)
    def post(self):
        """Create a new user"""
        data = request.json
        return UserService.create_user(data), 201

@user_ns.route('/<string:user_id>')
class User(Resource):
    @user_ns.marshal_with(user_model)
    def get(self, user_id):
        """Retrieve a user by ID"""
        user = UserService.get_user_by_id(user_id)
        if user:
            return user, 200
        user_ns.abort(404, "User not found")

    @user_ns.expect(user_update_model)
    @user_ns.marshal_with(user_model)
    def put(self, user_id):
        """Update a user's information"""
        data = request.json
        user = UserService.update_user(user_id, data)
        if user:
            return user, 200
        user_ns.abort(404, "User not found")
