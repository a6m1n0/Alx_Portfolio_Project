from datetime import datetime
from .. import db

class ElectionStatus:
    """Class containing constants for different election statuses in the secure online voting system."""
    PENDING = 'pending'
    OPEN = 'open'
    CLOSED = 'closed'

class Election(db.Model):
    """Class representing an election in the secure online voting system.

    Attributes:
        id (int): The unique identifier of the election.
        title (str): The title of the election.
        description (str): The description of the election.
        status (ElectionStatus): The status of the election.
        start_time (datetime): The timestamp of when the election will start.
        end_time (datetime): The timestamp of when the election will end.
        created_at (datetime): The timestamp of when the election was created.
        updated_at (datetime): The timestamp of when the election was
            last updated.
    """
    __tablename__ = 'elections'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.Enum(ElectionStatus.PENDING, ElectionStatus.OPEN, ElectionStatus.CLOSED), nullable=False, default=ElectionStatus.PENDING)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def __repr__(self):
        return f'<Election {self.title}>'
