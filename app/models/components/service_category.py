"""Summary: Service Category Model

A service category model used to convert a service category document into a service category object
"""
from app.aws.aws_cloudfront_client import create_cloudfront_url
from app.models.components.metadata.service_category_metadata import ServiceCategoryMetadata


class ServiceCategory:
    """
    A class to represent a service category model

    Attributes
    ----------
    active : bool
        Service Category's active status
    _id : str
        Service Category's id
    image_path : str
        Service Category's image path
    image_url : str
        Service Category's image url
    metadata : dict
        Service Category's metadata
    name : str
        Service Category's name
    """

    def __init__(self, service_category_document: dict) -> None:
        self.active = bool(service_category_document['active'])
        self._id = str(service_category_document['_id'])
        self.image_path = str(service_category_document['image_path'])
        self.image_url = create_cloudfront_url(image_path=self.image_path)
        self.metadata = ServiceCategoryMetadata(service_category_document['metadata']).__dict__
        self.name = str(service_category_document['name'])

    def database_dict(self) -> dict:
        """
        :return: A dictionary representation of the service category object (without _id)
        """
        return {
            'active': self.active,
            'image_path': self.image_path,
            'image_url': self.image_url,
            'metadata': self.metadata,
            'name': self.name,
        }
