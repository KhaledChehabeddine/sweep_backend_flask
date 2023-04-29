"""Summary: Review Model

A review model used to convert a review document into a review object
"""
from bson import ObjectId
from app.models.components.metadata.review_metadata import ReviewMetadata


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
        self.customer_id = review_document['customer_id']
        self.feedback = review_document['feedback']
        self._id = ObjectId(review_document['_id']) if ObjectId.is_valid(review_document['_id']) else ObjectId()
        self.metadata = ReviewMetadata(review_document['metadata']).__dict__
        self.rating = review_document['rating']
