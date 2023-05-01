"""Summary: Category Metadata Model

An category metadata model used to convert an category metadata document into an category metadata object
"""


class CategoryMetadata:
    """
    A class to represent a category metadata model

    Attributes
    ----------
    created_date : datetime
        Category's created date
    total_service_items : int
        Category's total service items
    updated_date : datetime
        Category's updated date
    """

    def __init__(self, category_metadata_document) -> None:
        self.created_date = category_metadata_document['created_date']
        self.total_service_items = int(category_metadata_document['total_service_items'])
        self.updated_date = category_metadata_document['updated_date']
