"""Summary: Service Provider Model

A service provider model used to convert a service provider document into a service provider object
"""
from app.models.components.metadata.service_provider_metadata import ServiceProviderMetadata


class ServiceProvider:
    """
    A class to represent a service provider model


    Attributes
    ----------
    average_rating : float
        Service provider's average rating
    category_ids : list[str]
        Service provider's category ids
    description : str
        Service provider's description
    flags : list[str]
        Service provider's flags
    metadata : dict
        Service provider's metadata document
    review_ids : list[str]
        Service provider's review ids
    service_category_ids : list[str]
        Service provider's service category ids
    service_item_ids : list[str]
        Service provider's service item ids
    """

    def __init__(self, service_provider_document: dict) -> None:
        self.average_rating = service_provider_document['average_rating']
        self.category_ids = service_provider_document['category_ids']
        self.description = service_provider_document['description']
        self.flags = service_provider_document['flags']
        self.metadata = ServiceProviderMetadata(
            service_provider_metadata_document=service_provider_document['metadata']
        ).__dict__
        self.review_ids = service_provider_document['review_ids']
        self.service_category_ids = service_provider_document['service_category_ids']
        self.service_item_ids = service_provider_document['service_item_ids']
