"""Summary: Search Result Model

A Search Result model used to convert a search result document into a search result object
"""
from app.models.search.metadata.search_result_metadata import SearchResultMetadata


class SearchResult:
    """
    A class to represent a search result object

    Attributes:
    ----------
    _id : str
        Search Result's ID
    metadata : SearchResultMetadata
        Search Result's metadata
    relevance_score : float
        Search Result's relevance score that indicates how well the search result matches the query
    service_provider_id : str
        Search Result's service provider ID
    service_provide_type : str
        Search Result's service provider type

    """

    def __init__(self, search_result_document: dict) -> None:
        self._id = str(search_result_document['_id'])
        self.metadata = SearchResultMetadata(
            search_result_metadata_document=search_result_document['metadata']
        ).__dict__
        self.relevance_score = float(search_result_document['relevance_score'])
        self.service_provider_type = str(search_result_document['service_provider_type'])
        self.service_provider_id = str(search_result_document['service_provider_id'])

    def database_dict(self) -> dict:
        """
        :return: Search Result's dictionary for creating a document (without _id)
        """
        return {
            '_id': self._id,
            'metadata': self.metadata,
            'relevance_score': self.relevance_score,
            'service_provider_type': self.service_provider_type,
            'service_provider_id': self.service_provider_id
        }
