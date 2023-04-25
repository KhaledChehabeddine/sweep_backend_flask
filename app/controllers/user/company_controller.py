"""Summary: Company Controller

A controller that assigns a child blueprint to sweep_api_v1 with routes for functions to create, read, update, and
delete companies from the database
"""
import pymongo
from bson import ObjectId
from flask import Blueprint, Response, jsonify, request
from pymongo.errors import OperationFailure
from app.aws.aws_cloudfront_client import create_cloudfront_url
from app.aws.aws_s3_client import upload_to_aws_s3, delete_from_aws_s3
from app.controllers.user.worker_controller import read_workers_by_company_id
from app.database.database import get_database
from app.functions.aws_s3_update import aws_s3_update
from app.functions.create_metadatas import create_service_provider_metadata, create_user_metadata
from app.functions.update_metadatas import update_user_metadata
from app.models.user.company import Company
from app.routes.blueprints import sweep_api_v1

company_api_v1 = Blueprint('company_api_v1', __name__, url_prefix='/company')
company_collection = get_database()['companies']

company_collection.create_index([('name', pymongo.ASCENDING)], unique=True)
company_collection.create_index([('user.email', pymongo.ASCENDING)], unique=True)
company_collection.create_index([('user.phone_number', pymongo.ASCENDING)], unique=True)
company_collection.create_index([('user.username', pymongo.ASCENDING)], unique=True)


def _configure_company(company_document: dict) -> Company:
    """
    :param company_document: A company document
    :return: A company object with the banner and logo image urls configured
    """
    worker = Company(company_document=company_document)
    worker.banner_image_url = create_cloudfront_url(file_path=worker.banner_file_path)
    worker.logo_image_url = create_cloudfront_url(file_path=worker.logo_file_path)
    return worker


@company_api_v1.route('/create', methods=['POST'])
def create_company() -> Response:
    """
    :return: Response object with a message describing if the company was created (if yes: add company id) and the
    status code
    """
    company_document = request.json

    company_document['metadata'] = {
        'number_of_employees': len(read_workers_by_company_id(company_id=company_document['_id']).json['data'])
    }

    company_document['service_provider']['metadata'] = \
        create_service_provider_metadata(service_provider_document=company_document['service_provider'])

    company_document['user']['metadata'] = create_user_metadata()

    upload_to_aws_s3(file_data=company_document['banner_image'], file_path=company_document['banner_file_path'])
    upload_to_aws_s3(file_data=company_document['logo_image'], file_path=company_document['logo_file_path'])

    try:
        company = Company(company_document=company_document)
        company_id = str(company_collection.insert_one(company.database_dict()).inserted_id)
    except (OperationFailure, TypeError):
        return jsonify(
            message='Company not added to the database.',
            status=500
        )
    return jsonify(
        data=company_id,
        message='Company added to the database.',
        status=200
    )


@company_api_v1.route('/read/id/<string:_id>', methods=['GET'])
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


@company_api_v1.route('/read', methods=['GET'])
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
        return jsonify(
            data=companies,
            message='All companies found in the database.',
            status=200
        )
    return jsonify(
        message='No company found in the database.',
        status=500
    )


@company_api_v1.route('/update/id/<string:_id>', methods=['PUT'])
def update_company_by_id(_id: str) -> Response:
    """
    :param _id: Company's id
    :return: Response object with a message describing if the company was updated and the status code
    """
    company_document = request.json

    company_document['metadata'] = {
        'number_of_employees': len(read_workers_by_company_id(company_id=company_document['_id']).json['data'])
    }

    company_document['service_provider']['metadata'] = \
        create_service_provider_metadata(service_provider_document=company_document['service_provider'])

    company_document['user']['metadata'] = \
        update_user_metadata(user_metadata_document=company_document['user']['metadata'])

    company_image_list = []
    if company_document['banner_image']:
        company_image_list.append((company_document['banner_file_path'], company_document['banner_image']))
    if company_document['logo_image']:
        company_image_list.append((company_document['logo_file_path'], company_document['logo_image']))
    aws_s3_update(object_image_list=company_image_list)

    company = Company(company_document=company_document)
    result = company_collection.update_one(
        {'_id': ObjectId(_id)},
        {'$set': company.database_dict()}
    )
    if len(company_image_list) > 0 or result.modified_count == 1:
        return jsonify(
            message='Company updated in the database using the id.',
            status=200
        )
    return jsonify(
        message='Company not updated in the database using the id.',
        status=500
    )


@company_api_v1.route('/delete/id/<string:_id>', methods=['DELETE'])
def delete_company_by_id(_id: str) -> Response:
    """
    :param _id: Company's id
    :return: Response object with a message describing if the company was deleted and the status code
    """
    company_document = read_company_by_id(_id=_id).json['data']

    delete_from_aws_s3(file_path=company_document['banner_file_path'])
    delete_from_aws_s3(file_path=company_document['logo_file_path'])

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


sweep_api_v1.register_blueprint(company_api_v1)
