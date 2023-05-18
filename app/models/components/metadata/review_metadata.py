"""Summary: Review Metadata Model

A review metadata model used to convert an review metadata document into an review metadata object
"""


class ReviewMetadata:
    """
    A class to represent a review metadata model

    Attributes
    ----------
    created_date : datetime
        Review's created date
    """

    def __init__(self, review_metadata_document) -> None:
        self.created_date = review_metadata_document.get('created_date')
