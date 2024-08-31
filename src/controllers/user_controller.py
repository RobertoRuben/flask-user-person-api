from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from src.services.user_service import UserService

user_blueprint = Blueprint('user_blueprint', __name__)

@user_blueprint.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        new_user = UserService.create_user(data)
        return jsonify(new_user), 201
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@user_blueprint.route('/users', methods=['GET'])
def get_users():
    try:
        users = UserService.get_all_users()
        return jsonify(users), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@user_blueprint.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    try:
        user = UserService.get_user_by_id(id)
        if user:
            return jsonify(user), 200
        return jsonify({"message": "Usuario no encontrado"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@user_blueprint.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        data = request.get_json()
        updated_user = UserService.update_user(id, data)
        if updated_user:
            return jsonify(updated_user), 200
        return jsonify({"message": "Usuario no encontrado"}), 404
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@user_blueprint.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        deleted_user = UserService.delete_user(id)
        if deleted_user:
            return jsonify(deleted_user), 200
        return jsonify({"message": "Usuario no encontrado"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500
