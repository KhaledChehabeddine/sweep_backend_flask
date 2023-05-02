"""Summary: Category Model

A category model used to convert a category document into a category object
"""
from bson import ObjectId
from app.models.components.metadata.category_metadata import CategoryMetadata
from app.models.components.service_item import ServiceItem


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
    service_items : List[dict]
        Category's service item documents
    """

    def __init__(self, category_document) -> None:
        self._id = ObjectId(category_document['_id']) if ObjectId.is_valid(category_document['_id']) else ObjectId()
        self.metadata = CategoryMetadata(category_document['metadata']).__dict__
        self.name = str(category_document['name'])
        self.service_items = [ServiceItem(service_item).__dict__ for service_item in category_document['service_items']]
