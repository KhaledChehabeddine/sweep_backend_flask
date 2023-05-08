"""Summary: Search Category Controller

A controller that assigns a child blueprint to sweep_api_v1 with routes for functions to create, read, update, and
delete search category items from the database
"""
from bson import ObjectId
from flask import Blueprint, Response, jsonify, request
from pymongo import ASCENDING, errors
from app.database.database import get_database
from app.functions.create_object_metadata import create_search_category_metadata
from app.models.search.search_category import SearchCategory

raw_search_category_api_v1 = Blueprint('search_category_api_v1', __name__, url_prefix='/search_category')
search_category_collection = get_database()['search_categories']

search_category_collection.create_index([('category_name', ASCENDING)], unique=True)


@raw_search_category_api_v1.route('/create', methods=['POST'])
def create_search_category() -> Response:
    """
    :return: Response object with a message describing if the search category was created (if yes: add search category
    id) and the status code
    """
    search_category_document = request.json

    search_category_document['metadata'] = \
        create_search_category_metadata()

    search_category = SearchCategory(search_category_document=search_category_document)
    try:
        search_category_id = str(search_category_collection.insert_one(search_category.database_document()).inserted_id)
    except errors.OperationFailure:
        return jsonify(
            message='Search category not added to the database.',
            status=500
        )
    return jsonify(
        data=search_category_id,
        message='Search category added to the database.',
        status=200
    )


@raw_search_category_api_v1.route('/read/id/<string:_id>', methods=['GET'])
def read_search_category_by_id(_id: str) -> Response:
    """
    :param _id: Search category's id
    :return: Response object with a message describing if the search category was found (if yes: add search category
    objects) and the status code
    """
    search_category_document = search_category_collection.find_one({'_id': ObjectId(_id)})
    if search_category_document:
        search_category = SearchCategory(search_category_document=search_category_document)
        return jsonify(
            data=search_category.__dict__,
            message='Search category found in the database using the id.',
            status=200,
        )
    return jsonify(
        message='Search category not found in the database using the id.',
        status=404
    )


@raw_search_category_api_v1.route('/read/name/<string:category_name>', methods=['GET'])
def read_search_category_by_name(category_name: str) -> Response:
    """
    :param category_name: Search category's name
    :return: Response object with a message describing if the search category was found (if yes: return search category
    objects) and the status code
    """
    search_category_document = search_category_collection.find_one({'category_name': category_name})
    if search_category_document:
        search_category = SearchCategory(search_category_document=search_category_document)
        return jsonify(
            data=search_category.__dict__,
            message='Search Category found in the database using the name.',
            status=200,
        )
    return jsonify(
        message='Search Category not found in the database using the name.',
        status=404
    )


@raw_search_category_api_v1.route('/read/all/', methods=['GET'])
def read_all_search_categories() -> Response:
    """
    :return: Response object with a message describing if the search categories were found (if yes: add search category
    objects) and the status code
    """
    search_categories = []
    search_category_documents = search_category_collection.find({})
    if search_category_documents:
        for search_category_document in search_category_documents:
            search_category = SearchCategory(search_category_document=search_category_document)
            search_categories.append(search_category.__dict__)
        return jsonify(
            data=search_categories,
            message='Search Categories found in the database.',
            status=200,
        )
    return jsonify(
        message='Search Categories not found in the database.',
        status=404
    )


@raw_search_category_api_v1.route('/update/id/<string:_id>', methods=['PUT'])
def update_search_category_by_id(_id: str) -> Response:
    """
    :param _id: Search Category's id
    :return: Response object with a message describing if the search category was updated (if yes: add search category
    id) and the status code
    """
    search_category_document = request.json

    search_category_document['metadata'] = create_search_category_metadata()

    search_category = SearchCategory(search_category_document=search_category_document)

    existing_category = search_category_collection.find_one({'_id': ObjectId(_id)})
    if not existing_category:
        return jsonify(
            message='Search Category not found in the database.',
            status=404
        )
    try:
        result = search_category_collection.update_one({'_id': ObjectId(_id)},
                                                       {'$set': search_category.database_document()})
    except errors.OperationFailure:
        return jsonify(
            message='Search Category not updated in the database.',
            status=500
        )
    if result.modified_count:
        return jsonify(
            data=_id,
            message='Search Category updated in the database.',
            status=200
        )
    return jsonify(
        message='An error occurred while updating the search category.',
        status=500
    )


@raw_search_category_api_v1.route('/delete/id/<string:_id>', methods=['DELETE'])
def delete_search_category_by_id(_id: str) -> Response:
    """
    :param _id: Search category's id
    :return: Response object with a message describing if the search category was deleted (if yes: add search category
    id) and the status code
    """
    existing_category = search_category_collection.find_one({'_id': ObjectId(_id)})
    if not existing_category:
        return jsonify(
            message='Search Category not found in the database.',
            status=404
        )
    try:
        result = search_category_collection.delete_one({'_id': ObjectId(_id)})
        if result.deleted_count == 1:
            return jsonify(
                message='Search category item deleted from the database using the id.',
                status=200
            )
        return jsonify(
            message='Search category item not deleted from the database using the id.',
            status=404
        )
    except errors.OperationFailure:
        return jsonify(
            message='Search category not deleted from the database.',
            status=500
        )


search_category_api_v1 = raw_search_category_api_v1
