from flask import Blueprint
from app.controllers.user_controller import user_api_v1

sweep_api_v1 = Blueprint('sweep_api_v1', __name__, url_prefix='/api/v1/sweep')

sweep_api_v1.register_blueprint(user_api_v1)
