from flask import Blueprint, request, jsonify
from app.services.candidate_service import CandidateService
from flask_jwt_extended import jwt_required
from app.models.election import Election
from app.models.user import UserRole
from ...utils.meddileware import role_required

candidate_bp = Blueprint('candidate', __name__)

@candidate_bp.route('/candidates', methods=['POST'])
@jwt_required()
@role_required(UserRole.ADMIN)
def create_candidate():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    election_id = data.get('election_id')

    if election_id is None:
        return jsonify({"status": "error", "message": "Election ID is required"}), 400

    election = Election.query.get(election_id)
    if not election:
        return jsonify({"status": "error", "message": "Election not found"}), 404

    result = CandidateService.create_candidate(name, description, election_id)
    if result['status'] == 'success':
        return jsonify(result), 201
    return jsonify(result), 400

@candidate_bp.route('/candidates', methods=['GET'])
@jwt_required()
def get_candidates():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    result = CandidateService.get_candidates(page, per_page)
    return jsonify(result), 200

@candidate_bp.route('/candidates/<int:election_id>', methods=['GET'])
@jwt_required()
def get_candidates_by_election(election_id):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    result = CandidateService.get_candidates_by_election(election_id, page, per_page)
    return jsonify(result), 200

@candidate_bp.route('/candidates/<int:id>', methods=['PUT'])
@jwt_required()
@role_required(UserRole.ADMIN)
def update_candidate(id):
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    result = CandidateService.update_candidate(id, name, description)
    if result['status'] == 'success':
        return jsonify(result), 200
    return jsonify(result), 400

@candidate_bp.route('/candidates/<int:id>', methods=['DELETE'])
@jwt_required()
@role_required(UserRole.ADMIN)
def delete_candidate(id):
    result = CandidateService.delete_candidate(id)
    if result['status'] == 'success':
        return jsonify(result), 200
    return jsonify(result), 400
