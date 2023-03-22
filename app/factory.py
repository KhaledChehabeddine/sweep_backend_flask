from app.controllers.user_controller import user_api_v1
from app.routes.blueprints import sweep_api_v1
from flask import Flask

application = None


def create_application():
    global application
    if application is None:
        application = Flask(__name__)
        application.register_blueprint(sweep_api_v1)
        application.register_blueprint(user_api_v1)
    return application
