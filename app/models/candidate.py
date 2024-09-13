from datetime import datetime
from .. import db

class Candidates(db.Model):
    """Class representing a candidate in the secure online voting system.

    Attributes:
        id (int): The unique identifier of the candidate.
        name (str): The name of the candidate.
        description (str): The description of the candidate.
        election_id (int): The unique identifier of the election that the
            candidate is running in.
        created_at (datetime): The timestamp of when the candidate was created.
        updated_at (datetime): The timestamp of when the candidate was
            last updated.
    """
    __tablename__ = 'candidates'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    election_id = db.Column(db.Integer, db.ForeignKey('elections.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'election_id': self.election_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def __repr__(self):
        return f'<Candidate {self.name}>'
