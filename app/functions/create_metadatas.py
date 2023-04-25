"""Summary: Create Metadata Functions

Functions to create metadatas for their respective object
"""
from datetime import datetime


def create_service_provider_metadata(service_provider_document: dict) -> dict:
    """
    :param service_provider_document: A service provider document
    :return: A dictionary representation of the service provider metadata
    """
    return {
        'total_categories': len(service_provider_document['category_ids']),
        'total_flags': len(service_provider_document['flags']),
        'total_reviews': len(service_provider_document['review_ids']),
        'total_service_categories': len(service_provider_document['service_category_ids']),
        'total_service_items': len(service_provider_document['service_item_ids'])
    }


def create_user_metadata() -> dict:
    """
    :return: A dictionary representation of the user metadata
    """
    return {
        'created_date': datetime.now(),
        'last_login_date': datetime.now(),
        'updated_date': datetime.now()
    }
