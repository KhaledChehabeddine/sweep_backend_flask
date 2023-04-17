"""Summary: Service item controller
A controller that assigns a child blueprint to sweep_api_v1 with routes for functions to create, read, update, and
delete service items from the database
"""

from bson import ObjectId
from flask import Blueprint, Response, jsonify, request
from pymongo.errors import OperationFailure
from app.aws.aws_cloudfront_client import create_cloudfront_url
from app.aws.aws_s3_client import upload_to_aws_s3, delete_from_aws_s3
from app.database.database import get_database
from app.functions.aws_update_operation_status import aws_update_operations
from app.models.utilities.service_item import ServiceItem
from app.routes.blueprints import sweep_api_v1

service_item_api_v1 = Blueprint('service_item_api_v1', __name__, url_prefix='/service_item')
service_item_collection = get_database()['service_items']


def _configure_service_item(service_item_document: dict) -> ServiceItem:
    """
    :param service_item_document: A dictionary representing a service item document
    :return: A service item object with the image url configured
    """
    service_item = ServiceItem(service_item_document=service_item_document)
    service_item.image_url = create_cloudfront_url(file_path=service_item.file_path)
    return service_item


@service_item_api_v1.route('/create', methods=['POST'])
def create_service_item() -> Response:
    """
    :return: Response object with a message describing if the service item was created and the status code
    """
    service_item_document = request.json

    upload_to_aws_s3(file_data=request.json['image'], file_path=request.json['file_path'])

    service_item = ServiceItem(service_item_document=service_item_document)
    try:
        service_item_collection.insert_one(service_item.database_dict())
    except OperationFailure:
        return jsonify(
            message='Service item not added to the database.',
            status=500
        )
    return jsonify(
        message='Service item added to the database.',
        status=200
    )


@service_item_api_v1.route('/read/id/_id>', methods=['GET'])
def read_service_item_by_id(_id: str) -> Response:
    """
    :param _id: Service item's id
    :return: Response object with a message describing if the service items were found (if yes: add user objects) and
    the status code
    """
    service_item_document = service_item_collection.find_one({'id': ObjectId(_id)})
    if service_item_document:
        service_item = _configure_service_item(service_item_document=service_item_document)
        return jsonify(
            data=service_item.__dict__,
            message='Service item found in the database using the id.',
            status=200,
        )
    return jsonify(
        message='Service item not found in the database using the id.',
        status=500
    )


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
            service_item = _configure_service_item(service_item_document=service_item_document)
            service_items.append(service_item.__dict__)
        return jsonify(
            data=service_items,
            message='All service items found in the database.',
            status=200,
        )
    return jsonify(
        message='No service item found in the database.',
        status=500
    )


@service_item_api_v1.route('/update/id/<string:_id>', methods=['PUT'])
def update_service_item_id(_id: str) -> Response:
    """
    :param _id: Service item's id
    :return: Response object with a message describing if the service item was updated and the status code
    """
    service_item_document = request.json

    aws_update_operations(object_document=service_item_document)

    service_item = ServiceItem(service_item_document=service_item_document)
    result = service_item_collection.update_one(
        {'_id': ObjectId(_id)},
        {'$set': service_item.database_dict()}
    )
    if request.json['image'] or result.modified_count == 1:
        return jsonify(
            message='Service item updated in the database.',
            status=200
        )
    return jsonify(
        message='Service item not updated in the database.',
        status=500
    )


@service_item_api_v1.route('/delete/<string:service_item_id>', methods=['DELETE'])
def delete_service_item_id(_id: str) -> Response:
    """
    :param _id: Service item's name
    :return: Response object with a message describing if the service item was deleted and the status code
    """
    service_item_document = read_service_item_by_id(_id=_id).json['data']

    delete_from_aws_s3(file_path=service_item_document['file_path'])

    result = service_item_collection.delete_one({'_id': ObjectId(_id)})
    if result.deleted_count == 1:
        return jsonify(
            message='Service item deleted from the database using the id.',
            status=200
        )
    return jsonify(
        message='Service item not deleted from the database using the id.',
        status=500
    )


sweep_api_v1.register_blueprint(service_item_api_v1)
