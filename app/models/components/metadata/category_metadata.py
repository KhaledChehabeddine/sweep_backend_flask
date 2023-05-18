"""Summary: Category Metadata Model

An category metadata model used to convert an category metadata document into an category metadata object
"""
from datetime import datetime


class CategoryMetadata:
    """
    A class to represent a category metadata model

    Attributes
    ----------
    created_date : datetime
        Category's created date
    total_service_items : int
        Category's total service items
    updated_date : datetime
        Category's updated date
    """

    def __init__(self, category_metadata_document) -> None:
        self.created_date = self._format_datetime(category_metadata_document.get('created_date', None))
        self.total_service_items = int(category_metadata_document.get('total_service_items', 0))
        self.updated_date = self._format_datetime(category_metadata_document.get('updated_date', None))

    @staticmethod
    def _format_datetime(date_string: str) -> str:
        if isinstance(date_string, str):
            return date_string
        if isinstance(date_string, datetime):
            return date_string.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return ''
