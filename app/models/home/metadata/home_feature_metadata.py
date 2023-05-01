"""Summary: Home Feature Metadata Model

A home feature metadata model used to convert a home feature metadata document into a home feature metadata object
"""
from datetime import datetime


class HomeFeatureMetadata:
    """
    A class to represent a home feature metadata model


    Attributes
    ----------
    created_date : datetime
        Home feature's created date
    updated_date : datetime
        Home feature's updated date
    """

    def __init__(self, home_feature_metadata_document: dict) -> None:
        self.created_date = home_feature_metadata_document['created_date']
        self.updated_date = home_feature_metadata_document['updated_date']
