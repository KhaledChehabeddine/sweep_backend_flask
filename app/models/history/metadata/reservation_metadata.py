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
        Reservation's image format
    image_height : int
        Reservation's image height
    image_width : int
        Reservation's image width
    """

    def __init__(self, reservation_metadata_document) -> None:
        self.created_date = reservation_metadata_document['created_date']
        self.image_format = reservation_metadata_document['image_format']
        self.image_height = reservation_metadata_document['image_height']
        self.image_width = reservation_metadata_document['image_width']
