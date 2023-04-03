"""Home sub feature model

A home sub feature model used to convert a home sub feature document into a home sub feature object
"""


from typing import List

from app.models.homepage.home_sub_feature_item import HomeSubFeatureItem


class HomeSubFeature:
    """
    A class to represent a home sub feature model


    Attributes
    ----------
    sub_title : str
        home sub feature's sub_title
    title : str
        home sub feature's title

    home_sub_feature_items : List[HomeSubFeatureItem]
        home sub feature's items

    Methods
    -------
    get_home_sub_feature_items() : List[HomeSubFeatureItem]
        Returns the home sub feature's items

    set_home_sub_feature_items(home_sub_feature_items) : None
        Sets the home sub feature's items

    get_sub_title() : str
        Returns the home sub feature's sub_title

    set_sub_title(sub_title) : None
        Sets the home sub feature's sub_title

    get_title() : str

        Returns the home sub feature's title

    set_title(title) : None
        Sets the home sub feature's title
    """

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
        :return: home sub feature's sub_title
        """
        return self.sub_title

    def set_sub_title(self, sub_title: str) -> None:
        """
        :param sub_title: home sub feature's sub title
        """
        self.sub_title = sub_title

    def get_title(self) -> str:
        """
        :return: home sub feature's title
        """
        return self.title
