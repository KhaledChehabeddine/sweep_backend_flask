"""Summary: Service Model

A service model used to convert a service item document into a service object
"""
from app.aws.aws_cloudfront_client import create_cloudfront_url
from app.models.components.metadata.service_item_metadata import ServiceItemMetadata


class ServiceItem:
    """
    A class to represent a service model


    Attributes
    ----------
    description : str
        Service's description
    _id : str
        Service's id
    image_path : str
        Service's file path
    image_url : str
        Service's image url
    metadata : dict
        Service's metadata document
    name : str
        Service's name
    price : float
        Service's price
    """

    def __init__(self, service_item_document: dict) -> None:
        self.description = service_item_document['description']
        self._id = str(service_item_document['_id'])
        self.image_path = service_item_document['image_path']
        self.image_url = create_cloudfront_url(file_path=self.image_path)
        self.metadata = ServiceItemMetadata(service_item_document['metadata']).__dict__
        self.name = service_item_document['name']
        self.price = service_item_document['price']
