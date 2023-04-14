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
    _id : str
        Service's id
    image : str
        Service's image
    name : str
        Service's name
    price : float
        Service's price
    """

    def __init__(self, service_item_document: dict) -> None:
        self.description = service_item_document['description']
        self._id = service_item_document['_id']
        self.image = service_item_document['image']
        self.name = service_item_document['name']
        self.price = service_item_document['price']

    def create_dict(self) -> dict:
        """
        :return: Service's dictionary representation
        """
        return {
            'description': self.description,
            'image': self.image,
            'name': self.name,
            'price': self.price
        }
