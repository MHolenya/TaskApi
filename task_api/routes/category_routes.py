from flask import Blueprint, jsonify
from task_api.models.database import db_session
from sqlalchemy.exc import SQLAlchemyError

# Create a Blueprint called 'tasks' to organize routes related to tasks
category_bp = Blueprint('category', __name__)


# Route to display all tasks
@category_bp.route('/categorys', methods=['GET'])
def get_all_categorys():
    try:
        categorys = Category.query.get_all()

    except SQLAlchemyError as e:
        return jsonify({'message': f'Errore retrieving user: {e}'}), 500
