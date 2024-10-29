from functools import wraps
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify
from app.models.user import User
from app import db
from .admin import admin_required
from flask import Blueprint, request, jsonify

def admin_required(fn):
    @wraps(fn)
    @jwt_required()
    def wrapper(*args, **kwargs):
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        
        if not user.is_admin:
            return jsonify({"error": "Admin access required"}), 403
        return fn(*args, **kwargs)
    return wrapper

admin_bp = Blueprint('admin', __name__)

# Créer un nouvel utilisateur
@admin_bp.route('/api/v1/admin/users', methods=['POST'])
@admin_required
def create_user():
    data = request.get_json()
    user = User(name=data['name'], email=data['email'], is_admin=data.get('is_admin', False))
    user.set_password(data['password'])

    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201

# Modification des informations de n'importe quel utilisateur
@admin_bp.route('/api/v1/admin/users/<int:user_id>', methods=['PUT'])
@admin_required
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    if 'password' in data:
        user.set_password(data['password'])
    db.session.commit()
    return jsonify(user.to_dict()), 200
