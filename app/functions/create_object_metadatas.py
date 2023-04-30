"""Summary: Create Object Metadata Functions

Functions to create metadatas for their respective object
"""
from datetime import datetime


def create_account_category_metadata(account_category_document: dict) -> dict:
    """
    :param account_category_document: An account category document
    :return: A dictionary representation of the account category metadata
    """
    return {
        'created_date': datetime.now(),
        'total_account_category_items': len(account_category_document['account_category_items']),
        'updated_date': datetime.now()
    }


def create_address_metadata(address_document: dict) -> dict:
    """
    :param address_document: An address document
    :return: A dictionary representation of the address metadata
    """
    address_document['metadata']['formatted_address'] = (
            address_document['street_address_1'] + ' ' + address_document['street_address_1'] + ' ' +
            address_document['city'] + ' ' + address_document['state'] + ' ' + address_document['country']
    )

    return address_document['metadata']


def create_category_metadata(category_document: dict) -> dict:
    """
    :param category_document: A category document
    :return: A dictionary representation of the category metadata
    """
    return {
        'created_date': datetime.now(),
        'total_service_items': len(category_document['service_item_ids']),
        'updated_date': datetime.now()
    }


def create_home_feature_metadata() -> dict:
    """
    :return: A dictionary representation of the home feature metadata
    """
    return {
        'created_date': datetime.now(),
        'updated_date': datetime.now()
    }


def create_home_main_feature_metadata(aws_s3_upload_data: dict) -> dict:
    """
    :param aws_s3_upload_data: A dictionary representation of the information about the uploaded image
    :return: A dictionary representation of the home main feature metadata
    """
    return {
        'image_format': aws_s3_upload_data['image_format'],
        'image_height': aws_s3_upload_data['image_height'],
        'image_width': aws_s3_upload_data['image_width']
    }


def create_review_metadata() -> dict:
    """
    :return: A dictionary representation of the review metadata
    """
    return {
        'created_date': datetime.now()
    }


def create_service_provider_metadata(service_provider_document: dict) -> dict:
    """
    :param service_provider_document: A service provider document
    :return: A dictionary representation of the service provider metadata
    """
    service_provider_document['metadata']['total_categories'] = len(service_provider_document['categories'])
    service_provider_document['metadata']['total_flags'] = len(service_provider_document['flags'])
    service_provider_document['metadata']['total_reviews'] = len(service_provider_document['reviews'])

    for category_document in service_provider_document['categories']:
        category_document['metadata'] = create_category_metadata(category_document=category_document)

    for review_document in service_provider_document['reviews']:
        review_document['metadata'] = create_review_metadata()

    service_provider_document['user']['metadata'] = create_user_metadata()

    for address_document in service_provider_document['user']['addresses']:
        address_document['metadata'] = create_address_metadata(address_document=address_document)

    return service_provider_document


def create_user_metadata() -> dict:
    """
    :return: A dictionary representation of the user metadata
    """
    return {
        'created_date': datetime.now(),
        'last_login_date': datetime.now(),
        'updated_date': datetime.now()
    }
