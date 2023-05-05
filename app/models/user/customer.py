"""Summary: Customer Model

A customer model used to convert a customer document into a customer object
"""
from app.models.user.metadata.customer_metadata import CustomerMetadata
from app.models.user.user import User


class Customer:
    """
    A class to represent a customer model

    Attributes
    ----------
    first_name : str
        Customer's first name
    _id : str
    last_name : str
        Customer's last name
        Customer's id
    metadata : dict
        Customer's metadata document
    user : dict
        Customer's user document
    """

    def __init__(self, customer_document: dict) -> None:
        self.first_name = str(customer_document['first_name'])
        self._id = str(customer_document['_id'])
        self.last_name = str(customer_document['last_name'])
        self.metadata = CustomerMetadata(customer_metadata_document=customer_document['metadata']).__dict__
        self.user = User(user_document=customer_document['user']).__dict__

    def database_dict(self):
        """
        :return: A dictionary representation of the customer object without the _id
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'metadata': self.metadata,
            'user': self.user
        }
