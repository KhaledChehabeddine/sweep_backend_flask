"""Summary: Service Item Metadata Model

A service item metadata model used to convert an service item metadata document into an service item metadata object
"""
from datetime import datetime


class ServiceItemMetadata:
    """
    A class to represent a service item metadata model

    Attributes
    ----------
    created_date : datetime
        Service item's created date
    image_format : str
        Service item's image format
    image_height : int
        Service item's image height
    image_width : int
        Service item's image width
    updated_date : datetime
        Service item's updated date
    """

    def __init__(self, service_item_metadata_document) -> None:
        self.created_date = self._format_datetime(service_item_metadata_document.get('created_date', None))
        self.image_format = service_item_metadata_document.get('image_format', '')
        self.image_height = service_item_metadata_document.get('image_height', 0)
        self.image_width = service_item_metadata_document.get('image_width', 0)
        self.updated_date = self._format_datetime(service_item_metadata_document.get('updated_date', None))

    @staticmethod
    def _format_datetime(date_string: str) -> str:
        if isinstance(date_string, str):
            return date_string
        if isinstance(date_string, datetime):
            return date_string.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return ''
