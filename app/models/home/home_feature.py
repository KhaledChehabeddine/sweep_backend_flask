"""Summary: Home Feature Model

A home feature model used to convert a home feature document into a home feature object
"""
from app.models.home.metadata.home_feature_metadata import HomeFeatureMetadata


class HomeFeature:
    """
    A class to represent a home feature model


    Attributes
    ----------
    active : bool
        Home feature's active status
    home_feature_type : str
        Home feature's type (main or sub)
    metadata : dict
        Home feature's metadata document
    priority: int
        Home feature's display order priority
    """

    def __init__(self, home_feature_document: dict) -> None:
        self.active = home_feature_document['active']
        self.clicks = home_feature_document['clicks']
        self.home_feature_type = home_feature_document['home_feature_type']
        self.metadata = HomeFeatureMetadata(home_feature_metadata_document=home_feature_document['metadata']).__dict__
        self.priority = home_feature_document['priority']
