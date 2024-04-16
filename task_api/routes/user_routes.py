from flask import Blueprint, jsonify, request
from task_api.models.user import User
from task_api.models.database import db_session
from sqlalchemy.exc import SQLAlchemyError

# Create a Blueprint called 'tasks' to organize routes related to tasks
users_bp = Blueprint('users', __name__)


@users_bp.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.json

        # TODO Enription logic
        username = data.get('username')
        password = data.get('password')
        # Assuming you have a User model
        user = User.query.filter_by(
            username=username, password=password)

        if user:
            return jsonify({'message': 'Login successful'})
        else:
            return jsonify({'message': 'Invalid username or password'}), 401
    else:
        return jsonify({'message': 'Method not allowed'}), 405


# Route for creating new user
@users_bp.route('/signup', methods=['POST'])
def post_user():
    try:
        request_body = request.json
        # get the values  passed in the JSON body of the POST request
        username = request_body.get('username')
        email = request_body.get('email')
        password = request_body.get('password')
        print(type(password))
        check_email = email is not str
        check_password = password is not str
        check_username = username is not str
        print(check_email, check_password, check_username)
        # check datatype
        if not check_email or not check_password or not check_username:
            return jsonify({'message': 'Missing required field(s)'}), 400
        # chek if user exist
        # TODO ecription logic and serch if user exist
        new_user = User(username=username, password=password, email=email)

        # add new user
        db_session.add(new_user)
        db_session.commit()

        return jsonify({'message': 'User registered succesfully'}), 201

    except SQLAlchemyError as e:
        db_session.rollback()
        return jsonify({'error': str(e)}), 500


# Route to delete a user
@users_bp.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        user = User.query.get(user_id)
        # check if user exist
        if user:

            db_session.delete(user)
            db_session.commit()

            return jsonify({'message': 'User deleted successfully'})
        # if user don't exist
        else:
            return jsonify({'message': 'User not found'}), 404

    except SQLAlchemyError as e:
        # Rollback in case of any database error
        db_session.rollback()
        return jsonify({'error': str(e)}), 500


# Route to update a user
@users_bp.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):

    try:
        user = User.query.get(user_id)
        # check if user exist
        if user:
            data = request.get_json()

            # Update user attributes with values from the JSON data,
            # if the value is not provided
            # use the current value from the user object
            password = data.get('password', user.password)
            username = data.get('username', user.username)
            email = data.get('email', user.status)

            # Assign the updated values to the uuser object
            # TODO ecription logic
            user.password = password
            user.username = username
            user.email = email

            db_session.commit()
            return jsonify({'message': 'User updated successfully'})

        # if task don't exist
        else:
            return jsonify({'message': 'User not found'}), 404

    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500
