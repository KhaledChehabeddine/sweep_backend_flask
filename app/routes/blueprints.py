"""Summary: Project Blueprints

Organize all root blueprints to easily allow child blueprints to be added to them
"""
from flask import Blueprint
from app.controllers.account.account_category_controller import account_category_api_v1
from app.controllers.user.company_controller import company_api_v1
from app.controllers.user.worker_controller import worker_api_v1

raw_sweep_api_v1 = Blueprint('sweep_api_v1', __name__, url_prefix='/api/v1/sweep')

raw_sweep_api_v1.register_blueprint(account_category_api_v1)
raw_sweep_api_v1.register_blueprint(company_api_v1)
raw_sweep_api_v1.register_blueprint(worker_api_v1)

sweep_api_v1 = raw_sweep_api_v1
