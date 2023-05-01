"""Summary: Service Category Controller

A controller that assigns a child blueprint to sweep_api_v1 with routes for functions to create, read, update, and
delete service category items from the database
"""
from bson import ObjectId
from flask import Blueprint, Response, jsonify, request
from pymongo import ASCENDING, errors
from app.database.database import get_database
from app.functions.create_object_metadatas import create_service_category_metadata
from app.functions.update_object_metadatas import update_service_category_metadata
from app.models.components.service_category import ServiceCategory
from app.aws.aws_s3_client import delete_image_from_aws_s3

raw_service_category_api_v1 = Blueprint('service_category_api_v1', __name__, url_prefix='/service_category')
service_category_collection = get_database()['service_categories']

service_category_collection.create_index([('name', ASCENDING)], unique=True)


@raw_service_category_api_v1.route('/create', methods=['POST'])
def create_service_category() -> Response:
    """
    :return: Response object with a message describing if the service category was created (if yes: add service category
    id) and the status code
    """
    service_category_document = request.json

    service_category_document['metadata'] = \
        create_service_category_metadata(service_category_document=service_category_document)

    service_category = ServiceCategory(service_category_document=service_category_document)
    try:
        service_category_id = str(service_category_collection.insert_one(service_category.database_dict()).inserted_id)
    except errors.OperationFailure:
        return jsonify(
            message='Service category not added to the database.',
            status=500
        )
    return jsonify(
        data=service_category_id,
        message='Service category added to the database.',
        status=200
    )


@raw_service_category_api_v1.route('/read/id/<string:_id>', methods=['GET'])
def read_service_category_by_id(_id: str) -> Response:
    """
    :param _id: Service Category's id
    :return: Response object with a message describing if the service categories were found (if yes: add user objects)
    and the status code
    """
    service_category_document = service_category_collection.find_one({'_id': ObjectId(_id)})
    if service_category_document:
        service_category = ServiceCategory(service_category_document=service_category_document)
        return jsonify(
            data=service_category.__dict__,
            message='Service category found in the database using the id.',
            status=200,
        )
    return jsonify(
        message='Service category not found in the database using the id.',
        status=500
    )


@raw_service_category_api_v1.route('/read', methods=['GET'])
def read_service_categories() -> Response:
    """
    :return: Response object with a message describing if the service categories were found (if yes: add user objects)
    and the status code
    """
    service_categories = []
    service_category_documents = service_category_collection.find()
    if service_category_documents:
        for service_category_document in service_category_documents:
            service_category = ServiceCategory(service_category_document=service_category_document)
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


@raw_service_category_api_v1.route('/update/id/<string:_id>', methods=['PUT'])
def update_service_category_by_id(_id: str) -> Response:
    """
    :param _id: Service Category's id
    :return: Response object with a message describing if the service category was updated and the status code
    """
    service_category_document = request.json

    service_category_document['metadata'] = \
        update_service_category_metadata(service_category_document=service_category_document)

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


@raw_service_category_api_v1.route('/delete/id/<string:_id>', methods=['DELETE'])
def delete_service_category_by_id(_id: str) -> Response:
    """
    :param _id: Service Category's id
    :return: Response object with a message describing if the service category was deleted and the status code
    """
    service_category_document = read_service_category_by_id(_id=_id).json['data']

    delete_image_from_aws_s3(image_path=service_category_document['image_path'])

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


service_category_api_v1 = raw_service_category_api_v1
