"""Summary: Home Sub Feature Item Controller CRUD Operations

A controller that assigns a child blueprint to sweep_api_v1 with routes for functions to create, read, update, and
delete home sub feature items from the database
"""

from bson import ObjectId
from flask import Blueprint, Response, jsonify, request
from pymongo.errors import OperationFailure
from app.database.database import get_database
from app.functions.aws_update_operation_status import aws_update_operations
from app.models.home.home_sub_feature_item import HomeSubFeatureItem
from app.routes.blueprints import sweep_api_v1
from app.aws.aws_cloudfront_client import create_cloudfront_url
from app.aws.aws_s3_client import upload_to_aws_s3, delete_from_aws_s3

home_sub_feature_item_api_v1 = Blueprint('home_sub_feature_item_api_v1', __name__, url_prefix='/home_sub_feature_item')
home_sub_feature_item_collection = get_database()['home_sub_feature_items']


def _configure_home_sub_feature_item(home_sub_feature_item_document: dict) -> HomeSubFeatureItem:
    """
    :param home_sub_feature_item_document: A dictionary representing a home sub feature item document
    :return: A home sub feature item object with the image url configured
    """
    home_sub_feature_item = HomeSubFeatureItem(home_sub_feature_item_document=home_sub_feature_item_document)
    home_sub_feature_item.image_url = create_cloudfront_url(file_path=home_sub_feature_item.file_path)
    return home_sub_feature_item


@home_sub_feature_item_api_v1.route('/create', methods=['POST'])
def create_home_sub_feature_item() -> Response:
    """
    :return: Response object with a message describing if the home sub feature item was created and the status code
    """
    home_sub_feature_item_document = request.json

    upload_to_aws_s3(file_data=request.json['image'], file_path=request.json['file_path'])

    home_sub_feature_item = HomeSubFeatureItem(home_sub_feature_item_document=home_sub_feature_item_document)
    try:
        home_sub_feature_item_collection.insert_one(home_sub_feature_item.database_dict())
    except OperationFailure:
        return jsonify(
            message='Home sub feature item not added to the database.',
            status=500
        )
    return jsonify(
        message='Home sub feature item added to the database.',
        status=200
    )


@home_sub_feature_item_api_v1.route('/read/id/<string:_id>', methods=['GET'])
def read_home_sub_feature_item_by_id(_id: str) -> Response:
    """
    :param _id: Home sub feature item's id
    :return: Response object with a message describing if the home sub feature item was found (if yes: add home
    sub feature item) and the status code
    """
    home_sub_feature_item_document = home_sub_feature_item_collection.find_one({'_id': ObjectId(_id)})
    if home_sub_feature_item_document:
        home_sub_feature_item = _configure_home_sub_feature_item(
            home_sub_feature_item_document=home_sub_feature_item_document
        )
        return jsonify(
            data=home_sub_feature_item.__dict__,
            message='Home sub feature item found in the database using the id.',
            status=200
        )
    return jsonify(
        message='Home sub feature item not found in the database using the id.',
        status=500
    )


@home_sub_feature_item_api_v1.route('/read', methods=['GET'])
def read_home_sub_feature_items() -> Response:
    """
    :return: Response object with a message describing if all the home sub feature items were found (if yes: add home
    sub feature items) and the status code
    """
    home_sub_feature_items = []
    home_sub_feature_item_documents = home_sub_feature_item_collection.find()
    if home_sub_feature_item_documents:
        for home_sub_feature_item_document in home_sub_feature_item_documents:
            home_sub_feature_item = _configure_home_sub_feature_item(
                home_sub_feature_item_document=home_sub_feature_item_document
            )
            home_sub_feature_items.append(home_sub_feature_item.__dict__)
        return jsonify(
            data=home_sub_feature_items,
            message='Home sub feature items found in the database.',
            status=200
        )
    return jsonify(
        message='No home sub feature item found in the database.',
        status=500
    )


@home_sub_feature_item_api_v1.route('/update/id/<string:_id>', methods=['PUT'])
def update_home_sub_feature_item_by_id(_id: str) -> Response:
    """
    :param _id: Home sub feature item's id
    :return: Response object with a message describing if the home sub feature item was found (if yes: update
    home sub feature item) and the status code
    """
    home_sub_feature_item_document = request.json

    aws_update_operations(object_document=home_sub_feature_item_document)

    home_sub_feature_item = HomeSubFeatureItem(home_sub_feature_item_document=home_sub_feature_item_document)
    result = home_sub_feature_item_collection.update_one(
        {'_id': ObjectId(_id)},
        {'$set': home_sub_feature_item.database_dict()}
    )
    if home_sub_feature_item_document['image'] or result.modified_count == 1:
        return jsonify(
            message='Home Sub Feature item updated in the database using the id.',
            status=200,
        )
    return jsonify(
        message='Home Sub Feature item not updated in the database using the id.',
        status=500
    )


@home_sub_feature_item_api_v1.route('/delete/id/<string:_id>', methods=['DELETE'])
def delete_home_sub_feature_item_by_id(_id: str) -> Response:
    """
    :param _id: Home sub feature item's id
    :return: Response object with a message describing if the home sub feature item was found (if yes: delete
    home sub feature item) and the status code
    """
    home_sub_feature_item_document = read_home_sub_feature_item_by_id(_id=_id).json['data']

    delete_from_aws_s3(file_path=home_sub_feature_item_document['file_path'])

    result = home_sub_feature_item_collection.delete_one({'_id': ObjectId(_id)})
    if result.deleted_count == 1:
        return jsonify(
            message='Home Sub feature item deleted from the database using the id.',
            status=200
        )
    return jsonify(
        message='Home Sub Feature item not deleted in the database using the id.',
        status=500
    )


sweep_api_v1.register_blueprint(home_sub_feature_item_api_v1)
