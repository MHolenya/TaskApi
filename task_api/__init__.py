from flask import Flask
from task_api.routes.tasks import tasks_bp


def create_app():
    # Create the Flask application instance
    app = Flask(__name__)
    app.register_blueprint(tasks_bp)
    return app
