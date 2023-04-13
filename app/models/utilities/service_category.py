"""Summary: Service Category Model

    A service category model used to convert a service category document into a service category object
"""


class ServiceCategory:
    """
    A class to represent a service category model

    Attributes
    ----------
    _id : str
        Service Category's id
    name : str
        Service Category's name
    icon : str
        Service Category's icon
    active : bool
        Service Category's active status

    Methods
    -------
    get_id() : str
        Returns the service category's id
    set_id(_id) : None
        Sets the service category's id
    get_name() : str
        Returns the service category's name
    set_name(name) : None
        Sets the service category's name
    get_icon() : str
        Returns the service category's icon
    set_icon(icon) : None
        Sets the service category's icon
    get_active() : bool
        Returns the service category's active status
    set_active(active) : None
        Sets the service category's active status
    """

    def __init__(self, service_category_document: dict) -> None:
        self._id = service_category_document['_id']
        self.name = service_category_document['name']
        self.icon = service_category_document['icon']
        self.active = service_category_document['active']

    def get_id(self) -> str:
        """
        :return: Service Category's id
        """
        return self._id

    def set_id(self, _id: str) -> None:
        """
        :param _id: Service Category's id
        """
        self._id = _id

    def get_name(self) -> str:
        """
        :return: Service Category's name
        """
        return self.name

    def set_name(self, name: str) -> None:
        """
        :param name: Service Category's name
        """
        self.name = name

    def get_icon(self) -> str:
        """
        :return: Service Category's icon
        """
        return self.icon

    def set_icon(self, icon: str) -> None:
        """
        :param icon: Service Category's icon
        """
        self.icon = icon

    def get_active(self) -> bool:
        """
        :return: Service Category's active status
        """
        return self.active

    def set_active(self, active: bool) -> None:
        """
        :param active: Service Category's active status
        """
        self.active = active
