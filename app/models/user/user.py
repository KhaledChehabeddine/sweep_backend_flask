"""Summary: User Model

A user model used to convert a user document into a user object
"""
from app.models.user.metadata.user_metadata import UserMetadata


class User:
    """
    A class to represent a user model


    Attributes
    ----------
    addresses : list[dict]
        User's address documents
    country : str
        User's country
    country_code : str
        User's country code
    email : str
        User's email
    metadata : dict
        User's metadata document
    password : str
        User's password
    phone_number : str
        User's phone number
    user_type : str
        User's type (company, customer, or worker)
    username : str
        User's username
    verified : bool
        User's verified status
    """

    def __init__(self, user_document: dict) -> None:
        self.addresses = user_document['addresses']
        self.country = user_document['country']
        self.country_code = user_document['country_code']
        self.email = user_document['email']
        self.metadata = UserMetadata(user_metadata_document=user_document['metadata']).__dict__
        self.password = user_document['password']
        self.phone_number = user_document['phone_number']
        self.user_type = user_document['user_type']
        self.username = user_document['username']
        self.verified = user_document['verified']
