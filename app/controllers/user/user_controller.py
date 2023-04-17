"""Summary: User Controller CRUD Operations

A controller that assigns a child blueprint to sweep_api_v1 with routes for functions to create, read, update, and
delete users from the database
"""

import pymongo
from bson import ObjectId
from flask import Blueprint, Response, jsonify, request
from pymongo.errors import OperationFailure
from app.database.database import get_database
from app.models.user.user import User
from app.routes.blueprints import sweep_api_v1

user_api_v1 = Blueprint('user_api_v1', __name__, url_prefix='/user')
user_collection = get_database()['users']

user_collection.create_index([('email', pymongo.ASCENDING)], unique=True)
user_collection.create_index([('phone_number', pymongo.ASCENDING)], unique=True)
user_collection.create_index([('username', pymongo.ASCENDING)], unique=True)


@user_api_v1.route('/create', methods=['POST'])
def create_user() -> Response:
    """
    :return: Response object with a message describing if the user was created and the status code
    """
    user_document = request.json
    user = User(user_document=user_document)
    try:
        user_collection.insert_one(user.database_dict())
    except OperationFailure:
        return jsonify(
            message='User not added to the database.',
            status=500
        )
    return jsonify(
        message='User added to the database.',
        status=200
    )


@user_api_v1.route('/read/id/<string:_id>', methods=['GET'])
def read_user_by_id(_id: str) -> Response:
    """
    :param _id: User's id
    :return: Response object with a message describing if the user was found (if yes: add user object) and the status
    code
    """
    user_document = user_collection.find_one({'_id': ObjectId(_id)})
    if user_document:
        user = User(user_document=user_document)
        return jsonify(
            user=user.__dict__,
            message='User found in the database using the id.',
            status=200
        )
    return jsonify(
        message='User not found in the database using the id.',
        status=500
    )


@user_api_v1.route('/read', methods=['GET'])
def read_users() -> Response:
    """
    :return: Response object with a message describing if all the users were found (if yes: add user objects) and the
    status code
    """
    users = []
    user_documents = user_collection.find()
    if user_documents:
        for user_document in user_documents:
            user = User(user_document=user_document)
            users.append(user.__dict__)
        return jsonify(
            data=users,
            message='Users found in the database.',
            status=200
        )
    return jsonify(
        message='No user found in the database.',
        status=500
    )


@user_api_v1.route('/update/id/<string:_id>', methods=['PUT'])
def update_user_by_id(_id: str) -> Response:
    """
    :param _id: User's id
    :return: Response object with a message describing if the user was found (if yes: update user) and the status code
    """
    user_document = request.json
    user = User(user_document=user_document)
    result = user_collection.update_one(
        {'_id': ObjectId(_id)},
        {'$set': user.__dict__}
    )
    if result.modified_count == 1:
        return jsonify(
            message='User updated in the database using the id.',
            status=200
        )
    return jsonify(
        message='User not updated in the database using the id.',
        status=500
    )


@user_api_v1.route('/delete/id/<string:_id>', methods=['DELETE'])
def delete_user_by_id(_id: str) -> Response:
    """
    :param _id: User's id
    :return: Response object with a message describing if the user was found (if yes: delete user) and the status code
    """
    result = user_collection.delete_one({'_id': ObjectId(_id)})
    if result.deleted_count == 1:
        return jsonify(
            message='User deleted from the database using the id.',
            status=200
        )
    return jsonify(
        message='User not deleted in the database using the id.',
        status=500
    )


sweep_api_v1.register_blueprint(user_api_v1)
