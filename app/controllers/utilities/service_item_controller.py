"""Summary: Service item controller
A controller that assigns a child blueprint to sweep_api_v1 with routes for functions to create, read, update, and
delete service items from the database
"""

import json

import pymongo
from bson import json_util
from flask import Blueprint, Response, jsonify, request
from pymongo.errors import OperationFailure
from app.database.database import get_database
from app.models.utilities.service_item import ServiceItem
from app.routes.blueprints import sweep_api_v1

service_item_api_v1 = Blueprint('service_item_api_v1', __name__, url_prefix='/service_item')
service_item_collection = get_database()['service_items']

service_item_collection.create_index([('name', pymongo.ASCENDING)], unique=True)


@service_item_api_v1.route('/create', methods=['POST'])
def create_service_item() -> Response:
    """
    :return: Response object with a message describing if the service item was created and the status code
    """
    service_item_document = request.json
    service_item = ServiceItem(service_item_document=service_item_document)
    try:
        service_item_collection.insert_one(service_item.__dict__)
    except OperationFailure:
        return jsonify({
            'message': 'Service item not added to the database.',
            'status': 500
        })
    return jsonify({
        'message': 'Service item added to the database.',
        'status': 200
    })


@service_item_api_v1.route('/read/<string:service_item_id>', methods=['GET'])
def read_service_item_by_id(service_item_id: str) -> Response:
    """
    :param service_item_id: Service item's id
    :return: Response object with a message describing if the service items were found (if yes: add user objects) and
    the status code
    """
    service_item_document = json.loads(json_util.dumps(service_item_collection.find_one(
        {'service_item_id': service_item_id})),
        object_hook=json_util.object_hook)
    if service_item_document:
        service_item = ServiceItem(service_item_document=service_item_document)
        return jsonify({
            'message': 'Service item found in the database using the id.',
            'status': 200,
            'service_item': service_item.__dict__
        })
    return jsonify({
        'message': 'Service item not found in the database using the id.',
        'status': 404
    })


@service_item_api_v1.route('/read/<string:service_item_name>', methods=['GET'])
def read_service_item_by_name(service_item_name: str) -> Response:
    """
    :param service_item_name: Service item's name
    :return: Response object with a message describing if the service items were found (if yes: add user objects) and
    the status code
    """
    service_item_documents = json.loads(
        json_util.dumps(service_item_collection.find({'service_item_name': service_item_name})),
        object_hook=json_util.object_hook)
    if service_item_documents:
        service_items = []
        for service_item_document in service_item_documents:
            service_item = ServiceItem(service_item_document=service_item_document)
            service_items.append(service_item.__dict__)
        return jsonify({
            'message': 'Service items found in the database using the name.',
            'status': 200,
            'service_items': service_items
        })
    return jsonify({
        'message': 'Service items not found in the database using the name.',
        'status': 404
    })


@service_item_api_v1.route('/read', methods=['GET'])
def read_service_items() -> Response:
    """
    :return: Response object with a message describing if the service items were found (if yes: add user objects) and
    the status code
    """
    service_items = []
    service_item_documents = service_item_collection.find()
    if service_item_documents:
        for service_item_document in service_item_documents:
            service_item_document = json.loads(json_util.dumps(service_item_document),
                                               object_hook=json_util.object_hook)
            service_item = ServiceItem(service_item_document=service_item_document)
            service_items.append(service_item.__dict__)
        return jsonify({
            'message': 'All categories found in the database.',
            'status': 200,
            'service_item': service_items
        })
    return jsonify({
        'message': 'No categories not found in the database.',
        'status': 404
    })


@service_item_api_v1.route('/update/<string:service_item_id>', methods=['PUT'])
def update_service_item_id(service_item_id: str) -> Response:
    """
    :param service_item_id: Service item's id
    :return: Response object with a message describing if the service item was updated and the status code
    """
    service_item_document = request.json
    service_item = ServiceItem(service_item_document=service_item_document)
    try:
        service_item_collection.update_one({'service_item_id': service_item_id}, {'$set': service_item.__dict__})
    except OperationFailure:
        return jsonify({
            'message': 'Service item not updated in the database.',
            'status': 500
        })
    return jsonify({
        'message': 'Service item updated in the database.',
        'status': 200
    })


@service_item_api_v1.route('/update/<string:service_item_name>', methods=['PUT'])
def update_service_item_by_name(service_item_name: str) -> Response:
    """
    :param service_item_name: Service item's id
    :return: Response object with a message describing if the service item was updated and the status code
    """
    service_item_document = request.json
    service_item = ServiceItem(service_item_document=service_item_document)
    try:
        service_item_collection.update_one({'service_item_id': service_item_name}, {'$set': service_item.__dict__})
    except OperationFailure:
        return jsonify({
            'message': 'Service item not updated in the database.',
            'status': 500
        })
    return jsonify({
        'message': 'Service item updated in the database.',
        'status': 200
    })


@service_item_api_v1.route('/delete/<string:service_item_id>', methods=['DELETE'])
def delete_service_item_id(service_item_id: str) -> Response:
    """
    :param service_item_id: Service item's name
    :return: Response object with a message describing if the service item was deleted and the status code
    """
    try:
        service_item_collection.delete_one({'service_item_name': service_item_id})
    except OperationFailure:
        return jsonify({
            'message': 'Service item not deleted from the database.',
            'status': 500
        })
    return jsonify({
        'message': 'Service item deleted from the database.',
        'status': 200
    })


@service_item_api_v1.route('/delete/<string:service_item_name>', methods=['DELETE'])
def delete_service_item_name(service_item_name: str) -> Response:
    """
    :param service_item_name: Service item's name
    :return: Response object with a message describing if the service item was deleted and the status code
    """
    try:
        service_item_collection.delete_one({'service_item_name': service_item_name})
    except OperationFailure:
        return jsonify({
            'message': 'Service item not deleted from the database.',
            'status': 500
        })
    return jsonify({
        'message': 'Service item deleted from the database.',
        'status': 200
    })


sweep_api_v1.register_blueprint(service_item_api_v1)
