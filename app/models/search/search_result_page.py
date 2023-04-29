"""Summary: Search Result Page Model

A search result page model used to convert a search result page document into a search result page object
"""
from app.models.search.metadata.search_result_page_metadata import SearchResultPageMetadata
from app.models.search.search_result import SearchResult


class SearchResultPage:
    """
    A class to represent a search result page object

    Attributes
    ----------
    _id : str
        The ID of the search result page object
    metadata : SearchResultPageMetadata
        The metadata for the search result page object
    search_results : List[SearchResult]
        A list of search results for the search result page
    results: List[SearchResult]
        A list of search results for the search result page
    """
    def __init__(self, search_result_page_dict: dict) -> None:
        self._id = search_result_page_dict['_id']
        self.metadata = SearchResultPageMetadata(search_result_page_dict['metadata'])
        self.search_results = search_result_page_dict['search_results']
        self.results = []
        for search_result in self.search_results:
            self.results.append(SearchResult(search_result))
