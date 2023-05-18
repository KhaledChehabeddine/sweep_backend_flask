"""Summary: Review Model

A review model used to convert a review document into a review object
"""
from bson import ObjectId


class Review:
    """
    A class to represent a review model


    Attributes
    ----------
    customer_id : str
        Review's customer id
    feedback : str
        Review's feedback
    _id : str
        Review's id
    metadata : dict
        Review's metadata document
    rating : int
        Review's rating
    """

    def __init__(self, review_document: dict) -> None:
        self.customer_id = str(review_document['customer_id'])
        self.feedback = str(review_document['feedback'])
        self._id = ObjectId(review_document['_id']) if ObjectId.is_valid(review_document['_id']) else ObjectId()
        self.metadata = review_document.get('metadata') or {}
        self.rating = int(review_document['rating'])
