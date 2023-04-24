"""Summary: Home Main feature Reward Model

A home main feature reward model used to convert a home main feature reward document into a home main feature reward
object
"""


class HomeMainFeatureReward:
    """
    A class to represent a home main feature reward model


    Attributes
    ----------
    amount : float
        Home main feature reward's amount
    code : str
        Home main feature reward's code
    file_path : str
        Home main feature reward's file path
    _id : str
        Home main feature reward's id
    image_url : str
        Home main feature reward's image url
    """

    def __init__(self, home_main_feature_reward_document: dict) -> None:
        self.amount = home_main_feature_reward_document['amount']
        self.code = home_main_feature_reward_document['code']
        self.file_path = home_main_feature_reward_document['file_path']
        self._id = home_main_feature_reward_document['_id']
        self.image_url = ''

    def database_dict(self) -> dict:
        """
        :return: Home main feature reward's dictionary for creating a document (without _id and image_url)
        """
        return {
            'amount': self.amount,
            'code': self.code,
            'file_path': self.file_path,
        }
