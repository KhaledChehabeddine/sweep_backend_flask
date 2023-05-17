"""Summary: Create Object Metadata Functions

Functions to create metadata for their respective object
"""
from datetime import datetime
from app.aws.aws_s3_client import upload_image_to_aws_s3


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
    for service_item_document in category_document['service_items']:
        service_item_document['metadata'] = create_service_item_metadata(service_item_document=service_item_document)

    return {
        'created_date': datetime.now(),
        'total_service_items': len(category_document['service_items']),
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


def create_home_main_feature_metadata(home_main_feature_document: dict) -> dict:
    """
    :param home_main_feature_document: A home main feature document
    :return: A home main feature document with configured metadata
    """
    if home_main_feature_document['image']:
        home_main_feature_image = (
            '',
            home_main_feature_document['image'],
            home_main_feature_document['image_path']
        )
        home_main_feature_document['metadata'] = upload_image_to_aws_s3(
            object_metadata_document=home_main_feature_document['metadata'],
            object_image=home_main_feature_image
        ).json['data']

    return home_main_feature_document


def create_review_metadata() -> dict:
    """
    :return: A dictionary representation of the review metadata
    """
    return {
        'created_date': datetime.now()
    }


def create_search_metadata(search_document) -> dict:
    """
    :return: A dictionary representation of the search metadata
    """
    return {
        'created_date': datetime.now(),
        'total_search_results': len(search_document['search_results']),
    }


def create_service_category_metadata(service_category_document: dict) -> dict:
    """
    :param service_category_document: A service category document
    :return: A dictionary representation of the service category metadata
    """
    if service_category_document['image']:
        service_category_image = ('', service_category_document['image'], service_category_document['image_path'])
        service_category_document['metadata'] = upload_image_to_aws_s3(
            object_metadata_document=service_category_document['metadata'],
            object_image=service_category_image
        ).json['data']
    try:
        if service_category_document['metadata']['created_date']:
            pass
    except KeyError:
        service_category_document['metadata']['created_date'] = datetime.now()
    service_category_document['metadata']['updated_date'] = datetime.now()

    return service_category_document['metadata']


def create_service_provider_metadata(service_provider_document: dict) -> dict:
    """
    :param service_provider_document: A service provider document
    :return: A dictionary representation of the service provider metadata
    """
    service_provider_document['metadata']['total_categories'] = len(service_provider_document['categories'])
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


def create_search_category_metadata(search_category_document: dict) -> dict:
    """
    :return: A dictionary representation of the search category metadata
    """
    return {
        'created_date': datetime.now(),
        'updated_date': datetime.now(),
        'total_companies': len(search_category_document['company_ids']),
        'total_workers': len(search_category_document['worker_ids'])
    }


def create_search_result_category_metadata():
    """
    :return: A dictionary representation of the search result category metadata
    """
    return {
        'created_date': datetime.now(),
        'updated_date': datetime.now()
    }


def create_service_item_metadata(service_item_document: dict) -> dict:
    """
    :param service_item_document: A service item document
    :return: A dictionary representation of the service item metadata
    """
    service_item_image = ('', service_item_document['image'], service_item_document['image_path'])
    service_item_document['metadata'] = upload_image_to_aws_s3(
        object_metadata_document=service_item_document['metadata'],
        object_image=service_item_image
    ).json['data']
    service_item_document['metadata']['created_date'] = datetime.now()
    service_item_document['metadata']['updated_date'] = datetime.now()

    return service_item_document['metadata']
