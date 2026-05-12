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

# PUT /users/<id> - Actualizar datos
@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = next((u for u in users_db if u['id'] == user_id), None)
    
    if not user:
        return jsonify({"message": "Usuario no encontrado"}), 404

    # Actualizamos solo los campos que vengan en el JSON
    user['username'] = data.get('username', user['username'])
    user['email'] = data.get('email', user['email'])
    user['password'] = data.get('password', user['password'])
    
    return jsonify(user), 200

# DELETE /users/<id> - Eliminar del sistema
@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users_db
    user = next((u for u in users_db if u['id'] == user_id), None)
    
    if not user:
        return jsonify({"message": "Usuario no encontrado"}), 404

    users_db = [u for u in users_db if u['id'] != user_id]
    return jsonify({"message": "Usuario eliminado correctamente"}), 200