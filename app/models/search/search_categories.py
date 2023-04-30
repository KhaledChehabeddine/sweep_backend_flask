"""Summary: Search Category Model

A search category model used to convert a search category document into a search category object
"""


class SearchCategory:
    """
    A class to represent a search category object

    Attributes
    ----------
    company_ids : List[str]
        The IDs of the companies associated with the search category
    tag : str
        The name of the search category
    worker_ids : List[str]
        The IDs of the workers associated with the search category
    company_ids : List[str]
        The IDs of the companys associated with the search category
    service_providers_ids : List[str]
        The IDs of the service provider associated with the search category
    """

    def __init__(self, search_category_dict: dict) -> None:
        self.company_ids = search_category_dict['company_ids']
        self.metadata = SearchCategory(search_category_dict['metadata'])
        self.service_providers_ids = search_category_dict['service_provider_ids']
        self.tag = search_category_dict['tags']
        self.worker_ids = search_category_dict['worker_ids']
