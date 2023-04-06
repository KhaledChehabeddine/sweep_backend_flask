"""Summary: Category Model

A category model used to convert a category document into a category object
"""

from typing import List
from app.models.utils.service import Service


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

    Methods
    -------
    get_id() : str
        Returns the category's id
    set_id(_id) : None
        Sets the category's id
    get_name() : str
        Returns the category's name
    set_name(name) : None
        Sets the category's name
    get_services() : List[Service]
        Returns the category's services
    set_services(services) : None
        Sets the category's services
    """

    def __init__(self, category_document) -> None:
        self._id = category_document['_id']
        self.name = category_document['name']
        self.services = category_document['services']

    def get_id(self) -> str:
        """
        :return: Category's id
        """
        return self._id

    def set_id(self, _id: str) -> None:
        """
        :param _id: Category's id
        """
        self._id = _id

    def get_name(self) -> str:
        """
        :return: Category's name
        """
        return self.name

    def set_name(self, name: str) -> None:
        """
        :param name: Category's name
        """
        self.name = name

    def get_services(self) -> List[Service]:
        """
        :return: Category's services
        """
        return self.services

    def set_services(self, services: List[Service]) -> None:
        """
        :param services: Category's services
        """
        self.services = services
