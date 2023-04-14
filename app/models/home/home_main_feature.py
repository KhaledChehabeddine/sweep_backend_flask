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
    """

    def __init__(self, home_main_feature_document: dict) -> None:
        self.home_main_feature_items = home_main_feature_document['home_main_feature_items']
        self._id = home_main_feature_document['_id']

    def create_dict(self) -> dict:
        """
        :return: Home main feature's dict (without _id)
        """
        return {
            'home_main_feature_items': self.home_main_feature_items
        }
