from datetime import datetime
from .. import db
import hashlib

class Votes(db.Model):
    """Class representing a vote in the secure online voting system.

    Attributes:
        id (int): The unique identifier of the vote.
        candidate_id (int): The unique identifier of the candidate that the
            vote was cast for.
        election_id (int): The unique identifier of the election that the
            vote was cast in.
        created_at (datetime): The timestamp of when the vote was created.
    """
    __tablename__ = 'votes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.id'), nullable=False)
    election_id = db.Column(db.Integer, db.ForeignKey('elections.id'), nullable=False)
    encrypted_vote = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


    def encrypt_vote(self, vote):
        vote_bytes = vote.encode('utf-8')
        hash_object = hashlib.sha256()
        hash_object.update(vote_bytes)
        encrypted_vote = hash_object.hexdigest()
        self.encrypted_vote = encrypted_vote


    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'candidate_id': self.candidate_id,
            'election_id': self.election_id,
            'created_at': self.created_at
        }

    def __repr__(self):
        return f'<Vote {self.id}>'
