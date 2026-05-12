from flask import Blueprint, jsonify, request
from app.database import users_db

# Creamos el Blueprint para organizar estas rutas
user_bp = Blueprint('user_bp', __name__)

# GET /users - Listar todos
@user_bp.route('/users', methods=['GET'])
def get_users():
    return jsonify(users_db), 200

# GET /users/<id> - Obtener uno solo
@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users_db if u['id'] == user_id), None)
    if user:
        return jsonify(user), 200
    return jsonify({"message": "Usuario no encontrado"}), 404

# POST /users - Crear uno nuevo
@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = {
        "id": len(users_db) + 1,
        "username": data.get('username'),
        "email": data.get('email'),
        "password": data.get('password')
    }
    users_db.append(new_user)
    return jsonify(new_user), 201
