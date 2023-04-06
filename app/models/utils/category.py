"""Summary: Category Document
    A category model used to convert a category document into a category object
"""
from typing import List

from app.models.utils.service import Service


class Category:
    """
    class to represent the category model

    Attributes
    ----------
    name : str
        category item's name
    service : List[Service]
        category item's services
    category_id : int
        category item's id

    Methods
    -------
    get_name() : str
        Returns the name of the category item
    set_name(name) : None
        Sets the name of the category item
    get_service() : List[Service]
        Returns the service of the category item
    set_service(service) : None
        Sets the service of the category item
    get_category_id() : int
        Returns the id of the category item
    set_category_id(category_id) : none
        Sets the id of the category item
    """

    def __init__(self, category_document) -> None:
        self.name = category_document['name']
        self.service = category_document['service']
        self.category_id = category_document['category_id']

    def get_name(self) -> str:
        """
        gets the name of the category item
        """
        return self.name

    def set_name(self, name: str) -> None:
        """
        sets the name of the category item
        """
        self.name = name

    def get_services(self) -> List[Service]:
        """
        gets the service of the category item
        """
        return self.service

    def set_services(self, service: List[Service]) -> None:
        """
        sets the service of the category item
        """
        self.service = service

    def get_category_id(self) -> int:
        """
        gets the id of the category id
        """
        return self.category_id

    def set_category_id(self, category_id: int) -> None:
        """
        sets the id of the category id
        """
        self.category_id = category_id
