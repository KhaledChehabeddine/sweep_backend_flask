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

    Methods
    -------
    get_feedback() : str
        Returns the review's feedback
    set_feedback(feedback) : None
        Sets the review's feedback
    get_id() : str
        Returns the review's id
    set_id(_id) : None
        Sets the review's id
    get_rating() : int
        Returns the review's rating
    set_rating(rating) : None
        Sets the review's rating
    get_reviewer() : str
        Returns the review's reviewer
    set_reviewer(reviewer) : None
        Sets the review's reviewer
    get_service_item_id() : str
        Returns the review's service id
    set_service_item_id(service_item_id) : None
        Sets the review's service item's id
    """

    def __init__(self, review_document: dict) -> None:
        self.feedback = review_document['feedback']
        self._id = review_document['_id']
        self.rating = review_document['rating']
        self.reviewer = review_document['reviewer']
        self.service_item_id = review_document['service_item_id']

    def get_feedback(self) -> str:
        """
        :return: Review's feedback
        """
        return self.feedback

    def set_feedback(self, feedback: str) -> None:
        """
        :param feedback: Review's feedback
        """
        self.feedback = feedback

    def get_id(self) -> str:
        """
        :return: Review's id
        """
        return self._id

    def set_id(self, _id: str) -> None:
        """
        :param _id: Review's id
        """
        self._id = _id

    def get_rating(self) -> int:
        """
        :return: Review's rating
        """
        return self.rating

    def set_rating(self, rating: int) -> None:
        """
        :param rating: Review's rating
        """
        self.rating = rating

    def get_reviewer(self) -> str:
        """
        :return: Review's reviewer
        """
        return self.reviewer

    def set_reviewer(self, reviewer: str) -> None:
        """
        :param reviewer: Review's reviewer
        """
        self.reviewer = reviewer

    def get_service_item_id(self) -> str:
        """
        :return: Review's service id
        """
        return self.service_item_id

    def set_service_item_id(self, service_item_id: str) -> None:
        """
        :param service_item_id: Review's service id
        """
        self.service_item_id = service_item_id
