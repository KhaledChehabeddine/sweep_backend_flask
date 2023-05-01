"""Summary: Search CategoryMetadata Model

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
    total_service_providers : int
        Search Category's total service providers
    total_workers : int
        Search Category's total workers
    updated_date : datetime
        Search Category's updated date
    """

    def __init__(self, search_metadata_dict: dict) -> None:
        self.created_date = search_metadata_dict['created_date']
        self.total_companies = int(search_metadata_dict['total_companies'])
        self.total_service_providers = int(search_metadata_dict['total_service_providers'])
        self.total_workers = int(search_metadata_dict['total_workers'])
        self.updated_date = search_metadata_dict['updated_data']
