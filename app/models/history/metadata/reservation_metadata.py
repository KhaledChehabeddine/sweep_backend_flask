"""Summary: Reservation Metadata Model

A reservation metadata model used to convert a reservation metadata document into a reservation metadata object
"""


class ReservationMetadata:
    """
    A class to represent a reservation metadata model

    Attributes
    ----------
    created_date : datetime
        Reservation's created date
    image_format : str
        Image's format
    image_height : int
        Image's height
    image_width : int
        Image's width
    """

    def __init__(self, reservation_metadata_document) -> None:
        self.created_date = reservation_metadata_document['created_date']
        self.image_format = str(reservation_metadata_document['image_format'])
        self.image_height = int(reservation_metadata_document['image_height'])
        self.image_width = int(reservation_metadata_document['image_width'])
