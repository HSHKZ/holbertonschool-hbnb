from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.place import Place
from app import db

places_bp = Blueprint('places', __name__)

# Création d'une place par un utilisateur authentifié
@places_bp.route('/api/v1/places', methods=['POST'])
@jwt_required()
def create_place():
    data = request.get_json()
    user_id = get_jwt_identity()

    place = Place(name=data['name'], owner_id=user_id)
    db.session.add(place)
    db.session.commit()
    return jsonify(place.to_dict()), 201

# Modification d'une place existante, seulement si l'utilisateur en est le propriétaire
@places_bp.route('/api/v1/places/<int:place_id>', methods=['PUT'])
@jwt_required()
def update_place(place_id):
    user_id = get_jwt_identity()
    place = Place.query.get(place_id)

    if place.owner_id != user_id:
        return jsonify({"error": "Permission denied"}), 403

    data = request.get_json()
    place.name = data.get('name', place.name)
    db.session.commit()
    return jsonify(place.to_dict()), 200
