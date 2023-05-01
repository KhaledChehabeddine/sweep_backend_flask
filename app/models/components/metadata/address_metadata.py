"""Summary: Address Metadata Model

An address metadata model used to convert an address metadata document into an address metadata object
"""


class AddressMetadata:
    """
    A class to represent an address metadata model

    Attributes
    ----------
    formatted_address : str
        Address' formatted address
    """

    def __init__(self, address_metadata_document) -> None:
        self.formatted_address = str(address_metadata_document['formatted_address'])
