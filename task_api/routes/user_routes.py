from flask import Blueprint, jsonify, request
from task_api.models.user import User
from task_api.models.database import db_session
from sqlalchemy.exc import SQLAlchemyError
from task_api.models.extensions import bcrypt

# Create a Blueprint called 'tasks' to organize routes related to tasks
users_bp = Blueprint('users', __name__)


# Route for Login with username and password
@users_bp.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.json

        if 'username' in data:
            username = data.get('username')
            user = User.query.filter_by(
                username=username).first()

        elif 'email' in data:
            email = data.get('email')
            user = User.query.filter_by(
                email=email).first()

        password = data.get('password')

        if user and bcrypt.check_password_hash(user.password, password):
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

        hashed_password = bcrypt.generate_password_hash(
            password).decode('utf-8')

        check_email = email is not str
        check_password = password is not str
        check_username = username is not str

        # check datatype
        if not check_email or not check_password or not check_username:
            return jsonify({'message': 'Missing required field(s)'}), 400

        # chek if user and email exist
        exist_email = User.chek_email(email)
        exist_username = User.chek_username(hashed_password)

        if exist_username:
            return jsonify({'message': 'username already exist'}), 400
        if exist_email:
            return jsonify({'message': 'email already exist'}), 400

            # TODO ecription logic

        new_user = User(username=username,
                        password=hashed_password, email=email)

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
        user = User.query.get(user_id).first()
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
