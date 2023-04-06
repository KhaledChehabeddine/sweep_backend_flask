"""Summary: Home Main Featured Model

A home main featured model used to convert a home main featured document into a home main featured object
"""

from typing import List
from app.models.home.home_main_feature_item import HomeMainFeaturedItem


class HomeMainFeatured:
    """
    A class to represent a home main featured model

    Attributes
    ----------
    home_main_featured_items : List[HomeMainFeaturedItem]
        Home main feature's items

    Methods
    -------
    get_home_main_featured_items() : List[HomeMainFeaturedItem]
        Returns the home main feature's items
    set_home_main_featured_items(home_main_featured_items) : None
        Sets the home main feature's items
    """

    def __init__(self, home_main_featured_document: dict) -> None:
        self.home_main_featured_items = home_main_featured_document['home_main_featured_items']

    def get_home_main_featured_items(self) -> List[HomeMainFeaturedItem]:
        """
        :return: Home main feature's items
        """
        return self.home_main_featured_items

    def set_home_main_featured_items(self, home_main_featured_items: List[HomeMainFeaturedItem]) -> None:
        """
        :param home_main_featured_items: Home main feature's items
        """
        self.home_main_featured_items = home_main_featured_items
