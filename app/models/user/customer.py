"""Summary: Customer Model

A customer model used to convert a customer document into a customer object
"""
from app.models.user.user import User


class Customer:
    """
    A class to represent a customer model

    Attributes
    ----------
    first_name : str
        Customer's first name
    _id : str
        Customer's id
    last_name : str
        Customer's last name
    recent_searches : list[str]
        Customer's recent searches
    user : dict
        Customer's user document
    """

    def __init__(self, customer_document: dict) -> None:
        self.first_name = str(customer_document['first_name'])
        self._id = str(customer_document['_id'])
        self.last_name = str(customer_document['last_name'])
        self.recent_searches = [str(recent_search) for recent_search in customer_document['recent_searches']]
        self.user = User(user_document=customer_document['user']).__dict__

    def database_dict(self) -> dict:
        """
        :return: A dictionary representation of the customer object without the _id
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'recent_searches': self.recent_searches,
            'user': self.user
        }
