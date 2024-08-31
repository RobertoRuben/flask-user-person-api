from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from src.services.person_service import PersonaService

person_blueprint = Blueprint('person_blueprint', __name__)

@person_blueprint.route('/persons', methods=['POST'])
def create_persona():
    try:
        data = request.get_json()
        new_persona = PersonaService.create_persona(data)
        return jsonify(new_persona), 201
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@person_blueprint.route('/persons', methods=['GET'])
def get_personas():
    try:
        personas = PersonaService.get_all_personas()
        return jsonify(personas), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@person_blueprint.route('/persons/<int:id>', methods=['GET'])
def get_persona(id):
    try:
        persona = PersonaService.get_persona_by_id(id)
        if persona:
            return jsonify(persona), 200
        return jsonify({"message": "Persona not found"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@person_blueprint.route('/persons/<int:id>', methods=['PUT'])
def update_persona(id):
    try:
        data = request.get_json()
        updated_persona = PersonaService.update_persona(id, data)
        if updated_persona:
            return jsonify(updated_persona), 200
        return jsonify({"message": "Persona not found"}), 404
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@person_blueprint.route('/persons/<int:id>', methods=['DELETE'])
def delete_persona(id):
    try:
        deleted_persona = PersonaService.delete_persona(id)
        if deleted_persona:
            return jsonify(deleted_persona), 200
        return jsonify({"message": "Persona not found"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500
