"""Summary: User Metadata Model

A user metadata model used to convert a user metadata document into a user metadata object
"""


class UserMetadata:
    """
    A class to represent a user metadata model


    Attributes
    ----------
    created_date : datetime
        User's created date
    last_login_date : datetime
        User's last login date
    updated_date : datetime
        User's updated date
    """

    def __init__(self, user_metadata_document: dict) -> None:
        self.created_date = user_metadata_document['created_date']
        self.last_login_date = user_metadata_document['last_login_date']
        self.updated_date = user_metadata_document['updated_date']
