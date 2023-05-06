"""Summary: Search result Category Controller

A controller that assigns a child blueprint to sweep_api_v1 with routes for functions to create, read, update, and
delete search result category items from the database
"""
from bson import ObjectId
from flask import Blueprint, Response, jsonify, request
from pymongo import ASCENDING, errors
from app.database.database import get_database
from app.functions.create_object_metadata import create_search_result_category_metadata
from app.models.search.search_result import SearchResult

raw_search_result_api_v1 = Blueprint('search_result_api_v1', __name__, url_prefix='/search_result')
search_result_collection = get_database()['search_results']

search_result_collection.create_index([('category_name', ASCENDING)], unique=True)


@raw_search_result_api_v1.route('/create', methods=['POST'])
def create_search_result() -> Response:
    """
    :return: Response object with a message describing if the search result was created (if yes: add search result
    id) and the status code
    """
    search_result_document = request.json

    search_result_document['metadata'] = \
        create_search_result_category_metadata()

    search_result = SearchResult(search_result_document=search_result_document)
    try:
        search_result_id = str(search_result_collection.insert_one(search_result.database_dict()).inserted_id)
    except errors.OperationFailure:
        return jsonify(
            message='Search Result not added to the database.',
            status=500
        )
    return jsonify(
        data=search_result_id,
        message='Search Result added to the database.',
        status=200
    )


@raw_search_result_api_v1.route('/read/id/<string:_id>', methods=['GET'])
def read_search_result_by_id(_id: str) -> Response:
    """
    :param _id: Search Result's id
    :return: Response object with a message describing if the search result was found (if yes: add search result
    objects) and the status code
    """
    search_result_document = search_result_collection.find_one({'_id': ObjectId(_id)})
    if search_result_document:
        search_result = SearchResult(search_result_document=search_result_document)
        return jsonify(
            data=search_result.__dict__,
            message='Search Result found in the database using the id.',
            status=200,
        )
    return jsonify(
        message='Search Result not found in the database using the id.',
        status=404,
    )


@raw_search_result_api_v1.route('/read/name/<string:name>', methods=['GET'])
def read_search_result_by_name(name: str) -> Response:
    """
    :param name: Search Result's name
    :return: Response object with a message describing if the search result was found (if yes: add search result
    objects) and the status code
    """
    search_result_document = search_result_collection.find_one({'name': name})
    if search_result_document:
        search_result = SearchResult(search_result_document=search_result_document)
        return jsonify(
            data=search_result.__dict__,
            message='Search Result found in the database using the name.',
            status=200,
        )
    return jsonify(
        message='Search Result not found in the database using the name.',
        status=404,
    )


@raw_search_result_api_v1.route('/read/all', methods=['GET'])
def read_all_search_results() -> Response:
    """
    :return: Response object with a message describing if the search results were found (if yes: add search result
    objects) and the status code
    """
    search_result_documents = search_result_collection.find()
    if search_result_documents:
        search_results = []
        for search_result_document in search_result_documents:
            search_result = SearchResult(search_result_document=search_result_document)
            search_results.append(search_result.__dict__)
        return jsonify(
            data=search_results,
            message='Search Results found in the database.',
            status=200,
        )
    return jsonify(
        message='Search Results not found in the database.',
        status=404,
    )


@raw_search_result_api_v1.route('/update/id/<string:_id>', methods=['PUT'])
def update_search_result_by_id(_id: str) -> Response:
    """
    :param _id: Search Result's id
    :return: Response object with a message describing if the search result was updated and the status code
    """
    search_result_document = search_result_collection.find_one({'_id': ObjectId(_id)})
    if search_result_document:
        search_result_document.update(request.json)
        search_result_collection.replace_one({'_id': ObjectId(_id)}, search_result_document)
        return jsonify(
            message='Search Result updated in the database using the id.',
            status=200,
        )
    return jsonify(
        message='Search Result not found in the database using the id.',
        status=404,
    )


@raw_search_result_api_v1.route('/update/name/<string:name>', methods=['PUT'])
def update_search_result_by_name(name: str) -> Response:
    """
    :param name: Search Result's name
    :return: Response object with a message describing if the search result was updated and the status code
    """
    search_result_document = search_result_collection.find_one({'name': name})
    if search_result_document:
        search_result_document.update(request.json)
        search_result_collection.replace_one({'name': name}, search_result_document)
        return jsonify(
            message='Search Result updated in the database using the name.',
            status=200,
        )
    return jsonify(
        message='Search Result not found in the database using the name.',
        status=404,
    )


@raw_search_result_api_v1.route('/delete/id/<string:_id>', methods=['DELETE'])
def delete_search_result_by_id(_id: str) -> Response:
    """
    :param _id: Search Result's id
    :return: Response object with a message describing if the search result was deleted and the status code
    """
    search_result_document = search_result_collection.find_one({'_id': ObjectId(_id)})
    if search_result_document:
        search_result_collection.delete_one({'_id': ObjectId(_id)})
        return jsonify(
            message='Search Result deleted in the database using the id.',
            status=200,
        )
    return jsonify(
        message='Search Result not found in the database using the id.',
        status=404,
    )


@raw_search_result_api_v1.route('/delete/all', methods=['DELETE'])
def delete_all_search_results() -> Response:
    """
    :return: Response object with a message describing if the search results were deleted and the status code
    """
    search_result_documents = search_result_collection.find()
    if search_result_documents:
        search_result_collection.delete_many({})
        return jsonify(
            message='Search Results deleted in the database.',
            status=200,
        )
    return jsonify(
        message='Search Results not found in the database.',
        status=404,
    )


search_result_api_v1 = raw_search_result_api_v1
