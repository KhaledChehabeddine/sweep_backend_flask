from flask import Blueprint


sweep_api_v1 = Blueprint(name='sweep_api_v1', import_name='sweep_api_v1', url_prefix='/api/v1/sweep')
user_api_v1 = Blueprint(name='user_api_v1', import_name='user_api_v1', url_prefix='/user')

sweep_api_v1.register_blueprint(user_api_v1)
