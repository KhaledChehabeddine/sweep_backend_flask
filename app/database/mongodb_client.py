"""Database Configurator

Initializes a mongodb client using CONNECTION_STRING only once to avoid unnecessary overhead
"""
import os
from typing import Any, Mapping
from pymongo import MongoClient

CONNECTION_STRING = 'mongodb+srv://admin:' + os.getenv('ATLAS_MONGODB_PASSWORD') + '@cluster0.zahtuza.mongodb.net' \
                                                                                   '/?retryWrites=true&w=majority'
MONGODB_CLIENT = None


def get_mongodb_client() -> MongoClient[Mapping[str, Any]]:
    """
    :return: MongoDB Client instance
    """
    global MONGODB_CLIENT
    if MONGODB_CLIENT is None:
        MONGODB_CLIENT = MongoClient(CONNECTION_STRING)
    return MONGODB_CLIENT
