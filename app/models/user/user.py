"""Summary: User Model

A user model used to convert a user document into a user object
"""
from app.models.components.address import Address
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
        User's type (service_provider, or worker)
    username : str
        User's username
    verified : bool
        User's verified status
    """

    def __init__(self, user_document: dict) -> None:
        self.addresses = [
            Address(address_document=address_document).__dict__ for address_document in user_document['addresses']
        ]
        self.country = str(user_document['country'])
        self.country_code = str(user_document['country_code'])
        self.email = str(user_document['email'])
        self.metadata = UserMetadata(user_metadata_document=user_document['metadata']).__dict__
        self.password = str(user_document['password'])
        self.phone_number = str(user_document['phone_number'])
        self.user_type = str(user_document['user_type'])
        self.username = str(user_document['username'])
        self.verified = bool(user_document['verified'])
