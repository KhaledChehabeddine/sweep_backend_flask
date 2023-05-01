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
    _id : str
        Customer's id
    metadata: dict
        Customer's metadata document
    reservation_ids : list[str]
        Customer's reservation ids
    user : dict
        Customer's user document
    """

    def __init__(self, customer_document: dict) -> None:
        self._id = str(customer_document['_id'])
        self.metadata = CustomerMetadata(customer_metadata_document=customer_document['metadata']).__dict__
        self.reservation_ids = customer_document['reservation_ids']
        self.user = User(user_document=customer_document['user']).__dict__

    def database_dict(self):
        """
        :return: A dictionary representation of the customer object without the _id
        """
        return {
            'metadata': self.metadata,
            'reservation_ids': self.reservation_ids,
            'user': self.user
        }
