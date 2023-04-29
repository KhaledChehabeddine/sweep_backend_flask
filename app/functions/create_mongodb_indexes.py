"""Summary: Create MongoDB Indexes Functions

Functions to create indexes for their respective collections
"""
from typing import Mapping, Any
import pymongo
from pymongo.collection import Collection


def create_service_provider_indexes(service_provider_collection: Collection[Mapping[str, Any]]) -> None:
    """
    :param service_provider_collection: A service provider collection
    """
    service_provider_collection.create_index([('service_provider.category._id', pymongo.ASCENDING)], unique=True)
    service_provider_collection.create_index([('service_provider.review._id', pymongo.ASCENDING)], unique=True)
    service_provider_collection.create_index([('service_provider.user.email', pymongo.ASCENDING)], unique=True)
    service_provider_collection.create_index([('service_provider.user.phone_number', pymongo.ASCENDING)], unique=True)
    service_provider_collection.create_index([('service_provider.user.username', pymongo.ASCENDING)], unique=True)
