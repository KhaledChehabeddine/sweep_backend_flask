import os
from pymongo import MongoClient

CONNECTION_STRING = 'mongodb+srv://admin:' + os.getenv('ATLAS_MONGODB_PASSWORD') + '@cluster0.zahtuza.mongodb.net' \
                                                                                   '/?retryWrites=true&w=majority'

database = None
mongodb_client = None


def get_database():
    global database
    if database is None:
        database = get_mongodb_client()['sweep_db']
    return database


def get_mongodb_client():
    global mongodb_client
    if mongodb_client is None:
        mongodb_client = MongoClient(CONNECTION_STRING)
    return mongodb_client
