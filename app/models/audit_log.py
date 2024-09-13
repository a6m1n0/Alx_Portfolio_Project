from datetime import datetime
from .. import db

class AuditLogs(db.Model):
    """Class representing an audit log in the secure online voting system.

    Attributes:
        id (int): The unique identifier of the audit log.
        user_id (int): The unique identifier of the user that performed the
            action.
        action (str): The action that was performed.
        timestamp (datetime): The timestamp of when the action was performed.
    """
    __tablename__ = 'audit_logs'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    action = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'action': self.action,
            'timestamp': self.timestamp
        }

    def __repr__(self):
        return f'<AuditLog {self.id}>'