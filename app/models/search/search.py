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
    search_results : List[SearchResult]
        Search object's search results
    """

    def __init__(self, search_document: dict) -> None:
        self._id = str(search_document['_id'])
        self.metadata = SearchMetadata(
            search_metadata_document=search_document['metadata']
        ).__dict__
        self.query = str(search_document['query'])
        self.search_results = [str(search_result_id) for search_result_id in search_document['search_results']]

    def database_dict(self) -> dict:
        """
        :return: Search's dictionary for creating a document (without _id)
        """
        return {
            '_id': self._id,
            'metadata': self.metadata,
            'query': self.query,
            'search_results': self.search_results
        }
