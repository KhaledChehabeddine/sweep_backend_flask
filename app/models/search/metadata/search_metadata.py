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
        The date and time the search object was created
    updated_date : datetime
        The date and time the search object was updated
    total_categories : int
        The total number of categories for the search object
    """

    def __init__(self, search_metadata_dict: dict) -> None:
        self.total_categories = search_metadata_dict['total_categories']
        self.created_date = datetime.strptime(search_metadata_dict['created_date'], '%Y-%m-%d %H:%M:%S')
        self.updated_date = datetime.strptime(search_metadata_dict['updated_date'], '%Y-%m-%d %H:%M:%S')
