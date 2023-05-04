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
    total_reviews : int
        Service provider's total reviews
    """

    def __init__(self, service_provider_metadata_document: dict) -> None:
        self.total_categories = int(service_provider_metadata_document['total_categories'])
        self.total_reviews = int(service_provider_metadata_document['total_reviews'])
