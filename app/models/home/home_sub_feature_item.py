"""Summary: Home Sub Feature Item Model

A home sub feature item model used to convert a home sub feature item document into a home sub feature item object
"""
from typing import List

from app.models.utils.category import Category
from app.models.utils.review import Review


class HomeSubFeatureItem:
    """
    A class to represent a home sub feature item model


    Attributes
    ----------
    description : str
        Home sub feature item's description
    image : str
        Home sub feature item's image
    title : str
        Home sub feature item's title
    rating : int
        Home sub feature item's rating
    reviews : List[Review]
        Home sub feature item's reviews
    location: str
        Home sub feature item's location
    flags : List[str]
        Home sub feature item's flags
    categories : List[Category]
        Home sub feature item's categories
    item_id : int
        home sub feature item's id

    Methods
    -------
    get_description() : str
        Returns the home sub feature item's description
    set_description(description) : None
        Sets the home sub feature item's description
    get_image() : str
        Returns the home sub feature item's image
    set_image(image) : None
        Sets the home sub feature item's image
    get_title() : str
        Returns the home sub feature item's title
    set_title(title) : None
        Sets the home sub feature item's title
    get_rating() : float
        returns the home sub feature item's rating
    set_rating(rating): float
        Sets the home sub feature item's rating
    get_reviews() : List[Review]
        Returns the home sub feature item's reviews
    set_reviews(reviews) : None
        Sets the home sub feature item's reviews
    get_location() : str
        Returns the home sub feature item's location
    set_location(location) : None
        Sets the home sub feature item's location
    get_flags() : List[str]
        Returns the home sub feature item's flags
    set_flags(flags) : None
        Sets the home sub feature item's flags
    get_categories() : List[Category]
        Returns the home sub feature item's categories
    set_categories) : None
        Sets the home sub feature item's categories
    get_item_id() : int
        Returns the id of the sub feature item
    set_item_id(item_id) : none
        Sets the id of the sub feature item
    """

    def __init__(self, home_sub_feature_item_document: dict) -> None:
        self.description = home_sub_feature_item_document['description']
        self.image = home_sub_feature_item_document['image']
        self.title = home_sub_feature_item_document['title']
        self.rating = home_sub_feature_item_document['rating']
        self.reviews = home_sub_feature_item_document['reviews']
        self.location = home_sub_feature_item_document['location']
        self.flags = home_sub_feature_item_document['flags']
        self.categories = home_sub_feature_item_document['categories']
        self.item_id = home_sub_feature_item_document['item_id']

    def get_description(self) -> str:
        """
        gets Home sub feature item's description
        """
        return self.description

    def set_description(self, description: str) -> None:
        """
        sets Home sub feature item's description
        """
        self.description = description

    def get_image(self) -> str:
        """
        gets Home sub feature item's image
        """
        return self.image

    def set_image(self, image: str) -> None:
        """
        sets image: Home sub feature item's image
        """
        self.image = image

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

    def get_rating(self) -> float:
        """
        gets rating of the sub feature item
        """
        return self.rating

    def set_rating(self, rating: float) -> None:
        """
        sets the rating of the sub feature item
        """
        self.rating = rating

    def get_reviews(self) -> List[Review]:
        """
        gets reviews of the sub feature item
        """
        return self.reviews

    def set_reviews(self, reviews: List[Review]) -> None:
        """
        sets reviews of the sub feature item
        """
        self.reviews = reviews

    def get_location(self) -> str:
        """
        gets location of the sub feature item (string of coordinates/link)
        """
        return self.location

    def set_location(self, location: str) -> None:
        """
        sets the location of the sub feature item (string of coordinates/link)
        """
        self.location = location

    def get_flags(self) -> List[str]:
        """
        gets flags of the sub feature item
        """
        return self.flags

    def set_flags(self, flags: List[str]) -> None:
        """
        sets flag of the sub feature item
        """
        self.flags = flags

    def get_categories(self) -> List[Category]:
        """
        gets a list of categories
        """
        return self.categories

    def set_categories(self, categories: List[Category]) -> None:
        """
        sets the categories
        """
        self.categories = categories

    def get_item_id(self) -> int:
        """
        gets the id of the category id
        """
        return self.item_id

    def set_item_id(self, item_id: int) -> None:
        """
        sets the id of the category id
        """
        self.item_id = item_id
