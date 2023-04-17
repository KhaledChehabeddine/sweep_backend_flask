"""Summary: Service Model

A service model used to convert a service item document into a service object
"""


class ServiceItem:
    """
    A class to represent a service model


    Attributes
    ----------
    description : str
        Service's description
    file_path : str
        Service's file path
    _id : str
        Service's id
    image_url : str
        Service's image
    name : str
        Service's name
    price : float
        Service's price
    """

    def __init__(self, service_item_document: dict) -> None:
        self.description = service_item_document['description']
        self.file_path = service_item_document['file_path']
        self._id = service_item_document['_id']
        self.image_url = ''
        self.name = service_item_document['name']
        self.price = service_item_document['price']

    def database_dict(self) -> dict:
        """
        :return: A dictionary representation of the service object (without _id and image_url)
        """
        return {
            'description': self.description,
            'file_path': self.file_path,
            'name': self.name,
            'price': self.price
        }
