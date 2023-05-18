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
        self.created_date = self._format_datetime(home_feature_metadata_document.get('created_date', None))
        self.updated_date = self._format_datetime(home_feature_metadata_document.get('updated_date', None))

    @staticmethod
    def _format_datetime(date_string: str) -> str:
        if isinstance(date_string, str):
            return date_string
        if isinstance(date_string, datetime):
            return date_string.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return ''
