"""Summary: Account Category Item Controller CRUD Operations

A controller that assigns a child blueprint to sweep_api_v1 with routes for functions to create, read, update, and
delete account category items from the database
"""

import json
import pymongo
from bson import json_util, ObjectId
from flask import Blueprint, Response, jsonify, request
from pymongo.errors import OperationFailure
from app.database.database import get_database
from app.models.account.account_category_item import AccountCategoryItem
from app.routes.blueprints import sweep_api_v1
from app.utilities.aws_cloudfront_client import create_cloudfront_url
from app.utilities.aws_s3_client import upload_to_aws_s3

account_category_item_api_v1 = Blueprint('account_category_item_api_v1', __name__, url_prefix='/account_category_item')
account_category_item_collection = get_database()['account_category_items']

account_category_item_collection.create_index(
    [('account_category_name', pymongo.ASCENDING), ('name', pymongo.ASCENDING)],
    unique=True
)


def _configure_account_category_item(account_category_item_document: dict) -> AccountCategoryItem:
    account_category_item_document = json.loads(json_util.dumps(account_category_item_document),
                                                object_hook=json_util.object_hook)
    account_category_item = AccountCategoryItem(account_category_item_document=account_category_item_document)
    account_category_item.image_url = create_cloudfront_url(file_path=account_category_item.file_path)
    return account_category_item


@account_category_item_api_v1.route('/create', methods=['POST'])
def create_account_category_item() -> Response:
    """
    :return: Response object with a message describing if the account category item was created and the status code
    """
    account_category_item_document = request.json
    upload_to_aws_s3(file_data=request.json['image'], file_path=request.json['file_path'])
    account_category_item = AccountCategoryItem(account_category_item_document=account_category_item_document)
    try:
        account_category_item_collection.insert_one(account_category_item.create_dict())
    except OperationFailure:
        return jsonify({
            'message': 'Account category item not added to the database.',
            'status': 500
        })
    return jsonify({
        'message': 'Account category item added to the database.',
        'status': 200
    })


@account_category_item_api_v1.route('/read', methods=['GET'])
def read_account_category_items() -> Response:
    """
    :return: Response object with a message describing if all the account category items were found (if yes: add account
    category items) and the status code
    """
    account_category_items = []
    account_category_item_documents = account_category_item_collection.find()
    if account_category_item_documents:
        for account_category_item_document in account_category_item_documents:
            account_category_item = _configure_account_category_item(
                account_category_item_document=account_category_item_document
            )
            account_category_items.append(account_category_item.__dict__)
        return jsonify({
            'data': account_category_items,
            'message': 'Account category items found in the database.',
            'status': 200
        })
    return jsonify({
        'message': 'No account category item found in the database.',
        'status': 404
    })


@account_category_item_api_v1.route('/read/id/<string:_id>', methods=['GET'])
def read_account_category_item_by_id(_id: str) -> Response:
    """
    :param _id: Account category item's id
    :return: Response object with a message describing if the account category item was found (if yes: add account
    category item) and the status code
    """
    account_category_item_document = account_category_item_collection.find_one({'_id': ObjectId(_id)})
    if account_category_item_document:
        account_category_item = _configure_account_category_item(
            account_category_item_document=account_category_item_document
        )
        return jsonify({
            'data': account_category_item.__dict__,
            'message': 'Account category item found in the database using the id.',
            'status': 200
        })
    return jsonify({
        'message': 'No account category item found in the database using the id.',
        'status': 404
    })


@account_category_item_api_v1.route('/read/account_category_name/<string:account_category_name>', methods=['GET'])
def read_account_category_items_by_account_category_name(account_category_name: str) -> Response:
    """
    :param account_category_name: Account category item's account category name
    :return: Response object with a message describing if the account category items were found (if yes: add account
    category items) and the status code
    """
    account_category_items = []
    account_category_item_documents = account_category_item_collection \
        .find({'account_category_name': account_category_name})
    if account_category_item_documents:
        for account_category_item_document in account_category_item_documents:
            account_category_item = _configure_account_category_item(
                account_category_item_document=account_category_item_document
            )
            account_category_items.append(account_category_item.__dict__)
        return jsonify({
            'data': account_category_items,
            'message': 'Account category items found in the database using the account category name.',
            'status': 200
        })
    return jsonify({
        'message': 'No account category item found in the database using the account category name.',
        'status': 404
    })


@account_category_item_api_v1.route('/update/id/<string:_id>', methods=['PUT'])
def update_account_category_item_by_id(_id: str) -> Response:
    """
    :param _id: Account category item's id
    :return: Response object with a message describing if the account category item was found (if yes: update
    account category item) and the status code
    """
    account_category_item_document = request.json
    account_category_item = AccountCategoryItem(account_category_item_document=account_category_item_document)
    result = account_category_item_collection.update_one(
        {'_id': ObjectId(_id)},
        {'$set': account_category_item.__dict__}
    )
    if result.modified_count == 1:
        return jsonify({
            'message': 'Account category item updated in the database using the id.',
            'status': 200,
        })
    return jsonify({
        'message': 'Account category item not found in the database using the id.',
        'status': 404
    })


@account_category_item_api_v1.route('/delete/id/<string:_id>', methods=['DELETE'])
def delete_account_category_by_id(_id: str) -> Response:
    """
    :param _id: Account category item's id
    :return: Response object with a message describing if the account category item was found (if yes: delete
    account category item) and the status code
    """
    result = account_category_item_collection.delete_one({'_id': ObjectId(_id)})
    if result.deleted_count == 1:
        return jsonify({
            'message': 'Account category item deleted from the database using the id.',
            'status': 200
        })
    return jsonify({
        'message': 'Account category item not found in the database using the id.',
        'status': 404
    })


sweep_api_v1.register_blueprint(account_category_item_api_v1)
