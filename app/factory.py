"""Summary: Application Configurator

Creates an application instance that registers all the project's blueprints
"""

from flask import Flask
from app.controllers.user_controller import user_api_v1
from app.routes.blueprints import sweep_api_v1


def create_application() -> Flask:
    """
    :return: Flask application instance
    """
    application = Flask(__name__)
    application.register_blueprint(sweep_api_v1)
    application.register_blueprint(user_api_v1)
    return application
