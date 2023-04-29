"""Summary: Category Model

A category model used to convert a category document into a category object
"""
from bson import ObjectId
from app.models.components.metadata.category_metadata import CategoryMetadata


class Category:
    """
    A class to represent a category model


    Attributes
    ----------
    _id : str
        Category's id
    metadata : dict
        Category's metadata document
    name : str
        Category's name
    service_item_ids : List[str]
        Category's service item ids
    """

    def __init__(self, category_document) -> None:
        self._id = ObjectId(category_document['_id']) if ObjectId.is_valid(category_document['_id']) else ObjectId()
        self.metadata = CategoryMetadata(category_document['metadata']).__dict__
        self.name = category_document['name']
        self.service_item_ids = category_document['service_item_ids']
