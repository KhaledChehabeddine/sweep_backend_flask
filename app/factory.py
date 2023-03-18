from bson import json_util, ObjectId
from datetime import datetime
from flask import Flask
from flask.json import JSONEncoder
from flask_cors import CORS
from app.routes.blueprints import sweep_api_v1
import os


class MongoJsonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        if isinstance(obj, ObjectId):
            return str(obj)
        return json_util.default(obj, json_util.CANONICAL_JSON_OPTIONS)


def create_app():
    app = Flask(__name__)

    CORS(app)
    app.json_encoder = MongoJsonEncoder
    app.register_blueprint(sweep_api_v1)

    @app.route(rule='/', defaults={'path': ''})
    @app.route('/<path:path>')
    def home(path):
        return "Hello World!"

    return app
