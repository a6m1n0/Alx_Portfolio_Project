from flask import Blueprint, request, jsonify
from app.services.election_service import ElectionService
from flask_jwt_extended import jwt_required
from ...models.user import UserRole
from ...utils.meddileware import role_required

election_bp = Blueprint('election', __name__)


@election_bp.route('/elections', methods=['POST'])
@jwt_required()
@role_required(UserRole.ADMIN)
def create_election():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    start_time = data.get('start_time')
    end_time = data.get('end_time')

    result = ElectionService.create_election(title, description, start_time, end_time)
    if result['status'] == 'success':
        return jsonify(result), 201
    return jsonify(result), 400

@election_bp.route('/elections', methods=['GET'])
@jwt_required()
def get_all_elections():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    result = ElectionService.get_all_elections(page=page, per_page=per_page)
    return jsonify(result), 200


@election_bp.route('/elections/<int:election_id>', methods=['GET'])
@jwt_required()
def get_election(election_id):
    result = ElectionService.get_election(election_id)
    if result['status'] == 'success':
        return jsonify(result), 200
    return jsonify(result), 404


@election_bp.route('/elections/<int:election_id>', methods=['PUT'])
@jwt_required()
@role_required(UserRole.ADMIN)
def update_election(election_id):
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    status = data.get('status')
    start_time = data.get('start_time')
    end_time = data.get('end_time')

    result = ElectionService.update_election(election_id, title, description, status, start_time, end_time)
    if result['status'] == 'success':
        return jsonify(result), 200
    return jsonify(result), 400


@election_bp.route('/elections/<int:election_id>', methods=['DELETE'])
@jwt_required()
@role_required(UserRole.ADMIN)
def delete_election(election_id):
    result = ElectionService.delete_election(election_id)
    if result['status'] == 'success':
        return jsonify(result), 200
    return jsonify(result), 404
