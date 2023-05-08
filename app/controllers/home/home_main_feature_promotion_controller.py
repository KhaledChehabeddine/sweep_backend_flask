"""Summary: Home Main Feature Promotion Controller

A controller that assigns a child blueprint to sweep_api_v1 with routes for functions to create, read, update, and
delete home main feature promotions from the database
"""
from bson import ObjectId
from flask import Blueprint, Response, jsonify, request
from pymongo.errors import OperationFailure
from app.database.database import get_database
from app.functions.create_object_metadata import create_home_feature_metadata, create_home_main_feature_metadata
from app.functions.update_object_metadata import update_home_feature_metadata
from app.models.home.home_main_feature_promotion import HomeMainFeaturePromotion
from app.aws.aws_s3_client import delete_image_from_aws_s3

raw_home_main_feature_promotion_api_v1 = Blueprint(
    'home_main_feature_promotion_api_v1',
    __name__,
    url_prefix='/home_main_feature_promotion'
)
home_main_feature_promotion_collection = get_database()['home_main_feature_promotions']


def _configure_home_main_feature_promotion(home_main_feature_promotion_document: dict, ) -> dict:
    """
    :param home_main_feature_promotion_document: A home main feature promotion document
    :return: A home main feature promotion document with configured metadata
    """
    home_main_feature_promotion_document['metadata']['total_companies'] = len(
        home_main_feature_promotion_document['company_ids']
    )
    home_main_feature_promotion_document['metadata']['total_service_providers'] = len(
        home_main_feature_promotion_document['company_ids'] + home_main_feature_promotion_document['worker_ids']
    )
    home_main_feature_promotion_document['metadata']['total_workers'] = len(
        home_main_feature_promotion_document['worker_ids']
    )

    home_main_feature_promotion_document['home_main_feature'] = create_home_main_feature_metadata(
        home_main_feature_document=home_main_feature_promotion_document['home_main_feature']
    )

    return home_main_feature_promotion_document


@raw_home_main_feature_promotion_api_v1.route('/create', methods=['POST'])
def create_home_main_feature_promotion() -> Response:
    """
    :return: Response object with a message describing if the home main feature promotion was created (if yes: add home
    main feature promotion id) and the status code
    """
    home_main_feature_promotion_document = request.json

    home_main_feature_promotion_document = _configure_home_main_feature_promotion(
        home_main_feature_promotion_document=home_main_feature_promotion_document
    )

    home_main_feature_promotion_document['home_main_feature']['home_feature']['metadata'] = \
        create_home_feature_metadata()

    home_main_feature_promotion = HomeMainFeaturePromotion(
        home_main_feature_promotion_document=home_main_feature_promotion_document
    )
    try:
        home_main_feature_promotion_id = str(
            home_main_feature_promotion_collection.insert_one(home_main_feature_promotion.database_dict()).inserted_id
        )
    except OperationFailure:
        return jsonify(
            message='Home main feature promotion not added to the database.',
            status=500
        )
    return jsonify(
        data=home_main_feature_promotion_id,
        message='Home main feature promotion added to the database.',
        status=200
    )


@raw_home_main_feature_promotion_api_v1.route('/read/id/<string:_id>', methods=['GET'])
def read_home_main_feature_promotion_by_id(_id: str) -> Response:
    """
    :param _id: Home main feature promotion's id
    :return: Response object with a message describing if the home main feature promotion was found (if yes: add home
    main feature promotion) and the status code
    """
    home_main_feature_promotion_document = home_main_feature_promotion_collection.find_one({'_id': ObjectId(_id)})
    if home_main_feature_promotion_document:
        home_main_feature_promotion = HomeMainFeaturePromotion(
            home_main_feature_promotion_document=home_main_feature_promotion_document
        )
        return jsonify(
            data=home_main_feature_promotion.__dict__,
            message='Home main feature promotion found in the database using the id.',
            status=200
        )
    return jsonify(
        message='Home main feature promotion not found in the database using the id.',
        status=500
    )


@raw_home_main_feature_promotion_api_v1.route('/read/all', methods=['GET'])
def read_home_main_feature_promotions() -> Response:
    """
    :return: Response object with a message describing if all the home main feature promotions were found (if yes: add
    home main feature promotions) and the status code
    """
    home_main_feature_promotions = []
    home_main_feature_promotion_documents = home_main_feature_promotion_collection.find()
    if home_main_feature_promotion_documents:
        for home_main_feature_promotion_document in home_main_feature_promotion_documents:
            home_main_feature_promotion = HomeMainFeaturePromotion(
                home_main_feature_promotion_document=home_main_feature_promotion_document
            )
            home_main_feature_promotions.append(home_main_feature_promotion.__dict__)
        if home_main_feature_promotions:
            return jsonify(
                data=home_main_feature_promotions,
                message='All home main feature promotions found in the database.',
                status=200
            )
    return jsonify(
        message='No home main feature promotion found in the database.',
        status=500
    )


@raw_home_main_feature_promotion_api_v1.route('/update/id/<string:_id>', methods=['PUT'])
def update_home_main_feature_promotion_by_id(_id: str) -> Response:
    """
    :param _id: Home main feature promotion's id
    :return: Response object with a message describing if the home main feature promotion was found (if yes: update
    home main feature promotion) and the status code
    """
    home_main_feature_promotion_document = request.json

    home_main_feature_promotion_document = _configure_home_main_feature_promotion(
        home_main_feature_promotion_document=home_main_feature_promotion_document
    )

    home_main_feature_promotion_document['home_main_feature']['home_feature']['metadata'] = \
        update_home_feature_metadata(
            home_feature_metadata_document=home_main_feature_promotion_document
            ['home_main_feature']['home_feature']['metadata']
        )

    home_main_feature_promotion = \
        HomeMainFeaturePromotion(home_main_feature_promotion_document=home_main_feature_promotion_document)
    result = home_main_feature_promotion_collection.update_one(
        {'_id': ObjectId(_id)},
        {'$set': home_main_feature_promotion.database_dict()}
    )
    if home_main_feature_promotion_document['home_main_feature']['image'] or result.modified_count == 1:
        return jsonify(
            message='Home main feature promotion updated in the database using the id.',
            status=200,
        )
    return jsonify(
        message='Home main feature promotion not updated in the database using the id.',
        status=500
    )


@raw_home_main_feature_promotion_api_v1.route('/delete/id/<string:_id>', methods=['DELETE'])
def delete_home_main_feature_promotion_by_id(_id: str) -> Response:
    """
    :param _id: Home main feature promotion's id
    :return: Response object with a message describing if the home main feature promotion was found (if yes: delete
    home main feature promotion) and the status code
    """
    home_main_feature_promotion_document = read_home_main_feature_promotion_by_id(_id=_id).json['data']

    delete_image_from_aws_s3(image_path=home_main_feature_promotion_document['home_main_feature']['image_path'])

    result = home_main_feature_promotion_collection.delete_one({'_id': ObjectId(_id)})
    if result.deleted_count == 1:
        return jsonify(
            message='Home main feature promotion deleted from the database using the id.',
            status=200
        )
    return jsonify(
        message='Home main feature promotion not deleted in the database using the id.',
        status=500
    )


home_main_feature_promotion_api_v1 = raw_home_main_feature_promotion_api_v1
