"""Summary: Service Provider Model

A service provider model used to convert a service provider document into a service provider object
"""
from app.models.components.category import Category
from app.models.components.review import Review
from app.models.user.metadata.service_provider_metadata import ServiceProviderMetadata
from app.models.user.user import User


class ServiceProvider:
    """
    A class to represent a service provider model


    Attributes
    ----------
    average_rating : float
        Service provider's average rating
    categories : list[dict]
        Service provider's category documents
    description : str
        Service provider's description
    flags : list[str]
        Service provider's flag documents
    metadata : dict
        Service provider's metadata document
    reviews : list[dict]
        Service provider's review documents
    service_provider_type : str
        Service provider's type (company or worker)
    user : dict
        Service provider's user document
    """

    def __init__(self, service_provider_document: dict) -> None:
        self.average_rating = float(service_provider_document['average_rating'])
        self.categories = [
            Category(category_document=category_document).__dict__
            for category_document in service_provider_document['categories']
        ]
        self.description = str(service_provider_document['description'])
        self.flags = [str(flag) for flag in service_provider_document['flags']]
        self.metadata = ServiceProviderMetadata(
            service_provider_metadata_document=service_provider_document['metadata']
        ).__dict__
        self.reviews = [
            Review(review_document=review_document).__dict__ for review_document in service_provider_document['reviews']
        ]
        self.service_provider_type = str(service_provider_document['service_provider_type'])
        self.user = User(user_document=service_provider_document['user']).__dict__
