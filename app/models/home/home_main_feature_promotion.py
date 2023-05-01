"""Summary: Home Main Feature Promotion Model

A home main feature promotion model used to convert a home main feature promotion document into a home main feature
promotion object
"""
from app.models.home.home_main_feature import HomeMainFeature
from app.models.home.metadata.home_main_feature_promotion_metadata import HomeMainFeaturePromotionMetadata


class HomeMainFeaturePromotion:
    """
    A class to represent a home main feature promotion model


    Attributes
    ----------
    company_ids : list[str]
        Home main feature promotion's company ids
    _id : str
        Home main feature promotion's id
    home_main_feature : dict
        Home main feature promotion's home main feature document
    metadata: dict
        Home main feature promotion's metadata document
    worker_ids : list[str]
        Home main feature promotion's worker ids
    """

    def __init__(self, home_main_feature_promotion_document: dict) -> None:
        self.company_ids = [str(company_id) for company_id in home_main_feature_promotion_document['company_ids']]
        self._id = str(home_main_feature_promotion_document['_id'])
        self.home_main_feature = HomeMainFeature(
            home_main_feature_document=home_main_feature_promotion_document['home_main_feature']
        ).__dict__
        self.metadata = HomeMainFeaturePromotionMetadata(
            home_main_feature_promotion_metadata_document=home_main_feature_promotion_document['metadata']
        ).__dict__
        self.worker_ids = [str(worker_id) for worker_id in home_main_feature_promotion_document['worker_ids']]

    def database_dict(self) -> dict:
        """
        :return: Home main feature promotion's dictionary for creating a document (without _id)
        """
        return {
            'company_ids': self.company_ids,
            'home_main_feature': self.home_main_feature,
            'metadata': self.metadata,
            'worker_ids': self.worker_ids,
        }
