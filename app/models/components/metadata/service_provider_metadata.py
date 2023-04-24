"""Summary: Service Provider Metadata Model

A service provider metadata model used to convert a service provider metadata document into a service provider metadata
object
"""


class ServiceProviderMetadata:
    """
    A class to represent a service provider metadata model


    Attributes
    ----------
    total_categories : int
        Service provider's total categories
    total_flags : int
        Service provider's total flags
    total_reviews : int
        Service provider's total reviews
    total_service_categories : int
        Service provider's total service categories
    total_service_items : int
        Service provider's total service items
    """

    def __init__(self, service_provider_metadata_document: dict) -> None:
        self.total_categories = service_provider_metadata_document['total_categories']
        self.total_flags = service_provider_metadata_document['total_flags']
        self.total_reviews = service_provider_metadata_document['total_reviews']
        self.total_service_categories = service_provider_metadata_document['total_service_categories']
        self.total_service_items = service_provider_metadata_document['total_service_items']
