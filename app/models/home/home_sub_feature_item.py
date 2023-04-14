"""Summary: Home Sub Feature Item Model

A home sub feature item model used to convert a home sub feature item document into a home sub feature item object
"""


class HomeSubFeatureItem:
    """
    A class to represent a home sub feature item model


    Attributes
    ----------
    categories : List[Category]
        Home sub feature item's categories
    description : str
        Home sub feature item's description
    file_path : str
        Home sub feature item's file_path
    flags : List[str]
        Home sub feature item's flags
    _id : str
        Home sub feature item's id
    image : str
        Home sub feature item's image
    location: str
        Home sub feature item's location
    rating : int
        Home sub feature item's rating
    reviews : List[Review]
        Home sub feature item's reviews
    service_id : int
        home sub feature item's id
    title : str
        Home sub feature item's title
    """

    def __init__(self, home_sub_feature_item_document: dict) -> None:
        self.file_path = home_sub_feature_item_document['file_path']
        self.categories = home_sub_feature_item_document['categories']
        self.description = home_sub_feature_item_document['description']
        self.flags = home_sub_feature_item_document['flags']
        self._id = home_sub_feature_item_document['_id']
        self.image = home_sub_feature_item_document['image']
        self.location = home_sub_feature_item_document['location']
        self.rating = home_sub_feature_item_document['rating']
        self.reviews = home_sub_feature_item_document['reviews']
        self.service_id = home_sub_feature_item_document['service_id']
        self.title = home_sub_feature_item_document['title']

    def create_dict(self) -> dict:
        """
        :return: Home sub feature item's dict (without _id)
        """
        return {
            'categories': self.categories,
            'description': self.description,
            'flags': self.flags,
            'image': self.image,
            'location': self.location,
            'rating': self.rating,
            'reviews': self.reviews,
            'service_id': self.service_id,
            'title': self.title
        }
