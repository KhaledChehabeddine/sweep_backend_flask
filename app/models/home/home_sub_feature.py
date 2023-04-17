"""Summary: Home Sub Feature Model

A home sub feature model used to convert a home sub feature document into a home sub feature object
"""


class HomeSubFeature:
    """
    A class to represent a home sub feature model


    Attributes
    ----------
    home_sub_feature_items : List[HomeSubFeatureItem]
        Home sub feature's items
    _id : str
        Home sub feature's id
    subtitle : str
        Home sub feature's subtitle
    title : str
        Home sub feature's title
    """

    def __init__(self, home_sub_feature_document: dict) -> None:
        self.home_sub_feature_items = home_sub_feature_document['home_sub_feature_items']
        self._id = home_sub_feature_document['_id']
        self.subtitle = home_sub_feature_document['subtitle']
        self.title = home_sub_feature_document['title']

    def database_dict(self) -> dict:
        """
        :return: Home sub feature's dictionary for creating a document (without _id)
        """
        return {
            'home_sub_feature_items': self.home_sub_feature_items,
            'subtitle': self.subtitle,
            'title': self.title
        }
