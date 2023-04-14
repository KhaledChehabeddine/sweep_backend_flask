"""Summary: Review Model

A review model used to convert a review document into a review object
"""


class Review:
    """
    A class to represent a review model


    Attributes
    ----------
    feedback : str
        Review's feedback
    _id : str
        Review's id
    rating : int
        Review's rating
    reviewer : str
        Review's reviewer
    service_item_id : str
        Review's service item's id
    """

    def __init__(self, review_document: dict) -> None:
        self.feedback = review_document['feedback']
        self._id = review_document['_id']
        self.rating = review_document['rating']
        self.reviewer = review_document['reviewer']
        self.service_item_id = review_document['service_item_id']

    def create_dict(self) -> dict:
        """
        :return: Review's dictionary representation
        """
        return {
            'feedback': self.feedback,
            'rating': self.rating,
            'reviewer': self.reviewer,
            'service_item_id': self.service_item_id
        }
