from app.models.candidate import Candidates
from app import db
from sqlalchemy import exc

class CandidateService:

    @staticmethod
    def create_candidate(name, description, election_id):
        try:
            new_candidate = Candidates(
                name=name,
                description=description,
                election_id=election_id
            )
            db.session.add(new_candidate)
            db.session.commit()
            return {"status": "success", "message": "Candidate created successfully"}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    @staticmethod
    def get_candidates(page=1, per_page=10):
        try:
            candidates_pagination = Candidates.query.paginate(page=page, per_page=per_page, error_out=False)

            candidates = [candidate.to_dict() for candidate in candidates_pagination.items]
            return {
                "status": "success",
                "candidates": candidates,
                "total": candidates_pagination.total,
                "page": candidates_pagination.page,
                "pages": candidates_pagination.pages,
                "has_next": candidates_pagination.has_next,
                "has_prev": candidates_pagination.has_prev
            }
        except exc.SQLAlchemyError as e:
            return {"status": "error", "message": str(e)}

    @staticmethod
    def get_candidates_by_election(election_id, page=1, per_page=10):
        try:
            candidates_pagination = Candidates.query.filter_by(election_id=election_id).paginate(page=page, per_page=per_page, error_out=False)

            candidates = [candidate.to_dict() for candidate in candidates_pagination.items]
            return {
                "status": "success",
                "candidates": candidates,
                "total": candidates_pagination.total,
                "page": candidates_pagination.page,
                "pages": candidates_pagination.pages,
                "has_next": candidates_pagination.has_next,
                "has_prev": candidates_pagination.has_prev
            }
        except exc.SQLAlchemyError as e:
            return {"status": "error", "message": str(e)}

    @staticmethod
    def update_candidate(id, name=None, description=None):
        try:
            candidate = Candidates.query.get(id)
            if not candidate:
                return {"status": "error", "message": "Candidate not found"}

            if name:
                candidate.name = name
            if description:
                candidate.description = description

            db.session.commit()
            return {"status": "success", "message": "Candidate updated successfully"}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    @staticmethod
    def delete_candidate(id):
        try:
            candidate = Candidates.query.get(id)
            if not candidate:
                return {"status": "error", "message": "Candidate not found"}

            db.session.delete(candidate)
            db.session.commit()
            return {"status": "success", "message": "Candidate deleted successfully"}
        except Exception as e:
            return {"status": "error", "message": str(e)}
