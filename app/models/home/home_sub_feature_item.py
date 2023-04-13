"""Summary: Home Sub Feature Item Model

A home sub feature item model used to convert a home sub feature item document into a home sub feature item object
"""

from typing import List
from app.models.utilities.category import Category
from app.models.utilities.review import Review


class HomeSubFeatureItem:
    """
    A class to represent a home sub feature item model


    Attributes
    ----------
    categories : List[Category]
        Home sub feature item's categories
    description : str
        Home sub feature item's description
    flags : List[str]
        Home sub feature item's flags
    _id : str
        Home sub feature item's id
    image : str
        Home sub feature item's image
    location: str
        Home sub feature item's location
    rating : int
        Home sub feature item's rating
    reviews : List[Review]
        Home sub feature item's reviews
    service_id : int
        home sub feature item's id
    title : str
        Home sub feature item's title

    Methods
    -------
    get_categories() : List[Category]
        Returns the home sub feature item's categories
    set_categories) : None
        Sets the home sub feature item's categories
    get_description() : str
        Returns the home sub feature item's description
    set_description(description) : None
        Sets the home sub feature item's description
    get_flags() : List[str]
        Returns the home sub feature item's flags
    set_flags(flags) : None
        Sets the home sub feature item's flags
    get_id() : str
        Returns the home sub feature item's id
    set_id(_id) : None
        Sets the home sub feature item's id
    get_image() : str
        Returns the home sub feature item's image
    set_image(image) : None
        Sets the home sub feature item's image
    get_location() : str
        Returns the home sub feature item's location
    set_location(location) : None
        Sets the home sub feature item's location
    get_rating() : float
        returns the home sub feature item's rating
    set_rating(rating): float
        Sets the home sub feature item's rating
    get_reviews() : List[Review]
        Returns the home sub feature item's reviews
    set_reviews(reviews) : None
        Sets the home sub feature item's reviews
    get_service_id() : int
        Returns the id of the sub feature item
    set_service_id(service_id) : none
        Sets the id of the sub feature item
    get_title() : str
        Returns the home sub feature item's title
    set_title(title) : None
        Sets the home sub feature item's title
    """

    def __init__(self, home_sub_feature_item_document: dict) -> None:
        self.categories = home_sub_feature_item_document['categories']
        self.description = home_sub_feature_item_document['description']
        self.flags = home_sub_feature_item_document['flags']
        self._id = home_sub_feature_item_document['_id']
        self.image = home_sub_feature_item_document['image']
        self.location = home_sub_feature_item_document['location']
        self.rating = home_sub_feature_item_document['rating']
        self.reviews = home_sub_feature_item_document['reviews']
        self.service_id = home_sub_feature_item_document['service_id']
        self.title = home_sub_feature_item_document['title']

    def get_categories(self) -> List[Category]:
        """
        :return: Home sub feature item's categories
        """
        return self.categories

    def set_categories(self, categories: List[Category]) -> None:
        """
        :param categories: Home sub feature item's categories
        """
        self.categories = categories

    def get_description(self) -> str:
        """
        :return: Home sub feature item's description
        """
        return self.description

    def set_description(self, description: str) -> None:
        """
        :param description: Home sub feature item's description
        """
        self.description = description

    def get_flags(self) -> List[str]:
        """
        :return: Home sub feature item's flags
        """
        return self.flags

    def set_flags(self, flags: List[str]) -> None:
        """
        :param flags: Home sub feature item's flags
        """
        self.flags = flags

    def get_id(self) -> str:
        """
        :return: Home sub feature item's id
        """
        return self._id

    def set_id(self, _id: str) -> None:
        """
        :param _id: Home sub feature item's id
        """
        self._id = _id

    def get_image(self) -> str:
        """
        :return: Home sub feature item's image
        """
        return self.image

    def set_image(self, image: str) -> None:
        """
        :param image: Home sub feature item's image
        """
        self.image = image

    def get_location(self) -> str:
        """
        :return: Home sub feature item's location
        """
        return self.location

    def set_location(self, location: str) -> None:
        """
        :param location: Home sub feature item's location
        """
        self.location = location

    def get_rating(self) -> float:
        """
        :return: Home sub feature item's rating
        """
        return self.rating

    def set_rating(self, rating: float) -> None:
        """
        :param rating: Home sub feature item's rating
        """
        self.rating = rating

    def get_reviews(self) -> List[Review]:
        """
        :return: Home sub feature item's reviews
        """
        return self.reviews

    def set_reviews(self, reviews: List[Review]) -> None:
        """
        :param reviews: Home sub feature item's reviews
        """
        self.reviews = reviews

    def get_title(self) -> str:
        """
        gets Home sub feature item's title
        """
        return self.title

    def set_title(self, title: str) -> None:
        """
        sets Home sub feature item's title
        """
        self.title = title

    def get_service_id(self) -> int:
        """
        gets the id of the category id
        """
        return self.service_id

    def set_service_id(self, service_id: int) -> None:
        """
        sets the id of the category id
        """
        self.service_id = service_id
