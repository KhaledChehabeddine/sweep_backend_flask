"""Summary: User Metadata Model

A customer metadata model used to convert a customer metadata document into a customer metadata object
"""


class CustomerMetadata:
    """
    A class to represent a customer metadata model

    Attributes:
    ----------
    created_date : datetime
        Customer's created date
    """

    def __init__(self, customer_metadata_document: dict) -> None:
        self.created_date = customer_metadata_document['created_date']
