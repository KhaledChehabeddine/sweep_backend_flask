"""Summary: User Controller CRUD Operations

A controller that assigns a child blueprint to sweep_api_v1 with routes for functions to create, read, update, and
delete users from the database
"""

import json
from bson import json_util
from flask import Blueprint, Response, jsonify, request
from pymongo.errors import OperationFailure
from app.database.database import get_database
from app.models.user.user import User
from app.routes.blueprints import sweep_api_v1

user_api_v1 = Blueprint('user_api_v1', __name__, url_prefix='/user')
user_collection = get_database()['users']


@user_api_v1.route('/create', methods=['POST'])
def create_user() -> Response:
    """
    :return: Response object with a message describing if the user was created and the status code
    """
    user_document = request.json
    user = User(user_document=user_document)
    try:
        user_collection.insert_one(user.__dict__)
    except OperationFailure:
        return jsonify({
            'message': 'User not added to the database.',
            'status': 500
        })
    return jsonify({
        'message': 'User added to the database.',
        'status': 200
    })


@user_api_v1.route('/read/<string:email>', methods=['GET'])
def read_user_by_email(email: str) -> Response:
    """
    :param email: User's email
    :return: Response object with a message describing if the user was found (if yes: add user object) and the status
    code
    """
    user_document = json.loads(json_util.dumps(user_collection.find_one({'email': email})),
                               object_hook=json_util.object_hook)
    if user_document:
        user = User(user_document=user_document)
        return jsonify({
            'message': 'User found in the database using the email.',
            'status': 200,
            'user': user.__dict__
        })
    return jsonify({
        'message': 'User not found in the database using the email.',
        'status': 404
    })


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
            user_document = json.loads(json_util.dumps(user_document), object_hook=json_util.object_hook)
            user = User(user_document=user_document)
            users.append(user.__dict__)
        return jsonify({
            'message': 'Users found in the database.',
            'status': 200,
            'users': users
        })
    return jsonify({
        'message': 'No user found in the database.',
        'status': 404
    })


@user_api_v1.route('/update/<string:email>', methods=['PUT'])
def update_user_by_email(email: str) -> Response:
    """
    :param email: User's email
    :return: Response object with a message describing if the user was found (if yes: update user) and the status code
    """
    user_document = request.json
    user = User(user_document=user_document)
    result = user_collection.update_one(
        {'email': email},
        {'$set': user.__dict__}
    )
    if result.modified_count == 1:
        return jsonify({
            'message': 'User updated in the database using the email.',
            'status': 200,
        })
    return jsonify({
        'message': 'User not found in the database using the email.',
        'status': 500,
    })


@user_api_v1.route('/delete/<string:email>', methods=['DELETE'])
def delete_user_by_email(email: str) -> Response:
    """
    :param email: User's email
    :return: Response object with a message describing if the user was found (if yes: delete user) and the status code
    """
    result = user_collection.delete_one({'email': email})
    if result.deleted_count == 1:
        return jsonify({
            'message': 'User deleted from the database using the email.',
            'status': 200
        })
    return jsonify({
        'message': 'User not found in the database using the email.',
        'status': 404
    })


sweep_api_v1.register_blueprint(user_api_v1)
