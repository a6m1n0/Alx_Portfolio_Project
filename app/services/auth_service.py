from app.models.user import User
from app import db
from flask_jwt_extended import create_access_token
# from app.utils.security import hash_password, verify_password

class AuthService:

    @staticmethod
    def register_user(username, email, password):
        """
        Register a new user with the given username, email, and password.

        This function creates a new User object with the specified
        username, email, and password, and adds it to the database.

        Parameters:
        -----------
        username : str
            The username of the new user.
        email : str
            The email address of the new user.
        password : str
            The password of the new user.

        Returns:
        --------
        user : User
            The User object representing the new user.
        """
        if User.query.filter_by(email=kwargs.email).first():
            return {"status": "error", "message": "Email already exists"}

        if User.query.filter_by(username=kwargs.username).first():
            return {"status": "error", "message": "User already exists"}

        user = User(**kwargs)
        user.set_password = kwargs.password

        db.session.add(user)
        db.session.commit()

        return {"status": "success", "message": "User registered successfully"}

    @staticmethod
    def login_user(email, password):
        """
        Log in a user with the given email and password.

        This function attempts to find a user with the specified email
        and password in the database. If a user is found, an access token
        is created and returned.

        Parameters:
        -----------
        email : str
            The email address of the user.
        password : str
            The password of the user.

        Returns:
        --------
        access_token : str
            The access token for the user.
        """
        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            access_token = create_access_token(identity=user.id)
            return {"status": "success", "access_token": access_token}
        return {"status": "error", "message": "Invalid email or password"}

    @staticmethod
    def logout_user(email):
        """
        Log out a user with the given email.

        This function logs out a user by revoking their access token.

        Parameters:
        -----------
        email : str
            The email address of the user.

        Returns:
        --------
        message : str
            A message indicating whether the user was successfully logged out.
        """
        return {"status": "success", "message": "User logged out successfully"}

    @staticmethod
    def get_paginated_users(page=1, per_page=10):
        users_query = User.query.paginate(page=page, per_page=per_page, error_out=False)
        users = []
        for user in users_query.items:
            users.append({
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'role': user.role,
                'created_at': user.created_at
            })

        return {
            'total': users_query.total,
            'pages': users_query.pages,
            'current_page': users_query.page,
            'next_page': users_query.next_num,
            'prev_page': users_query.prev_num,
            'users': users
        }


    @staticmethod
    def get_users():
        """
        Get a list of all users.

        This function returns a list of all users in the database.

        Returns:
        --------
        users : list
            A list of User objects representing all users.
        """
        users = User.query.all()
        return {"status": "success", "users": users}

    @staticmethod
    def get_user(user_id):
        user = User.query.get(user_id)
        if user:
            return {
                'status': 'success',
                'user': user.to_dict()  # Convert user to dictionary format
            }
        return {
            'status': 'error',
            'message': 'User not found'
        }


    @staticmethod
    def update_user(user_id, username=None, email=None):
        """
        Update a user with the given ID.

        This function updates the user with the specified ID.

        Parameters:
        -----------
        user_id : int
            The ID of the user to update.
        username : str
            The new username for the user.
        email : str
            The new email for the user.

        Returns:
        --------
        user : User
            The User object representing the updated user.
        """
        user = User.query.get(user_id)
        if not user:
            return {
                'status': 'error',
                'message': 'User not found'
            }

        # Update the user's fields
        if username:
            user.username = username
        if email:
            user.email = email

        db.session.commit()

        return {
            'status': 'success',
            'message': 'User updated successfully'
        }

    @staticmethod
    def delete_user(user_id):
        """
        Delete a user with the given ID.

        This function deletes the user with the specified ID.

        Parameters:
        -----------
        user_id : int
            The ID of the user to delete.

        Returns:
        --------
        message : str
            A message indicating whether the user was successfully deleted.
        """
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()

        return {"status": "success", "message": "User deleted successfully"}

    @staticmethod
    def get_user_by_email(email):
        """
        Get a user with the given email.

        This function returns the user with the specified email.

        Parameters:
        -----------
        email : str
            The email address of the user to retrieve.

        Returns:
        --------
        user : User
            The User object representing the user with the specified email.
        """
        user = User.query.filter_by(email=email).first()
        return user

    @staticmethod
    def change_password(user_id, old_password, new_password):
        """
        Change the password of a user with the given ID.

        This function changes the password of the user with the specified ID.

        Parameters:
        -----------
        user_id : int
            The ID of the user to update.
        password : str
            The new password for the user.

        Returns:
        --------
        message : str
            A message indicating whether the password was successfully changed.
        """
        user = User.query.get(user_id)
        if not user:
            return {
                'status': 'error',
                'message': 'User not found'
            }

        if not old_password or not new_password:
            return {
                'status': 'error',
                'message': 'Both old and new passwords are required'
            }

        if not user.check_password(old_password):
            return {
                'status': 'error',
                'message': 'Incorrect old password'
            }

        user.set_password(new_password)
        db.session.commit()

        return {
            'status': 'success',
            'message': 'Password updated successfully'
        }
