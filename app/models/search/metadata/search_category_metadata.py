"""Summary: Search CategoryMetadata Model

A search metadata model used to convert a search metadata document into a user metadata object
"""

from datetime import datetime


class SearchCategoryMetadata:
    """
    A class to represent the metadata for a search category object

    Attributes
    ----------
    created_date : datetime
        The date and time the search object was created
    updated_date : datetime
        The date and time the search object was updated
    total_companies : int
        Home sub feature's total companies
    total_service_providers : int
        Home sub feature's total service providers (sum of companies and workers)
    total_workers : int
        Home sub feature's total workers
    """

    def __init__(self, search_metadata_dict: dict) -> None:
        self.created_date = datetime.strptime(search_metadata_dict['created_date'], '%Y-%m-%d %H:%M:%S')
        self.updated_date = datetime.strptime(search_metadata_dict['updated_data'], '%Y-%m-%d %H:%M:%S')
        self.total_companies = search_metadata_dict['total_companies']
        self.total_service_providers = search_metadata_dict['total_service_providers']
        self.total_workers = search_metadata_dict['total_workers']
