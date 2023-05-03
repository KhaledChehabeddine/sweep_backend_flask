"""Summary: Customer Controller

A controller that assigns a child blueprint to sweep_api_v1 with routes for functions to create, read, update, and
delete customers from the database
"""
from flask import Blueprint

from app.database.database import get_database

raw_customer_api_v1 = Blueprint('customer_api_v1', __name__, url_prefix='/customer')
customer_collection = get_database()['customers']


def _configure_customer(customer_document: dict) -> dict:
    """
    :param customer_document: A customer document
    :return: A customer document with configured metadata
    """

    return customer_document
