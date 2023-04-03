"""

"""
from typing import List

from app.models.homepage.home_sub_feature_item import HomeSubFeatureItem


class HomeSubFeature:

    def __init__(self, home_sub_feature_document: dict) -> None:
        self.sub_title = home_sub_feature_document['sub_title']
        self.title = home_sub_feature_document['title']
        self.home_sub_feature_items= home_sub_feature_document['home_sub_feature_items']

    def get_home_sub_feature_items(self) -> List[HomeSubFeatureItem]:
        """
        :return: home sub feature's items
        """
        return self.home_sub_feature_items

    def set_home_sub_feature_items(self, home_sub_feature_items: List[HomeSubFeatureItem]) -> None:
        """
        :param home_sub_feature_items: home sub feature's items
        """
        self.home_sub_feature_items = home_sub_feature_items

    def get_sub_title(self) -> str:

        """
        :return: home sub feature's sub title
        """
        return self.sub_title

    def set_sub_title(self, sub_title: str) -> None:
        """
        :param sub_title: home sub feature's sub title
        """
        self.sub_title = sub_title

    def get_title(self) -> str:
