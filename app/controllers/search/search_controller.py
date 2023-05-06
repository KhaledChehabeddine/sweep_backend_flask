"""Summary: Search Controller

A controller that assigns a child blueprint to sweep_api_v1 with routes for functions to create, read, update, and
delete search items from the database
"""
from bson import ObjectId
from flask import Blueprint, Response, jsonify, request
from pymongo import ASCENDING, errors
from app.database.database import get_database
from app.functions.create_object_metadatas import create_search_metadata
from app.models.search.search import Search

raw_search_api_v1 = Blueprint('search_api_v1', __name__, url_prefix='/search')
search_collection = get_database()['searches']

search_collection.create_index([('name', ASCENDING)], unique=True)


@raw_search_api_v1.route('/create', methods=['POST'])
def create_search() -> Response:
    """
    :return: Response object with a message describing if the search was created (if yes: add search
    id) and the status code
    """
    search_document = request.json

    search_document['metadata'] = \
        create_search_metadata()

    search = Search(search_document=search_document)
    try:
        search_id = str(search_collection.insert_one(search.database_dict()).inserted_id)
    except errors.OperationFailure:
        return jsonify(
            message='Search not added to the database.',
            status=500

        )
    return jsonify(
        data=search_id,
        message='Search added to the database.',
        status=200
    )


@raw_search_api_v1.route('/read/id/<string:_id>', methods=['GET'])
def read_search_by_id(_id: str) -> Response:
    """
    :param _id: Service Category's id
    :return: Response object with a message describing if the searches were found (if yes: add user objects)
    and the status code
    """
    search_document = search_collection.find_one({'_id': ObjectId(_id)})
    if search_document:
        search = Search(search_document=search_document)
        return jsonify(
            data=search.__dict__,
            message='Search found in the database using the id.',
            status=200,
        )
    return jsonify(
        message='Search not found in the database using the id.',
        status=404
    )


@raw_search_api_v1.route('/read/query/<string:query>', methods=['GET'])
def read_search_by_query(query: str) -> Response:
    """
    :param query: Service Category's query
    :return: Response object with a message describing if the searches were found (if yes: add search objects)
    and the status code
    """
    search_document = search_collection.find_one({'query': query})
    if search_document:
        search = Search(search_document=search_document)
        return jsonify(
            data=search.__dict__,
            message='Search found in the database using the query.',
            status=200,
        )
    return jsonify(
        message='Search not found in the database using the query.',
        status=404
    )


@raw_search_api_v1.route('/read/all/', methods=['GET'])
def read_searches() -> Response:
    """
    :return: Response object with a message describing if the searches were found (if yes: add user objects)
    and the status code
    """
    searches = []
    search_documents = search_collection.find()
    if search_documents:
        for search_document in search_documents:
            search = Search(search_document=search_document)
            searches.append(search.__dict__)
        return jsonify(
            data=searches,
            message='All searches found in the database.',
            status=200,
        )
    return jsonify(
        message='No search found in the database.',
        status=404
    )


@raw_search_api_v1.route('/update/id/<string:_id>', methods=['PUT'])
def update_search_by_id(_id: str) -> Response:
    """
    :param _id: Search's id
    :return: Response object with a message describing if the search was updated and the status code
    """
    search_document = request.json

    search_document['metadata'] = \
        create_search_metadata()

    search = Search(search_document=search_document)
    result = search_collection.update_one(
        {'_id': ObjectId(_id)},
        {'$set': search.database_dict()}
    )
    if result.modified_count == 1:
        return jsonify(
            message='Search item updated in the database using the id.',
            status=200
        )
    return jsonify(
        message='Search item not updated in the database using the id.',
        status=404
    )


@raw_search_api_v1.route('/delete/id/<string:_id>', methods=['DELETE'])
def delete_search_by_id(_id: str) -> Response:
    """
    :param _id: Search's id
    :return: Response object with a message describing if the search was deleted and the status code
    """

    result = search_collection.delete_one({'_id': ObjectId(_id)})
    if result.deleted_count == 1:
        return jsonify(
            message='Search item deleted from the database using the id.',
            status=200
        )
    return jsonify(
        message='Search item not deleted from the database using the id.',
        status=404
    )


search_api_v1 = raw_search_api_v1
