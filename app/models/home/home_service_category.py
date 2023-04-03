"""Home Service Category Model

A home service category model used to convert a home service category document into a home service category object
"""

from typing import List
from app.models.home.service_category_item import ServiceCategoryItem


class HomeServiceCategory:
    """
    A class to represent a home service category model

    Attributes
    ----------
    service_category_items : List[ServiceCategoryItem]
        Home service category's items


    Methods
    -------
    get_service_category_item_list() : List[ServiceCategoryItem]
        Returns the home service category's items
    set_service_category_item_list(service_category_item_list) : None
        Sets the home service category's items
    """

    def __init__(self, service_category_item_document: dict) -> None:
        self.service_category_items = service_category_item_document['service_category_items']

    def get_service_category_item_list(self) -> List[ServiceCategoryItem]:
        """
        :return: Home service category's items
        """
        return self.service_category_items

    def set_service_category_item_list(self, service_category_items: list) -> None:
        """
        :param service_category_items: Home service category's items
        """
        self.service_category_items = service_category_items
