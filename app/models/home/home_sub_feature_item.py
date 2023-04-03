"""Summary: Home Sub Feature Item Model

A home sub feature item model used to convert a home sub feature item document into a home sub feature item object
"""


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
    """

    def __init__(self, home_sub_feature_item_document: dict) -> None:
        self.description = home_sub_feature_item_document['description']
        self.image = home_sub_feature_item_document['image']
        self.title = home_sub_feature_item_document['title']

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

    def get_title(self) -> str:
        """
        :return: Home sub feature item's title
        """
        return self.title

    def set_title(self, title: str) -> None:
        """
        :param title: Home sub feature item's title
        """
        self.title = title
