"""Summary: Review Controller CRUD Operations

A controller that assigns a child blueprint to sweep_api_v1 with routes for functions to create, read, update, and
delete reviews from the database
"""

from bson import ObjectId
from flask import Blueprint, Response, jsonify, request
from pymongo.errors import OperationFailure
from app.database.database import get_database
from app.models.utilities.review import Review
from app.routes.blueprints import sweep_api_v1

review_api_v1 = Blueprint('review_api_v1', __name__, url_prefix='/review')
review_collection = get_database()['reviews']


@review_api_v1.route('/create', methods=['POST'])
def create_review() -> Response:
    """
    :return: Response object with a message describing if the review was created and the status code
    """
    review_document = request.json
    review = Review(review_document=review_document)
    try:
        review_collection.insert_one(review.database_dict())
    except OperationFailure:
        return jsonify(
            message='Review not added to the database.',
            status=500
        )
    return jsonify(
        message='Review added to the database.',
        status=200
    )


@review_api_v1.route('/read/id/<string:_id>', methods=['GET'])
def read_review_by_id(_id: str) -> Response:
    """
    :param _id: Review's id
    :return: Response object with a message describing if the reviews were found (if yes: add user objects) and the
    status code
    """
    review_document = review_collection.find_one({'_id': ObjectId(_id)})
    if review_document:
        review = Review(review_document=review_document)
        return jsonify(
            data=review.__dict__,
            message='Review found in the database using the id.',
            status=200,
        )
    return jsonify(
        message='Review not found in the database using the id.',
        status=500
    )


@review_api_v1.route('/read', methods=['GET'])
def read_reviews() -> Response:
    """
    :return: Response object with a message describing if all the reviews were found (if yes: add user objects) and the
    status code
    """
    reviews = []
    review_documents = review_collection.find()
    if review_documents:
        for review_document in review_documents:
            review = Review(review_document=review_document)
            reviews.append(review.__dict__)
        return jsonify(
            data=reviews,
            message='All reviews found in the database.',
            status=200
        )
    return jsonify(
        message='No review found in the database.',
        status=500
    )


@review_api_v1.route('/update/id/<string:_id>', methods=['PUT'])
def update_review_by_id(_id: str) -> Response:
    """
    :param _id: Review's id
    :return: Response object with a message describing if the review was updated and the status code
    """
    review_document = request.json
    review = Review(review_document=review_document)
    result = review_collection.update_one(
        {'_id': ObjectId(_id)},
        {'$set': review.__dict__}
    )
    if result.modified_count == 1:
        return jsonify(
            message='Review updated in the database using the id.',
            status=200,
        )
    return jsonify(
        message='Review not updated in the database using the id.',
        status=500,
    )


@review_api_v1.route('/delete/id/<string:_id>', methods=['DELETE'])
def delete_review_by_id(_id: str) -> Response:
    """
    :param _id: Review's id
    :return: Response object with a message describing if the review was deleted and the status code
    """
    result = review_collection.delete_one({'_id': ObjectId(_id)})
    if result.deleted_count == 1:
        return jsonify(
            message='Review deleted in the database using the id.',
            status=200,
        )
    return jsonify(
        message='Review not deleted in the database using the id.',
        status=500,
    )


sweep_api_v1.register_blueprint(review_api_v1)
