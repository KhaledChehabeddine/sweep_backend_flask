"""Summary: Category Model

A category model used to convert a category document into a category object
"""

from typing import List
from app.models.utilities.service_item import ServiceItem


class Category:
    """
    A class to represent a category model

    Attributes
    ----------
    _id : str
        Category's id
    name : str
        Category's name
    services : List[Service]
        Category's services
    """

    def __init__(self, category_document) -> None:
        self._id = category_document['_id']
        self.name = category_document['name']
        self.services = category_document['services']

    def create_dict(self) -> dict:
        """
        :return: Category's dictionary representation
        """
        return {
            'name': self.name,
            'services': self.services
        }
