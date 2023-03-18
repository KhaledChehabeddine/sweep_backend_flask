from flask import current_app
from flask_pymongo import PyMongo
from werkzeug.local import LocalProxy

database = None


def get_database():
    global database
    if database is None:
        database = PyMongo(current_app).db
    return database


mongodb_client = LocalProxy(get_database())
