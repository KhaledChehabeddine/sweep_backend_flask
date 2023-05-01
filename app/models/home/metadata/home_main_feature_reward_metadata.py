"""Summary: Home Main Feature Reward Metadata Model

A home main feature reward metadata model used to convert a home main feature reward metadata document into a home main
feature reward metadata object
"""


class HomeMainFeatureRewardMetadata:
    """
    A class to represent a home main feature reward metadata model


    Attributes
    ----------
    total_amount_claimed : float
        Home main feature reward's total amount claimed (amount * total claimed customers)
    total_claimed_customers : int
        Home main feature reward's total claimed customers
    """

    def __init__(self, home_main_feature_reward_metadata_document: dict) -> None:
        self.total_amount_claimed = float(home_main_feature_reward_metadata_document['total_amount_claimed'])
        self.total_claimed_customers = int(home_main_feature_reward_metadata_document['total_claimed_customers'])
