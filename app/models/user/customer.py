"""Summary: Customer Model

A customer model used to convert a customer document into a customer object

Attributes
----------
_id: str
    Customer's id
reservation_ids: list[str]
    Customer's reservation ids
user: dict
    Customer's user document
"""
from app.models.user.user import User


def __init__(self, customer_document: dict) -> None:
    self._id = customer_document['_id']
    self.reservation_ids = customer_document['reservation_ids']
    self.user = User(user_document=customer_document['user']).__dict__


def database_dict(self):
    """
    :return: A dictionary representation of the customer object without the _id
    """
    return {
        'reservation_ids': self.reservation_ids,
        'user': self.user
    }
