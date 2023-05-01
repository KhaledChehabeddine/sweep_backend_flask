"""Summary: Home Main Feature Reward Model

A home main feature reward model used to convert a home main feature reward document into a home main feature reward
object
"""
from app.models.home.home_main_feature import HomeMainFeature
from app.models.home.metadata.home_main_feature_reward_metadata import HomeMainFeatureRewardMetadata


class HomeMainFeatureReward:
    """
    A class to represent a home main feature reward model


    Attributes
    ----------
    amount : float
        Home main feature reward's amount
    claimed_customer_ids : list[str]
        Home main feature reward's claimed customer ids
    code : str
        Home main feature reward's code
    _id : str
        Home main feature reward's id
    home_main_feature : dict
        Home main feature reward's home main feature document
    metadata : dict
        Home main feature reward's metadata document
    """

    def __init__(self, home_main_feature_reward_document: dict) -> None:
        self.amount = float(home_main_feature_reward_document['amount'])
        self.claimed_customer_ids = [
            str(claimed_customer_id)
            for claimed_customer_id in home_main_feature_reward_document['claimed_customer_ids']
        ]
        self.code = str(home_main_feature_reward_document['code'])
        self._id = str(home_main_feature_reward_document['_id'])
        self.home_main_feature = HomeMainFeature(
            home_main_feature_document=home_main_feature_reward_document['home_main_feature']
        ).__dict__
        self.metadata = HomeMainFeatureRewardMetadata(
            home_main_feature_reward_metadata_document=home_main_feature_reward_document['metadata']
        ).__dict__

    def database_dict(self) -> dict:
        """
        :return: Home main feature reward's dictionary for creating a document (without _id)
        """
        return {
            'amount': self.amount,
            'claimed_customer_ids': self.claimed_customer_ids,
            'code': self.code,
            'home_main_feature': self.home_main_feature,
            'metadata': self.metadata,
        }
