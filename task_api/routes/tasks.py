from flask import Blueprint, jsonify

# Create a Blueprint called 'tasks' to organize routes related to tasks
tasks_bp = Blueprint('tasks', __name__)

# Route to display all tasks


@tasks_bp.route('/tasks')
def show_tasks():
    # For now, we'll just return a dummy list of tasks
    tasks = [
        {'id': 1, 'title': 'Go grocery shopping',
            'description': 'Buy groceries for the week'},
        {'id': 2, 'title': 'Finish report',
            'description': 'Prepare report for Monday meeting'},
        {'id': 3, 'title': 'Go to the gym',
         'description': 'Exercise for an hour'}
    ]
    return jsonify(tasks)

# Route to display details of a specific task


@tasks_bp.route('/task/<int:task_id>')
def show_task(task_id):
    # For now, we'll just return a dummy task
    task = {'id': task_id, 'title': 'Go grocery shopping',
            'description': 'Buy groceries for the week'}
    return jsonify(task)
