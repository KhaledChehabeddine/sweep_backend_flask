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
    user_id : str
        The ID of the user who made the search
    query : str
        The search query entered by the user
    """

    def __init__(self, search_metadata_dict: dict) -> None:
        self.created_date = datetime.strptime(search_metadata_dict['created_date'], '%Y-%m-%d %H:%M:%S')
        self.user_id = search_metadata_dict['user_id']
        self.query = search_metadata_dict['query']
