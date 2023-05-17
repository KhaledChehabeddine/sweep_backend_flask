
"""Summary: User Metadata Model

A user metadata model used to convert a user metadata document into a user metadata object
"""
from datetime import datetime
from typing import Any


class UserMetadata:
    """
    A class to represent a user metadata model

    Attributes
    ----------
    created_date : datetime
        User's created date
    last_login_date : datetime
        User's last login date
    updated_date : datetime
        User's updated date
    """

    def __init__(self, user_metadata_document: dict) -> None:
        self.created_date = str(self._format_datetime(user_metadata_document.get('created_date', None)))
        self.last_login_date = str(self._format_datetime(user_metadata_document.get('last_login_date', None)))
        self.updated_date = str(self._format_datetime(user_metadata_document.get('updated_date', None)))

    @staticmethod
    def _format_datetime(date_string: Any) -> str:
        if isinstance(date_string, str):
            return date_string
        if isinstance(date_string, datetime):
            return date_string.strftime('%Y-%m-%dT%H:%M:%S.%f')
        else:
            return ''
