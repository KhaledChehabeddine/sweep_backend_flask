"""Summary: Home Feature Item Model

A home feature item model used to convert a home feature item document into a home feature item object
"""


class HomeFeatureItem:
    """
    A class to represent a home feature item model


    Attributes
    ----------
    category_ids : List[str]
        Home feature item's categories
    description : str
        Home feature item's description
    file_path : str
        Home feature item's file_path
    flags : List[str]
        Home feature item's flags
    _id : str
        Home feature item's id
    image_url : str
        Home feature item's image url
    location: str
        Home feature item's location
    rating : float
        Home feature item's rating (average of all reviews)
    review_ids : List[str]
        Home feature item's reviews
    service_id : int
        Home feature item's service id
    title : str
        Home feature item's title
    """

    def __init__(self, home_feature_item_document: dict) -> None:
        self.category_ids = home_feature_item_document['category_ids']
        self.description = home_feature_item_document['description']
        self.file_path = home_feature_item_document['file_path']
        self.flags = home_feature_item_document['flags']
        self._id = home_feature_item_document['_id']
        self.image_url = ''
        self.location = home_feature_item_document['location']
        self.rating = home_feature_item_document['rating']
        self.review_ids = home_feature_item_document['review_ids']
        self.service_id = home_feature_item_document['service_id']
        self.title = home_feature_item_document['title']

    def database_dict(self) -> dict:
        """
        :return: Home feature item's dictionary for creating a document (without _id and image_url)
        """
        return {
            'category_ids': self.category_ids,
            'description': self.description,
            'file_path': self.file_path,
            'flags': self.flags,
            'location': self.location,
            'rating': self.rating,
            'review_ids': self.review_ids,
            'service_id': self.service_id,
            'title': self.title
        }
