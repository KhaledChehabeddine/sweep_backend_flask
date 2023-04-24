"""Summary: Home Main feature Promotion Model

A home main feature promotion model used to convert a home main feature promotion document into a home main feature
promotion object
"""


class HomeMainFeaturePromotion:
    """
    A class to represent a home main feature promotion model


    Attributes
    ----------
    file_path : str
        Home main feature promotion's file path
    _id : str
        Home main feature promotion's id
    image_url : str
        Home main feature promotion's image url
    service_firm_ids : List[str]
        Home main feature promotion's service firm ids
    service_worker_ids : List[str]
        Home main feature promotion's service worker ids
    """

    def __init__(self, home_main_feature_promotion_document: dict) -> None:
        self.file_path = home_main_feature_promotion_document['file_path']
        self._id = home_main_feature_promotion_document['_id']
        self.image_url = ''
        self.service_firm_ids = home_main_feature_promotion_document['service_firm_ids']
        self.service_worker_ids = home_main_feature_promotion_document['service_worker_ids']

    def database_dict(self) -> dict:
        """
        :return: Home main feature promotion's dictionary for creating a document (without _id and image_url)
        """
        return {
            'file_path': self.file_path,
            'service_firm_ids': self.service_firm_ids,
            'service_worker_ids': self.service_worker_ids,
        }
