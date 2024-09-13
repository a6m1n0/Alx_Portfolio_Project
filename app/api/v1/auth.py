from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    result = AuthService.register_user(username, email, password)

    if result['status'] == 'success':
        return jsonify(result), 201
    return jsonify(result), 400

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    result = AuthService.login_user(email, password)

    if result['status'] == 'success':
        return jsonify(result), 200
    return jsonify(result), 400

@auth_bp.route('/logout', methods=['POST'])
def logout():
    data = request.get_json()
    email = data.get('email')

    result = AuthService.logout_user(email)

    if result['status'] == 'success':
        return jsonify(result), 200
    return jsonify(result), 400

@auth_bp.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    result = AuthService.get_paginated_users(page, per_page)
    return jsonify(result), 200

@auth_bp.route('/users/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    result = AuthService.get_user(user_id)

    if result['status'] == 'success':
        return jsonify(result), 200
    return jsonify(result), 400

@auth_bp.route('/users/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')

    result = AuthService.update_user(user_id, username, email)

    if result['status'] == 'success':
        return jsonify(result), 200
    return jsonify(result), 400

@auth_bp.route('/users/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    result = AuthService.delete_user(user_id)

    if result['status'] == 'success':
        return jsonify(result), 200
    return jsonify(result), 400

@auth_bp.route('/users/<int:user_id>/change-password', methods=['PUT'])
@jwt_required()
def change_password(user_id):
    data = request.get_json()
    old_password = data.get('old_password')
    new_password = data.get('new_password')

    if not old_password or not new_password:
        return jsonify({
            'status': 'error',
            'message': 'Old and new password are required'
        }), 400

    result = AuthService.change_password(user_id, old_password, new_password)

    if result['status'] == 'success':
        return jsonify(result), 200
    return jsonify(result), 400
