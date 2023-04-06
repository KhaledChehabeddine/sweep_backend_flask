"""Summary: Account Main Category Controller CRUD Operations

A controller that assigns a child blueprint to sweep_api_v1 with routes for functions to create, read, update, and
delete account main categories from the database
"""

import json
from bson import json_util
from flask import Blueprint, Response, jsonify, request
from pymongo.errors import OperationFailure
from app.database.database import get_database
from app.models.account.account_main_category import AccountMainCategory
from app.routes.blueprints import sweep_api_v1

account_main_category_api_v1 = Blueprint('account_main_category_api_v1', __name__, url_prefix='/account_main_category')
account_main_category_collection = get_database()['account_main_categories']


@account_main_category_api_v1.route('/create', methods=['POST'])
def create_account_main_category() -> Response:
    """
    :return: Response object with a message describing if the account main category was created and the status code
    """
    account_main_category_document = request.json
    account_main_category = AccountMainCategory(account_main_category_document=account_main_category_document)
    try:
        account_main_category_collection.insert_one(account_main_category.__dict__)
    except OperationFailure:
        return jsonify({
            'message': 'Account main category not added to the database.',
            'status': 500
        })
    return jsonify({
        'message': 'Account main category added to the database.',
        'status': 200
    })


@account_main_category_api_v1.route('/read', methods=['GET'])
def read_account_main_category() -> Response:
    """
    :return: Response object with a message describing if the account main category was found (if yes: add account main
    category) and the status code
    """
    account_main_category = None
    account_main_category_documents = account_main_category_collection.find()
    if account_main_category_documents:
        for account_main_category_document in account_main_category_documents:
            account_main_category_document = json\
                .loads(json_util.dumps(account_main_category_document), object_hook=json_util.object_hook)
            account_main_category = AccountMainCategory(account_main_category_document=account_main_category_document)
        return jsonify({
            'message': 'Account main category found in the database.',
            'status': 200,
            'account_main_category': account_main_category.__dict__
        })
    return jsonify({
        'message': 'Account main category not found in the database.',
        'status': 404
    })


@account_main_category_api_v1.route('/update', methods=['PUT'])
def update_account_main_category() -> Response:
    """
    :return: Response object with a message describing if the account main category was found (if yes: update account
    main category) and the status code
    """
    account_main_category_document = request.json
    account_main_category = AccountMainCategory(account_main_category_document=account_main_category_document)
    result = account_main_category_collection.update_one(
        {},
        {'$set': account_main_category.__dict__}
    )
    if result.modified_count == 1:
        return jsonify({
            'message': 'Account main category updated in the database.',
            'status': 200,
        })
    return jsonify({
        'message': 'Account main category not found in the database.',
        'status': 404
    })


@account_main_category_api_v1.route('/delete', methods=['DELETE'])
def delete_account_main_category() -> Response:
    """
    :return: Response object with a message describing if the account main category was found (if yes: delete account
    main category) and the status code
    """
    result = account_main_category_collection.delete_one({}, {'limit': 1})
    if result.deleted_count == 1:
        return jsonify({
            'message': 'Account main category deleted from the database.',
            'status': 200
        })
    return jsonify({
        'message': 'Account main category not found in the database.',
        'status': 404
    })


sweep_api_v1.register_blueprint(account_main_category_api_v1)
