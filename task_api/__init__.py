from flask import Flask
from flask_cors import CORS
from task_api.routes.task_routes import tasks_bp
from task_api.routes.user_routes import users_bp
from task_api.routes.category_routes import category_bp


def create_app():
    # Create the Flask application instance
    app = Flask(__name__)
    app.register_blueprint(tasks_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(category_bp)
    app.debug = True
    CORS(app)
    return app
