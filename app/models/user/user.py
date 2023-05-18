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
        """
        :param user_document: A user document
        """
        self.addresses = [
            Address(address_document=address_document).__dict__
            for address_document in user_document.get('addresses', [])
        ]
        self.country = str(user_document.get('country', ''))
        self.country_code = str(user_document.get('country_code', ''))
        self.email = str(user_document.get('email', ''))
        self.metadata = UserMetadata(user_metadata_document=user_document.get('metadata', {})).__dict__
        self.password = str(user_document.get('password', ''))
        self.phone_number = str(user_document.get('phone_number', ''))
        self.user_type = str(user_document.get('user_type', ''))
        self.username = str(user_document.get('username', ''))
        self.verified = bool(user_document.get('verified', False))

    def database_dict(self) -> dict:
        """
        :return: A dictionary representation of the user object
        """
        user_dict = {
            'addresses': self.addresses,
            'country': self.country,
            'country_code': self.country_code,
            'email': self.email,
            'metadata': self.metadata,
            'password': self.password,
            'phone_number': self.phone_number,
            'user_type': self.user_type,
            'username': self.username,
            'verified': self.verified,
        }

        if isinstance(self.metadata, UserMetadata):
            if self.metadata.created_date is not None:
                user_dict['metadata']['created_date'] = str(self.metadata.created_date)
            if self.metadata.last_login_date is not None:
                user_dict['metadata']['last_login_date'] = str(self.metadata.last_login_date)
            if self.metadata.updated_date is not None:
                user_dict['metadata']['updated_date'] = str(self.metadata.updated_date)

        for address in user_dict['addresses']:
            if '_id' in address:
                address['_id'] = str(address['_id'])

        return user_dict
