"""Summary: Search Category Model

A search category model used to convert a search category document into a search category object
"""


class SearchCategory:
    """
    A class to represent a search category object

    Attributes
    ----------
    company_ids : List[str]
        Search Category's total companies associated with the category name
    category_name : str
        Search Category's name
    _id : str
        Search Category's ID
    metadata : SearchCategoryMetadata
        The metadata for the search category object
    service_providers_ids : List[str]
        Search Category's total service providers associated with the category name
    tags :List[str]
        Search Category's tags associated with the category name
    worker_ids : List[str]
        Search Category's total workers associated with the category name
    """

    def __init__(self, search_category_dict: dict) -> None:
        self.company_ids = [str(company_id) for company_id in search_category_dict['company_ids']]
        self.category_name = str(search_category_dict['category_name'])
        self._id = str(search_category_dict['_id'])
        self.metadata = SearchCategory(search_category_dict['metadata'])
        self.service_providers_ids = [str(service_provider_id) for service_provider_id in search_category_dict[
            'service_providers_ids']]
        self.tags = [str(tag) for tag in search_category_dict['tags']]
        self.worker_ids = [str(worker_id) for worker_id in search_category_dict['worker_ids']]
