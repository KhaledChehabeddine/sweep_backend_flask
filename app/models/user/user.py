"""Summary: User Model

A user model used to convert a user document into a user object
"""


class User:
    """
    A class to represent a user model


    Attributes
    ----------
    address : str
        User's address
    country : str
        User's country
    country_code : str
        User's country code
    email : str
        User's email
    _id : str
        User's id
    password : str
        User's password
    phone_number : str
        User's phone number
    username : str
        User's username
    """

    def __init__(self, user_document: dict) -> None:
        self.address = user_document['address']
        self.country = user_document['country']
        self.country_code = user_document['country_code']
        self.email = user_document['email']
        self._id = str(user_document['_id'])
        self.password = user_document['password']
        self.phone_number = user_document['phone_number']
        self.username = user_document['username']

    def create_dict(self) -> dict:
        """
        :return: User's dict (without _id)
        """
        return {
            'address': self.address,
            'country': self.country,
            'country_code': self.country_code,
            'email': self.email,
            'password': self.password,
            'phone_number': self.phone_number,
            'username': self.username
        }
