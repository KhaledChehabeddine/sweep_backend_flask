"""Summary: Worker Controller

A controller that assigns a child blueprint to sweep_api_v1 with routes for functions to create, read, update, and
delete workers from the database
"""
import pymongo
from bson import ObjectId
from flask import Blueprint, Response, jsonify, request
from pymongo.errors import OperationFailure
from app.aws.aws_cloudfront_client import create_cloudfront_url
from app.aws.aws_s3_client import upload_to_aws_s3, delete_from_aws_s3
from app.database.database import get_database
from app.functions.aws_s3_update import aws_s3_update
from app.functions.create_metadatas import create_service_provider_metadata, create_user_metadata
from app.functions.update_metadatas import update_user_metadata
from app.models.user.worker import Worker
from app.routes.blueprints import sweep_api_v1

worker_api_v1 = Blueprint('worker_api_v1', __name__, url_prefix='/worker')
worker_collection = get_database()['workers']

worker_collection.create_index([('user.email', pymongo.ASCENDING)], unique=True)
worker_collection.create_index([('user.phone_number', pymongo.ASCENDING)], unique=True)
worker_collection.create_index([('user.username', pymongo.ASCENDING)], unique=True)


def _configure_worker(worker_document: dict) -> Worker:
    """
    :param worker_document: A worker document
    :return: A worker object with the banner and profile image urls configured
    """
    worker = Worker(worker_document=worker_document)
    worker.banner_image_url = create_cloudfront_url(file_path=worker.banner_file_path)
    worker.profile_image_url = create_cloudfront_url(file_path=worker.profile_file_path)
    return worker


@worker_api_v1.route('/create', methods=['POST'])
def create_worker() -> Response:
    """
    :return: Response object with a message describing if the worker was created (if yes: add worker id) and the status
    code
    """
    worker_document = request.json

    worker_document['metadata'] = {
        'formatted_name': (
                worker_document['first_name'] + ' ' + worker_document['middle_name'] + ' ' +
                worker_document['last_name']
        )
    }

    worker_document['service_provider']['metadata'] = \
        create_service_provider_metadata(service_provider_document=worker_document['service_provider'])

    worker_document['user']['metadata'] = create_user_metadata()

    upload_to_aws_s3(file_data=worker_document['banner_image'], file_path=worker_document['banner_file_path'])
    upload_to_aws_s3(file_data=worker_document['profile_image'], file_path=worker_document['profile_file_path'])

    try:
        worker = Worker(worker_document=worker_document)
        worker_id = str(worker_collection.insert_one(worker.database_dict()).inserted_id)
    except (OperationFailure, TypeError):
        return jsonify(
            message='Worker not added to the database.',
            status=500
        )
    return jsonify(
        data=worker_id,
        message='Worker added to the database.',
        status=200
    )


@worker_api_v1.route('/read/id/<string:_id>', methods=['GET'])
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


@worker_api_v1.route('/read/company_id/<string:company_id>', methods=['GET'])
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
            message='All workers found in the database.',
            status=200,
        )
    return jsonify(
        message='No worker found in the database.',
        status=500
    )


@worker_api_v1.route('/read', methods=['GET'])
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
        return jsonify(
            data=workers,
            message='All workers found in the database.',
            status=200,
        )
    return jsonify(
        message='No worker found in the database.',
        status=500
    )


@worker_api_v1.route('/update/id/<string:_id>', methods=['PUT'])
def update_worker_by_id(_id: str) -> Response:
    """
    :param _id: Worker's id
    :return: Response object with a message describing if the worker was updated and the status
    code
    """
    worker_document = request.json

    worker_document['metadata'] = {
        'formatted_name': (
                worker_document['first_name'] + ' ' + worker_document['middle_name'] + ' ' +
                worker_document['last_name']
        )
    }

    worker_document['service_provider']['metadata'] = \
        create_service_provider_metadata(service_provider_document=worker_document['service_provider'])

    worker_document['user']['metadata'] = \
        update_user_metadata(user_metadata_document=worker_document['user']['metadata'])

    worker_image_list = []
    if worker_document['banner_image']:
        worker_image_list.append((worker_document['banner_file_path'], worker_document['banner_image']))
    if worker_document['profile_image']:
        worker_image_list.append((worker_document['profile_file_path'], worker_document['profile_image']))
    aws_s3_update(object_image_list=worker_image_list)

    worker = Worker(worker_document=worker_document)
    result = worker_collection.update_one(
        {'_id': ObjectId(_id)},
        {'$set': worker.database_dict()}
    )
    if len(worker_image_list) > 0 or result.modified_count == 1:
        return jsonify(
            message='Worker updated in the database using the id.',
            status=200
        )
    return jsonify(
        message='Worker not updated in the database using the id.',
        status=500
    )


@worker_api_v1.route('/delete/id/<string:_id>', methods=['DELETE'])
def delete_worker_by_id(_id: str) -> Response:
    """
    :param _id: Worker's id
    :return: Response object with a message describing if the worker was deleted and the status code
    """
    worker_document = read_worker_by_id(_id=_id).json['data']

    delete_from_aws_s3(file_path=worker_document['banner_file_path'])
    delete_from_aws_s3(file_path=worker_document['profile_file_path'])

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


sweep_api_v1.register_blueprint(worker_api_v1)
