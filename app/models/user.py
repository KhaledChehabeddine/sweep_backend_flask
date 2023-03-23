"""Summary: User Model

A user model used to convert a user document into a user object
"""


class User:
    """
    A class to represent a user


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
    password : str
        User's password
    phone_number : str
        User's phone number

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
        :return: User's address
        """
        return self.address

    def set_address(self, address) -> None:
        """
        :param address: User's address
        """
        self.address = address

    def get_country(self) -> str:
        """
        :return: User's country
        """
        return self.country

    def set_country(self, country) -> None:
        """
        :param country: User's country
        """
        self.country = country

    def get_country_code(self):
        """
        :return: User's country code
        """
        return self.country_code

    def set_country_code(self, country_code):
        """
        :param country_code: User's country code
        """
        self.country_code = country_code

    def get_email(self):
        """
        :return: User's email
        """
        return self.email

    def set_email(self, email):
        """
        :param email: User's email
        """
        self.email = email

    def get_password(self):
        """
        :return: User's password
        """
        return self.password

    def set_password(self, password):
        """
        :param password: User's password
        """
        self.password = password

    def get_phone_number(self):
        """
        :return: User's phone number
        """
        return self.phone_number

    def set_phone_number(self, number):
        """
        :param number: User's phone number
        """
        self.phone_number = number
