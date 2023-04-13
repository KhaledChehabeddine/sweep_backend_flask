"""Summary: Service Category Controller

A controller that assigns a child blueprint to sweep_api_v1 with routes for functions to create, read, update, and
delete service category items from the database
"""

import json
from bson import json_util
from flask import Blueprint, Response, jsonify, request
from pymongo.errors import OperationFailure
from app.database.database import get_database
from app.models.utilities.service_category import ServiceCategory
from app.routes.blueprints import sweep_api_v1

service_category_api_v1 = Blueprint('service_category_api_v1', __name__, url_prefix='/service_category')
service_category_collection = get_database()['service_categories']


@service_category_api_v1.route('/create', methods=['POST'])
def create_service_category() -> Response:
    """
    :return: Response object with a message describing if the service category was created and the status code
    """
    service_category_document = request.json
    service_category = ServiceCategory(service_category_document=service_category_document)
    try:
        service_category_collection.insert_one(service_category.__dict__)
    except OperationFailure:
        return jsonify({
            'message': 'Service category not added to the database.',
            'status': 500
        })
    return jsonify({
        'message': 'Service category added to the database.',
        'status': 200
    })


@service_category_api_v1.route('/read/<string:service_category_id>', methods=['GET'])
def read_service_category_by_id(service_category_id: str) -> Response:
    """
    :param service_category_id: Service Category's id
    :return: Response object with a message describing if the service categories were found (if yes: add user objects)
    and the status code
    """
    service_category_document = json.loads(json_util.dumps(service_category_collection.find_one(
        {'service_category_id': service_category_id})), object_hook=json_util.object_hook)
    if service_category_document:
        service_category = ServiceCategory(service_category_document=service_category_document)
        return jsonify({
            'message': 'Service category found in the database using the id.',
            'status': 200,
            'service_category': service_category.__dict__
        })
    return jsonify({
        'message': 'Service category not found in the database using the id.',
        'status': 404
    })


@service_category_api_v1.route('/read/<string:service_category_name>', methods=['GET'])
def read_service_category_by_name(service_category_name: str) -> Response:
    """
    :param service_category_name: Service Category's name
    :return: Response object with a message describing if the service categories were found (if yes: add user objects)
    and the status code
    """
    service_category_document = json.loads(json_util.dumps(service_category_collection.find_one(
        {'service_category_name': service_category_name})), object_hook=json_util.object_hook)
    if service_category_document:
        service_category = ServiceCategory(service_category_document=service_category_document)
        return jsonify({
            'message': 'Service category found in the database using the name.',
            'status': 200,
            'service_category': service_category.__dict__
        })
    return jsonify({
        'message': 'Service category not found in the database using the name.',
        'status': 404
    })


@service_category_api_v1.route('/read', methods=['GET'])
def read_service_categories() -> Response:
    """
    :return: Response object with a message describing if the service categories were found (if yes: add user objects)
    and the status code
    """
    service_categories = []
    service_category_documents = service_category_collection.find()
    if service_category_documents:
        for service_category_document in service_category_documents:
            service_category_document = json.loads(json_util.dumps(service_category_document),
                                                   object_hook=json_util.object_hook)
            service_item = ServiceCategory(service_category_document=service_category_document)
            service_categories.append(service_item.__dict__)
        return jsonify({
            'message': 'All categories found in the database.',
            'status': 200,
            'service_category': service_categories
        })
    return jsonify({
        'message': 'No categories not found in the database.',
        'status': 404
    })


@service_category_api_v1.route('/update/<string:service_category_id>', methods=['PUT'])
def update_service_category_by_id(service_category_id: str) -> Response:
    """
    :param service_category_id: Service Category's id
    :return: Response object with a message describing if the service category was updated and the status code
    """
    service_category_document = request.json
    service_category = ServiceCategory(service_category_document=service_category_document)
    try:
        service_category_collection.update_one({'service_item_id': service_category_id},
                                               {'$set': service_category.__dict__})
    except OperationFailure:
        return jsonify({
            'message': 'Service category not updated in the database.',
            'status': 500
        })
    return jsonify({
        'message': 'Service category updated in the database.',
        'status': 200
    })


@service_category_api_v1.route('/update/<string:service_category_name>', methods=['PUT'])
def update_service_category_by_name(service_category_name: str) -> Response:
    """
    :param service_category_name: Service Category's name
    :return: Response object with a message describing if the service category was updated and the status code
    """
    service_category_document = request.json
    service_category = ServiceCategory(service_category_document=service_category_document)
    try:
        service_category_collection.update_one({'service_item_name': service_category_name},
                                               {'$set': service_category.__dict__})
    except OperationFailure:
        return jsonify({
            'message': 'Service category not updated in the database.',
            'status': 500
        })
    return jsonify({
        'message': 'Service category not updated in the database.',
        'status': 200
    })


@service_category_api_v1.route('/delete/<string:service_category_id>', methods=['DELETE'])
def delete_service_category_by_id(service_category_id: str) -> Response:
    """
    :param service_category_id: Service Category's id
    :return: Response object with a message describing if the service category was deleted and the status code
    """
    try:
        service_category_collection.delete_one({'service_category_id': service_category_id})
    except OperationFailure:
        return jsonify({
            'message': 'Service category not deleted from the database.',
            'status': 500
        })
    return jsonify({
        'message': 'Service category deleted from the database.',
        'status': 200
    })


@service_category_api_v1.route('/delete/<string:service_category_name>', methods=['DELETE'])
def delete_service_category_by_name(service_category_name: str) -> Response:
    """
    :param service_category_name: Service Category's name
    :return: Response object with a message describing if the service category was deleted and the status code
    """
    try:
        service_category_collection.delete_one({'service_category_name': service_category_name})
    except OperationFailure:
        return jsonify({
            'message': 'Service category not deleted from the database.',
            'status': 500
        })
    return jsonify({
        'message': 'Service category deleted from the database.',
        'status': 200
    })


sweep_api_v1.register_blueprint(service_category_api_v1)
