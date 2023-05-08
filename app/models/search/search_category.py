"""Summary: Search Category Model

A search category model used to convert a search category document into a search category object
"""
from app.models.search.metadata.search_category_metadata import SearchCategoryMetadata


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
    tags :List[str]
        Search Category's tags associated with the category name
    worker_ids : List[str]
        Search Category's total workers associated with the category name
    """

    def __init__(self, search_category_document: dict) -> None:
        self.company_ids = [str(company_id) for company_id in search_category_document['company_ids']]
        self.category_name = str(search_category_document['category_name'])
        self._id = str(search_category_document['_id'])
        self.metadata = SearchCategoryMetadata(
            search_category_metadata_document=search_category_document['metadata']
        ).__dict__
        self.tags = [str(tag) for tag in search_category_document['tags']]
        self.worker_ids = [str(worker_id) for worker_id in search_category_document['worker_ids']]

    def database_document(self) -> dict:
        """
        :return: Home main feature reward's dictionary for creating a document (without _id)
        """
        return {
            'category_name': self.category_name,
            'company_ids': self.company_ids,
            'metadata': self.metadata,
            'tags': self.tags,
            'worker_ids': self.worker_ids
        }
