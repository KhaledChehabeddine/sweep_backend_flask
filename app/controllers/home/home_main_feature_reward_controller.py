"""Summary: Home Main Feature Reward Controller CRUD Operations

A controller that assigns a child blueprint to sweep_api_v1 with routes for functions to create, read, update, and
delete home main feature rewards from the database
"""
from bson import ObjectId
from flask import Blueprint, Response, jsonify, request
from pymongo.errors import OperationFailure
from app.database.database import get_database
from app.functions.create_object_metadatas import create_home_feature_metadata
from app.functions.update_object_metadatas import update_home_main_feature_metadata
from app.models.home.home_main_feature_reward import HomeMainFeatureReward
from app.routes.blueprints import sweep_api_v1
from app.aws.aws_s3_client import delete_image_from_aws_s3

home_main_feature_reward_api_v1 = Blueprint(
    'home_main_feature_reward_api_v1',
    __name__,
    url_prefix='/home_main_feature_reward'
)
home_main_feature_rewards_collection = get_database()['home_main_feature_rewards']


@home_main_feature_reward_api_v1.route('/create', methods=['POST'])
def create_home_main_feature_reward() -> Response:
    """
    :return: Response object with a message describing if the home main feature reward was created (if yes: add home
    main feature reward) and the status code
    """
    home_main_feature_reward_document = request.json

    home_main_feature_reward_document['metadata'] = {
        'total_amount_claimed': 0,
        'total_claimed_customers': 0
    }

    # aws_s3_upload_response = upload_image_to_aws_s3(image_data=request.json['image'], image_path=request.json[
    # 'file_path']).json home_main_feature_reward_document['home_main_feature']['metadata'] = \
    # create_home_main_feature_metadata(aws_s3_upload_data=aws_s3_upload_response['data'])

    home_main_feature_reward_document['home_main_feature']['home_feature']['metadata'] = create_home_feature_metadata()

    home_main_feature_reward = HomeMainFeatureReward(
        home_main_feature_reward_document=home_main_feature_reward_document
    )
    try:
        home_main_feature_reward_id = str(
            home_main_feature_rewards_collection.insert_one(home_main_feature_reward.database_dict()).inserted_id
        )
    except OperationFailure:
        return jsonify(
            message='Home main feature reward not added to the database.',
            status=500
        )
    return jsonify(
        data=home_main_feature_reward_id,
        message='Home main feature reward added to the database.',
        status=200
    )


@home_main_feature_reward_api_v1.route('/read/id/<string:_id>', methods=['GET'])
def read_home_main_feature_reward_by_id(_id: str) -> Response:
    """
    :param _id: Home main feature reward's id
    :return: Response object with a message describing if the home main feature reward was found (if yes: add home
    main feature reward) and the status code
    """
    home_main_feature_reward_document = home_main_feature_rewards_collection.find_one({'_id': ObjectId(_id)})
    if home_main_feature_reward_document:
        home_main_feature_reward = HomeMainFeatureReward(
            home_main_feature_reward_document=home_main_feature_reward_document
        )
        return jsonify(
            data=home_main_feature_reward.__dict__,
            message='Home main feature reward found in the database using the id.',
            status=200
        )
    return jsonify(
        message='Home main feature reward not found in the database using the id.',
        status=500
    )


@home_main_feature_reward_api_v1.route('/read', methods=['GET'])
def read_home_main_feature_rewards() -> Response:
    """
    :return: Response object with a message describing if all the home main feature rewards were found (if yes: add home
    main feature rewards) and the status code
    """
    home_main_feature_rewards = []
    home_main_feature_reward_documents = home_main_feature_rewards_collection.find()
    if home_main_feature_reward_documents:
        for home_main_feature_reward_document in home_main_feature_reward_documents:
            home_main_feature_reward = HomeMainFeatureReward(
                home_main_feature_reward_document=home_main_feature_reward_document
            )
            home_main_feature_rewards.append(home_main_feature_reward.__dict__)
        return jsonify(
            data=home_main_feature_rewards,
            message='Home main feature rewards found in the database.',
            status=200
        )
    return jsonify(
        message='No home main feature reward found in the database.',
        status=500
    )


@home_main_feature_reward_api_v1.route('/update/id/<string:_id>', methods=['PUT'])
def update_home_main_feature_reward_by_id(_id: str) -> Response:
    """
    :param _id: Home main feature reward's id
    :return: Response object with a message describing if the home main feature reward was found (if yes: update home
    main feature reward) and the status code
    """
    home_main_feature_reward_document = request.json

    home_main_feature_reward_document['metadata']['total_amount_claimed'] = \
        home_main_feature_reward_document['amount'] * \
        home_main_feature_reward_document['metadata']['total_claimed_customers']

    home_main_feature_reward_document = update_home_main_feature_metadata(
        object_document=home_main_feature_reward_document['home_main_feature']['metadata']
    )

    home_main_feature_reward = HomeMainFeatureReward(
        home_main_feature_reward_document=home_main_feature_reward_document
    )
    result = home_main_feature_rewards_collection.update_one(
        {'_id': _id},
        {'$set': home_main_feature_reward.database_dict()}
    )
    if home_main_feature_reward_document['image'] or result.modified_count == 1:
        return jsonify(
            message='Home main feature reward updated in the database using the id.',
            status=200,
        )
    return jsonify(
        message='Home main feature reward not updated in the database using the id.',
        status=500
    )


@home_main_feature_reward_api_v1.route('/delete/id/<string:_id>', methods=['DELETE'])
def delete_home_main_feature_reward_by_id(_id: str) -> Response:
    """
    :param _id: Home main feature reward's id
    :return: Response object with a message describing if the home main feature reward was found (if yes: delete
    home main feature reward) and the status code
    """
    home_main_feature_reward_document = read_home_main_feature_reward_by_id(_id=_id).json['data']

    delete_image_from_aws_s3(image_path=home_main_feature_reward_document['file_path'])

    result = home_main_feature_rewards_collection.delete_one({'_id': ObjectId(_id)})
    if result.deleted_count == 1:
        return jsonify(
            message='Home main feature reward deleted from the database using the id.',
            status=200
        )
    return jsonify(
        message='Home main feature reward not deleted in the database using the id.',
        status=500
    )


sweep_api_v1.register_blueprint(home_main_feature_reward_api_v1)
