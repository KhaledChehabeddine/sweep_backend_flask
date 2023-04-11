"""Summary: Account Category Item Controller CRUD Operations

A controller that assigns a child blueprint to sweep_api_v1 with routes for functions to create, read, update, and
delete account categories items from the database
"""

import json
from bson import json_util
from flask import Blueprint, Response, jsonify, request
from pymongo.errors import OperationFailure
from app.database.database import get_database
from app.models.account.account_category_item import AccountCategoryItem
from app.routes.blueprints import sweep_api_v1

account_category_item_api_v1 = Blueprint('account_category_item_api_v1', __name__, url_prefix='/account_category_item')
account_category_item_collection = get_database()['account_category_items']


@account_category_item_api_v1.route('/create', methods=['POST'])
def create_account_item_category() -> Response:
    """
    :return: Response object with a message describing if the account category was created and the status code
    """
    account_category_item_document = request.json
    account_category_item = AccountCategoryItem(account_category_item_document=account_category_item_document)
    try:
        account_category_item_collection.insert_one(account_category_item.__dict__)
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
    :return: Response object with a message describing if the account category item was found and the status code
    (if yes: add account category item) and the status code
    """
    account_category_items = []
    account_category_item_documents = account_category_item_collection.find()
    if account_category_item_documents:
        for account_category_item_document in account_category_item_documents:
            account_category_item_document = json \
                .loads(json_util.dumps(account_category_item_document), object_hook=json_util.object_hook)
            account_category_item = AccountCategoryItem(
                account_category_item_document=account_category_item_document)
            account_category_items.append(account_category_item.__dict__)
        return jsonify({
            'message': 'Account category items found in the database.',
            'status': 200,
            'account_category_item': account_category_items
        })
    return jsonify({
        'message': 'No account category item found in the database.',
        'status': 404
    })


@account_category_item_api_v1.route('/update/<string:name>', methods=['PUT'])
def update_account_category_item_by_name(name: str) -> Response:
    """
    :param name: Account category item's name
    :return: Response object with a message describing if the account category item was found (if yes: update
    account category) and the status code
    """
    account_category_item_document = request.json
    account_category_item = AccountCategoryItem(
        account_category_item_document=account_category_item_document)
    result = account_category_item_collection.update_one(
        {'name': name},
        {'$set': account_category_item.__dict__}
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


@account_category_item_api_v1.route('/delete/<string:name>', methods=['DELETE'])
def delete_account_category_by_name(name: str) -> Response:
    """
    :param name: Account category item's name
    :return: Response object with a message describing if the account category item was found (if yes: delete
    account category) and the status code
    """
    result = account_category_item_collection.delete_one({'name': name})
    if result.deleted_count == 1:
        return jsonify({
            'message': 'Account category item deleted from the database using the name.',
            'status': 200
        })
    return jsonify({
        'message': 'Account category item not found in the database using the name.',
        'status': 404
    })


sweep_api_v1.register_blueprint(account_category_item_api_v1)
