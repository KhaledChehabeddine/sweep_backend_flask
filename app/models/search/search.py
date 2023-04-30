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
        The ID of the search object
    metadata : SearchMetadata
        The metadata for the search object
    categories : List[str]
        A list of categories for the search results
    """

    def __init__(self, search_dict: dict) -> None:
        self._id = search_dict['_id']
        self.metadata = SearchMetadata(search_dict['metadata'])
        self.categories = search_dict['categories']
