"""Summary: Customer Controller

A controller that assigns a child blueprint to sweep_api_v1 with routes for functions to create, read, update, and
delete customers from the database
"""
from datetime import datetime
from flask import Blueprint, Response, request, jsonify
from pymongo.errors import OperationFailure
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
    customer_document['metadata']['created_date'] = datetime.now()
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


@raw_customer_api_v1.route('/read/id/<string:_id>', methods=['GET'])
def read_customer(_id: str) -> Response:
    """
    :return:
    """


customer_api_v1 = raw_customer_api_v1
