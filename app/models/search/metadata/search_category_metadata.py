"""Summary: Search Category Metadata Model

A search metadata model used to convert a search metadata document into a user metadata object
"""


class SearchCategoryMetadata:
    """
    A class to represent the metadata for a search category object

    Attributes
    ----------
    created_date : datetime
        Search Category's created date
    total_companies : int
        Search Category's total companies
    total_workers : int
        Search Category's total workers
    updated_date : datetime
        Search Category's updated date
    """

    def __init__(self, search_category_metadata_document: dict) -> None:
        self.created_date = search_category_metadata_document['created_date']
        self.total_companies = int(search_category_metadata_document['total_companies'])
        self.total_workers = int(search_category_metadata_document['total_workers'])
        self.updated_date = search_category_metadata_document['updated_data']
