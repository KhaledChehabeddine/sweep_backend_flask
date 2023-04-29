"""Summary: Service Category Controller

A controller that assigns a child blueprint to sweep_api_v1 with routes for functions to create, read, update, and
delete service category items from the database
"""

import pymongo
from bson import ObjectId
from flask import Blueprint, Response, jsonify, request
from pymongo.errors import OperationFailure
from app.database.database import get_database
from app.models.components.service_category import ServiceCategory
from app.routes.blueprints import sweep_api_v1
from app.aws.aws_cloudfront_client import create_cloudfront_url
from app.aws.aws_s3_client import delete_image_from_aws_s3

service_category_api_v1 = Blueprint('service_category_api_v1', __name__, url_prefix='/service_category')
service_category_collection = get_database()['service_categories']

service_category_collection.create_index([('name', pymongo.ASCENDING)], unique=True)


def _configure_service_category(service_category_document: dict) -> ServiceCategory:
    """
    :param service_category_document: A dictionary representing a service category document
    :return: A service category object with the image url configured
    """
    service_category = ServiceCategory(service_category_document=service_category_document)
    service_category.image_url = create_cloudfront_url(file_path=service_category.file_path)
    return service_category


@service_category_api_v1.route('/create', methods=['POST'])
def create_service_category() -> Response:
    """
    :return: Response object with a message describing if the service category was created and the status code
    """
    service_category_document = request.json

    # upload_image_to_aws_s3(image_data=request.json['image'], image_path=request.json['file_path'])

    service_category = ServiceCategory(service_category_document=service_category_document)
    try:
        service_category_collection.insert_one(service_category.database_dict())
    except OperationFailure:
        return jsonify(
            message='Service category not added to the database.',
            status=500
        )
    return jsonify(
        message='Service category added to the database.',
        status=200
    )


@service_category_api_v1.route('/read/id/<string:_id>', methods=['GET'])
def read_service_category_by_id(_id: str) -> Response:
    """
    :param _id: Service Category's id
    :return: Response object with a message describing if the service categories were found (if yes: add user objects)
    and the status code
    """
    service_category_document = service_category_collection.find_one({'_id': ObjectId(_id)})
    if service_category_document:
        service_category = _configure_service_category(service_category_document=service_category_document)
        return jsonify(
            data=service_category.__dict__,
            message='Service category found in the database using the id.',
            status=200,
        )
    return jsonify(
        message='Service category not found in the database using the id.',
        status=500
    )


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
            service_category = _configure_service_category(service_category_document=service_category_document)
            service_categories.append(service_category.__dict__)
        return jsonify(
            data=service_categories,
            message='All service categories found in the database.',
            status=200,
        )
    return jsonify(
        message='No service category found in the database.',
        status=500
    )


@service_category_api_v1.route('/update/id/<string:_id>', methods=['PUT'])
def update_service_category_by_id(_id: str) -> Response:
    """
    :param _id: Service Category's id
    :return: Response object with a message describing if the service category was updated and the status code
    """
    service_category_document = request.json

    # aws_update_operations(object_document=service_category_document)

    service_category = ServiceCategory(service_category_document=service_category_document)
    result = service_category_collection.update_one(
        {'_id': ObjectId(_id)},
        {'$set': service_category.database_dict()}
    )
    if service_category_document['image'] or result.modified_count == 1:
        return jsonify(
            message='Service category updated in the database using id.',
            status=200
        )
    return jsonify(
        message='Service category not updated in the database using id.',
        status=500
    )


@service_category_api_v1.route('/delete/id/<string:_id>', methods=['DELETE'])
def delete_service_category_by_id(_id: str) -> Response:
    """
    :param _id: Service Category's id
    :return: Response object with a message describing if the service category was deleted and the status code
    """
    service_category_document = read_service_category_by_id(_id=_id).json['data']

    delete_image_from_aws_s3(image_path=service_category_document['file_path'])

    result = service_category_collection.delete_one({'_id': ObjectId(_id)})
    if result.deleted_count == 1:
        return jsonify(
            message='Service category item deleted from the database using the id.',
            status=200
        )
    return jsonify(
        message='Service category item not deleted from the database using the id.',
        status=500
    )


sweep_api_v1.register_blueprint(service_category_api_v1)
