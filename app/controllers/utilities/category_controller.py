"""Summary: Category Controller
A controller that assigns a child blueprint to sweep_api_v1 with routes for functions to create, read, update, and
delete categories from the database
"""

import json
import pymongo
from bson import json_util, ObjectId
from flask import Blueprint, Response, jsonify, request
from pymongo.errors import OperationFailure
from app.database.database import get_database
from app.models.utilities.category import Category
from app.routes.blueprints import sweep_api_v1

category_api_v1 = Blueprint('category_api_v1', __name__, url_prefix='/category')
category_collection = get_database()['categories']

category_collection.create_index([('name', pymongo.ASCENDING)], unique=True)


@category_api_v1.route('/create', methods=['POST'])
def create_category() -> Response:
    """
    :return: Response object with a message describing if the category was created and the status code
    """
    category_document = request.json
    category = Category(category_document=category_document)
    try:
        category_collection.insert_one(category.database_dict())
    except OperationFailure:
        return jsonify(
            message='Category not added to the database.',
            status=500
        )
    return jsonify(
        message='Category added to the database.',
        status=200
    )


@category_api_v1.route('/read/id/<string:_id>', methods=['GET'])  # notice the change in the route
def read_category_by_id(_id: str) -> Response:
    """
    :param _id: Category's id
    :return: Response object with a message describing if the categories were found (if yes: add user objects) and the
    status code
    """
    category_document = category_collection.find_one({'_id': ObjectId(_id)})
    if category_document:
        category = Category(category_document=category_document)
        return jsonify(
            data=category.__dict__,
            message='Category found in the database using the id.',
            status=200,
        )
    return jsonify(
        message='Category not found in the database using the id.',
        status=404
    )


@category_api_v1.route('/read', methods=['GET'])
def read_categories() -> Response:
    """
    :return: Response object with a message describing if the categories were found (if yes: add user objects) and the
    status code
    """
    categories = []
    category_documents = category_collection.find()
    if category_documents:
        for category_document in category_documents:
            category_document = json.loads(json_util.dumps(category_document), object_hook=json_util.object_hook)
            category = Category(category_document=category_document)
            categories.append(category.__dict__)
        return jsonify(
            data=categories,
            message='All categories found in the database.',
            status=200,
        )
    return jsonify(
        message='No categories not found in the database.',
        status=404
    )


@category_api_v1.route('/update/id/<string:_id>', methods=['PUT'])
def update_category_by_id(_id: str) -> Response:
    """
    :param _id: Category's id
    :return: Response object with a message describing if the category was updated and the status code
    """
    category_document = request.json
    category = Category(category_document=category_document)
    result = category_collection.update_one(
        {'_id': ObjectId(_id)},
        {'$set': category.__dict__}
    )
    if result.modified_count == 1:
        return jsonify(
            message='Category updated in the database.',
            status=200
        )
    return jsonify(
        message='Category not updated in the database.',
        status=500
    )


@category_api_v1.route('/delete/id/<string:_id>', methods=['DELETE'])
def delete_category_by_id(_id: str) -> Response:
    """
    :param _id: Category's id
    :return: Response object with a message describing if the category was deleted and the status code
    """

    result = category_collection.delete_one({_id: ObjectId(_id)})
    if result.deleted_count == 1:
        return jsonify(
            message='Category deleted from the database.',
            status=200
        )
    return jsonify(
        message='Category not deleted from the database.',
        status=500
    )


sweep_api_v1.register_blueprint(category_api_v1)
