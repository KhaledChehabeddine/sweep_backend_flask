"""Summary: Reservation Controller

A controller that assigns a child blueprint to sweep_api_v1 with routes for functions to create, read, update, and
delete reservations from the database
"""
from datetime import datetime
from bson import ObjectId
from flask import Blueprint, Response, request, jsonify
from pymongo.errors import OperationFailure
from app.controllers.user.company_controller import read_company_by_id
from app.controllers.user.worker_controller import read_worker_by_id
from app.database.database import get_database
from app.models.history.reservation import Reservation

raw_reservation_api_v1 = Blueprint('reservation_api_v1', __name__, url_prefix='/reservation')
reservation_collection = get_database()['reservations']


@raw_reservation_api_v1.route('/create', methods=['POST'])
def create_reservation() -> Response:
    """
    :return: Response object with a message describing if the reservation was created (if yes: add account category
    id) and the status code
    """

    reservation_document = request.json

    if reservation_document['service_provider_type'] == 'worker':
        service_provider = read_worker_by_id(_id=reservation_document['service_provider_id']).json['data']
        reservation_document['image_path'] = service_provider['profile_image_path']
        reservation_document['image_url'] = service_provider['profile_image_url']
        reservation_document['metadata']['image_format'] = service_provider['metadata']['profile_image_format']
        reservation_document['metadata']['image_height'] = service_provider['metadata']['profile_image_height']
        reservation_document['metadata']['image_width'] = service_provider['metadata']['profile_image_width']

    if reservation_document['service_provider_type'] == 'company':
        service_provider = read_company_by_id(_id=reservation_document['service_provider_id']).json['data']
        reservation_document['image_path'] = service_provider['logo_image_path']
        reservation_document['image_url'] = service_provider['logo_image_url']
        reservation_document['metadata']['image_format'] = service_provider['metadata']['logo_image_format']
        reservation_document['metadata']['image_height'] = service_provider['metadata']['logo_image_height']
        reservation_document['metadata']['image_width'] = service_provider['metadata']['logo_image_width']

    reservation_document['metadata']['created_date'] = datetime.now()

    reservation = Reservation(reservation_document=reservation_document)
    try:
        reservation_id = str(reservation_collection.insert_one(reservation.database_dict()).inserted_id)
    except OperationFailure:
        return jsonify(
            message='Reservation not added to the database.',
            status=500
        )
    return jsonify(
        data=reservation_id,
        message='Reservation added to the database.',
        status=200
    )


@raw_reservation_api_v1.route('/read/id/<string:_id>', methods=['GET'])
def read_reservation_by_id(_id: str) -> Response:
    """
    :param _id: Reservation's id
    :return: Response object with a message describing if the reservation was found (if yes: add reservation)
    and the status code
    """
    reservation_document = reservation_collection.find_one({'_id': ObjectId(_id)})
    if reservation_document is None:
        return jsonify(
            message='Reservation not found.',
            status=404
        )
    reservation = Reservation(reservation_document=reservation_document)
    return jsonify(
        data=reservation.__dict__,
        message='Reservation found.',
        status=200
    )


@raw_reservation_api_v1.route('/read/customer_id/<string:name>', methods=['GET'])
def read_reservations_by_customer_id(customer_id: str) -> Response:
    """
    :param customer_id: Customer's id
    :return: Response object with message if the customer's reservations were found (if
    yes: add reservations) and the status code
    """
    reservation_documents = reservation_collection.find({'customer_id': customer_id})
    if reservation_documents is None:
        return jsonify(
            message='Customer reservations not found.',
            status=404
        )
    reservations = []
    for reservation_document in reservation_documents:
        reservation = Reservation(reservation_document=reservation_document)
        reservations.append(reservation.__dict__)
    return jsonify(
        data=reservations,
        message='Customer reservations found.',
        status=200
    )


@raw_reservation_api_v1.route('/read/service_provider_id/<string:name>', methods=['GET'])
def read_reservations_by_service_provider_id(service_provider_id: str) -> Response:
    """
    :param service_provider_id: Service provider's id
    :return: Response object with message if the service provider's reservations were found (if
    yes: add reservations) and the status code
    """
    reservation_documents = reservation_collection.find({'service_provider_id': service_provider_id})
    if reservation_documents is None:
        return jsonify(
            message='Service provider reservations not found.',
            status=404
        )
    reservations = []
    for reservation_document in reservation_documents:
        reservation = Reservation(reservation_document=reservation_document)
        reservations.append(reservation.__dict__)
    return jsonify(
        data=reservations,
        message='Service provider reservations found.',
        status=200
    )


@raw_reservation_api_v1.route('/read/all', methods=['GET'])
def read_reservations() -> Response:
    """
    :return: Response object with message if the reservations were found (if yes: return reservations)
    and the status code
    """
    reservations = []
    reservation_documents = reservation_collection.find()
    if reservation_documents:
        for reservation_document in reservation_documents:
            reservation = Reservation(reservation_document=reservation_document)
            reservations.append(reservation.__dict__)
        if reservations:
            return jsonify(
                data=reservations,
                message='Reservations found.',
                status=200
            )
    return jsonify(
        message='Reservations not found.',
        status=404
    )


@raw_reservation_api_v1.route('/delete/id/<string:_id>', methods=['DELETE'])
def delete_reservation_by_id(_id: str) -> Response:
    """
    :param _id: Reservation's id
    :return: Response object with message if the reservation was deleted and the status code
    """
    reservation_document = reservation_collection.find_one({'_id': ObjectId(_id)})
    if reservation_document is None:
        return jsonify(
            message='Reservation not found.',
            status=404
        )
    reservation_collection.delete_one({'_id': ObjectId(_id)})
    return jsonify(
        message='Reservation deleted.',
        status=200
    )


reservation_api_v1 = raw_reservation_api_v1
