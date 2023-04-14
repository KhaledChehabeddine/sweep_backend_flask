"""Summary: Home Main Feature Controller CRUD Operations

A controller that assigns a child blueprint to sweep_api_v1 with routes for functions to create, read, update, and
delete home categories from the database
"""

import json
import pymongo
from bson import json_util
from flask import Blueprint, Response, jsonify, request
from pymongo.errors import OperationFailure
from app.database.database import get_database
from app.models.home.home_main_feature import HomeMainFeature
from app.routes.blueprints import sweep_api_v1

home_main_feature_api_v1 = Blueprint('home_main_feature_api_v1', __name__, url_prefix='/home_main_feature')
home_main_feature_collection = get_database()['home_categories']

home_main_feature_collection.create_index([('name', pymongo.ASCENDING)], unique=True)


@home_main_feature_api_v1.route('/create', methods=['POST'])
def create_home_main_feature() -> Response:
    """
    :return: Response object with a message describing if the home main feature was created and the status code
    """
    home_main_feature_document = request.json
    home_main_feature = HomeMainFeature(home_main_feature_document=home_main_feature_document)
    try:
        home_main_feature_collection.insert_one(home_main_feature.create_dict())
    except OperationFailure:
        return jsonify({
            'message': 'Home main feature not added to the database.',
            'status': 500
        })
    return jsonify({
        'message': 'Home main feature added to the database.',
        'status': 200
    })


@home_main_feature_api_v1.route('/read', methods=['GET'])
def read_home_categories() -> Response:
    """
    :return: Response object with a message describing if all the home categories were found (if yes: add home
    categories) and the status code
    """
    home_categories = []
    home_main_feature_documents = home_main_feature_collection.find()
    if home_main_feature_documents:
        for home_main_feature_document in home_main_feature_documents:
            home_main_feature_document = json \
                .loads(json_util.dumps(home_main_feature_document), object_hook=json_util.object_hook)
            home_main_feature = HomeMainFeature(home_main_feature_document=home_main_feature_document)
            home_categories.append(home_main_feature.__dict__)
        return jsonify({
            'data': home_categories,
            'message': 'Home categories found in the database.',
            'status': 200
        })
    return jsonify({
        'message': 'No home main feature found in the database.',
        'status': 404
    })


@home_main_feature_api_v1.route('/read/name/<string:name>', methods=['GET'])
def read_home_main_feature_by_name(name: str) -> Response:
    """
    :param name: Home main feature's name :return: Response object with a message describing if the home main feature
    was found (if yes: add home main feature) and the status code
    """
    home_main_feature_document = json.loads(json_util.dumps(home_main_feature_collection.find_one({'name': name})),
                                            object_hook=json_util.object_hook)
    if home_main_feature_document:
        home_main_feature = HomeMainFeature(home_main_feature_document=home_main_feature_document)
        return jsonify({
            'data': home_main_feature.__dict__,
            'message': 'Home main feature found in the database using the name.',
            'status': 200
        })
    return jsonify({
        'message': 'Home main feature not found in the database using the name.',
        'status': 404
    })


@home_main_feature_api_v1.route('/update/name/<string:name>', methods=['PUT'])
def update_home_main_feature_by_name(name: str) -> Response:
    """
    :param name: Home main feature's name
    :return: Response object with a message describing if the home main feature was found (if yes: update home
    main feature) and the status code
    """
    home_main_feature_document = request.json
    home_main_feature = HomeMainFeature(home_main_feature_document=home_main_feature_document)
    result = home_main_feature_collection.update_one(
        {'name': name},
        {'$set': home_main_feature.__dict__}
    )
    if result.modified_count == 1:
        return jsonify({
            'message': 'Home main feature updated in the database using the name.',
            'status': 200
        })
    return jsonify({
        'message': 'Home main feature not found in the database using the name.',
        'status': 404
    })


@home_main_feature_api_v1.route('/delete/name/<string:name>', methods=['DELETE'])
def delete_home_main_feature_by_name(name: str) -> Response:
    """
    :param name: Home main feature's name
    :return: Response object with a message describing if the home main feature was found (if yes: delete home
    main feature) and the status code
    """
    result = home_main_feature_collection.delete_one({'name': name})
    if result.deleted_count == 1:
        return jsonify({
            'message': 'Home main feature deleted from the database using the name.',
            'status': 200
        })
    return jsonify({
        'message': 'Home main feature not found in the database using the name.',
        'status': 404
    })


sweep_api_v1.register_blueprint(home_main_feature_api_v1)
