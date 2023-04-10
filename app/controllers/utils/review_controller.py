"""Summary: Review Controller CRUD Operations

A controller that assigns a child blueprint to sweep_api_v1 with routes for functions to create, read, update, and
delete reviews from the database
"""

import json
from bson import json_util
from flask import Blueprint, Response, jsonify, request
from pymongo.errors import OperationFailure
from app.database.database import get_database
from app.models.utils.review import Review
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
        review_collection.insert_one(review.__dict__)
    except OperationFailure:
        return jsonify({
            'message': 'Review not added to the database.',
            'status': 500
        })
    return jsonify({
        'message': 'Review added to the database.',
        'status': 200
    })


@review_api_v1.route('/read/<string:review_id>', methods=['GET'])
def read_review_by_id(review_id: str) -> Response:
    """
    :param review_id: Review's id
    :return: Response object with a message describing if the reviews were found (if yes: add user objects) and the
    status code
    """
    review_document = json.loads(json_util.dumps(review_collection.find_one({'review_id': review_id})),
                                 object_hook=json_util.object_hook)
    if review_document:
        review = Review(review_document=review_document)
        return jsonify({
            'message': 'Review found in the database using the id.',
            'status': 200,
            'review': review.__dict__
        })
    return jsonify({
        'message': 'Review not found in the database using the id.',
        'status': 404
    })


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
            review_document = json.loads(json_util.dumps(review_document), object_hook=json_util.object_hook)
            review = Review(review_document=review_document)
            reviews.append(review.__dict__)
        return jsonify({
            'message': 'All reviews found in the database.',
            'reviews': reviews,
            'status': 200
        })
    return jsonify({
        'message': 'No review found in the database.',
        'status': 404
    })


@review_api_v1.route('/update/<string:review_id>', methods=['PUT'])
def update_review_by_id(review_id: str) -> Response:
    """
    :param review_id: Review's id
    :return: Response object with a message describing if the review was updated and the status code
    """
    review_document = request.json
    review = Review(review_document=review_document)
    result = review_collection.update_one(
        {'review_id': review_id},
        {'$set': review.__dict__}
    )
    if result.modified_count == 1:
        return jsonify({
            'message': 'Review updated in the database using the id.',
            'status': 200,
        })
    return jsonify({
        'message': 'Review not found in the database using the id.',
        'status': 500,
    })


@review_api_v1.route('/delete/<string:review_id>', methods=['DELETE'])
def delete_review_by_id(review_id: str) -> Response:
    """
    :param review_id: Review's id
    :return: Response object with a message describing if the review was deleted and the status code
    """
    result = review_collection.delete_one({'review_id': review_id})
    if result.deleted_count == 1:
        return jsonify({
            'message': 'Review deleted in the database using the id.',
            'status': 200,
        })
    return jsonify({
        'message': 'Review not found in the database using the id.',
        'status': 500,
    })


sweep_api_v1.register_blueprint(review_api_v1)
