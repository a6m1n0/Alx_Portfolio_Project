from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from flask import jsonify
from ..models.user import User

def role_required(required_roles):
    """
    Role-based access control decorator.

    Args:
        required_roles (list): List of roles allowed to access the route.

    Returns:
        Function: Decorated function that enforces role-based access.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            current_user = get_jwt_identity()
            user = User.query.get(current_user)

            if user is None:
                return jsonify({"error": "User not found"}), 404

            if user.role not in required_roles:
                return jsonify({"error": "Access denied"}), 403

            return func(*args, **kwargs)
        return wrapper
    return decorator

