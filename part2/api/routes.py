from flask import Blueprint, jsonify
from app.facade.hbnb_facade import HbnbFacade

api_blueprint = Blueprint('api', __name__)
facade = HbnbFacade()

@api_blueprint.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "OK"})
