from flask import jsonify, Response
from flask_cors import CORS
from pymongo.errors import OperationFailure
from app.database.database import get_mongodb_client
from app.models.user import User

user_api_v1 = Blueprint('user_api_v1', __name__, url_prefix='/user')


@user_api_v1.route('/create', methods=['POST'])
def create_user() -> (Response, int):
    try:
        user = User(
            request.form.get('address'),
            request.form.get('country'),
            request.form.get('country_code'),
            request.form.get('email'),
            request.form.get('number'),
            request.form.get('password')
        )
        result = get_mongodb_client().users.insert_one(user.convert_to_document())
    except OperationFailure:
        return jsonify({'message': 'Could not add user to the database.'}), 500
    return jsonify(result), 200


@user_api_v1.route('/read/<email>', methods=['GET'])
def read_user_by_email(email: str) -> (Response, int):
    user = get_mongodb_client().users.find_one({
        'email': email
    })
    return jsonify(user), 200 if user else jsonify({'message': 'User not found using email.'}), 404


@user_api_v1.route('/update/<email>', methods=['PUT'])
def update_user(user: User) -> (Response, int):
    result = get_mongodb_client().users.update_one(
        {'email': user.get_email()},
        {'$set': user.convert_to_document()}
    )
    return jsonify({'message': 'User successfully updated.'}), 200 if result.modified_count == 1 \
        else jsonify({'message': 'User not found using email.'}), 404


@user_api_v1.route('/delete/<email>', methods=['DELETE'])
def delete_user(email: str):
    result = get_mongodb_client().users.delete_one({'email': email})
    return jsonify({'message': 'User successfully deleted.'}), 200 if result.deleted_count == 1 \
        else jsonify({'message': 'User not found using email.'}), 500
