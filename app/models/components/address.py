"""Summary: Address Model

An address model used to convert an address document into an address object
"""
from app.models.components.metadata.address_metadata import AddressMetadata


class Address:
    """
    A class to represent an address model

    Attributes
    ----------
    city : str
        Address's city
    country : str
        Address's country
    latitude : float
        Address's latitude
    longitude : float
        Address's longitude
    metadata : dict
        Address's metadata document
    name : str
        Address's name
    state : str
        Address's state
    street_address_1 : str
        Address's street address 1
    street_address_2 : str
        Address's street address 2
    zip_code : str
        Address's zip code
    """

    def __init__(self, address_document) -> None:
        self.city = address_document['city']
        self.country = address_document['country']
        self.latitude = address_document['latitude']
        self.longitude = address_document['longitude']
        self.metadata = AddressMetadata(address_document['metadata']).__dict__
        self.name = address_document['name']
        self.state = address_document['state']
        self.street_address_1 = address_document['street_address_1']
        self.street_address_2 = address_document['street_address_2']
        self.zip_code = address_document['zip_code']
