"""Summary: Reservation Model

A reservation model used to convert a reservation document into a reservation object.
"""
from app.aws.aws_cloudfront_client import create_cloudfront_url
from app.models.history.metadata.reservation_metadata import ReservationMetadata


class Reservation:
    """
    A class to represent a reservation model

    Attributes:
    ----------
    customer_id : str
        Reservation's customer id
    datetime : datetime
        Reservation's datetime
    description : str
        Reservation's description
    _id : str
        Reservation's id
    image_path : str
        Reservation's image path
    image_url : str
        Reservation's image url
    metadata : dict
        Reservation's metadata document
    price : str
        Reservation's price
    service_provider_id : str
        Reservation's service provider id
    service_provider_type: str
        Reservation's service provider type
    subtitle : str
        Reservation's subtitle
    title : str
        Reservation's title
    """

    def __init__(self, reservation_document: dict) -> None:
        self.customer_id = str(reservation_document['customer_id'])
        self.datetime = reservation_document['datetime']
        self.description = reservation_document['description']
        self._id = str(reservation_document['_id'])
        self.image_path = reservation_document['image_path']
        self.image_url = create_cloudfront_url(reservation_document['image_path'])
        self.metadata = ReservationMetadata(reservation_document['metadata']).__dict__
        self.price = reservation_document['price']
        self.service_provider_id = str(reservation_document['service_provider_id'])
        self.service_provider_type = str(reservation_document['service_provider_type'])
        self.subtitle = reservation_document['subtitle']
        self.title = reservation_document['title']

    def database_dict(self) -> dict:
        """
        :return: A dictionary representation of the reservation object (without _id)
        """
        return {
            'customer_id': self.customer_id,
            'datetime': self.datetime,
            'description': self.description,
            'image_path': self.image_path,
            'image_url': self.image_url,
            'metadata': self.metadata,
            'price': self.price,
            'service_provider_id': self.service_provider_id,
            'service_provider_type': self.service_provider_type,
            'subtitle': self.subtitle,
            'title': self.title
        }
