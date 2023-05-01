"""Summary: Home Main Feature Metadata Model

A home main feature metadata model used to convert a home main feature metadata document into a home main feature
metadata object
"""


class HomeMainFeatureMetadata:
    """
    A class to represent a home main feature metadata model


    Attributes
    ----------
    image_format : str
        Home main feature's image format
    image_height : int
        Home main feature's image height
    image_width : int
        Home main feature's image width
    """

    def __init__(self, home_main_feature_metadata_document: dict) -> None:
        self.image_format = str(home_main_feature_metadata_document['image_format'])
        self.image_height = int(home_main_feature_metadata_document['image_height'])
        self.image_width = int(home_main_feature_metadata_document['image_width'])
