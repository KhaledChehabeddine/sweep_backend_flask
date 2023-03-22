import os
from pymongo import MongoClient

CONNECTION_STRING = 'mongodb+srv://admin:' + os.getenv('ATLAS_MONGODB_PASSWORD') + '@cluster0.zahtuza.mongodb.net' \
                                                                                   '/?retryWrites=true&w=majority'

database = None
mongo_client = None


def get_database():
    global database
    if database is None:
        database = get_mongo_client()['student_db']
    return database


def get_mongo_client():
    global mongo_client
    if mongo_client is None:
        mongo_client = MongoClient(CONNECTION_STRING, retryWrites=True, retryReads=True)
    return mongo_client
