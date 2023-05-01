"""Summary: Search Metadata Model

A search metadata model used to convert a search metadata document into a user metadata object
"""

from datetime import datetime


class SearchMetadata:
    """
    A class to represent the metadata for a search object

    Attributes
    ----------
    created_date : datetime
        Search's created date
    updated_date : datetime
        Search's updated date
    """

    def __init__(self, search_metadata_dict: dict) -> None:
        self.created_date = search_metadata_dict['created_date']
        self.updated_date = search_metadata_dict['updated_date']
