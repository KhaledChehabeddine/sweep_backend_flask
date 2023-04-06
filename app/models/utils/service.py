"""Summary: service Document
    A service model used to convert a service document into a service object
"""


class Service:
    """
    class to represent the service model


    Attributes
    ----------
    image_link : str
        service's image_link
    name : str
        service's name
    description : str
        service's description
    price : int
        service's price
    service_id : int
        service's id

    Methods
    -------
    get_image_link() : str
        returns the service's image_link
    set_image_link(image_link) : None
        sets the service's image_link
    get_name() : str
        returns the service's name
    set_name(name) : None
        sets the service's name
    get_description() : str
        returns the service's description
    set_description(description) : None
        sets the service's description
    get_price() : int
        returns the service's price
    set_price(price) : None
        sets the service's price
    get_service_id() : int
        returns the service's id
    set_service_id(service_id) : None
        sets the service's price
    """

    def __init__(self, service_document: dict) -> None:
        self.image_link = service_document['image']
        self.name = service_document['name']
        self.description = service_document['description']
        self.price = service_document['price']
        self.service_id = service_document['service_id']

    def get_image_link(self) -> str:
        """
        returns the image_link of the service item
        """
        return self.image_link

    def set_image_link(self, image_link: str) -> None:
        """
        sets the image_link of the service item
        """
        self.image_link = image_link

    def get_name(self) -> str:
        """
        returns the name of the service item
        """
        return self.name

    def set_name(self, name: str) -> None:
        """
        sets the name of the service item
        """
        self.name = name

    def get_description(self) -> str:
        """
        returns the description of the service item
        """
        return self.description

    def set_description(self, description: str) -> None:
        """
        sets the description of the service item
        """
        self.description = description

    def get_price(self) -> int:
        """
        returns the price of the service item
        """
        return self.price

    def set_price(self, price: int) -> None:
        """
        sets the price of the service item
        """
        self.price = price

    def get_service_id(self) -> int:
        """
        gets the service's id
        """
        return self.service_id

    def set_service_id(self, service_id: int) -> None:
        """
        sets the service's id
        """
        self.service_id = service_id
