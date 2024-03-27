from flask import Blueprint, jsonify
from task_api.models.database import db_session
from task_api.models.task import Task
from sqlalchemy.exc import SQLAlchemyError

# Create a Blueprint called 'tasks' to organize routes related to tasks
tasks_bp = Blueprint('tasks', __name__)


# Route to display all tasks
@tasks_bp.route('/tasks', methods=['GET'])
def show_tasks():
    try:
        # Retrieve all tasks from the database
        tasks = Task.query.all()
        task_list = Task.to_dict(tasks)
        return jsonify({'tasks': task_list})

    except SQLAlchemyError as e:
        return jsonify({'error': f'Error retrieving categories: {e}'}), 500


# Route to display details of a specific task
@tasks_bp.route('/task/<int:task_id>', methods=['GET'])
def show_task(task_id):
    try:
        task = Task.query.filter_by(task_id=task_id).first()
        task_dict = Task.to_dict(task)
        if not task:
            return jsonify({'error': 'No such task exists.'}), 404
        else:
            return jsonify(task_dict)

    except SQLAlchemyError as e:
        return jsonify({'error': f'Error retrieving task: {e}'}), 500
