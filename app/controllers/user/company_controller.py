"""Summary: Company Controller

A controller that assigns a child blueprint to sweep_api_v1 with routes for functions to create, read, update, and
delete companies from the database
"""
from typing import Any
from bson import ObjectId
from flask import Blueprint, Response, jsonify, request
from pymongo import ASCENDING, errors
from app.aws.aws_s3_client import upload_images_to_aws_s3, delete_images_from_aws_s3
from app.controllers.user.worker_controller import read_workers_by_company_id
from app.database.database import get_database
from app.functions.create_mongodb_indices import create_service_provider_indexes
from app.functions.create_object_metadata import create_service_provider_metadata
from app.functions.update_object_metadata import update_service_provider_metadata
from app.models.user.company import Company

raw_company_api_v1 = Blueprint('company_api_v1', __name__, url_prefix='/company')
company_collection = get_database()['companies']

company_collection.create_index([('name', ASCENDING)], unique=True)
create_service_provider_indexes(service_provider_collection=company_collection)


def _configure_company(company_document: dict) -> Company:
    """
    :param company_document: A company document
    :return: A company object with configured ids
    """
    company = Company(company_document=company_document)

    for category_document in company.service_provider['categories']:
        category_document['_id'] = str(category_document['_id'])

    for review_document in company.service_provider['reviews']:
        review_document['_id'] = str(review_document['_id'])

    return company


def _configure_company_document(company_document: dict, company_images: list[tuple[str, Any, Any]]) -> dict:
    """
    :param company_document: A company document
    :param company_images: A list of tuples of each image info in the format [type, data, path]
    :return: A company document with a configured metadata
    """
    company_document['metadata'] = upload_images_to_aws_s3(
        object_metadata_document=company_document['metadata'],
        object_images=company_images
    ).json['data']
    company_document['metadata']['total_employees'] = (
        0 if company_document['_id'] == "-1"
        else len(read_workers_by_company_id(company_id=company_document['_id']).json['data'])
    )
    company_document['metadata']['total_service_categories'] = len(company_document['service_category_ids'])

    return company_document


@raw_company_api_v1.route('/create', methods=['POST'])
def create_company() -> Response:
    """
    :return: Response object with a message describing if the company was created (if yes: add company id) and the
    status code
    """
    company_document = request.json

    company_images = [
        ('banner_', company_document['banner_image'], company_document['banner_image_path']),
        ('logo_', company_document['logo_image'], company_document['logo_image_path'])
    ]
    company_document = _configure_company_document(company_document=company_document, company_images=company_images)

    company_document['service_provider'] = \
        create_service_provider_metadata(service_provider_document=company_document['service_provider'])

    company = Company(company_document=company_document)
    try:
        company_id = str(company_collection.insert_one(company.database_dict()).inserted_id)
    except errors.OperationFailure:
        return jsonify(
            message='Company not added to the database.',
            status=500
        )
    return jsonify(
        data=company_id,
        message='Company added to the database.',
        status=200
    )


@raw_company_api_v1.route('/read/id/<string:_id>', methods=['GET'])
def read_company_by_id(_id: str) -> Response:
    """
    :param _id: Company's id
    :return: Response object with a message describing if the company was found (if yes: add company) and the status
    code
    """
    company_document = company_collection.find_one({'_id': ObjectId(_id)})
    if company_document:
        company = _configure_company(company_document=company_document)
        return jsonify(
            data=company.__dict__,
            message='Company found in the database using the id.',
            status=200
        )
    return jsonify(
        message='Company not found in the database using the id.',
        status=500
    )


@raw_company_api_v1.route('/read/all', methods=['GET'])
def read_companies() -> Response:
    """
    :return: Response object with a message describing if all the companies were found (if yes: add companies) and the
    status code
    """
    companies = []
    company_documents = company_collection.find()
    if company_documents:
        for company_document in company_documents:
            company = _configure_company(company_document=company_document)
            companies.append(company.__dict__)
        if companies:
            return jsonify(
                data=companies,
                message='All companies found in the database.',
                status=200
            )
    return jsonify(
        message='No company found in the database.',
        status=500
    )


@raw_company_api_v1.route('/update/id/<string:_id>', methods=['PUT'])
def update_company_by_id(_id: str) -> Response:
    """
    :param _id: Company's id
    :return: Response object with a message describing if the company was updated and the status code
    """
    company_document = request.json

    company_images = []
    if company_document['banner_image']:
        company_images.append(('banner_', company_document['banner_image_path'], company_document['banner_image']))
    if company_document['logo_image']:
        company_images.append(('logo_', company_document['logo_image_path'], company_document['logo_image']))
    company_document = _configure_company_document(company_document=company_document, company_images=company_images)

    company_document['service_provider'] = \
        update_service_provider_metadata(service_provider_document=company_document['service_provider'])

    company = Company(company_document=company_document)
    result = company_collection.update_one(
        {'_id': ObjectId(_id)},
        {'$set': company.database_dict()}
    )
    if len(company_images) > 0 or result.modified_count == 1:
        return jsonify(
            message='Company updated in the database using the id.',
            status=200
        )
    return jsonify(
        message='Company not updated in the database using the id.',
        status=500
    )


@raw_company_api_v1.route('/delete/id/<string:_id>', methods=['DELETE'])
def delete_company_by_id(_id: str) -> Response:
    """
    :param _id: Company's id
    :return: Response object with a message describing if the company was deleted and the status code
    """
    company_document = read_company_by_id(_id=_id).json['data']

    image_paths = [company_document['banner_image_path'], company_document['logo_image_path']]
    delete_images_from_aws_s3(image_paths=image_paths)

    result = company_collection.delete_one({'_id': ObjectId(_id)})
    if result.deleted_count == 1:
        return jsonify(
            message='Company deleted from the database using the id.',
            status=200
        )
    return jsonify(
        message='Company not deleted from the database using the id.',
        status=500
    )


company_api_v1 = raw_company_api_v1
