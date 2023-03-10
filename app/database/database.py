from flask import g, current_app
from flask_pymongo import PyMongo
from werkzeug.local import LocalProxy


def get_database():
    """
    Initialize the MongoDB Client globally, reducing the number of connections to improve performance.
    """
    database = getattr(g, '_database', None)
    if database is None:
        database = g._database = PyMongo(current_app).db
    return database


mongodb_client = LocalProxy(get_database())
