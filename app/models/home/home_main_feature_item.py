"""Summary: Home Main feature Item Model

A home main feature item model used to convert a home main feature item document into a home main feature item object
"""


class HomeMainFeatureItem:
    """
    A class to represent a home main feature item model


    Attributes
    ----------
    _id : str
        Home main feature item's id
    image : str
        Home main feature item's image
    """

    def __init__(self, home_main_feature_item_document: dict) -> None:
        self._id = home_main_feature_item_document['_id']
        self.image = home_main_feature_item_document['image']
        self.file_path = home_main_feature_item_document['file_path']

    def create_dict(self) -> dict:
        """
        :return: Home main feature item's dict (without _id)
        """
        return {
            'image': self.image,
            'file_path': self.file_path
        }
