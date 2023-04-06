"""Summary: Service Model

A service model used to convert a service document into a service object
"""


class Service:
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

    Methods
    -------
    get_description() : str
        Returns the service's description
    set_description(description) : None
        Sets the service's description
    get_id() : str
        Returns the service's id
    set_id(_id) : None
        Sets the service's id
    get_image() : str
        Returns the service's image
    set_image(image) : None
        Sets the service's image
    get_name() : str
        Returns the service's name
    set_name(name) : None
        Sets the service's name
    get_price() : float
        Returns the service's price
    set_price(price) : None
        Sets the service's price
    """

    def __init__(self, service_document: dict) -> None:
        self.description = service_document['description']
        self._id = service_document['_id']
        self.image = service_document['image']
        self.name = service_document['name']
        self.price = service_document['price']

    def get_description(self) -> str:
        """
        :return: Service's description
        """
        return self.description

    def set_description(self, description: str) -> None:
        """
        :param description: Service's description
        """
        self.description = description

    def get_id(self) -> str:
        """
        :return: Service's id
        """
        return self._id

    def set_id(self, _id: str) -> None:
        """
        :param _id: Service's id
        """
        self._id = _id

    def get_image(self) -> str:
        """
        :return: Service's image
        """
        return self.image

    def set_image(self, image: str) -> None:
        """
        :param image: Service's image
        """
        self.image = image

    def get_name(self) -> str:
        """
        :return: Service's name
        """
        return self.name

    def set_name(self, name: str) -> None:
        """
        :param name: Service's name
        """
        self.name = name

    def get_price(self) -> float:
        """
        :return: Service's price
        """
        return self.price

    def set_price(self, price: float) -> None:
        """
        :param price: Service's price
        """
        self.price = price
