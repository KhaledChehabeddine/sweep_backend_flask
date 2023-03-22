class User:
    def __init__(self, address: str, country: str, country_code: str, email: str, number: str, password: str):
        self.address = address
        self.country = country
        self.country_code = country_code
        self.email = email
        self.number = number
        self.password = password

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_country(self):
        return self.country

    def set_country(self, country):
        self.country = country

    def get_country_code(self):
        return self.country_code

    def set_country_code(self, country_code):
        self.country_code = country_code

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number = number

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password
