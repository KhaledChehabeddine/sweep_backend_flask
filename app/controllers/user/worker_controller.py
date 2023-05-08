"""Summary: Worker Controller

A controller that assigns a child blueprint to sweep_api_v1 with routes for functions to create, read, update, and
delete workers from the database
"""
from typing import Any
from bson import ObjectId
from flask import Blueprint, Response, jsonify, request
from pymongo import errors
from app.aws.aws_s3_client import upload_images_to_aws_s3, delete_images_from_aws_s3
from app.database.database import get_database
from app.functions.create_mongodb_indices import create_service_provider_indexes
from app.functions.create_object_metadata import create_service_provider_metadata
from app.functions.update_object_metadata import update_service_provider_metadata
from app.models.user.worker import Worker

raw_worker_api_v1 = Blueprint('worker_api_v1', __name__, url_prefix='/worker')
worker_collection = get_database()['workers']

create_service_provider_indexes(service_provider_collection=worker_collection)


def _configure_worker(worker_document: dict) -> Worker:
    """
    :param worker_document: A worker document
    :return: A worker object with configured ids
    """
    worker = Worker(worker_document=worker_document)

    for category_document in worker.service_provider['categories']:
        category_document['_id'] = str(category_document['_id'])

    for review_document in worker.service_provider['reviews']:
        review_document['_id'] = str(review_document['_id'])

    return worker


def _configure_worker_document(worker_document: dict, worker_images: list[tuple[str, Any, Any]]) -> dict:
    """
    :param worker_document: A worker document
    :param worker_images: A list of tuples of each image info in the format [type, data, path]
    :return: A worker document with a configured metadata
    """
    worker_document['metadata'] = upload_images_to_aws_s3(
        object_metadata_document=worker_document['metadata'],
        object_images=worker_images
    ).json['data']
    worker_document['metadata']['formatted_name'] = (
            worker_document['first_name'] + ' ' + worker_document['middle_name'] + ' ' + worker_document['last_name']
    )

    return worker_document


@raw_worker_api_v1.route('/create', methods=['POST'])
def create_worker() -> Response:
    """
    :return: Response object with a message describing if the worker was created (if yes: add worker id) and the status
    code
    """
    worker_document = request.json

    worker_images = [
        ('banner_', worker_document['banner_image'], worker_document['banner_image_path']),
        ('profile_', worker_document['profile_image'], worker_document['profile_image_path'])
    ]
    worker_document = _configure_worker_document(worker_document=worker_document, worker_images=worker_images)

    worker_document['service_provider'] = \
        create_service_provider_metadata(service_provider_document=worker_document['service_provider'])

    worker = Worker(worker_document=worker_document)
    try:
        worker_id = str(worker_collection.insert_one(worker.database_dict()).inserted_id)
    except errors.OperationFailure:
        return jsonify(
            message='Worker not added to the database.',
            status=500
        )
    return jsonify(
        data=worker_id,
        message='Worker added to the database.',
        status=200
    )


@raw_worker_api_v1.route('/read/id/<string:_id>', methods=['GET'])
def read_worker_by_id(_id: str) -> Response:
    """
    :param _id: Worker's id
    :return: Response object with a message describing if the worker was found (if yes: add worker) and the status code
    """
    worker_document = worker_collection.find_one({'_id': ObjectId(_id)})
    if worker_document:
        worker = _configure_worker(worker_document=worker_document)
        return jsonify(
            data=worker.__dict__,
            message='Worker found in the database using the id.',
            status=200,
        )
    return jsonify(
        message='Worker not found in the database using the id.',
        status=500
    )


@raw_worker_api_v1.route('/read/company_id/<string:company_id>', methods=['GET'])
def read_workers_by_company_id(company_id: str) -> Response:
    """
    :param company_id: Worker's company id
    :return: Response object with a message describing if the workers were found (if yes: add workers) and the status
    code
    """
    workers = []
    worker_documents = worker_collection.find({'company_id': company_id})
    if worker_documents:
        for worker_document in worker_documents:
            worker = _configure_worker(worker_document=worker_document)
            workers.append(worker.__dict__)
        return jsonify(
            data=workers,
            message='All workers with the company id found in the database.',
            status=200,
        )
    return jsonify(
        message='No worker with the company id found in the database.',
        status=500
    )


@raw_worker_api_v1.route('/read/all', methods=['GET'])
def read_workers() -> Response:
    """
    :return: Response object with a message describing if the workers were found (if yes: add workers) and the status
    code
    """
    workers = []
    worker_documents = worker_collection.find()
    if worker_documents:
        for worker_document in worker_documents:
            worker = _configure_worker(worker_document=worker_document)
            workers.append(worker.__dict__)
        if workers:
            return jsonify(
                data=workers,
                message='All workers found in the database.',
                status=200,
            )
    return jsonify(
        message='No worker found in the database.',
        status=500
    )


@raw_worker_api_v1.route('/update/id/<string:_id>', methods=['PUT'])
def update_worker_by_id(_id: str) -> Response:
    """
    :param _id: Worker's id
    :return: Response object with a message describing if the worker was updated and the status
    code
    """
    worker_document = request.json

    worker_images = []
    if worker_document['banner_image']:
        worker_images.append(('banner_', worker_document['banner_image_path'], worker_document['banner_image']))
    if worker_document['profile_image']:
        worker_images.append(('profile_', worker_document['profile_image_path'], worker_document['profile_image']))
    worker_document = _configure_worker_document(worker_document=worker_document, worker_images=worker_images)

    worker_document['service_provider'] = \
        update_service_provider_metadata(service_provider_document=worker_document['service_provider'])

    worker = Worker(worker_document=worker_document)
    result = worker_collection.update_one(
        {'_id': ObjectId(_id)},
        {'$set': worker.database_dict()}
    )
    if len(worker_images) > 0 or result.modified_count == 1:
        return jsonify(
            message='Worker updated in the database using the id.',
            status=200
        )
    return jsonify(
        message='Worker not updated in the database using the id.',
        status=500
    )


@raw_worker_api_v1.route('/delete/id/<string:_id>', methods=['DELETE'])
def delete_worker_by_id(_id: str) -> Response:
    """
    :param _id: Worker's id
    :return: Response object with a message describing if the worker was deleted and the status code
    """
    worker_document = read_worker_by_id(_id=_id).json['data']

    image_paths = [worker_document['banner_image_path'], worker_document['profile_image_path']]
    delete_images_from_aws_s3(image_paths=image_paths)

    result = worker_collection.delete_one({'_id': ObjectId(_id)})
    if result.deleted_count == 1:
        return jsonify(
            message='Worker deleted from the database using the id.',
            status=200
        )
    return jsonify(
        message='Worker not deleted from the database using the id.',
        status=500
    )


worker_api_v1 = raw_worker_api_v1
