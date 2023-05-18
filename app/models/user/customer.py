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
    last_name : str
        Customer's last name
        Customer's id
    recent_searches : list
        Customer's recent searches
    transaction_history : list
        Customer's transaction history
    user : dict
        Customer's user document
    """

    def __init__(self, customer_document: dict) -> None:
        self.first_name = str(customer_document['first_name'])
        self._id = str(customer_document['_id'])
        self.last_name = str(customer_document['last_name'])
        self.recent_searches = customer_document['recent_searches']
        self.transaction_history = customer_document['transaction_history']
        self.user = User(user_document=customer_document['user']).__dict__

    def database_dict(self) -> dict:
        """
        :return: A dictionary representation of the customer object without the _id
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'recent_searches': self.recent_searches,
            'transaction_history': self.transaction_history,
            'user': self.user
        }
