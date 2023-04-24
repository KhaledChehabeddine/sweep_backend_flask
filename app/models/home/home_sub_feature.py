"""Summary: Home Sub Feature Model

A home sub feature model used to convert a home sub feature document into a home sub feature object
"""


class HomeSubFeature:
    """
    A class to represent a home sub feature model


    Attributes
    ----------
    _id : str
        Home sub feature's id
    service_firm_ids : List[str]
        Home sub feature's service firm ids
    service_worker_ids : List[str]
        Home sub feature's service worker ids
    subtitle : str
        Home sub feature's subtitle
    title : str
        Home sub feature's title
    """

    def __init__(self, home_sub_feature_document: dict) -> None:
        self._id = home_sub_feature_document['_id']
        self.service_firm_ids = home_sub_feature_document['service_firm_ids']
        self.service_worker_ids = home_sub_feature_document['service_worker_ids']
        self.subtitle = home_sub_feature_document['subtitle']
        self.title = home_sub_feature_document['title']

    def database_dict(self) -> dict:
        """
        :return: Home sub feature's dictionary for creating a document (without _id)
        """
        return {
            'service_firm_ids': self.service_firm_ids,
            'service_worker_ids': self.service_worker_ids,
            'subtitle': self.subtitle,
            'title': self.title
        }
