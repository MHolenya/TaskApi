from flask import Blueprint, jsonify, request
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


@tasks_bp.route('/task', methods=['POST'])
def post_task():
    try:
        # Get the request body
        request_body = request.json
        user_id = request_body.get('user_id')
        title = request_body.get('title')
        description = request_body.get('description')
        status = request_body.get('status')
        category_id = request_body.get('category_id')
        due_date = request_body.get('due_date')

        # Check that required fields are present
        checks = {
            'user_id': not isinstance(user_id, int),
            'category_id': not isinstance(category_id, int),
            'title': not isinstance(title, str),
            'description': not isinstance(description, str),
            'status': not isinstance(status, str),
            'due_date': not isinstance(due_date, str)
        }
        print(description)
        print(checks)
        any_checks_failed = any(checks.values())
        if any_checks_failed:
            msg = 'At least one type check failed for the provided data.'
            return jsonify({'message': msg}), 400

        # Add new task to the database
        new_task = Task(
            user_id=user_id,
            title=title,
            description=description,
            status=status,
            category_id=category_id,
            due_date=due_date
        )

        db_session.add(new_task)
        db_session.commit()
        # Return successful creation message with category
        return jsonify({'message': 'Task added succesfully'}), 201

    except SQLAlchemyError as e:
        db_session.rollback()
        return jsonify({'error': str(e)}), 500


# Route to delete a task
@tasks_bp.route('/task/<int:task_id>', methods=['DELETE'])
def delete_category(task_id):
    try:
        task = Task.query.get(task_id)

        if task:

            db_session.delete(task)
            db_session.commit()

            return jsonify({'message': 'Task deleted successfully'})

        else:
            return jsonify({'message': 'Task not found'}), 404

    except SQLAlchemyError as e:
        # Rollback in case of any database error
        db_session.rollback()
        return jsonify({'error': str(e)}), 500
