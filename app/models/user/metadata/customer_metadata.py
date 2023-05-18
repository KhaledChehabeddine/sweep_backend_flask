"""Summary: User Metadata Model

A customer metadata model used to convert a customer metadata document into a customer metadata object
"""
from datetime import datetime
from typing import Any


class CustomerMetadata:
    """
    A class to represent a customer metadata model

    Attributes:
    ----------
    created_date : datetime
        Customer's created date
    """

    def __init__(self, customer_metadata_document: dict) -> None:
        self.created_date = self._format_datetime(customer_metadata_document.get('created_date', None))

    @staticmethod
    def _format_datetime(date_string: Any) -> str:
        if isinstance(date_string, str):
            return date_string
        if isinstance(date_string, datetime):
            return date_string.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return ''
