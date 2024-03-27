from flask import Blueprint, jsonify, request
from task_api.models.user import User
from task_api.models.database import db_sesion
from sqlalchemy.exc import SQLAlchemyError

# Create a Blueprint called 'tasks' to organize routes related to tasks
users_bp = Blueprint('users', __name__)


@users_bp.route('/users', methods=['GET'])
def get_user():
    users = User.query.all()
    print(users)
    return jsonify(users)


@users_bp.route('/register_user', methods=['POST'])
def post_user():
    try:
        request_body = request.json
        username = request_body.get('username')
        email = request_body.get('email')
        password = request_body.get('password')
        new_user = User(username=username, password=password, email=email)
        print(new_user)
        db_sesion.add(new_user)
        db_sesion.commit()

        return jsonify({'message': 'User registered succesfully'}), 201

    except SQLAlchemyError as e:
        db_sesion.rollback()
        return jsonify({'error': str(e)}), 500
