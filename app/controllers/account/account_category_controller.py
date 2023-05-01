"""Summary: Account Category Controller

A controller that assigns a child blueprint to sweep_api_v1 with routes for functions to create, read, update, and
delete account categories from the database
"""
from datetime import datetime
from bson import ObjectId
from flask import Blueprint, Response, jsonify, request
from pymongo import ASCENDING
from pymongo.errors import OperationFailure
from app.aws.aws_s3_client import upload_image_to_aws_s3, delete_images_from_aws_s3
from app.database.database import get_database
from app.models.account.account_category import AccountCategory

raw_account_category_api_v1 = Blueprint('account_category_api_v1', __name__, url_prefix='/account_category')
account_category_collection = get_database()['account_categories']

account_category_collection.create_index([('name', ASCENDING)], unique=True)
account_category_collection.create_index([('account_category_items.name', ASCENDING)], unique=True)


def _configure_account_category_document(account_category_document: dict) -> tuple[dict, bool]:
    """
    :param account_category_document: An account category document
    :return: An account category document with a configured metadata
    """
    image_updated = False
    for account_category_item_document in account_category_document['account_category_items']:
        if account_category_item_document['image']:
            image_updated = True
            account_category_item_image = (
                '',
                account_category_item_document['image'],
                account_category_item_document['image_path']
            )
            account_category_item_document['metadata'] = upload_image_to_aws_s3(
                object_metadata_document=account_category_item_document['metadata'],
                object_image=account_category_item_image
            ).json['data']

    return account_category_document, image_updated


@raw_account_category_api_v1.route('/create', methods=['POST'])
def create_account_category() -> Response:
    """
    :return: Response object with a message describing if the account category was created (if yes: add account category
    id) and the status code
    """
    account_category_document = request.json

    account_category_document['metadata']['created_date'] = datetime.now()
    account_category_document['metadata']['total_account_category_items'] = len(
        account_category_document['account_category_items']
    )

    account_category_document = \
        _configure_account_category_document(account_category_document=account_category_document)[0]

    account_category = AccountCategory(account_category_document=account_category_document)
    try:
        account_category_id = str(account_category_collection.insert_one(account_category.database_dict()).inserted_id)
    except OperationFailure:
        return jsonify(
            message='Account category not added to the database.',
            status=500
        )
    return jsonify(
        data=account_category_id,
        message='Account category added to the database.',
        status=200
    )


@raw_account_category_api_v1.route('/read/id/<string:_id>', methods=['GET'])
def read_account_category_by_id(_id: str) -> Response:
    """
    :param _id: Account category's id
    :return: Response object with a message describing if the account category was found (if yes: add account category)
    and the status code
    """
    account_category_document = account_category_collection.find_one({'_id': ObjectId(_id)})
    if account_category_document:
        account_category = AccountCategory(account_category_document=account_category_document)
        return jsonify(
            data=account_category.__dict__,
            message='Account category found in the database using the id.',
            status=200
        )
    return jsonify(
        message='Account category not found in the database using the id.',
        status=500
    )


@raw_account_category_api_v1.route('/read/name/<string:name>', methods=['GET'])
def read_account_category_by_name(name: str) -> Response:
    """
    :param name: Account category's name
    :return: Response object with a message describing if the account category was found (if yes: add account category)
    and the status code
    """
    account_category_document = account_category_collection.find_one({'name': name})
    if account_category_document:
        account_category = AccountCategory(account_category_document=account_category_document)
        return jsonify(
            data=account_category.__dict__,
            message='Main account category found in the database.',
            status=200
        )
    return jsonify(
        message='Main account category not found in the database.',
        status=500
    )


@raw_account_category_api_v1.route('/read/exclude/name/<string:name>', methods=['GET'])
def read_account_categories_exclude_name(name: str) -> Response:
    """
    :param name: Account category's name
    :return: Response object with a message describing if the account categories were found (if yes: add account
    categories) and the status code
    """
    account_categories = []
    account_category_documents = account_category_collection.find({'name': {'$ne': name}})
    if account_category_documents:
        for account_category_document in account_category_documents:
            account_category = AccountCategory(account_category_document=account_category_document)
            account_categories.append(account_category.__dict__)
        return jsonify(
            data=account_categories,
            message='Account categories without the name found in the database.',
            status=200
        )
    return jsonify(
        message='No account category without the name found in the database.',
        status=500
    )


@raw_account_category_api_v1.route('/read', methods=['GET'])
def read_account_categories() -> Response:
    """
    :return: Response object with a message describing if all the account categories were found (if yes: add account
    categories) and the status code
    """
    account_categories = []
    account_category_documents = account_category_collection.find()
    if account_category_documents:
        for account_category_document in account_category_documents:
            account_category = AccountCategory(account_category_document=account_category_document)
            account_categories.append(account_category.__dict__)
        return jsonify(
            data=account_categories,
            message='Account categories found in the database.',
            status=200
        )
    return jsonify(
        message='No account category found in the database.',
        status=500
    )


@raw_account_category_api_v1.route('/update/id/<string:_id>', methods=['PUT'])
def update_account_category_by_id(_id: str) -> Response:
    """
    :param _id: Account category's id
    :return: Response object with a message describing if the account category was found (if yes: update account
    category) and the status code
    """
    account_category_document = request.json

    account_category_document['metadata']['total_account_category_items'] = \
        len(account_category_document['account_category_items'])
    account_category_document['metadata']['updated_date'] = datetime.now()

    account_category_document, image_updated = \
        _configure_account_category_document(account_category_document=account_category_document)

    account_category = AccountCategory(account_category_document=account_category_document)
    result = account_category_collection.update_one(
        {'_id': ObjectId(_id)},
        {'$set': account_category.database_dict()}
    )
    if image_updated or result.modified_count == 1:
        return jsonify(
            message='Account category updated in the database using the id.',
            status=200
        )
    return jsonify(
        message='Account category not updated in the database using the id.',
        status=500
    )


@raw_account_category_api_v1.route('/delete/id/<string:_id>', methods=['DELETE'])
def delete_account_category_by_id(_id: str) -> Response:
    """
    :param _id: Account category's id
    :return: Response object with a message describing if the account category was found (if yes: delete account
    category) and the status code
    """
    account_category_document = read_account_category_by_id(_id=_id).json['data']

    image_paths = []
    for account_category_item in account_category_document['account_category_items']:
        image_paths.append(account_category_item['image_path'])
    delete_images_from_aws_s3(image_paths=image_paths)

    result = account_category_collection.delete_one({'_id': ObjectId(_id)})
    if result.deleted_count == 1:
        return jsonify(
            message='Account category deleted from the database using the id.',
            status=200
        )
    return jsonify(
        message='Account category not deleted in the database using the id.',
        status=500
    )


account_category_api_v1 = raw_account_category_api_v1
