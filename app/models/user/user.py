"""Summary: user Model

A user model used to convert a user document into a user object
"""


class User:
    """
    A class to represent a user model


    Attributes
    ----------
    address : str
        user's address
    country : str
        user's country
    country_code : str
        user's country code
    email : str
        user's email
    password : str
        user's password
    phone_number : str
        user's phone number

    Methods
    -------
    get_address() : str
        Returns the user's address
    set_address(address) : None
        Sets the user's address
    get_country() : str
        Returns the user's country
    set_country(country) : None
        Sets the user's country
    get_country_code() : str
        Returns the user's country code
    set_country_code(country_code) : None
        Sets the user's country code
    get_email() : str
        Returns the user's email
    set_email(email) : None
        Sets the user's email
    get_password() : str
        Returns the user's password
    set_password(password) : None
        Sets the user's password
    get_phone_number() : str
        Returns the user's phone number
    set_phone_number(phone_number) : None
        Sets the user's phone number
    """

    def __init__(self, user_document: dict) -> None:
        self.address = user_document['address']
        self.country = user_document['country']
        self.country_code = user_document['country_code']
        self.email = user_document['email']
        self.password = user_document['password']
        self.phone_number = user_document['phone_number']

    def get_address(self) -> str:
        """
        :return: user's address
        """
        return self.address

    def set_address(self, address) -> None:
        """
        :param address: user's address
        """
        self.address = address

    def get_country(self) -> str:
        """
        :return: user's country
        """
        return self.country

    def set_country(self, country) -> None:
        """
        :param country: user's country
        """
        self.country = country

    def get_country_code(self):
        """
        :return: user's country code
        """
        return self.country_code

    def set_country_code(self, country_code):
        """
        :param country_code: user's country code
        """
        self.country_code = country_code

    def get_email(self):
        """
        :return: user's email
        """
        return self.email

    def set_email(self, email):
        """
        :param email: user's email
        """
        self.email = email

    def get_password(self):
        """
        :return: user's password
        """
        return self.password

    def set_password(self, password):
        """
        :param password: user's password
        """
        self.password = password

    def get_phone_number(self):
        """
        :return: user's phone number
        """
        return self.phone_number

    def set_phone_number(self, number):
        """
        :param number: user's phone number
        """
        self.phone_number = number
