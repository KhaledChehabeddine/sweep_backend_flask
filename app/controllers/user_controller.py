from app.database.database import get_database
from app.models.user import User
from app.routes.blueprints import sweep_api_v1
from flask import Blueprint, Response, jsonify, request
from pymongo.errors import OperationFailure

user_api_v1 = Blueprint('user_api_v1', __name__, url_prefix='/user')
user_collection = get_database()['users']


@user_api_v1.route('/create', methods=['POST'])
def create_user() -> Response:
    user = User(
        address=request.json['address'],
        country=request.json['country'],
        country_code=request.json['country_code'],
        email=request.json['email'],
        number=request.json['number'],
        password=request.json['password']
    )
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
    user_document = user_collection.find_one({'email': email})
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


@user_api_v1.route('/update/<string:email>', methods=['PUT'])
def update_user(email: str) -> Response:
    if read_user_by_email(email).json['status'] == 200:
        user = User(
            address=request.json['address'],
            country=request.json['country'],
            country_code=request.json['country_code'],
            email=request.json['email'],
            number=request.json['number'],
            password=request.json['password']
        )
        result = user_collection.update_one(
            {'email': email},
            {'$set': user.__dict__}
        )
        if result.modified_count == 1:
            return jsonify({
                'message': 'User updated in the database using the email.',
                'status': 200,
                'user': user.__dict__
            })
    return jsonify({
        'message': 'User not found in the database using the email.',
        'status': 404
    })


@user_api_v1.route('/delete/<email>', methods=['DELETE'])
def delete_user(email: str) -> Response:
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
