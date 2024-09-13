from app.models.vote import Votes
from app import db
from sqlalchemy.exc import IntegrityError

class VoteService:

    @staticmethod
    def cast_vote(user_id, candidate_id, election_id):
        try:
            # Ensure the user hasn't voted in this election
            existing_vote = Votes.query.filter_by(user_id=user_id, election_id=election_id).first()
            if existing_vote:
                return {"status": "error", "message": "User has already voted in this election"}

            # Cast a vote
            new_vote = Votes(user_id=user_id, candidate_id=candidate_id, election_id=election_id)
            new_vote.encrypt_vote(f'{user_id}:{election_id}:{candidate_id}')  # Encrypt vote using method in model

            db.session.add(new_vote)
            db.session.commit()

            return {"status": "success", "message": "Vote cast successfully"}
        except IntegrityError:
            db.session.rollback()
            return {"status": "error", "message": "Invalid data provided"}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    @staticmethod
    def get_votes(election_id, page, per_page):
        try:
            votes_query = Votes.query.filter_by(election_id=election_id).paginate(page=page, per_page=per_page, error_out=False)

            votes = [vote.to_dict() for vote in votes_query.items]

            return {
                "status": "success",
                "votes": votes,
                "total": votes_query.total,
                "pages": votes_query.pages,
                "current_page": votes_query.page
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}
