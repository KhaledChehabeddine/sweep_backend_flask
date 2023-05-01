"""Summary: Reservation Controller

A controller that assigns a child blueprint to sweep_api_v1 with routes for functions to create, read, update, and
delete reservations from the database
"""
from datetime import datetime
from flask import Blueprint, Response, jsonify, request
from pymongo.errors import OperationFailure
from app.aws.aws_s3_client import upload_image_to_aws_s3
from app.models.history.reservation import Reservation

raw_reservation_api_v1 = Blueprint('reservation_api_v1', __name__, url_prefix='/reservation')


def _configure_reservation_document(reservation_document: dict) -> dict:
    """
    :param reservation_document: A reservation document
    :return: A reservation document with the configured metadata
    """
    reservation_document['metadata'] = upload_image_to_aws_s3(
        object_metadata_document=reservation_document['metadata'],
        object_image=('', reservation_document['image'], reservation_document['image_path'])
    ).json['data']

    reservation_document['metadata']['datetime'] = datetime.now()

    return reservation_document


@raw_reservation_api_v1.route('create', methods=['POST'])
def create_reservation() -> Response:
    """
    :return: Response object with a message describing if the reservation was created (if yes: add account category
    id) and the status code
    """

    reservation_document = request.json
    reservation_document['metadata'] = {}  # Missing metadata function
    reservation_document = _configure_reservation_document(reservation_document=reservation_document)
    reservation_document = Reservation(reservation_document=reservation_document)
    try:
       #  reservation_id = str(reservation_document.insert_one(reservation_document.database_dict()).inserted_id)
    except OperationFailure:
        return jsonify(
            message='Account category not added to the database.',
            status=500
        )
    return jsonify(
       #  data=reservation_id,
        message='Account category added to the database.',
        status=200
    )


@raw_reservation_api_v1.route('/read/id/<string:_id>', methods=['GET'])
def read_reservation_by_id(_id: str) -> Response:
    """
    :param name: Reservation's id
    :return: Response object with message if the reservation was found (if yes: add reservation) and the status code
    """
    # reservation = _configure_reservation_document()
