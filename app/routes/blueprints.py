"""Summary: Project Blueprints

Organize all root blueprints to easily allow child blueprints to be added to them
"""

from flask import Blueprint

sweep_api_v1 = Blueprint('sweep_api_v1', __name__, url_prefix='/api/v1/sweep')
