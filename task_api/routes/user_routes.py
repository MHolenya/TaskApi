from flask import Blueprint, jsonify, request
from task_api.models.user import User
from task_api.models.database import db_session
from sqlalchemy.exc import SQLAlchemyError

# Create a Blueprint called 'tasks' to organize routes related to tasks
users_bp = Blueprint('users', __name__)


# Route for get all users
@users_bp.route('/user<int:user_id>', methods=['GET'])
def get_user(user_id):

    try:
        user = User.query.filter_by(id=user_id).first()
        if user:
            return jsonify(user)
        else:
            return jsonify({'message': 'User not found'}), 404

    except SQLAlchemyError as e:
        return jsonify({'message': f'Errore retrieving user: {e}'}), 500


# Route for creating new user
@users_bp.route('/register_user', methods=['POST'])
def post_user():
    try:
        request_body = request.json
        # get the values  passed in the JSON body of the POST request
        username = request_body.get('username')
        email = request_body.get('email')
        password = request_body.get('password')

        check_email = email is not str
        check_password = password is not str
        check_username = username is not str

        # check datatype
        if any([check_email, check_password, check_username]):
            return jsonify({'message': 'Missing required field(s)'}), 400

        new_user = User(username=username, password=password, email=email)

        # add new user
        db_session.add(new_user)
        db_session.commit()

        return jsonify({'message': 'User registered succesfully'}), 201

    except SQLAlchemyError as e:
        db_session.rollback()
        return jsonify({'error': str(e)}), 500
