from flask import Blueprint, request, jsonify
from app.models.amenity import Amenity
from app import db
from .admin import admin_required

amenities_bp = Blueprint('amenities', __name__)

# Ajouter une commodité
@amenities_bp.route('/api/v1/admin/amenities', methods=['POST'])
@admin_required
def create_amenity():
    data = request.get_json()
    amenity = Amenity(name=data['name'])
    db.session.add(amenity)
    db.session.commit()
    return jsonify(amenity.to_dict()), 201

# Modifier une commodité existante
@amenities_bp.route('/api/v1/admin/amenities/<int:amenity_id>', methods=['PUT'])
@admin_required
def update_amenity(amenity_id):
    amenity = Amenity.query.get(amenity_id)
    if not amenity:
        return jsonify({"error": "Amenity not found"}), 404

    data = request.get_json()
    amenity.name = data.get('name', amenity.name)
    db.session.commit()
    return jsonify(amenity.to_dict()), 200
