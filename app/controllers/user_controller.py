from app.database.database import get_database
from app.models.user import User
from app.routes.blueprints import sweep_api_v1
from flask import Blueprint, Response, jsonify, request
from pymongo.errors import OperationFailure

user_api_v1 = Blueprint('user_api_v1', __name__, url_prefix='/user')


@user_api_v1.route('/create', methods=['POST'])
def create_user() -> (Response, int):
    try:
        user = User(
            request.json['address'],
            request.json['country'],
            request.json['country_code'],
            request.json['email'],
            request.json['number'],
            request.json['password']
        )
        print(user.__dict__)
        result = get_database()['users'].insert_one(user.__dict__)
    except OperationFailure:
        return jsonify({'message': 'Could not add user to the database.'}), 500
    return jsonify(result), 200


@user_api_v1.route('/read/<email>', methods=['GET'])
def read_user_by_email(email: str) -> (Response, int):
    user = get_database().get_collection('users').find_one({'email': email})
    return jsonify(user), 200 if user else jsonify({'message': 'User not found using email.'}), 404


@user_api_v1.route('/update/<email>', methods=['PUT'])
def update_user(user: User) -> (Response, int):
    result = get_database().get_collection('users').update_one(
        {'email': user.get_email()},
        {'$set': user.__dict__}
    )
    return jsonify({'message': 'User successfully updated.'}), 200 if result.modified_count == 1 \
        else jsonify({'message': 'User not found using email.'}), 404


@user_api_v1.route('/delete/<email>', methods=['DELETE'])
def delete_user(email: str):
    result = get_database().get_collection('users').delete_one({'email': email})
    return jsonify({'message': 'User successfully deleted.'}), 200 if result.deleted_count == 1 \
        else jsonify({'message': 'User not found using email.'}), 500


sweep_api_v1.register_blueprint(user_api_v1)
