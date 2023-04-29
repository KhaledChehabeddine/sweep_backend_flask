"""Summary: Home Main Feature Model

A home main feature model used to convert a home main feature document into a home main feature object
"""
from app.models.home.home_feature import HomeFeature
from app.models.home.metadata.home_main_feature_metadata import HomeMainFeatureMetadata


class HomeMainFeature:
    """
    A class to represent a home main feature model


    Attributes
    ----------
    home_feature : dict
        Home main feature's home feature document
    home_main_feature_type : str
        Home main feature's type (promotion or reward)
    image_path : str
        Home main feature's image path
    image_url : str
        Home main feature's image url
    metadata : dict
        Home main feature's metadata document
    """

    def __init__(self, home_main_feature_document: dict) -> None:
        self.home_feature = HomeFeature(home_main_feature_document['home_feature'])
        self.home_main_feature_type = home_main_feature_document['home_main_feature_type']
        self.image_path = home_main_feature_document['image_path']
        self.image_url = ''
        self.metadata = HomeMainFeatureMetadata(
            home_main_feature_metadata_document=home_main_feature_document['metadata']
        ).__dict__
