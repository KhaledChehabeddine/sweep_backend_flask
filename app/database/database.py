from flask import current_app
from flask_pymongo import PyMongo
from werkzeug.local import LocalProxy

database = None
mongodb_client = None


def initialize_database(application):
    global database
    database = PyMongo(application).db


def get_database():
    global database
    return database


def get_mongodb_client():
    global mongodb_client
    if mongodb_client is None:
        mongodb_client = LocalProxy(get_database())
    return mongodb_client
