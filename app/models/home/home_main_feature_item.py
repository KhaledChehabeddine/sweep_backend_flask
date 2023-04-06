"""Summary: Home Main Featured Item Model

A home main featured item model used to convert a home main featured item document into a home main featured item object
"""


class HomeMainFeatureItem:
    """
    A class to represent a home main featured item model


    Attributes
    ----------
    _id : str
        Home main featured item's id
    image : str
        Home main featured item's image

    Methods
    -------
    get_id() : str
        Returns the home main featured item's id
    set_id(_id) : None
        Sets the home main featured item's id
    get_image() : str
        Returns the home main featured item's image
    set_image(image) : None
        Sets the home main featured item's image
    """

    def __init__(self, home_main_featured_item_document: dict) -> None:
        self._id = home_main_featured_item_document['_id']
        self.image = home_main_featured_item_document['image']

    def get_id(self) -> str:
        """
        :return: Home main featured item's id
        """
        return self._id

    def set_id(self, _id: str) -> None:
        """
        :param _id: Home main featured item's id
        """
        self._id = _id

    def get_image(self) -> str:
        """
        :return: Home main featured item's image
        """
        return self.image

    def set_image(self, image: str) -> None:
        """
        :param image: Home main featured item's image
        """
        self.image = image
