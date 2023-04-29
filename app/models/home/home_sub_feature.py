"""Summary: Home Sub Feature Model

A home sub feature model used to convert a home sub feature document into a home sub feature object
"""
from app.models.home.home_feature import HomeFeature
from app.models.home.metadata.home_sub_feature_metadata import HomeSubFeatureMetadata


class HomeSubFeature:
    """
    A class to represent a home sub feature model


    Attributes
    ----------
    company_ids : list[str]
        Home sub feature's company ids
    home_feature : dict
        Home sub feature's home feature document
    _id : str
        Home sub feature's id
    metadata : dict
        Home sub feature's metadata document
    subtitle : str
        Home sub feature's subtitle
    title : str
        Home sub feature's title
    worker_ids : list[str]
        Home sub feature's worker ids
    """

    def __init__(self, home_sub_feature_document: dict) -> None:
        self.company_ids = home_sub_feature_document['company_ids']
        self.home_feature = HomeFeature(home_feature_document=home_sub_feature_document['home_feature']).__dict__
        self._id = home_sub_feature_document['_id']
        self.metadata = HomeSubFeatureMetadata(
            home_sub_feature_metadata_document=home_sub_feature_document['metadata']
        ).__dict__
        self.subtitle = home_sub_feature_document['subtitle']
        self.title = home_sub_feature_document['title']
        self.worker_ids = home_sub_feature_document['worker_ids']

    def database_dict(self) -> dict:
        """
        :return: Home sub feature's dictionary for creating a document (without _id)
        """
        return {
            'company_ids': self.company_ids,
            'home_feature': self.home_feature,
            'metadata': self.metadata,
            'subtitle': self.subtitle,
            'title': self.title,
            'worker_ids': self.worker_ids,
        }
