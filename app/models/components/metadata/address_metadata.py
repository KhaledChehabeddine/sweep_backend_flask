"""Summary: Address Metadata Model

An address metadata model used to convert an address metadata document into an address metadata object
"""


class AddressMetadata:
    """
    A class to represent an address metadata model

    Attributes
    ----------
    created_date : datetime
        Address' created date
    formatted_address : str
        Address' formatted address
    updated_date : datetime
        Address' updated date
    """

    def __init__(self, address_metadata_document) -> None:
        self.created_date = address_metadata_document['created_date']
        self.formatted_address = address_metadata_document['formatted_address']
        self.updated_date = address_metadata_document['updated_date']
