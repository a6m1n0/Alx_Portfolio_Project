from flask import Blueprint, request, jsonify
from app.services.vote_service import VoteService
from flask_jwt_extended import jwt_required, get_jwt_identity

vote_bp = Blueprint('vote', __name__)

@vote_bp.route('/vote', methods=['POST'])
@jwt_required()
def cast_vote():
    data = request.get_json()
    candidate_id = data.get('candidate_id')
    election_id = data.get('election_id')

    user_id = get_jwt_identity()
    result = VoteService.cast_vote(user_id, candidate_id, election_id)
    if result['status'] == 'success':
        return jsonify(result), 201
    return jsonify(result), 400

@vote_bp.route('/votes', methods=['GET'])
@jwt_required()
def get_votes():
    election_id = request.args.get('election_id')
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    result = VoteService.get_votes(election_id, page, per_page)
    return jsonify(result), 200
