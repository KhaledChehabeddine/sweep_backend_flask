"""Summary: Search Result Model

A search result model used to convert a search result document into a search object
"""
from app.models.search.metadata.search_result_metadata import SearchResultMetadata


class SearchResult:
    """
    A class to represent a search result object

    Attributes
    ----------
    id : str
        The ID of the search result object
    metadata : SearchResultMetadata
        The metadata for the search result object
    worker_id : str
        The ID of the worker associated with the search result
    organization_id : str
        The ID of the organization associated with the search result
    """
    def __init__(self, search_result_dict: dict) -> None:
        self.id = search_result_dict['_id']
        self.metadata = SearchResultMetadata(search_result_dict['metadata'])
        self.worker_id = search_result_dict['worker_id']
        self.organization_id = search_result_dict['organization_id']
