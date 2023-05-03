"""Summary: Search Metadata Model

A search metadata model used to convert a search metadata document into a user metadata object
"""


class SearchMetadata:
    """
    A class to represent the metadata for a search object

    Attributes
    ----------
    created_date : datetime
        Search's created date
    updated_date : datetime
        Search's updated date
    total_search_results : int
        Search's total search results
    """

    def __init__(self, search_metadata_document: dict) -> None:
        self.created_date = search_metadata_document['created_date']
        self.updated_date = search_metadata_document['updated_date']
        self.total_search_results = int(search_metadata_document['total_search_results'])
