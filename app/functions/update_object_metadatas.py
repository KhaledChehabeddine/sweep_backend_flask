"""Summary: Update Object Metadata Functions

Functions to update metadatas for their respective object
"""
from datetime import datetime

from app.aws.aws_s3_client import upload_image_to_aws_s3
from app.functions.create_object_metadatas import create_address_metadata


def update_category_metadata(category_metadata_document: dict) -> dict:
    """
    :param category_metadata_document: A category metadata document
    :return: A updated category metadata document
    """
    category_metadata_document['updated_date'] = datetime.now()

    return category_metadata_document


def update_home_feature_metadata(home_feature_metadata_document: dict) -> dict:
    """
    :param home_feature_metadata_document: A home feature metadata document
    :return: A updated home feature metadata document
    """
    home_feature_metadata_document['updated_date'] = datetime.now()

    return home_feature_metadata_document


def update_service_category_metadata(service_category_document: dict) -> dict:
    """
    :param service_category_document: A service category document
    :return: A updated service category document
    """
    if service_category_document['image']:
        service_category_image = ('', service_category_document['image'], service_category_document['image_path'])
        service_category_document['metadata'] = upload_image_to_aws_s3(
            object_metadata_document=service_category_document['metadata'],
            object_image=service_category_image
        ).json['data']
    service_category_document['metadata']['updated_date'] = datetime.now()

    return service_category_document['metadata']


def update_service_provider_metadata(service_provider_document: dict) -> dict:
    """
    :param service_provider_document: A service provider document
    :return: A updated service provider document
    """
    service_provider_document['metadata']['total_categories'] = len(service_provider_document['categories'])
    service_provider_document['metadata']['total_flags'] = len(service_provider_document['flags'])
    service_provider_document['metadata']['total_reviews'] = len(service_provider_document['reviews'])

    for category_document in service_provider_document['categories']:
        category_document['metadata'] = \
            update_category_metadata(category_metadata_document=category_document['metadata'])

    service_provider_document['user']['metadata'] = \
        update_user_metadata(user_metadata_document=service_provider_document['user']['metadata'])

    for address_document in service_provider_document['user']['addresses']:
        address_document['metadata'] = create_address_metadata(address_document=address_document)

    return service_provider_document


def update_user_metadata(user_metadata_document: dict) -> dict:
    """
    :param user_metadata_document: A user metadata document
    :return: A updated user metadata document
    """
    user_metadata_document['updated_date'] = datetime.now()

    return user_metadata_document
