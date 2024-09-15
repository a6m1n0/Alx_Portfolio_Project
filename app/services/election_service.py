from app.models.election import Election
from app.models.election import ElectionStatus
from app import db
from datetime import datetime

class ElectionService:

    @staticmethod
    def create_election(title, description, start_time, end_time):
        try:
            election = Election.query.filter_by(title=title).first()
            if election:
                return {"status": "error", "message": "Election already exists"}
                
            election = Election(
                title=title,
                description=description,
                status=ElectionStatus.PENDING,
                start_time=datetime.fromisoformat(start_time),
                end_time=datetime.fromisoformat(end_time)
            )
            db.session.add(election)
            db.session.commit()
            return {"status": "success", "message": "Election created successfully"}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    @staticmethod
    def get_all_elections(page=1, per_page=10):
        """Fetch paginated elections."""
        elections = Election.query.paginate(page=page, per_page=per_page, error_out=False)
        return {
            "status": "success",
            "total": elections.total,
            "pages": elections.pages,
            "current_page": elections.page,
            "next_num": elections.next_num,
            "prev_num": elections.prev_num,
            "elections": [election.to_dict() for election in elections.items]
        }

    @staticmethod
    def get_election(election_id):
        election = Election.query.get(election_id)
        if not election:
            return {"status": "error", "message": "Election not found"}
        return {"status": "success", "election": election.to_dict()}

    @staticmethod
    def update_election(election_id, title=None, description=None, status=None, start_time=None, end_time=None):
        election = Election.query.get(election_id)
        if not election:
            return {"status": "error", "message": "Election not found"}

        try:
            if title:
                election.title = title
            if description:
                election.description = description
            if status:
                election.status = status
            if start_time:
                election.start_time = datetime.fromisoformat(start_time)
            if end_time:
                election.end_time = datetime.fromisoformat(end_time)

            db.session.commit()
            return {"status": "success", "message": "Election updated successfully"}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    @staticmethod
    def delete_election(election_id):
        election = Election.query.get(election_id)
        if not election:
            return {"status": "error", "message": "Election not found"}
        try:
            db.session.delete(election)
            db.session.commit()
            return {"status": "success", "message": "Election deleted successfully"}
        except Exception as e:
            return {"status": "error", "message": str(e)}
