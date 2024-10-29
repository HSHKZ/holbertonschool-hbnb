from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.user import User
from app import db

users_bp = Blueprint('users', __name__)

# Modification des informations de l'utilisateur connecté
@users_bp.route('/api/v1/users/me', methods=['PUT'])
@jwt_required()
def update_user():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    data = request.get_json()
    user.name = data.get('name', user.name)
    # Empêche la modification de l'email et du mot de passe
    db.session.commit()
    return jsonify(user.to_dict()), 200
