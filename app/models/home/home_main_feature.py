"""Summary: Home Main Featured Model

A home main featured model used to convert a home main featured document into a home main featured object
"""

from typing import List
from app.models.home.home_main_feature_item import HomeMainFeatureItem


class HomeMainFeature:
    """
    A class to represent a home main featured model


    Attributes
    ----------
    home_main_feature_items : List[HomeMainFeatureItem]
        Home main feature's items
    _id : str
        Home main feature's id

    Methods
    -------
    get_home_main_feature_items() : List[HomeMainFeatureItem]
        Returns the home main feature's items
    set_home_main_feature_items(home_main_feature_items) : None
        Sets the home main feature's items
    get_id() : str
        Returns the home main feature's id
    set_id(_id) : None
        Sets the home main feature's id
    """

    def __init__(self, home_main_feature_document: dict) -> None:
        self.home_main_feature_items = home_main_feature_document['home_main_feature_items']
        self._id = home_main_feature_document['_id']

    def get_home_main_featured_items(self) -> List[HomeMainFeatureItem]:
        """
        :return: Home main feature's items
        """
        return self.home_main_feature_items

    def set_home_main_featured_items(self, home_main_feature_items: List[HomeMainFeatureItem]) -> None:
        """
        :param home_main_feature_items: Home main feature's items
        """
        self.home_main_feature_items = home_main_feature_items

    def get_id(self) -> str:
        """
        :return: Home main feature's id
        """
        return self._id

    def set_id(self, _id: str) -> None:
        """
        :param _id: Home main feature's id
        """
        self._id = _id
