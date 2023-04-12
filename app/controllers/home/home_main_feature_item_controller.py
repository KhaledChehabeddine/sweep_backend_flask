"""Summary: Home main feature item Controller CRUD Operations

A controller that assigns a child blueprint to sweep_api_v1 with routes for functions to create, read, update, and
delete account categories items from the database
"""

import json
from bson import json_util
from flask import Blueprint, Response, jsonify, request
from pymongo.errors import OperationFailure
from app.database.database import get_database
from app.models.home.home_main_feature_item import HomeMainFeatureItem
from app.routes.blueprints import sweep_api_v1

home_main_feature_item_api_v1 = Blueprint('home_main_feature_item_api_v1', __name__,
                                          url_prefix='/home_main_feature_item')
home_main_feature_item_collection = get_database()['home_main_feature_items']


@home_main_feature_item_api_v1.route('/create', methods=['POST'])
def create_account_item_category() -> Response:
    """
    :return: Response object with a message describing if the account category was created and the status code
    """
    home_main_feature_item_document = request.json
    home_main_feature_item = HomeMainFeatureItem(home_main_feature_item_document=home_main_feature_item_document)
    try:
        home_main_feature_item_collection.insert_one(home_main_feature_item.__dict__)
    except OperationFailure:
        return jsonify({
            'message': 'home main feature item not added to the database.',
            'status': 500
        })
    return jsonify({
        'message': 'home main feature item added to the database.',
        'status': 200
    })


@home_main_feature_item_api_v1.route('/read', methods=['GET'])
def read_home_main_feature_items() -> Response:
    """
    :return: Response object with a message describing if the home main feature item was found and the status code
    (if yes: add home main feature item) and the status code
    """
    home_main_feature_items = []
    home_main_feature_item_documents = home_main_feature_item_collection.find()
    if home_main_feature_item_documents:
        for home_main_feature_item_document in home_main_feature_item_documents:
            home_main_feature_item_document = json \
                .loads(json_util.dumps(home_main_feature_item_document), object_hook=json_util.object_hook)
            home_main_feature_item = HomeMainFeatureItem(
                home_main_feature_item_document=home_main_feature_item_document)
            home_main_feature_items.append(home_main_feature_item.__dict__)
        return jsonify({
            'message': 'home main feature items found in the database.',
            'status': 200,
            'home_main_feature_item': home_main_feature_items
        })
    return jsonify({
        'message': 'No home main feature items found in the database.',
        'status': 404
    })


@home_main_feature_item_api_v1.route('/update/<string:_id>', methods=['PUT'])
def update_home_main_feature_item_by_name(_id: str) -> Response:
    """
    :param _id: Home main feature item's _id
    :return: Response object with a message describing if the home main feature item was found (if yes: update from
    home main feature items) and the status code
    """
    home_main_feature_item_document = request.json
    home_main_feature_item = HomeMainFeatureItem(
        home_main_feature_item_document=home_main_feature_item_document)
    result = home_main_feature_item_collection.update_one(
        {'_id': _id},
        {'$set': home_main_feature_item.__dict__}
    )
    if result.modified_count == 1:
        return jsonify({
            'message': 'Account category updated in the database using the id.',
            'status': 200,
        })
    return jsonify({
        'message': 'Account category not found in the database using the id.',
        'status': 404
    })


@home_main_feature_item_api_v1.route('/delete/<string:_id>', methods=['DELETE'])
def delete_home_main_feature_by_id(_id: str) -> Response:
    """
    :param _id: Home main feature item id
    :return: Response object with a message describing if the home main item was found (if yes: delete from the
    home main feature items) and the status code
    """
    result = home_main_feature_item_collection.delete_one({'_id': _id})
    if result.deleted_count == 1:
        return jsonify({
            'message': 'Home main feature item deleted from the database using the id.',
            'status': 200
        })
    return jsonify({
        'message': 'Home main feature item not found in the database using the id.',
        'status': 404
    })


sweep_api_v1.register_blueprint(home_main_feature_item_api_v1)
