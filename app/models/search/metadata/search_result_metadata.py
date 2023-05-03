"""Summary: Search Result Metadata Model

A search result metadata model used to convert a search metadata document into a search result metadata object
"""


class SearchResultMetadata:
    """
    A class to represent the metadata for a search result object

    Attributes
    ----------
    created_date : datetime
        Search Result's created date
    updated_date : datetime
        Search Result's updated date
    """

    def __init__(self, search_result_metadata_document: dict) -> None:
        self.created_date = search_result_metadata_document['created_date']
        self.updated_date = search_result_metadata_document['updated_date']
