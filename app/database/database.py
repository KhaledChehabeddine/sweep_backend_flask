"""Summary: Database Initializer

Initializes a database using a mongodb client only once to avoid unnecessary overhead
"""
from typing import Any, Mapping
from pymongo.database import Database
from app.database.mongodb_client import get_mongodb_client

DATABASE = None


def get_database() -> Database[Mapping[str, Any]]:
    """
    :return: Database instance
    """
    global DATABASE
    if DATABASE is None:
        DATABASE = get_mongodb_client()['sweep_db']
    return DATABASE
