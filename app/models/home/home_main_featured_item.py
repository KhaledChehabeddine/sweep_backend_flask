"""Summary: Home Main Featured Item Model

A home main featured item model used to convert a home main featured item document into a home main featured item object
"""


class HomeMainFeaturedItem:
    """
    A class to represent a home main featured item model

    Attributes
    ----------
    image_link : str
        Home main featured item's image link

    Methods
    -------
    get_image_link() : str
        Returns the home main featured item's image link
    set_image_link(image_link) : None
        Sets the home main featured item's image link
    """

    def __init__(self, home_main_featured_item_document: dict) -> None:
        self.image_link = home_main_featured_item_document['image_link']

    def get_image_link(self) -> str:
        """
        :return: Home main featured item's image link
        """
        return self.image_link

    def set_image_link(self, image_link: str) -> None:
        """
        :param image_link: Home main featured item's image link
        """
        self.image_link = image_link
