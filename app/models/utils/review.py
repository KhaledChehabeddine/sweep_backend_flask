"""Summary: Review model
    a review model used to convert a review document into a review object
"""
from typing import List

from app.models.utils.service import Service


class Review:
    """
    A class to represent a review model


    Attributes
    ----------
    feedback : str
        Review's feedback
    rating : int
        Review's rating
    reviewer : str
        Review's reviewer
    review_id : str
        Review's id
    services : List[Service]
        review's services

    Methods
    -------
    get_feedback() : str
        Returns the review's feedback
    set_feedback(feedback) : None
        Sets the review's feedback
    get_rating() : int
        Returns the review's rating
    set_rating(rating) : None
        Sets the review's rating
    get_reviewer() : str
        Returns the review's reviewer
    set_reviewer(reviewer) : None
        Sets the review's reviewer
    get_review_id() : str
        Returns the review's id
    set_review_id(review_id) : None
        Sets the review's id
    get_services() : List[services]
        Returns the review's services
    set_services(services) : None
        Sets the review's services
    """

    def __init__(self, reviews_document: dict) -> None:
        self.feedback = reviews_document['feedback']
        self.rating = reviews_document['rating']
        self.reviewer = reviews_document['reviewer']
        self.review_id = reviews_document['review_id']
        self.services = reviews_document['services']

    def get_feedback(self) -> str:
        """
        returns the feedback
        """
        return self.feedback

    def set_feedback(self, feedback: str) -> None:
        """
        sets the feedback
        """
        self.feedback = feedback

    def get_rating(self) -> int:
        """
        returns the rating
        """
        return self.rating

    def set_rating(self, rating: int) -> None:
        """
        sets the rating
        """
        self.rating = rating

    def get_reviewer(self) -> str:
        """
        returns the reviewer
        """
        return self.reviewer

    def set_reviewer(self, reviewer: str) -> None:
        """
        sets the reviewer
        """
        self.reviewer = reviewer

    def get_review_id(self) -> str:
        """
        returns the id
        """
        return self.review_id

    def set_review_id(self, review_id: str) -> None:
        """
        sets the id
        """
        self.review_id = review_id

    def get_services(self) -> List[Service]:
        """
        returns the service
        """
        return self.services

    def set_services(self, services: List[Service]) -> None:
        """
        set the service
        """
        self.services = services
