from flask import jsonify, Response
from flask_cors import CORS
from pymongo.errors import OperationFailure
from app.database.database import mongodb_client
from app.models.user import User
from app.routes.blueprints import sweep_api_v1, user_api_v1


@user_api_v1.route(rule='/create', methods=['POST'])
def create_user(user: User) -> (Response, int):
    try:
        result = mongodb_client.users.insert_one(user.convert_to_document())
    except OperationFailure:
        return jsonify({'message': 'Could not add user to the database.'}), 500
    return jsonify(result), 200


@user_api_v1.route(rule='/read/<email>', methods=['GET'])
def read_user_by_email(email: str) -> (Response, int):
    user = mongodb_client.users.find_one({
        'email': email
    })
    return jsonify(user), 200 if user else jsonify({'message': 'User not found using email.'}), 404


@user_api_v1.route(rule='/update/<email>', methods=['PUT'])
def update_user(user: User) -> (Response, int):
    result = mongodb_client.users.update_one(
        {'email': user.get_email()},
        {'$set': user.convert_to_document()}
    )
    return jsonify({'message': 'User successfully updated.'}), 200 if result.modified_count == 1 \
        else jsonify({'message': 'User not found using email.'}), 404


@user_api_v1.route(rule='/delete/<email>', methods=['DELETE'])
def delete_user(email: str):
    result = mongodb_client.users.delete_one({'email': email})
    return jsonify({'message': 'User successfully deleted.'}), 200 if result.deleted_count == 1 \
        else jsonify({'message': 'User not found using email.'}), 500
