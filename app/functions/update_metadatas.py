"""Summary: Update Metadata Functions

Functions to update metadatas for their respective object
"""
from datetime import datetime


def update_user_metadata(user_metadata_document: dict) -> dict:
    """
    :param user_metadata_document: A user metadata document
    :return: A dictionary representation of the user metadata
    """
    return {
        'created_date': user_metadata_document['created_date'],
        'last_login_date': user_metadata_document['last_login_date'],
        'updated_date': datetime.now()
    }
