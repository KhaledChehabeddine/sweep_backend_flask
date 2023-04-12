"""Summary: Home sub feature item Controller CRUD Operations

A controller that assigns a child blueprint to sweep_api_v1 with routes for functions to create, read, update, and
delete account categories items from the database
"""

import json
from bson import json_util
from flask import Blueprint, Response, jsonify, request
from pymongo.errors import OperationFailure
from app.database.database import get_database
from app.models.home.home_sub_feature_item import HomeSubFeatureItem
from app.routes.blueprints import sweep_api_v1

home_sub_feature_item_api_v1 = Blueprint('home_sub_feature_item_api_v1', __name__,
                                         url_prefix='/home_sub_feature_item')
home_sub_feature_item_collection = get_database()['home_sub_feature_items']


@home_sub_feature_item_api_v1.route('/create', methods=['POST'])
def create_account_item_category() -> Response:
    """
    :return: Response object with a message describing if the account category was created and the status code
    """
    home_sub_feature_item_document = request.json
    home_sub_feature_item = HomeSubFeatureItem(home_sub_feature_item_document=home_sub_feature_item_document)
    try:
        home_sub_feature_item_collection.insert_one(home_sub_feature_item.__dict__)
    except OperationFailure:
        return jsonify({
            'message': 'home sub feature item not added to the database.',
            'status': 500
        })
    return jsonify({
        'message': 'home sub feature item added to the database.',
        'status': 200
    })


@home_sub_feature_item_api_v1.route('/read', methods=['GET'])
def read_home_sub_feature_items() -> Response:
    """
    :return: Response object with a message describing if the home sub feature item was found and the status code
    (if yes: add home sub feature item) and the status code
    """
    home_sub_feature_items = []
    home_sub_feature_item_documents = home_sub_feature_item_collection.find()
    if home_sub_feature_item_documents:
        for home_sub_feature_item_document in home_sub_feature_item_documents:
            home_sub_feature_item_document = json \
                .loads(json_util.dumps(home_sub_feature_item_document), object_hook=json_util.object_hook)
            home_sub_feature_item = HomeSubFeatureItem(
                home_sub_feature_item_document=home_sub_feature_item_document)
            home_sub_feature_items.append(home_sub_feature_item.__dict__)
        return jsonify({
            'message': 'home sub feature items found in the database.',
            'status': 200,
            'home_sub_feature_item': home_sub_feature_items
        })
    return jsonify({
        'message': 'No home sub feature items found in the database.',
        'status': 404
    })


@home_sub_feature_item_api_v1.route('/update/<string:name>', methods=['PUT'])
def update_home_sub_feature_item_by_name(name: str) -> Response:
    """
    :param name: Home sub feature item's name
    :return: Response object with a message describing if the home sub feature item was found (if yes: update from
    home sub feature items) and the status code
    """
    home_sub_feature_item_document = request.json
    home_sub_feature_item = HomeSubFeatureItem(
        home_sub_feature_item_document=home_sub_feature_item_document)
    result = home_sub_feature_item_collection.update_one(
        {'name': name},
        {'$set': home_sub_feature_item.__dict__}
    )
    if result.modified_count == 1:
        return jsonify({
            'message': 'Account category updated in the database using the name.',
            'status': 200,
        })
    return jsonify({
        'message': 'Account category not found in the database using the name.',
        'status': 404
    })


@home_sub_feature_item_api_v1.route('/delete/<string:name>', methods=['DELETE'])
def delete_home_sub_feature_by_id(name: str) -> Response:
    """
    :param name: Home sub feature item name
    :return: Response object with a message describing if the home sub item was found (if yes: delete from the
    home sub feature items) and the status code
    """
    result = home_sub_feature_item_collection.delete_one({'name': name})
    if result.deleted_count == 1:
        return jsonify({
            'message': 'Home sub feature item deleted from the database using the name.',
            'status': 200
        })
    return jsonify({
        'message': 'Home sub feature item not found in the database using the name.',
        'status': 404
    })


sweep_api_v1.register_blueprint(home_sub_feature_item_api_v1)
