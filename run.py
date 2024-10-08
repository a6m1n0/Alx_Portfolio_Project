from app import create_app, db, Migrate
from app.models.user import User
from app.models.election import Election
from app.models.candidate import Candidates
from app.models.audit_log import AuditLogs
from app.models.vote import Votes
import os

# Create the Flask application using the specified configuration
app = create_app(os.getenv('FLASK_CONFIG') or 'default')

# Initialize database migration support
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    """
    Provide a shell context that includes database models.

    This function returns a dictionary of objects that will be automatically
    available in the Flask shell, allowing easy access to database models
    and the database instance for interactive development.

    Returns:
    --------
    dict:
        A dictionary mapping names to objects, including the database
        instance and the models: User, UserRole, Assessment, Submission,
        Course, and Lesson.
    """
    return dict(db=db, User=User, Election=Election,
                Candidates=Candidates, AuditLogs=AuditLogs,
                Votes=Votes)  # Type: ignore

@app.cli.command()
def test():
    """
    Run the unit tests for the application.

    This function discovers and runs all unit tests located in the 'tests'
    directory, providing output with verbosity level 2 for detailed test
    results.

    Usage:
    ------
    flask test
    """
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
