"""Summary: Database Configurator

Creates a mongodb client, using CONNECTION_STRING, which is used to connect to the project database(s). Connection is
only made once to avoid unnecessary overhead.
"""

import os
from typing import Any, Mapping
from pymongo import MongoClient
from pymongo.database import Database

CONNECTION_STRING = 'mongodb+srv://admin:' + os.getenv('ATLAS_MONGODB_PASSWORD') + '@cluster0.zahtuza.mongodb.net' \
                                                                                   '/?retryWrites=true&w=majority'


def get_mongodb_client() -> MongoClient[Mapping[str, Any]]:
    """
    :return: MongoDB Client instance
    """
    return MongoClient(CONNECTION_STRING)


def get_database() -> Database[Mapping[str, Any]]:
    """
    :return: Database instance
    """
    return get_mongodb_client()['sweep_db']


database = get_database()
