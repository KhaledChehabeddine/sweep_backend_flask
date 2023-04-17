"""Summary: Home Main feature Item Model

A home main feature item model used to convert a home main feature item document into a home main feature item object
"""


class HomeMainFeatureItem:
    """
    A class to represent a home main feature item model


    Attributes
    ----------
    file_path : str
        Home main feature item's file path
    _id : str
        Home main feature item's id
    image_url : str
        Home main feature item's image url
    promotion_home_feature_item_ids : List[str]
        Home main feature item's promotion home feature item ids
    reward_amount : float
        Home main feature item's reward amount
    reward_code : str
        Home main feature item's reward code
    type : str
        Home main feature item's type (promotion or reward)
    """

    def __init__(self, home_main_feature_item_document: dict) -> None:
        self.file_path = home_main_feature_item_document['file_path']
        self._id = home_main_feature_item_document['_id']
        self.image_url = ''
        self.promotion_home_feature_item_ids = home_main_feature_item_document['promotion_home_feature_item_ids']
        self.reward_amount = home_main_feature_item_document['reward_amount']
        self.reward_code = home_main_feature_item_document['reward_code']
        self.type = home_main_feature_item_document['type']

    def database_dict(self) -> dict:
        """
        :return: Home main feature item's dictionary for creating a document (without _id and image_url)
        """
        return {
            'file_path': self.file_path,
            'promotion_home_feature_item_ids': self.promotion_home_feature_item_ids,
            'reward_amount': self.reward_amount,
            'reward_code': self.reward_code,
            'type': self.type,
        }
