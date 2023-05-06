"""Summary: Customer Controller

A controller that assigns a child blueprint to sweep_api_v1 with routes for functions to create, read, update, and
delete customers from the database
"""
from datetime import datetime
from bson import ObjectId
from flask import Blueprint, Response, request, jsonify
from pymongo.errors import OperationFailure
from app.controllers.history.reservation_controller import read_reservations_by_customer_id
from app.database.database import get_database
from app.models.user.customer import Customer

raw_customer_api_v1 = Blueprint('customer_api_v1', __name__, url_prefix='/customer')
customer_collection = get_database()['customers']


@raw_customer_api_v1.route('/create', methods=['POST'])
def create_customer() -> Response:
    """
    :return: Response object with a message describing if the customer was created (if yes: add account category
    id) and the status code
    """

    customer_document = request.json
    customer_document['user']['metadata']['created_date'] = datetime.now()
    customer = Customer(customer_document=customer_document)
    try:
        customer_id = str(customer_collection.insert_one(customer.database_dict()).inserted_id)
    except OperationFailure:
        return jsonify(
            message='Customer not added to the database.',
            status=500
        )
    return jsonify(
        data=customer_id,
        message='Customer added to the database.',
        status=200
    )


@raw_customer_api_v1.route('/update/id/<string:_id>/add/search', methods=['PUT'])
def update_customer_add_search_by_id(_id: str) -> Response:
    """
    :param _id: Customer id
    :return: Response object with a message describing if the search was added to customer and the status code
    """
    customer_document = customer_collection.find_one({'_id': ObjectId(_id)})
    if customer_document:
        customer = Customer(customer_document=customer_document)
        customer.recent_searches.append(request.json)
        customer_collection.update_one({'_id': ObjectId(_id)}, {'$set': customer.database_dict()})
        return jsonify(
            message='Search added to customer using the id.',
            status=200
        )
    return jsonify(
        message='Search not added to customer using the id.',
        status=404
    )


@raw_customer_api_v1.route('/update/id/<string:_id>/add/transaction', methods=['PUT'])
def update_customer_add_transaction_by_id(_id: str) -> Response:
    """
    :param _id: Customer id
    :return: Response object with a message describing if the transaction was added to customer and the status code
    """
    customer_document = customer_collection.find_one({'_id': ObjectId(_id)})
    if customer_document:
        customer = Customer(customer_document=customer_document)
        customer.transaction_history.append(request.json)
        customer_collection.update_one({'_id': ObjectId(_id)}, {'$set': customer.database_dict()})
        return jsonify(
            message='Transaction added to customer using the id.',
            status=200
        )
    return jsonify(
        message='Transaction not added to customer using the id.',
        status=404
    )


@raw_customer_api_v1.route('/read/id/<string:_id>', methods=['GET'])
def read_customer_by_id(_id: str) -> Response:
    """
    :param _id: Customer id
    :return: Response object with a message describing if the customer was read and the status code
    """
    customer_document = customer_collection.find_one({'_id': ObjectId(_id)})
    if customer_document:
        customer = Customer(customer_document=customer_document)
        return jsonify(
            data=customer.__dict__,
            message='Customer found in the database using the id.',
            status=200
        )
    return jsonify(
        message='Customer not found in the database using the id.',
        status=404
    )


@raw_customer_api_v1.route('/read/all', methods=['GET'])
def read_all_customers() -> Response:
    """
    :return: Response object with a message describing if the customer was read and the status code
    """
    customers = []
    customer_documents = customer_collection.find({})
    if customer_documents:
        for customer_document in customer_documents:
            customer = Customer(customer_document=customer_document)
            customers.append(customer.__dict__)
        if customers:
            return jsonify(
                data=customers,
                message='All customers found in the database.',
                status=200
            )
    return jsonify(
        message='No customer found in the database.',
        status=404
    )


@raw_customer_api_v1.route('read/id/reservations/all', methods=['GET'])
def read_all_customer_reservations_by_id(_id: str) -> Response:
    """
    :param _id: Customer id
    :return: Response object with a message describing if the customer's reservations were read and the status code
    """
    if customer_collection.find({'_id': ObjectId(_id)}):
        read_reservations_by_customer_id(_id)
    return jsonify(
        message='No reservation for the customer found in the database.',
        status=404
    )


@raw_customer_api_v1.route('/update/id/<string:_id>', methods=['PUT'])
def update_customer_by_id(_id: str) -> Response:
    """
    :param _id: Customer id
    :return: Response object with a message describing if the customer was updated and the status code
    """
    customer_document = customer_collection.find_one({'_id': ObjectId(_id)})
    if customer_document:
        customer_document = request.json
        customer_document['user']['metadata']['updated_date'] = datetime.now()
        customer = Customer(customer_document=customer_document)
        customer_collection.update_one(
            {'_id': ObjectId(_id)},
            {'$set': customer.database_dict()}
        )
        return jsonify(
            message='Customer updated in the database using the id.',
            status=200
        )
    return jsonify(
        message='Customer not updated in the database using the id.',
        status=404
    )


@raw_customer_api_v1.route('/delete/id/<string:_id>', methods=['DELETE'])
def delete_customer_by_id(_id: str) -> Response:
    """
    :param _id: Customer id
    :return: Response object with a message describing if the customer was deleted and the status code
    """
    customer_document = customer_collection.find_one({'_id': ObjectId(_id)})
    if customer_document:
        customer_collection.delete_one({'_id': ObjectId(_id)})
        return jsonify(
            message='Customer deleted from the database using the id.',
            status=200
        )
    return jsonify(
        message='Customer not deleted from the database using the id.',
        status=404
    )


customer_api_v1 = raw_customer_api_v1
