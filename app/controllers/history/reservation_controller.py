"""Summary: Reservation Controller

A controller that assigns a child blueprint to sweep_api_v1 with routes for functions to create, read, update, and
delete reservations from the database
"""
from datetime import datetime
from flask import Blueprint, Response, request, jsonify
from pymongo import ASCENDING
from pymongo.errors import OperationFailure
from app.aws.aws_s3_client import upload_image_to_aws_s3
from app.database.database import get_database
from app.models.history.reservation import Reservation

raw_reservation_api_v1 = Blueprint('reservation_api_v1', __name__, url_prefix='/reservation')
reservation_collection = get_database()['reservations']

reservation_collection.create_index([('name', ASCENDING)], unique=True)


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
    reservation_document = _configure_reservation_document(reservation_document=reservation_document)
    reservation = Reservation(reservation_document=reservation_document)
    try:
        reservation_id = str(reservation_collection.insert_one(reservation_document.database_dict()).inserted_id)
    except OperationFailure:
        return jsonify(
            message='Account category not added to the database.',
            status=500
        )
    return jsonify(
        data=reservation_id,
        message='Account category added to the database.',
        status=200
    )


@raw_reservation_api_v1.route('/read/id/<string:_id>', methods=['GET'])
def read_reservation_by_id(_id: str) -> Response:
    """
    :param _id: Reservation's id
    :return: Response object with a message describing if the reservation was found (if yes: add reservation)
    and the status code
    """
    reservation_document = reservation_collection.find_one({'_id': _id})
    if reservation_document is None:
        return jsonify(
            message='Reservation not found.',
            status=404
        )
    reservation = Reservation(reservation_document=reservation_document)
    return jsonify(
        data=reservation.database_dict(),
        message='Reservation found.',
        status=200
    )


@raw_reservation_api_v1.route('/read/customer_id/<string:name>', methods=['GET'])
def read_reservations_by_customer_id(_id: str) -> Response:
    """
    :param _id: Customer's id
    :return: Response object with message if the customer's reservations were found (if
    yes: add reservations) and the status code
    """
    reservation_documents = reservation_collection.find({'customer_id': _id})
    if reservation_documents is None:
        return jsonify(
            message='Reservations not found.',
            status=404
        )
    reservations = []
    for reservation_document in reservation_documents:
        reservation = Reservation(reservation_document=reservation_document)
        reservations.append(reservation.database_dict())
    return jsonify(
        data=reservations,
        message='Reservations found.',
        status=200
    )


@raw_reservation_api_v1.route('/read', methods=['GET'])
def read_reservations() -> Response:
    """
    :return: Response object with message if the reservations were found (if yes: add reservations) and the status code
    """
    reservation_documents = reservation_collection.find({})
    if reservation_documents is None:
        return jsonify(
            message='Reservations not found.',
            status=404
        )
    reservations = []
    for reservation_document in reservation_documents:
        reservation = Reservation(reservation_document=reservation_document)
        reservations.append(reservation.database_dict())
    return jsonify(
        data=reservations,
        message='Reservations found.',
        status=200
    )


@raw_reservation_api_v1.route('/delete/id/<string:_id>', methods=['DELETE'])
def delete_reservation_by_id(_id: str) -> Response:
    """
    :param _id: Reservation's id
    :return: Response object with message if the reservation was deleted and the status code
    """
    reservation_document = reservation_collection.find_one({'_id': _id})
    if reservation_document is None:
        return jsonify(
            message='Reservation not found.',
            status=404
        )
    reservation_collection.delete_one({'_id': _id})
    return jsonify(
        message='Reservation deleted.',
        status=200
    )


raw_reservation_api_v1 = raw_reservation_api_v1
