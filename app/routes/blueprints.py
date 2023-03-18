from flask import Blueprint

sweep_api_v1 = Blueprint('sweep_api_v1', __name__, url_prefix='/api/v1/sweep')
user_api_v1 = Blueprint('user_api_v1', __name__, url_prefix='/user')

sweep_api_v1.register_blueprint(user_api_v1)
