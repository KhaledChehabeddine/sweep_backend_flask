"""Summary: Home Sub Feature Controller CRUD Operations

A controller that assigns a child blueprint to sweep_api_v1 with routes for functions to create, read, update, and
delete home sub features from the database
"""

import json
from bson import json_util
from flask import Blueprint, Response, jsonify, request
from pymongo.errors import OperationFailure
from app.database.database import get_database
from app.models.home.home_sub_feature import HomeSubFeature
from app.routes.blueprints import sweep_api_v1

home_sub_feature_api_v1 = Blueprint('home_sub_feature_api_v1', __name__, url_prefix='/home_sub_feature')
home_sub_feature_collection = get_database()['home_sub_features']


@home_sub_feature_api_v1.route('/create', methods=['POST'])
def create_home_sub_feature() -> Response:
    """
    :return: Response object with a message describing if the home sub feature was created and the status code
    """
    home_sub_feature_document = request.json
    home_sub_feature = HomeSubFeature(home_sub_feature_document=home_sub_feature_document)
    try:
        home_sub_feature_collection.insert_one(home_sub_feature.create_dict())
    except OperationFailure:
        return jsonify({
            'message': 'Home sub feature not added to the database.',
            'status': 500
        })
    return jsonify({
        'message': 'Home sub feature added to the database.',
        'status': 200
    })


@home_sub_feature_api_v1.route('/read', methods=['GET'])
def read_home_sub_features() -> Response:
    """
    :return: Response object with a message describing if all the home sub features were found (if yes: add home
    sub features) and the status code
    """
    home_sub_features = []
    home_sub_feature_documents = home_sub_feature_collection.find()
    if home_sub_feature_documents:
        for home_sub_feature_document in home_sub_feature_documents:
            home_sub_feature_document = json \
                .loads(json_util.dumps(home_sub_feature_document), object_hook=json_util.object_hook)
            home_sub_feature = HomeSubFeature(home_sub_feature_document=home_sub_feature_document)
            home_sub_features.append(home_sub_feature.__dict__)
        return jsonify({
            'data': home_sub_features,
            'message': 'Home sub features found in the database.',
            'status': 200
        })
    return jsonify({
        'message': 'No home sub features found in the database.',
        'status': 404
    })


@home_sub_feature_api_v1.route('/read/name/<string:name>', methods=['GET'])
def read_home_sub_feature_by_name(name: str) -> Response:
    """
    :param name: Home sub feature's name
    :return: Response object with a message describing if the home sub feature was found (if yes: add home sub feature)
    and the status code
    """
    home_sub_feature_document = json.loads(json_util.dumps(home_sub_feature_collection.find_one({'name': name})),
                                           object_hook=json_util.object_hook)
    if home_sub_feature_document:
        home_sub_feature = HomeSubFeature(home_sub_feature_document=home_sub_feature_document)
        return jsonify({
            'data': home_sub_feature.__dict__,
            'message': 'Home sub feature found in the database using the name.',
            'status': 200
        })
    return jsonify({
        'message': 'Home sub feature not found in the database using the name.',
        'status': 404
    })


@home_sub_feature_api_v1.route('/update/name/<string:name>', methods=['PUT'])
def update_home_sub_feature_by_name(name: str) -> Response:
    """
    :param name: Home sub feature's name
    :return: Response object with a message describing if the home sub feature was found (if yes: update home
    sub feature) and the status code
    """
    home_sub_feature_document = request.json
    home_sub_feature = HomeSubFeature(home_sub_feature_document=home_sub_feature_document)
    result = home_sub_feature_collection.update_one(
        {'name': name},
        {'$set': home_sub_feature.__dict__}
    )
    if result.modified_count == 1:
        return jsonify({
            'message': 'Home sub feature updated in the database using the name.',
            'status': 200
        })
    return jsonify({
        'message': 'Home sub feature not found in the database using the name.',
        'status': 404
    })


@home_sub_feature_api_v1.route('/delete/name/<string:name>', methods=['DELETE'])
def delete_home_sub_feature_by_name(name: str) -> Response:
    """
    :param name: Home sub feature's name
    :return: Response object with a message describing if the home sub feature was found (if yes: delete home
    sub feature) and the status code
    """
    result = home_sub_feature_collection.delete_one({'name': name})
    if result.deleted_count == 1:
        return jsonify({
            'message': 'Home sub feature deleted from the database using the name.',
            'status': 200
        })
    return jsonify({
        'message': 'Home sub feature not found in the database using the name.',
        'status': 404
    })


sweep_api_v1.register_blueprint(home_sub_feature_api_v1)
