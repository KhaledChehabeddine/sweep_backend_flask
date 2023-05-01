"""Summary: Search Model

A Search model used to convert a search document into a search object
"""
from app.models.search.metadata.search_metadata import SearchMetadata


class Search:
    """
    A class to represent a search object

    Attributes
    ----------
    _id : str
        Search object's ID
    metadata : SearchMetadata
        Search object's metadata
    query : str
        Search object's query for the search object
    """

    def __init__(self, search_dict: dict) -> None:
        self._id = str(search_dict['_id'])
        self.metadata = SearchMetadata(search_dict['metadata'])
        self.query = str(search_dict['query'])
