"""Summary: Category Controller
A controller that assigns a child blueprint to sweep_api_v1 with routes for functions to create, read, update, and
delete categories from the database
"""

import json
from bson import json_util
from flask import Blueprint, Response, jsonify, request
from pymongo.errors import OperationFailure
from app.database.database import get_database
from app.models.utils.category import Category
from app.routes.blueprints import sweep_api_v1

category_api_v1 = Blueprint('category_api_v1', __name__, url_prefix='/category')
category_collection = get_database()['categories']


@category_api_v1.route('/create', methods=['POST'])
def create_category() -> Response:
    """
    :return: Response object with a message describing if the category was created and the status code
    """
    category_document = request.json
    category = Category(category_document=category_document)
    try:
        category_collection.insert_one(category.__dict__)
    except OperationFailure:
        return jsonify({
            'message': 'Category not added to the database.',
            'status': 500
        })
    return jsonify({
        'message': 'Category added to the database.',
        'status': 200
    })


@category_api_v1.route('/read/<string:category_id>', methods=['GET'])
def read_category_by_id(category_id: str) -> Response:
    """
    :param category_id: Category's id
    :return: Response object with a message describing if the categories were found (if yes: add user objects) and the
    status code
    """
    category_document = json.loads(json_util.dumps(category_collection.find_one({'category_id': category_id})),
                                   object_hook=json_util.object_hook)
    if category_document:
        category = Category(category_document=category_document)
        return jsonify({
            'message': 'Category found in the database using the id.',
            'status': 200,
            'category': category.__dict__
        })
    return jsonify({
        'message': 'Category not found in the database using the id.',
        'status': 404
    })


@category_api_v1.route('/read/<string:category_name>', methods=['GET'])
def read_category_by_name(category_name: str) -> Response:
    """
    :param category_name: Category's id
    :return: Response object with a message describing if the categories were found (if yes: add user objects) and the
    status code
    """
    category_document = json.loads(json_util.dumps(category_collection.find_one({'category_name': category_name})),
                                   object_hook=json_util.object_hook)
    if category_document:
        category = Category(category_document=category_document)
        return jsonify({
            'message': 'Category found in the database using the name.',
            'status': 200,
            'category': category.__dict__
        })
    return jsonify({
        'message': 'Category not found in the database using the name.',
        'status': 404
    })


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
        return jsonify({
            'message': 'All categories found in the database.',
            'status': 200,
            'categories': categories
        })
    return jsonify({
        'message': 'No categories not found in the database.',
        'status': 404
    })


@category_api_v1.route('/update/<string:category_id>', methods=['PUT'])
def update_category_by_id(category_id: str) -> Response:
    """
    :param category_id: Category's id
    :return: Response object with a message describing if the category was updated and the status code
    """
    category_document = []
    category = Category(category_document=category_document)
    result = category_collection.update_one(
        {'category_id': category_id},
        {'$set': category.__dict__}
    )
    if result.modified_count == 1:
        return jsonify({
            'message': 'Category updated in the database.',
            'status': 200
        })
    return jsonify({
        'message': 'Category not updated in the database.',
        'status': 500
    })


@category_api_v1.route('/update/<string:category_name>', methods=['PUT'])
def update_category_by_name(category_name: str) -> Response:
    """
    :param category_name: Category's id
    :return: Response object with a message describing if the category was updated and the status code
    """
    category_document = []
    category = Category(category_document=category_document)
    result = category_collection.update_one(
        {'category_name': category_name},
        {'$set': category.__dict__}
    )
    if result.modified_count == 1:
        return jsonify({
            'message': 'Category updated in the database.',
            'status': 200
        })
    return jsonify({
        'message': 'Category not updated in the database.',
        'status': 500
    })


@category_api_v1.route('/delete/<string:category_id>', methods=['DELETE'])
def delete_category_by_id(category_id: str) -> Response:
    """
    :param category_id: Category's id
    :return: Response object with a message describing if the category was deleted and the status code
    """

    result = category_collection.delete_one({'category_id': category_id})
    if result.deleted_count == 1:
        return jsonify({
            'message': 'Category deleted from the database.',
            'status': 200
        })
    return jsonify({
        'message': 'Category not deleted from the database.',
        'status': 500
    })


@category_api_v1.route('/delete/<string:category_name>', methods=['DELETE'])
def delete_category_by_name(category_name: str) -> Response:
    """
    :param category_name: Category's id
    :return: Response object with a message describing if the category was deleted and the status code
    """

    result = category_collection.delete_one({'category_id': category_name})
    if result.deleted_count == 1:
        return jsonify({
            'message': 'Category deleted from the database.',
            'status': 200
        })
    return jsonify({
        'message': 'Category not deleted from the database.',
        'status': 500
    })


sweep_api_v1.register_blueprint(category_api_v1)
